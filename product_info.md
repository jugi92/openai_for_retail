GPT-3 (Generative Pre-trained Transformer)

Settings: engine="text-davinci-003", temperature=0.7, max_tokens=100, top_p=0.5, frequency_penalty=0, presence_penalty=0, best_of=1, stop=None

1. Query:
    ```
    Extrahiere die Produktkategorie:
    Welche Alkoholhaltigen Getränke auf Traubenbasis bietet Netto an?
    Produktkategorie:
    ```
    Response:
    ```
    Alkoholhaltige Getränke auf Traubenbasis
    ```

1. Query:
    ```
    Extrahiere die Produktkategorie:
    Welche Alkoholhaltigen Getränke auf Traubenbasis bietet Netto an?
    Produktkategorie:
    Alkoholhaltige Getränke auf Traubenbasis
    Wie nennt man diese auch?
    ```
    Response:
    ```
    Wein
    ```

1. Query: max_tokens=500
    ```
    Schreibe eine überzeugende Produktbeschreibung für das folgende Produkt:
    Doppio Passo Primitivo Rosato Puglia IGT
    Gattung: Roséwein
    Temperaturempfehlung: 8°C
    Alkoholgehalt: 12,0 % vol
    Flascheninhalt: 0,75 Liter
    Herkunftsland: Italien
    Anbauregion: Apulien
    Geschmacksrichtung: halbtrocken
    Rebsorte: Primitivo
    ```
    Response:
    ```
    Der Doppio Passo Primitivo Rosato Puglia IGT ist ein ausgezeichneter Roséwein aus Italien. Er stammt aus der Anbauregion Apulien und wird aus der Rebsorte Primitivo hergestellt. Der Wein ist halbtrocken und hat einen Alkoholgehalt von 12,0 % vol. Der Doppio Passo Primitivo Rosato Puglia IGT ist ein sehr fruchtiger und leicht säuerlicher Wein, der ein angenehmes und erfrischendes Aroma hat. Der Wein ist leicht und hat eine sehr schöne rosa Farbe. Er schmeckt hervorragend zu Fisch, Geflügel und leichten Salaten. Genießen Sie den Doppio Passo Primitivo Rosato Puglia IGT am besten bei einer Temperatur von 8°C. Er ist in einer 0,75 Liter Flasche erhältlich. Probieren Sie diesen hervorragenden Wein und lassen Sie sich von seinem unvergleichlichen Geschmack überzeugen.
    ```

1. Query: max_tokens=500
    ```
    Die ausschweifende, begeisterte Bewertung eines Kenners mit Fachjargon für das folgende Produkt:
    Doppio Passo Primitivo Rosato Puglia IGT
    Gattung: Roséwein
    Temperaturempfehlung: 8°C
    Alkoholgehalt: 12,0 % vol
    Flascheninhalt: 0,75 Liter
    Herkunftsland: Italien
    Anbauregion: Apulien
    Geschmacksrichtung: halbtrocken
    Rebsorte: Primitiv
    ```
    Response:
    ```
    Dieser Doppio Passo Primitivo Rosato Puglia IGT ist ein wunderbarer Roséwein aus Apulien, Italien. Er ist ein halbtrockener Wein mit einem Alkoholgehalt von 12,0 % vol und einer empfohlenen Serviertemperatur von 8°C. Der Wein ist aus der Rebsorte Primitivo hergestellt und kommt in einer 0,75 Liter Flasche. Der Wein ist komplex und aromatisch mit Noten von frischen Erdbeeren, reifen Himbeeren und Aromen von Blumen. Er ist saftig und hat eine angenehme Säure, die sich durch den ganzen Gaumen zieht. Der Abgang ist lang und fruchtig. Ein wunderbarer Wein, der ein einzigartiges Aroma und eine reiche Textur bietet. Ein Wein, der sich perfekt für ein romantisches Abendessen oder ein Glas Wein am Abend eignet.
    ```

1. Query max_tokens=500, presence_penalty=0.5
    ```
    Die ausschweifende, begeisterte Bewertung eines Kenners mit Fachjargon für das folgende Produkt:
    Makita HP488DWAE Akkuschlagbohrschrauber + Makita Bitset E-00016 31-teilig im Koffer
    - Farbe:  Grün / Blau & Schwarz Bohrmaschine
    - Akkuspannung 18 V
    - Akkutyp (Ni-MH/Li-Ion Li-ion
    - Leerlaufdrehzahl 0 - 400 / 1400 min-¹
    - Max. Drehmoment hart/weich 42 / 24 Nm
    - Drehmomenteinstellungen 16
    - Schlagzahl 0 - 6000 / 21 000 min-¹
    - Max. Bohrleistung in Holz 36 mm
    - Max. Bohrleistung in Mauerwerk 13 mm
    - Max. Bohrleistung in Mauerwerk 13 mm
    - Max. Bohrleistung in Stahl 13 mm
    - Aufnahmeschaft 1/2""-20UNF ""
    - Bohrfutterspannweite 1,5 - 13 mm
    - Schallleistungspegel (dB) 92 dB(A)
    - Schalldruckpegel (dB) 81 dB(A)
    - K-Wert Geräusch 3 dB(A)
    - Vibration Bohren = 2,5 m/s²
    ```
    Response:
    ```
    Der Makita HP488DWAE Akkuschlagbohrschrauber + Makita Bitset E-00016 31-teilig im Koffer ist ein absolutes Highlight! Dieses innovative Werkzeug überzeugt durch seine starke 18V Li-Ion Akkuspannung, die eine Leerlaufdrehzahl von 0 - 400 / 1400 min-¹ und ein Max. Drehmoment von 42 / 24 Nm ermöglicht. Es verfügt über 16 Drehmomenteinstellungen und eine Schlagzahl von 0 - 6000 / 21 000 min-¹. Der HP488DWAE bietet eine beeindruckende Max. Bohrleistung in Holz von 36 mm, in Mauerwerk von 13 mm und in Stahl von 13 mm. Der Aufnahmeschaft beträgt 1/2""-20UNF "" und das Bohrfutterspannweite reicht von 1,5 - 13 mm. Der Schallleistungspegel (dB) liegt bei 92 dB(A) und der Schalldruckpegel (dB) bei 81 dB(A). Der K-Wert Geräusch beträgt 3 dB(A) und die Vibration beim Bohren liegt bei 2,5 m/s². Dieser Makita HP488DWAE Akkuschlagbohrschrauber + Makita Bitset E-00016 31-teilig im Koffer ist ein wahres Kraftpaket, das alle Anforderungen an ein modernes Werkzeug erfüllt und eine hervorragende Leistung bietet.
    ```

1. Query 
    ```
    Wie viel Alkohol enthält der Doppio Passo Primitivo Rosato Puglia IGT?
    ```
    Response (wrong, see https://www.netto-online.de/doppio-passo-primitivo-rosato-puglia-igt-12-0-vol-0-75-liter/p-2275423000:
    ```
    Der Doppio Passo Primitivo Rosato Puglia IGT enthält 12,5 % Vol. Alkohol.
    ```

1. Query:
    ```
    "Wie viel Alkohol enthält der Doppio Passo Primitivo Rosato Puglia IGT"
    Extract the product from the the text above.
    Product:
    ```
    Response:
    ```
    Doppio Passo Primitivo Rosato Puglia IGT
    ```

1. Query:
    ```
    "Wie viel Alkohol enthält der Doppio Passo Primitivo Rosato Puglia IGT"
    Extract the product from the the text above.
    Product: Doppio Passo Primitivo Rosato Puglia IGT
    Write a sql query to get the product information from the article table with the column product_name being similar to the the previously mentioned product.
    ```
    Response
    ```
    SELECT * FROM article WHERE product_name LIKE '%Doppio Passo Primitivo Rosato Puglia IGT%';
    ``` 

    > Run the query against the database and get the full product description as below (For demo copied from website. The technology for this is already available in autocomplete of the search box):

1. Query:
    ```
    "Wie viel Alkohol enthält der Doppio Passo Primitivo Rosato Puglia IGT"

    Answer the above question with the information from the text below:

    "Feiner Duft nach roten Johannisbeeren, hellen Brombeeren und weißen Kirschen und bemerkenswert dichtes Aroma im Geschmack für einen Rosé. Geschmeidiger Körper mit feiner Säure, dennoch aber auch diskreter Frische im Kern. Ein auffallend charaktervoller Rosé, der auch kräftigere Speisen gut begleiten kann.

    Ein intensiv aromatischer Primitivo- Wein nach apulischer Tradition, mit fruchtig-süßem und würzigem Bukett. Unverwechselbares Aroma nach Brombeeren und roten Johannisbeeren.

    Gattung: Roséwein

    Rezeptempfehlung: Putenbrustfilet mit Tomaten-Parmesan-Kruste, Filet im Baconmantel

    Speiseempfehlung: Idealer Begleiter zu Fischgerichten, Pasta mit feinen Saucen und delikaten Wurstwaren.

    Temperaturempfehlung: 8°C

    Alkoholgehalt: 12,0 % vol

    Flascheninhalt: 0,75 Liter

    Herkunftsland
    Italien
    Anbauregion
    Apulien
    Geschmacksrichtung
    halbtrocken
    Rebsorte
    Primitivo
    ArtikelnummeResponse: 2275423000
    Artikel gehört zur Kategorie: Lebensmittel"
    ```
    Response (now correct)
    ```
    Der Doppio Passo Primitivo Rosato Puglia IGT enthält 12,0 % vol Alkohol.
    ```

1. Query:
    ```
    "Schmeckt der Doppio Passo Primitivo auch zu Wildgulasch?"
    Answer the above question with the information from the text below:
    "Feiner Duft nach roten Johannisbeeren, hellen Brombeeren und weißen Kirschen und bemerkenswert dichtes Aroma im Geschmack für einen Rosé. Geschmeidiger Körper mit feiner Säure, dennoch aber auch diskreter Frische im Kern. Ein auffallend charaktervoller Rosé, der auch kräftigere Speisen gut begleiten kann.

    Ein intensiv aromatischer Primitivo- Wein nach apulischer Tradition, mit fruchtig-süßem und würzigem Bukett. Unverwechselbares Aroma nach Brombeeren und roten Johannisbeeren.

    Gattung: Roséwein

    Rezeptempfehlung: Putenbrustfilet mit Tomaten-Parmesan-Kruste, Filet im Baconmantel

    Speiseempfehlung: Idealer Begleiter zu Fischgerichten, Pasta mit feinen Saucen und delikaten Wurstwaren.

    Temperaturempfehlung: 8°C

    Alkoholgehalt: 12,0 % vol

    Flascheninhalt: 0,75 Liter

    Herkunftsland
    Italien
    Anbauregion
    Apulien
    Geschmacksrichtung
    halbtrocken
    Rebsorte
    Primitivo
    ArtikelnummeResponse: 2275423000
    Artikel gehört zur Kategorie: Lebensmittel"
    ```
    Response: (wrong / at least not provable with the text)
    ```
    Ja, der Doppio Passo Primitivo passt auch gut zu Wildgulasch. Er hat ein auffallend charaktervolles Aroma und einen geschmeidigen Körper mit feiner Säure, der kräftigere Speisen gut begleiten kann.
    ```

1. Query:
    ```
    "Schmeckt der Doppio Passo Primitivo auch zu Wildgulasch?"

    Answer the above question with the information from the text below or state that the information is not contained in the text:

    "Feiner Duft nach roten Johannisbeeren, hellen Brombeeren und weißen Kirschen und bemerkenswert dichtes Aroma im Geschmack für einen Rosé. Geschmeidiger Körper mit feiner Säure, dennoch aber auch diskreter Frische im Kern. Ein auffallend charaktervoller Rosé, der auch kräftigere Speisen gut begleiten kann.

    Ein intensiv aromatischer Primitivo- Wein nach apulischer Tradition, mit fruchtig-süßem und würzigem Bukett. Unverwechselbares Aroma nach Brombeeren und roten Johannisbeeren.

    Gattung: Roséwein

    Rezeptempfehlung: Putenbrustfilet mit Tomaten-Parmesan-Kruste, Filet im Baconmantel

    Speiseempfehlung: Idealer Begleiter zu Fischgerichten, Pasta mit feinen Saucen und delikaten Wurstwaren.

    Temperaturempfehlung: 8°C

    Alkoholgehalt: 12,0 % vol

    Flascheninhalt: 0,75 Liter

    Herkunftsland
    Italien
    Anbauregion
    Apulien
    Geschmacksrichtung
    halbtrocken
    Rebsorte
    Primitivo
    ArtikelnummeResponse: 2275423000
    Artikel gehört zur Kategorie: Lebensmittel"
    ```
    Response (correct)
    ```
    The information is not contained in the text.
    ```

1. Query:
    ```
    "Schmeckt der Doppio Passo Primitivo auch zu Wildgulasch?"
    Name 5 products that sell well with the product from the question above:
    {
    "1":"
    ```
    Response:
    ```
    "Schmeckt der Doppio Passo Primitivo auch zu Wildgulasch?"
    Name 5 products that sell well with the product from the question above:
    {
    "1":"Weißbrot",
    "2":"Rotwein",
    "3":"Gemüse-Gemüse-Gemisch",
    "4":"Käseplatte",
    "5":"Schokoladenkuchen"
    }
    ```

GPT-3 does not know the Products of Netto. The next step could be fine-tuning a model with the actual information of Netto so that GPT would 
