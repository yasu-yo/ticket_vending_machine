import sys
import os

print('**********************\n券売機シミュレーター\n**********************')

# グローバル変数の定義
menu = [['特製ラーメン', 1000, 0], ['醬油ラーメン', 780, 0], ['塩ラーメン', 880, 0], ['ごはん', 150, 0]]
temp_dep = [0, 0, 0, 0]
total = 0

def simulate_vending_machine():
    global menu, temp_dep, total
    print('\n商品      金額\n=======================\n1.特製ラーメン 1000円\n2.醤油ラーメン 780円\n3.しおラーメン 880円\n4.ごはん 150円')
    
    while True: 
        choice = input('購入する商品番号(支払いに進む場合はc)>').strip()
        if choice == 'c':
            print(f'\n 商品　　　　数量\n1.特性ラーメン {menu[0][2]}\n2. 醤油ラーメン{menu[1][2]}\n3.塩ラーメン {menu[2][2]}\n4.ごはん {menu[3][2]}\n===\n合計{total}円')
            break
        elif choice in ['1', '2', '3', '4']:
            total += menu[int(choice)-1][1]
            menu[int(choice)-1][2] += 1
            temp_dep[int(choice)-1] += 1
        else:
            print('1から4、またはcを押してください')
    
    dep = int(input('現金を投入してください>'))
    print(f'ご購入ありがとうございます。おつり{dep - total}円です')
    # 必要に応じてグローバル変数をリセットする場合
    menu = [['特製ラーメン', 1000, 0], ['醬油ラーメン', 780, 0], ['塩ラーメン', 880, 0], ['ごはん', 150, 0]]
    # temp_dep = [0, 0, 0, 0]
    total = 0

def Management_screen():
    global menu, temp_dep, total
    print(f'***********************\n管理画面\n***********************\n\n======= 商品一覧 =======\n\n商品      単価  販売数  売上金額\n\n=======================\n1.特製ラーメン 1000円  {temp_dep[0]}   {(menu[0][1])*(temp_dep[0])}円\n2.醤油ラーメン 780円   {temp_dep[1]}     {(menu[1][1])*(temp_dep[1])}\n3.しおラーメン 880円     {temp_dep[2]}     {(menu[2][1])*(temp_dep[2])}円\n4.ごはん 150円      {temp_dep[3]}        {(menu[3][1])*(temp_dep[3])}円\n\n\n———\n総売上金額 {(menu[0][1])*(temp_dep[0])+(menu[1][1])*(temp_dep[1])+(menu[2][1])*(temp_dep[2])+(menu[3][1])*(temp_dep[3])}円')

def main():
    while True:
        print("\nキーを押してください：")
        print("1: シミュレーション画面")
        print("2: 管理画面")
        print("q: 終了")
        
        choice = input().strip().lower()
        
        if choice == '1':
            simulate_vending_machine()
        elif choice == '2':
            Management_screen()
        elif choice == 'q':
            print("シミュレーターを終了します")
            sys.exit(0)
        else:
            print("無効な選択です。もう一度お試しください。")

if __name__ == "__main__":
    main()
