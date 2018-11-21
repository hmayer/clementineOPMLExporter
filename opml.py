from jinja2 import Template
root = Template('<?xml version="1.0" encoding="utf-8"?>\n<opml version="2.0">\n\t{{ head }}\n\t{{ body }}\n</opml>\n')
head = Template('<head>\n\t\t<title>Clementine Exporter</title>\n\t\t<dateCreated>{{ now }}</dateCreated>\n\t</head>')
body = Template('<body>\n{% for outline in outlines %}\t\t{{outline}}\n{% endfor %}\n\t</body>')
outline = Template('<outline text="{{ description }}" title="{{ title }}" type="rss" xmlUrl="{{ url }}"/>')

