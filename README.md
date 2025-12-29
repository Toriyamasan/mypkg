# mypkg

[![test](https://github.com/Toriyamasan/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/Toriyamasan/mypkg/actions/workflows/test.yml)

角度（度数法）を送信し、受信側で弧度法（ラジアン）に変換して表示するROS 2パッケージです。

## 必要な環境
* **OS**: Ubuntu 22.04 LTS
* **ROS 2**: Humble Hawksbill
* **GitHub Actions環境**: ubuntu-22.04（動作確認済み）
* **Python**: 3.10 以上

## インストール
リポジトリをワークスペースの `src` ディレクトリにクローンします。

```bash
cd ~/ros2_ws/src
git clone [https://github.com/Toriyamasan/mypkg.git](https://github.com/Toriyamasan/mypkg.git)
cd ~/ros2_ws
colcon build --packages-select mypkg
source install/setup.bash
```

##使い方
2つのターミナルを使用して、送信側（talker）と受信側（listener）を起動します。

###1. 受信側の起動

```bash
ros2 run mypkg listener
```

###2. 送信側の起動
別のターミナルで以下を実行します。

```bash
ros2 run mypkg talker
```

送信側は0度から240度まで15度刻みで値を送信し、受信側で以下のように変換結果が表示されます。 [INFO] [listener]: 受信: 15 deg -> 変換後: 0.2618 rad

##テスト方法
リポジトリ直下の test/test.bash を実行することで、ノード間の通信と角度計算の正確性を一括でチェックします。

```bash
cd ~/ros2_ws/src/mypkg
./test/test.bash
```

##ライセンス
*このソフトウェアパッケージは、GNU General Public License v3.0（GPL-3.0）ライセンスの下、再頒布、コピー、改変、および使用が許可されます。

*ライセンスの詳細は、本リポジトリ内の COPYING ファイルを参照してください。

© 2025 Toriyamasan
