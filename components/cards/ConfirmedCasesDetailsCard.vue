<template>
  <v-col cols="12" md="6" class="DataCard">
    <data-view
      :title="$t('検査陽性者の状況')"
      :title-id="'details-of-confirmed-cases'"
      :date="mainSummary.last_update"
    >
      <template v-slot:description>
        <ul class="ListStyleNone">
          <li>
            {{
              $t('（注）チャーター機帰国者、クルーズ船乗客等は含まれていない')
            }}
          </li>
          <!--<li>
            {{
              $t(
                '（注）「重症」は、集中治療室（ICU）等での管理又は人工呼吸器管理が必要な患者数を計上'
              )
            }}
          </li>
          <li>
            {{
              $t(
                '（注）退院者数の把握には一定の期間を要しており、確認次第数値を更新している'
              )
            }}
          </li>-->
        </ul>
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

    return {
      mainSummary,
      confirmedCases
    }
  }
}
</script>
