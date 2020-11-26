<template>
  <data-view :title="title" :title-id="titleId" :date="date">
    <template v-slot:description>
      <slot name="description" />
    </template>
    <h4 :id="`${titleId}-graph`" class="visually-hidden">
      {{ $t(`{title}のグラフ`, { title }) }}
    </h4>
    <scrollable-chart v-show="canvas" :display-data="displayData">
      <template v-slot:chart="{ chartWidth }">
        <scatter
          :ref="'scatterChart'"
          :chart-id="chartId"
          :chart-data="displayData"
          :options="displayOption"
          :height="240"
          :width="chartWidth"
        />
      </template>
      <template v-slot:sticky-chart>
        <scatter
          class="sticky-legend"
          :chart-id="`${chartId}-header`"
          :chart-data="displayDataHeader"
          :options="displayOptionHeader"
          :plugins="yAxesBgPlugin"
          :height="240"
        />
      </template>
    </scrollable-chart>
    <template v-slot:dataTable>
      <data-view-table :headers="tableHeaders" :items="tableData" />
    </template>
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
import { Chart } from 'chart.js'
import {
  GraphDataType,
  ChildGraphDataType
} from '@/utils/formatClustersScatter'
import DataView from '@/components/DataView.vue'
import DataViewBasicInfoPanel from '@/components/DataViewBasicInfoPanel.vue'
import DataViewTable, {
  TableHeader,
  TableItem
} from '@/components/DataViewTable.vue'
import ScrollableChart from '@/components/ScrollableChart.vue'
import OpenDataLink from '@/components/OpenDataLink.vue'
import { DisplayData, yAxesBgPlugin } from '@/plugins/vue-chart'

import { getGraphSeriesStyle } from '@/utils/colors'
import { getComplementedDate } from '@/utils/formatDate'

type Data = {
  dataKind: 'transition'
  canvas: boolean
}
type Methods = {
  numberToColumnNameList: (num: number) => string[]
}
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
  displayOption: Chart.ChartOptions
  displayDataHeader: DisplayData
  displayOptionHeader: Chart.ChartOptions
  tableHeaders: TableHeader[]
  tableData: TableItem[]
}
type Props = {
  title: string
  titleId: string
  chartId: string
  chartData: GraphDataType
  date: string
  unit: string
  info: object
  url: string
  yAxesBgPlugin: Chart.PluginServiceRegistrationOptions[]
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
  components: {
    DataView,
    DataViewBasicInfoPanel,
    DataViewTable,
    ScrollableChart,
    OpenDataLink
  },
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
    url: {
      type: String,
      required: false,
      default: ''
    },
    yAxesBgPlugin: {
      type: Array,
      default: () => yAxesBgPlugin
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
      const self = this
      const unit = this.unit
      const data = this.chartData
      const translatedClusters = this.chartData.clusters.map(cluster => {
        return this.$t(cluster)
      })
      const clustersAlphabet = this.numberToColumnNameList(
        this.chartData.clusters.length
      )
      const options: Chart.ChartOptions = {
        tooltips: {
          displayColors: false,
          callbacks: {
            label(tooltipItem: any) {
              return `${
                clustersAlphabet[data.datasets[tooltipItem.index].y]
              }) ${translatedClusters[data.datasets[tooltipItem.index].y]}: ${
                data.datasets[tooltipItem.index].label
              } ${unit}`
            },
            title(tooltipItem: any) {
              const label = data.datasets[tooltipItem[0].index].x
              return self.$d(
                new Date(getComplementedDate(label)),
                'dateWithoutYear'
              )
            }
          }
        },
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
                fontStyle: 'bold'
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
                  return clustersAlphabet[i]
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
    displayDataHeader() {
      return {
        labels: ['2020/1/1'],
        datasets: [
          {
            data: [this.chartData.clusters.length],
            backgroundColor: 'transparent',
            borderWidth: 0,
            borderColor: 'transparent'
          }
        ]
      }
    },
    displayOptionHeader() {
      const data = this.chartData
      const clustersAlphabet = this.numberToColumnNameList(
        this.chartData.clusters.length
      )
      const options: Chart.ChartOptions = {
        maintainAspectRatio: false,
        legend: {
          display: false
        },
        tooltips: { enabled: false },
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
                fontColor: 'transparent', // #808080
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
                drawTicks: false, // true -> false
                drawBorder: false,
                tickMarkLength: 10
              },
              ticks: {
                fontSize: 11,
                fontColor: 'transparent', // #808080
                padding: 13, // 3 + 10(tickMarkLength)
                fontStyle: 'bold'
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
              stacked: true,
              gridLines: {
                display: true,
                drawOnChartArea: false,
                color: '#E5E5E5' // #E5E5E5
              },
              ticks: {
                suggestedMin: 0,
                maxTicksLimit: 12,
                fontColor: '#808080', // #808080
                max: data.clusters.length,
                callback: (i: number) => {
                  return clustersAlphabet[i]
                }
              }
            }
          ]
        },
        animation: { duration: 0 }
      }
      return options
    },
    tableHeaders() {
      return [
        { text: this.$t('クラスター/感染源'), value: 'text' },
        {
          text: this.$t('人数'),
          value: '0',
          align: 'end'
        }
      ]
    },
    tableData() {
      const clusters = this.chartData.clusters
      const clustersAlphabet = this.numberToColumnNameList(
        this.chartData.clusters.length
      )
      const data: TableItem[] = []
      clusters.forEach((dl, i) => {
        if (dl !== '') {
          data.push({
            text: `${clustersAlphabet[i]}) ${this.$t(dl)}`,
            0: 0
          })
        }
      })
      this.chartData.datasets.forEach(d => {
        data[clusters.indexOf(clusters[d.y - 1])][0] += d.label
      })
      return data.reverse()
    }
  },
  methods: {
    numberToColumnNameList(num: number): string[] {
      const resultList = []
      for (let i = 0; i < num; i++) {
        let j = num - i
        let temp
        let letter = ''
        if (i) {
          while (j > 0) {
            temp = (j - 1) % 26
            letter = String.fromCharCode(temp + 65) + letter
            j = (j - temp - 1) / 26
          }
        }
        resultList.push(letter)
      }
      return resultList
    }
  },
  mounted() {
    const scatterChart = this.$refs.scatterChart as Vue
    const scatterElement = scatterChart.$el
    const canvas = scatterElement.querySelector('canvas')
    const labelledbyId = `${this.titleId}-graph`

    if (canvas) {
      canvas.setAttribute('role', 'img')
      canvas.setAttribute('aria-labelledby', labelledbyId)
    }
  }
}

export default Vue.extend(options)
</script>

<style lang="scss" scoped>
.Graph-Desc {
  margin: 10px 0;
  font-size: 12px;
  color: $gray-3;
}
</style>
