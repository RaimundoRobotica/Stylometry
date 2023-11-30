import nltk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.ensemble import GradientBoostingClassifier



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
        tokens_df = pd.DataFrame(self.tokens, columns=['token'])
        freq_token = self.tokens_df(rows=-1)
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

    def corpus_content(self):
        corpus_content = pd.DataFrame({'Title':[i.title for i in self.list_of_texts],'Author':[i.author for i in self.list_of_texts]})
        return corpus_content


    def comparar_textos(self, n=10):
        most_common_words_df = pd.DataFrame(columns=self.ordered_tokens[:n])
        for i in self.list_of_texts:
            most_common_words_df.loc[i.title] = [i.tokens.count(j) for j in self.ordered_tokens[:n]]    
        return most_common_words_df
    
    def analisis1(self, n=10):
        df = self.comparar_textos(n=n).T
        df = (df/df.sum()).T
        return df
    
    def train_knn(self, k=3, n=1000):
        dict = {'title':[], 'author':[], 'prediction':[], 'tokens':[]}
        authors = pd.DataFrame([i.author for i in self.list_of_texts])
        df = self.analisis1(n=n)
        knn = KNeighborsClassifier(n_neighbors=k)
        for i in range(len(self.list_of_texts)):
            X = df.drop(self.list_of_texts[i].title).values
            y = authors.drop(i)
            test = df.loc[self.list_of_texts[i].title].values.reshape(1, -1)
            knn.fit(X, y.values.ravel())
            prediction = knn.predict(test)
            dict['title'].append(self.list_of_texts[i].title)
            dict['author'].append(self.list_of_texts[i].author)
            dict['prediction'].append(prediction[0])
            dict['tokens'].append(len(self.list_of_texts[i].tokens))
        return pd.DataFrame(dict), knn



    def knn(self, k=3, n=1000):
        df = self.analisis1(n=n)
        unknown_writers = [n for n,i in enumerate([j.author for j in self.list_of_texts]) if i == None]
        new_point = df.iloc[unknown_writers,:]
        knn = KNeighborsClassifier(n_neighbors=k)

        X = df.drop(df.index[unknown_writers])
        y = pd.DataFrame([i.author for i in self.list_of_texts]).dropna()

        knn.fit(X, y.values.ravel())
        
        prediction = knn.predict(new_point)
        return pd.DataFrame({'Título':[i.title for n, i in enumerate(self.list_of_texts) if n in unknown_writers], 'Autor_sugerido':prediction})
        
    
    def train_svc(self, n =1000, kernel='linear', degree=None, coef0=None, C=100, authors=['Emilia Pardo Bazán', 'Benito Pérez Galdós']):
        dict = {'title':[], 'author':[], 'prediction':[], 'tokens':[]}
        y = pd.DataFrame([i.author for i in self.list_of_texts])
        df = self.analisis1(n=n)
        mask = (np.array([i. author for i in self.list_of_texts]) == authors[0]) | (np.array([i. author for i in self.list_of_texts]) == authors[1])
        df = df[mask]
        y = y[mask]
        svm = SVC(kernel=kernel, degree=degree, coef0=coef0, C = 10)
        for i in range(len(df)):
            X = df.drop(self.list_of_texts[i].title).values
            y_it = y.drop(i)
            test = df.loc[self.list_of_texts[i].title].values.reshape(1, -1)
            svm.fit(X, y_it)
            prediction = svm.predict(test)
            svm.score(X, y_it)
            dict['title'].append(self.list_of_texts[i].title)
            dict['author'].append(self.list_of_texts[i].author)
            dict['prediction'].append(prediction[0])
            dict['tokens'].append(len(self.list_of_texts[i].tokens))
        return pd.DataFrame(dict), svm
    

    def train_clustering(self,n=1000, n_clusters=3, n_init=10, random_state=42):
        dict = {'title':[i.title for i in self.list_of_texts], 
                'author':[i.author for i in self.list_of_texts], 
                'prediction':[], 
                'tokens':[len(i.tokens) for i in self.list_of_texts]}
        df = self.analisis1(n=n)
        kmeans = KMeans(n_clusters=n_clusters, n_init=n_init, random_state=random_state)
        prediction = kmeans.fit_predict(df)
        dict['prediction'] = prediction
        return pd.DataFrame(dict), kmeans
    
    def train_dt(self, n=1000, max_depth=2, random_state=42, picture=False):
        dict = {'title':[], 'author':[], 'prediction':[], 'tokens':[]}
        authors = pd.DataFrame([i.author for i in self.list_of_texts])
        df = self.analisis1(n=n)
        tree_clf = DecisionTreeClassifier(max_depth=max_depth,
                                  random_state=random_state)
        for i in range(len(self.list_of_texts)):
            X = df.drop(self.list_of_texts[i].title).values
            y = authors.drop(i)
            test = df.loc[self.list_of_texts[i].title].values.reshape(1, -1)
            tree_clf.fit(X, y.values.ravel())
            prediction = tree_clf.predict(test)
            dict['title'].append(self.list_of_texts[i].title)
            dict['author'].append(self.list_of_texts[i].author)
            dict['prediction'].append(prediction[0])
            dict['tokens'].append(len(self.list_of_texts[i].tokens))
        if picture:
            texto_modelo = export_text(
                    decision_tree = tree_clf,
                    feature_names = list(df.columns))
            print(texto_modelo)
        return pd.DataFrame(dict), tree_clf
    
    def train_gbc(self, n=1000, max_depth=2, n_estimators=100, learning_rate=1.0, random_state=42):
        dict = {'title':[], 'author':[], 'prediction':[], 'tokens':[]}
        authors = pd.DataFrame([i.author for i in self.list_of_texts])
        df = self.analisis1(n=n)

        gbct = GradientBoostingClassifier(max_depth=max_depth,
                                 n_estimators=n_estimators,
                                 learning_rate=learning_rate,
                                 random_state=random_state)
        
        for i in range(len(self.list_of_texts)):
            X = df.drop(self.list_of_texts[i].title).values
            y = authors.drop(i)
            test = df.loc[self.list_of_texts[i].title].values.reshape(1, -1)
            gbct.fit(X, y.values.ravel())
            prediction = gbct.predict(test)
            dict['title'].append(self.list_of_texts[i].title)
            dict['author'].append(self.list_of_texts[i].author)
            dict['prediction'].append(prediction[0])
            dict['tokens'].append(len(self.list_of_texts[i].tokens))
        return pd.DataFrame(dict), gbct
