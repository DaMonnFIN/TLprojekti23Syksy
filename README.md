# Tietoliikenteen sovellusprojekti 2023 syksy

## Projektiin osallistujat:
## Taneli Huikari ja Oliver Jäälehto

## Kuvaus
Tässä projektissa kehitetään järjestelmä, joka hyödyntää nRF5340 Development Kit -kehitysalustaa anturidatan keräämiseen ja langattomaan siirtoon. Kehitetty client-ohjelmisto mittaa anturidataa, kuten asentoa, ja lähettää tiedot langattomasti IoT-reitittimen kautta Oamkin MySQL-tietokantaan. Tietokantaan tallennettu data on saatavilla TCP-sokettirajapinnan kautta, ja sitä voidaan hakea yksinkertaisen HTTP API:n avulla. Projektissa keskitytään erityisesti anturidatan analysointiin ja hyödyntämiseen koneoppimistarkoituksiin, käyttäen K-Means algoritmia asentoanturin tilan tunnistamiseen ja tulkitsemiseen.

#Projektin kuvaus ja tavoitteet voivat tarkentua ja muuttua projektin edetessä.

## Projektissa käytettävät teknologiat ja opittavat taidot

### Laitteistot ja alustat
- **nRF5340 Development Kit**: Anturidatan, kuten kiihtyvyyden ja asennon, mittaus sekä langaton tiedonsiirto.
- **Raspberry Pi**: Toimii IoT-reitittimenä, joka välittää kerätyn anturidatan MySQL-tietokantaan.

### Käyttöjärjestelmät ja työkalut
- **Windows**: Peruskäyttö/pääkäyttöjärjestelmä.
- **Linux**: Käytetään palvelimien ja tietokantojen hallintaan, sisältäen komentorivin käytön ja skriptauksen.
- **GitBash**: Käytetään Git-komentojen suorittamiseen Windows-ympäristössä.

### Ohjelmointikielet ja kehitysympäristöt
- **Python**: Käytetään datan käsittelyyn, tiedostojen käsittelyyn, virheidenkäsittelyyn sekä K-Means algoritmin toteutukseen.
- **SQL**: Tietokantojen käsittely ja hallinta, tietojen haku ja manipulointi MySQL-tietokannassa.
- **C**: nRF5340 Development Kitin ohjelmointi ja anturidatan kerääminen.
- **Visual Studio Code**: Suositeltu kehitysympäristö koodin kirjoittamiseen ja projektin kehittämiseen.
- **Markdown**: Readme tiedoston tekstit.

### Tietokantaohjelmistot
- **MySQL**: Tietokannan hallinta, datan tallennus ja TCP-sokettirajapinnan kautta tapahtuva datan välitys.

### Datan analysointi ja koneoppiminen
- **K-Means algoritmi**: Käytetään asentoanturin tilan ryhmittelyyn ja tunnistamiseen, mahdollistaen tarkan ja tehokkaan asennon seurannan.

### Versionhallinta ja yhteistyö
- **Git ja GitHub**: Koodin versionhallinta, dokumentaation ylläpito, haara- ja yhdistämisoperaatiot sekä konfliktien ratkaiseminen.
- **GitHub Kanban taulu**: Projektinhallinta ja tehtävien seuranta.

### Yhteistyötyökalut
- **Discord**: Tiimin välinen kommunikointi ja tiedostojen jako.
- **Whatsapp**: Tiimin välinen kommunikointi  ja tiedostojen jako.
