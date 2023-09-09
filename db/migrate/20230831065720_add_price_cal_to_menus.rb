class AddPriceCalToMenus < ActiveRecord::Migration[7.0]
  def change
    add_column :menus, :price, :integer
    add_column :menus, :cal, :integer
  end
end
