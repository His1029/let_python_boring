import urllib.request

imgname = "logo_courses_ai.png"

url = "https://aiacademy.jp/assets/images/" + imgname

# urlretrieveの第一引数はアップロードされている画像のURL、第二引数には保存したい画像ファイル名
urllib.request.urlretrieve(url, imgname)

print("保存完了")