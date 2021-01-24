<template>
  <!--<div v-scroll="onScroll" class="MainPage">-->
  <div class="MainPage">
    <div class="Header mb-3">
      <page-header :icon-path="headerItem.iconPath">{{
        headerItem.title
      }}</page-header>
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
    <monitoring-comment-card />
    <!--<lazy-tokyo-alert-card v-if="TokyoAlert.alert" />
    <lazy-static-info
      v-if="$vuetify.breakpoint.smAndUp || showStaticInfo"
      class="mb-4"
      :url="'https://www.fukushihoken.metro.tokyo.lg.jp/iryo/kansen/coronasodan.html'"
      :text="$t('自分や家族の症状に不安や心配があればまずは電話相談をどうぞ')"
      :btn-text="$t('相談の手順を見る')"
    />-->
  </div>
</template>

<script lang="ts">
import { mdiChartTimelineVariant } from '@mdi/js'
import Vue from 'vue'
import { MetaInfo } from 'vue-meta'

import AboutSite from '@/components/AboutSite.vue'
import MonitoringCommentCard from '@/components/MonitoringCommentCard.vue'
import PageHeader from '@/components/PageHeader.vue'
import WhatsNew from '@/components/WhatsNew.vue'
import lastUpdate from '@/data/last_update.json'
// import Data from '@/data/data.json'
import News from '@/data/news.json'
// import TokyoAlert from '@/data/tokyo_alert.json'
import { convertISO8601FormatToDatetime } from '@/utils/formatDate'

export default Vue.extend({
  components: {
    PageHeader,
    AboutSite,
    WhatsNew,
    MonitoringCommentCard,
  },
  data() {
    // const { lastUpdate } = Data

    return {
      // TokyoAlert,
      headerItem: {
        iconPath: mdiChartTimelineVariant,
        title: this.$t('兵庫県内の最新感染動向'),
      },
      lastUpdate,
      newsItems: News.newsItems,
      // showStaticInfo: false,
    }
  },
  computed: {
    updatedAt() {
      return convertISO8601FormatToDatetime(lastUpdate.last_update)
    },
    formattedDateForDisplay() {
      return `${this.$d(new Date(lastUpdate.last_update), 'dateTime')} JST`
    },
  },
  /* methods: {
    onScroll() {
      this.showStaticInfo = true
    },
  }, */
  head(): MetaInfo {
    return {
      title: this.$tc('兵庫県 新型コロナウイルスまとめサイト'),
      titleTemplate: '',
    }
  },
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
