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

sql = "SELECT type, count(*) from airport"
sql += " where iso_country ='" + maakoodi + "'group by type"



kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()
for rivi in tulos:
    print(f"{rivi[0]} on {rivi[1]} kappaletta.")