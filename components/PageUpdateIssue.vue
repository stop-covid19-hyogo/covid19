<template>
  <div class="PageUpdateIssue">
    <div class="PageUpdateIssue-heading">
      <h3 class="PageUpdateIssue-title">
        <v-icon size="2.4rem" class="PageUpdateIssue-title-icon">
          {{ mdiAlert }}
        </v-icon>
        {{ $t('ページデータ更新停止について') }}
      </h3>
    </div>
    <div class="PageUpdateIssue-body">
      <p>
        {{
          $t(
            '兵庫県が公開するオープンデータの形式が大幅に変更され、対応に時間がかかっています。'
          )
        }}
        {{ $t('ご迷惑をおかけしますが、対応までしばらくお待ちください。') }}
      </p>
    </div>
  </div>
</template>

<script lang="ts">
import { mdiAlert } from '@mdi/js'
import Vue from 'vue'

export default Vue.extend({
  data() {
    return {
      mdiAlert,
    }
  },
})
</script>

<style lang="scss">
.PageUpdateIssue {
  background-color: #f99;
  box-shadow: $shadow;
  border: 0.5px solid #f55 !important;
  border-radius: 4px;
  padding: 10px;
  margin-bottom: 20px;

  .PageUpdateIssue-heading {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    margin-bottom: 8px;

    .PageUpdateIssue-title {
      display: flex;
      padding: 6px;
      align-items: center;
      color: $gray-1;
      @include card-h2();
      &-icon {
        margin: 3px;
      }
    }
  }
  .PageUpdateIssue-body {
    margin: 5px;
    @include font-size(14);

    .PageUpdateIssue-Button {
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
