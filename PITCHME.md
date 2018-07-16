### Python勉強会
[GitHub(https://github.com/tmu-sig/learn-python)](https://github.com/tmu-sig/learn-python)  
[スライド(https://gitpitch.com/tmu-sig/learn-python)](https://gitpitch.com/tmu-sig/learn-python)  
Yuma Kinoshita

+++

### 第0回 イントロダクション
#### もくじ
- 席替え
- この勉強会について
- Gitを使おう
- ふりかえり

+++

### 席替え
- 誕生日の早い順に並んで座ろう
  - 1月-12月
- 制限時間3分

+++

### この勉強会について
#### なんで勉強会をやるの?
- 研究室生活をもっと意味のあるものにしたい
- みなさんの負担を減らしたい
  - お互いにサポートしあえる環境にしたい

+++

### みなさんにしてほしいこと
- わからないことは何でも聞く！
- 「こうしたほうがいい」と思うことは  
  どんどん言う！
- 困っている人には積極的なアドバイスを！

#### ただし以下のことに注意
- 他人がイラッとするような  
  発言や伝え方をしない
  - 「なんでできないの？」など
- 教える際には，相手を置いてきぼりにしない

+++

### 勉強会の進め方
- ペアプログラミング
  - 毎回ペアを作ってプログラミング
  - 一つの作業をお互いにサポート

+++

### Gitを使おう
<img src="https://git-scm.com/images/logos/downloads/Git-Logo-2Color.png" alt="git logo" title="git logo" width="200">
#### Gitって？
- [wikipedia](https://ja.wikipedia.org/wiki/Git)によれば…
  > プログラムのソースコードなどの変更履歴を
    記録・追跡するための分散型バージョン管理システム
- **よくわからない**

+++

### 質問 ファイルを編集するときは？
- 編集後どんどん上書き保存
- 編集前とは別のファイルを作り保存
- バージョン管理ソフトを使っている

+++

### Gitを使うと
- どんどん上書き保存！
- 困ったら好きなところに巻き戻せる！
- 複数人での共有が簡単！

+++

### Gitをインストールしよう
- Windows
  - [Git for Windows](https://gitforwindows.org/)
- Mac
  ```
  $ brew install git
  ```
- Ubuntu
  ```
  $ sudo apt install git
  ```

#### インストールできたことを確認
```
$ git --version
```
- Windowsの場合はGit Bashを起動

+++

### GitHubに登録しよう
<img src="https://assets-cdn.github.com/images/modules/logos_page/Octocat.png" alt="github logo" title="github logo" width="200">
#### Githubって？
- 無料で使えるGitサーバ
- [ここ](https://github.com/)からアカウントを作成
  - 全世界に公開されるので個人情報には注意

#### アカウントができたら
- [tmu-sig](https://github.com/tmu-sig/)に参加

+++

### リポジトリをコピーしてみよう！
#### リポジトリって？
- フォルダとかファイルとかのまとまり
- tmu-sig/learn-pythonというリポジトリには，  
  この勉強会用のファイルがまとまっている

#### リポジトリのコピー
- ダウンロード先のディレクトリに移動
  ```
  $ cd ダウンロード先
  ```
- githubからリポジトリをコピー
  ```
  $ git clone リポジトリのURL
  ```

+++

### リポジトリにファイルを追加しよう！
- learn-python/0_introduction/ 以下に
  "自分のアカウント名.txt"というファイルを作成
- 作成できたら以下のコマンドを実行
  ```
  $ git add --all
  $ git commit -m "initial commit"
  $ git pull
  $ git push origin master
  ```
- [リポジトリのページ](https://github.com/tmu-sig/learn-python)が  
  更新されていることを確認

+++

### 今日はここまで

+++

### ふりかえり
- 今日の勉強会の評価をお願いします
  - 「せーの」といったら，指の数で評価を表してください
    - 5本（パー）: とても良かった
    - 0本（グー）: とても悪かった
- 勉強会の進め方などに気になるところや  
  意見などあればいつでも言ってください

+++

### 第1回
#### もくじ
- 席替え
- Pythonの実行環境を作ろう
- 開発環境を整えよう
- ふりかえり

+++
### 席替え
- 制限時間3分

+++

### Pythonの実行環境を作ろう
#### 実行環境？
- プログラム（hogehoge.py）は  
  ただのテキストファイル
- 実行環境＝ファイルに書かれている内容を解釈して，PCに命令する
- pythonではプロジェクトごとに  
  仮想環境を作ることが一般的
  - 輪講ゼミではpython2系，この勉強会ではpython3系を使うといったことが簡単に
  - パッケージの管理が簡単

+++

### Python3のインストール
このスライドでは[ここ](https://medium.com/@chezou/python%E3%81%AE%E7%92%B0%E5%A2%83%E6%A7%8B%E7%AF%89%E3%82%92%E8%87%AA%E5%88%86%E3%81%AA%E3%82%8A%E3%81%AB%E6%95%B4%E7%90%86%E3%81%97%E3%81%A6%E3%81%BF%E3%82%8B-dc8d8f2fe989)  
の方法に従ってインストールする
- Windows
  - [公式ページ](https://www.python.org/)
    のインストーラーを実行
  - C:\\usr\\local\\bin\\Python36 と  
    C:\\usr\\local\\bin\\Python36\\Scripts をPATHに追加
- Mac
  ```
  $ brew install python3
  ```
- Ubuntu
  ```
  $ sudo apt install python3
  ```

+++

### pip, virtualenvのインストール
- pip: pythonのパッケージを管理するソフト
- virtualenv: 仮想環境を作るためのソフト
- Windows
  - [ここ](https://bootstrap.pypa.io/get-pip.py)からget-pip.pyをダウンロード
  - get-pip.pyを実行
    ```
    $ python get-pip.py
    ```
  - virtualenvをインストール
    ```
    $ pip install virtualenv
    ```

+++

### pip, virtualenvのインストール
- Mac, Ubuntu
  ```
  $ wget https://bootstrap.pypa.io/get-pip.py
  $ export PATH="~/.local/bin/:$PATH"
  $ python get-pip.py --user
  $ pip install virtualenv --user
  ```
  - exportの行は，.profileや.bash_profileなどに  
    追加しておく

+++

### 仮想環境の構築
- プロジェクトのディレクトリへ移動  
  （gitからcloneしたlearn-pythonの下）
  ```
  $ cd hogehoge/learn-python/
  ```
- virtualenvを使ってpython 3.6の環境を作る
  ```
  $ virtualenv venv -p python3.6
  ```
  うまくいかないときは
  ```
  $ virtualenv venv -p python3.6のフルパス
  ```
<!---
受講者には.gitignoreを変更させない
- gitでvenvフォルダが同期されないようにする
  ```
  $ echo venv >> .gitignore
  ```
-->

+++

### 仮想環境の有効化・無効化
- 有効化
  - Windows
    ```
    $ .\venv\Scripts\activate
    ```
  - Mac, Ubuntu
    ```
    $ source venv/bin/activate
    ```
  - 仮想環境が有効化されると，  
    ターミナル左に(venv)と表示される
- 無効化
  ```
  $ deactivate
  ```

+++

### 開発環境を整えよう
#### 開発環境って？
- プログラムはテキストファイル（.txtと一緒）
- テキストエディタがあれば編集できる！
- **ただし…** シンプルなテキストエディタで  
  プログラムを書くのは苦行

  <img src="https://raw.githubusercontent.com/tmu-sig/learn-python/master/fig/texteditor.png" alt="text editor logo" title="text editor logo" width="200">

+++

### いろいろなテキストエディタ
<img src="https://www.kaoriya.net/blog/2013/12/06/vimlogo-564x564.png" alt="vim logo" title="vim logo" width="100">
<img src="https://raw.githubusercontent.com/cg433n/emacs-mac-icon/master/emacs.iconset/icon_128x128.png" alt="emacs logo" title="emacs logo" width="100">
- vim
  - 高機能テキストエディタ
  - 慣れるとすごい速さで  
    テキストを編集できるらしい
- emacs
  - vimのライバル
- **ただし…** プログラミング用にプラグインを入れたりするのがめんどくさい

+++

### atom
<img src="https://raw.githubusercontent.com/atom/atom/master/resources/app-icons/stable/png/128.png" alt="vim logo" title="vim logo" width="200">
#### atomって？
- githubが作っているテキストエディタ
- インストールするだけで簡単に使える
- プラグインによる機能拡張も簡単

+++

### atomのインストール
- [ここ](https://atom.io)からインストーラーを  
  ダウンロード・実行

**これだけ**

+++

### atomの日本語化
- メニューとかが英語だと使いにくい！って人へ
- atomの左上のメニューから  
  File > Settings を選択
- Settingsの左のメニューからInstallを選択
- Search packagesの欄に"japanese-menu"と入力・エンター
- 一番上に出てきたパッケージをInstall!

+++

### 今日はここまで

+++

### ふりかえり
- 今日の勉強会の評価をお願いします
  - 「せーの」といったら，指の数で評価を表してください
    - 5本（パー）: とても良かった
    - 0本（グー）: とても悪かった
- 勉強会の進め方などに気になるところや  
  意見などあればいつでも言ってください

+++

### 第2回
#### もくじ
- 席替え
- Hello World!
- 四則演算をしてみよう
- 変数と関数を使おう！
- Fizz Buzz
- ふりかえり

+++

### 席替え
- 名前 (First name) のアルファベット順
- 各班のチーム名を考えよう
  - それぞれの特徴をよく表現するように！
- 制限時間5分

+++

### 前準備
- learn-pythonフォルダに移動し仮想環境を有効化
  - Windows
    ```
    $ .\venv\Scripts\activate
    ```
    ※ 日本語環境ではバックスラッシュ(＼)と円マーク(￥)は同じ
  - Mac, Ubuntu
    ```
    $ source venv/bin/activate
    ```
- pythonの対話環境を起動
  ```
  $ python
  ```

+++

### Hello World!
- プログラミング最初の一歩
- 端末上に **Hello World!** と  
  表示するプログラムを作ろう

+++

### 次に答えがあるから見ないでね！

+++

### Hello World!
- 答え
  ```
  >>> print("Hello World!")
  ```
- 解説
  - print(): 文字列や変数を画面に表示する関数
  - "", '': pythonでは文字列を  
  ダブルクォーテーション("")  
  もしくはシングルクォーテーション('')で  
  表す．
    - それ以外の文字は，変数名や関数名などのプログラムの内容だと解釈される

+++

### 四則演算をしてみよう
- 適当な整数同士の四則演算と除算の余りを計算しよう
  - 和 sum, 差 difference, 積 product,  
    商 quotient, 余り remainder
- 入力と答えの型(type)を確認しよう

+++

### 次に答えがあるから見ないでね！

+++

### 四則演算をしてみよう
- 答え (3と4の四則演算の場合)
  ```
  >>> type(3)
  >>> type(4)
  >>> 3 + 4
  >>> 3 - 4
  >>> 3 * 4
  >>> 3 / 4
  >>> 3 % 4
  >>> type(3+4)
  ```
- 解説
  - 除算の結果のみfloat型になる  
   (暗黙的な型変換(キャスト)が行われる)
- 除算の答えをint型にしよう！

+++

### 次に答えがあるから見ないでね！

+++

### 四則演算をしてみよう
- 答え
  ```
  >>> int(3/4)
  ```
- 解説
  - 型変換(キャスト)をする際には，  
    型名(変換したいもの)とすればいい

+++

### 変数と関数を使おう
- 変数: 数値や文字列などの情報を記憶
- 関数: 一連の処理をひとまとまりにしたもの
  - 数学の関数とは違う
- 与えられた2つの整数num1とnum2の  
  四則演算と余りを計算し，画面に表示する関数  
  calculate(num1, num2)を実装しよう！
  - 実装したものは，  
    2_functions/チーム名.pyとして保存
  - gitにpush!

+++

### 次に答えがあるから見ないでね！

+++

### 変数と関数を使おう
- 答え
  ```python:kinoshita.py
  def calculate(num1, num2):
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(num1 / num2)
    print(num1 % num2)

  if __name__ == "__main__":
    calculate(3, 4)
    ```
  - 解説
    - 下のif文の部分はメイン関数に相当

+++

### 今日はここまで

+++

### ふりかえり
- 今日の勉強会の評価をお願いします
  - 「せーの」といったら，指の数で評価を表してください
    - 5本（パー）: とても良かった
    - 0本（グー）: とても悪かった
- 勉強会の進め方などに気になるところや  
  意見などあればいつでも言ってください

+++

### 第3回

+++

### 席替え
- 出身地（北から順に）
- 制限時間3分

+++

### git pull
- ターミナル(Git Bash)上で以下を実行
  ```
  $ git pull
  ```
- エラーが出た人は，何もせずストップ

+++

### 良いプログラムを書くために
プログラムを書くときに最も重要なことは？

+++
### 良いプログラムを書くために
- 最も重要なことは  
  ***他の人にとってわかりやすいコードを書く***
- そのためにまず気をつけてほしいこと
  - 変数・関数には具体的な名前をつける
    - NG: a, aa, a1
  - 1行は80文字以内！
  - 1つの関数やスクリプトは細かく分ける
- [おすすめの本](https://www.oreilly.co.jp/books/9784873115658/)

+++

### Fizz Buzz
#### ゲームをします！
- 1から順番に数を数えるゲーム
- ただし…
  - 3の倍数のときは Fizz
  - 5の倍数のときは Buzz
  - 3と5の両方の倍数のときは Fizz Buzz

+++

### Fizz Buzz
- 整数値numを引数として
  - 3の倍数なら Fizz
  - 5の倍数なら Buzz
  - 3と5の両方の倍数なら FizzBuzz
  - それ以外のときはnum自身を端末上に  
    表示する関数fizz_buzz(num)を作ろう！
    - 3_for/チーム名_fizzbuzz.py に定義しよう

+++

### 次に答えがあるから見ないでね！

+++

### Fizz Buzz
- 答え
  ```
  def fizz_buzz(num):
    if num % 3 != 0 and num % 5 != 0:
      print(num, end="")
    if num % 3 == 0:
      print("Fizz", end="")
    if num % 5 == 0:
      print("Buzz", end="")
    print()
  ```
- 解説
  - print(…, end="")とすることで  
    改行されなくなる

+++

### for文
- 繰り返し同じ処理を行うときに使う
- 最も基本的なfor文の書き方
  - 0から9まで変数iを変化させる例
  ```
  for i in range(10):
    処理
  ```
- main関数でfor文を使って  
  1から99までの整数値を  
  fizz_buzz()に入力してみよう

+++

### 次に答えがあるから見ないでね！

+++

### for文
- 答え
  ```
  if __name__ == "__main__":
    for i in range(1, 100):
      fizz_buzz(i)
  ```

+++

### リスト
- リスト (list)
  - データ構造の一つ
    - 配列 (array) に似ている
  - 要素の型がそれぞれ違っても良い
- リストの生成
  ```
  list1 = [0, 1, 2, 3, 4] #要素を具体的に列挙
  list2 = list(range(5)) #range型からキャスト
  list3 = [i for i in range(5)] #リスト内包表記
  ```

+++

### リスト
1. ```list1 = ["a", "b", "c", "d", "e"]``` とする
  1. 第0番目の要素を画面に表示しよう
  1. 第4番目の要素を画面に表示しよう
  1. 第1番目から3番目の要素を画面に表示しよう
  1. 末尾に要素"f"を追加しよう
1. ```list2 = list(range(5))``` とする
  1. list1の末尾にlist2の要素を追加しよう

+++

### 次に答えがあるから見ないでね！

+++

### リスト
1. 答え
  1. ```print(list1[0])```
  1. ```print(list1[4])```
  1. ```print(list1[1:4])```
  1. ```list1.append("f")```
1. 答え
  1. ```list1.extend(list2)```

+++

### 今日はここまで

+++

### ふりかえり
- 今日の勉強会の評価をお願いします
  - 「せーの」といったら，指の数で評価を表してください
    - 5本（パー）: とても良かった
    - 0本（グー）: とても悪かった
- 勉強会の進め方などに気になるところや  
  意見などあればいつでも言ってください

+++

### 第4回

+++

### 席替え
- 好きな数を思い浮かべてください
- その数の小さい順（昇順）に座ろう
- 制限時間3分

+++

### git pull
- ターミナル(Git Bash)上で以下を実行
  ```
  $ git pull
  ```
- エラーが出た人は，何もせずストップ

+++

### ソート
- リスト（など）の要素をある順序で並び替える処理
- pythonではsorted関数を使ってソートできる
  ```
    list1 = [6, 3, 9, 1, 0, 2, 3, 8]
    sorted(list1)
    print(list1)
    ```
- これ以降は数を昇順に並び替えることだけを考える

+++

### バブルソート
- 簡単なソートアルゴリズム
- 以下のような処理の繰り返し
  - 一番小さい要素を先頭にもってくる
  - 次に小さい要素を2番目に持ってくる

+++

### バブルソート
- バブルソートを用いて任意のリストを  
  ソートする関数bubble_sort()  
  を実装しよう！
  - 入力のリストはint型, float型の要素のみを含む
  - sorted(), max(), min()などの関数は使わない
  - 実装したものは，  
    4_sort/チーム名_bubble_sort.pyとして保存
- 作成したソートプログラムをテストするために  
  どのような入力を与えればいいか考えてみよう

+++

### git push
- 作成できたら以下のコマンドを実行
  ```
  $ git add --all
  $ git commit -m "initial commit"
  $ git pull
  $ git push origin master
  ```

+++

### 再帰処理
- ある関数の中から自分自身を呼び出す処理
- ループと同じようなものだが  
  再帰処理を使うとプログラムが簡単になる場合がある
- フィボナッチ数列
  - x<sub>n</sub> = x<sub>n-1</sub> + x<sub>n-2</sub>
  - 0, 1, 1, 3, 5, 8, 13, 21, ...

+++

### 再帰処理
- 再帰処理を使ってフィボナッチ数列  
  の第n項を計算する関数fibonacci(n)を作ろう！
  - 実装したものは，  
    4_sort/チーム名_fibonacci.pyとして保存

+++

### クイックソート
- ソートアルゴリズムのひとつ
- 名前の通り（だいたい）速い
- 再帰処理を使う
- アルゴリズム
  - ピボットを選ぶ
  - ピボットより小さい数を前方，  
    大きい数を後方に移動させる
  - 分割されたそれぞれを  
    クイックソートによりソートする

+++

### クイックソート
- クイックソートによりリストの要素をソートする関数  
  quicksort()を作ろう！
  - 実装したものは，  
    4_sort/チーム名_quicksort.pyとして保存

+++

### 今日はここまで
- ひとまず前期はこれでおわり
- 夏休み中も勉強したい！って人がいれば  
  協力します

+++

### ふりかえり
- 今日の勉強会の評価をお願いします
  - 「せーの」といったら，指の数で評価を表してください
    - 5本（パー）: とても良かった
    - 0本（グー）: とても悪かった
- 勉強会の進め方などに気になるところや  
  意見などあればいつでも言ってください

+++
