# ai_descript

Ez a projekt képek és videók automatikus elemzésére és szöveges leírására szolgál OpenAI Vision modellek (pl. GPT-4o) segítségével. A szkript képes videofájlokból képkockákat kinyerni, majd azokat (vagy meglévő képeket) elemezni és a leírásokat strukturált formában elmenteni.

## Funkciók

- **Videó feldolgozás**: Képkockák kinyerése megadott időközönként.
- **Képfelismerés**: OpenAI GPT-4o vagy más Vision modellek használata a képtartalom elemzéséhez.
- **Batch feldolgozás**: Egyszerre több fájl automatikus elemzése.
- **Testreszabható promptok**: Egyedi instrukciók adhatók az AI-nak a leírások stílusára és tartalmára vonatkozóan.
- **Kimeneti formátum**: A generált leírások szöveges fájlba vagy JSON formátumba menthetők.

## Követelmények

- Python 3.10 vagy újabb
- Gemini API kulcs

## Telepítés

1. Klónozd a tárolót:
   ```bash
   git clone https://github.com/simsononroad/ai_descript.git
   cd ai_descript
   ```

2. Hozz létre egy virtuális környezetet (opcionális, de ajánlott):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows esetén: venv\Scripts\activate
   ```

3. Telepítsd a szükséges függőségeket:
   ```bash
   pip install -r requirements.txt
   ```

## Konfiguráció

Hozz létre egy `.txt` fájlt a projekt gyökérkönyvtárában, és add meg az OpenAI API kulcsodat:

```txt
your_api_key_here
```

A `config.py` (vagy a program paraméterezése) segítségével beállíthatod a vizsgálni kívánt könyvtárat, a kimeneti mappát és a használni kívánt modellt.

## Használat

A program indításához futtasd a `main.py` fájlt:

```bash
python main.py
```

### Paraméterek és működés

1. **Bemenet**: Helyezd a feldolgozni kívánt képeket vagy videókat az `input` mappába (vagy a konfigurációban megadott helyre).
2. **Feldolgozás**: 
   - Videó esetén a szkript mintavételezi a képkockákat.
   - Minden képet továbbít az OpenAI API-nak.
3. **Kimenet**: A leírások a `output` mappában fognak megjelenni, a forrásfájl nevével megegyező szöveges fájlokban.

## Projekt felépítése

- `main.py`: A fő futtatható állomány, amely koordinálja a munkafolyamatot.
- `utils.py`: Segédfüggvények a képfeldolgozáshoz és az API hívásokhoz.
- `requirements.txt`: A futtatáshoz szükséges Python csomagok listája.

## Licenc

Ez a projekt az MIT licenc alatt áll. További részletekért lásd a `LICENSE` fájlt.