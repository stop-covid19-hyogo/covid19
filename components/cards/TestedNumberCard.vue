<template>
  <v-col cols="12" md="6" class="DataCard">
    <time-stacked-bar-chart
      :title="$t('検査実施件数')"
      :title-id="'number-of-tested'"
      :chart-id="'time-stacked-bar-chart-inspections'"
      :chart-data="inspectionsGraph"
      :date="inspectionsSummary.last_update"
      :items="inspectionsItems"
      :labels="inspectionsLabels"
      :unit="$t('件.tested')"
      :data-labels="inspectionsDataLabels"
      :url="
        'http://open-data.pref.hyogo.lg.jp/index.php?key=muve6rx2r-175#_175'
      "
    >
      <!-- 件.tested = 検査数 -->
      <!--<template v-if="$i18n.locale !== 'ja-basic'" v-slot:additionalNotes>
        {{ $t('※1: 疑い例・接触者調査') }}
        <br />
        {{ $t('※2: チャーター便・クルーズ船') }}
      </template>-->
    </time-stacked-bar-chart>
  </v-col>
</template>

<script>
import inspectionsSummary from '@/data/inspections_summary.json'
import TimeStackedBarChart from '@/components/TimeStackedBarChart.vue'

export default {
  components: {
    TimeStackedBarChart
  },
  data() {
    // 検査実施日別状況
    const allInspectionsArray = []
    for (let i = 0; i < inspectionsSummary.data['検査検体数'].length; i++) {
      allInspectionsArray.push(
        inspectionsSummary.data['検査検体数'][i] -
          inspectionsSummary.data['陽性確認'][i]
      )
    }
    const inspectionsGraph = [
      inspectionsSummary.data['陽性確認'],
      allInspectionsArray
    ]

    const inspectionsItems = [this.$t('陽性患者数'), this.$t('陰性確認者')]
    const inspectionsLabels = inspectionsSummary.labels
    const inspectionsDataLabels = [this.$t('陽性患者数'), this.$t('陰性確認者')]

    const data = {
      inspectionsSummary,
      inspectionsGraph,
      inspectionsItems,
      inspectionsLabels,
      inspectionsDataLabels
    }
    return data
  }
}
</script>
