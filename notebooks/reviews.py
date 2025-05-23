# %%
import pandas as pd

# %%
raw_reviews = pd.read_csv("data/01_raw/reviews.csv")

# %%
prod_reviews = raw_reviews.sample(100, random_state=17)

# %%
dev_reviews = raw_reviews.loc[~raw_reviews.index.isin(prod_reviews.index)]
dev_reviews.shape

# %%
prod_reviews.to_csv("data/01_raw/reviews_prod.csv", index=False)
dev_reviews.to_csv("data/01_raw/reviews_dev.csv", index=False)
