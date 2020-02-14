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
Padel Hall of Fame tarjoaa mahdollisuuden järjestää padel turnauksia tai yksittäisiä pelejä. Käyttäjä voi valita 3-N määrän
osallistujia turnaukseen ja rajata halutessaan osallistujia taitotason mukaan, yksittäiseen otteluun käyttäjä voi valita 2 tai 4 pelaaja. 
Jokaisesta turnauksesta tai ottelusta laaditaan esite, josta selviää turnauksen nimi, aika, paikka, pelaajamäärä, vaadittu taitotaso ja
osallistumismaksu.


Muut käyttäjät voivat ilmoittautua, osallistuminen vahvistuu vain jos käyttäjällä on vaadittu määrä saldoa tilillään. Käyttäjä
voi lisätä saldoa tililleen, saldon laskutus kuulu tämän järjestelmän piiriin.

#### Toimintoja
  * Kirjautuminen
  * Pelin tai turnauksen luonti ja muokkaus
  * Vapaiden kenttien katselu ja varauksen teko
  * Varausmaksun teko
  * Ilmoittautuneiden luettelo
  * Kenttävarauksen peruuttaminen asiakkaan toimesta
  * Pelin tai turnauksen peruutus asiakkaan toimesta
  * Pelin tai turnauksen peruutus yrityksen toimesta

### Dokumentaatio

#### Tietokantakaavio
![alt text](https://github.com/larikkai/PHoF/blob/master/documentation/Tietokantakaavio.jpg "Tietokantakaavio")

[Käyttötapaukset](https://github.com/larikkai/PHoF/blob/master/documentation/user_storyt.pdf "Käyttötapaukset")

