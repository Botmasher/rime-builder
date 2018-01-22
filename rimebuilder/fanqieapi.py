import xml.etree.ElementTree as elemtree
import fetchurl
import urllib.parse

class FanqieAPI:
	# https://en.wiktionary.org/w/index.php?title=test&printable=yes
	# parse XML
	url = u"https://en.wiktionary.org/w/index.php?title="
	url_options = u"&printable=yes"

	def __init__(self):
		self.memo = {}

	def locate_fanqie_node(self, xml):
		root = elemtree.fromstring(xml)
		#find the w:Fanqie node
		for elem in root.iter("tr"):
			if elem.find("th/small/a") and "title" in elem.fromstring("th/small/a") and elem.fromstring("th/small/a").attrib['title'] == "w:Fanqie":
			#if "title" in elem.attrib and elem.attrib['title'] == "w:Fanqie":
				# backup to the actual Fanqie rhyme using XPath expression
				things = elem.find("td/span/").text
				print (things)

	def rhyme(self, zi):
		path = u"%s%s%s" % (self.url, urllib.parse.quote(zi, encoding='utf-8'), self.url_options)
		if zi in self.memo:
			data = self.memo[zi]['data']
		else:
			data = fetchurl.fetchHTML(path)
		self.memo[zi] = {'path': path, 'data': data}
		self.locate_fanqie_node(data)
		return data
