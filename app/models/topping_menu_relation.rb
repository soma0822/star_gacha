class ToppingMenuRelation < ApplicationRecord
  belongs_to :topping
  belongs_to :menu
end
