import nltk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression



class Text:
    def __init__(self, title, text, author= None, lang='spanish'):
        self.title = title
        self.author = author
        self.text = text.replace('\n', ' ')
        self.sentences = [i.strip() for i in nltk.sent_tokenize(self.text, language=lang)]
        self.tokens = [token.lower() for token in nltk.word_tokenize(self.text, language=lang)]
        self.words = [i for i in self.tokens if i.isalpha()]
        self.unique_words = set(self.words)
        
    
    def text_info(self):
        print(f'Número de oraciones: {len(self.sentences)}')
        print(f'Número de tokens: {len(self.tokens)}')
        print(f'Número de palabras: {len(self.words)}')
        print(f'Número de palabras únicas: {len(self.unique_words)}')

    def tokens_df(self, columns=10, rows=1):
        df = pd.DataFrame(self.tokens, columns=['token'])
        return df.groupby('token').value_counts().sort_values(ascending=False)[:rows]
    
    def zipf(self):
        tokens = pd.DataFrame(self.tokens, columns=['token'])
        freq_token = self.tokens(rows=-1)
        X = np.array(range(1, len(freq_token) + 1)).reshape(-1, 1)
        X_log=np.log10(X)
        y = freq_token
        y_log = np.log10(y)
        
        ln = LinearRegression()
        ln.fit(X_log, y_log)

        plt.loglog(X, y, 'o', color = 'r')

        plt.xlabel('Rango')
        plt.ylabel('Frecuencia')
        plt.title(f'Ley de Zipf para \"{self.title}\"')
        plt.show()

        return (ln.intercept_, float(-1 * ln.coef_[0]))
    
    def mendenhall(self, n=15):
        length_distributions = nltk.FreqDist([len(token) for token in self.words])
        length_distributions.plot(n, title='Mendenhall');





class Corpus:
    def __init__(self, list_of_texts):
        self.list_of_texts = list_of_texts

        self.sentences = []
        for i in list_of_texts:
            for j in i.sentences:
                self.sentences.append(j)

        self.tokens = []
        for i in list_of_texts:
            for j in i.tokens:
                self.tokens.append(j)

        self.ordered_tokens = list(pd.DataFrame(self.tokens, columns=['token']).groupby('token').value_counts().sort_values(ascending=False).index)

        self.words = [i for i in self.tokens if i.isalpha()]
        self.unique_words = set(self.words)
        
    
    def corpus_info(self):
        print(f'Número de oraciones: {len(self.sentences)}')
        print(f'Número de tokens: {len(self.tokens)}')
        print(f'Número de palabras: {len(self.words)}')
        print(f'Número de palabras únicas: {len(self.unique_words)}')


    def comparar_textos(self, n=10):
        most_common_words_df = pd.DataFrame(columns=self.ordered_tokens[:n])
        for i in self.list_of_texts:
            most_common_words_df.loc[i.title] = [i.tokens.count(j) for j in self.ordered_tokens[:n]]    
        return most_common_words_df
    
    def analisis1(self, n=10):
        df = self.comparar_textos(n=n).T
        df = (df/df.sum()).T
        return df

    def knn(self, n=50):
        df = self.analisis1(n=n)
        unknown_writers = [n for n,i in enumerate([j.author for j in self.list_of_texts]) if i == None]
        new_point = df.iloc[unknown_writers,:]
        knn = KNeighborsClassifier(n_neighbors=3)

        X = df.drop(df.index[unknown_writers])
        y = pd.DataFrame([i.author for i in self.list_of_texts]).dropna()

        knn.fit(X, y.values.ravel())
        
        prediction = knn.predict(new_point)
        return pd.DataFrame({'Título':[i.title for n, i in enumerate(self.list_of_texts) if n in unknown_writers], 'Autor_sugerido':prediction})
        





