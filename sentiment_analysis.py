import csv
import sys
import re
import pandas as pd
from textblob import TextBlob

data = []

with open('t13.csv', 'rb') as file:
	my_table = csv.reader(file, delimiter=' ')
	for line in my_table:
		text=', '.join(line)
		regex_clean=' '.join(re.sub("([\d \t ])|(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(RT)", " ", text).split())
		
		#TextBlob analisa cada linha "limpa"
		analysis= TextBlob(regex_clean)
		polarity = 'Positiva'
		
		#É usada a polaridade do TextBlob para a analise de sentimentos
		if (analysis.sentiment.polarity < 0):
			polarity = 'Negativa'
		elif (0 <= analysis.sentiment.polarity <= 0.2):
			polarity = 'Neutra'
		
		dic = {}
		dic['Sentiment_Type']=polarity
		dic['Tweet']=regex_clean
		data.append(dic)

#Transforma o dict em um DataFrame
df=pd.DataFrame(data)

#Transforma o DataFrame em .csv
df.to_csv('sentiment_analysis.csv')


#
# Visualização gráfica usando matplotlib 
#

import matplotlib.pyplot as plt
%matplotlib inline

#Quantidade Total de Sentimentos por Categoria (Positiva, Neutra ou Negativa)
tweet_totals = df.groupby('Sentiment_Type').size()

my_plot = tweet_totals.sort(ascending=True).plot(kind='bar')

my_plot = tweet_totals.plot(kind='bar',legend=None,title="Analise de Sentimentos Twiter")
my_plot.set_xlabel("Categoria")
my_plot.set_ylabel("Numero de Tweets")




