class Item < ActiveRecord::Migration[7.0]
  def change
    add_column :items, :menu_ids, :integer
  end
end
