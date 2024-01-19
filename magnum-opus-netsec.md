### Stéphane Van den Broeck
# Magnum Opus Network Security

### Github links:
- [https://github.com/stephanevdb/VigilantEye-Master](https://github.com/stephanevdb/VigilantEye-Master)
- [https://github.com/stephanevdb/VigilantEye-Worker](https://github.com/stephanevdb/VigilantEye-Worker)

## VigilantEye
VigilantEye is een Python webapp gebouwd met Flask, Gebruikmakend van een master en worker node. Hiermee kan je verschillende scans uit te voeren met zowel ingebouwde modules als eigen modules die zijn toegevoegd aan de MODULES folder.

## Ingebouwde modules
Alle modules werken indien mogelijk in ipv4 en ipv6.

- Ping
- Traceroute

### Prerequisites

- Python (3.11 of hoger)
- Communicatie tussen de master en worker op poorten `8666` en `8667`

### Installatie

Installeer de benodigde dependencies:

```bash
pip install -r requirements.txt
```

## Docker

Voor instructies over het gebruik van VigilantEye met Docker, raadpleeg de docker documentatie [https://github.com/stephanevdb/VigilantEye-Master/blob/main/DOCKER.md](https://github.com/stephanevdb/VigilantEye-Master/blob/main/DOCKER.md).

## Gebruik

Start de master:

```bash
python app.py
```

De web GUI is toegankelijk op poort `8666` van de master.

Start een worker node nadat de master is gestart.

## Werkpunten

Oorspronkelijk wou ik met een queue systeem werken maar ben hiertoe niet geraakt wegens tijdgebrek. Ook had ik graag nog enkele extra modules uitgewerkt.




