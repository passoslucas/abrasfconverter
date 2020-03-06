import os
from xml.etree import ElementTree
import xml.etree.ElementTree as ET

file_name = 'nfs.xml'
full_file = os.path.abspath(os.path.join(file_name))

dom = ElementTree.parse(full_file)

nota = dom.findall('Nota')

for x in nota:
    cnpj_tom = x.find('cpfCnpjTomador').text
    num_nota = x.find('numeroNota').text
    emissao = x.find('dataEmissao').text
    situacao_nota = x.find('situacaoNota').text
    valor_Bruto = x.find('valorBruto').text
    codigo_ver = x.find('codigoVerificacao').text
    competencia = x.find('competencia').text
    cnpj_pres = x.find('cpfCnpjPrestador').text
    aliquota = x.find('aliquotaServicos').text
    valor_deducao = x.find('valorDeducao').text
    valor_iss = x.find('valorIss').text
    valor_liq = x.find('valorLiquidoNfse').text
    valor_inss = x.find('valorInss').text
    desc_cond = x.find('valorDescontoCondicionado').text
    desc_incond = x.find('valorDescontoIncondicionado').text
    discriminacao = x.find('discriminacao').text
    mun_serv = x.find('municipioPrestacaoServico').text
    cod_serv = x.find('itemListaServico').text
    nome_tom = x.find('razaoSocialTomador').text
    base_calc = x.find('baseDeCalculo').text
    valor_iss = x.find('valorIssRetido').text
    nome_prest = x.find('razaoSocialPrestador').text
    cep_prest = x.find('cepPrestador').text
    prest_end_rua = x.find('enderecoPrestador').text
    prest_end_num = x.find('numeroEnderecoPrestador').text
    prest_end_compl = x.find('complementoEnderecoPrestador').text
    prest_end_bairro = x.find('bairroPrestador').text
    prest_end_cidade = x.find('descricaoCidadePrestador').text
    prest_cod_cidade = x.find('cidadePrestador').text
    tom_end_cidade = x.find('descricaoCidadeTomador').text
    prest_uf = x.find('ufPrestador').text
    prest_fone = x.find('telefonePrestador').text
    iss_retido = x.find('issRetido').text
    tom_end_rua = x.find('enderecoTomador').text
    tom_end_num = x.find('numeroEnderecoTomador').text
    tom_end_bairro = x.find('bairroTomador').text
    tom_cod_cidade = x.find('cidadeTomador').text
    tom_uf = x.find('ufTomador').text
    cep_tom = x.find('cepTomador').text
    valor_nota = x.find('valorNota').text
    optante = x.find('optanteSimplesNacional').text

xml_doc = ET.Element('ConsultarNfseResposta')

listaNfse = ET.SubElement(xml_doc, 'ListaNfse')
compNfse = ET.SubElement(listaNfse, 'CompNfse')
nfse = ET.SubElement(compNfse, 'Nfse')
infNfse = ET.SubElement(nfse, 'InfNfse')
ET.SubElement(infNfse, 'Numero').text = num_nota

tree = ET.ElementTree(xml_doc)
tree.write('sample.xml', encoding="ISO-8859-1")


# def prettify(element, indent='  '):
#     queue = [(0, element)]  # (level, element)
#     while queue:
#         level, element = queue.pop(0)
#         children = [(level + 1, child) for child in list(element)]
#         if children:
#             element.text = '\n' + indent * (level+1)  # for child open
#         if queue:
#             element.tail = '\n' + indent * queue[0][0]  # for sibling open
#         else:
#             element.tail = '\n' + indent * (level-1)  # for parent close
#         queue[0:0] = children  # prepend so children come before siblings