<template>
  <component :is="cardComponent" />
</template>

<script lang="ts">
/* eslint-disable simple-import-sort/sort -- ブラウザでの表示順に合わせて各 card の component を import する */
/*
// ---- モニタリング項目
// 検査陽性者の状況
import ConfirmedCasesDetailsCard from '@/components/cards/ConfirmedCasesDetailsCard.vue'
// 報告日別による陽性者数の推移
import ConfirmedCasesNumberCard from '@/components/cards/ConfirmedCasesNumberCard.vue'
// モニタリング項目
import MonitoringItemsOverviewCard from '@/components/cards/MonitoringItemsOverviewCard.vue'
// モニタリング項目(1)新規陽性者数
import MonitoringConfirmedCasesNumberCard from '@/components/cards/MonitoringConfirmedCasesNumberCard.vue'
// モニタリング項目(2)#7119における発熱等相談件数
import ConsultationAboutFeverNumberCard from '@/components/cards/ConsultationAboutFeverNumberCard.vue'
// モニタリング項目(3)新規陽性者における接触歴等不明者数
import UntrackedRateCard from '@/components/cards/UntrackedRateCard.vue'
// モニタリング項目(4)検査の陽性率
import PositiveRateCard from '@/components/cards/PositiveRateCard.vue'
// モニタリング項目(5)救急医療の東京ルールの適用件数
import TokyoRulesApplicationNumberCard from '@/components/cards/TokyoRulesApplicationNumberCard.vue'
// モニタリング項目(6)入院患者数
import HospitalizedNumberCard from '@/components/cards/HospitalizedNumberCard.vue'
// モニタリング項目(7)重症患者数
import SevereCaseCard from '@/components/cards/SevereCaseCard.vue'
// ---- その他 参考指標
// 陽性者の属性
import ConfirmedCasesAttributesCard from '@/components/cards/ConfirmedCasesAttributesCard.vue'
// 陽性者数（区市町村別）
import ConfirmedCasesByMunicipalitiesCard from '@/components/cards/ConfirmedCasesByMunicipalitiesCard.vue'
// 発症日別による陽性者数の推移
import PositiveNumberByDevelopedDateCard from '@/components/cards/PositiveNumberByDevelopedDateCard.vue'
// 確定日別による陽性者数の推移
import PositiveNumberByDiagnosedDateCard from '@/components/cards/PositiveNumberByDiagnosedDateCard.vue'
// 検査実施件数
import TestedNumberCard from '@/components/cards/TestedNumberCard.vue'
// 新型コロナコールセンター相談件数
import TelephoneAdvisoryReportsNumberCard from '@/components/cards/TelephoneAdvisoryReportsNumberCard.vue'
// 受診相談窓口における相談件数
import MonitoringConsultationDeskReportsNumberCard from '@/components/cards/MonitoringConsultationDeskReportsNumberCard.vue'
// 東京都発熱相談センターにおける相談件数
import TokyoFeverConsultationCenterReportsNumberCard from '@/components/cards/TokyoFeverConsultationCenterReportsNumberCard.vue'
// 都営地下鉄の利用者数の推移
import MetroCard from '@/components/cards/MetroCard.vue'
// 都庁来庁者数の推移
import AgencyCard from '@/components/cards/AgencyCard.vue'
*/
// ---- 兵庫県版項目
// 検査陽性者の状況
import ConfirmedCasesDetailsCard from '@/components/cards/ConfirmedCasesDetailsCard.vue'
// 治療中患者数の変化状況
import ChangesPatientsNumberCard from '@/components/cards/ChangesPatientsNumberCard.vue'
// 陽性患者数
import ConfirmedCasesNumberCard from '@/components/cards/ConfirmedCasesNumberCard.vue'
// 検査実施件数
import TestedNumberCard from '@/components/cards/TestedNumberCard.vue'
// 陽性者の属性
import ConfirmedCasesAttributesCard from '@/components/cards/ConfirmedCasesAttributesCard.vue'
// 年代別陽性患者数
import PatientsByAge from '@/components/cards/PatientsByAge.vue'
// クラスター別陽性患者数
// import PatientsByClusters from '@/components/cards/PatientsByClusters.vue'
// 入院患者数と残り病床数
// import PatientsAndSickbeds from '@/components/cards/PatientsAndSickbeds.vue'
/* eslint-enable simple-import-sort/sort */

import { Vue, Component } from 'nuxt-property-decorator'
import type { NuxtOptionsHead as MetaInfo } from '@nuxt/types/config/head'
import type { NuxtConfig } from '@nuxt/types'
import { getLinksLanguageAlternative } from '@/utils/i18nUtils'
import { convertDateToSimpleFormat } from '@/utils/formatDate'

@Component({
  components: {
    /*
    // ---- モニタリング項目
    ConfirmedCasesDetailsCard,
    ConfirmedCasesNumberCard,
    MonitoringItemsOverviewCard,
    MonitoringConfirmedCasesNumberCard,
    ConsultationAboutFeverNumberCard,
    UntrackedRateCard,
    PositiveRateCard,
    TokyoRulesApplicationNumberCard,
    HospitalizedNumberCard,
    SevereCaseCard,
    // ---- その他 参考指標
    ConfirmedCasesAttributesCard,
    ConfirmedCasesByMunicipalitiesCard,
    PositiveNumberByDevelopedDateCard,
    PositiveNumberByDiagnosedDateCard,
    TestedNumberCard,
    TelephoneAdvisoryReportsNumberCard,
    MonitoringConsultationDeskReportsNumberCard,
    TokyoFeverConsultationCenterReportsNumberCard,
    MetroCard,
    AgencyCard,
     */
    // ---- 兵庫県版項目
    ConfirmedCasesDetailsCard,
    ChangesPatientsNumberCard,
    ConfirmedCasesNumberCard,
    TestedNumberCard,
    ConfirmedCasesAttributesCard,
    PatientsByAge,
    // PatientsByClusters,
    // PatientsAndSickbeds,
  },
})
export default class CardContainer extends Vue implements NuxtConfig {
  data() {
    let title, updatedAt, cardComponent
    switch (this.$route.params.card) {
      // NOTE: 以下，ブラウザでの表示順に合わせて条件分岐を行う
      /*
      // ---- モニタリング項目
      // 検査陽性者の状況
      case 'details-of-confirmed-cases':
        cardComponent = 'confirmed-cases-details-card'
        break
      // 報告日別による陽性者数の推移
      case 'number-of-confirmed-cases':
        cardComponent = 'confirmed-cases-number-card'
        break
      // モニタリング項目
      case 'monitoring-items-overview':
        cardComponent = 'monitoring-items-overview-card'
        break
      // モニタリング項目(1)新規陽性者数
      case 'monitoring-number-of-confirmed-cases':
        cardComponent = 'monitoring-confirmed-cases-number-card'
        break
      // モニタリング項目(2)#7119における発熱等相談件数
      case 'number-of-reports-to-consultations-about-fever-in-7119':
        cardComponent = 'consultation-about-fever-number-card'
        break
      // モニタリング項目(3)新規陽性者における接触歴等不明者数
      case 'untracked-rate':
        cardComponent = 'untracked-rate-card'
        break
      // モニタリング項目(4)検査の陽性率
      case 'positive-rate':
        cardComponent = 'positive-rate-card'
        break
      // モニタリング項目(5)救急医療の東京ルールの適用件数
      case 'number-of-tokyo-rules-applied':
        cardComponent = 'tokyo-rules-application-number-card'
        break
      // モニタリング項目(6)入院患者数
      case 'number-of-hospitalized':
        cardComponent = 'hospitalized-number-card'
        break
      // モニタリング項目(7)重症患者数
      case 'positive-status-severe-case':
        cardComponent = 'severe-case-card'
        break
      // ---- その他 参考指標
      // 陽性者の属性
      case 'attributes-of-confirmed-cases':
        cardComponent = 'confirmed-cases-attributes-card'
        break
      // 陽性者数（区市町村別）
      case 'number-of-confirmed-cases-by-municipalities':
        cardComponent = 'confirmed-cases-by-municipalities-card'
        break
      // 発症日別による陽性者数の推移
      case 'positive-number-by-developed-date':
        cardComponent = 'positive-number-by-developed-date-card'
        break
      // 確定日別による陽性者数の推移
      case 'positive-number-by-diagnosed-date':
        cardComponent = 'positive-number-by-diagnosed-date-card'
        break
      // 検査実施件数
      case 'number-of-tested':
        cardComponent = 'tested-number-card'
        break
      // 新型コロナコールセンター相談件数
      case 'number-of-reports-to-covid19-telephone-advisory-center':
        cardComponent = 'telephone-advisory-reports-number-card'
        break
      // 受診相談窓口における相談件数
      case 'monitoring-number-of-reports-to-covid19-consultation-desk':
        cardComponent = 'monitoring-consultation-desk-reports-number-card'
        break
      // 東京都発熱相談センターにおける相談件数
      case 'number-of-reports-to-tokyo-fever-consultation-center':
        cardComponent = 'tokyo-fever-consultation-center-reports-number-card'
        break
      // 都営地下鉄の利用者数の推移
      case 'predicted-number-of-toei-subway-passengers':
        cardComponent = 'metro-card'
        break
      // 都庁来庁者数の推移
      case 'agency':
        cardComponent = 'agency-card'
       */
      // ---- 兵庫県版項目
      // 検査陽性者の状況
      case 'details-of-confirmed-cases':
        cardComponent = 'confirmed-cases-details-card'
        break
      // 治療中患者数の変化状況
      case 'changes-in-number-of-hospitalized-patients':
        cardComponent = 'changes-patients-number-card'
        break
      // 陽性患者数
      case 'number-of-confirmed-cases':
        cardComponent = 'confirmed-cases-number-card'
        break
      // 検査実施件数
      case 'number-of-tested':
        cardComponent = 'tested-number-card'
        break
      // 陽性者の属性
      case 'attributes-of-confirmed-cases':
        cardComponent = 'confirmed-cases-attributes-card'
        break
      // 年代別陽性患者数
      case 'patients-by-age':
        cardComponent = 'patients-by-age'
        break
      /* // クラスター別陽性患者数
      case 'patients-by-clusters':
        cardComponent = 'patients-by-clusters'
        break
      case 'patients-and-sickbeds':
        cardComponent = 'patients-and-sickbeds' */
    }
    /* eslint-enable simple-import-sort/sort */
    return {
      cardComponent,
      title,
      updatedAt,
    }
  }

  head() {
    const url = 'https://stop-covid19-hyogo.org'
    const timestamp = new Date().getTime()
    const defaultTitle = this.$tc('兵庫県 新型コロナウイルスまとめサイト')
    const ogpImage =
      (this.$i18n.locale ?? 'ja') === 'ja'
        ? `${url}/ogp/${this.$route.params.card}.png?t=${timestamp}`
        : `${url}/ogp/${this.$i18n.locale}/${this.$route.params.card}.png?t=${timestamp}`
    const description = `${this.$t(
      '兵庫県の新型コロナウイルス感染症 (COVID-19) に関する最新情報を提供するために、有志の仲間が開設したまとめサイトです。'
    )} ${this.$t(
      '兵庫県内の感染者数、検査実施件数、入院患者数などをわかりやすく伝えることで、現状を把握して適切な対策を取れるようにすることを目的としています。'
    )}`

    const mInfo: MetaInfo = {
      title: `${
        (this.$data.title ?? '') !== ''
          ? this.$data.title + ' | ' + defaultTitle
          : defaultTitle
      }`,
      link: [
        ...(getLinksLanguageAlternative(
          `cards/${this.$route.params.card}`,
          this.$i18n.locales,
          this.$i18n.defaultLocale
        ) as []),
      ],
      meta: [
        {
          hid: 'og:url',
          property: 'og:url',
          content: `${url}${this.$route.path}/`,
        },
        {
          hid: 'og:title',
          property: 'og:title',
          content: `${
            (this.$data.title ?? '') !== ''
              ? this.$data.title + ' | ' + defaultTitle
              : defaultTitle
          }`,
        },
        {
          hid: 'description',
          name: 'description',
          content: `${this.$t('{date} 更新', {
            date: convertDateToSimpleFormat(this.$data.updatedAt),
          })}: ${description}`,
        },
        {
          hid: 'og:description',
          property: 'og:description',
          content: `${this.$t('{date} 更新', {
            date: convertDateToSimpleFormat(this.$data.updatedAt),
          })}: ${description}`,
        },
        {
          hid: 'og:image',
          property: 'og:image',
          content: `${ogpImage}`,
        },
        {
          hid: 'twitter:image',
          name: 'twitter:image',
          content: `${ogpImage}`,
        },
      ],
    }
    return mInfo
  }
}
</script>
