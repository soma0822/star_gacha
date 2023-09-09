class AddColumnsToItems < ActiveRecord::Migration[7.0]
  def change
    add_column :items, :topping1, :string
    add_column :items, :topping2, :string
    add_column :items, :topping3, :string
  end
end
