GPT-3 (Generative Pre-trained Transformer)

Settings: engine="text-davinci-003", temperature=0.7, max_tokens=100, top_p=0.5, frequency_penalty=0, presence_penalty=0, best_of=1, stop=None

1. Query:
    ```
    Extrahiere die Produktkategorie:
    Welche Alkoholhaltigen Getränke auf    Traubenbasis bietet Netto an?
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
