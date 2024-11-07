import qrcode
import csv
from pathlib import Path

# フォルダのパスを指定
folder_path = Path(r'C:\Users\katsuki\Documents\health_web')
# 対象とする拡張子を指定
target_extension = '.html'  # 例：.htmlファイルのみ

# 拡張子が指定したものと一致するファイルを取得
file_names = [file.stem for file in folder_path.iterdir() if file.is_file() and file.suffix == target_extension]
base_url = "https://heartfelt-custard-c35b63.netlify.app//"
urls = [base_url + file_name for file_name in file_names]

# ファイル名を出力
for file_name in file_names:
    print(file_name)

# URLリストをCSVファイルに書き出し
with open("urls.csv", "w", newline="") as file:
    writer = csv.writer(file)
    for url in urls:
        writer.writerow([url])

# QRコード画像を保存するフォルダを作成
Path("images").mkdir(exist_ok=True)

# CSVファイルからURLを読み込み、QRコードを生成
with open("urls.csv", "r") as file:
    reader = csv.reader(file)
    for index, row in enumerate(reader):
        url = row[0]
        qr = qrcode.make(url)
        
        # 各URLごとに異なるファイル名で保存（例：htmlファイル名に基づく）
        qr.save(f"images/{file_names[index]}.png")
