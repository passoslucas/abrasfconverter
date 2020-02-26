import xml.etree.ElementTree as ET

mytree = ET.parse('abrasf.xml')
myroot = mytree.getroot()

print(myroot.tag)
print(myroot[0][0][0][0][1].tag)

# for x in myroot.findall('ConsultarNfseResposta'):
#     notanumber = x.find('Numero').text
#     ver_code = x.find('CodigoVerificacao').text
#     print('Nota: {} - Cod: {}'.format(notanumber, ver_code))





# myroot[0].remove(myroot[3][0])
# mytree.write('new4.xml')


# myroot[0][0].attrib.pop('name')
# mytree.write('new3.xml')


# ET.SubElement(myroot[0], 'escritorio')

# for x in myroot.iter('escritorio'):
#     b = 'Passos Contabilidade'
#     x.text = str(b)
# mytree.write('new2.xml')


# for x in myroot.iter('discriminacao'):
#     a = str(x.text) + 'discriminacao has been added'
#     x.text = str(a)
#     x.set('updated', 'yes')

# mytree.write('new.xml')


