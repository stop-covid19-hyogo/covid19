<template>
  <div class="MainPage">
    <page-header
      :icon="headerItem.icon"
      :title="headerItem.title"
      :date="headerItem.date"
    />

    <!-- <whats-new class="mb-4" :items="newsItems" />
    <static-info
      class="mb-4"
      :url="'/flow'"
      :text="'自分や家族の症状に不安や心配があればまずは電話相談をどうぞ'"
      :btn-text="'相談の手順を見る'"
    /> -->

    <v-row class="DataBlock">
      <v-col cols="12" md="6" class="DataCard">
        <svg-card
          title="検査陽性者の状況"
          :title-id="'details-of-confirmed-cases'"
          :date="inspectionsSummary.last_update"
        >
          <confirmed-cases-table v-bind="confirmedCases" />
        </svg-card>
      </v-col>
      <v-col cols="12" md="6" class="DataCard">
        <time-bar-chart
          title="陽性患者数"
          :title-id="'number-of-confirmed-cases'"
          :chart-id="'time-bar-chart-patients'"
          :chart-data="patientsGraph"
          :date="patients.last_update"
          :unit="'人'"
          :url="'https://web.pref.hyogo.lg.jp/kk03/corona_hasseijyokyo.html'"
        />
      </v-col>
      <v-col cols="12" md="6" class="DataCard">
        <data-table
          :title="'陽性患者の属性'"
          :title-id="'attributes-of-confirmed-cases'"
          :chart-data="patientsTable"
          :chart-option="{}"
          :date="patients.last_update"
          :info="sumInfoOfPatients"
          :url="'https://web.pref.hyogo.lg.jp/kk03/corona_hasseijyokyo.html'"
        />
      </v-col>
      <v-col cols="12" md="6" class="DataCard">
        <time-stacked-bar-chart
          title="検査実施数"
          :title-id="'number-of-tested'"
          :chart-id="'time-stacked-bar-chart-inspections'"
          :chart-data="inspectionsGraph"
          :date="inspectionsSummary.last_update"
          :items="inspectionsItems"
          :labels="inspectionsLabels"
          :unit="'件'"
          :url="'https://web.pref.hyogo.lg.jp/kf16/singatakoronakensa.html'"
        />
      </v-col>
      <v-col cols="12" md="6" class="DataCard">
        <time-bar-chart
          title="年代別陽性患者数"
          :title-id="'number-of-confirmed-cases'"
          :chart-id="'time-bar-chart-patients'"
          :chart-data="ageGraph"
          :date="age.last_update"
          :unit="'人'"
          :url="'https://web.pref.hyogo.lg.jp/kk03/corona_hasseijyokyo.html'"
          :show-button="false"
        />
      </v-col>
      <v-col cols="12" md="6" class="DataCard">
        <data-table
          :title="'クラスター別陽性患者数'"
          :title-id="'attributes-of-confirmed-cases'"
          :chart-data="clustersTable"
          :chart-option="{}"
          :date="clustersSummary.last_update"
          :info="sumInfoOfPatients"
          :url="'https://web.pref.hyogo.lg.jp/kk03/corona_hasseijyokyo.html'"
          :desc="'（注）同一の対象者が複数含まれる場合あり'"
        />
      </v-col>
    </v-row>
  </div>
</template>

<script>
import PageHeader from '@/components/PageHeader.vue'
import TimeBarChart from '@/components/TimeBarChart.vue'
import TimeStackedBarChart from '@/components/TimeStackedBarChart.vue'
import lastUpdate from '@/data/last_update.json'
import patients from '@/data/patients.json'
import patientsSummary from '@/data/patients_summary.json'
import mainSummary from '@/data/main_summary.json'
import dischargesSummary from '@/data/discharges_summary.json'
import inspectionsSummary from '@/data/inspections_summary.json'
import age from '@/data/age.json'
import clustersSummary from '@/data/clusters_summary.json'
import DataTable from '@/components/DataTable.vue'
import formatGraph from '@/utils/formatGraph'
import formatTable from '@/utils/formatTable'
import formatConfirmedCases from '@/utils/formatConfirmedCases'
import formatVariableGraph from '@/utils/formatVariableGraph'
import formatClustersTable from '@/utils/formatClustersTable'
import News from '@/data/news.json'
import SvgCard from '@/components/SvgCard.vue'
import ConfirmedCasesTable from '@/components/ConfirmedCasesTable.vue'

export default {
  components: {
    PageHeader,
    TimeBarChart,
    TimeStackedBarChart,
    DataTable,
    SvgCard,
    ConfirmedCasesTable
  },
  data() {
    // 感染者数グラフ
    const patientsGraph = formatGraph(patientsSummary.data)
    // 感染者数
    const patientsTable = formatTable(patients.data)
    // 退院者グラフ
    const dischargesGraph = formatGraph(dischargesSummary.data)

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
    const inspectionsItems = [
      '陽性確認者数',
      '検査検体数'
    ]
    const inspectionsLabels = inspectionsSummary.labels

    // 年齢別陽性患者数
    const ageGraph = formatVariableGraph(age.data)

    // クラスター別陽性患者数
    const clustersTable = formatClustersTable(clustersSummary.data)

    // 死亡者数
    // #MEMO: 今後使う可能性あるので一時コメントアウト
    // const fatalitiesTable = formatTable(
    //   patients.data.filter(patient => patient['備考'] === '死亡')
    // )
    // 検査陽性者の状況
    const confirmedCases = formatConfirmedCases(mainSummary)

    const sumInfoOfPatients = {
      lText: patientsGraph[
        patientsGraph.length - 1
      ].cumulative.toLocaleString(),
      sText: patientsGraph[patientsGraph.length - 1].label + 'の累計',
      unit: '人'
    }

    const data = {
      patients,
      inspectionsSummary,
      age,
      clustersSummary,
      patientsTable,
      patientsGraph,
      dischargesGraph,
      inspectionsGraph,
      inspectionsItems,
      inspectionsLabels,
      ageGraph,
      clustersTable,
      confirmedCases,
      sumInfoOfPatients,
      headerItem: {
        icon: 'mdi-chart-timeline-variant',
        title: '兵庫県内の最新感染動向',
        date: lastUpdate.last_update
      },
      newsItems: News.newsItems
    }
    return data
  },
  head() {
    return {
      title: '兵庫県内の最新感染動向'
    }
  }
}
</script>

<style lang="scss" scoped>
.MainPage {
  .DataBlock {
    margin: 20px -8px;
    .DataCard {
      @include largerThan($medium) {
        padding: 10px;
      }
      @include lessThan($small) {
        padding: 4px 8px;
      }
    }
  }
}
</style>
