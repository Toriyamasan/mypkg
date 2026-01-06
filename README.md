# mypkg

[![test](https://github.com/Toriyamasan/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/Toriyamasan/mypkg/actions/workflows/test.yml)

角度（度数法）を送信し、受信側で弧度法（ラジアン）に変換して表示するROS 2パッケージです。

## ノードとトピックの機能

### talker ノード
角度データを生成し、定期的に配信するノードです。

* **配信トピック**
    * `/angle` ([person_msgs/msg/Person]): 角度データを含むメッセージを配信します。
        * `name`: データ種別 ("degree")
        * `age`: 度数法での角度値

### listener ノード
`/angle` トピックから度数法のデータを受け取り、弧度法に計算し直して表示するノードです。

* **購読トピック**
    * `/angle` ([person_msgs/msg/Person]): 変換対象の角度データを受け取ります。

## 実行方法

### ノードの起動
2つのターミナルを使用して、それぞれのノードを起動します。

**ターミナル1（受信側）:**
```bash
$ ros2 run mypkg listener
```

**ターミナル2（送信側）:**
```bash
$ ros2 run mypkg talker
```

## 出力の例
送信側（talker）が起動すると、受信側（listener）に以下のように変換結果が表示されます。

```Plaintext
[INFO] [listener]: 受信: 15 deg -> 変換後: 0.2618 rad
[INFO] [listener]: 受信: 30 deg -> 変換後: 0.5236 rad
```

## ライセンス＊
* このソフトウェアパッケージは、GNU General Public License v3.0 (GPL-3.0) の下で公開されています。
* © 2025 Toriyamasan
