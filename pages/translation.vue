<template>
  <div class="Tranlation">
    <page-header class="mb-3">
      {{ $t('翻訳協力者の募集について') }}
    </page-header>
    <static-card>
      <h3>{{ $t('翻訳に協力していただける方を募集しています') }}</h3>
      <p>
        {{
          $t(
            '当サイトでは、今後たくさんの方にこのサイトを見て、自身の行動を考えてもらうために、多言語化対応に向けて動いています。'
          )
        }}<br />
        {{
          $t(
            'それと同時に、このサイトの翻訳を手伝っていただける方を募集します。'
          )
        }}
      </p>
      <p>
        {{ $t('これを機に、当サイトへ少しでも貢献していただければ幸いです。') }}
      </p>
    </static-card>
    <static-card>
      <h3>{{ $t('翻訳の参加方法') }}</h3>
      <p class="StaticCard-Note">
        <span>{{ $t('※') }}</span>
        <span>
          {{
            $t(
              '※ 翻訳への参加はパソコンを前提としています。スマートフォンなどでも可能ですが、ページのレイアウトが違う可能性がありますのでご了承ください。'
            )
          }}
        </span>
      </p>
      <p>
        {{
          $t(
            '当サイトでは、Transifexというサービスを用いて翻訳の管理をしております。'
          )
        }}
      </p>
      <i18n
        tag="p"
        path="翻訳にご協力いただけるという方は、まず以下の手順に従って{transifex}にご登録ください。"
      >
        <template v-slot:transifex>
          <app-link to="https://www.transifex.com/signup/" :icon-size="16">
            {{ $t('Transifex') }}
          </app-link>
        </template>
      </i18n>
      <ol>
        <li>
          {{
            $t(
              'ユーザー名、メールアドレス、パスワードを入力し、サービス規約とプライバシーポリシーに同意のうえでサインアップしましょう。'
            )
          }}
        </li>
        <img :src="$t('transifex.signup')" alt="signup" />
        <li>
          {{
            $t(
              'そのまま進んで、姓、名を入力して部門と肩書を入力してください。'
            )
          }}<br />
          {{
            $t(
              'わからなければ、部門は「Localization」、肩書は「翻訳者」が適当でしょう。'
            )
          }}<br />
          {{
            $t(
              'これらの設定は非公開となっていますので、設定を変えることがなければ公開されることはありません。'
            )
          }}
        </li>
        <img :src="$t('transifex.board')" alt="board" />
        <li>
          {{
            $t(
              '今回は当サイトの翻訳プロジェクトに参加することになりますので、「既存のプロジェクトに参加」を選択して次へ進みましょう。'
            )
          }}
        </li>
        <img :src="$t('transifex.participate')" alt="participate" />
        <li>
          {{
            $t(
              '次に、あなたが翻訳できる言語を入力(複数選択可)し、「始める」ボタンを押して登録は完了です。'
            )
          }}
        </li>
        <img :src="$t('transifex.language')" alt="language" />
        <li>
          {{
            $t(
              'サイトでの設定は終わりましたが、アカウントを完全に有効化できていませんので、入力したメールアドレス宛に送られたメールからアカウントを有効化してください。'
            )
          }}
        </li>
      </ol>
    </static-card>
    <static-card>
      <h3>{{ $t('実際に翻訳する') }}</h3>
      <p>
        {{ $t('Transifexに登録出来たら、実際に翻訳をしてみましょう。') }}
      </p>
      <i18n
        tag="p"
        path="今の状態ではまだ当サイトの翻訳プロジェクトには参加できていないので、{projectPage}にアクセスし、「チームに参加」ボタンをクリックして参加しましょう。"
      >
        <template v-slot:projectPage>
          <app-link
            to="https://www.transifex.com/stop-covid19-hyogo/covid19/"
            :icon-size="16"
          >
            {{ $t('プロジェクトの公開ページ') }}
          </app-link>
        </template>
      </i18n>
      <img :src="$t('transifex.openpage')" alt="openpage" />
      <i18n
        tag="p"
        path="翻訳できる言語を選択したら、{dashboard}にアクセスし、右上の方にある「翻訳」ボタンをクリックしましょう。"
      >
        <template v-slot:dashboard>
          <app-link
            to="https://www.transifex.com/stop-covid19-hyogo/covid19/dashboard/"
            :icon-size="16"
          >
            {{ $t('ダッシュボード') }}
          </app-link>
        </template>
      </i18n>
      <img :src="$t('transifex.dashboard')" alt="dashboard" />
      <p>
        {{
          $t(
            '翻訳言語の選択を求められるので、選択して下さい。いよいよ翻訳に移ります。'
          )
        }}
      </p>
      <img :src="$t('transifex.selectlang')" alt="selectlang" />
      <p>
        {{
          $t(
            '翻訳単語の一覧が出てくるため、この中から翻訳できる単語や文章を選んで、「翻訳文を入力してください」部分に翻訳を打ち込みます。'
          )
        }}
      </p>
      <img :src="$t('transifex.selectphrase')" alt="selectphrase" />
      <p>
        {{
          $t(
            '翻訳が出来たら、「翻訳を保存」ボタンを押すと、翻訳が登録されます。翻訳登録後は、レビュアーによるレビューが行われ、その後サイトに反映されることになります。'
          )
        }}
      </p>
      <img :src="$t('transifex.waitreview')" alt="waitreview" />
    </static-card>
    <static-card>
      <h3>{{ $t('レビュアーになりたい方へ') }}</h3>
      <i18n
        tag="p"
        path="翻訳がするだけではなくてレビューもしたい、もっと貢献したい、という方はぜひ{community}へ参加してください！"
      >
        <template v-slot:community>
          <app-link
            to="https://stop-covid19-hyogo.slack.com/join/shared_invite/zt-dlg7je1f-mKaKwRqadIj6l7dm7wSdKg"
            :icon-size="16"
          >
            {{ $t('コミュニティ(slack)') }}
          </app-link>
        </template>
      </i18n>
      <p>
        {{
          $t(
            'レビュアーになりたい節を伝えていただければ、運営メンバーで検討いたします。'
          )
        }}
      </p>
    </static-card>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import { MetaInfo } from 'vue-meta'

import AppLink from '@/components/AppLink.vue'
import PageHeader from '@/components/PageHeader.vue'
import StaticCard from '@/components/StaticCard.vue'
export default Vue.extend({
  components: {
    PageHeader,
    StaticCard,
    AppLink,
  },
  head(): MetaInfo {
    return {
      title: this.$tc('翻訳協力者の募集について'),
    }
  },
})
</script>
