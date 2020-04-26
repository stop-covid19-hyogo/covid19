<template>
  <v-col cols="12" md="6" class="DataCard">
    <!--<data-table
      :title="$t('クラスター別陽性患者数')"
      :title-id="'patients-by-clusters'"
      :chart-data="clustersTable"
      :chart-option="{}"
      :date="clustersSummary.last_update"
      :info="sumInfoOfClusters"
      :url="
       'http://open-data.pref.hyogo.lg.jp/?page_id=141'
      "
      :desc="$t('（注）同一の対象者が複数含まれる場合あり')"
    />-->
    <!--<time-bar-chart
      title="クラスター別陽性患者数"
      :title-id="'patients-by-clusters'"
      :chart-id="'time-bar-chart-patients-by-clusters'"
      :chart-data="clustersGraph"
      :date="clustersSummary.last_update"
      :unit="'人'"
      :url="
        'http://open-data.pref.hyogo.lg.jp/index.php?key=mu9jmny45-175#_175'
      "
      :desc="'（注）同一の対象者が複数含まれる場合あり'"
      :show-button="false"
      :horizontal="true"
      :overlap="patientsTable.datasets.length"
    />-->
    <scatter
      :title="$t('クラスター別陽性患者数')"
      :title-id="'patients-by-clusters'"
      :chart-id="'time-bar-chart-patients-by-clusters'"
      :chart-data="clustersScatter"
      :date="clusters.last_update"
      :unit="'人'"
      :info="sumInfoOfClusters"
      :desc="$t('（注）重複者とは、複数のクラスターに該当する人を指す')"
      :url="
        'http://open-data.pref.hyogo.lg.jp/index.php?key=mu9jmny45-175#_175'
      "
    />
  </v-col>
</template>

<script>
import clusters from '@/data/clusters.json'
// import clustersSummary from '@/data/clusters_summary.json'
import patients from '@/data/patients.json'
// import DataTable from '@/components/DataTable.vue'
import Scatter from '@/components/Scatter'
// import formatClustersTable from '@/utils/formatClustersTable'
import formatTable from '@/utils/formatTable'
// import formatVariableGraph from '@/utils/formatVariableGraph'
import formatClustersScatter from '@/utils/formatClustersScatter'

export default {
  components: {
    // DataTable
    Scatter
  },
  data() {
    // クラスター別陽性患者数
    // const clustersTable = formatClustersTable(clustersSummary.data)
    // const clustersGraph = formatVariableGraph(clustersSummary.data)

    // 感染者数
    const patientsTable = formatTable(patients.data)

    // 日別クラスター陽性患者数
    const clustersScatter = formatClustersScatter(clusters.data)

    let clusterTotal = 0
    clustersScatter.datasets.forEach(d => {
      clusterTotal += d.label
    })
    const sumInfoOfClusters = {
      lText: clusterTotal.toLocaleString(),
      sText:
        this.$t('重複者') +
        ': ' +
        (clusterTotal - patientsTable.datasets.length).toLocaleString() +
        this.$t('人'),
      unit: this.$t('人')
    }

    const data = {
      clusters,
      // clustersSummary,
      // clustersTable,
      clustersScatter,
      sumInfoOfClusters
    }
    return data
  }
}
</script>
