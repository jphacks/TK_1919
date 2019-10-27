# Unagi-Recommendation うなレコ
![うなぎレコメンデーション](https://github.com/jphacks/TK_1919/blob/master/readme_images/logo.png "Unagi-recomendation")
# Demo
[![デモムービー](image.png)](https://youtu.be/c4XjRWWVmU8)

## 目次
- [製品概要](#製品概要)
- [背景](#背景)
- [使い方](#使い方)
- [特長](#特長)
- [解決出来ること](#解決出来ること)
- [今後の展望](#今後の展望)
- [開発内容](#開発内容)
- [活用した技術](#活用した技術)
- [独自開発技術-ハックデイで開発したもの](#独自開発技術-ハックデイで開発したもの)

## 製品概要
### Travel × Tech
![トラベルテック](https://github.com/jphacks/TK_1919/blob/master/readme_images/travelTech.png "TravelTech")


### 背景
 台風19号で結構前から準備をしていた学科旅行が消えて悲しかった。もう一度、全員の好みを聞いて調整するのはめんどくさい。
どこに旅行に行きたいかを決めるのが、すぐにはわからない上に、時間がかかるのが問題点。実際
にははっきりとどこに行きたいかがわかっている人はほとんどいないので、その時の気分で選んで
いる。
 気分で選んでいるのに、比較する観光地は自分がよく知っている観光地に限られてしまう。
 ↓
 自分の旅行先の気分や好みを読み取ってマッチした観光地をリコメンドしてくれるサービスを作れば良い

### 製品概要
 うなレコは視線推定の技術を使って、あなたの好みにあった旅行先をリコメンドするサービスです
 長ったらしい文章を読むことなく、ハンズフリーで30秒ほどの時間で診断は完了するので、あなたは好きな時間に旅行先を決めることができます。
 一緒に旅行する友達にやってもらうことも簡単です。


### 使い方
#### 1. あなたの好みを測るために、２つの写真のペアが１５組現れます。好きな写真の方をみてください
![操作方法](https://github.com/jphacks/TK_1919/blob/master/fig_ReadMe/%E6%93%8D%E4%BD%9C%E6%96%B9%E6%B3%95.png "screenImages")
![操作方法1](https://github.com/jphacks/TK_1919/blob/master/fig_ReadMe/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202019-10-27%2013.34.29.png "screenImages1")
#### 2. 写真の選び方から、あなたが今本当に行くべき旅行先を提案します
![操作方法2](https://github.com/jphacks/TK_1919/blob/master/fig_ReadMe/screenImage.png "screenImages2")
#### 3. グループで旅行する場合は、グループの満足度を最大化するような旅行先を提案します
![操作方法3](https://github.com/jphacks/TK_1919/blob/master/fig_ReadMe/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202019-10-27%2013.35.59.png "screenImages3")

### 特長

#### 1. 特長1
タイピング、クリック不要!
ただ、気になる方の写真をみるだけで旅行先を提案できます！

![操作方法4](https://github.com/jphacks/TK_1919/blob/master/fig_ReadMe/%E3%83%9E%E3%82%A6%E3%82%B9%E3%83%BB%E3%82%AD%E3%83%BC%E3%83%9C%E3%83%BC%E3%83%89%E3%81%AA%E3%81%97.png "screenImages3")
#### 2. 特長2
提案された旅行先の観光情報や写真がページから見れるので、旅行先の決定を迅速に行えます！
#### 3. 特徴3
提案された旅行先の情報は自分で調べることなく、自動で表示されます！
#### 4. 特長4
ぼっち旅行だけでなく、グループでの旅行にも対応しています！

### 解決出来ること

* タイピング、クリック不要なので、手が不自由な方や、使いづらい状態でも使用できます
* 自分で旅行先の情報を調べて比較することなく、ユーザーは潜在的な嗜好から旅行先を自動で選ぶことができます
* 検索ではなかなか出てこないようなマイナーな観光地の情報も得ることができます
* 旅行先を複数人で決める際に、意見が別れて時間がかかりますが「うなレコ」なら複数人でも一瞬で旅行先を決めることが出来ます。

### 今後の展望
* 現在は診断された結果に対して、観光地の画像と観光情報を乗せているだけですが、宿の情報や旅行サイトの口コミ情報も表示する
* アフィリエイトのリンクを貼って収益化を可能にする

## 開発内容
* AWSを用いてサーバーレスな構成にすることで、オートスケールを実現しスケーラブルなシステムを開発した、
* SSL通信を実現し、画像のプライバシーに考慮した通信を行った
* ユーザーの好みを画像に向ける視線によって取得できるようにした
* ユーザーの好みに一致した観光地をリコメンドするシステムの開発
* 観光地の画像や観光情報をスクレイピングにより取得
* ユーザーの好みとマッチする観光地の特性を表現する文章を自動生成
* 複数人での旅行プラン作成に寄与するために、全員の満足度が高く、かつ、特定の人の負担が大きくなりすぎるとエラーを出すようなシステムを開発した


### 活用した技術

#### API-データ
今回スポンサーから提供されたAPI、製品などの外部技術があれば記述をして下さい。

* NEC 遠隔視線推定技術API
* AWS(S3,Lambda,Crowd Front,API geteway,root 53)

#### フレームワーク-ライブラリ-モジュール
* Jquery
* python
* JS
* BeautiuflSoup

#### デバイス
* PC(Webブラウザ)

### 独自開発技術-ハックデイで開発したもの

#### 2日間に開発した独自の機能技術

* 機械学習による満足度の最大化モデルの開発
* 観光地紹介文の自動生成
