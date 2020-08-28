![alt text](https://cdn.discordapp.com/attachments/732937171119636564/748864140184911942/Annotation_2020-08-28_131821.png)

# PoC - Les chevaliers de la table Bouygues

## Description

L'équipe des chevaliers de la table Bouygues est une des finalistes du challenge *EDHEC DA-IA*.
Le challenge a été organisé par Bouygues Telecom en partenariat avec IBM en 2020.

Le but était de proposer et développer une stratégie digitale pour booster la vente des forfaits mobiles sur le site de Bouygues Telecom.

Ce PoC consiste en un chatbot qui recommande un forfait mobile en se basant sur un modèle IA de clustering.

Le clustering se fait actuellement sur un open dataset sur la consommation des utilisateurs.

Les services utilisés sont:

  - IBM Watson Assistant
  - IBM Function
  - IBM Watson Machine Learning


## Démo

### Upload du dataset (00:00')

* Aller sur [IBM Cloud Pak for Data](https://eu-de.dataplatform.cloud.ibm.com)

### Création d'un modeler (00:19')

### Création d'un modèle IA à partir du modeler (00:48')
* Il faut avoir un output (node vert)

### Déploiment du modèle IA (01:03')
* Le modèle est déployé sous forme d'endpoint
* On peut tester l'endpoint directment sur IBM Cloud via l'onglet "Test" (01:42')

### Création d'un skill sur Watson Assistant (02:07')
* Retourner sur [IBM Cloud Pak for Data](https://eu-de.dataplatform.cloud.ibm.com)

### Création d'une IBM Function (03:02')
* Retourner sur [IBM Cloud](https://cloud.ibm.com/)


### Création d'un token IAM (03:53')
* On a besoin d'un token IAM pour appeler l'endpoint du modèle IA.

### Génération de l'apikey via curl (04:29')
* Remplacez `VOTRE_TOKEN_IAM` par le votre

```
curl -k -X POST \
--header "Content-Type: application/x-www-form-urlencoded" \
--header "Accept: application/json" \
--data-urlencode "grant_type=urn:ibm:params:oauth:grant-type:apikey" \
--data-urlencode "apikey=VOTRE_TOKEN_IAM" \
"https://iam.bluemix.net/identity/token"
```
> La durée de vie du token est d'1 heure. Pensez à regénerer l'apikey.

### Connecter l'IBM Function au webhook de Watson Assitant (05:50')
* N'oubliez pas d'ajouter `.json` à la fin de l'url pour avoir la réponse en JSON.

### Tester notre skill en mode dev (06:46')

### Création d'un "preview link" (07:09')
* Votre chatbot est déployé / hébergé par IBM. C'est la solution idéale pour faire tester votre chatbot aux autres utilisateurs.
