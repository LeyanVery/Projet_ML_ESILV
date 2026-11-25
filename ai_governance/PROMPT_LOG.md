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

## Interaction 2 - Review and Improvement of the Week 1 Report

Date: November 25, 2026
Author: James HIM
AI Tool: ChatGPT

### Original Prompt

J'ai relu notre rapport Week 1 ainsi que les différents fichiers de notre projet Machine Learning et j'ai identifié plusieurs points qui nécessitent des améliorations.

Je souhaite que tu analyses ces problèmes et que tu m'indiques précisément les modifications à effectuer. Je vais appliquer tes recommandations directement dans VS Code.

Voici les points que j'ai identifiés :

1. Problem formalisation: Notre problématique manque de formalisation mathématique. Je souhaite définir clairement le vecteur de variables explicatives X, la variable cible y, l'objectif de prédiction et les métriques que nous utiliserons pour évaluer nos modèles.

2. Business scope: Les enjeux financiers de notre problématique ne sont pas suffisamment développés. Il faut expliquer les conséquences d'un faux positif (refuser ou signaler un client fiable) et d'un faux négatif (ne pas détecter un client qui fera défaut). Il faut également préciser le périmètre réel de notre projet.

3. Yeh & Lien (2009): Cette référence figure dans notre bibliographie, mais elle n'est pas suffisamment intégrée dans le corps du rapport. Je souhaite mieux l'exploiter tout en nuançant son utilisation comme benchmark, car les résultats de leur étude ne sont pas nécessairement directement comparables à ceux que nous obtiendrons.

4. Dataset documentation: Notre rapport ne présente pas suffisamment les 23 variables explicatives. Je souhaite ajouter un tableau récapitulatif indiquant leur description et leur type.

5. Class imbalance: La formulation actuelle concernant le déséquilibre des classes doit être corrigée. Notre dataset contient 22,12 % de défauts de paiement. Il faut éviter de présenter ce déséquilibre comme particulièrement important sans le contextualiser.

6. Report wording: Certaines formulations de notre rapport, notamment l'expression « Of course », ne sont pas suffisamment adaptées à un rapport académique. Je souhaite les reformuler.

7. Repository documentation: Notre README.md est actuellement vide. Je souhaite le compléter avec une présentation claire du projet, de son objectif et de son organisation.

8. Dataset validation: Je souhaite également renforcer notre script check_dataset.py en ajoutant une vérification des doublons et une inspection des variables catégorielles X2, X3 et X4.

Pour chaque point, indique précisément où effectuer les modifications et fournis-moi les paragraphes ou le code directement utilisables.

Il est important de conserver la cohérence avec notre travail existant, de ne pas inventer de résultats expérimentaux et de distinguer les éléments déjà vérifiés des recommandations méthodologiques.

Je souhaite également que tu me guides étape par étape pour appliquer ces changements dans VS Code.

### AI Response

ChatGPT analysed the identified weaknesses and provided concrete modifications for the project.

The proposed improvements included:
- Adding a mathematical formalisation of the prediction problem.
- Clarifying the financial implications of classification errors and defining the business scope.
- Improving the integration of Yeh & Lien (2009) while being cautious about direct performance comparisons.
- Adding a summary table of the 23 explanatory variables.
- Correcting the interpretation of class imbalance.
- Improving the academic wording of the report.
- Completing the README.md file.
- Adding duplicate detection and categorical variable inspection to check_dataset.py.

ChatGPT also provided ready-to-use paragraphs and code snippets to facilitate implementation in VS Code.

### Verification and Critical Review

We reviewed the proposed modifications and checked their consistency with our project and dataset.

We paid particular attention to:
- The accuracy of the mathematical definition and prediction target.
- The descriptions and types of the dataset variables.
- The financial interpretation of false positives and false negatives.
- The appropriate positioning of Yeh & Lien (2009), without treating their results as automatically comparable to ours.
- The distinction between our verified dataset characteristics and future experimental objectives.

We also ensured that the class imbalance was described accurately, based on the 22.12% default rate already verified using Python.

### Our Decision

We decided to retain the relevant recommendations and improve our Week 1 report accordingly.

We refined the discussion of Yeh & Lien (2009), clarified the problem formulation and business scope, and improved the dataset documentation.

We also worked on improving the project repository and its validation procedures.

The creation of CONTRIBUTIONS.md was discussed but has not yet been completed.

No model has been trained at this stage.

## Interaction 3 - Clarifying the Success Criterion

Date: November 25, 2026
Author: James HIM
AI Tool: Copilot

### Original Prompt

Replace the vague success criterion in "Problem formalisation" with a
cross-validation variability comparison against the logistic regression
baseline, and clarify that Yeh and Lien [2] are prior scientific work rather
than a performance target.

### Verification and Critical Review

The previous wording compared our model with Yeh and Lien's findings, then
clarified that their probability-estimation criterion was not interchangeable
with ROC-AUC or PR-AUC. The revised criterion compares the model with the
logistic regression baseline and requires the difference to exceed variability
across cross-validation folds.

### Our Decision

We adopted the proposed wording without changing other report sections.