import pandas as pd

predict = pd.read_csv('../plot_entropy_rate_dt/predictability_dist_only_POI_NSD_DBSCAN.csv', index_col=0)

col = predict.columns
usernames = []
for c in col:
	usernames.append(c[:-4])

predict.columns = usernames