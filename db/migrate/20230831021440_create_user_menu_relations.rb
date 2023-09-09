class CreateUserMenuRelations < ActiveRecord::Migration[7.0]
  def change
    create_table :user_menu_relations do |t|
      t.references :user, null: false, foreign_key: true
      t.references :menu, null: false, foreign_key: true

      t.timestamps
    end
  end
end
