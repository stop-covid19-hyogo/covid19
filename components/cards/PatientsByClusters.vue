<template>
  <v-col cols="12" md="6" class="DataCard">
    <scatter
      :title="$t('クラスター別陽性患者数')"
      :title-id="'patients-by-clusters'"
      :chart-id="'time-bar-chart-patients-by-clusters'"
      :chart-data="clustersScatter"
      :date="clusters.last_update"
      :unit="$t('人')"
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
import patients from '@/data/patients.json'
import Scatter from '@/components/Scatter'
import formatTable from '@/utils/formatTable'
import formatClustersScatter from '@/utils/formatClustersScatter'

export default {
  components: {
    Scatter
  },
  data() {
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
      clustersScatter,
      sumInfoOfClusters
    }
    return data
  }
}
</script>
