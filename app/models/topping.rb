class Topping < ApplicationRecord
  has_many :topping_menu_relations
  has_many :menus, through: :topping_menu_relations
end
