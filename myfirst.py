import seaborn as sns
iris = sns.load_dataset('iris') # returns a pandas dataframe
import pandas as p
sns.boxplot(data=iris)
