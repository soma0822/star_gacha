class AddColumnsToUsers < ActiveRecord::Migration[7.0]
  def change
    add_column :users, :menu_ids, :integer
  end
end
