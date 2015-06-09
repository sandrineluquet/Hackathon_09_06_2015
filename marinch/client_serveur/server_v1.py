#! /usr/bin/python
# -*- coding:utf-8 -*-
#Définition d'un serveur réseau rudimentaire Ce serveur attend la connexion d'un client, pour entamer un dialogue avec lui
import socket, sys, os

HOST = os.environ.get('RDB_HOST') or '192.168.1.34'
PORT = 50000

# 1) création du socket :
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2) liaison du socket à une adresse précise :
try:
    mySocket.bind((HOST, PORT))
except socket.error:
    print "La liaison du socket à l'adresse choisie a échoué."
    sys.exit()

while 1:
    # 3) Attente de la requête de connexion d'un client :
    print "Serveur prêt, en attente de requêtes ..."
    mySocket.listen(5)

    # 4) Etablissement de la connexion :
    connexion, adresse = mySocket.accept()
    print "Client connecté, adresse IP %s, port %s" % (adresse[0], adresse[1])

    # 5) Dialogue avec le client :
    connexion.send("Vous êtes connecté au serveur Marinch. Envoyez vos messages.\n")
    connexion.send("Bonjour, a vous de parler en premier =)")
    msgClient = connexion.recv(1024)
    while 1:
        print "C>", msgClient
        if msgClient.upper() == "FIN" or msgClient == "":
            break
        msgServeur = raw_input("S> ")
        connexion.send(msgServeur)
        msgClient = connexion.recv(1024)

    # 6) Fermeture de la connexion :
    connexion.send("Au revoir !")
    print "Connexion interrompue."
    connexion.close()

    ch = raw_input("<R>ecommencer <T>erminer ? ")
    if ch.upper() =='T':
        break
