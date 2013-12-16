import xml.dom.minidom as minidom
import sys


def GetChildElements(node):

	"""Return a list of all child nodes that are elements."""
	childElements = []
	# For each child node...

	for childNode in node.childNodes:
		if childNode.nodeType == minidom.Node.ELEMENT_NODE:
			childElements.append(childNode)
	return childElements
	
def FindChildElementsByTagnameAndAttributes(node, tagname = None, attrdict=None):
	"""Return a list of child elements of the current node that match the criteria.
	args:
		tagname -- str: a valid element tag name
		attrdict -- a dictionary of the form:
			attrname -- str: the name of an attribute
			attrvalue -- the attribute value
	"""
	matchingElements = []
	# For each child node...

	childElements = GetChildElements(node)

	# If a tagname was provided...
	if tagname:
		matchingElements = filter(lambda x: x.tagName == tagname, childElements)

	# if an attribute dictionary was provided...
	if attrdict:
		# for each child element...
		for childElement in matchingElements:
			# for each attribute in dictionary...
			for attrname in attrdict.keys():
				# If the attribute does not match...
				if childElement.getAttribute(attrname) != str(attrdict[attrname]):
					matchingElements.remove(childElement)
					break
					
	#print "XXXX matchingelements len=", len(matchingElements)
	return matchingElements
	
def FindFirstChildElementByTagnameAndAttributes(node, tagname = None, attrdict=None):
	"""Return a single child element of the current node that matches the criteria.
	args:
		tagname -- str: a valid element tag name
		attrdict -- a dictionary of the form:
			attrname -- str: the name of an attribute
			attrvalue -- the attribute value
	"""
	match = None
	matchingElements = FindChildElementsByTagnameAndAttributes(node, tagname, attrdict)
	# If any were found...
	if matchingElements:
		# Get the first one.
		match = matchingElements[0]
	return match
	
def GetText(element_node):
	"""Return the text held in a element node's text nodes.
	args:
		element_node -- a DOM node
	"""
	text = ''
	# For each child node...
	for childNode in element_node.childNodes:
		if childNode.nodeType == minidom.Node.TEXT_NODE:
			# Append the text stored in the text node.
			text += childNode.data
	return text

