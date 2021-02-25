from spalla import Verifica
#Verifica.firma("Chiara Gualdi")
#Verifica.stampa_esercizi()
def es2():
    es = Verifica.inizia_esercizio(2)
    es.dati = es.dati*es.dati
    es.consegna(es.dati)
def es22():
    es = Verifica.inizia_esercizio(22)
    print(es.dati)
    nuovalista=[]
    for i in es.dati:
        if i<=6:
            if i>=3:
                nuovalista.append(i)
    es.consegna(nuovalista)

#Verifica.stampa_voto()