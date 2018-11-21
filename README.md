# clementineOPMLExporter
Export podcasts registered in Clementine media player to OPML file using the default SQLite3 clementine database.

# Install
1. Off course clone repo
2. Create a venv with: `python3 -m venv .venv` (yep, inside repo folder)
3. Ran: `python export.py` (see options below if you have strange things in your environment)

# Options
* **--folder** | **-f**   Clementine config folder if other than default ~/.config/Clementine/
* **--output** | **-o**   Output file to save OPML, otherwise is printed in standard output

Now you can import in another aggregator, Judas
