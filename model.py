from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import RandomizedSearchCV

params={'hidden_layer_sizes':[(100,),(150,100),(150,75)],'learning_rate_init':[0.01,0.001,0.1,1],'activation';['relu','logistic'],'solver':['sgd','adam']}
clf = MLPClassifier(solver='adam',activation='relu',hidden_layer_sizes=(150,75),max_iter=2000,batch_size=27017,learning_rate_init=0.01)
rs=RandomizedSearchCV(clf,params,random_state=1, cv=5, verbose=0,n_jobs=-1)

rs.fit(train_Xv,y_train)


rs.score(test_Xv,y_test)


df['review'][30]