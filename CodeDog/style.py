from glob import iglob
import os


STYLE_PATH = os.path.join(os.path.dirname(__file__), "style")
_styleCache = {}


def getStyle(name: str):
	if name in _styleCache:
		return _styleCache[name]
	style = ""
	path = os.path.join(STYLE_PATH, name)
	if not os.path.exists(path):
		raise FileNotFoundError(f"Failed to find file/folder at '{path}'")
	if os.path.isfile(path):
		with open(path) as f:
			style = f.read()
	elif os.path.isdir(path):
		for filePath in iglob(os.path.join(path, "*.css"), recursive=True):
			with open(filePath) as f:
				style += "\n\n%s" % f.read()
	else:
		raise FileNotFoundError(f"Failed to find file/folder at '{path}'")
	_styleCache[name] = style.strip()
	return style


def clearStyleCache():
	_styleCache.clear()
