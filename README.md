# ExperelationGenerator
csvからplantUML形式の関係図を生成するためのプログラム

pythonだよ

data配下にあるファイルを編集してmain.pyを実行すると
```
export\experelation.pu
```
ができるので、
内容コピってここに張り付けるといいよ

http://www.plantuml.com/plantuml/uml/SyfFKj2rKt3CoKnELR1Io4ZDoSa70000

#### member.csv
```
key : 個人識別用のID
name : 名前
color : カラーコード
arms : 武器
job : 職
```

#### relation.csv
```
relNum : 矢印のID
fromKey : 矢印の出る側の人のID
toKey : 矢印の向き先の人のID
style : 矢印のスタイル(あんま気にせんでいい)
note : 矢印の詳細
```
