from _ast import Break
import sqlite3

conn = sqlite3.connect('ISa.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE Dolznosti
(
	ID_Dolznost INT PRIMARY KEY NOT NULL,
	NameDolznosti VARCHAR(45),
	KolvoRabDay INT,
	ZP INT NOT NULL
)
''')

cursor.execute('''
    CREATE TABLE Rabotniki
(
	ID_Rabotnik INT PRIMARY KEY NOT NULL,
	Surname VARCHAR (35),
	NameR VARCHAR (30),
	Dolznost_ID INT,
	FOREIGN KEY (Dolznost_ID) REFERENCES Dolznosti(ID_Dolznost)
)
''')

cursor.execute('''
    CREATE TABLE Zaprosi
(
	ID_Zaprosika INT PRIMARY KEY IDENTITY(1,1),
	Surname VARCHAR (35),
	NameR VARCHAR (30),
	Dolznost_ID INT
)
''')

cursor.execute('''
    CREATE TABLE Otdeli
(
	ID_Otdela INT PRIMARY KEY NOT NULL,
	NameOtdel varchar(55)
)
''')

cursor.execute('''
    CREATE TABLE Lekarstva
(
	ID_Lekarstva INT PRIMARY KEY NOT NULL,
	NameLekarstva varchar(45),
	Otdela_ID INT UNIQUE,
    FOREIGN KEY (Otdela_ID) REFERENCES Otdeli(ID_Otdela)
)
''')

cursor.execute('''
    CREATE TABLE Sootnoshenie
(
	ID_Sootnoshenie INT PRIMARY KEY NOT NULL,
	Otdela_ID INT NOT NULL,
	Rabotnik_ID INT NOT NULL,
	FOREIGN KEY (Rabotnik_ID) REFERENCES Rabotniki(ID_Rabotnik),
    FOREIGN KEY (Otdela_ID) REFERENCES Otdeli(ID_Otdela)
)
''')

dolznosti = [(1, 'Грузчик', 6, 60000), (2, 'Сортировщик', 4, 35000), (3, 'Зам. Админа', 5, 70000),
             (4, 'Админ', 3, 80000), (5, 'Фасовщик', 6, 40000)]
cursor.executemany("INSERT INTO Dolznosti (ID_Dolznost, NameDolznosti, KolvoRabDay, ZP) VALUES (?, ?, ?, ?)", dolznosti)

otdeli = [(12, 'Твёрдые'), (48, 'МяEгкие'), (53, 'Жидкие'), (89, 'Газообразные')]
cursor.executemany("INSERT INTO Otdeli (ID_Otdela, NameOtdel) VALUES (?, ?)", otdeli)

rabotniki = [(1, 'Иванов', 'Андрей', 1), (2, 'Соколов', 'Владислав', 2), (3, 'Воробьёв', 'Михаил', 3),
             (4, 'Самарский', 'Александр', 1), (5, 'Пригожин', 'Евгений', 1), (6, 'Сергеев', 'Василий', 4),
             (7, 'Ситникова', 'Алёна', 5), (8, 'Прапоров', 'Евгений', 2)]
cursor.executemany("INSERT INTO Rabotniki (ID_Rabotnik, Surname, NameR, Dolznost_ID) VALUES (?, ?, ?, ?)", rabotniki)

lekarstva = [(1, 'Ибупранол', 12), (2, 'Лепоксин', 48), (3, 'Нурофен', 53), (4, 'Тантум Верде Форте', 89)]
cursor.executemany("INSERT INTO Lekarstva (ID_Lekarstva, NameLekarstva, Otdela_ID) VALUES (?, ?, ?)", lekarstva)

soot = [(1, 1, 12), (2, 2, 48), (3, 3, 53), (4, 4, 89), (5, 5, 53), (6, 6, 48), (7, 7, 12), (8, 8, 89), (9, 2, 53),
        (10, 8, 12)]
cursor.executemany("INSERT INTO Sootnoshenie (ID_Sootnoshenie, Rabotnik_ID, Otdela_ID) VALUES (?, ?, ?)", soot)

conn.commit()
conn.close()


def update:


def delete:


print("Аптека")
print("1. Зарегистрироваться")
print("2. Войти")
print("3. Войти как админ")
print("4. Выйти")
while True:
    try:
        a = int(input())
        break
    except ValueError:
        print("Пожалуйста, введите корректное число.")

if a == 4:
    print('ну лан бб')
    Break

if a == 1:
    print("Регистрация")
    print("Введите ваше имя: ")
    Name = input()
    print("Введите вашу фамилию: ")
    Family = input()
    print("Введите ваше отчество: ")
    Otchestvo = input()
    print("Введите вашу должность")
