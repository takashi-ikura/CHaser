# CHaser-Server 高速版

## ソース
chsr_ex.rb

実行方法の例
```sh
ruby chsr_ex.rb
```
詳しくは[起動時のパラメータ]を参照してください。


## 変更内容
**Add 2024/7/27 Takashi Ikura**

結果だけを表示するように修正しました。
Waitのパラメタは無効化しています。

## 内容
**CHaser Server on Ruby (unofficial)**

Rubyで書いた、U-16プログラミングコンテストの競技「CHaser」のサーバープログラムです。
Windowsのコマンドプロンプト、Macのコンソールなどで、Rubyがインストールされている環境で動作します。

## 起動時のパラメタ

```sh
ruby chsr_ex.rb -h
```

で簡単なヘルプが表示されます。

```sh
ruby chsr_ex.rb
```

で map_simple.map というマップファイルを読み込んで起動します。マップファイルを指定するには 

```sh
ruby chsr_ex.rb -m ファイル名
```

とします。

```sh
ruby chsr_ex.rb -w 数字
```

**※wパラメタは無効となっています**

画面表示のウェイトを指定できます（単位は秒）。デフォルトは 0.5 です。

```sh
ruby chsr_ex.rb -p [数字]
```

でポーズモードで起動します。指定したターンごとにEnterの入力を待ちます。数字を省略すると1ターン毎になります。

```sh
ruby chsr_ex.rb -z
```

で全角モードで起動します。Windowsのコマンドプロンプト以外では表示が崩れるようです。

起動後、ポート2009(COOL)、2010(HOT)にクライアントプログラムを接続して、エンターキーでゲーム開始になります。

## ライセンスなど
公式のサーバーと同一の動作を保証するものではありません。

This software is released under the MIT License, see LICENSE.

（このソフトウェアは、MITライセンスのもとで公開されています。LICENSEを見てください。） 

## 大元のリポジトリ

https://github.com/t-akisato/CHaser-Server

## その他

- コミットのコメントの初期値設定
```sh
git config commit.template commit_temp.txt
```

- Emailとユーザ名の設定
```sh
git config --global user.name "あなたの名前"
git config --global user.email "あなたのメールアドレス"
```
