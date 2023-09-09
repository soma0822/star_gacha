class ChangePriceCalDefalutOnMenus < ActiveRecord::Migration[7.0]
  def change
    change_column_default :menus, :price, from: nil, to: 0
    change_column_default :menus, :cal, from: nil, to: 0
  end
end
