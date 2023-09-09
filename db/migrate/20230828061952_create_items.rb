class CreateItems < ActiveRecord::Migration[7.0]
  def change
    create_table :items do |t|
      t.string :product_name
      t.integer :price
      t.integer :cal
      t.string :food_or_drink

      t.timestamps
    end
  end
end
