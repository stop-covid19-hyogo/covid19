<template>
  <v-col cols="12" md="6" class="DataCard">
    <client-only>
      <scatter-chart
        :title="$t('クラスター別陽性患者数')"
        :title-id="'patients-by-clusters'"
        :chart-id="'time-bar-chart-patients-by-clusters'"
        :chart-data="clustersScatter"
        :date="clusters.last_update"
        :unit="$t('人')"
        :info="sumInfoOfClusters"
        :url="'http://open-data.pref.hyogo.lg.jp/index.php?key=mu9jmny45-175#_175'"
      >
        <template v-slot:additionalDescription>
          <span>{{ $t('（注）') }}</span>
          <ul>
            <li>
              {{ $t('重複者とは、複数のクラスターに該当する人を指す') }}
            </li>
            <li>
              {{
                $t(
                  'クラスター名が長いため、一部表記をアルファベットで置き換えている。詳細はテーブルを参照'
                )
              }}
            </li>
          </ul>
        </template>
      </scatter-chart>
    </client-only>
  </v-col>
</template>

<script>
import ScatterChart from '@/components/ScatterChart.vue'
import clusters from '@/data/clusters.json'
import patients from '@/data/patients.json'
import formatClustersScatter from '@/utils/formatClustersScatter'
import { formatTable } from '@/utils/formatTable'

export default {
  components: {
    ScatterChart,
  },
  data() {
    // 感染者数
    const patientsTable = formatTable(patients.data)

    // 日別クラスター陽性患者数
    const clustersScatter = formatClustersScatter(clusters.data)

    let clusterTotal = 0
    clustersScatter.datasets.forEach((d) => {
      clusterTotal += d.label
    })
    const sumInfoOfClusters = {
      lText: clusterTotal.toLocaleString(),
      sText:
        this.$t('重複者') +
        ': ' +
        (clusterTotal - patientsTable.datasets.length).toLocaleString() +
        this.$t('人'),
      unit: this.$t('人'),
    }

    return {
      clusters,
      clustersScatter,
      sumInfoOfClusters,
    }
  },
}
</script>
