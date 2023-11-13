#二人の趣味を記入
A = {"将棋","オセロ","囲碁","トランプ","ダーツ"}
B = {"パチンコ","オセロ","ダーツ","ビリヤード","チェス"}

#集合関数で計算
set = (A & B)
union = (A | B)

#画面に表示
input("心の準備ができたらEnterキーを押してください")
affinity = (len(set) / len(union)) * 100
print("相性度は{}%".format(affinity))
