<template>
  <div class="MainPage">
    <div class="Header mb-3">
      <page-header :icon="headerItem.icon">{{ headerItem.title }}</page-header>
      <div class="UpdatedAt">
        <span>{{ $t('最終更新') }}</span>
        <time :datetime="updatedAt">{{ formattedDateForDisplay }}</time>
      </div>
      <div
        v-show="!['ja', 'ja-basic'].includes($i18n.locale)"
        class="Annotation"
      >
        <span>{{ $t('注釈') }}</span>
      </div>
    </div>
    <about-site />
    <whats-new class="mb-4" :items="newsItems" :is-emergency="false" />
    <!--<monitoring-comment-card />
    <tokyo-alert-card v-if="TokyoAlert.alert" />
    <static-info
      class="mb-4"
      :url="localePath('/flow')"
      :text="$t('自分や家族の症状に不安や心配があればまずは電話相談をどうぞ')"
      :btn-text="$t('相談の手順を見る')"
    />-->
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import { MetaInfo } from 'vue-meta'
import PageHeader from '@/components/PageHeader.vue'
import AboutSite from '@/components/AboutSite.vue'
import WhatsNew from '@/components/WhatsNew.vue'
/* import StaticInfo from '@/components/StaticInfo.vue'
import TokyoAlertCard from '@/components/TokyoAlertCard.vue'
import MonitoringCommentCard from '@/components/MonitoringCommentCard.vue' */
import lastUpdate from '@/data/last_update.json'
import News from '@/data/news.json'
// import TokyoAlert from '@/data/tokyo_alert.json'
import { convertISO8601FormatToDatetime } from '@/utils/formatDate'

export default Vue.extend({
  components: {
    PageHeader,
    AboutSite,
    WhatsNew
    /* StaticInfo,
    TokyoAlertCard,
    MonitoringCommentCard */
  },
  data() {
    return {
      lastUpdate,
      // TokyoAlert,
      headerItem: {
        icon: 'mdi-chart-timeline-variant',
        title: this.$t('兵庫県内の最新感染動向')
      },
      newsItems: News.newsItems
    }
  },
  computed: {
    updatedAt() {
      return convertISO8601FormatToDatetime(lastUpdate.last_update)
    },
    formattedDateForDisplay() {
      return this.$d(new Date(lastUpdate.last_update), 'dateTime')
    }
  },
  head(): MetaInfo {
    return {
      title: this.$tc('兵庫県 新型コロナウイルスまとめサイト'),
      titleTemplate: '',
      __dangerouslyDisableSanitizers: ['script'],
      script: [
        {
          innerHTML: `{
            "@context": "https://schema.org",
            "@type": "SpecialAnnouncement",
            "name": "兵庫県内の新型コロナウイルス感染動向",
            "text": "兵庫県内における新型コロナウイルスの陽性患者数や属性、PCR検査数などをお知らせしています。",
            "url": "https://stop-covid19-hyogo.org/",
            "datePosted": "2020-05-05T00:00",
            "spatialCoverage": [
              {
                "@context":"https://schema.org/",
                "@type": "AdministrativeArea",
                "name": "兵庫県"
              }
            ],
            "category": "https://www.wikidata.org/wiki/Q81068910",
            "diseaseSpreadStatistics" : [
              {
                "@type": "Dataset",
                "name": "兵庫県 新型コロナウイルス陽性者の状況（推移）",
                "description": "兵庫県が公式に発表した、検査実施人数（累計）、陽性者数（累計）、入院中、中等症以下、重症、死亡（累計）、退院（累計）の推移データ。",
                "sameAs": "http://open-data.pref.hyogo.lg.jp/?page_id=141",
                "license": "https://creativecommons.org/licenses/by/4.0/deed.ja",
                "distribution": {
                  "@type": "DataDownload",
                  "contentUrl": "https://web.pref.hyogo.lg.jp/kk03/documents/yousei.xlsx",
                  "encodingFormat": "xlsx"
                }
              },
              {
                "@type": "Dataset",
                "name": "兵庫県 新型コロナウィルス感染症の県内検査状況",
                "description": "兵庫県が公式に発表した、新型コロナウイルスのPCR検査件数と、その検査における陽性確認件数のデータ。",
                "sameAs": "http://open-data.pref.hyogo.lg.jp/?page_id=141",
                "license": "https://creativecommons.org/licenses/by/4.0/deed.ja",
                "distribution": {
                  "@type": "DataDownload",
                  "contentUrl": "https://web.pref.hyogo.lg.jp/kk03/documents/pcr.xlsx",
                  "encodingFormat": "xlsx"
                }
              },
              {
                "@type": "Dataset",
                "name": "兵庫県 新型コロナウィルスに感染した患者の状況",
                "description": "兵庫県が公式に発表した、新型コロナウイルス感染者の属性（年代、性別、居住地、職業、発症日など）データ。",
                "sameAs": "http://open-data.pref.hyogo.lg.jp/?page_id=141",
                "license": "https://creativecommons.org/licenses/by/4.0/deed.ja",
                "distribution": {
                  "@type": "DataDownload",
                  "contentUrl": "https://web.pref.hyogo.lg.jp/kk03/corona_kanjyajyokyo.html",
                  "encodingFormat": "text/html"
                }
              }
            ]
          }`,
          type: 'application/ld+json'
        }
      ]
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
}
</style>
