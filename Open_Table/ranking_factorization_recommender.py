import pandas as pd
import graphlab as gl

data_set = pd.read_csv("E:\\Google Drive\\Fall 17 Sem 2\\620 Data Visualization\\Project\\Data\\data_with_overall_rating.csv")
#print(data_set[1:2])
user = data_set[['Name']]
cuisine = data_set[['Cuisine']]
environment = data_set[['Environment']]
overall_rating = data_set[['Overall_Rating']]
price = [['Price']]
train_data = gl.SFrame(data_set)
#sf = gl.SFrame({'user_id':user.values.tolist(),
#				'item_id':cuisine.values.tolist(),
#				'rating' :overall_rating.values.tolist()})
def popularity_recommender(item_value,target_value,train_data):
	popularity_model = gl.popularity_recommender.create(train_data, user_id='Name', item_id=item_value, target=target_value)
	print("Popularity Recommender")
	popularity_recomm = popularity_model.recommend(users=range(1,5),k=5)
	popularity_recomm.print_rows(num_rows=25)
	print(type(popularity_recomm))
	return popularity_recomm.to_dataframe()

	
# m = gl.recommender.create(sf,target='rating')
# recs = m.recommend()
# print(recs)


def similarity_recommender(item_value,target_value,train_data):
	item_similarity_model = gl.recommender.item_similarity_recommender.create(train_data, user_id='Name', item_id= item_value, target=target_value)
	item_similarity_model.predict(train_data)
	recs = item_similarity_model.recommend(users=range(1,5),k=5)
	print("Item Similarity Recommender")
	print(recs.print_rows(num_rows=25))
	print(type(recs))
	return recs.to_dataframe()
	
def factorization_recommenders(item_value,target_value,train_data):
	factorization_recommender_model = gl.recommender.factorization_recommender.create(train_data, user_id='Name', item_id=item_value, target=target_value)
	factorization_recommender_model.predict(train_data)
	recs = factorization_recommender_model.recommend(users=range(1,5),k=5)
	print("Item Factorization Recommender")
	print(recs.print_rows(num_rows=25))
	print(type(recs))
	return recs.to_dataframe()



# sim = similarity_recommender("Price","Overall_Rating",train_data)
# print(type(sim))
recommendation = popularity_recommender("Cuisine","Overall_Rating",train_data)
recommendation.to_csv('recommendation.csv')
print(type(recommendation))
f = open('success','wb+')
f.close()
# fac = item_content_recommender("Cuisine","Overall_Rating",train_data)
# print(type(fac))