import sqlite3
import argparse
import time
from pathlib import Path
from pprint import pprint
from opml import root, head, body, outline

default_folder = "%s/.config/Clementine" % (str(Path.home()),)

optparse = argparse.ArgumentParser(description="Process Clementine config folder")
optparse.add_argument('--folder', '-f', dest='folder', default=default_folder)
optparse.add_argument('--output', '-o', dest='output', default=None)
args = optparse.parse_args()

clementine_db = "%s/clementine.db" % (args.folder,)
try:
    connection = sqlite3.connect(clementine_db)
except:
    print("Não foi possível conectar na base de dados [%s], verifique se o Clementine não está sendo executado" % (clementine_db,))
    exit(0)

db = connection.cursor()

podcasts = db.execute("SELECT url, title, description FROM podcasts")

outlines = []

for (url, title, description) in podcasts:
    line = outline.render(url=url, title=title, description=description)
    outlines.append(line)

outputBody = body.render(outlines=outlines)
outputHead = head.render(now=time.ctime())
outputRoot = root.render(body=outputBody, head=outputHead)

if args.output:
    out = open(args.output, "w")
    out.write(outputRoot)
    out.close()
else:
    print(outputRoot)
