class ChangeColumnsDefaultOnMenus < ActiveRecord::Migration[7.0]
  def change
    change_column_default :menus, :fav, from: nil, to: false
  end
end
