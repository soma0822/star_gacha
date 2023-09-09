
file_path = "menu_prices.csv"  # 読み込むファイルのパスを指定

with open(file_path, "r") as file:
	line = file.readline()  # 一行読み込む
	while line:
		# ここでlineを処理する（例: プリントする）
		name, price = line.strip().split(",")
		print("Item.create!( product_name: " + name + ",\n\t\t\tprice: " + price + ",\n\t\t\tcal: 0,\n\t\t\tfood_or_drink: drink") # strip()で改行を取り除く
		line = file.readline()  # 次の行を読み込む