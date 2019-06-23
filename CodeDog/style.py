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


# `styleName` is like "dark" or "light"
# `stylePath` is like "global" or "home/projectsList"
def getStyle(styleName: str, stylePath: str):
	# if we have a cached version of this file
	if styleName in _styleCache and stylePath in _styleCache[styleName]:
		# return cached
		return _styleCache[styleName][stylePath]
	# if we don't have an existing cache for `styleName`
	if styleName not in _styleCache:
		# create an empty dict for any cached files for are `stylename`
		_styleCache[styleName] = {}
	# join path's together that should lead to the css file
	cssPath = os.path.join(STYLE_PATH, styleName, os.path.normpath(stylePath) + ".css")
	# if its a file
	if os.path.isfile(cssPath):
		# open the file under variable name `f`
		with open(cssPath) as f:
			# read all file content
			cssData = f.read()
			# cache the file's content
			_styleCache[styleName][stylePath] = cssData
			# return the file's content
			return cssData
	else:
		# it did not exit or is not a file
		# so raise an error/exception
		raise FileNotFoundError(f"Failed to find '{stylePath}.css' for style '{styleName}' (at '{cssPath}')")


def clearStyleCache():
	# empty the dictionary
	_styleCache.clear()


getStyle("light")


print(_styleCache)
