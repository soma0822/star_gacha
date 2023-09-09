class AddColumnsToMenus < ActiveRecord::Migration[7.0]
  def change
    add_column :menus, :fav, :boolean
  end
end
