<template>
  <v-col cols="12" md="6" class="DataCard">
    <circle-chart
      :title="$t('入院患者数と残り病床数')"
      :title-id="'patients-and-sickbeds'"
      :chart-data="sickbedsGraph"
      :date="sickbedsSummary.last_update"
      :unit="$t('床')"
      :info="$t('総病床数')"
      :url="'https://web.pref.hyogo.lg.jp/kk03/corona_hasseijyokyo.html'"
    />
  </v-col>
</template>

<script>
import sickbedsSummary from '@/data/sickbeds_summary.json'
import CircleChart from '@/components/CircleChart.vue'
import formatVariableGraph from '@/utils/formatVariableGraph'

export default {
  components: {
    CircleChart
  },
  data() {
    // 年代別陽性患者数
    const sickbedsGraph = formatVariableGraph(sickbedsSummary.data)

    const data = {
      sickbedsSummary,
      sickbedsGraph
    }
    return data
  }
}
</script>
