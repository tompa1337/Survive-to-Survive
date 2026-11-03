# Survive to Survive – Designdokument (v0.1)

> Överlevnadsspel på stenåldern för **1–6 spelare i co-op**.
> En blandning av **Age of Empires** (by + tidsåldrar), **Minecraft** (samla, tillverka, bygga fritt) och **Far Cry** (öppen värld i förstapersonsvy, jakt, fiendeläger).

---

## 1. Pitch

Ni är en liten stam som har drivits iväg från era jaktmarker när istiden kryper söderut. I en öppen, farlig värld måste ni samla, jaga och bygga upp en by, och föra stammen genom tidsåldrarna innan isen når er.

**Spelkänsla:** Spänningen när man smyger på en mammut tillsammans, lugnet vid lägerelden när man bygger, och paniken när en rivaliserande stam anfaller i mörkret.

## 2. Kärnloop

```
  Utforska ──► Samla / Jaga ──► Tillverka / Bygga ──► Utveckla byn (tidsålder)
     ▲                                                        │
     └──────────── Nya områden, djur och hot låses upp ◄──────┘
```

- **Kort loop (minuter):** Samla trä och sten → tillverka ett verktyg → samla snabbare.
- **Mellanloop (en kväll):** Jaga, bygga ut byn och försvara den mot ett anfall.
- **Lång loop (flera kvällar):** Ta stammen genom fyra tidsåldrar innan istiden kommer.

## 3. Tidsåldrar (från Age of Empires)

| # | Tidsålder | Nytt som låses upp | Krav för att gå vidare |
|---|-----------|--------------------|------------------------|
| 1 | **Eldens tid** (tidig stenålder) | Lägereld, vindskydd, stenyxa, spjut | Ett "eldhjärta" (stor eld) + 50 trä, 30 sten |
| 2 | **Jägarnas tid** | Pilbåge, fällor, skinnkläder, torkställning, palissad | Fälla en mammut tillsammans |
| 3 | **Böndernas tid** | Åkrar, tama djur, lerkrukor, långhus, vakttorn | Långhus + förråd fullt med mat |
| 4 | **Bronsens gryning** (slutmål) | Smedja, bronsvapen, stenmonument | Bygga stenmonumentet → "överlevt istiden" |

Att gå upp en tidsålder kräver att **hela gruppen** bidrar med resurser till byns eldhjärta.

## 4. Resurser

| Resurs | Var | Används till |
|--------|-----|--------------|
| Trä | Träd, buskar | Byggnader, eld, skaft |
| Sten | Stenblock, flodbäddar | Verktyg, grunder, murar |
| Flinta | Grottor, klippor | Vassa eggar, pilspetsar |
| Skinn | Djur | Kläder (värme), tält, säckar |
| Ben | Djur | Nålar, smycken, verktyg |
| Kött / bär / rötter | Jakt, insamling | Mat (måste tillagas över eld) |
| Lera | Flodstränder | Krukor, väggar (tidsålder 3) |
| Koppar + tenn | Djupa grottor | Brons (tidsålder 4) |

## 5. Överlevnad

- **Hunger:** sjunker hela tiden. Rått kött ger lite och kan göra en sjuk, tillagat ger mycket.
- **Värme:** sjunker på natten, i regn och nära isen. Höjs vid eld och med skinnkläder.
- **Hälsa:** skador från djur, fiender och fall.
- **Elden är spelets hjärta.** Den värmer, lagar mat, skrämmer bort rovdjur och lyser upp natten. Den måste matas med trä, annars slocknar den.
- **Istiden:** för varje säsong flyttar isgränsen närmare på kartan. Det håller tempot uppe och tvingar fram framsteg.

## 6. Roller i co-op (6 spelare)

Rollerna är **mjuka**: alla kan göra allt, men varje roll har ett eget verktyg och en bonus. Man kan byta roll vid byns eldhjärta.

| Roll | Startverktyg | Bonus | Kännetecken |
|------|--------------|-------|-------------|
| **Jägaren** | Spjut | +skada mot djur, spårar fotspår | Pälskappa, ansiktsmålning |
| **Samlaren** | Korg + grävpinne | +mängd bär/rötter, hittar örter | Stor korg på ryggen |
| **Byggaren** | Stenyxa | Bygger snabbare, bär mer trä | Bred, trä på axeln |
| **Hantverkaren** | Flintknacka | Tillverkar bättre verktyg | Verktygsbälte, lerfläckar |
| **Spejaren** | Slunga + horn | Springer snabbare, markerar fiender åt laget | Lätt utrustning, fjädrar |
| **Shamanen** | Stav + örtpung | Helar, ser i mörker, kan "läsa" vädret | Benhalsband, kranium på staven |

**Saker som kräver flera spelare:**
- Fälla en mammut: en spejar och lockar, två driver den mot fällan, resten anfaller.
- Flytta monumentstenar: 4 personer bär tillsammans.
- Nattanfall: någon håller elden vid liv medan resten försvarar palissaden.

## 7. Världen (från Far Cry)

- **Öppen karta** med biomer: tallskog, älvdal, myr, klippiga höglandet, grottor och isgränsen i norr.
- **Dag och natt:** natten är mörk på riktigt. Facklor och eld är livsviktiga.
- **Djur:**
  - Fredliga: hjort, vildsvin, kanin, uroxe
  - Farliga: varg (i flock), grottbjörn, sabeltandad tiger
  - Jättar: ullig mammut, ullhårig noshörning
- **Rivaliserande stammar:** har läger på kartan som kan erövras (precis som utposter i Far Cry). De skickar räder mot er by.
- **Smygande:** högt gräs, vind och lukt. Djur flyr om de känner lukten av er i vinden.

## 8. Bygga (från Minecraft)

- Fritt byggande med **delar** (stockar, väggar av ris, stenblock, tak av skinn), inte bara färdiga hus.
- Färdiga **nyckelbyggnader** som låser upp funktioner: eldhjärta, förråd, torkställning, verkstad, långhus, vakttorn, smedja.
- Byn kan förstöras vid anfall. Försvar som palissad och fällor gör skillnad.

## 9. Teknik

| Del | Förslag |
|-----|---------|
| Prototyp | Webbläsare (three.js), finns i `prototype/` för att snabbt testa känslan |
| Riktigt spel | **Godot 4** (gratis, lätt att lära sig, inbyggt nätverk) eller **Unreal Engine 5** (snyggast, starkt multiplayer, tyngre) |
| Multiplayer | Värd-klient (en spelare är värd), upp till 6 spelare. Senare dedikerad server |
| 3D-modeller | Blender, enkla former + toon-shading och svarta konturer (grottmålningsstil) |

## 10. Grafisk stil: "Levande grottmålning"

**Hela spelet är målat som en grottvägg**: karaktärer, värld, menyer och ikoner. Det ger en stil som ingen annan har, och den är billigare att producera än realistisk 3D.

**Palett** (bara naturpigment):

| Färg | Hex | Används till |
|------|-----|--------------|
| Röd ockra | `#9a321e` | Jägaren, Shamanen, eld, bär, viktiga saker |
| Gul ockra | `#c98a1f` | Samlaren, solljus, mat |
| Kol | `#231812` | Byggaren, konturer, natt |
| Krita | `#f3e8cf` | Hantverkaren, ben, stjärnor |
| Umbra | `#6b3f22` | Spejaren, trä |
| Stenvägg | `#c99d72` | Mark, himmel på dagen, bakgrunder |

**Världen i 3D:**
- Toon-shading med 3 tonsteg och **svarta penselkonturer** runt allt.
- Mark och himmel i stenväggsfärger. Marken har en struktur med fläckar och sprickor, som en grottvägg.
- Träd i kol, umbra och mörk röd ockra. Stenar i krita. Bärbuskar i gul ockra med röda bär.
- **Målade stenar** står utspridda i världen med handavtryck, mammutar, jägare och spiraler. Det är stammens berättelser, och senare kan de bli ledtrådar eller uppdrag.
- Natten är kolsvart med stjärnor i ockra. Elden är röd och gul.

**Karaktärer:** varje roll skiljer sig åt på fyra sätt så att den känns igen direkt, även på avstånd: **färg, kroppsform, siluett och symbol**.

| Roll | Färg | Kroppsform | Siluett | Symbol |
|------|------|-----------|---------|--------|
| Jägaren | Röd | Lång, smal, omvänd triangel | Vargöron, spjut | Spjutspets |
| Samlaren | Gul | Liten, rund cirkel | Blomkrona, korg på ryggen | Tre bär |
| Byggaren | Svart | Kort, bred rektangel | Stock över huvudet | Stock |
| Hantverkaren | Vit med svart kontur | Romb, på knä | Spretig hårknut, flinta | Flintspets |
| Spejaren | Brun | Bara streck, längst | Tre fjädrar, slunga | Fotspår |
| Shamanen | Röd med vita prickar | Bred mantel, triangel uppåt | Jättestora hjorthorn | Spiral |

Referens: `art/grottmalning_roller.svg`. Äldre stilförslag finns i `art/karaktarer.svg` och `art/alternativ_a–d.svg`.

**Idé:** När stammen går upp en tidsålder målas en ny bild på väggen i byns grotta, så att stammens historia växer fram.

## 11. Färdplan

1. **Prototyp 0.1** ✅ Gå runt, samla trä och sten, tända eld, hunger och värme, dag och natt.
2. **Prototyp 0.2** ✅ Världen i grottmålningsstil, målade stenar, ny meny.
3. **Prototyp 0.3** ✅ Djur (varg, björn, vildsvin) med beteenden, jakt och slakt, stekt kött, verktygsfält med mushjul, verktyg synligt i handen (hand, stenyxa, spjut, fackla), byggande (lägereld, vindskydd, hydda, palissad, totempåle).
4. **Prototyp 0.4** ✅ Rollval, specialbyggnad för varje klass, karta (mini + stor), instruktionssten.
5. **Prototyp 0.5** ✅ Eldhjärtat (byggs stegvis, säker zon, återuppståndelse, rollbyte, gemensamt bränsle) och tidsålder 1 → 2 med pilbåge och skinnkläder.
6. **Prototyp 0.6:** Mammutjakt (målet i Jägarnas tid).
7. **Motorval:** flytta till Godot eller Unreal, få 2 spelare online samtidigt.
8. **Vertical slice:** tidsålder 1–2, 6 spelare, ett nattanfall, mammutjakt.

## 12. Prototyp 0.3 – hur det fungerar nu

**Verktyg** (byt med mushjulet eller 1–5, det valda verktyget syns i handen):

| Verktyg | Tillverkas | Effekt |
|---------|-----------|--------|
| Hand | – | Samlar och slår svagt |
| Stenyxa | C: 3 trä, 2 sten | Dubbel insamling, skada 8 |
| Spjut | V: 4 trä, 2 sten | Lång räckvidd (4,6 m), skada 15 |
| Fackla | T: 3 trä | Ljus, mindre kyla, vargar håller avstånd |
| Bygga | – | Spökbild av byggnaden, R byter, klick bygger |

**Djur:**

| Djur | Beteende | Ger |
|------|----------|-----|
| Varg | Flockar om 3. Jagar på natten, skygg på dagen. Rädd för eld och fackla | 1 kött, 2 skinn, 2 ben |
| Björn | Vaktar revir och jagar den som kommer nära. Rädd för eld | 5 kött, 4 skinn, 3 ben |
| Vildsvin | Fridfullt, men laddar när det blir skadat | 4 kött, 1 skinn, 1 ben |

**Byggnader:** Lägereld (5 trä, 3 sten), Vindskydd (8 trä, mindre nattkyla), Hydda (16 trä, 4 sten, 2 skinn, varm och vargar kommer inte in), Palissad (4 trä, stoppar djur), Totempåle (6 trä, 2 sten).

**Mat:** rått kött ger magont, så stek det vid elden med F. Stekt kött ger mest.

## 13. Klasser och specialbyggnader (prototyp 0.4)

Man väljer roll på startskärmen. Varje roll har en liten bonus och en **specialbyggnad som bara den rollen kan bygga**. I co-op behöver stammen alltså alla roller för att få allt.

| Roll | Bonus | ★ Specialbyggnad | Kostnad | Effekt |
|------|-------|------------------|---------|--------|
| Jägaren | +30 % skada mot djur | **Fällgrop** | 4 trä, 2 sten | Djur som går i den fastnar och tar 40 skada. Gillras om efter 20 s |
| Samlaren | +1 bär per plock | **Bärodling** | 3 trä, 4 bär | Växer fram 4 bär var 45:e sekund. Skörda med E |
| Byggaren | Byggen kostar 25 % mindre trä | **Vakttorn** | 14 trä, 4 sten | Visar alla djur inom 90 m på kartan |
| Hantverkaren | Verktyg kostar 1 trä mindre | **Verkstad** | 8 trä, 6 sten | E förbättrar verktyget i handen (2 ben, 1 sten), högst två gånger: + och ++ |
| Spejaren | Springer 15 % snabbare | **Varde** | 6 sten | E reser till nästa varde (snabbresa) |
| Shamanen | Läker dubbelt så snabbt | **Stencirkel** | 10 sten | Läker och värmer alla som står i den |

**Karta:** en minikarta uppe till höger och en stor karta med M. Kartan är målad i grottstil med höjdkurvor, sjön, träd, målade stenar, eldar och byggnader. Djur syns när de är nära dig, och överallt inom 90 m från ett vakttorn.

**Instruktionssten:** står vid startplatsen och visar alla recept, inklusive din rolls specialbyggnad. E öppnar en läsbar version.

## 14. Första tidsåldern och eldhjärtat (finns i prototyp 0.5)

**Tidsålder 1 – Eldens tid.** Stammen har just flytt och har ingenting. Målet är att slå läger och klara de första nätterna. Allt i prototypen hittills hör hit: samla, verktyg, eld, skydd, de första djuren och specialbyggnaderna. Tidsåldern är klar när:
1. stammen har byggt **eldhjärtat** tillsammans,
2. varje roll har byggt sin specialbyggnad, och
3. stammen har överlevt 3 nätter med eldhjärtat brinnande.

Då kommer **Jägarnas tid** (pilbåge, skinnkläder, mammutjakt).

**Eldhjärtat** är byns stora gemensamma eld och spelets mitt:
- **Byggs tillsammans:** alla lägger trä och sten i det (t.ex. 40 trä, 25 sten, 6 skinn). Ingen kan bygga det ensam. En stapel visar hur mycket som saknas.
- **Säker zon:** inom ljuscirkeln (ca 15 m) går inga rovdjur in, och man blir varm.
- **Återuppståndelse:** den som dör vaknar vid eldhjärtat.
- **Rollbyte:** här kan man byta roll.
- **Delad bränsle:** det slocknar om stammen slutar mata det. Då försvinner skyddet, och vargarna kommer.
- **Växer med stammen:** för varje tidsålder byggs det ut (stenring → stensatt härd med totem → stort eldhus) och en ny bild målas på grottväggen bredvid.
- **Lyft tidsåldern:** när kraven är uppfyllda offrar stammen resurser i elden och tidsåldern höjs.

**Så fungerar det i prototypen:**
- Eldhjärtats plats är markerad med röda flaggor nära starten. Tryck E där för att lägga i det du har. Stenar och stockar syns efter hand. Totalt krävs 40 trä, 25 sten och 4 skinn.
- När det är färdigt får man en stor eld med stenring, sittstockar och två totempålar. Inom cirka 15 m går inga djur in, och man blir varm. Den som dör vaknar här, men tappar maten den bar.
- E vid eldhjärtat öppnar en panel: **1** matar elden (5 trä = 300 s, max 900 s), **2** byter roll (1–6), **3** lyfter tidsåldern.
- Kravlistan syns högst upp på skärmen. Ensam räcker det att din egen specialbyggnad är byggd. I co-op ska alla rollers byggnader stå.
- Offret är 20 trä, 10 sten, 4 skinn och 4 ben. Därefter visas "JÄGARNAS TID" på skärmen, eldhjärtat växer, och en ring av resta stenar och två nya målade stenar dyker upp.
- **Nytt i tidsålder 2:** Pilbåge [B] (5 trä, 2 skinn), som skjuter pilar upp till 32 m och som träd stoppar, och Skinnkläder [K] (4 skinn, 2 ben), som halverar kylan på natten.

## 15. Öppna frågor

- Förstapersonsvy hela tiden, eller kan man växla till tredje person?
- Ska man kunna dö permanent, eller återuppstå vid eldhjärtat?
- Hur lång ska en hel spelomgång vara: en kväll eller flera veckor?
- Ska det finnas PvP (stam mot stam) senare, eller bara co-op?
