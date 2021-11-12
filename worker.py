import sqlite3 as sq



def mainA1(query, jadval,m=''):
    conn = sq.connect('source1.db')
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM {jadval}')
    natija = cursor.fetchall()


    n = 2

    kalitlar = []
    qiymatlar = []

    dict1 = {}

    for x in natija:
        for i in x:
            if n % 2 == 0:
                kalitlar.append(i)
            else:
                qiymatlar.append(i)
            n += 1



    a = 0
    natija = ''

    for i in kalitlar:
        dict1[i] = qiymatlar[a]
        a += 1

    a = 1

    for i in query:
        natija += dict1[i]
        if 'morze' in m:natija += ' '

    return natija



def alisa(query, jadval,file_joylashuv='source1.db'):
    conn = sq.connect(file_joylashuv)
    cursor = conn.cursor()

    cursor.execute(f'SELECT * FROM {jadval}')

    natija = cursor.fetchall()

    n = 2

    kalitlar = []
    qiymatlar = []

    dict1 = {}

    for x in natija:
        for i in x:
            if n % 2 == 0:
                kalitlar.append(i)
            else:
                qiymatlar.append(i)
            n += 1



    a = 0

    for i in kalitlar:
        dict1[i] = qiymatlar[a]
        a += 1

    return dict1[query]
