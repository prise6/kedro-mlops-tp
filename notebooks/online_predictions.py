# run this before
# mlflow models serve -m models:/price_regressor@challenger --env-manager local --port 5005

# %%
import json

import requests

# %%
serving_inputs = {
    "dataframe_split": {
        "columns": [
            "engines",
            "passenger_capacity",
            "crew",
            "d_check_complete",
            "moon_clearance_complete",
            "iata_approved",
            "company_rating",
            "review_scores_rating",
        ],
        "data": [
            [1, 4, 1, 1, 0, 0, 1, 94],
            [3, 5, 3, 0, 0, 1, 1, 94],
            [2, 3, 3, 1, 0, 0, 1, 100],
            [1, 2, 1, 0, 0, 1, 1, 92],
            [0, 3, 1, 1, 0, 1, 1, 97],
        ],
    }
}

# %%
payload = json.dumps(serving_inputs)
response = requests.post(
    url="http://localhost:5005/invocations",
    data=payload,
    headers={"Content-Type": "application/json"},
)

# %%
response.json()

# %%
# generate production serving image:
# mlflow models generate-dockerfile -m models:/price_regressor@challenger --env-manager local --enable-mlserver
# https://www.mlflow.org/docs/latest/deployment/deploy-model-locally/#serving-frameworks
