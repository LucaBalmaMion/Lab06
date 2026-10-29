from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        # TODO
        cnx = get_connection()
        cursore = cnx.cursor(dictionary=True)
        query = "select * from strumento"
        cursore.execute(query)
        lista_strumenti = []
        for riga in cursore:
            lista_strumenti.append(Strumento(riga["codice"], riga['tipo'], riga['marca'], riga['anno_acquisto'], riga['valore'], riga['disponibile']))
        return lista_strumenti

    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        # TODO
        lista_strumenti = self.get_strumenti()
        lista_strumenti_tipo = []
        for elemento in lista_strumenti:
            if elemento.tipo == tipo:
                lista_strumenti_tipo.append(elemento)
        if len(lista_strumenti_tipo) == 0:
            return None
        else:
            return lista_strumenti_tipo
