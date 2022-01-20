# Hylkyilmoitus backend
[![GitHub Actions](https://github.com/Sukellusilmoitus/backend/workflows/CI/badge.svg)](https://github.com/Sukellusilmoitus/backend/actions)
[![codecov](https://codecov.io/gh/Sukellusilmoitus/backend/branch/master/graph/badge.svg)](https://app.codecov.io/gh/Sukellusilmoitus/backend)

## Usage

Make sure you have Python 3.8 or higher and pip installed. Activate the virtual environment and install the dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r ./requirements.txt
```

After this you can start the api

```bash
python3 src/index.py
```

If `curl http://localhost:5000/api/helloworld` is successful, the api is up and running.

## Definition of done
Scrumin mukaisesti projektissa toteutetaan backlogista löytyvät user storyt, 
joille on jokaiselle määritelty hyväksymiskriteerit.
Projektin product- ja sprint-backlogit ja siten myös hyväksymiskriteerit löytyvät tästä sheetistä: [backlogit](https://helsinkifi-my.sharepoint.com/:x:/g/personal/amikko_ad_helsinki_fi/EaUHpV9XQy1BmeSrSOFVoi8BKp4hDY_YXGRn8sG6nbl1oA?rtime=T01JVzDb2Ug)

Hyväksymiskriteerit testataan käyttäen Robot-frameworkia.
Koodia testataan kattavasti myös unit testeillä.
Koodityyli noudattaa lintin avulla määriteltyjä sääntöjä.

Asiakas voi seurata koodin ja testien tilannetta CI-palvelusta:
* Frontend: [codecov](https://app.codecov.io/gh/Sukellusilmoitus/frontend)
* Backend: [codecov](https://app.codecov.io/gh/Sukellusilmoitus/backend)

Koodin arkkitehtuuri on suunniteltua ja perusteltua,
pyrkimyksenä on mahdollisimman hyvä ylläpidettävyys pitämällä koodi selkeänä.

### Tarkistuslista User Storylle
* Tuotettu koodia suunnitelluille toiminnallisuuksille
* User storyn vaatimuksiin vastattu
* Projekti käynnistyy ilman virheitä
* Unit testit kirjoitettu ja läpäisty
* Toiminnallisuus on testattu hyväksymistesteillä
* Refraktorointi on valmis
* Product ownerin mielestä toiminnallisuus on valmis

### Tarkistuslista Sprintille
* Definition of done sprintin user storyille täytetty
* Kaikki unit testit läpäisty
* Linttaus läpäisty
* Backlog on päivitetty
* Kaikki bugit on korjattu
* Sprintin toteutettu toiminallisuus käyty läpi Product Ownerin kanssa
* Sprinttiin liittyvät "to do" asiat valmiita

### Tarkistuslista viimeiselle Releaselle
* Koodi on valmista
* Kaikki testit läpäisevät
* Kaikki hyväksymiskriteerit täyttyvät
* Ryhmä on hyväksynyt releasen
* Ei keskeneräistä työtä releasen mukana
* Kaikki DoD asetetut vaatimukset täyttyvät

## Ohjelman viimeisin versio

...
tähän mennessä valmiit ominaisuudet on listattu projektin backlogeissa.

## Ohjelman käyttöohje

......

### Asennus ja käynnistys


.....

### Käyttöliittymä

......
