from lxml import etree
import sys

xml_filename = "Xml/maraicher.xml"
if len(sys.argv) >= 2:
    xml_filename = sys.argv[1]

# lecture du fichier XML
tree = etree.parse(xml_filename)

# validation du XML avec un schema XSD
xsd = etree.XMLSchema(file='Xml/maraicher.xsd')
if not xsd.validate(tree):
    print("Document XML non valide (mal formé ou non conforme au schema)")
    sys.exit(1)

# element racine
root = tree.getroot()

# pretty print XML
etree.dump(root)

# acces to children
children = root.getchildren()

# XPATH simple 
fruits = tree.xpath("/produits/fruit")

total = 0
for fruit in fruits:
    # print("Fruit:", fruit.attrib['type'])
    print("Fruit:", fruit.get('type'))
    print("\t-Producteur:",  fruit.xpath('producteur/text()')[0])
    price = int(fruit.get('prix'))
    total += price
    print("\t-Prix:", price)
print("Somme prix:", total)

# change price of last fruit
fruit.set('prix', '210')

total2 =  tree.xpath("sum(//fruit/@prix)")
print("Somme prix:", total2)

total3 = sum(int(p) for p in tree.xpath("//fruit/@prix"))
print("Somme prix:", total3)

print("Type du 1er fruit:", tree.xpath("/produits/fruit[1]/@type")[0])
print("Producteur du 1er fruit:", tree.xpath("//fruit[1]/producteur/text()")[0])
print("Types de tous les fruits:", tree.xpath("/produits/fruit/@type"))

print("Legumes bio:", tree.xpath('//legume[bio]'))
print("Legumes pas bio:", tree.xpath('//legume[not(bio)]'))
print("Type de produits de prix = 190:", tree.xpath('/produits/*[@prix = 190]/@type'))
print("Type de produits de prix >= 200:", tree.xpath('/produits/*[@prix >= 200]/@type'))

# Save modified XML
tree.write(
    'Xml/maraicher2.xml', 
    pretty_print=True, 
    xml_declaration=True, 
    encoding='UTF-8'
)