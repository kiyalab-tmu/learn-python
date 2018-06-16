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
- Pythonの実行環境を作ろう
- 開発環境を整えよう
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
**よくわからない**

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
- tmu-sig/learn-pythonというリポジトリには，この勉強会用のファイルがまとまっている

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

### Pythonの実行環境を作ろう
#### 実行環境？
- プログラム（hogehoge.py）はただのテキストファイル
- 実行環境＝ファイルに書かれている内容を解釈して．PCに命令する
- pythonではプロジェクトごとに仮想環境を作ることが一般的
  - 輪講ゼミではpython2系，この勉強会ではpython3系を使うといったことが簡単に
  - パッケージの管理が簡単

+++

### Python3のインストール
このスライドでは[ここ](https://medium.com/@chezou/python%E3%81%AE%E7%92%B0%E5%A2%83%E6%A7%8B%E7%AF%89%E3%82%92%E8%87%AA%E5%88%86%E3%81%AA%E3%82%8A%E3%81%AB%E6%95%B4%E7%90%86%E3%81%97%E3%81%A6%E3%81%BF%E3%82%8B-dc8d8f2fe989)
の方法に従ってインストールする
- Windows
  - [公式ページ](https://www.python.org/)から，
    Python3.6.5のインストーラーをダウンロード・実行
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
- pip pythonのパッケージを管理するソフト
- virtualenv 仮想環境を作るためのソフト
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
- Mac, Ubuntu
  ```
  $ wget https://bootstrap.pypa.io/get-pip.py
  $ export PATH="~/.local/bin/:$PATH"
  $ python get-pip.py --user
  $ pip install virtualenv --user
  ```
  - exportの行は，.profileや.bash_profileなどに追加しておく

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
- gitでvenvフォルダが同期されないようにする
  ```
  $ echo venv >> .gitignore
  ```

+++

### 仮想環境の有効化・無効化
- 有効化
  - Windows
    ```
    $ . venv/Script/activate
    ```
  - Mac, Ubuntu
    ```
    $ source venv/bin/activate
    ```
  - 仮想環境が有効化されると，ターミナル左に(venv)と表示される
- 無効化
  ```
  $ deactivate
  ```

+++

### 開発環境を整えよう
#### 開発環境って？

+++

### 第1回
