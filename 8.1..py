import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='airport',
    user='root',
    password='juhannus',
    autocommit=True
    )

icao = input("Kerro haettavan lentokentän ICAO-koodi: ")

sql = "SELECT name from airport where ident = '" + icao + "'"


kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()
for rivi in tulos:
    print(f"{rivi[0]}")