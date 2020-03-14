# プロジェクトへの参加方法

本プロジェクトにご協力いただきありがとうございます。

プロジェクトの責任者をしています、大山と申します。何か質問があれば、Slack 等でお気軽に質問してください。プロジェクトへの参加方法をお伝えいたします。

なお、わかりやすい簡単な修正をスポット的に行うだけであれば、自分のリポジトリに Fork をして、修正版を Pull Request いただいても問題ございません。

開発に参加する前に、[プロジェクトの行動規範](CODE_OF_CONDUCT.md) をご一読ください。

## コミュニケーションについて

本プロジェクト用のチャットを Slack にて準備しております。サイト制作にご協力頂ける方であれば誰でも参加可能です。[こちら](https://join.slack.com/t/stop-covid19-hyogo/shared_invite/zt-cq8r7q3a-Pr4UyYDeKjyr8z4N6HbwLg)からご参加下さい。

また、コミュニケーションにあたっては、Code for Japan の [行動規範](https://github.com/codeforjapan/codeofconduct) もご確認ください。

## プロジェクトの進め方について

GitHub の [Project](https://github.com/stop-covid19-hyogo/covid19/projects/1) をつかって、対応すべき Issue とその進捗を管理しています。

自分ができそうな Issue に誰もアサインされていない場合、Issue に「やります！」等とコメントしてから開発をはじめてください。

### Issue へのコメントや Pull Request について

- Issue へのコメントはご自由にどうぞ！新しい質問や提案なども受け付けます
- Issue を追加する場合、必ず既に同様の Issue が無いか検索をしてから作成してください
- improve(改善提案)がついたIssueについては必ず反映できると限りませんのでご了承ください（特にUI系について）
- good first issue / help wanted / bug を優先して対応いただけると助かります
- わかりやすい簡単な修正をスポット的に行うだけであれば、自分のリポジトリに Fork をして、修正版を Pull Request いただいてもかまいません。

### 注意事項

- 半日以上作業から離れそうな場合は、他の人が作業を引き継げるようにしておいてください。（Issue を抱えたまま長時間オフになると、そのIssueがブロックされてしまいます。）
- 1日以上更新されない Issue については、当方で assign を外させていただくことがあります。作業途中でも、[Draft Pull Request](https://qiita.com/tatane616/items/13da1b6797a7b871ad58) を送ってもらえると、動きが把握しやすくなります。
- Issue に関連した質問等は、Slack より Issue 内のコメントを活用しましょう
- 提案なども受け付けます！積極的に新しく Issue を作ってください。

## ブランチ運用について

東京都版とは異なり `development` ブランチのみを使用して開発を行っています。

`master` `staging` などのブランチは使用しておりません。

- development: 開発用のブランチです
- dev-page: 開発環境 (development) のコンテンツを格納するブランチです
- stg-page: 検証環境 (staging) のコンテンツを格納するブランチです
- prod-page: 本番環境のコンテンツを格納するブランチです（検討中）

## 各種環境とデプロイについて

本プロジェクトでは以下の環境が存在します。

### development / 開発環境

https://dev-covid19-hyogo.netlify.com/

Password: `stop.covid19.hyogo`

最新の開発状況が反映される環境です。 `development` ブランチを更新すると CI/CD が実行されサーバーのコンテンツを更新します。

サーバーには[Netlify](https://www.netlify.com/) を使用しています。

### staging / 検証環境

https://stg-covid19-hyogo.netlify.com/

Password: `stop.covid19.hyogo`

本番リリース前の確認を行うための環境です。 `v[0-9]+.[0-9]+.[0-9]+-staging.[0-9]+` という形式でタグを付けると CI/CD が実行されサーバーのコンテンツを更新します。

- タグの例
    - `v0.1.0-staging.1`
    - `v1.0.0-staging.3`

なお、GitHub のリリース機能ではタグを付けることができません。間違わないよう注意して下さい。

サーバーには[Netlify](https://www.netlify.com/) を使用しています。

### production / 本番環境

本番環境です。 GitHub で[リリース](https://github.com/stop-covid19-hyogo/covid19/releases)すると CI/CD が実行されサーバーのコンテンツを更新します。

サーバーには AWS を使用しています。

## 各種リソースについて

### デザインデータ

サイトで使用するデザインデータは Figma を使用して制作しています。[こちら](https://www.figma.com/files/recent)をご覧下さい。

本ドキュメントの更新も大歓迎です！
