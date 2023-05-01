# AutoActiveExternalDriver

## Détails

**AutoActiveExternalDriver** est un script écrit en **Python** permettant d'automatiser le montage des systèmes de stockages externes _(USB, HDD externe, SSD externe, ...)_.  

## Prérequis

Pour pouvoir utiliser le script, il faut **impérativement**:

- Un système Linux (Debian, Ubuntu, ArchLinux, ...)
- Git
- Crontab
- Python (>= 3.8.10)
- Pip  

## Installation 

Pour installer le script et ses dépendances, merci de suivre **ces étapes**:

```bash
git clone https://github.com/luxferre-code/AutoActiveExternalDriver.git
cd AutoActiveExternalDriver/
```  

Maintenant que vous êtes dans le répertoire, il suffit d'ajouter comme taches planifiés le script.  
Il faudra avant tous savoir ce quel disque vous voulez monter automatiquement. 

La commande vous permet d'afficher tous les disques et partitions disponibles:  
```bash
lsblk
```

A noté que le programme **monte uniquement les partitions**.  

Je vous conseille, par des mesures simples, de prendre les **sdX** (le X nous ne l'utiliserons pas).  

Maintenant, ajoutons la taches **cron**:  

```bash
crontab -e
```

Puis ajoutons la ligne:

```bash
* * * * * sudo python3 EMPLACEMENT_ABSOLU_DE_AAED.PY sd EMPLACEMENT_ABSOLU_DE_OU_MONTER_LA_PARTITION
```

N'oublier pas de changer:
- **EMPLACEMENT_ABSOLU_DE_AAED.PY**
- **EMPLACEMENT_ABSOLU_DE_OU_MONTER_LA_PARTITION**  

Dans mon cas, je noterai:  

```bash
* * * * * sudo python3 /home/luxferre/Workspace/AutoActiveExternalDriver/AAED.py sd /media
```

Vous pouvez aussi changer les temps ([lien vers CronHub](https://crontab.cronhub.io/))

## Licence

Ce projet est protéger par la licence **MIT**

## Auteur

Le seul auteur de ce script est [Valentin Thuillier](https://luxferre-code.fr/)