# kedro_mlops_tp

[![Powered by Kedro](https://img.shields.io/badge/powered_by-kedro-ffc900?logo=kedro)](https://kedro.org)

## Pré-requis

* Installer [`uv`](https://github.com/astral-sh/uv)
* Installer [`kedro`](https://docs.kedro.org/en/stable/index.html) via `uvx kedro`
* A chaque situation relancer `uv sync`


## Objectifs

* Initialisation du projet - découverte des pipelines ☑️
* Profiling des données (EDA) ☑️
* Validation des données avec pandera (data validation) ☑️
* Ajout de mlflow (experiment tracking) ☑️
* Evaluation du modèles avec mlflow.evaluate (Model validation) ☑️
* Interprétabilité du modèle et explicabilité avec InterpretML (XAI) ☑️
* Ajout de dvc (data versioning) ☑️
* Reporting avec evidently (drift) ☑️
* Packager le projet avec docker (prod) ☑️
* Model serving ☑️

## Situations


## Découverte de Kedro

> It is 2160, and the space tourism industry is booming. Globally, thousands of space shuttle companies take tourists to the Moon and back. You have been able to source data that lists the amenities offered in each space shuttle, customer reviews, and company information.


1. `uvx kedro new --starter=spaceflights-pandas`
2. `uv sync`

* [kedro](https://kedro.org/)
* [essential-components-of-a-kedro-project](https://docs.kedro.org/en/stable/get_started/minimal_kedro_project.html#essential-components-of-a-kedro-project)
* [kedro spaceflights tuto](https://docs.kedro.org/en/stable/tutorial/tutorial_template.html)


🚨 **Avertissement**: dans la suite des situations, le repo [prise6/kedro-mlops-tp](https://github.com/prise6/kedro-mlops-tp) doit être cloner. Ce dernier étend le tutoriel _spacefights_ de base avec des notions de MLOps dans le cadre d'un TP.

Ci dessous un exemple pour se mettre dans la situation 1.

```bash
git clone https://github.com/prise6/kedro-mlops-tp
cd kedro-mlops-tp
git checkout situation/1
uv sync
```

## Situation 1: un projet structuré

`git checkout situation/1`

1. Quelles sont les pipelines ? A quoi elles servent ?
2. Quelles sont les outils d'aide à la qualité utilisées ? Que manque-t-il ?
3. Comment créer les données `reviews_prod.csv` et `reviews_dev.csv` ?
4. Lancer le pipeline de `data_processing`. Corriger les erreurs.

<details>

<summary>Retour à la normale</summary>

`git checkout feat-pipeline`

</details>

## Situation 2: exploration

`git checkout situation/2`

1. Lancer le pipeline de `data_processing`. Corriger les erreurs.
2. Quelles nodes a été ajouté ? De quel type est l'output ?
3. Donne les variables les plus corrélées.
4. Explorer.

Indice: [ici](https://docs.profiling.ydata.ai/latest/getting-started/concepts/)

<details>

<summary>Retour à la normale</summary>

`git checkout feat-profiling`

</details>

## Situation 3: validation de donnée

`git checkout situtation/3`

1. Lancer le notebook `data_validation.py` en interactif ou en CLI.
2. Corriger les erreurs.
3. Ajouter une règle de validation
4. Lancer le pipeline `data_processing`. Corriger les erreurs.

Indices:
* [pandera](https://pandera.readthedocs.io/en/stable/index.html)
* [kedro-pandera](https://kedro-pandera.readthedocs.io/en/stable/index.html)

<details>

<summary>Retour à la normale</summary>

`git checkout feat-data-validation`

</details>


## Situation 4: traquer les expériences

`git checkout situation/4`

1. Lancer le notebook `experiment_tracking.py`. Que faut-il lancer avant ?
2. Changer le nom de l'expérience.
3. Decommenter les lignes qui suivents `# A DECOMMENTER` petit à petit. Commenter les résultats.
4. Logger la signature et des données d'exemples du modèle.
5. Quelles sont les fonctionnalités de mlflow ? Différence entre Tracking server, backend store, artifactor store et model registry ?

Indices: 

* [mlflow](https://mlflow.org/docs/latest/)
* [mlfow-dataset](https://mlflow.org/docs/latest/dataset/)
* [mlflow api python](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.sklearn.html?highlight=autolog#mlflow.sklearn.autolog)
* [mlflow tracking](https://mlflow.org/docs/latest/tracking/#tracking-setup)

<details>

<summary>Retour à la normale</summary>

`git checkout feat-mlflow`

</details>

## Situation 5: mlflow + kedro

`git checkout situation/5`

1. Ajouter mlflow à kedro. Aidez vous de la documentation. 
2. Lister les pipelines kedro. Lancer la pipeline `trainig`. Verifier les artifacts dans l'UI mlflow.
3. Lancer la pipeline `inference`. Corrigez les erreurs.

Indices:

* pour `1/` on cherche qqch de simple et on veut ajouter `--env base` comme paramètre. 
* [kedro-mlflow](https://kedro-mlflow.readthedocs.io/en/latest/source/02_getting_started/01_installation/01_installation.html).
* pour `3/`, faites des actions manuelles dans l'UI de mlflow. Regarder dans `catalog` l'entrée `selected_regressor`.

<details>

<summary>Retour à la normale</summary>

`git checkout feat-kedro-mlflow`

</details>


## Situation 6: evaluation du modèle

`git checkout situation/6`

* Lancer la pipeline d'entrainement et noter l'ajout du noeud `evaluate_model`.
* Que fait `mlflow.evaluate` ?
* Quelles sont les variables explicatives du modèles ?

<details>

<summary>Retour à la normale</summary>

`git checkout feat-evaluate`

</details>


## Situation 7: expliquer les prédictions

`git checkout situation/7`

* Lancer la pipeline `prediction` et noter l'ajout du noeud `explain`.
* Voir les artifacts générés dans mlflow.
* Comment interpréter les graphiques ?

<details>

<summary>Retour à la normale</summary>

`git checkout feat-xai`

</details>


## Situation 8: data versionning

`git checkout situation/8`

* Installer `dvc`. Suivre la documentation.
* Modifier les données. Créer un commit. Puis revenir aux données précédentes.
* Est-ce possible de traquer les données depuis un serveur distant ?
* Quelles données doivent être absolument traquées pour assurer la reproductibilité ?


Indices:
* [kedro dvc](https://docs.kedro.org/en/stable/integrations/kedro_dvc_versioning.html)
* quelques commandes: `dvc checkout`, `dvc data status`, `dvc init`, `dvc status`, `dvc add`


<details>

<summary>Retour à la normale</summary>

`git checkout feat-dvc`

</details>


## Situation 9: reproductibilité avec dvc pipeline

`git checkout situation/9`

* Prendre connaissance du fichier `dvc.yaml`
* Traquer les données `reviews_dev.csv` et `shuttles.xlsx` avec `dvc add ...`.
* Lancer `dvc dag` puis `dvc repro`
* Relancer `dvc repro`: que se passe-t-il ?
* Essayer de mofier les inputs et voir ce qu'il se passe.
* Ajouter un nouveau stage pour la prédiction.

Indice:
* [kedro dvc (advanced)](https://docs.kedro.org/en/stable/integrations/kedro_dvc_versioning.html#advanced-use-cases) 


<details>

<summary>Retour à la normale</summary>

`git checkout feat-dvc-repro`

</details>


## Situation 10: monitoring et drift

`git checkout situation/10`

* Lancer le pipeline de prédiction `kedro run --pipeline prediction`.
* Voir le noeud `create_evidently_report`.
* Ajouter les tests de evidently.
* Commenter les résultats.

Indices: 
* [evidentlyai](https://docs.evidentlyai.com/docs/library/tests)


<details>

<summary>Retour à la normale</summary>

`git checkout feat-monitoring-drift`

</details>


## Situation 11: dockerization

`git checkout situation/11`

* Exporter les requirements `uv export --no-hashes --no-dev --no-annotate --no-editable --no-emit-project -o requirements.txt`
* Suivre la documentation pour packager le projet kedro avec docker.
* A part docker, comment packager le projet ?

Indice:
* [kedro-docker](https://github.com/kedro-org/kedro-plugins/tree/main/kedro-docker)
* `kedro docker init`, `kedro docker build`, `kedro docker run`


<details>

<summary>Retour à la normale</summary>

`git checkout feat-docker`

</details>


## Situation 12: model serving


`git checkout situation/12`

* Lancer le notebook `online_predictions.py`. Faites en sorte que la requête fonctionne.
* Suivre la documentation mlflow pour déployer un serveur localement.
* Comment déployer de façon plus propre ? Quelles commandes pour générer l'image?

Indice:
* [deploy model locally](https://mlflow.org/docs/latest/deployment/deploy-model-locally/)
* [mlflow model to kubernetes](https://mlflow.org/docs/latest/deployment/deploy-model-to-kubernetes/)


<details>

<summary>Retour à la normale</summary>

`git checkout feat-model-serving`

</details>




## Notes de mes commandes

```bash
uvx kedro new --starter spaceflights-pandas --name kedro_mlops_t
git init --initial-branch main
uv sync -p python3.12
ruff format
ruff check
mypy .
python notebooks/reviews.py
kedro run --pipeline inference
kedro run --pipeline inference --nodes explain_node
kedro run python -m notebooks.experiment_tracking
dvc init
dvc data status
git checkout ed91b5c758a35450fa2615ccbf0b354797cbd813 data/01_raw/companies.csv.dvc
dvc repro
dvc status
dvc checkout
uv add kedro-docker
uv export --no-hashes --no-dev --no-annotate --no-editable --no-emit-project -o requirements.txt
kedro docker build
kedro docker run
mlflow models serve -m models:/price_regressor@challenger --env-manager local --port 5005
```