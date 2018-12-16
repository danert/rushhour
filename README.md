# Rush Hour (Media Maffia)

Rush Hour is een puzzel waarin een rode auto staat: de jouwe. Deze moet in zo min mogelijk stappen naar de uitgang geleid worden. Echter, andere voertuigen versperren de weg; auto's van twee eenheden lang en trucks van drie eenheden lang die alleen in hun rijrichting bewogen mogen worden. Ze mogen niet draaien. Kortom: het is de bedoeling om de rode auto naar buiten te leiden met zo min mogelijk stappen.


## Aan de slag

### Vereisten

Deze codebase is volledig geschreven in [Python3.6.3](https://www.python.org/downloads/). In requirements.txt staan alle benodigde packages om de code succesvol te draaien. Deze zijn gemakkelijk te installeren via pip dmv. de volgende instructie:

```
pip install -r requirements.txt
```

### Structuur

???

### Test

Om de code te draaien met de standaardconfiguratie (bv. brute-force en voorbeeld.csv) gebruik de instructie als volgt. 

```
python game.py [probleem nummer] [algoritme] [eventuele bound voor depth first]
```

Bijvoorbeeld voor spel nummer 4, met een depth first algoritme en een bound van 30:

```
python game.py 4 df 30
```


Deze tabel laat de kortste oplossingen zien die zijn gevonden met de aangegeven algoritmes.

| problem  | random | breadth-first | depth-first |
| ------------- | ------------- | ------------- | ------------- |
| 1  | 453  |   32  |       |
| 2  | 51  |    14  | 1651 |
| 3  | 117  |   20 |  395 |
| 4  | 432  |   26  |       |
| 5  | 294  |     |       |
| 6  | 183  |     |       |
| 7 | 318 | |       |

#### Visualisatie oplossing probleem 2 (breadth-first)
<img src="https://github.com/danert/rushhour/blob/master/doc/rushhour_bf_prob2.gif" width="50%" height="50%"/>

#### Uitleg per algoritme
Voor de uitleg van elk apart algoritme, zie _'algorithms'_ map.

#### Vergelijking algoritmes
Het random algoritme kan men het best gebruiken als er gegarandeerd een oplossing gevonden moet worden. Het gaat hierbij niet om de beste, niet de meest efficiënte, maar wel de snelste. Verder kan dit algoritme alle borden (snel) oplossen. In vergelijking met het random algoritme vindt het breadth-first algoritme gegarandeerd de beste en kortste oplossing. Dit algoritme werkt in vergelijking met het random en depth-first algoritme het traagst en kan om deze reden niet alle borden oplossen. Tot slot zorgt het depth-first algoritme altijd voor een oplossing. Dit is niet de beste en kortste oplossing, maar hij vindt wel sneller een oplossing dan het breadth-first algoritme.

We kunnen de uitkomsten van het random-algoritme goed gebruiken om de depth-first te optimaliseren. Door de kortste uitkomst van het random-algoritme te nemen kunnen we dit gebruiken als upper bound. Als de depth-first een pad in de tree afgaat dat meer stappen nodig heeft dan die kortste oplossing kan hij doorgaan naar het volgende pad. 

<img src="https://github.com/danert/rushhour/blob/master/doc/20181207014853.jpg" width="100%" height="100%"/>

Hierboven zie je een vergelijking tussen de kortst gevonden oplossingen van twee verschillende algoritmes.

<img src="https://github.com/danert/rushhour/blob/master/doc/20181207025833.jpg" width="100%" height="100%"/>

De grafiek hierboven laat het verschil zien tussen het aantal borden wat ieder algoritme 'bekijkt' voordat er een oplossing is gevonden. Omdat het random algoritme steeds één bord per keer bekijkt en hiermee willekeurig een zet doet, is het aantal borden dat 'bekeken' is gelijk aan de oplossing. Het breadth-first algoritme bekijkt van ieder bord de andere borden die hieruit gevormd kunnen worden en daarom is dit getal veel groter dan die van het random algoritme. Bij de borden van 9x9 en 12x12 zal dit verschil nog groter zijn, aangezien er veel meer auto's, moves en dus ook meer bordformaties zijn.
