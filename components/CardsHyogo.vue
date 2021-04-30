<template>
  <cards-lazy-row :rows="rows" />
</template>

<script lang="ts">
/* eslint-disable simple-import-sort/sort -- ブラウザでの表示順に合わせて各 card の component を import する */
import Vue from 'vue'

// 検査陽性者の状況
const ConfirmedCasesDetailsCard = () =>
  import('@/components/cards/ConfirmedCasesDetailsCard.vue')
// 治療中患者数の変化状況
const ChangesPatientsNumberCard = () =>
  import('@/components/cards/ChangesPatientsNumberCard.vue')
// 陽性患者数
const ConfirmedCasesNumberCard = () =>
  import('@/components/cards/ConfirmedCasesNumberCard.vue')
// 検査実施件数
const TestedNumberCard = () => import('@/components/cards/TestedNumberCard.vue')
// 陽性患者の属性
const ConfirmedCasesAttributesCard = () =>
  import('@/components/cards/ConfirmedCasesAttributesCard.vue')
// 年齢別陽性患者数
const PatientsByAge = () => import('@/components/cards/PatientsByAge.vue')
// クラスター別陽性患者数
// const PatientsByClusters = () =>
//   import('@/components/cards/PatientsByClusters.vue')
// 入院患者数と残り病床数
// const PatientsAndSickbeds = () =>
//   import('@/components/cards/PatientsAndSickbeds.vue')
/* eslint-enable simple-import-sort/sort */

export default Vue.extend({
  data() {
    return {
      rows: [
        [ConfirmedCasesDetailsCard, ChangesPatientsNumberCard],
        [ConfirmedCasesNumberCard, TestedNumberCard],
        [ConfirmedCasesAttributesCard, PatientsByAge],
        /* [
          PatientsByClusters,
          PatientsAndSickbeds,
        ], */
      ],
    }
  },
})
</script>

<style lang="scss" scoped>
.AttentionNote {
  margin: 10px 0;
  padding: 12px;
  background-color: $emergency;
  border-radius: 4px;
  color: $gray-2;
  @include font-size(12);

  p {
    margin: 0;
  }
}
</style>
