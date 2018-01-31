import csv
import sys
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from itertools import chain

# Abrindo, limpando e parseando o arquivo
data = []
with open('t13.csv', 'rb') as file:
	my_table = csv.reader(file, delimiter=' ')
	for line in my_table:
		text=', '.join(line)
		regex_clean=' '.join(re.sub("([\d \t ])|(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(RT)", " ", text).split())
		dic = {}
		dic['Tweet']=regex_clean
		data.append(dic)

#Transforma o dict em um DataFrame
df=pd.DataFrame(data)

#Resolve os problemas de linhas com eror de NaN e faz um split por palavras
tweet = df['Tweet'].astype(str).str.split()

#Usando a lib de Counter para contar as palavras de dentro do DF
counter = Counter(chain.from_iterable(tweet))

#Ignoramos palavras que sao usadas com frequencia mas que nao sao relevantes para nossa analise
ignore = ['the','a','if','in','it','of','or', 'and', 'The', 'for', 'is', 'on', 's', 'nan', 'amp', 'How', 'how', 'you', 
'with', 'are', 'from', 'by', 'via', 't', 'What', 'what', 'de', 'at', 'A', 'that', 'to']
for word in list(counter):
    if word in ignore:
        del counter[word]



counter_ordered = dict(counter.most_common(20))

tweet_words = counter_ordered.keys()
tweet_counts = counter_ordered.values()

#Cria o grafico usando o numpy para dimensionar os dados e o matplotlib para montar a estrutura
indexes = np.arange(len(tweet_words))
width = 0.7
plt.bar(indexes, tweet_counts, width)
plt.xticks(indexes + width * 0.5, tweet_words, rotation='vertical')
plt.show()









