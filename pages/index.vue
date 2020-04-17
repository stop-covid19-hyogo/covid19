<template>
  <div class="MainPage">
    <div class="Header mb-3">
      <page-header :icon="headerItem.icon">
        {{ headerItem.title }}
      </page-header>
      <div class="UpdatedAt">
        <span>{{ $t('最終更新') }} </span>
        <time :datetime="updatedAt">{{ updatedTimeStr }}</time>
      </div>
      <div
        v-show="!['ja', 'ja-basic'].includes($i18n.locale)"
        class="Annotation"
      >
        <span>{{ $t('注釈') }} </span>
      </div>
    </div>
    <whats-new class="mb-4" :items="newsItems" />
    <!-- <static-info
      class="mb-4"
      :url="localePath('/flow')"
      :text="$t('自分や家族の症状に不安や心配があればまずは電話相談をどうぞ')"
      :btn-text="$t('相談の手順を見る')"
    /> -->
    <v-row class="DataBlock">
      <!-- 検査陽性者の状況 -->
      <confirmed-cases-details-card />
      <!-- 検査実施状況 -->
      <!--<tested-cases-details-card />-->
      <!-- 陽性患者数 -->
      <confirmed-cases-number-card />
      <!-- 陽性患者の属性 -->
      <confirmed-cases-attributes-card />
      <!-- 検査実施人数 -->
      <!--<inspection-persons-number-card />-->
      <!-- 検査実施件数 -->
      <tested-number-card />
      <!-- 新型コロナコールセンター相談件数 -->
      <!--<telephone-advisory-reports-number-card />-->
      <!-- 区市町村別患者数 -->
      <!--<confirmed-cases-by-municipalities-card />-->
      <!-- 新型コロナ受診相談窓口相談件数 -->
      <!--<consultation-desk-reports-number-card />-->
      <!-- 都営地下鉄の利用者数の推移 -->
      <!--<metro-card />-->
      <!-- 年代別陽性患者数 -->
      <patients-by-age />
      <!-- クラスター別陽性患者数 -->
      <patients-by-clusters />
      <!-- 入院患者数と残り病床数 -->
      <!--<patients-and-sickbeds />-->
      <!-- 都庁来庁者数の推移 -->
      <!--<agency-card />-->
    </v-row>
    <v-divider />
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import { MetaInfo } from 'vue-meta'
import PageHeader from '@/components/PageHeader.vue'
import WhatsNew from '@/components/WhatsNew.vue'
// import StaticInfo from '@/components/StaticInfo.vue'
import lastUpdate from '@/data/last_update.json'
import News from '@/data/news.json'
import ConfirmedCasesDetailsCard from '@/components/cards/ConfirmedCasesDetailsCard.vue'
import ConfirmedCasesNumberCard from '@/components/cards/ConfirmedCasesNumberCard.vue'
import ConfirmedCasesAttributesCard from '@/components/cards/ConfirmedCasesAttributesCard.vue'
// import ConfirmedCasesByMunicipalitiesCard from '@/components/cards/ConfirmedCasesByMunicipalitiesCard.vue'
// import TestedCasesDetailsCard from '@/components/cards/TestedCasesDetailsCard.vue'
// import InspectionPersonsNumberCard from '@/components/cards/InspectionPersonsNumberCard.vue'
import TestedNumberCard from '@/components/cards/TestedNumberCard.vue'
/* import TelephoneAdvisoryReportsNumberCard from '@/components/cards/TelephoneAdvisoryReportsNumberCard.vue'
import ConsultationDeskReportsNumberCard from '@/components/cards/ConsultationDeskReportsNumberCard.vue'
import MetroCard from '@/components/cards/MetroCard.vue'
import AgencyCard from '@/components/cards/AgencyCard.vue' */
import PatientsByAge from '@/components/cards/PatientsByAge.vue'
import PatientsByClusters from '@/components/cards/PatientsByClusters.vue'
// import PatientsAndSickbeds from '@/components/cards/PatientsAndSickbeds.vue'
import { convertISO8601FormatToDatetime } from '@/utils/formatDate'

export default Vue.extend({
  components: {
    PageHeader,
    WhatsNew,
    // StaticInfo,
    ConfirmedCasesDetailsCard,
    ConfirmedCasesNumberCard,
    ConfirmedCasesAttributesCard,
    /* ConfirmedCasesByMunicipalitiesCard,
    TestedCasesDetailsCard,
    InspectionPersonsNumberCard, */
    TestedNumberCard,
    /* TelephoneAdvisoryReportsNumberCard,
    ConsultationDeskReportsNumberCard,
    MetroCard,
    AgencyCard, */
    PatientsByAge,
    PatientsByClusters
    // PatientsAndSickbeds
  },
  data() {
    const updatedTimeStr = convertISO8601FormatToDatetime(
      lastUpdate.last_update
    )
    const data = {
      updatedTimeStr,
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
      return convertISO8601FormatToDatetime(lastUpdate.last_update)
    }
  },
  head(): MetaInfo {
    return {
      title: this.$t('兵庫県非公式 新型コロナウイルスまとめサイト') as string,
      titleTemplate: ''
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
