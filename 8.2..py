import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='airport',
    user='root',
    password='juhannus',
    autocommit=True
    )

maakoodi = input("Kerro haettava maakoodi (esimerkiksi FI): ")

sql = "SELECT code from airport where country = '" + maakoodi + "'"


kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()
for rivi in tulos:
    print(f"{rivi[0]}")