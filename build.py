# snippets.py → index.html
import json, sys
sys.path.insert(0, '.')
from snippets import S, SECTIONS
data = json.dumps({"sections": SECTIONS, "items": S}, ensure_ascii=False).replace("</", "<\\/")
tpl = open("template.html", encoding="utf-8").read()
open("index.html", "w", encoding="utf-8").write(tpl.replace("__DATA__", data))
print(len(S), "items")
