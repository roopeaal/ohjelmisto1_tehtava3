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

tyyppien_kutsumanimet = {
    'balloonport': 'Ilmapallolaitureita',
    'closed': 'Suljettuja kenttiä',
    'heliport': 'Helikopterikenttiä',
    'large_airport': 'Isoja lentokenttiä',
    'medium_airport': 'Keskikokoisia lentokenttiä',
    'seaplane_base': 'Vesilentokenttiä',
    'small_airport': 'Pieniä lentokenttiä'
}

sql = "SELECT type, count(*) from airport"
sql += " where iso_country ='" + maakoodi + "'group by type"



kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()


for rivi in tulos:
    tyyppi = tyyppien_kutsumanimet.get(rivi[0], rivi[0])  # Haetaan suomenkielinen nimi sanakirjasta
    print(f"{tyyppi} on {rivi[1]} kappaletta.")