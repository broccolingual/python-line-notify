## How to Install

[こちら](https://github.com/broccolingual/python-line-notify/tree/master/dist)
から対応するバージョンのwhlファイルをインストールし、パスを指定して`pip install`を行う。
<br>`pip install ~/python_line_notify-1.1.0-py3-none-any.whl`

```python
import python_line_notify

client = python_line_notify.Client('<Line Notify Token>')

# 相対パスから画像を添付(png, jpgのみ)
client.send(content='image from File', image='./test/wumpus.png')

# URLから画像を添付(jpgのみ), 通知OFF
client.send(content='image from URL', image='https://~~~~~/~~~.jpg', notify=True)
```

## Line Notify API Document

https://notify-bot.line.me/doc/ja/

## License
MIT License