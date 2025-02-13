import keyboard
import os
print('**********************\n券売機シミュレーター\n**********************')
print('please enter')
# Enterキー押下で画面がクリアされて処理が進む
# ESCキー押下で管理画面に処理が進む
# qキー押下でシミュレータ終了
# 商品リスト（商品番号: [商品名, 価格]）

def on_enter_press():
    pass

def on_esc_press():
    pass

def on_q_press():
    os._exit(0)  # コンソールを終了する

def main():
    # print("キーを押してください：Enterでシミュレーション画面、Escで管理画面、Qで終了")

    # Enterキーが押されたときのイベントハンドラを登録
    keyboard.on_press_key("enter", lambda _: on_enter_press())

    # Escキーが押されたときのイベントハンドラを登録
    keyboard.on_press_key("esc", lambda _: on_esc_press())

    # qキーが押された時のイベントハンドラを登録
    keyboard.on_press_key("q", lambda _: on_q_press())

    # 無限ループで待機
    while True:
        pass

if __name__ == "__main__":
    main()
    