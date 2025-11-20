# 📄 UTF-8 ～SHIFT-JISに自動変換スクリプト – Documentation
### 📌 概要 (Overview)

このスクリプトは、指定フォルダ内の UTF-8 形式の CSV ファイルを自動で Shift-JIS に変換し、変換後のファイルを保存します。また、古くなった変換済みファイルやログファイルを自動で削除し、フォルダを常にクリーンな状態に保ちます。

### 📁 機能一覧 (Features)
#### ✔ 1. UTF-8 → Shift-JIS 自動変換

* 入力フォルダ内の .csv ファイルを検出

* Shift-JIS に変換して別フォルダへ保存

* 変換後、元の UTF-8 ファイルを自動削除

#### ✔ 2. 古い CSV ファイルの自動削除

* output_folder 内の変換済みファイルを監視

* 最終更新日から 7日以上 経過したファイルを削除

* 設定は変数 delete_after_days で変更可能

#### ✔ 3. Daily Log File 自動生成

* log フォルダを自動生成

* YYYYMMDD.log 形式でその日のログファイルを作成

* すべての処理内容をタイムスタンプ付きで記録

> 例：log/20250119.log

#### ✔ 4. 1ヶ月以上古いログファイルの自動削除

* log_delete_days = 30

* 30日以上古いログファイルのみ削除（他のログは消さない）

### 🧭 フォルダ構成 (Folder Structure)
    ProjectFolder/
     ├─ utftosjis.py (このスクリプト)
     ├─ log/
     │    ├─ 20250119.log
     │    ├─ 20250120.log
     │    └─ … (過去ログ)
     ├─ utf-8filefolder(入力)/         ← UTF-8 CSV 入力
     └─ shfit-jis file-folder(変換後)/       ← Shift-JIS 出力

### ⚙ 設定 (Configuration)

スクリプト冒頭の設定を変更すればフォルダを自由に変更できます：
<pre>
<code>
input_folder = r"...(UTF-8 input)" 
output_folder = r"...(Shift-JIS output)"　
delete_after_days = 7        # CSV delete period
log_delete_days = 30         # Log delete period </code></pre>

### 🔄 処理の流れ (Processing Flow)
#### 1️⃣ Start
==== UTF-8 → Shift-JIS 変換開始 ====

#### 2️⃣ CSV 変換

* UTF-8 を読み込み

* Shift-JIS に再保存

* 元ファイル自動削除

#### 3️⃣ 古いファイルの削除

* 7日以上前の変換済みファイルを削除

#### 4️⃣ Log cleanup

* 30日以上古いログファイルを削除

#### 5️⃣ 完了
==== 全処理完了 ====

### 🧪 必要なライブラリ (Requirements)
👉 外部インストールは不要（標準ライブラリのみ）

使用している modules:

* os

* time

* datetime

* shutil

Python があればそのまま実行可能。

#### 📌 ログ出力例 (Example log content)

> [2025-01-19 10:32:02] ==== UTF-8 → Shift-JIS 変換開始 ====<br>
> [2025-01-19 10:32:02] [OK] 20250119.csv → 20250119_sjis.csv へ変換完了<br>
> [2025-01-19 10:32:02] ==== 古いファイル削除処理開始 ====<br>
> [2025-01-19 10:32:02] [DELETE] 古いファイル削除: 20241201_sjis.csv<br>
> [2025-01-19 10:32:02] ==== Log ファイル整理開始 ====<br>
> [2025-01-19 10:32:02] [DELETE_LOG] 20241215.log 削除（35 days old）<br>
> [2025-01-19 10:32:02] ==== 全処理完了 ====<br>

### 🧩 カスタマイズ可能ポイント
|項目	|変更方法|
|:-----|:-------:|
|CSV入力フォルダ|	input_folder |
|shift-JIS保存先|output_folder |
|CSV削除日数 |delete_after_days|
|Log削除日数|	log_delete_days|
|Log出力場所|	log_folder で変更可能|
## # ✔ まとめ (Summary)

このスクリプトは以下の処理を完全自動で実行します：

* UTF-8 CSV → Shift-JIS CSV 変換

* 元ファイル自動削除

* 古いCSVの自動整理（7日）

* 日付別ログ作成

* 古いログ自動削除（30日）

運用に適した、完全自動のファイル整理システムになっています。
