import sys
import os

print('**********************\n券売機シミュレーター\n**********************')

# グローバル変数の定義
menu = [['特製ラーメン', 1000, 0], ['醬油ラーメン', 780, 0], ['塩ラーメン', 880, 0], ['ごはん', 150, 0]]
temp_dep = [0, 0, 0, 0]
total = 0
cnt_buy = 0
choice_list = []

def simulate_vending_machine():
    global menu, temp_dep, total, cnt_buy, choice_list
    print('\n商品      金額\n=======================\n1.特製ラーメン 1000円\n2.醤油ラーメン 780円\n3.しおラーメン 880円\n4.ごはん 150円')
    
    while True: 
        choice = input('購入する商品番号(支払いに進む場合はc,戻る場合はq)>').strip()
        if choice == 'c':
            print(f'\n 商品　　　　数量\n1.特製ラーメン {menu[0][2]}\n2. 醤油ラーメン {menu[1][2]}\n3.塩ラーメン {menu[2][2]}\n4.ごはん {menu[3][2]}\n===\n合計 {total} 円')
            break
        elif choice in ['1', '2', '3', '4']:
            choice_list.append(int(choice))
            total += menu[int(choice)-1][1]
            menu[int(choice)-1][2] += 1
            temp_dep[int(choice)-1] += 1
        elif choice == 'q':
            main()
        else:
            print('1から4、またはcを押してください')
    
    dep = int(input('現金を投入してください>'))
    while True:
        if dep < total:
            cancel = input(f'{total - dep}円不足しています。キャンセルしますか(y/n)>').strip().lower()
            if cancel == 'y':
                for choice in choice_list:
                    menu[int(choice)-1][2] -= 1
                    temp_dep[int(choice)-1] -= 1
                choice_list = []
                total = 0
                dep = 0
                break
            elif cancel == 'n':
                dep += int(input(f"{total - dep}円不足しています。追加投入してください>"))
        else:
            print(f'ご購入ありがとうございます。おつり{dep - total}円です')
            cnt_buy += 1
            break
    
    # 必要に応じてグローバル変数をリセットする場合
    menu = [['特製ラーメン', 1000, 0], ['醬油ラーメン', 780, 0], ['塩ラーメン', 880, 0], ['ごはん', 150, 0]]
    total = 0

def Management_screen():
    global menu, temp_dep, total, cnt_buy
    print(f'***********************\n管理画面\n***********************\n\n======= 商品一覧 =======\n\n商品      単価  販売数  売上金額\n\n=======================\n1.特製ラーメン 1000円  {temp_dep[0]}   {(menu[0][1])*(temp_dep[0])}円\n2.醤油ラーメン 780円   {temp_dep[1]}     {(menu[1][1])*(temp_dep[1])}円\n3.しおラーメン 880円     {temp_dep[2]}     {(menu[2][1])*(temp_dep[2])}円\n4.ごはん 150円      {temp_dep[3]}        {(menu[3][1])*(temp_dep[3])}円\n\n\n———\n総売上金額 {(menu[0][1])*(temp_dep[0])+(menu[1][1])*(temp_dep[1])+(menu[2][1])*(temp_dep[2])+(menu[3][1])*(temp_dep[3])}円')
    print('=== 管理メニュー ===\n1.売上をリセットする\n2.商品の価格を変更する\n※売上がリセットされていないと利用できません。\n3.管理画面を終了する')
    mana_code = int(input("管理コード入力:").strip())
    print(mana_code)
    while True:
        if mana_code == 1:
            temp_dep = [0, 0, 0, 0]
            print(f"売上をリセットしました。\n======= 商品一覧 =======\n\n商品      単価  販売数  売上金額\n\n=======================\n1.特製ラーメン 1000円  {temp_dep[0]}   {(menu[0][1])*(temp_dep[0])}円\n2.醤油ラーメン 780円   {temp_dep[1]}     {(menu[1][1])*(temp_dep[1])}円\n3.しおラーメン 880円     {temp_dep[2]}     {(menu[2][1])*(temp_dep[2])}円\n4.ごはん 150円      {temp_dep[3]}        {(menu[3][1])*(temp_dep[3])}円\n\n\n———\n総売上金額 {(menu[0][1])*(temp_dep[0])+(menu[1][1])*(temp_dep[1])+(menu[2][1])*(temp_dep[2])+(menu[3][1])*(temp_dep[3])}円")
            cnt_buy = 0
            break
        elif mana_code == 2:
            if cnt_buy > 0:
                print('売上をリセットしてから選択してください。')
                break
            else:
                print(f"======= 商品一覧 =======\n\n商品      単価  販売数  売上金額\n\n=======================\n1.特製ラーメン 1000円  {temp_dep[0]}   {(menu[0][1])*(temp_dep[0])}円\n2.醤油ラーメン 780円   {temp_dep[1]}     {(menu[1][1])*(temp_dep[1])}\n3.しおラーメン 880円     {temp_dep[2]}     {(menu[2][1])*(temp_dep[2])}円\n4.ごはん 150円      {temp_dep[3]}        {(menu[3][1])*(temp_dep[3])}円")
                num = int(input("価格を変更する商品の番号を入力して下さい。>").strip())
                price = int(input("変更金額を入力してください。").strip())
                y_or_n = input(f'【{num}.{menu[num - 1][0]} {price}円】に変更します。\nよろしいですか(Y/N) >').strip().lower()
                if y_or_n == 'y':
                    menu[num - 1][1] = price
                    print(f'{num}.{menu[num - 1][0]} {menu[num - 1][1]}円')
                    print("変更しました。")
                    print(f"======= 商品一覧 =======\n\n商品      単価  販売数  売上金額\n\n=======================\n1.特製ラーメン {menu[0][1]}円  {temp_dep[0]}   {(menu[0][1])*(temp_dep[0])}円\n2.醤油ラーメン {menu[1][1]}円   {temp_dep[1]}     {(menu[1][1])*(temp_dep[1])}\n3.しおラーメン {menu[2][1]}円     {temp_dep[2]}     {(menu[2][1])*(temp_dep[2])}円\n4.ごはん {menu[3][1]}円      {temp_dep[3]}        {(menu[3][1])*(temp_dep[3])}円")
                    break
        elif mana_code == 3:
            print('**********************\n券売機シミュレーター\n**********************')
            break

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
