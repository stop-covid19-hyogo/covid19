<template>
  <data-view :title="title" :title-id="titleId" :date="date">
    <template v-slot:description>
      {{ desc }}
    </template>
    <scatter
      :style="{ display: canvas ? 'block' : 'none' }"
      :chart-id="chartId"
      :chart-data="displayData"
      :options="displayOption"
      :height="240"
    />
    <v-data-table
      :style="{ top: '-9999px', position: canvas ? 'fixed' : 'static' }"
      :headers="tableHeaders"
      :items="tableData"
      :items-per-page="-1"
      :hide-default-footer="true"
      :height="240"
      :fixed-header="true"
      :disable-sort="true"
      :mobile-breakpoint="0"
      class="cardTable"
      item-key="name"
    />
    <template v-slot:infoPanel>
      <data-view-basic-info-panel
        :l-text="info.lText"
        :s-text="info.sText"
        :unit="info.unit"
      />
    </template>
    <template v-slot:footer>
      <open-data-link v-show="url" :url="url" />
    </template>
  </data-view>
</template>

<script lang="ts">
import Vue from 'vue'
import { ThisTypedComponentOptionsWithRecordProps } from 'vue/types/options'
import {
  GraphDataType,
  ChildGraphDataType
} from '@/utils/formatClustersScatter'
import {
  headers as TableHeader,
  TableDataType
} from '@/utils/formatClustersTable'
import DataView from '@/components/DataView.vue'
import DataViewBasicInfoPanel from '@/components/DataViewBasicInfoPanel.vue'
import OpenDataLink from '@/components/OpenDataLink.vue'

import { getGraphSeriesStyle } from '@/utils/colors'

type Data = {
  dataKind: 'transition'
  canvas: boolean
}
type Methods = {}
type Computed = {
  displayData: {
    labels: string[]
    datasets: {
      fill: boolean
      showLine: boolean
      data: ChildGraphDataType[]
      backgroundColor: string
    }[]
  }
  displayOption: {
    tooltips: {
      displayColors: boolean
      callbacks: {
        label: (tooltipItem: any) => string
        title: (tooltipItem: any, data: any) => string
      }
    }
    responsive: boolean
    maintainAspectRatio: boolean
    legend: {
      display: boolean
    }
    scales: object
  }
  tableHeaders: {
    text: string
    value: string
  }[]
  tableData: {
    [key: number]: number
  }[]
}
type Props = {
  title: string
  titleId: string
  chartId: string
  chartData: GraphDataType
  date: string
  unit: string
  info: object
  desc: string
  url: string
}

const options: ThisTypedComponentOptionsWithRecordProps<
  Vue,
  Data,
  Methods,
  Computed,
  Props
> = {
  created() {
    this.canvas = process.browser
  },
  components: { DataView, DataViewBasicInfoPanel, OpenDataLink },
  props: {
    title: {
      type: String,
      default: ''
    },
    titleId: {
      type: String,
      default: ''
    },
    chartId: {
      type: String,
      default: 'scatter-chart'
    },
    chartData: {
      type: Object,
      default: () => {
        return {
          datasets: [],
          clusters: [],
          labels: []
        }
      }
    },
    date: {
      type: String,
      required: true
    },
    unit: {
      type: String,
      default: ''
    },
    info: {
      type: Object,
      default: () => {}
    },
    desc: {
      type: String,
      required: false,
      default: ''
    },
    url: {
      type: String,
      required: false,
      default: ''
    }
  },
  data: () => ({
    dataKind: 'transition',
    canvas: true
  }),
  computed: {
    displayData() {
      const style = getGraphSeriesStyle(1)[0]
      return {
        labels: this.chartData.labels,
        datasets: [
          {
            fill: false,
            showLine: false,
            data: this.chartData.datasets,
            backgroundColor: style.fillColor,
            borderColor: style.strokeColor,
            borderWidth: 0
          }
        ]
      }
    },
    displayOption() {
      const unit = this.unit
      const data = this.chartData
      const options = {
        tooltips: {
          displayColors: false,
          callbacks: {
            label(tooltipItem: any) {
              return `${data.clusters[data.datasets[tooltipItem.index].y]} で ${
                data.datasets[tooltipItem.index].label
              } ${unit}`
            },
            title(tooltipItem: any) {
              return data.datasets[tooltipItem[0].index].x
            }
          }
        },
        responsive: true,
        maintainAspectRatio: false,
        legend: {
          display: false
        },
        scales: {
          xAxes: [
            {
              id: 'day',
              stacked: true,
              gridLines: {
                display: false
              },
              ticks: {
                fontSize: 9,
                maxTicksLimit: 15,
                fontColor: '#808080',
                maxRotation: 0
              },
              type: 'time',
              time: {
                displayFormats: {
                  day: 'D'
                },
                parser: 'M/D',
                unit: 'day'
              }
            },
            {
              id: 'month',
              stacked: true,
              gridLines: {
                drawOnChartArea: false,
                drawTicks: true,
                drawBorder: false,
                tickMarkLength: 10
              },
              ticks: {
                fontSize: 11,
                fontColor: '#808080',
                padding: 3,
                fontStyle: 'bold',
                gridLines: {
                  display: true
                }
              },
              type: 'time',
              time: {
                unit: 'month',
                parser: 'M/D',
                displayFormats: {
                  month: 'MMM'
                }
              }
            }
          ],
          yAxes: [
            {
              location: 'bottom',
              stacked: true,
              gridLines: {
                display: true,
                color: '#E5E5E5'
              },
              ticks: {
                suggestedMin: 0,
                maxTicksLimit: 12,
                fontColor: '#808080',
                max: data.clusters.length,
                callback: (i: number) => {
                  return data.clusters[i]
                }
              }
            }
          ]
        }
      }
      if (this.$route.query.ogp === 'true') {
        Object.assign(options, { animation: { duration: 0 } })
      }
      return options
    },
    tableHeaders() {
      return TableHeader
    },
    tableData() {
      const clusters = this.chartData.clusters
      const data: TableDataType[] = []
      clusters.forEach(dl => {
        data.push({
          クラスター: dl,
          人数: 0
        })
      })
      this.chartData.datasets.forEach(d => {
        data[clusters.indexOf(clusters[d.y])]['人数'] += d.label
      })
      return data.reverse()
    }
  }
}

export default Vue.extend(options)
</script>

<style module lang="scss">
.Graph {
  &Desc {
    width: 100%;
    margin: 0;
    margin-bottom: 0 !important;
    padding-left: 0 !important;
    font-size: 12px;
    color: $gray-3;
    list-style: none;
  }
  &Link {
    text-decoration: none;
  }
}
</style>
