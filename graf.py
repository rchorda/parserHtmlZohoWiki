from BeautifulSoup import BeautifulSoup
import codecs
fileObj = codecs.open( "Graf.html", "r", "utf-8" )
html = fileObj.read() # Returns a Unicode string from the UTF-8 bytes in the file

soup = BeautifulSoup(html)
#print soup.prettify()
#print soup.findAll('a')
prevGrupo = ""
for indice in  soup.findAll('a'): 
    #if (indice.findPrevious('h2').text == "Uzbekistan:"): 
    if (indice.findPrevious('h2').text == "Kazakhstan:"): 
	if (indice.findPrevious('h1').text != prevGrupo):
	    prevGrupo = indice.findPrevious('h1').text
	    print "=====", prevGrupo,"=====\n"
	print "[[",indice['href'],"|",indice.text,"]]\n"
exit()
for indice in  soup.findAll('a'): 
    if (indice.findPrevious('h2').text == "Kazakhstan:"): 
	print indice.findPrevious('h1').text, indice.text
