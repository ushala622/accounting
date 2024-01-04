import datetime
from datetime import date
from datetime import timedelta
import 計算1
from 計算1 import category_total
expense_list = []
categories = ['food', 'clothing', 'housing', 'transportation', 'entertainment']

def add_expense(): #新增支出模組
    selected_date = ''
    while True:
        date = input("請輸入日期：(YYYY-MM-DD)") #輸入日期
        category = input("請輸入支出類別：") #輸入類別
        amount = float(input("請輸入支出總額：")) #輸入支出
        description = input("請輸入描述：") #輸入描述
        current_list = [date,category,amount,description] #建立儲存序列
        expense_list.append(current_list) 
        print(date,category,amount,description) #印出日期、類別、支出、描述
        
        x = input("是否要繼續新增收入？(y/n)") 
        if x == 'y':
            continue
        elif x =='n':
            break

def total_expense(): #查詢當日總額模組
    #outputstring = ''
    total = 0.0 
    selected_date = input("請輸入你要查詢的日期：(YYYY-MM-DD)") 
    for i in expense_list:
        if selected_date == i[0]:
            #outputstring += i[0] + str(i[1] + i[2] + i[3] + "\n"
            total += i[2]
            #print(outputstring)
    print(selected_date, ",的支出總額為" ,total)

def month_expense(): #查詢當月總額模組
    total = 0.0 
    selected_month = input("請輸入你要查詢的月份：(YYYY-MM)")
    for i in expense_list:
        if i[0][:7] == selected_month:
            total += i[2]
    print(selected_month, ",的支出總額為" ,total)


print("您已進入記帳系統")
print("1. 新增支出")
print("2. 查詢當日支出總額")
print("3. 查詢當月支出總額")
print("4. 圓餅圖")
print("5. 退出")
while True:
    choice = input("請輸入: 1/2/3/4/5 ")
    if choice == '1':
        add_expense()
    elif choice =='2':
        total_expense()
    elif choice =='3':
        month_expense()
    elif choice =='4':
        category_total(expense_list)
    else:
        exit()
