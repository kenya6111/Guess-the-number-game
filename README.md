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

### pip
pipは、Python用のパッケージマネージャで、パッケージのインストールと管理を行うことができます。

[pipのインストールガイド](https://pip.pypa.io/en/stable/installation/)に従って、pipをインストールしてください。

aptを使用してpipをインストールする場合は、下記手順でインストールしてください。

1. pipがインストールされているか確認する。<br>`pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)` のように表示された場合は、pipがインストールされています。<br>以降の手順はスキップしてください。
```
pip3 --version
```

2. システムを更新する
```
sudo apt-get update
```

3. pipをインストールする
```
sudo apt install python3-pip
```

4. pipがインストールされたことを確認する。<br>`pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)` のように表示されていれば、pipのインストールは完了です!
```
pip3 --version
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
⭐️後で記載する!!!

テキストや参考にした記事などを再度読み返して技術の理解を深めてから書く。

ここがエンジニアに一番読んでもらいたい箇所なのでできるだけ詳細に書く。

## 📮今後の実装したいもの
- [x] オンラインでエディタに記述したMarkdownをHTMLへ変換できるサービスを作成する

## 📑参考文献
### 公式ドキュメント
- [Python](https://docs.python.org/ja/3/)

### 参考にしたサイト
- [Python_Download](https://www.python.org/downloads/)
- [pipのインストールガイド](https://pip.pypa.io/en/stable/installation/)
- [markdownのプロジェクトの説明](https://pypi.org/project/Markdown/)
- [Markdown記法一覧](https://qiita.com/oreo/items/82183bfbaac69971917f#:~:text=Markdown%EF%BC%88%E3%83%9E%E3%83%BC%E3%82%AF%E3%83%80%E3%82%A6%E3%83%B3%EF%BC%89%E3%81%AF%E3%80%81,%E3%82%82%E9%96%8B%E7%99%BA%E3%81%95%E3%82%8C%E3%81%A6%E3%81%84%E3%82%8B%E3%80%82)
- [HTML の基本](https://developer.mozilla.org/ja/docs/Learn/Getting_started_with_the_web/HTML_basics)
