<template>
  <div class="MainPage">
    <!--<page-header
      :icon="headerItem.icon"
      :title="headerItem.title"
      :date="headerItem.date"
    />

    <whats-new class="mb-4" :items="newsItems" />
    <static-info
      class="mb-4"
      :url="'/flow'"
      :text="'自分や家族の症状に不安や心配があればまずは電話相談をどうぞ'"
      :btn-text="'相談の手順を見る'"
    />

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
          :title-id="'patients-by-age'"
          :chart-id="'time-bar-chart-patients-by-age'"
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
          :title-id="'patients-by-clusters'"
          :chart-data="clustersTable"
          :chart-option="{}"
          :date="clustersSummary.last_update"
          :info="sumInfoOfClusters"
          :url="'https://web.pref.hyogo.lg.jp/kk03/corona_hasseijyokyo.html'"
          :desc="'（注）同一の対象者が複数含まれる場合あり'"
        />
        <time-bar-chart
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
        />
      </v-col>
      <v-col cols="12" md="6" class="DataCard">
        <circle-chart
          title="入院患者数と残り病床数"
          :title-id="'patients-and-sickbeds'"
          :chart-data="sickbedsGraph"
          :date="sickbedsSummary.last_update"
          :unit="'床'"
          :info="'総病床数'"
          :url="'https://web.pref.hyogo.lg.jp/kk03/corona_hasseijyokyo.html'"
        />
      </v-col>-->
    <div class="Header mb-3">
      <page-header :icon="headerItem.icon">
        {{ headerItem.title }}
      </page-header>
      <div class="UpdatedAt">
        <span>{{ $t('最終更新') }} </span>
        <time :datetime="updatedAt">{{ lastUpdate.last_update }}</time>
      </div>
      <div
        v-show="!['ja', 'ja-basic'].includes($i18n.locale)"
        class="Annotation"
      >
        <span>{{ $t('注釈') }} </span>
      </div>
    </div>
    <!--<whats-new class="mb-4" :items="newsItems" />
    <static-info
      class="mb-4"
      :url="localePath('/flow')"
      :text="$t('自分や家族の症状に不安や心配があればまずは電話相談をどうぞ')"
      :btn-text="$t('相談の手順を見る')"
    />-->
    <v-row class="DataBlock">
      <confirmed-cases-details-card />
      <!--<tested-cases-details-card />-->
      <confirmed-cases-number-card />
      <confirmed-cases-attributes-card />
      <!--<inspection-persons-number-card />-->
      <tested-number-card />
      <!--<telephone-advisory-reports-number-card />
      <consultation-desk-reports-number-card />
      <metro-card />
      <agency-card />
      <shinjuku-visitors-card />
      <chiyoda-visitors-card />-->
      <patients-by-age />
      <patients-by-clusters />
      <patients-and-sickbeds />
    </v-row>
    <!--<v-divider />
    <v-row class="DataBlock">
      <shinjuku-st-map-card />
      <tokyo-st-map-card />
    </v-row>-->
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import { MetaInfo } from 'vue-meta'
import PageHeader from '@/components/PageHeader.vue'
// import WhatsNew from '@/components/WhatsNew.vue'
// import StaticInfo from '@/components/StaticInfo.vue'
import lastUpdate from '@/data/last_update.json'
import News from '@/data/news.json'
import ConfirmedCasesDetailsCard from '@/components/cards/ConfirmedCasesDetailsCard.vue'
// import TestedCasesDetailsCard from '@/components/cards/TestedCasesDetailsCard.vue'
import ConfirmedCasesNumberCard from '@/components/cards/ConfirmedCasesNumberCard.vue'
import ConfirmedCasesAttributesCard from '@/components/cards/ConfirmedCasesAttributesCard.vue'
import TestedNumberCard from '@/components/cards/TestedNumberCard.vue'
/* import InspectionPersonsNumberCard from '@/components/cards/InspectionPersonsNumberCard.vue'
import TelephoneAdvisoryReportsNumberCard from '@/components/cards/TelephoneAdvisoryReportsNumberCard.vue'
import ConsultationDeskReportsNumberCard from '@/components/cards/ConsultationDeskReportsNumberCard.vue' */
import PatientsByAge from '@/components/cards/PatientsByAge.vue'
import PatientsByClusters from '@/components/cards/PatientsByClusters.vue'
import PatientsAndSickbeds from '@/components/cards/PatientsAndSickbeds.vue'
// import MetroCard from '@/components/cards/MetroCard.vue'
// import AgencyCard from '@/components/cards/AgencyCard.vue'
import { convertDatetimeToISO8601Format } from '@/utils/formatDate'
/* import ShinjukuVisitorsCard from '@/components/cards/ShinjukuVisitorsCard.vue'
import ChiyodaVisitorsCard from '@/components/cards/ChiyodaVisitorsCard.vue'
import ShinjukuStMapCard from '@/components/cards/ShinjukuStMapCard.vue'
import TokyoStMapCard from '@/components/cards/TokyoStMapCard.vue' */

export default Vue.extend({
  components: {
    PageHeader,
    // WhatsNew,
    // StaticInfo,
    ConfirmedCasesDetailsCard,
    // TestedCasesDetailsCard,
    ConfirmedCasesNumberCard,
    ConfirmedCasesAttributesCard,
    TestedNumberCard,
    /* InspectionPersonsNumberCard,
    TelephoneAdvisoryReportsNumberCard,
    ConsultationDeskReportsNumberCard,
    MetroCard,
    AgencyCard,
    ShinjukuVisitorsCard,
    ChiyodaVisitorsCard,
    ShinjukuStMapCard,
    TokyoStMapCard */
    PatientsByAge,
    PatientsByClusters,
    PatientsAndSickbeds
  },
  data() {
    const data = {
      lastUpdate,
      headerItem: {
        icon: 'mdi-chart-timeline-variant',
        title: this.$t('兵庫県内の最新感染動向')
      },
      newsItems: News.newsItems
    }
    return data
  },
  computed: {
    updatedAt() {
      return convertDatetimeToISO8601Format(this.$data.lastUpdate.last_update)
    }
  },
  head(): MetaInfo {
    return {
      title: this.$t('兵庫県内の最新感染動向') as string
    }
  }
})
</script>

<style lang="scss" scoped>
.MainPage {
  .Header {
    display: flex;
    flex-wrap: wrap;
    align-items: flex-end;

    @include lessThan($small) {
      flex-direction: column;
      align-items: baseline;
    }
  }

  .UpdatedAt {
    @include font-size(14);

    color: $gray-3;
    margin-bottom: 0.2rem;
  }

  .Annotation {
    @include font-size(12);

    color: $gray-3;
    @include largerThan($small) {
      margin: 0 0 0 auto;
    }
  }
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
