<template>
  <div>
    <confirmed-cases-details-card
      v-if="this.$route.params.card == 'details-of-confirmed-cases'"
    />
    <!--<tested-cases-details-card
      v-else-if="this.$route.params.card == 'details-of-tested-cases'"
    />-->
    <confirmed-cases-number-card
      v-else-if="this.$route.params.card == 'number-of-confirmed-cases'"
    />
    <!--<confirmed-cases-by-municipalities-card
      v-else-if="
        this.$route.params.card == 'number-of-confirmed-cases-by-municipalities'
      "
    />-->
    <confirmed-cases-attributes-card
      v-else-if="this.$route.params.card == 'attributes-of-confirmed-cases'"
    />
    <tested-number-card
      v-else-if="this.$route.params.card == 'number-of-tested'"
    />
    <!--<inspection-persons-number-card
      v-else-if="this.$route.params.card == 'number-of-inspection-persons'"
    />
    <telephone-advisory-reports-number-card
      v-else-if="
        this.$route.params.card ==
          'number-of-reports-to-covid19-telephone-advisory-center'
      "
    />
    <consultation-desk-reports-number-card
      v-else-if="
        this.$route.params.card ==
          'number-of-reports-to-covid19-consultation-desk'
      "
    />
    <metro-card
      v-else-if="
        this.$route.params.card == 'predicted-number-of-toei-subway-passengers'
      "
    />
    <agency-card v-else-if="this.$route.params.card == 'agency'" />-->
    <patients-by-age v-else-if="this.$route.params.card == 'patients-by-age'" />
    <patients-by-clusters
      v-else-if="this.$route.params.card == 'patients-by-clusters'"
    />
    <!-- <patients-and-sickbeds
      v-else-if="this.$route.params.card == 'patients-and-sickbeds'"
    /> -->
  </div>
</template>

<script>
/* import Data from '@/data/data.json'
import MetroData from '@/data/metro.json'
import agencyData from '@/data/agency.json'
import patientData from '@/data/patient.json' */
import patients from '@/data/patients.json'
import inspectionsSummary from '@/data/inspections_summary.json'
import age from '@/data/age.json'
import clustersSummary from '@/data/clusters_summary.json'
// import sickbedsSummary from '@/data/sickbeds_summary.json'
import ConfirmedCasesDetailsCard from '@/components/cards/ConfirmedCasesDetailsCard.vue'
// import TestedCasesDetailsCard from '@/components/cards/TestedCasesDetailsCard.vue'
import ConfirmedCasesNumberCard from '@/components/cards/ConfirmedCasesNumberCard.vue'
import ConfirmedCasesAttributesCard from '@/components/cards/ConfirmedCasesAttributesCard.vue'
// import ConfirmedCasesByMunicipalitiesCard from '@/components/cards/ConfirmedCasesByMunicipalitiesCard.vue'
import TestedNumberCard from '@/components/cards/TestedNumberCard.vue'
/* import InspectionPersonsNumberCard from '@/components/cards/InspectionPersonsNumberCard.vue'
import TelephoneAdvisoryReportsNumberCard from '@/components/cards/TelephoneAdvisoryReportsNumberCard.vue'
import ConsultationDeskReportsNumberCard from '@/components/cards/ConsultationDeskReportsNumberCard.vue'
import MetroCard from '@/components/cards/MetroCard.vue'
import AgencyCard from '@/components/cards/AgencyCard.vue' */
import PatientsByAge from '@/components/cards/PatientsByAge.vue'
import PatientsByClusters from '@/components/cards/PatientsByClusters.vue'
// import PatientsAndSickbeds from '@/components/cards/PatientsAndSickbeds.vue'
import { convertISO8601FormatToDatetime } from '@/utils/formatDate'

export default {
  components: {
    ConfirmedCasesDetailsCard,
    // TestedCasesDetailsCard,
    ConfirmedCasesNumberCard,
    ConfirmedCasesAttributesCard,
    // ConfirmedCasesByMunicipalitiesCard,
    TestedNumberCard,
    /* InspectionPersonsNumberCard,
    TelephoneAdvisoryReportsNumberCard,
    ConsultationDeskReportsNumberCard,
    MetroCard,
    AgencyCard */
    PatientsByAge,
    PatientsByClusters
    // PatientsAndSickbeds
  },
  data() {
    let title, updatedAt
    switch (this.$route.params.card) {
      case 'details-of-confirmed-cases':
        title = this.$t('検査陽性者の状況')
        updatedAt = inspectionsSummary.last_update
        break
      /* case 'details-of-tested-cases':
        title = this.$t('検査実施状況')
        updatedAt = Data.inspection_status_summary.date
        break */
      case 'number-of-confirmed-cases':
        title = this.$t('陽性患者数')
        updatedAt = patients.last_update
        break
      /* case 'number-of-confirmed-cases-by-municipalities':
        title = this.$t('陽性患者数（区市町村別）')
        updatedAt = patientData.date
        break */
      case 'attributes-of-confirmed-cases':
        title = this.$t('陽性患者の属性')
        updatedAt = patients.last_update
        break
      case 'number-of-tested':
        title = this.$t('検査実施件数')
        updatedAt = inspectionsSummary.last_update
        break
      /* case 'number-of-inspection-persons':
        title = this.$t('検査実施人数')
        updatedAt = Data.inspection_persons.date
        break
      case 'number-of-reports-to-covid19-telephone-advisory-center':
        title = this.$t('新型コロナコールセンター相談件数')
        updatedAt = Data.contacts.date
        break
      case 'number-of-reports-to-covid19-consultation-desk':
        title = this.$t('新型コロナ受診相談窓口相談件数')
        updatedAt = Data.querents.date
        break
      case 'predicted-number-of-toei-subway-passengers':
        title = this.$t('都営地下鉄の利用者数の推移')
        updatedAt = MetroData.date
        break
      case 'agency':
        title = this.$t('都庁来庁者数の推移')
        updatedAt = agencyData.date
        break */
      case 'patients-by-age':
        title = this.$t('年代別陽性患者数')
        updatedAt = age.last_update
        break
      case 'patients-by-clusters':
        title = this.$t('クラスター別陽性患者数')
        updatedAt = clustersSummary.last_update
        break
      /* case 'patients-and-sickbeds':
        title = this.$t('入院患者数と残り病床数')
        updatedAt = sickbedsSummary.last_update
        break */
    }

    const updatedTimeStr = convertISO8601FormatToDatetime(updatedAt)
    const data = {
      title,
      updatedTimeStr
    }
    return data
  },
  head() {
    const url = 'https://stop-covid19-hyogo.org'
    const timestamp = new Date().getTime()
    const ogpImage =
      this.$i18n.locale === 'ja'
        ? `${url}/ogp/${this.$route.params.card}.png?t=${timestamp}`
        : `${url}/ogp/${this.$i18n.locale}/${this.$route.params.card}.png?t=${timestamp}`
    const description = `${this.$t(
      '兵庫県の新型コロナウイルス感染症 (COVID-19) に関する最新情報を提供するために、有志の仲間が開設したまとめサイトです。'
    ) +
      this.$t(
        '兵庫県内の感染者数、検査実施件数、入院患者数などをわかりやすく伝えることで、現状を把握して適切な対策を取れるようにすることを目的としています。'
      )}`

    return {
      title: this.title,
      meta: [
        {
          hid: 'og:url',
          property: 'og:url',
          content: url + this.$route.path + '/'
        },
        {
          hid: 'og:title',
          property: 'og:title',
          content:
            this.title +
            ' | ' +
            this.$t('兵庫県非公式') +
            ' ' +
            this.$t('新型コロナウイルス') +
            this.$t('まとめサイト')
        },
        {
          hid: 'description',
          name: 'description',
          content: description
        },
        {
          hid: 'og:description',
          property: 'og:description',
          content: description
        },
        {
          hid: 'og:image',
          property: 'og:image',
          content: ogpImage
        },
        {
          hid: 'twitter:image',
          name: 'twitter:image',
          content: ogpImage
        }
      ]
    }
  }
}
</script>
