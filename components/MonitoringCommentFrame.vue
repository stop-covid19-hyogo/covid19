<template>
  <div>
    <div
      class="MonitoringCommentFrame"
      :style="{ borderColor: `${colors[level]}` }"
    >
      <p>{{ $t(status) }}</p>
    </div>
    <div
      class="MonitoringCommentFrameAfter"
      :style="{
        borderColor: `${colors[level]}`,
        background: `${colors[level]}`
      }"
    />
  </div>
</template>

<script>
import Vue from 'vue'

export default Vue.extend({
  props: {
    level: {
      type: Number,
      required: true,
      default: 0
    },
    status: {
      type: String,
      required: true,
      default: ''
    }
  },
  data() {
    return {
      colors: ['#5dbaf0', '#96cd5f', '#fdbe40', '#fa1629', '#bababa']
    }
  }
})
</script>

<style lang="scss" scoped>
.MonitoringCommentFrame {
  border: solid 1px;
  text-align: center;
  margin-bottom: 10px;
  > p {
    margin-top: auto;
    margin-bottom: auto;
    position: relative;
    font-style: normal;
    font-weight: bold;
    color: $gray-2;
    padding: 10px 0 10px 0;

    @include font-size(13);
  }
}

.MonitoringCommentFrameAfter {
  margin-top: -11px;
  content: '';
  padding: 7px;
  border: solid 1px;
}
</style>
