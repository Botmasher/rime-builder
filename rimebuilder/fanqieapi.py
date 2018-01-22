import xml.etree.ElementTree as elemtree
import fetchurl
import urllib.parse

class FanqieAPI:
	# parsable wiki entry
	url = u"https://en.wiktionary.org/w/index.php?title="
	url_params = u"&printable=yes"

	def __init__(self):
		self.memo = {}

	def locate_fanqie_node(self, xml):
		root = elemtree.fromstring(xml)
		#find the th label node titled w:Fanqie
		for elem in root.iter("tr"):
			table_node = elem.find("th/small/a")
			if table_node is not None and table_node.attrib and table_node.attrib['title'] == "w:Fanqie":
				# find the td parallel node with actual rime data
				fanqie_elems = elem.findall("td/span/")
				fanqie = "%s%s切" % (fanqie_elems[0].text, fanqie_elems[1].text)
				return fanqie
		return None

	def rhyme(self, zi):
		path = u"%s%s%s" % (self.url, urllib.parse.quote(zi, encoding='utf-8'), self.url_params)
		if zi in self.memo:
			data = self.memo[zi]['data']
		else:
			data = fetchurl.fetchHTML(path)
		self.memo[zi] = {'path': path, 'data': data}
		fanqie = self.locate_fanqie_node(data)
		return fanqie
