<template>
  <v-col cols="12" md="6" class="DataCard">
    <time-bar-chart
      :title="$t('年代別陽性患者数')"
      :title-id="'patients-by-age'"
      :chart-id="'time-bar-chart-patients-by-age'"
      :chart-data="ageGraph"
      :date="age.last_update"
      :unit="$t('人')"
      :url="'http://open-data.pref.hyogo.lg.jp/?page_id=141'"
      :show-button="false"
      :use-scroll="false"
    />
  </v-col>
</template>

<script>
import age from '@/data/age.json'
import TimeBarChart from '@/components/TimeBarChart.vue'
import formatVariableGraph from '@/utils/formatVariableGraph'

export default {
  components: {
    TimeBarChart
  },
  data() {
    // 年代別陽性患者数
    const ageGraph = formatVariableGraph(age.data)
    // 年代を翻訳
    ageGraph.forEach((d, i) => {
      const label = d.label
      if (label.substr(-1, 1) === '代') {
        const age = label.substring(0, 2)
        ageGraph[i].label = this.$t('{age}代', { age })
      } else {
        ageGraph[i].label = this.$t(label)
      }
    })

    const data = {
      age,
      ageGraph
    }
    return data
  }
}
</script>
