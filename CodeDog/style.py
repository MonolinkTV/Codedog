from glob import iglob
import os


# path of the folder containing all the styles
# `__file__` is a python magic variable that in this
# case is `[PATH_TO_PROJECT_DIR]\CodeDog\style.py`
# then we get the `dirname()` so it removes `style.py` from name
# then joins `style` to the path for the folder
STYLE_PATH = os.path.join(os.path.dirname(__file__), "style")
# keep the styles around so we don't need to get them from files
# all the time
_styleCache = {}


# TODO: fix that .css cant be at the end of a file in style
def getStyle(name: str):
	# if name is in are cache
	if name in _styleCache:
		# return the cached style
		return _styleCache[name]
	# create a variable to store the style in
	style = ""
	# add the `name` to the path ([PATH_TO_PROJECT_DIR]\CodeDog\style\[NAME])
	path = os.path.join(STYLE_PATH, name)
	# if it does not exist
	if not os.path.exists(path):
		# raise an error saying that it failed to find
		raise FileNotFoundError(f"Failed to find file/folder at '{path}'")
	# if its a file
	elif os.path.isfile(path):
		# open it up
		with open(path) as f:
			# read all the content and store it in variable `style`
			style = f.read()
	# if its a directory
	elif os.path.isdir(path):
		# find every file ending with `.css`
		for filePath in iglob(os.path.join(path, "*.css"), recursive=True):
			# open it up
			with open(filePath) as f:
				# add the content to the style `variable`
				# joining multiple together into one large style
				style += "\n\n%s" % f.read()
	else:
		# raise an error saying that it failed to find
		# but in this case its an unsupported type
		# for example a symlink
		raise FileNotFoundError(f"Failed to find file/folder at '{path}'")
	# save the style in the cache
	_styleCache[name] = style.strip()
	# return the resulting style
	return style


def clearStyleCache():
	# empty the dictionary
	_styleCache.clear()
