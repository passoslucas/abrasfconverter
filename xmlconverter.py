import os

# os.chdir('\\Users\\User\\Desktop\\test')

# for f in os.listdir():
#     f_name, f_ext = (os.path.splitext(f))
#     f_part1, f_part2 = (f_name.split('-'))
#     f_part2 = f_part2.upper()
#     f_part1 = f_part1.upper()
#     #print('{}+{}'.format(f_part1, f_part2))

#     new_name = '{}{}'.format(f_part1, f_part2, f_ext)
#     os.rename(f, new_name)

#change the file name, cutting into pieces end chosing only the ones i want


xml_archive = open("nfs.xml", "r")
xml_list = []

for line in xml_archive:
    line = line.strip().split(" ")
    print(line)

xml_archive.close()

nfs_number
ver_code
emiss_date(year, month, day, hour, minute, seconds)
comp_date(year, month)
other_info
serv_value
inss_value
calc_base
rate
serv_final_value
iss_value
serv_code
city_serv_code
cnpj_prest
city_subs
company_name
fantasy_name
company_address
company_address_number
company_address_location
company_city_code
company_cep
company_phone
company_email
client_cnpj
client_name
client_address
client_address_number
client_address_comp
client_address_location
client_city_code
client_state_code








<?xml version="1.0" encoding="ISO-8859-1" standalone="yes"?>
<ConsultarNfseResposta xmlns:ns2="http://www.w3.org/2000/09/xmldsig#">
    <ListaNfse>
        <CompNfse>
            <Nfse>
                <InfNfse>
                    <Numero>{}</Numero>#.format(nfs_number)
                    <CodigoVerificacao>{}}</CodigoVerificacao>#.format(ver_code)
                        <DataEmissao>{2019}-{12}-{18}T{13}:{38}:{12}.700-03:00</DataEmissao>#.format(emiss_date)
                    <IdentificacaoRps/>
                    <NaturezaOperacao>2</NaturezaOperacao>
                    <OptanteSimplesNacional>1</OptanteSimplesNacional>
                    <Competencia>{2019}-{12}-01T00:00:00-03:00</Competencia>#.format(comp_date)
                    <OutrasInformacoes>{BANCO CAIXA ECON�MICA FEDERAL AG: 1769 OP: 003 C/C: 00001355-1}</OutrasInformacoes>#.format(other_info)
                    <Servico>
                        <Valores>
                            <ValorServicos>{59124.06}</ValorServicos>#.format(serv_value)
                            <ValorDeducoes>0.00</ValorDeducoes>
                            <ValorInss>6503.65</ValorInss>#.format(inss_value)
                            <IssRetido>1</IssRetido>
                            <BaseCalculo>{59124.06}</BaseCalculo>#,format(calc_base)
                            <Aliquota>3</Aliquota>#.format(rate)
                            <ValorLiquidoNfse>49959.83</ValorLiquidoNfse>#.format(serv_final_value)
                            <ValorIssRetido>1773.72</ValorIssRetido>#.format(iss_value)
                            <DescontoCondicionado>0.00</DescontoCondicionado>
                            <DescontoIncondicionado>0.00</DescontoIncondicionado>
                        </Valores>
                        <ItemListaServico>0702</ItemListaServico>#.format(serv_code)
                        <Discriminacao>{[[{Descricao=EXECU��O DE OBRA DE REFORMA E MANUTEN��O DOS BANHEIROS P�BLICOS DO CENTRO DE INFORMA��ES TUR�STICAS, LOCALIZADOS NA PRA�A MAJOR NICOLLETTI PARA MUNICIPIO DE GRAMADO.}][ItemServico={0702}][Quantidade={1}][ValorUnitario={59124.06}][ValorServico={59124.06}][ValorBaseCalculo={59124.06}][Aliquota={3}][Deducoes=0][DescontoCondicionado=0][DescontoIncondicionado=0]]}</Discriminacao>#.format(serv_description, serv_code, serv_qtd, serv_value, calc_base, rate)
                        <CodigoMunicipio>4309100</CodigoMunicipio>#.format(city_serv_code)
                    </Servico>
                    <PrestadorServico>
                        <IdentificacaoPrestador>
                            <Cnpj>{18885555000123}</Cnpj>#.format(cnpj_prest)
                            <InscricaoMunicipal>{430-0384/2762}</InscricaoMunicipal>#.format(city_subs)
                        </IdentificacaoPrestador>
                        <RazaoSocial>{VALMIR STEFINI DA SILVA}</RazaoSocial>#.fomrat(company_name)
                        <NomeFantasia>{EMPREITEIRA E PRESTADOR DE SERVICOS STEFINI}</NomeFantasia>#.format(fantasy_name)
                        <Endereco>
                            <Endereco>R Tancredo Neves</Endereco>#.format(company_address)
                            <Numero>1092</Numero>#.format(company_address_number)
                            <Bairro>RIO BRANCO</Bairro>#.format(company_address_location)
                            <CodigoMunicipio>4316006</CodigoMunicipio>#.format(company_city_code)
                            <Cep>95690000</Cep>#.format(company_cep)
                        </Endereco>
                        <Contato>
                            <Telefone>5135471594</Telefone>#.format(company_phone)
                            <Email>teresasilva@tca.com.br</Email>#.format(company_email)
                        </Contato>
                    </PrestadorServico>
                    <TomadorServico>
                        <IdentificacaoTomador>
                            <CpfCnpj>
                                <Cnpj>88847082000155</Cnpj>#.format(client_cnpj)
                            </CpfCnpj>
                        </IdentificacaoTomador>
                        <RazaoSocial>{MUNICIPIO DE GRAMADO}</RazaoSocial>#.format(client_name)
                        <Endereco>
                            <Endereco>{AV DAS HORTENSIAS}</Endereco>#.format(client_address)
                            <Numero>{2029}</Numero>#.format(client_address_number)
                            <Complemento>{TERREO}</Complemento>#.format(client_address_comp)
                            <Bairro>{CENTRO}</Bairro>#.format(client_address_location)
                            <CodigoMunicipio>{4309100}</CodigoMunicipio>#.format(client_city_code)
                            <Uf>{RS}</Uf>#.format(client_state_code)
                        </Endereco>
                        <Contato/>
                    </TomadorServico>
                    <IntermediarioServico/>
                    <ConstrucaoCivil/>
                    <CondicaoPagamento>
                        <Condicao>1</Condicao>
                        <QtdParcela>1</QtdParcela>
                        <Parcelas>
                            <Parcela>1</Parcela>
                            <Valor>{49959.83}</Valor>#.format(serv_final_value)
                        </Parcelas>
                    </CondicaoPagamento>
                </InfNfse>
            </Nfse>
            <NfseCancelamento>
                <Confirmacao>
                    <Pedido>
                        <InfPedidoCancelamento/>
                        <ns2:Signature/>
                    </Pedido>
                    <InfConfirmacaoCancelamento>
                        <Sucesso>false</Sucesso>
                    </InfConfirmacaoCancelamento>
                </Confirmacao>
            </NfseCancelamento>
            <NfseSubstituicao>
                <SubstituicaoNfse/>
            </NfseSubstituicao>
        </CompNfse>
    </ListaNfse>
    <ListaMensagemRetorno/>
</ConsultarNfseResposta>
