# Description
Le projet **mask_detection_based_on_yolov8** est un ensemble complet de ressources conçu pour la détection du prot du masque.  

Ce référentiel GitHub est la principale source de scripts Python et de données associées, formant un écosystème dédié à la recherche et au développement dans le domaine de la vision par ordinateur et de l'apprentissage automatique.  

# Installation du repo et création de l'environnement virtuel
Pour installer ce projet, commencez par ouvrir le Terminal ou l'Invite de commande : Sur Windows, ouvrez l'Invite de Commande ou PowerShell. Sur macOS ou Linux, ouvrez le Terminal.

Exécutez :
`git clone https://github.com/Gueyefall/mask_detection_based_on_yolov8.git`

PS : Il faudra se connecter avec ses identfiants git en ayant les droits d'accès au repo  
Sinon, juste télécharger le zip avec le bouton dédié dans la liste déroulante "Code" plus haut.

Pour la suite, d'abord vérifier si python (idéalement la 3.9 ou plus) est installé  
`python --version` ou `python3 --version`

* Installer Python : Assurez-vous que Python est installé sur votre système. Vous pouvez le télécharger depuis le site officiel de Python. L'installation de Python inclut également pip (gestionnaire de paquets Python) et venv (module pour créer des environnements virtuels).

* Ensuite Installer pip,  le gestionnaire de paquets de Python. Il est nécessaire pour installer les dépendances. Si vous n'avez pas pip, installez-le en suivant les instructions sur le [site officiel de pip](https://pip.pypa.io/en/stable/installation/)

* Pour pour de [détails sur les environnments virtuels](https://packaging.python.org/en/latest/tutorials/installing-packages/#creating-and-using-virtual-environments)

Créer un Environnement Virtuel : Exécutez la commande suivante pour créer un environnement virtuel. *Remplacez nom_env* par le nom que vous souhaitez donner à votre environnement virtuel :  

* Sur Windows : `python -m venv nom_env`  
* Sur macOS et Linux : `python3 -m venv nom_env`

Activer l'Environnement Virtuel : Une fois l'environnement virtuel créé, vous devez l'activer :  

* Sur Windows : `.\nom_env\Scripts\activate`
* Sur macOS et Linux : `source nom_env/bin/activate`

Lorsque l'environnement virtuel est activé, vous verrez généralement le nom de l'environnement virtuel affiché dans votre ligne de commande (au début, entre parenthèses).

*PS : Désactiver l'Environnement Virtuel : Lorsque vous avez terminé vos travaux dans l'environnement virtuel, vous pouvez le désactiver en exécutant :* `deactivate`

# Installation des  dépendances
Exécutez la commande suivante pour installer toutes les dépendances listées dans requirements.txt :  
`pip install -r requirements.txt`

De plus, vous devrez probablement installer des paquets supplémentaires avant de lancer YOLO...

* Gérer les drivers pour la GPU (variable selon le fournisseur : nvidia, amd, etc.)  
[Drivers NVIDIA CUDNN](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html)  
[Drivers AMD ROCm](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/tutorial/quick-start.html#rocm-install-quick)  

* Pour la dépendance incontournable qu'est PyTorch (si non installé), se référer à : https://pytorch.org/
