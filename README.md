# P9_matthieu_guimard

## Créer un profil développeur
Il existe deux manière pour créer un profil développeur et pouvoir gérer le site.

### Créer un profil directement sur le site.

Après avoir lancé l'environnement virtuel et le serveur en local, le développeur pourra rentrer l'adresse du serveur sur son navigateur et arrivera directement sur la page de connexion. Ici il faudra ensuite appuyer sur le bouton "S'INCRIRE".
Rentrer alors son identifiant et son mot de passe. Pour des raisons de sécurité il n'est pas possible de s'octroyer les droits directements depuis le front.
Une fois votre profil créé, vous pouvez fermer votre serveur et lancer le shell de django avec la commande:

>
> python manage.py shell
>

Une fois dans le shell il faudra importer le model User depuis votre base de données puis le profil que vous venez de créer.
Les lignes de coed qui suivent supposent que vous venez de créer un profil avec le nom d'utilisateur "Développeur"

>
> from authentication.models import User
> 
> user = User.objects.get(username="Développeur")
>

Une fois que vous avez créé l'instance de votre profil dans le shell vous pourrez alors vous attribuer le rôle de superuser nécessaire pour accéder à l'admin du site.

>
>user.is_superuser=True
>
>user.save()
>

Votre profil est maintenant superuser et vous pouvez accéder à l'admin en rajoutant /admin à la fin de l'url fourni lors du lancement de votre serveur en local.


>http://127.0.0.1:8000/admin
