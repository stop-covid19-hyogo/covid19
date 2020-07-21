<template>
  <div>
    <card-row class="DataBlock">
      <!-- 検査陽性者の状況 -->
      <confirmed-cases-details-card />
      <!-- 治療中患者数の変化状況 -->
      <changes-patients-number-card />
      <!-- 陽性患者数 -->
      <confirmed-cases-number-card />
      <!-- 検査実施件数 -->
      <tested-number-card />
      <!-- 陽性患者の属性 -->
      <confirmed-cases-attributes-card />
      <!-- 年代別陽性患者数 -->
      <patients-by-age />
      <!-- クラスター別陽性患者数 -->
      <patients-by-clusters />
      <!-- 入院患者数と残り病床数 -->
      <!--<patients-and-sickbeds />-->
    </card-row>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import CardRow from '@/components/cards/CardRow.vue'
import ConfirmedCasesDetailsCard from '@/components/cards/ConfirmedCasesDetailsCard.vue'
import ChangesPatientsNumberCard from '@/components/cards/ChangesPatientsNumberCard.vue'
import ConfirmedCasesNumberCard from '@/components/cards/ConfirmedCasesNumberCard.vue'
import TestedNumberCard from '@/components/cards/TestedNumberCard.vue'
import ConfirmedCasesAttributesCard from '@/components/cards/ConfirmedCasesAttributesCard.vue'
import PatientsByAge from '@/components/cards/PatientsByAge.vue'
import PatientsByClusters from '@/components/cards/PatientsByClusters.vue'
// import PatientsAndSickbeds from '@/components/cards/PatientsAndSickbeds.vue'

export default Vue.extend({
  components: {
    CardRow,
    ConfirmedCasesDetailsCard,
    ChangesPatientsNumberCard,
    ConfirmedCasesNumberCard,
    TestedNumberCard,
    ConfirmedCasesAttributesCard,
    PatientsByAge,
    PatientsByClusters
    // PatientsAndSickbeds
  }
})
</script>

<style lang="scss" scoped>
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
</style>
