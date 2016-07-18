import pandas as pd
import pickle

def get_predict():
	predict = pd.read_csv('../plot_entropy_rate_dt/predictability_dist_only_POI_NSD_DBSCAN.csv', index_col=0)

	col = predict.columns
	usernames = []
	for c in col:
		usernames.append(c[:-4])

	predict.columns = usernames
	return predict

def get_questionare_answers():
	with open('/lscr_paper/amoellga/Data/Telefon/questiondic.p', 'rb') as f:
		answers = pickle.load(f)
	return answers

predict = get_predict()
usernames = predict.columns
answers = get_questionare_answers()