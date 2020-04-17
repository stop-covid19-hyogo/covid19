<template>
  <v-col cols="12" md="6" class="DataCard">
    <data-view
      :title="$t('検査陽性者の状況')"
      :title-id="'details-of-confirmed-cases'"
      :date="mainSummary.last_update"
    >
      <template v-slot:button>
        <p :class="$style.note">
          {{ $t('（注）チャーター機帰国者、クルーズ船乗客等は含まれていない') }}
          <br />
          {{
            $t('（注）「入院中」には、入院調整中・宿泊療養に移行した方を含む')
          }}
        </p>
      </template>
      <confirmed-cases-details-table
        :aria-label="$t('検査陽性者の状況')"
        v-bind="confirmedCases"
      />
      <template v-slot:footer>
        <open-data-link
          :url="'http://open-data.pref.hyogo.lg.jp/?page_id=141'"
        />
      </template>
    </data-view>
  </v-col>
</template>

<style lang="scss" module>
.note {
  margin-top: 10px;
  margin-bottom: 0;
  font-size: 12px;
  color: $gray-3;
}
</style>

<script>
import mainSummary from '@/data/main_summary.json'
import formatConfirmedCases from '@/utils/formatConfirmedCases'
import DataView from '@/components/DataView.vue'
import ConfirmedCasesDetailsTable from '@/components/ConfirmedCasesDetailsTable.vue'
import OpenDataLink from '@/components/OpenDataLink'

export default {
  components: {
    DataView,
    ConfirmedCasesDetailsTable,
    OpenDataLink
  },
  data() {
    // 検査陽性者の状況
    const confirmedCases = formatConfirmedCases(mainSummary)

    const data = {
      mainSummary,
      confirmedCases
    }
    return data
  }
}
</script>
