# Guess-the-number-game

## 🌱概要
数当てゲーム

## ✨デモ


## 📝説明
自身の指定した最小値〜最大値の範囲内でランダムに決定される数値の数を当てるゲーム。
回答制限回数は５回まで。

## 🧰前提条件

### Git
Gitがインストールされていない場合は、下記手順でインストールしてください。

1. ターミナルを起動する。<br>使用するOSによりターミナルの名称が異なりますので注意してください。<br>(例. Windows:コマンドプロンプト,mac:ターミナル)

2. Gitがインストールされているか確認する。<br>`git version 2.34.1` のように表示された場合は、Gitがインストールされています。<br>以降の手順はスキップしてください。<br>**また、ターミナルは引き続き使用しますので開いたままにしてください!**
```
git --version
```

3. システムを更新する
```
sudo apt-get update
```

4. Gitをインストールする
```
sudo apt install git
```

5. Gitがインストールされたことを確認する。<br>`git version 2.34.1` のように表示されていれば、Gitのインストールは完了です!
```
git --version
```

### Python 3.x
[Python](https://www.python.org/downloads/)の公式サイトからあなたのPCのOSに合わせて、ダウンロードしてください。

ダウンロードしたファイルを使用してインストールできます。

Pythonがインストールされているかは、下記コマンドで確認することができます。

`Python 3.10.12`のように表示されていれば、Pythonはインストールされています。

```
python3 --version
```

## 🙋使用例
一通りの手順のイメージは[デモ](#デモ)を参考にしてください。

## 💾使用技術
<table>
<tr>
  <th>カテゴリ</th>
  <th>技術スタック</th>
</tr>
<tr>
  <td>開発言語</td>
  <td>Python</td>
</tr>
<tr>
  <td rowspan=2>インフラ</td>
  <td>Ubuntu</td>
</tr>
<tr>
  <td>VirtualBox</td>
</tr>
<tr>
  <td rowspan=2>その他</td>
  <td>Git</td>
</tr>
<tr>
  <td>Github</td>
</tr>
</table>

## 📜作成の経緯
⭐️後で記載する!!!

作成した理由を記載する。

## ⭐️こだわった点
 - guess_number_game()として再利用可能な部品化
 - get_input(),get_random_numberも関数化し、再利用性の向上、可読性向上、デバックの容易化、詳細な処理を隠蔽し処理を抽象化することでメインロジックが簡潔になる
 - 「=」や「>」の左右の余白
 - ユーザーへのプロンプトメッセージを改善し、何回目の試行かが明確にわかるようにした。
 - while Trueループを追加し、ゲーム終了後に再プレイするかどうかをユーザーに尋ねる機能を追加しました。

テキストや参考にした記事などを再度読み返して技術の理解を深めてから書く。

ここがエンジニアに一番読んでもらいたい箇所なのでできるだけ詳細に書く。



## 📑参考文献
### 公式ドキュメント
- [Python](https://docs.python.org/ja/3/)
