### 検索ツールサンプル
### これをベースに課題の内容を追記してください
# 検索ソース
import csv
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

### 検索ツール
def search():
  word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    ### ここに検索ロジックを書く
  if word in source:
    print("{}が見つかりした".format(word))
  else:
    print("{}が見つかりませんでした".format(word))
    source.append(word)
    print(source)
    with open("data.csv",'w') as f:
      writer=csv.writer(f)
      writer.writerow(source)

if __name__ == "__main__":
    search()