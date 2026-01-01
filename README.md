# 🫀 CardioPredict AI - Prédiction de Maladie Cardiaque avec Spark MLlib

[![Spark](https://img.shields.io/badge/Apache_Spark-3.2.1-E25A1C?style=flat&logo=apache-spark)](https://spark.apache.org/)
[![Scala](https://img.shields.io/badge/Scala-2.12-DC322F?style=flat&logo=scala)](https://www.scala-lang.org/)
[![Docker](https://img.shields.io/badge/Docker-Cluster-blue?style=flat&logo=docker)](https://www.docker.com/)
[![Flask](https://img.shields.io/badge/Flask-3.0.3-000000?style=flat&logo=flask)](https://flask.palletsprojects.com/)
[![Render](https://img.shields.io/badge/Déployé%20sur-Render-6C3AFC?style=flat&logo=render)](https://render.com)

> **Projet Big Data complet** : Classification et clustering sur le dataset **UCI Heart Disease** avec **Apache Spark MLlib** en mode distribué, suivi du développement et déploiement d'une application web interactive.

**🌐 Démo en ligne** : [https://cardiopredict-oubi.onrender.com](https://cardiopredict-oubi.onrender.com/)

---

## 📊 Vue d'Ensemble du Projet

### Phase 1 : Big Data avec Spark MLlib
- **Dataset** : UCI Statlog Heart Disease (270 patients, 13 features médicales)
- **Environnement** : Cluster Docker (Master + Slave) avec HDFS et Spark Standalone
- **Technologies** : Spark 3.2.1, Scala 2.12, Hadoop 3.x, Maven
- **Algorithmes** : Decision Tree, Random Forest, K-Means
- **Résultats** : Random Forest Accuracy ≈ 84%

### Phase 2 : Application Web Interactive
- **Framework** : Flask 3.0.3 (Python)
- **Fonctionnalités** : Prédiction en temps réel, visualisation des risques, recommandations personnalisées

---

## 🎯 Objectifs Pédagogiques Couverts

✅ **RDD Operations** : textFile, map, filter, count, cache, randomSplit  
✅ **Types MLlib** : Vectors.dense, LabeledPoint  
✅ **Preprocessing** : StandardScaler (withMean, withStd)  
✅ **Classification** : DecisionTree, RandomForest avec tuning  
✅ **Clustering** : KMeans + WSSSE  
✅ **Évaluation** : Accuracy, Error rate, Feature Importance  
✅ **Déploiement** : Application web production-ready  

---

## 📸 Aperçu Visuel

### Application Web Déployée
<img width="1881" height="967" alt="Capture d’écran 2026-01-01 221756" src="https://github.com/user-attachments/assets/4c1db0b6-6db7-4d84-95f4-2b79deb4f971" />


### Architecture du Cluster Spark
```
Docker Network: cluster
├── master (NameNode + Spark Master)
│   ├── Ports: 7077, 8080, 9870, 8088
│   └── Services: HDFS, Spark, YARN
└── slave1 (DataNode + Spark Worker)
    └── Services: HDFS DataNode, Spark Worker
```

---

## PARTIE 1 : Développement avec Spark MLlib

### Étape 1 : Préparation de l'Environnement

#### 1.1 Démarrage du Cluster Docker

**Terminal 1 - Master :**
<img width="1228" height="558" alt="carbon" src="https://github.com/user-attachments/assets/7fb05aec-5735-4977-b47a-0e54e262d844" />

**Terminal 2 - Slave :**
<img width="1142" height="522" alt="carbon (1)" src="https://github.com/user-attachments/assets/bbc0dc3c-c216-49a4-b888-0e0ea56a6733" />

<img width="1918" height="532" alt="Capture d’écran 2026-01-01 221548" src="https://github.com/user-attachments/assets/ee80cd29-ae6c-468f-96ad-9fe64ca5ec79" />


#### 1.2 Configuration des Services

**Dans chaque container :**
<img width="856" height="484" alt="carbon (2)" src="https://github.com/user-attachments/assets/d128c420-e5a8-4952-bec7-efc127b1ab4e" />


**Sur le Master uniquement :**
<img width="806" height="856" alt="carbon (3)" src="https://github.com/user-attachments/assets/ac27d91b-ed5c-4076-80a0-c5bdf5fc3c05" />


**Sortie attendue de `jps` :**
<img width="552" height="596" alt="carbon (4)" src="https://github.com/user-attachments/assets/97a9847d-b166-4f75-8cc7-2acf36142784" />


### Étape 2 : Préparation du Dataset

#### 2.1 Téléchargement et Nettoyage
<img width="1952" height="894" alt="carbon (5)" src="https://github.com/user-attachments/assets/a2168786-c06c-4266-b9ed-a47fe85cece4" />


#### 2.2 Description du Dataset

| Feature | Description | Type |
|---------|-------------|------|
| age | Âge du patient | Numérique |
| sex | Sexe (1=homme, 0=femme) | Catégorique |
| cp | Type de douleur thoracique (1-4) | Catégorique |
| trestbps | Pression artérielle au repos (mmHg) | Numérique |
| chol | Cholestérol sérique (mg/dl) | Numérique |
| fbs | Glycémie à jeun > 120 mg/dl (1=oui) | Binaire |
| restecg | Résultats ECG au repos (0-2) | Catégorique |
| thalach | Fréquence cardiaque maximale | Numérique |
| exang | Angine induite par l'exercice (1=oui) | Binaire |
| oldpeak | Dépression ST induite par l'exercice | Numérique |
| slope | Pente du segment ST (1-3) | Catégorique |
| ca | Nombre de vaisseaux colorés (0-3) | Catégorique |
| thal | Thalassémie (3=normal, 6=défaut fixe, 7=défaut réversible) | Catégorique |
| **target** | **Label : 0=sain, 1=maladie cardiaque** | **Binaire** |

#### 2.3 Chargement dans HDFS

<img width="1917" height="842" alt="Capture d’écran 2026-01-01 220118" src="https://github.com/user-attachments/assets/3fd01c1b-a375-4444-bdcf-609ea8c80bd0" />
<img width="1917" height="788" alt="Capture d’écran 2026-01-01 220144" src="https://github.com/user-attachments/assets/483bb0b3-1da9-41d2-883c-1fec61f4703c" />
<img width="1917" height="793" alt="Capture d’écran 2026-01-01 220203" src="https://github.com/user-attachments/assets/e382ef35-5022-46e4-9712-51a309c4949d" />
<img width="756" height="653" alt="Capture d’écran 2026-01-01 220220" src="https://github.com/user-attachments/assets/c0eb925b-f03c-413e-9062-1f1ee842b2f2" />

### Étape 3 : Création du Projet Spark MLlib

#### 3.1 Structure du Projet Maven

<img width="1176" height="782" alt="carbon (6)" src="https://github.com/user-attachments/assets/722c6f84-7a72-4450-b6d7-253612e77827" />


#### 3.2 Configuration `pom.xml`
<img width="1378" height="2830" alt="carbon (7)" src="https://github.com/user-attachments/assets/3a74c171-1c0c-4302-916a-499a541aad5a" />


#### 3.3 Code Scala Principal

**Créer le répertoire source :**
<img width="1194" height="522" alt="carbon (8)" src="https://github.com/user-attachments/assets/b85db371-1bca-4898-9064-8d1355e388a4" />


**Voir le code complet dans** : [`HeartDiseaseML.scala`](src/main/scala/com/spark/ml/HeartDiseaseML.scala)
<img width="2048" height="12330" alt="carbon (9)" src="https://github.com/user-attachments/assets/05886c4b-4c15-440c-a52a-cf958af6e2fd" />




#### 4.2 Soumission du Job Spark
<img width="1462" height="596" alt="carbon (10)" src="https://github.com/user-attachments/assets/6c744e06-302e-498f-a678-e3402d777212" />


#### Visualisation des Résultats

**Interfaces Web disponibles :**
- **Spark UI** : http://localhost:8080 - Monitoring des jobs
- **HDFS UI** : http://localhost:9870 - Système de fichiers
- **YARN UI** : http://localhost:8088 - Gestion des ressources

<img width="1917" height="977" alt="Capture d’écran 2026-01-01 222302" src="https://github.com/user-attachments/assets/133549d2-df84-4653-8ed2-065b010d2d74" />
<img width="1917" height="907" alt="Capture d’écran 2026-01-01 222146" src="https://github.com/user-attachments/assets/fcf663cb-31ed-41ea-87fb-9f7a0317ae15" />
<img width="1918" height="892" alt="Capture d’écran 2026-01-01 222203" src="https://github.com/user-attachments/assets/bd5f2c6a-0cb2-4679-bcd6-383b2a1f0058" />
<img width="1918" height="796" alt="Capture d’écran 2026-01-01 222219" src="https://github.com/user-attachments/assets/2b8768da-cdec-4083-a804-6b5863cff4f8" />

---

## 🌐 PARTIE 2 : Développement de l'Application Web

### Étape 6 : Analyse des Résultats et Extraction des Insights

Après avoir obtenu les résultats de Spark MLlib, j'ai analysé :

1. **Feature Importance** : Les facteurs les plus prédictifs
   - `thal` (thalassémie) : 23.4%
   - `ca` (vaisseaux colorés) : 18.8%
   - `cp` (type de douleur) : 16.5%
   - `oldpeak` (dépression ST) : 14.3%

2. **Accuracy du modèle** : ~84% avec Random Forest

3. **Facteurs de risque** : Identification des seuils critiques
   - Cholestérol > 240 mg/dl
   - Âge > 55 ans
   - Thal = 6 ou 7 (défauts)
   - CA > 0 (vaisseaux bloqués)

---

### Étape 7 : Création de l'Application Flask

#### 7.1 Structure du Projet Web

```
heart-disease-web/
├── app.py                 # Application Flask
├── requirements.txt       # Dépendances Python
├── templates/
│   └── index.html        # Interface utilisateur
└── README.md
```

### Étape 8 : Déploiement 

#### 8.1 Préparation du Repository GitHub


##  Résultats et Comparaisons

### Performance du Modèle Spark MLlib

| Algorithme | Accuracy | Error Rate | Notes |
|------------|----------|------------|-------|
| Decision Tree | 82.7% | 17.3% | Rapide, interprétable |
| Random Forest | **83.9%** | 16.1% | **Meilleur résultat** |
| K-Means (3 clusters) | WSSSE: 1234 | - | Clustering non supervisé |

### Feature Importance (Random Forest)

```
1. thal          23.4%  ████████████████████████
2. ca            18.8%  ███████████████████
3. cp            16.5%  █████████████████
4. oldpeak       14.3%  ███████████████
5. chol           9.9%  ██████████
6. age            7.6%  ████████
7. thalach        4.2%  ████
8. exang          3.1%  ███
9. slope          1.5%  ██
10. autres        0.7%  █
```

### Comparaison Spark vs Application Web

| Aspect | Spark MLlib | Application Web |
|--------|-------------|----------------|
| **But** | Entraînement du modèle | Prédiction en production |
| **Environnement** | Cluster distribué | Cloud (Render) |
| **Performance** | 84% accuracy | Simulation basée sur feature importance |
| **Scalabilité** | Très haute (Big Data) | Moyenne (web classique) |
| **Temps réponse** | Minutes (batch) | < 1 seconde (temps réel) |

---

## 🎓 Compétences Démontrées

### Big Data & Spark
- ✅ Configuration d'un cluster Spark (Master/Slave)
- ✅ Manipulation de HDFS
- ✅ Programmation Scala avec Spark MLlib
- ✅ RDD operations (map, filter, reduce)
- ✅ Machine Learning distribué
- ✅ Évaluation de modèles (accuracy, feature importance)

### Développement Web
- ✅ Développement backend avec Flask
- ✅ Interface utilisateur moderne (HTML/CSS/JS)
- ✅ Intégration de logique ML dans une application
- ✅ Gestion de formulaires et validation

### DevOps & Déploiement
- ✅ Gestion de version avec Git/GitHub
- ✅ Déploiement sur plateforme cloud (Render)
- ✅ Configuration CI/CD (auto-deploy)
- ✅ Containerisation avec Docker

---

## 📁 Structure Finale du Projet

```
cardiopredict-project/
├── spark-ml/                          # Partie Spark MLlib
│   ├── heart-disease-spark/
│   │   ├── pom.xml
│   │   ├── src/
│   │   │   └── main/
│   │   │       └── scala/
│   │   │           └── com/
│   │   │               └── spark/
│   │   │                   └── ml/
│   │   │                       └── HeartDiseaseML.scala
│   │   └── target/
│   │       └── heart-disease-spark-1.0-SNAPSHOT-jar-with-dependencies.jar
│   └── data/
│       ├── heart.dat
│       └── heart_prepared.dat
│
└── web-app/                           # Application Web
    ├── app.py
    ├── requirements.txt
    ├── templates/
    │   └── index.html
    ├── screenshots/
    │   ├── demo-interface.png
    │   ├── results-console.png
    │   └── ...
    └── README.md
```



## 📝 Rapport Technique

### Abstract
Ce projet démontre l'utilisation complète d'Apache Spark MLlib pour l'analyse de données médicales, du traitement distribué à la mise en production via une application web. Le dataset UCI Heart Disease (270 patients) a été traité dans un cluster Spark distribué, permettant d'obtenir une accuracy de 83.9% avec Random Forest. Les insights obtenus ont ensuite été intégrés dans une application Flask moderne déployée sur Render.com.

### Méthodologie
1. **Collecte** : Dataset UCI standardisé
2. **Preprocessing** : Normalisation avec StandardScaler
3. **Modélisation** : DecisionTree, RandomForest, KMeans
4. **Évaluation** : Accuracy, Feature Importance, WSSSE
5. **Production** : Application web interactive

### Résultats Clés
- Random Forest surpasse Decision Tree (+1.2% accuracy)
- Thalassémie (thal) est le facteur le plus prédictif (23.4%)
- Le clustering K-Means identifie 3 groupes distincts de patients
- L'application web permet des prédictions en < 1 seconde

### Conclusion
Ce projet illustre le cycle complet d'un projet Big Data : du traitement distribué avec Spark à la mise en production d'une solution utilisable par des non-techniciens. La combinaison Spark MLlib + Flask offre un équilibre optimal entre performance d'entraînement et réactivité en production.

---

## 👥 Auteur

**Rania Chebbi**  
Projet Big Data - Apache Spark & MLlib  


---

**Fait avec ❤️ et beaucoup de ☕**


