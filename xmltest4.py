import os
import xml.etree.ElementTree as ET
from varname import varname
# import xml.dom.minidom

file_name = 'nfs.xml'
full_file = os.path.abspath(os.path.join(file_name))
tree = ET.parse(full_file)
nota = tree.findall('Nota')

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
    cod_mun_serv = x.find('municipioPrestacaoServico').text
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


final_file_name = 'abrasf_test.xml'
final_full_file = os.path.abspath(os.path.join(final_file_name))
dom = ET.parse(final_full_file)
nota_lst = dom.findall('InfNfse')

for item in nota_lst:
    print ('Numero: ', item.find('Numero').text)

# root = dom.getroot()

# for elem in root.iter():
#     tag_name = elem.tag
#     tag_text = elem.text
#     #print(tag_name, tag_text)


# for y in notaTest:
#     numeroNota = y.find('Numero')
#     print(numeroNota)
    
    



















# for tag_name in 

#     #estrutura inicial
#     xml_doc = ET.Element('ConsultarNfseResposta')
#     listaNfse = ET.SubElement(xml_doc, 'ListaNfse')
#     compNfse = ET.SubElement(listaNfse, 'CompNfse')
#     nfse = ET.SubElement(compNfse, 'Nfse')

#     #cabecalho
#     infNfse = ET.SubElement(nfse, 'InfNfse')
#     ET.SubElement(infNfse, 'Numero').text = num_nota
#     ET.SubElement(infNfse, 'CodigoVerificacao').text = codigo_ver
#     ET.SubElement(infNfse, 'DataEmissao').text = emissao
#     ET.SubElement(infNfse, 'IdentificacaoRps')
#     ET.SubElement(infNfse, 'NaturezaOperacao').text = '2'

#     #geral / simples
#     geral = '1'
#     simples = '2'

#     if optante == '1':
#         optante = simples

#     ET.SubElement(infNfse, 'OptanteSimplesNacional').text = optante

#     #descricao do servico
#     ET.SubElement(infNfse, 'Competencia').text = competencia
#     ET.SubElement(infNfse, 'OutrasInformacoes').text = discriminacao

#     #valores servico
#     servico = ET.SubElement(infNfse, 'Servico')
#     valores = ET.SubElement(servico, 'Valores')
#     ET.SubElement(valores, 'ValorServicos').text = valor_Bruto
#     ET.SubElement(valores, 'ValorDeducoes').text = valor_deducao
#     ET.SubElement(valores, 'ValorInss').text = valor_inss
#     ET.SubElement(valores, 'ValorIr')
#     ET.SubElement(valores, 'IssRetido').text = iss_retido
#     ET.SubElement(valores, 'BaseCalculo').text = base_calc
#     ET.SubElement(valores, 'Aliquota').text = aliquota
#     ET.SubElement(valores, 'ValorLiquidoNfse').text = valor_liq
#     ET.SubElement(valores, 'ValorIssRetido').text = valor_iss
#     ET.SubElement(valores, 'DescontoCondicionado').text = desc_cond
#     ET.SubElement(valores, 'DescontoIncondicionado').text = desc_incond

#     #servico
#     ET.SubElement(servico, 'ItemListaServico').text = cod_serv
#     ET.SubElement(servico, 'Discriminacao')
#     ET.SubElement(servico, 'CodigoMunicipio').text = cod_mun_serv

#     #prestador
#     prestador_servico = ET.SubElement(infNfse, 'PrestadorServico')
#     id_prestador = ET.SubElement(prestador_servico, 'IdentificacaoPrestador')

#     ET.SubElement(id_prestador, 'Cnpj').text = cnpj_pres
#     ET.SubElement(id_prestador, 'InscricaoMunicipal')

#     ET.SubElement(prestador_servico, 'RazaoSocial').text = nome_prest
#     ET.SubElement(prestador_servico, 'NomeFantasia').text = nome_prest

#     endereco_prest = ET.SubElement(prestador_servico, 'Endereco')

#     ET.SubElement(endereco_prest, 'Endereco').text = prest_end_rua
#     ET.SubElement(endereco_prest, 'Numero').text = prest_end_num
#     ET.SubElement(endereco_prest, 'Bairro').text = prest_end_bairro
#     ET.SubElement(endereco_prest, 'CodigoMunicipio').text = prest_cod_cidade
#     ET.SubElement(endereco_prest, 'Cep').text = cep_prest

#     contato_pres = ET.SubElement(prestador_servico, 'Contato')
#     ET.SubElement(contato_pres, 'Telefone').text = prest_fone
#     ET.SubElement(endereco_prest, 'Email')

#     #tomador
#     tomador_servico = ET.SubElement(infNfse, 'TomadorServico')
#     id_tomador = ET.SubElement(tomador_servico, 'IdentificacaoTomador')
#     cpf_cnpj_tom = ET.SubElement(id_tomador, 'CpfCnpj')

#     ET.SubElement(cpf_cnpj_tom, 'Cnpj').text = cnpj_tom

#     ET.SubElement(tomador_servico, 'RazaoSocial').text = nome_tom
#     ET.SubElement(tomador_servico, 'NomeFantasia').text = nome_tom

#     endereco_tom = ET.SubElement(tomador_servico, 'Endereco')

#     ET.SubElement(endereco_tom, 'Endereco').text = tom_end_rua
#     ET.SubElement(endereco_tom, 'Numero').text = tom_end_num
#     ET.SubElement(endereco_tom, 'Bairro').text = tom_end_bairro
#     ET.SubElement(endereco_tom, 'CodigoMunicipio').text = tom_cod_cidade
#     ET.SubElement(endereco_tom, 'Uf').text = tom_uf

#     contato_tom = ET.SubElement(tomador_servico, 'Contato')

#     ET.SubElement(infNfse, 'IntermediarioServico')
#     ET.SubElement(infNfse, 'ConstrucaoCivil')

#     #pagamento
#     cond_pagamento = ET.SubElement(infNfse, 'CondicaoPagamento')
#     ET.SubElement(cond_pagamento, 'Condicao').text = '1'
#     ET.SubElement(cond_pagamento, 'QtdParcela').text = '1'

#     parcelas = ET.SubElement(cond_pagamento, 'Parcelas')
#     ET.SubElement(parcelas, 'Parcela').text = '1'
#     ET.SubElement(parcelas, 'Valor').text = valor_nota

#     #cancelamento / substituicao
#     nfse_cancelamento = ET.SubElement(compNfse, 'NfseCancelamento')
#     confirmacao_cancelamento = ET.SubElement(nfse_cancelamento, 'Confirmacao')

#     pedido_cancelamento = ET.SubElement(confirmacao_cancelamento, 'Pedido')
#     ET.SubElement(pedido_cancelamento, 'InfPedidoCancelamento')
#     ET.SubElement(pedido_cancelamento, 'ns2:Signature')

#     inf_cancelamento = ET.SubElement(confirmacao_cancelamento, 'InfConfirmacaoCancelamento')

#     if situacao_nota == 'A':
#         situacao_nota = 'False'
#     else:
#         situacao_nota = 'True'

#     ET.SubElement(inf_cancelamento, 'Sucesso').text = situacao_nota
#     nfse_subs = ET.SubElement(compNfse, 'NfseSubstituicao')
#     ET.SubElement(nfse_subs, 'SubstituicaoNfse')

#     ET.SubElement(xml_doc, 'ListaMensagemRetorno')

# def create_new_file():
#     tree = ET.ElementTree(xml_doc)
#     tree.write('sample.xml', encoding="ISO-8859-1")

