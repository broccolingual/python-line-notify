## How to Install

[こちら](https://github.com/broccolingual/python-line-notify/tree/master/dist)
から対応するバージョンのwhlファイルをインストールし、パスを指定して`pip install`を行う。
<br>`pip install ~/python_line_notify-1.1.0-py3-none-any.whl`

```python
import python_line_notify

# トークンの発行方法は下記を参照
client = python_line_notify.Client('<Line Notify Token>')

# 相対パスから画像を添付(png, jpgのみ)
client.send(content='image from File', image='./test/wumpus.png')

# URLから画像を添付(jpgのみ), 通知OFF
client.send(content='image from URL', image='https://~~~~~/~~~.jpg', notify=True)

# StickerIDからステッカーを添付
# (StickerPackageId, StickerId)
# https://devdocs.line.me/files/sticker_list.pdf
client.send(content='sticker from ids', sticker=(2, 141))
```

## トークンの発行方法(必須)

### Step.1

下記のリンクからLine Notifyのページにアクセスして、通知を行いたいLineアカウントでログイン。
<br>URL -> https://notify-bot.line.me/ja/

### Step.2

ログインしたら、右上のメニューからマイページに移動
<br>
![step2](https://gyazo.com/fada6884d23b900c73be670bee9d1bc7.png)

### Step.3 

マイページの「アクセストークンの発行」から「トークンを発行する」をクリック
<br>
![step3](https://gyazo.com/12307e426ca85d118c089ce9f0e3f339.png)

### Step.4

トークンに利用する名前(適当で良い ※ただし、通知時にその名前が表示されるので注意)を入力し、通知を送信するトークルームを一つ選択して、「発行する」を押す。
<br>`※「1:1でLine Notifyから通知を受け取る」にしておけば、自分自身に通知を送信できる`
<br>
![step4](https://gyazo.com/81025477655f54f8ddf08f198dc87b46.png)

<br>`※発行したトークンは、大切に保管して下さい。トークンはなるべくスクリプトに直に書かず、環境変数などから読み込むことを推奨します。`

## Line Notify API Document

https://notify-bot.line.me/doc/ja/

## License
MIT License