import pandas as pd
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

df = pd.read_csv(url,names=['sepal length','sepal width','petal length','petal width','target'])

from sklearn.preprocessing import StandardScaler
features = ['sepal length','sepal width','petal length','petal width']
x = df.loc[:,features].values
y = df.loc[:,['target']].values
x = StandardScaler().fit_transform(x)

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents,columns=['principal component 1',
                                                               'principal component 2'])
finalDf = pd.concat([principalDf,df[['target']]],axis=1)

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('Dwa komponenty PCA', fontsize = 20)

targets = ['Iris-setosa','Iris-versicolor','Iris-virginica']
colors= ['r','g','b']
for target, color in zip(targets, colors):
    itk = finalDf['target'] == target
    ax.scatter(finalDf.loc[itk,'principal component 1'], finalDf.loc[itk,'principal component 2'],
               c = color,
               s = 50)
    ax.legend(targets)
    ax.grid()
plt.show()
print(pca.explained_variance_ratio_)ata"
