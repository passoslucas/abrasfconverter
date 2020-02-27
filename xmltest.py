import xml.etree.ElementTree as ET

mytree = ET.parse('abrasf.xml')
myroot = mytree.getroot()


for child in myroot[0][0][0][0]:
    print(child.text)

#cabecalho nota
num_nota = (myroot[0][0][0][0][0].text)
ver_code = (myroot[0][0][0][0][1].text)
optante = (myroot[0][0][0][0][5].text)
outras_info = (myroot[0][0][0][0][7].text)

#dados nota
valor_servico = (myroot[0][0][0][0][8][0][0].text)
valor_inss = (myroot[0][0][0][0][8][0][2].text)
valor_ir = (myroot[0][0][0][0][8][0][3].text)
iss_retido = (myroot[0][0][0][0][8][0][4].text)
base_calculo = (myroot[0][0][0][0][8][0][5].text)
aliquota = (myroot[0][0][0][0][8][0][6].text)
valor_liq = (myroot[0][0][0][0][8][0][7].text)
valor_iss_ret = (myroot[0][0][0][0][8][0][8].text)
desc_cond = (myroot[0][0][0][0][8][0][9].text)
desc_incond = (myroot[0][0][0][0][8][0][10].text)

#dados servico
cod_serv = (myroot[0][0][0][0][8][1].text)
discrim_serv = (myroot[0][0][0][0][8][2].text)
cod_mun_serv = (myroot[0][0][0][0][8][3].text)

#dados do prestador
prestador_cnpj = (myroot[0][0][0][0][9][0][0].text)
prestador_im = (myroot[0][0][0][0][9][0][1].text)
prestador_nome = (myroot[0][0][0][0][9][1].text)
prestador_nome_fant = (myroot[0][0][0][0][9][2].text)
prestador_end_rua = (myroot[0][0][0][0][9][3][0].text)
prestador_end_num = (myroot[0][0][0][0][9][3][1].text)
prestador_end_bairro = (myroot[0][0][0][0][9][3][2].text)
prestador_cod_mun = (myroot[0][0][0][0][9][3][3].text)
prestador_end_cep = (myroot[0][0][0][0][9][3][4].text)
prestador_contato = (myroot[0][0][0][0][9][4][0].text)
prestador_email = (myroot[0][0][0][0][9][4][1].text)

#dados tomador
tomador_cnpj = (myroot[0][0][0][0][10][0][0][0].text)
tomador_nome = (myroot[0][0][0][0][10][1].text)
tomador_end_rua = (myroot[0][0][0][0][10][2][0].text)
tomador_end_num = (myroot[0][0][0][0][10][2][1].text)
tomador_end_comp = (myroot[0][0][0][0][10][2][2].text)
tomador_end_bairro = (myroot[0][0][0][0][10][2][3].text)
tomador_cod_mun = (myroot[0][0][0][0][10][2][4].text)
tomador_uf = (myroot[0][0][0][0][10][2][5].text)

#dados pagamento
valor_parcela = (myroot[0][0][0][0][13][2][1].text)

#cancelamento
cancelada = (myroot[0][0][1][0][1][0].text)


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


