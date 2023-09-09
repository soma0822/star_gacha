require 'will_paginate'
require 'will_paginate/active_record'

class MenusController < ApplicationController
  def index
    return unless logged_in?

    @menus = current_user.menus.order(created_at: :desc).paginate(page: params[:page], per_page: 8)
  end

  def show
    @menu = Menu.find(params[:id]) if params[:id]
  end

  def fav_menus
    return unless logged_in?

    fav_menus = current_user.menus.where(fav: true)
    @menus = fav_menus.order(created_at: :desc).paginate(page: params[:page], per_page: 8)
  end

  def toggle_fav
    @menu = Menu.find(params[:id])
    @menu.update(fav: !@menu.fav)
    redirect_to request.referer
  end

  def spin_gacha
    @menu = spin(params[:max].to_i, params[:menu_type])
    if logged_in?
      current_user.menus.find_by(fav: false)&.destroy if current_user.menus.count >= 100
      @menu.users << current_user
    end
    @menu.save
    redirect_to menu_path(@menu.id)
  end

  private

  def spin(max, menu_type)
    menu = Menu.new
    menu_type_array = menu_type.split
    drink_or_food = menu_type_array.shift
    while (item = random_item(max - menu.price, drink_or_food))
      menu.items.push(item)
      menu.price += item.price
      menu.cal += item.cal
      drink_or_food = menu_type_array.shift if menu_type_array.any?
    end

    (1..3).each do |topping_number|
      add_random_topping(menu, max - menu.price, topping_number)
    end
    menu
  end

  # フードかドリンクか指定してランダムにitemを一つ取得する
  def random_item(max, drink_or_food)
    valid_items = Item.where('price <= ? AND food_or_drink = ?', max, drink_or_food)
    valid_items.any? ? valid_items.sample : nil
  end

  # トッピングをランダムに選び、条件を満たす限り追加する関数
  def add_random_topping(menu, max, topping_number)
    topping_name = menu.items[0].send("topping#{topping_number}")&.split&.sample
    topping = Topping.find_by(product_name: topping_name)

    return unless topping && max > topping.price

    menu.toppings.push(topping)
    topping.price
    menu.price += topping.price
  end
end
