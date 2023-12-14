import mysql.connector
import csv

def hae_tiedot():
    # Tietokannan konfiguraatiot
    config = {
        "host": "172.20.241.9",
        "user": "dbaccess_ro", 
        "password": "vsdjkvwselkvwe234wv234vsdfas",
        "database": "measurements"
    }

    # Määritä groupid
    groupid = 17

    try:
        # Yhdistä tietokantaan
        conn = mysql.connector.connect(**config)

        # Luo kursori
        cursor = conn.cursor()

        # Suorita SQL-kysely
        query = "SELECT * FROM rawdata WHERE groupid = %s"
        cursor.execute(query, (groupid,))

        # Avaa CSV-tiedosto kirjoitusta varten
        with open('mysqltiedot.csv', 'w', newline='') as file:
            writer = csv.writer(file)

            # Kirjoita rivit tiedostoon
            for row in cursor:
                writer.writerow(row)
                print(row)

    except mysql.connector.Error as err:
        print("Virhe: ", err)

    finally:
        # Sulje yhteys
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    hae_tiedot()
