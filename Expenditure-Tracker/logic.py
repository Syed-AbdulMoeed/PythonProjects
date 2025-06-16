import pandas as pd
import datetime
import matplotlib.pyplot as plt


def num_input():
    while True:
        try:
            return int(input("Enter the cost of your purchase: "))
        except (ValueError):
            print("Please Enter a number")


def add_expense(df, category, name, cost, date):
    id = 1 + df.shape[0]
    #creat dict to turn into pd df row
    row = { 'category': category, 'name' : name, 'cost':cost, 'date':date, 'id':id}

    return pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    


months = {'January': 1,'February':2,'March':3,'April':4,
          'May':5,'June':6,'July':7,'August':8,
          'September':9,'October':10,'November':11,'December':12}


def delete(df, ids):
    df.drop(df[df['id'].isin(ids)].index, inplace=True)
    df.reset_index(drop=True, inplace=True)


def most_spent(df):
    n = df.shape[0]
    if n > 4:
        return df.sort_values('cost', ascending=False).head(5)
    elif n == 0:
        return None
    else:
        return df.sort_values('cost', ascending=False).head(n)

def view_df(df):
    return [(row.name, row.category, row.cost, row.date) for row in df.itertuples(index=False)]



def view_month(df, mon):
    return df[df['date'].dt.month == mon]


def monthly_summary(df):
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    monthly = df.groupby(df['date'].dt.to_period('M'))['cost'].sum()
    result = [(name, total)for name, total in monthly.items()]
    return result
        
def save_csv(df):
    df.to_csv('expenses.csv', index=False)

def group(df):
    return  df.groupby(df['date'].dt.to_period('M'))['cost'].sum()


def menu(df, num):
    print('1 to view df')
    print('2 to add expense')
    print('3 to delete')
    print('4 to view highest')
    print('5 to view monthly')
    options = [1,2,3,4,5]
    while True:
        try:
            choice = int(input())
            if choice in options:
                break
            else:
                print("enter a correct number")
        except(TypeError, ValueError):
            print("Please enter a valid number")
    if choice == 1:
        view_df(df)
    elif choice == 2:
        add_expense(df, num)
    elif choice == 3:
        delete()
    elif choice == 4:
        print(most_spent(df))
    elif choice == 5:
        monthly_summary(df)


def read_csv():
    costs = pd.read_csv('expenses.csv')
    costs['id'] = costs.index + 1
    costs['date'] = pd.to_datetime(costs['date'])
    costs['date'] = costs['date'].dt.strftime('%Y-%m-%d')
    return costs



def main():
    costs = pd.read_csv('expenses.csv')
    costs['id'] = costs.index + 1
    costs['date'] = pd.to_datetime(costs['date'])
    num = costs.shape[0]
    category_costs = costs.groupby('category')['cost'].sum()
    print(category_costs)
    #category_costs.plot.pie()
    #plt.show()
    

def chart(df):
    category_costs = df.groupby('category')['cost'].sum()
    category_costs.plot.pie(shadow=True)
    plt.title('Cost by Category')
    plt.ylabel(None)
    plt.show()


def sort(df):
    return df.sort_values('cost', ascending=False)



#only April
#april = test[test['date'].dt.month == 4]





'''
test['Weeks'] = test['date'].dt.isocalendar().week

april = test[test['date'].dt.month == 4]
print(test.sort_values('date'))

print(test.loc[0].category)
print(test.sort_values('cost', ascending=False).head(1))
'''

