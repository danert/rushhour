#### Random Algoritme (geeft een oplossing voor alle borden)
Met het gebruik van het random-algoritme hebben we voor ieder bord een oplossing gevonden. Dit algoritme zoekt een willekeurige auto op het bord en verplaatst hem over een willekeurige afstand. Dit algoritme hoeft niks op te slaan (in tegenstelling tot de andere algoritmes in onze vergelijking) Dit zorgt er dan ook voor dat de random algoritme het snelst een oplossing vindt. Het random algoritme zet willekeurige stappen en hoeft alleen deze stappen (de route) te onthouden terwijl de breadth-first langzaam een tree afgaat die steeds groter wordt. 

#### Random Algoritme (oneindig)
In dit algoritme wordt het random algoritme aangeroepen, maar wordt dit, in tegenstelling tot het normale random algoritme, oneindig gedaan. Als grens wordt de kortste oplossing genomen: als deze grens tijdens het berekenen van een uitkomst wordt bereikt, wordt de berekeing gestopt en start het random algoritme opnieuw. Wordt er een kortere oplossing gevonden dan de kortste oplossing tot nu toe, dan wordt deze geprint en wordt de grens bijgesteld tot de nieuwe kortste oplossing.

#### Breadth-First Algoritme (geeft tot nu toe op de eerste drie borden een oplossing)
Het breadth-first algoritme vindt gegarandeerd de best mogelijke oplossing. Met de beste oplossing wordt het minst aantal stappen bedoeld. Dit algoritme vormt een tree met alle mogelijke moves, waarbij hij elke generatie stap voor stap afgaat. Het nadeel van dit algoritme is dat deze vrij langzaam te werk gaat. Voor de eerste drie borden met een grootte van 6x6 vindt het algoritme nog binnen een paar minuten de beste oplossing, aangezien de statespace relatief klein is (kleiner dan een miljoen). Bij de grotere borden duurt het vinden van een oplossing significant langer. De statespace voor deze borden is dan namelijk een getal met bijna 20 nullen.

#### Depth-First
Voor de borden groter dan 6x6 komt een depth-first algoritme beter van pas. Dit algoritme gaat net als de breadth-first een tree af, maar de depth-first slaat slechts één pad op in zijn geheugen. Hierdoor is het algoritme veel sneller dan de breadth-first, maar deze garandeert niet dat de beste oplossing gevonden wordt. Aan de depth-first kan een grens (bound) worden meegegeven om het algoritme op die manier sneller en efficiënter te maken: de grens (bound) wordt gesteld op de korste oplossing die is gevonden met de andere algoritmes. 