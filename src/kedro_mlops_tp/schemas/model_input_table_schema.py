from typing import cast

import pandas as pd
import pandera.pandas as pa
from pandera.typing import Series


class ModelInputTableSchema(pa.DataFrameModel):
    shuttle_id: Series[int] = pa.Field(unique=True)
    engine_type: Series[str] = pa.Field(isin=["Quantum", "Plasma", "Nuclear"])
    passenger_capacity: Series[int] = pa.Field(ge=0, le=20)
    review_scores_rating: Series[float] = pa.Field(le=100)

    @pa.dataframe_check
    def score_correlation(cls, df: pd.DataFrame) -> Series[bool]:
        return cast(
            Series[bool],
            df["review_scores_rating"].corr(df["review_scores_comfort"]) >= 0.5,
        )
