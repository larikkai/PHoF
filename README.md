# Padel Hall of Fame

## Aineopintojen harjoitustyö: tietokantasovellus, kevät 2020
Sovellus on Helsingin yliopiston tietojenkäsittelytieteeen kandiohjelman kurssilla Aineopintojen harjoitustyö: tietokantasovellus.

### Heroku
[Padel Hall of Fame - Heroku](http://padel-hall-of-fame.herokuapp.com/ "Heroku-linkki")

#### Testitunnukset
| Usertype        | Username      | Password        |
| :-------------: |:-------------:| :-------------: |
| Admin           | admin         | test123         |
| User            | test_user1    | test123         |

### Kuvaus
Padel Hall of Fame tarjoaa käyttäjille mahdollisuuden osasllistua ja järjestää padel turnauksia tai yksittäisiä pelejä. Käyttäjä voi valita 3-N määrän
osallistujia turnaukseen, yksittäiseen otteluun käyttäjä voi valita 2 tai 4 pelaaja. Osallistujamäärän lisäksi käyttäjä voi määrittää tapahtumalleen nimen.
Kun tapahtumaan on liittynyt vaadittu määrä pelaajia voi tapahtuman järjestäjä asettaa tuloksen, jonka jälkeen tapahtuma on päättynyt ja se tilastoidaan. 
Käyttäjä voi liittyä muiden käyttäjien järjestämiin tapahtumiin jos niissä on tilaa ja poistua jos ottelu ei ole vielä täynnä. Etu- ja uutissivulla käyttäjä voi tutustua uutisaiheisiin.

Admin käyttäjät voivat peruskäyttäjien toimintojen lisäksi luoda sisältöä uutisten muodossa. Käytössä on oma erillinen admin-paneeli sivuston ylläpitootimintoja varten.

#### Toimintoja
  * Ilmoittautuminen
  * Kirjautuminen
  * Uutiset
  * Pelin tai turnauksen luonti ja muokkaus
  * Vapaiden kenttien katselu ja varauksen teko
  * Ilmoittautuneiden luettelo
  * Pelin tai turnauksen peruutus käyttäjän toimesta
  * Pelin tai turnauksen peruutus adminin toimesta

### Dokumentaatio

[Tietokantakaavio](https://github.com/larikkai/PHoF/blob/master/documentation/database_diagram.jpg "Tietokantakaavio")

[Käyttötapaukset](https://github.com/larikkai/PHoF/blob/master/documentation/user_storyt.md "Käyttötapaukset")

