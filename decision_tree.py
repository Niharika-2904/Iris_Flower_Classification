import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
import joblib

df = pd.read_csv(r"C:\Users\Dell\Downloads\iris\iris.data", names = ["sepal length", "sepal width",
      "petal length","petal width","class" ]) #csv-comma separated values

print(df.head())

features = df.iloc[:,0:4]   
target = df.iloc[:,-1]

print(features.head())
print(target.head())

target_encoder = LabelEncoder()
target_encoder.fit(target)
target = target_encoder.transform(target)   

print(target[:5])
print(target_encoder.classes_)

X_train,X_test,Y_train,Y_test= train_test_split(features,target,test_size =0.2, random_state=100)

clf = DecisionTreeClassifier() 
clf.fit(X_train,Y_train)    #fit method in the DecisionTreeClassifier object

pred_value = clf.predict([[5.1,3.9,1.8,0.5]])
print(pred_value)

print(f"\n\nFlower: {target_encoder.classes_[pred_value[0]]}\n\n")


# Save model
joblib.dump(clf, "iris_model.joblib")
joblib.dump(target_encoder, "iris_encoder.joblib")



#Y_pred = clf.predict(X_test)

#acc = accuracy_score(Y_test,Y_pred )
#print(f"{acc=}")

#print(f"{confusion_matrix(Y_test,Y_pred)=}")
#print(f"{classification_report(Y_test,Y_pred)}")       



