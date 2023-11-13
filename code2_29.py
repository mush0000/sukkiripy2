#得点を入れるリスト型を用意
scores = []
#点数をリストに追加
scores.append(int(input("国語>")))
scores.append(int(input("社会>")))
scores.append(int(input("理科>")))
scores.append(int(input("数学>")))
scores.append(int(input("英語>")))

#合計を関数で出す
total = sum(scores)
ave = total / len(scores)

#結果を表示
print(total)
print(ave)