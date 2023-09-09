# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the bin/rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: "Star Wars" }, { name: "Lord of the Rings" }])
#   Character.create(name: "Luke", movie: movies.first)

require 'csv'

# CSVファイルのパスを指定して読み込む
csv_path = 'db/menu_prices.csv'

# CSVファイルの各行を読み込んでデータベースに登録する
CSV.foreach(csv_path, headers: false) do |row|
  product_name, cal, price, topping1, topping2, topping3 = row[0], row[1].to_i, row[2].to_i, row[3], row[4], row[5]

  Item.create!(
    product_name: product_name,
    cal: cal,
    price: price,
    food_or_drink: "drink",
    topping1: topping1,  
    topping2: topping2,  
    topping3: topping3,  
  )
end

csv_path = 'db/menu_food.csv'

CSV.foreach(csv_path, headers: false) do |row|
  product_name, cal, price = row[0], row[1].to_i, row[2].to_i

  Item.create!(
    product_name: product_name,
    price: price,
    cal: cal,
    food_or_drink: "food"
  )
end

csv_path = 'db/topping.csv'

CSV.foreach(csv_path, headers: false) do |row|
  product_name, price = row[0], row[1].to_i

  Topping.create!(
    product_name: product_name,
    price: price,
  )
end