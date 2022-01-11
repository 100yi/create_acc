from simbols import *

import requests, os, pathlib, random, json, datetime, smtplib


def create_acc(type_mail='@mail.ru'):

    if not type_mail.startswith('@'):
        print('bad type mail')
        return None

    password = ''
    for i in range(5):
        password += random.choice(l1)
        password += random.choice(l2)
        password += random.choice(l3)
        password += random.choice(l4)
    email = ''
    for i in range(9):
        if i % 2 == 0:
            email += random.choice(l4)
        email += random.choice(l1)
        if i != 0 and i % 3 == 0:
            email += '_'
    email += type_mail
    print(email, password)
    time_create = datetime.datetime.now()
    data = {'email': email, 'password': password, 'no_importtant_data': {'lfi': 1}}
    with open('data.json', 'r') as file:
        r = json.load(file)
        r.append(data)
    with open('data.json', 'w') as file:
        json.dump(r, file, indent=4)


def main():
    create_acc()


if __name__ == '__main__':
    main()
