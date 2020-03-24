<template>
  <v-col cols="12" md="6" class="DataCard">
    <data-table
      :title="$t('クラスター別陽性患者数')"
      :title-id="'patients-by-clusters'"
      :chart-data="clustersTable"
      :chart-option="{}"
      :date="clustersSummary.last_update"
      :info="sumInfoOfClusters"
      :url="'https://web.pref.hyogo.lg.jp/kk03/corona_hasseijyokyo.html'"
      :desc="$t('（注）同一の対象者が複数含まれる場合あり')"
    />
    <!--<time-bar-chart
      title="クラスター別陽性患者数"
      :title-id="'patients-by-clusters'"
      :chart-id="'time-bar-chart-patients-by-clusters'"
      :chart-data="clustersGraph"
      :date="clustersSummary.last_update"
      :unit="'人'"
      :url="'https://web.pref.hyogo.lg.jp/kk03/corona_hasseijyokyo.html'"
      :desc="'（注）同一の対象者が複数含まれる場合あり'"
      :show-button="false"
      :horizontal="true"
      :overlap="patientsTable.datasets.length"
    />-->
  </v-col>
</template>

<script>
import clustersSummary from '@/data/clusters_summary.json'
import patientsSummary from '@/data/patients_summary.json'
import DataTable from '@/components/DataTable.vue'
import formatClustersTable from '@/utils/formatClustersTable'
import formatGraph from '@/utils/formatGraph'
import formatVariableGraph from '@/utils/formatVariableGraph'

export default {
  components: {
    DataTable
  },
  data() {
    // クラスター別陽性患者数
    const clustersTable = formatClustersTable(clustersSummary.data)
    const clustersGraph = formatVariableGraph(clustersSummary.data)

    // 感染者数グラフ 感染者数取得のため
    const patientsGraph = formatGraph(patientsSummary.data)

    const sumInfoOfClusters = {
      lText: clustersGraph[
        clustersGraph.length - 1
      ].cumulative.toLocaleString(),
      sText:
        this.$t('重複者') +
        ': ' +
        (
          clustersGraph[clustersGraph.length - 1].cumulative -
          patientsGraph[patientsGraph.length - 1].cumulative
        ).toLocaleString() +
        this.$t('人'),
      unit: this.$t('人')
    }

    const data = {
      clustersSummary,
      clustersTable,
      sumInfoOfClusters
    }
    return data
  }
}
</script>
