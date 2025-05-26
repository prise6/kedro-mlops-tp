# %%
import pandas as pd
import pandera.pandas as pa
from pandera.typing import DataFrame

from kedro_mlops_tp.schemas import ModelInputTableSchema


# %%
@pa.check_types
def read_model_input_table(filepath: str) -> DataFrame[ModelInputTableSchema]:
    return pd.read_parquet(filepath).pipe(DataFrame[ModelInputTableSchema])


# %%
read_model_input_table("data/03_primary/model_input_table.parquet")

# %%
