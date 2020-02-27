import xml.etree.ElementTree as ET

mytree = ET.parse('nfs.xml')
myroot = mytree.getroot()

for line in myroot.iter('cpfCnpjTomador'):
    newcnpj = int(x.text) + 1
    x.text = str(newcnpj)

mytree.write('nfs60.xml')

#cabecalho nota
# num_nota = int((myroot[3][1].text))
# cod_ver = (myroot[3][5].text)
# x = (myroot[3][2].text)
# data_emissao, hora_emissao , y = (x.split(' '))
# optante = int((myroot[3][79].text))
# competencia = (myroot[3][6].text)
# obs_nota = (myroot[3][25].text)

# #dados nota
# valor_bruto = float((myroot[3][4].text))
# deducoes = float((myroot[3][14].text))
# valor_inss = float((myroot[3][18].text))
# valor_ir = float((myroot[3][19].text))
# iss_retido = int((myroot[3][59].text))
# base_calc = float((myroot[3][32].text))
# aliquota_bruta = float((myroot[3][13].text))
# aliquota = aliquota_bruta * 100
# valor_liq = float((myroot[3][16].text))
# valor_iss_ret = float((myroot[3][33].text))
# desc_cond = float((myroot[3][23].text))
# desc_incond = float((myroot[3][24].text))

# #dados servico
# cod_serv = int((myroot[3][29].text))
# discrim_serv = str((myroot[3][51].text))
# cod_mun_serv = int((myroot[3][26].text))

# #dados prestador
# prestador_cnpj = (myroot[3][36].text)
# prestador_nome = (myroot[3][11].text)
# prestador_end_rua = (myroot[3][40].text)
# prestador_end_num = (myroot[3][41].text)
# prestador_end_comp = (myroot[3][42].text)
# prestador_end_bairro = (myroot[3][43].text)
# prestador_cod_mun = (myroot[3][45].text)
# prestador_end_cep = (myroot[3][39].text)
# prestador_contato = (myroot[3][48].text)
# prestador_uf = (myroot[3][47].text)
# prestador_end_mun = (myroot[3][44].text)

# #dados tomador
# tomador_cnpj = (myroot[3][0].text)
# tomador_nome = (myroot[3][31].text)
# tomador_end_rua = (myroot[3][63].text)
# tomador_end_num = (myroot[3][64].text)
# tomador_end_bairro = (myroot[3][65].text)
# tomador_cod_mun = (myroot[3][66].text)
# tomador_end_cep = (myroot[3][68].text)
# tomador_uf = (myroot[3][67].text)
# tomador_end_mun = (myroot[3][46].text)

# #dados pagamento
# valor_nota = float((myroot[3][70].text))

# #cancelamento
# cancelamento = 'false'
# sit_nota = (myroot[3][3].text)
# if sit_nota == 'A':
#     cancelamento = "false"
# else:
#     cancelamento = "true"

