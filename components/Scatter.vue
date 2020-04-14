<template>
  <data-view :title="title" :title-id="titleId" :date="date">
    <template v-slot:description>
      {{ desc }}
    </template>
    <h4 :id="`${titleId}-graph`" class="visually-hidden">
      {{ $t(`{title}のグラフ`, { title }) }}
    </h4>
    <div class="LegendStickyChart">
      <div class="scrollable" :style="{ display: canvas ? 'block' : 'none' }">
        <div :style="{ width: `${chartWidth}px` }">
          <scatter
            :ref="'scatterChart'"
            :chart-id="chartId"
            :chart-data="displayData"
            :options="displayOption"
            :plugins="scrollPlugin"
            :height="240"
            :width="chartWidth"
          />
        </div>
      </div>
      <scatter
        class="sticky-legend"
        :style="{ display: canvas ? 'block' : 'none' }"
        :chart-id="`${chartId}-header`"
        :chart-data="displayDataHeader"
        :options="displayOptionHeader"
        :plugins="yAxesBgPlugin"
        :height="240"
        :width="chartWidth"
      />
    </div>
    <template v-slot:dataTable>
      <v-data-table
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
      >
        <template v-slot:body="{ items }">
          <tbody>
            <tr v-for="item in items" :key="item.text">
              <th>{{ item['クラスター'] }}</th>
              <td class="text-end">{{ item['人数'] }}</td>
            </tr>
          </tbody>
        </template>
      </v-data-table>
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
import { TranslateResult } from 'vue-i18n'
import { ThisTypedComponentOptionsWithRecordProps } from 'vue/types/options'
import { Chart } from 'chart.js'
import {
  GraphDataType,
  ChildGraphDataType
} from '@/utils/formatClustersScatter'
import DataView from '@/components/DataView.vue'
import DataViewBasicInfoPanel from '@/components/DataViewBasicInfoPanel.vue'
import OpenDataLink from '@/components/OpenDataLink.vue'
import { DisplayData, yAxesBgPlugin, scrollPlugin } from '@/plugins/vue-chart'

import { getGraphSeriesStyle } from '@/utils/colors'

type Data = {
  dataKind: 'transition'
  canvas: boolean
  chartWidth: number | null
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
  displayOption: Chart.ChartOptions
  displayDataHeader: DisplayData
  displayOptionHeader: Chart.ChartOptions
  tableHeaders: {
    text: TranslateResult
    value: string
  }[]
  tableData: {
    [key: string]: string
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
  scrollPlugin: Chart.PluginServiceRegistrationOptions[]
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
    },
    scrollPlugin: {
      type: Array,
      default: () => scrollPlugin
    },
    yAxesBgPlugin: {
      type: Array,
      default: () => yAxesBgPlugin
    }
  },
  data: () => ({
    dataKind: 'transition',
    chartWidth: null,
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
      const translatedClusters = this.chartData.clusters.map(cluster => {
        return this.$t(cluster)
      })
      const options: Chart.ChartOptions = {
        tooltips: {
          displayColors: false,
          callbacks: {
            label(tooltipItem: any) {
              return `${
                translatedClusters[data.datasets[tooltipItem.index].y]
              }: ${data.datasets[tooltipItem.index].label} ${unit}`
            },
            title(tooltipItem: any) {
              return data.datasets[tooltipItem[0].index].x
            }
          }
        },
        responsive: false,
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
    displayDataHeader() {
      return {
        labels: ['2020/1/1'],
        datasets: [
          {
            data: [this.chartData.clusters.length],
            backgroundColor: 'transparent',
            borderWidth: 0
          }
        ]
      }
    },
    displayOptionHeader() {
      const data = this.chartData
      const options: Chart.ChartOptions = {
        responsive: false,
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
                  return data.clusters[i]
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
        { text: this.$t('クラスター/感染源'), value: 'クラスター' },
        {
          text: this.$t('人数'),
          value: '人数',
          align: 'end'
        }
      ]
    },
    tableData() {
      const clusters = this.chartData.clusters
      const data: { [x: string]: any }[] = []
      clusters.forEach(dl => {
        if (dl !== '') {
          data.push({
            クラスター: this.$t(dl),
            人数: 0
          })
        }
      })
      this.chartData.datasets.forEach(d => {
        data[clusters.indexOf(clusters[d.y - 1])]['人数'] += d.label
      })
      data.forEach((d, i) => {
        data[i]['人数'] = d['人数'].toLocaleString()
      })
      return data.reverse()
    }
  },
  mounted() {
    if (this.$el) {
      this.chartWidth =
        ((this.$el!.clientWidth - 22 * 2 - 38) / 30) *
          this.displayData.labels!.length +
        38
      this.chartWidth = Math.max(
        this.$el!.clientWidth - 22 * 2,
        this.chartWidth
      )
    }
    const scatterChart = this.$refs.scatterChart as Vue
    const barElement = scatterChart.$el
    const canvas = barElement.querySelector('canvas')
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
