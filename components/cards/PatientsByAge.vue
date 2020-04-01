<template>
  <v-col cols="12" md="6" class="DataCard">
    <time-bar-chart
      :title="$t('年代別陽性患者数')"
      :title-id="'patients-by-age'"
      :chart-id="'time-bar-chart-patients-by-age'"
      :chart-data="ageGraph"
      :date="age.last_update"
      :unit="'人'"
      :url="
       'http://open-data.pref.hyogo.lg.jp/?page_id=141'
      "
      :show-button="false"
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

    const data = {
      age,
      ageGraph
    }
    return data
  }
}
</script>
