import pickle
import os

def counter(user):
    with open('data.pickle', 'rb') as f:
        data = pickle.load(f)
    if user == "Jura":
        pop = data.pop(user)
        data.update({user:pop+1})
        with open('data.pickle', 'wb') as f:
            pickle.dump(data, f)
        print(data)
    elif user == "Kirill":
        pop = data.pop(user)
        data.update({user: pop + 1})
        with open('data.pickle', 'wb') as f:
            pickle.dump(data, f)
        print(data)
    else:
        pass

if os.path.exists('/home/kirill/PycharmProjects/TelegramBot/data.pickle'):
    while True:
        user = input("Enter username: ")
        counter(user)

else:
   print("Not exist")
   data = {"Jura":0, "Kirill":0}
   with open('data.pickle', 'wb') as f:
       pickle.dump(data, f)
   while True:
        user = input("Enter username: ")
        counter(user)