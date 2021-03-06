import tkinter as tk
from tkinter import filedialog
import os
import xml.etree.ElementTree as ET
# import xml.dom.minidom

path = tk.Tk()
path.withdraw()

full_file = filedialog.askopenfile()
print (full_file)
dom = ET.parse(full_file)
notas = dom.findall('Notas')
nota = dom.findall('Nota')

for x in nota:

    cnpj_tom = x.find('cpfCnpjTomador').text
    num_nota = x.find('numeroNota').text
    emissao = x.find('dataEmissao').text
    situacao_nota = x.find('situacaoNota').text
    valor_Bruto = x.find('valorBruto').text
    codigo_ver = x.find('codigoVerificacao').text
    competencia = x.find('competencia').text
    nat_operacao = x.find('naturezaOperacao').text
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
    #prest_end_compl = x.find('complementoEnderecoPrestador').text
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


    #estrutura inicial
    xml_doc = ET.Element('ConsultarNfseResposta')
    listaNfse = ET.SubElement(xml_doc, 'ListaNfse')
    compNfse = ET.SubElement(listaNfse, 'CompNfse')
    nfse = ET.SubElement(compNfse, 'Nfse')

    #cabecalho
    infNfse = ET.SubElement(nfse, 'InfNfse')
    ET.SubElement(infNfse, 'Numero').text = num_nota
    ET.SubElement(infNfse, 'CodigoVerificacao').text = codigo_ver
    ET.SubElement(infNfse, 'DataEmissao').text = emissao
    ET.SubElement(infNfse, 'IdentificacaoRps')

    #tributacao
    dentro_municipio = '1'
    fora_municipio = '2'
    retencao = '1'
    sem_retencao = '2'

    if nat_operacao == '[5.7] Imposto recolhido pelo regime �nico de arrecada��o - Com reten��o' or '[5.7] Imposto recolhido pelo regime único de arrecadação - Com retenção':
        nat_operacao = dentro_municipio
        iss_retido = retencao

    if nat_operacao == '[6.3] Imposto devido fora de Cachoeirinha, com obriga��o de reten��o na fonte' or '[6.3] Imposto devido fora de Cachoeirinha, com obrigação de retenção na fonte':
        nat_operacao = fora_municipio
        iss_retido = retencao
    
    if nat_operacao == '[5.9] Imposto recolhido pelo regime �nico de arrecada��o - Sem reten��o' or '[5.9] Imposto recolhido pelo regime único de arrecadação - Sem retenção':
        nat_operacao = dentro_municipio
        iss_retido = sem_retencao

    ET.SubElement(infNfse, 'NaturezaOperacao').text = nat_operacao

    ET.SubElement(infNfse, 'OptanteSimplesNacional').text = optante

    #descricao do servico
    ET.SubElement(infNfse, 'Competencia').text = competencia
    ET.SubElement(infNfse, 'OutrasInformacoes').text = discriminacao

    #valores servico
    servico = ET.SubElement(infNfse, 'Servico')
    valores = ET.SubElement(servico, 'Valores')
    ET.SubElement(valores, 'ValorServicos').text = valor_Bruto
    ET.SubElement(valores, 'ValorDeducoes').text = valor_deducao
    ET.SubElement(valores, 'ValorInss').text = valor_inss
    ET.SubElement(valores, 'ValorIr')
    ET.SubElement(valores, 'IssRetido').text = iss_retido
    ET.SubElement(valores, 'BaseCalculo').text = base_calc
    ET.SubElement(valores, 'Aliquota').text = aliquota
    ET.SubElement(valores, 'ValorLiquidoNfse').text = valor_liq
    ET.SubElement(valores, 'ValorIssRetido').text = valor_iss
    ET.SubElement(valores, 'DescontoCondicionado').text = desc_cond
    ET.SubElement(valores, 'DescontoIncondicionado').text = desc_incond

    #servico
    ET.SubElement(servico, 'ItemListaServico').text = cod_serv
    ET.SubElement(servico, 'Discriminacao')
    ET.SubElement(servico, 'CodigoMunicipio').text = cod_mun_serv

    #prestador
    prestador_servico = ET.SubElement(infNfse, 'PrestadorServico')
    id_prestador = ET.SubElement(prestador_servico, 'IdentificacaoPrestador')

    ET.SubElement(id_prestador, 'Cnpj').text = cnpj_pres
    ET.SubElement(id_prestador, 'InscricaoMunicipal')

    ET.SubElement(prestador_servico, 'RazaoSocial').text = nome_prest
    ET.SubElement(prestador_servico, 'NomeFantasia').text = nome_prest

    endereco_prest = ET.SubElement(prestador_servico, 'Endereco')

    ET.SubElement(endereco_prest, 'Endereco').text = prest_end_rua
    ET.SubElement(endereco_prest, 'Numero').text = prest_end_num
    ET.SubElement(endereco_prest, 'Bairro').text = prest_end_bairro
    ET.SubElement(endereco_prest, 'CodigoMunicipio').text = prest_cod_cidade
    ET.SubElement(endereco_prest, 'Cep').text = cep_prest

    contato_pres = ET.SubElement(prestador_servico, 'Contato')
    ET.SubElement(contato_pres, 'Telefone').text = prest_fone
    ET.SubElement(endereco_prest, 'Email')

    #tomador
    tomador_servico = ET.SubElement(infNfse, 'TomadorServico')
    id_tomador = ET.SubElement(tomador_servico, 'IdentificacaoTomador')
    cpf_cnpj_tom = ET.SubElement(id_tomador, 'CpfCnpj')

    ET.SubElement(cpf_cnpj_tom, 'Cnpj').text = cnpj_tom

    ET.SubElement(tomador_servico, 'RazaoSocial').text = nome_tom
    ET.SubElement(tomador_servico, 'NomeFantasia').text = nome_tom

    endereco_tom = ET.SubElement(tomador_servico, 'Endereco')

    ET.SubElement(endereco_tom, 'Endereco').text = tom_end_rua
    ET.SubElement(endereco_tom, 'Numero').text = tom_end_num
    ET.SubElement(endereco_tom, 'Bairro').text = tom_end_bairro
    ET.SubElement(endereco_tom, 'CodigoMunicipio').text = tom_cod_cidade
    ET.SubElement(endereco_tom, 'Uf').text = tom_uf

    contato_tom = ET.SubElement(tomador_servico, 'Contato')

    ET.SubElement(infNfse, 'IntermediarioServico')
    ET.SubElement(infNfse, 'ConstrucaoCivil')

    #pagamento
    cond_pagamento = ET.SubElement(infNfse, 'CondicaoPagamento')
    ET.SubElement(cond_pagamento, 'Condicao').text = '1'
    ET.SubElement(cond_pagamento, 'QtdParcela').text = '1'

    parcelas = ET.SubElement(cond_pagamento, 'Parcelas')
    ET.SubElement(parcelas, 'Parcela').text = '1'
    ET.SubElement(parcelas, 'Valor').text = valor_nota

    #cancelamento / substituicao
    nfse_cancelamento = ET.SubElement(compNfse, 'NfseCancelamento')
    confirmacao_cancelamento = ET.SubElement(nfse_cancelamento, 'Confirmacao')

    pedido_cancelamento = ET.SubElement(confirmacao_cancelamento, 'Pedido')
    ET.SubElement(pedido_cancelamento, 'InfPedidoCancelamento')
    ET.SubElement(pedido_cancelamento, 'ns2:Signature')

    inf_cancelamento = ET.SubElement(confirmacao_cancelamento, 'InfConfirmacaoCancelamento')

    if situacao_nota == 'A':
        situacao_nota = 'False'
    else:
        situacao_nota = 'True'

    ET.SubElement(inf_cancelamento, 'Sucesso').text = situacao_nota
    nfse_subs = ET.SubElement(compNfse, 'NfseSubstituicao')
    ET.SubElement(nfse_subs, 'SubstituicaoNfse')

    ET.SubElement(xml_doc, 'ListaMensagemRetorno')

    formato_arquivo = '.xml'

    tree = ET.ElementTree(xml_doc)
    tree.write(num_nota + formato_arquivo, encoding="ISO-8859-1")

    def indent(elem, level=0):
        i = "\n" + level*"    "
        j = "\n" + (level-1)*"    "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i
            if not elem.tail or not elem.tail.strip():
                elem.tail = j
            for SubElement in elem:
                indent(SubElement, level+1)
        else:
            if level and(not elem.tail or not elem.tail.strip()):
                elem.tail = j

    def parse(num_nota, formato_arquivo, parser=None):
        tree = ET
        tree.parse(num_nota + formato_arquivo)
        return tree

    root = tree.getroot()
    indent(root)
    tree.write(num_nota + formato_arquivo, encoding="ISO-8859-1")