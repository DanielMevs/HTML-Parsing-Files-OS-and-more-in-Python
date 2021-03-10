'''Sometimes when working with XML/HTML, you don't want to build a parser
that just runs line by line. You want to have the entire doc in memory and
manipulate it at will. For this you will need to operate on the document's DOM'''
#How to use the XML miniDOM class that Python provides, to load an XML file and then
#operate on the document while it's in memory
#Example file for parsing and processing XML

import xml.dom.minidom

def main():
    #use the parse() function to load and parse an XML file
    doc = xml.dom.minidom.parse("samplexml.xml")

    #print out the document node and the name of the first child tag
    print(doc.nodeName)
    print(doc.firstChild.tagName)

    #get a list of XML tags from the document and print each one
    skills = doc.getElementsByTagName("skill")
    print("%d skills: " % skills.length)
    for skill in skills:
        print(skill.getAttribute("name"))

    #create a new XML tag and add it into the document
    newSkill = doc.createElement("skill")
    newSkill.setAttribute("name", "jQuery")
    doc.firstChild.appendChild(newSkill)

if __name__ == "__main__":
    main()
    
    

