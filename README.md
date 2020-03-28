# 兵庫県非公式 新型コロナウイルスまとめサイト

![](https://github.com/stop-covid19-hyogo/covid19/workflows/production%20deploy/badge.svg)

[![兵庫県非公式 新型コロナウイルスまとめサイト](https://user-images.githubusercontent.com/43156990/77025400-53e94080-69d4-11ea-9978-18c715f4925d.png)](https://stop-covid19-hyogo.org/)

<!--
### 日本語 | [English](./docs/en/README.md) | [Español](./docs/es/README.md) | [한국어](./docs/ko/README.md) | [繁體中文](./docs/zh_TW/README.md) | [简体中文](./docs/zh_CN/README.md) | [Tiếng Việt](./docs/vi/README.md) | [ภาษาไทย](./docs/th/README.md) | [Français](./docs/fr/README.md)
-->

## 貢献の仕方

### コミュニケーションについて

Slack でディスカッションを行っております。

サイト制作にご協力頂ける方であれば誰でも参加可能です。[ここ](https://join.slack.com/t/stop-covid19-hyogo/shared_invite/zt-cq8r7q3a-Pr4UyYDeKjyr8z4N6HbwLg)からご参加下さい。

コミュニケーションにあたっては、Code for Japan の [行動規範](https://github.com/codeforjapan/codeofconduct) もご確認ください。

### 行動原則

[サイト構築にあたっての行動原則](./.github/CODE_OF_CONDUCT.md)を御覧ください。

## 東京都オリジナルから派生した他のサイト

[Link先](./FORKED_SITES.md)を御覧ください。

## 開発者向け情報

サイト制作・開発に関する詳細は[プロジェクトへの参加方法](./.github/CONTRIBUTING.md)をご確認下さい。

### 環境構築手順

- 必要となるNode.jsのバージョン: 10.19.0以上

**yarn を使う場合**
```bash
# install dependencies
$ yarn install

# serve with hot reload at localhost:3000
$ yarn dev
```

**docker compose を使う場合**
```bash
# serve with hot reload at localhost:3000
$ docker-compose up --build
```

**Vagrant を使う場合**
```bash
# serve with hot reload at localhost:3000
$ vagrant up
```

### `Cannot find module ****` と怒られた時

**yarn を使う場合**
```bash
$ yarn install
```

**docker compose を使う場合**
```bash
$ docker-compose run --rm app yarn install
```

### 本番環境/その他の判定

`process.env.GENERATE_ENV` の値が、本番の場合は`'production'`に、それ以外の場合は `'development'` になっています。  
テスト環境のみで実行したい処理がある場合はこちらの値をご利用ください。


### CONTRIBUTORS.md への追加について

[CONTRIBUTORS.md](./CONTRIBUTORS.md) はご協力いただいた皆様を紹介するためのファイルです。

サイト制作に関わったエンジニアやデザイナーはもちろん、制作には関わらないけど貢献していただいた方々もご紹介できればと思ってます。何かしらの貢献を行った方はぜひ追記をお願いします。

追加をご希望の場合は Pull Request を送っていただくか、この [Issue](https://github.com/stop-covid19-hyogo/covid19/issues/60) にコメントをお願いします。

## ライセンス

本ソフトウェアは、[MITライセンス](./LICENSE.txt)の元提供されています。
