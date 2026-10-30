# Projet Python avec Docker

Ce petit projet utilise Python pour calculer la moyenne, la valeur maximale et la valeur minimale d'une liste de temperatures. Docker permet de lancer le programme dans un environnement Python prepare a l'avance.

## Avant de commencer

Il faut avoir installe Docker et Docker Compose, et verifier que Docker est en cours d'execution.

Ouvre un terminal dans le dossier principal du projet, celui qui contient `compose.yaml`. Par exemple :

```bash
cd ~/Desktop/python
```

## Lancer le projet

### 1. Construire et demarrer le conteneur

```bash
docker compose up -d --build
```

Cette commande construit l'image Docker du projet, puis demarre le conteneur en arriere-plan. L'option `--build` demande de reconstruire l'image, notamment si les dependances ont change.

### 2. Verifier que le conteneur fonctionne

```bash
docker compose ps
```

Le service `app` doit apparaitre avec un etat indiquant qu'il fonctionne.

### 3. Executer le programme

```bash
docker compose exec app python /app/app.py
```

Le resultat affiche les trois calculs. Avec les valeurs actuelles, la moyenne est `20.9`, le maximum `23` et le minimum `19`.

Le conteneur ne lance pas le script tout seul : il reste disponible pour qu'on puisse lui demander d'executer des commandes. C'est pour cela qu'il faut utiliser `docker compose exec` pour lancer le programme.

## Executer un autre script Python

Tu peux ajouter d'autres fichiers Python dans le dossier `app` de ton ordinateur. Par exemple, si tu crees le fichier `app/mon_script.py`, tu peux le lancer depuis le terminal du projet avec :

```bash
docker compose exec app python /app/mon_script.py
```

Dans le conteneur, le dossier `app` de ton ordinateur est accessible sous le nom `/app`. Remplace `mon_script.py` par le nom du fichier que tu veux executer. Les modifications sont disponibles tout de suite : tu n'as pas besoin de reconstruire l'image.

Tu peux aussi ouvrir un terminal Bash dans le conteneur :

```bash
docker compose exec app bash
```

Une fois dans ce terminal, lance le script avec Python :

```bash
python /app/mon_script.py
```

Pour revenir au terminal de ton ordinateur, tape :

```bash
exit
```

## Commandes Docker utiles

| Commande | A quoi elle sert |
| --- | --- |
| `docker compose up -d --build` | Construit l'image si besoin et demarre le conteneur en arriere-plan. |
| `docker compose build` | Construit ou reconstruit l'image sans demarrer le conteneur. |
| `docker compose ps` | Affiche les conteneurs du projet et leur etat. |
| `docker compose exec app python /app/app.py` | Lance le script Python dans le conteneur deja demarre. |
| `docker compose exec app bash` | Ouvre un terminal Bash a l'interieur du conteneur. Tape `exit` pour en sortir. |
| `docker compose logs -f app` | Affiche les messages du service `app` et continue a afficher les nouveaux. Tape `Ctrl+C` pour arreter l'affichage. |
| `docker compose stop` | Arrete le conteneur sans le supprimer. On peut le redemarrer ensuite. |
| `docker compose down` | Arrete et supprime le conteneur et le reseau crees pour ce projet. Les fichiers du projet sur ton ordinateur ne sont pas supprimes. |

Pour redemarrer un conteneur arrete avec `stop`, utilise :

```bash
docker compose start
```

## Le fichier `requirements.txt`

`requirements.txt` est la liste des bibliotheques Python dont le projet a besoin. Ici, il contient :

```text
numpy
```

NumPy est une bibliotheque qui facilite les calculs sur des listes de nombres. Dans `app.py`, elle sert a calculer la moyenne (`mean`), le maximum (`max`) et le minimum (`min`) des temperatures.

Lors de la construction de l'image, le `Dockerfile` installe les bibliotheques indiquees dans `requirements.txt`. Si tu ajoutes ou modifies une dependance dans ce fichier, reconstruis et redemarre avec :

```bash
docker compose up -d --build
```

## Ou modifier le programme

Le script se trouve dans `app/app.py`. Le dossier `app` de ton ordinateur est partage avec le conteneur : les changements faits dans `app.py` sont donc disponibles tout de suite, sans reconstruire l'image. Tu peux relancer le programme avec la commande de l'etape 3 pour voir le resultat.