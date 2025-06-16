# have cards shown 
import pandas as pd
import random

def show_menu(df):
    while True:
        print('1 - Add Flash Card')
        print('2 - View Flash Cards')
        print('3 - Practice Mode') #goes to random or by category
        print('4 - Delete Card')
        print('5 - Search Cards')
        print('6 - Quit')
        while True:
            choice = num_input()
            if choice in [1, 2, 3, 4, 5, 6]:
                break
        if choice == 1:
            df = add_card(df)
        elif choice == 2:
            view_cards(df)
        elif choice == 3:
            practice(df)
        elif choice == 4:
            df = delete_card(df)
        elif choice == 5:
            search_card(df)
        else:
            break


def practice(df):
    print('1 - Random Practice')
    print('2 - By Category')
    while True:
        choice = num_input()
        if choice == 1:
            practice_random(df)
            break
        elif choice ==2:
            by_category(df)
            break
            
    



def add_card(df):
    question = input('Enter Question: ')
    answer = input('Enter Answer: ')
    category = input('Category: ')
    index = df.shape[0]
    row = {'category' : category,'index' : index,'question': question, 'answer': answer, 'correct_attempts' : 0, 'incorrect_attempts' : 0}
    df = pd.concat((df, pd.DataFrame([row])), ignore_index=True)
    df.to_csv('cards.csv', index=False)
    return df
    

def view_cards(df):
    for row in df.itertuples():
        print(f" {row.index} : ({row.category}) {row.question} : {row.answer} | Correct Attempts : {row.correct_attempts} | Incorrect Attempts : {row.incorrect_attempts}")


def practice_random(df):
    indexs = [ i for i in range(df.shape[0])] 
    while indexs:
        index = random.choice(indexs)
        indexs = work(df, index, indexs)
    df.to_csv('cards.csv', index=False)
    print('Completed!')



def by_category(df):
    #list of index of cards with given category
    options = df['category'].unique()
    print('Categories: ' , options)
    category = input('Enter Category: ')
    indexs = df[df['category']==category].index.tolist()
    if indexs:
        while indexs:
            index = random.choice(indexs)
            indexs = work(df, index, indexs)
            df.to_csv('cards.csv', index=False)
        print('Completed!')
    else:
        print('No result')


def del_index(index, indexs):
    for i,val in enumerate(indexs):
        if val == index:
            del indexs[i]
            return indexs


def work(df, index, indexs):
    print(df.loc[index, 'question'])
    answer = input('Answer :')
    if answer == str(df.loc[index, 'answer']):
        df.loc[index, 'correct_attempts'] += 1
        indexs = del_index(index, indexs)
    else:
        df.loc[index, 'incorrect_attempts'] += 1
    return indexs
    

def num_input():
    while True:
        try:
            return int(input('Enter Index: '))
        except:
            pass


def delete_card(df):
    view_cards(df)
    index = num_input()
    df = df[df['index']!=index]
    df = df.reset_index(drop=True)
    reset_index(df)
    df.to_csv('cards.csv', index=False)
    return df
    

def search_card(df):
    keyword = input('Enter keyword to search')
    print(df[df['question'].str.contains(keyword, case=False)])


def reset_index(df):
    df['index'] = df.index 


def main():
    df = pd.read_csv('cards.csv', dtype={'answer': str})
    show_menu(df)


main()
