class Menu < ApplicationRecord
  has_many :item_menu_relations, dependent: :delete_all
  has_many :items, through: :item_menu_relations

  has_many :topping_menu_relations, dependent: :delete_all
  has_many :toppings, through: :topping_menu_relations

  has_many :user_menu_relations, dependent: :delete_all
  has_many :users, through: :user_menu_relations, validate: false

  validates :items, presence: true
end
