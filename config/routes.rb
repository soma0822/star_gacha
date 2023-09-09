Rails.application.routes.draw do
  root  "menus#show"
  
  post  "menus/spin-gacha",       to: "menus#spin_gacha", as: "spin_gacha"
  post  "menus/toggle-favorite",  to: "menus#toggle_fav", as: "toggle_fav"
  get   "menus/favorite-menus",   to: "menus#fav_menus",  as: "fav_menus"
  resources :menus, only: [:index, :show]

  get   "/signup",    to: "users#new"
  resources :users, only: [:show, :create]

  get   "/login",     to: "sessions#new"
  post  "/login",     to: "sessions#create"
  get   "/logout",    to: "sessions#destroy"
end
