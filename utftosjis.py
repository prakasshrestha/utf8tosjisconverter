import os
import shutil
import time
from datetime import datetime, timedelta

# ===== ▼ SETTINGS ▼ =====
input_folder = r"utf-8のファイルパス設定してください。"
output_folder = r"shift_jis変換後のファイル出力するパスを入力してください。"

delete_after_days = 7       # converted CSV cleanup
log_delete_days = 30        # log cleanup (1 month)
# ===== ▲ SETTINGS ▲ =====

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
log_folder = os.path.join(BASE_DIR, "log")


def ensure_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)


def get_log_path():
    ensure_folder(log_folder)
    today_str = datetime.now().strftime("%Y%m%d")
    return os.path.join(log_folder, f"{today_str}.log")


def write_log(message):
    log_path = get_log_path()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {message}\n"
    with open(log_path, "a", encoding="utf-8") as lf:
        lf.write(line)


# ========== NEW: Log cleanup function ==========
def delete_old_logs():
    """log フォルダ内の30日以上古い log file を削除"""
    ensure_folder(log_folder)
    now = datetime.now()

    for filename in os.listdir(log_folder):
        if not filename.endswith(".log"):
            continue

        log_path = os.path.join(log_folder, filename)

        # YYYYMMDD.log → date extraction
        base, _ = os.path.splitext(filename)

        try:
            file_date = datetime.strptime(base, "%Y%m%d")
        except:
            # unexpected filename
            continue

        # days difference
        age_days = (now - file_date).days

        if age_days >= log_delete_days:
            try:
                os.remove(log_path)
                write_log(f"[DELETE_LOG] {filename} 削除（{age_days} days old）")
            except Exception as e:
                write_log(f"[ERROR] Log 削除失敗: {filename} → {e}")


# =====================================================


def convert_utf8_to_shiftjis():
    ensure_folder(output_folder)

    files = [f for f in os.listdir(input_folder) if f.endswith(".csv")]

    if not files:
        write_log("変換すべき CSV ファイルがありません。")
        return

    for filename in files:
        input_path = os.path.join(input_folder, filename)
        name, ext = os.path.splitext(filename)
        new_filename = f"{name}_sjis{ext}"
        output_path = os.path.join(output_folder, new_filename)

        try:
            with open(input_path, "r", encoding="utf-8") as f:
                content = f.read()

            with open(output_path, "w", encoding="shift_jis", errors="ignore") as f:
                f.write(content)

            write_log(f"[OK] {filename} → {new_filename} へ変換完了")
            os.remove(input_path)

        except Exception as e:
            write_log(f"[ERROR] {filename} の変換中にエラー: {e}")


def delete_old_files():
    now = time.time()

    for f in os.listdir(output_folder):
        file_path = os.path.join(output_folder, f)

        if not os.path.isfile(file_path):
            continue

        modified_time = os.path.getmtime(file_path)
        age_days = (now - modified_time) / (24 * 60 * 60)

        if age_days >= delete_after_days:
            try:
                os.remove(file_path)
                write_log(f"[DELETE] 古いファイル削除: {f}")
            except Exception as e:
                write_log(f"[ERROR] 古いファイル削除失敗: {f} → {e}")


if __name__ == "__main__":
    write_log("==== UTF-8 → Shift-JIS 変換開始 ====")
    convert_utf8_to_shiftjis()

    write_log("==== 古いファイル削除処理開始 ====")
    delete_old_files()

    write_log("==== Log ファイル整理開始 ====")
    delete_old_logs()

    write_log("==== 全処理完了 ====")
