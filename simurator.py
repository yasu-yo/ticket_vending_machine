import sys
import os

print('**********************\n券売機シミュレーター\n**********************')

# 商品リスト（商品番号: [商品名, 価格]）
menu = [('特製ラーメン', 1000), ('醬油ラーメン', 780), ('塩ラーメン', 880), ('ごはん', 150)]

def simulate_vending_machine():
    print('\n商品      金額\n=======================\n1.特製ラーメン 1000円\n2.醤油ラーメン 780円\n3.しおラーメン 880円\n4.ごはん 150円')

    total = 0
    while True: 
        choice = input('購入する商品番号(支払いに進む場合はc)>').strip()
        if choice == 'c':
            # print(f'お会計: {total}円')
            break
        elif choice in ['1', '2', '3', '4']:
            total += menu[int(choice)-1][1]
            # print(f'合計金額: {total}円')
        else:
            print('1から4、またはcを押してください')

def main():
    while True:
        print("\nキーを押してください：")
        print("1: シミュレーション画面")
        print("2: 管理画面（未実装）")
        print("q: 終了")
        
        choice = input().strip().lower()
        
        if choice == '1':
            simulate_vending_machine()
        elif choice == '2':
            print("管理画面へ移動します（未実装）")
        elif choice == 'q':
            print("シミュレーターを終了します")
            sys.exit(0)
        else:
            print("無効な選択です。もう一度お試しください。")

if __name__ == "__main__":
    main()






