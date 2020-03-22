import pickle
a = pickle.load(open("pretrained_model.p","rb"))
# Perspective Score, Stanford Polite 


print(a.predict([[0.1,0.2]]))

print(a.predict([[1,1],[5,5]]))





#import get_results 
#get_results.test_on("new_issues","new_comments","output_file")
