class CreateToppingMenuRelations < ActiveRecord::Migration[7.0]
  def change
    create_table :topping_menu_relations do |t|
      t.references :topping, null: false, foreign_key: true
      t.references :menu, null: false, foreign_key: true

      t.timestamps
    end
  end
end
