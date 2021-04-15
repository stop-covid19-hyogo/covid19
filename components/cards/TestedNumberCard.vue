<template>
  <v-col cols="12" md="6" class="DataCard">
    <client-only>
      <time-stacked-bar-chart
        :title="$t('検査実施件数')"
        :title-id="'number-of-tested'"
        :chart-id="'time-stacked-bar-chart-inspections'"
        :chart-data="inspectionsGraph"
        :date="last_update"
        :items="inspectionsItems"
        :labels="inspectionsLabels"
        :unit="$t('件.tested')"
        :url="'http://open-data.pref.hyogo.lg.jp/?page_id=141'"
        :data-labels="inspectionsDataLabels"
        :table-labels="inspectionsTableLabels"
      >
        <!-- 件.tested = 検査数 -->
        <template v-slot:additionalDescription>
          <span>{{ $t('（注）') }}</span>
          <ul>
            <!--<li>
              {{
                $t(
                  '検体採取日を基準とする。ただし、一部検査結果判明日に基づくものを含む'
                )
              }}
            </li>-->
            <li>
              {{ $t('同一の対象者について複数の検体を検査する場合がある') }}
            </li>
            <!--<li>
              {{
                $t('2020年5月13日以降は、PCR検査に加え、抗原検査の件数を含む')
              }}
            </li>
            <li>
              {{
                $t(
                  '速報値として公開するものであり、後日確定データとして修正される場合がある'
                )
              }}
            </li>-->
            <li>
              {{
                $t('民間検査機関等の検査件数には抗原検査の検査件数も含まれる')
              }}
            </li>
          </ul>
        </template>
      </time-stacked-bar-chart>
    </client-only>
  </v-col>
</template>

<script>
import dayjs from 'dayjs'
import duration from 'dayjs/plugin/duration'

import TimeStackedBarChart from '@/components/TimeStackedBarChart.vue'
// import Data from '@/data/data.json'
import inspectionsSummary from '@/data/inspections_summary.json'
dayjs.extend(duration)

export default {
  components: {
    TimeStackedBarChart,
  },
  data() {
    // const inspectionsSummary = Data.inspections_summary
    // eslint-disable-next-line camelcase
    const { last_update, data } = inspectionsSummary

    // 検査実施日別状況
    const inspectionsGraph = [data['地方衛生研究所等'], data['民間検査機関等']]

    const inspectionsItems = [
      this.$t('地方衛生研究所等'),
      this.$t('民間検査機関等'),
    ]
    const inspectionsLabels = inspectionsSummary.labels
    const inspectionsDataLabels = [
      this.$t('地方衛生研究所等'),
      this.$t('民間検査機関等'),
    ]
    const inspectionsTableLabels = [
      this.$t('地方衛生研究所等'),
      this.$t('民間検査機関等'),
    ]

    return {
      last_update,
      inspectionsGraph,
      inspectionsItems,
      inspectionsLabels,
      inspectionsDataLabels,
      inspectionsTableLabels,
    }
  },
}
</script>
