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
| 3D-modeller | Blender, lågpolystil (enkla former, starka färger) för att hålla nere arbetet |

## 10. Grafisk stil

**Stiliserad lågpoly** med varma färger: ockra, bränd orange, mossgrönt och isblått. Tydliga silhuetter så att man ser direkt vem som är vilken roll, även på avstånd. Se `art/karaktarer.svg`.

## 11. Färdplan

1. **Prototyp 0.1** ✅ Gå runt, samla trä och sten, tända eld, hunger och värme, dag och natt.
2. **Prototyp 0.2:** Djur att jaga, tillverka spjut, tillaga mat.
3. **Prototyp 0.3:** Bygga första byggnaderna, eldhjärta och tidsålder 1 → 2.
4. **Motorval:** flytta till Godot eller Unreal, få 2 spelare online samtidigt.
5. **Vertical slice:** tidsålder 1–2, 6 spelare, ett nattanfall, mammutjakt.

## 12. Öppna frågor

- Förstapersonsvy hela tiden, eller kan man växla till tredje person?
- Ska man kunna dö permanent, eller återuppstå vid eldhjärtat?
- Hur lång ska en hel spelomgång vara: en kväll eller flera veckor?
- Ska det finnas PvP (stam mot stam) senare, eller bara co-op?
