import xml.etree.ElementTree as ET

mytree = ET.parse('nfs.xml')
myroot = mytree.getroot()

tomador_cnpj = (myroot[3][0].text)
num_nota = (myroot[3][1].text)
data_emissao = (myroot[3][2].text)
sit_nota = (myroot[3][3].text)
valor_bruto = (myroot[3][4].text)
competencia = (myroot[3][5].text)
prestador_cnpj = (myroot[3][8].text)
prestador_nome = (myroot[3][10].text)
aliquota = (myroot[3][12].text)
iss_retido = (myroot[3][14].text)
valor_liq = (myroot[3][15].text)
valor_inss = ((myroot[3][17].text))
desc_cond = (myroot[3][22].text)
desc_incond = (myroot[3][23].text)
discrim_serv = (myroot[3][24].text)
cod_mun_serv = (myroot[3][25].text)
cod_mun_serv = (myroot[3][28].text)
tomador_nome = (myroot[3][31].text)
valor_base_calc = (myroot[3][32].text)
valor_iss_ret = (myroot[3][33].text)
prestador_end_rua = (myroot[3][40].text)
prestador_cnpj = (myroot[3][36].text)
prestador_end_cep = (myroot[3][39].text)
prestador_end_num = (myroot[3][41].text)
prestador_end_comp = (myroot[3][42].text)
prestador_end_bairro = (myroot[3][43].text)
prestador_end_mun = (myroot[3][44].text)
prestador_cod_mun = (myroot[3][45].text)
tomador_end_mun = (myroot[3][46].text)
prestador_uf = (myroot[3][47].text)
prestador_contato = (myroot[3][48].text)
tomador_end_rua = (myroot[3][63].text)
tomador_end_num = (myroot[3][64].text)
tomador_end_bairro = (myroot[3][65].text)
tomador_cod_mun = (myroot[3][66].text)
tomador_uf = (myroot[3][67].text)
tomador_end_cep = (myroot[3][68].text)
valor_nota = (myroot[3][70].text)
optante = (myroot[3][79].text)



print(tomador_cnpj, tomador_nome)



# print(num_nota, ver_code, optante, outras_info, valor_servico, valor_inss, valor_ir, iss_retido, base_calculo, aliquota, valor_liq, valor_iss_ret, desc_cond, desc_incond)
# print(cod_serv, discrim_serv, cod_mun_serv)
# print(prestador_cnpj, prestador_im, prestador_nome)
# print(prestador_end_rua, prestador_end_num, prestador_end_bairro, prestador_cod_mun, prestador_end_cep, prestador_contato, prestador_email)
# print(tomador_cnpj, tomador_nome, tomador_end_rua, tomador_end_num, tomador_end_comp, tomador_end_bairro, tomador_cod_mun, tomador_uf)
# print(valor_parcela)
# print(cancelada)



# for x in myroot.findall('ConsultarNfseResposta'):
#     num_nota = x.find('Numero').text
#     ver_code = x.find('CodigoVerificacao').text
#     print('Nota: {} - Cod: {}'.format(num_nota, ver_code))



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


