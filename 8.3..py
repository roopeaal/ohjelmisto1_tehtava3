import mysql.connector
from geopy.distance


def kissa():
    sql = "SELECT name from airport where ident = '" + icao + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for rivi in tulos:
        print(f"{rivi[0]}")


yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='airport',
    user='root',
    password='juhannus',
    autocommit=True
    )

icao1 = input("Kerro ensimmäisen lentokentän ICAO-koodi: ")
icao2 = input("Kerro toisen lentokentän ICAO-koodi: ")
kissa()