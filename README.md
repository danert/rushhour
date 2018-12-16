# Rush Hour (Media Maffia)

Rush Hour is een puzzel waarin een rode auto staat: de jouwe. Deze moet in zo min mogelijk stappen naar de uitgang geleid worden. Echter, andere voertuigen versperren de weg; auto's van twee eenheden lang en trucks van drie eenheden lang die alleen in hun rijrichting bewogen mogen worden. Ze mogen niet draaien. Kortom: het is de bedoeling om de rode auto naar buiten te leiden met zo min mogelijk stappen. De borden verschillen in formaat: 6x6, 9x9 en 12x12 (zie afbeelding).


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

### Uitleg per algoritme
Voor de uitleg van elk apart algoritme, zie _'algorithms'_ map.

## Auteurs

* Daan Visser
* Duncan Vrösch
* Farginda Muhammad

## Dankwoord

* Minor Programmeren van de UvA
