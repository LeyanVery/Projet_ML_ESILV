# AI Prompt Log

Project: Credit Card Default Prediction Using Machine Learning

Team: Leyan VERY and James HIM

This document records the main interactions with AI tools used during our machine learning project. For each interaction, we will keep the original prompt, the AI's response, the checks we performed, and the decisions we made


## Interaction 1 - Dataset Validation and Methodology

Date: November 23, 2026
Author: Leyan VERY
AI Tool: ChatGPT

### Original Prompt

Nous réalisons un projet de Machine Learning en spécialisation Finance à l'ESILV, consacré à la prédiction du défaut de paiement par carte de crédit.

Nous avons sélectionné le dataset "Default of Credit Card Clients" de l'UCI Machine Learning Repository (ID 350).

Nous avons effectué une première vérification avec Python et obtenu :

- 30 000 observations
- 23 variables explicatives (X1 à X23)
- 6 636 défauts de paiement (22,12 %)
- 23 364 non-défauts (77,88 %)
- Aucune valeur manquante

Avant de commencer la modélisation, nous souhaitons vérifier la pertinence de nos choix d'un point de vue financier et statistique.

1. Analyse la pertinence de ce dataset pour prédire le défaut de paiement et explique ses principales limites.
2. Identifie les variables susceptibles de présenter un risque de data leakage. Précise quelles informations doivent être disponibles au moment de la prédiction.
3. Propose une stratégie de séparation des données entre entraînement et test, en justifiant le choix et les risques associés.
4. Évalue l'impact potentiel du déséquilibre des classes sur les résultats et recommande des métriques adaptées. Explique pourquoi l'accuracy seule pourrait être insuffisante.
5. Propose une baseline simple et interprétable, adaptée à notre problématique financière.
6. Identifie les hypothèses statistiques et les contrôles que nous devrons effectuer avant l'entraînement.

Pour chaque recommandation, justifie ton choix et indique les risques, les alternatives possibles ainsi que les vérifications nécessaires.

Ne génère aucun résultat expérimental fictif. Distingue les constats vérifiés des hypothèses et des recommandations.

Nous voulons pouvoir comprendre, vérifier et défendre chaque décision méthodologique lors de notre soutenance.

### AI Response

We asked ChatGPT to critically evaluate our dataset and propose
a methodology for our credit default prediction project.

ChatGPT recommended:
- Keeping the UCI Credit Default dataset.
- Using an 80/20 stratified train-test split.
- Applying 5-fold cross-validation on the training data.
- Using logistic regression as our first predictive model.
- Evaluating performance with precision, recall, F1 and ROC-AUC.
- Checking potential data leakage before training.

### Verification and Critical Review

We had already verified the dataset using Python:
- 30,000 observations
- 23 features
- 22.12% of customers in the default class
- No missing values

We also identified two points requiring further verification.

First, the availability of September 2005 variables at the
prediction date is not fully established by the documentation.

Second, the proposed validation strategy cannot measure
how well the model would perform in a different economic period.

### Our Decision

We decided to retain the dataset and use the proposed methodology
as a starting point for Week 2.

We will verify the data categories, check for duplicates and
implement the train-test split before fitting any preprocessing.

No model has been trained at this stage.
