### Projet de Base de Données NCBI

Ce projet vise à créer et gérer des bases de données relationnelles en utilisant les données fournies par la banque de données NCBI. 
  
Il permettra d'installer les métas-données ainsi que les caractéristiques des génomes d'un taxon donné.
  
Les données principales incluses dans ces bases de données sont liées à l'assemblage génomique, aux génomes, aux contigs, aux échantillons biologiques (biosamples) et aux informations spécifiques à chaque élément.  
  
Chaque base de données est créée à l'aide de scripts individuels portant leur nom respectif, et l'exécution du script principal main permet d'automatiser ce processus.




Le projet est structuré de la manière suivante :  
  
**main.py**: Le script principal à exécuter pour automatiser la création des bases de données relationnelles.  
**assembly.py**: Crée la base de données "Assembly" en extrayant et stockant les données relatives aux assemblages génomiques.  
**genome.py**: Crée la base de données "Genome" en extrayant et stockant les informations sur les génomes.  
**contigs.py**: Crée la base de données "Contigs" en extrayant et stockant les données concernant les contigs.  
**sample.py**: Crée la base de données "Biosample" en extrayant et stockant les informations sur les échantillons biologiques.  
**database.py**: Crée les tables grâce à Mysql.


