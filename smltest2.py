import xml.etree.ElementTree as ET

data = '''<?xml version="1.0" encoding="ISO-8859-1" ?><Notas>
  <camposModificados></camposModificados>
  <contemChaveEquals>false</contemChaveEquals>
  <chaveEquals></chaveEquals>
  <Nota>
    <cpfCnpjTomador>87115838001857</cpfCnpjTomador>
    <numeroNota>20207</numeroNota>
    <dataEmissao>2020-02-17 09:34:14.0 BRT</dataEmissao>
    <situacaoNota>A</situacaoNota>
    <valorBruto>12119.9</valorBruto>
    <codigoVerificacao>58416681</codigoVerificacao>
    <competencia>202002</competencia>
    <inscricaoAtividade>148560</inscricaoAtividade>
    <naturezaOperacao>[6.3] Imposto devido fora de Cachoeirinha, com obriga��o de reten��o na fonte</naturezaOperacao>
    <cpfCnpjPrestador>23449000000179</cpfCnpjPrestador>
    <guia>N�O</guia>
    <nome>EDER AMADOR FERREIRA -ME</nome>
    <serieNota>NF</serieNota>
    <aliquotaServicos>0.03</aliquotaServicos>
    <valorDeducao>0</valorDeducao>
    <valorIss>363.6</valorIss>
    <valorLiquidoNfse>10423.11</valorLiquidoNfse>
    <valorCofins>0.0</valorCofins>
    <valorInss>1333.19</valorInss>
    <valorIr>0.0</valorIr>
    <valorCsll>0.0</valorCsll>
    <valorPis>0.0</valorPis>
    <outrasRetencoes>0</outrasRetencoes>
    <valorDescontoCondicionado>0.0</valorDescontoCondicionado>
    <valorDescontoIncondicionado>0</valorDescontoIncondicionado>
    <discriminacao>Aditivo Salas Sarandi
  </Nota>
</Notas>'''

myroot = ET.fromstring(data)
print(myroot.tag)