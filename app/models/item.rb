class Item < ApplicationRecord
  has_many :item_menu_relations
  has_many :menus, through: :item_menu_relations
end
