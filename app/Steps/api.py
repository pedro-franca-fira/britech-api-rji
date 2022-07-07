
from app.Auth.authentication import basicAuthentication
from app.Config import YESTERDAY, API_HML
from dateUts import *


def todosCotistas():
    link =  f'{API_HML}/Fundo/BuscaCotistasPorCPFCNPJouID?cpfCnpj=&idCotista=&nome='
    response = basicAuthentication(link)
    return response


def fundoPosicao(ListCotista,data=""):
      lista = []
      for idCotista in ListCotista:
          link = f'{API_HML}/Fundo/BuscaPosicaoCotistaPorData?dataPosicao={data}&idPosicao=&idCotista={idCotista}&idCarteira=&tipoCotistaMovimentacao='
          response = basicAuthentication(link)
          if not response == []:
                lista.append(response)
                print(f'{len(lista)}: {idCotista}: cliente posicao')

      return lista




def todasCarteiras(dt):
    link =  f'{API_HML}/Common/BuscaCliente?idCliente=&idClienteExterno=&DataAlteracao='
    link =  f'{link}{dt}'
    response = basicAuthentication(link)
    return response

def idCotista(listId):
    lista = []
    for id_cliente in listId:
        link = f'http://saa-ast-0034/WS/api/Fundo/BuscaCotistasPorFundo?idCarteira={id_cliente}'
        response = basicAuthentication(link)
        if not response == []:
            lista.append(response)
        else:
            pass#print("ERROR:",response,id_cliente)
    return lista




def operacaoCotistaAnalitico(listCarteira,dateI,dateF):
    lista = []
    
    link = f'{API_HML}' + '/Fundo/OperacaoCotistaAnalitico?idsCarteiras={}'
    
    ystd = f'&dataInicio={dateI}&dataFim={dateF}'
    tdy = f'&dataInicio=1900-01-01&dataFim={now(fmt="sql")}'
    

    for idCarteira in listCarteira:
        prm = ystd if YESTERDAY else tdy
        url = f'{link.format(idCarteira)}{prm}'
        print(url)
        response = basicAuthentication(url)
        if not response == []:
            lista.append(response)
            print(f'{idCarteira} - {len(response)} [operacaoCotistaAnalitico]')
    return lista