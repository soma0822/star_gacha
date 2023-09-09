class SessionsController < ApplicationController
  def new
    @from_gacha = params[:from_gacha]
    return unless params[:from_gacha] == 'true'

    flash.now[:danger] = '履歴を確認するには，ログインしてください'
  end

  def create
    user = User.find_by(email: params[:session][:email].downcase)
    if user&.authenticate(params[:session][:password])
      reset_session      # ログインの直前に必ずこれを書くこと
      log_in user
      if params[:session][:from_gacha] == 'true'
        params[:session][:from_gacha] = 'false'
        redirect_to menus_path
      else
        redirect_to user
      end
    else
      # エラーメッセージを作成する
      flash.now[:danger] = 'ログインに失敗しました。入力情報を確認して再度ログインしてください'
      render 'new', status: :unprocessable_entity
    end
  end

  def destroy
    log_out
    redirect_to root_path, status: :see_other
  end
end
