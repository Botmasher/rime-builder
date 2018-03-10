import fetchurl
import urllib.parse
import urllib.error
import xml.etree.ElementTree as elemtree

class WordLookupAPI:
	url = u"https://en.wiktionary.org/w/index.php?title="
	url_params = u"&printable=yes"

	def __init__(self):
		self.memo = {}

	def locate_en_headword(self, xml):
		"""Return the English language headword from an online dictionary page"""
		root = elemtree.fromstring(xml)
		# find top of page headword
		for header in root.iter("h1"):
			if header is not None and header.attrib and header.attrib.get('id') == "firstHeading":
				# confirm English section for headword
				lang_headers = root.iter("h2")
				for lang_header in lang_headers:
					lang_span = lang_header.find("span")
					# English headword found
					if lang_span is not None and lang_span.attrib and lang_span.attrib.get('id') == "English":
						return header.text
		return None

	def is_word(self, string):
		"""Verify that the string is an uncapitalized headword in an English dictionary"""
		if string is None: return False
		word = self.memo.get(string)
		# look for word in online dictionary
		if word is None:
			try:
				path = u"%s%s%s" % (self.url, urllib.parse.quote(string.lower(), encoding='utf-8'), self.url_params)
				data = fetchurl.fetchHTML(path)
				word = self.locate_en_headword(data)
				self.memo[string] = word
			except urllib.error.HTTPError:
				return False		# 404
		if word is not None and word[0].islower():
			return True
		return False