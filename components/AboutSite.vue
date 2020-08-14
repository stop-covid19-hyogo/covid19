<template>
  <div class="AboutSite">
    <div class="AboutSite-heading">
      <h3 class="AboutSite-title">{{ $t('当サイトについて') }}</h3>
    </div>
    <div class="AboutSite-body">
      <i18n
        tag="p"
        path="当サイトは新型コロナウイルス感染症（COVID-19）に関する最新情報を提供するために、{volunteer}が開設したまとめサイトです。"
      >
        <template v-slot:volunteer>{{ $t('有志の仲間') }}</template>
      </i18n>
      <div class="AboutSite-Button">
        <nuxt-link class="link" to="/about">{{ $t('もっと見る') }}</nuxt-link>
      </div>
    </div>
  </div>
</template>

<style lang="scss">
.AboutSite {
  @include card-container();

  padding: 10px;
  margin-bottom: 20px;

  .AboutSite-heading {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    margin-bottom: 8px;

    .AboutSite-title {
      display: flex;
      padding: 6px;
      align-items: center;
      color: $gray-2;
      @include card-h2();
    }
  }
  .AboutSite-body {
    margin: 5px;
    @include font-size(14);

    .AboutSite-Button {
      flex: 1 0 auto;
      text-align: right;
      > .link {
        text-decoration: none;
        @include button-text('sm');
      }
      @include lessThan($small) {
        margin-top: 4px;
      }
    }
  }
}
</style>
