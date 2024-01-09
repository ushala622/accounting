import matplotlib.pyplot as plt
import matplotlib

def func(s, d): #圖表文字格式設定
    t = int(round(s/100.*sum(d)))
    return f'{s:.1f}%\n{t}'

def category_total(expense_list): #查詢類別總額+圓餅圖模組 （潔羚）
    global food, clothing, housing, transportation, entertainment  # 使用全域變數
    food = 0
    clothing = 0
    housing = 0
    transportation = 0
    entertainment = 0
    total = 0.0
    
    for i in expense_list:
        if i[1] == 'food':
            food += i[2]
        elif i[1] == 'clothing':
            clothing += i[2]
        elif i[1] == 'housing':
            housing += i[2]
        elif i[1] == 'transportation':
            transportation += i[2]
        elif i[1] == 'entertainment':
            entertainment += i[2]

    total = food + clothing + housing + transportation + entertainment
    food_percentage = (food / total) * 100
    clothing_percentage = (clothing / total) * 100
    housing_percentage = (housing / total) * 100
    transportation_percentage = (transportation / total) * 100
    entertainment_percentage = (entertainment / total) * 100

    data = [food_percentage, clothing_percentage, housing_percentage, transportation_percentage, entertainment_percentage]
    labels = ["food", "clothing", "housing", "transportation", "entertainment"]
    colors = ["red", "green", "blue", "yellow", "orange"]

    plt.pie(data, labels=labels, colors=colors, autopct=lambda i: func(i, [food, clothing, housing, transportation, entertainment]))
            #"%.2f%%")
    plt.title("Total Expense Categories")
    plt.show()