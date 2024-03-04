#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Firstly, we are importing all the libraries and tools we need
import pandas as pd


# In[2]:


import numpy as np


# In[3]:


import re, string


# In[4]:


import nltk


# In[5]:


from nltk.tokenize import word_tokenize


# In[6]:


from nltk.corpus import stopwords


# In[7]:


from nltk.stem import SnowballStemmer


# In[8]:


from nltk.corpus import wordnet


# In[9]:


from nltk.stem import WordNetLemmatizer


# In[10]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
from sklearn.metrics import roc_curve, auc, roc_auc_score


# In[11]:


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer


# In[12]:


import gensim
from gensim.models import Word2Vec


# In[13]:


import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams


# In[14]:


# Loading the dataset with 100 texts for training
df_train = pd.read_csv('~/Desktop/dataset100.csv', index_col=None, header=0, engine='python' )


# In[15]:


df_train.info()


# In[16]:


# Combining headlines with texts for each news article
df_train['text'] = df_train['title'] + df_train['text']


# In[17]:


df_train


# In[18]:


# There is a neater preprocessing variant than in WEKA
def preprocess(text):
    text = text.lower() 
    text=text.strip()  
    text=re.compile('<.*?>').sub('', text) 
    text = re.compile('[%s]' % re.escape(string.punctuation)).sub(' ', text)  
    text = re.sub('\s+', ' ', text)  
    text = re.sub(r'\[[0-9]*\]',' ',text) 
    text=re.sub(r'[^\w\s]', '', str(text).lower().strip())
    text = re.sub(r'\d',' ',text) 
    text = re.sub(r'\s+',' ',text) 
    return text


# In[19]:


# This function removes articles, prepositions, etc., 
# while they are still present in WEKA
def stopword(string):
    a= [i for i in string.split() if i not in stopwords.words('english')]
    return ' '.join(a)


# In[20]:


# There is a helper function to add NTLK positions tags
wl = WordNetLemmatizer()

def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN


# In[21]:


def lemmatizer(string):
    word_pos_tags = nltk.pos_tag(word_tokenize(string)) # Get position tags
    a=[wl.lemmatize(tag[0], get_wordnet_pos(tag[1])) for idx, tag in enumerate(word_pos_tags)] # Map the position tag and lemmatize the word/token
    return " ".join(a)


# In[22]:


def finalpreprocess(string):
    return lemmatizer(stopword(preprocess(string)))
df_train['clean_text'] = df_train['text'].apply(lambda x: finalpreprocess(x))
df_train.head()


# In[23]:


# min_count=1 - word should be present at least once across all documents
df_train['clean_text_tok']=[nltk.word_tokenize(i) for i in df_train['clean_text']]
model = Word2Vec(df_train['clean_text_tok'],min_count=1)   
dict(zip(model.wv.index_to_key, model.wv.vectors))

w2v = dict(zip(model.wv.index_to_key, model.wv.vectors))

class MeanEmbeddingVectorizer(object):
    def __init__(self, word2vec):
        self.word2vec = word2vec
        self.dim = len(next(iter(word2vec.values())))

    def fit(self, X, y):
        return self

    def transform(self, X):
        return np.array([
            np.mean([self.word2vec[w] for w in words if w in self.word2vec]
                    or [np.zeros(self.dim)], axis=0)
            for words in X
        ])


# In[24]:


# Splitting the training dataset into train and test 80/20 proportion
X_train, X_val, y_train, y_val = train_test_split(df_train['clean_text'],
                                                  df_train['label'],
                                                  test_size=0.2,
                                                  shuffle=True)
# Running 'Word to Vector function' on tokenized sentences
X_train_tok = [nltk.word_tokenize(i) for i in X_train]  
X_val_tok = [nltk.word_tokenize(i) for i in X_val] 


# In[25]:


# Vectorisation using Bag-of-Words + TF-IDF + Word2Vec
tfidf_vectorizer = TfidfVectorizer(use_idf=True)
X_train_vectors_tfidf = tfidf_vectorizer.fit_transform(X_train) 
X_val_vectors_tfidf = tfidf_vectorizer.transform(X_val)


# In[26]:


modelw = MeanEmbeddingVectorizer(w2v)
X_train_vectors_w2v = modelw.transform(X_train_tok)
X_val_vectors_w2v = modelw.transform(X_val_tok)


# In[27]:


#Building Model 1 with Logistic Regression + TF-IDF

lr_tfidf=LogisticRegression(solver = 'liblinear', C=10, penalty = 'l2')
lr_tfidf.fit(X_train_vectors_tfidf, y_train) 

y_predict = lr_tfidf.predict(X_val_vectors_tfidf)
y_prob = lr_tfidf.predict_proba(X_val_vectors_tfidf)[:,1]

print(classification_report(y_val,y_predict))
print('Confusion Matrix:',confusion_matrix(y_val, y_predict))
 
fpr, tpr, thresholds = roc_curve(y_val, y_prob)
roc_auc = auc(fpr, tpr)
print('AUC:', roc_auc)  


# In[28]:


#Building Model 2 with Naive Bayes + TF-IDF

nb_tfidf = MultinomialNB()
nb_tfidf.fit(X_train_vectors_tfidf, y_train)

y_predict = nb_tfidf.predict(X_val_vectors_tfidf)
y_prob = nb_tfidf.predict_proba(X_val_vectors_tfidf)[:,1]
 
print(classification_report(y_val,y_predict))
print('Confusion Matrix:',confusion_matrix(y_val, y_predict))
 
fpr, tpr, thresholds = roc_curve(y_val, y_prob)
roc_auc = auc(fpr, tpr)
print('AUC:', roc_auc) 


# In[29]:


#Building Model 3 With Logistic Regression + WordToVector

lr_w2v=LogisticRegression(solver = 'liblinear', C=10, penalty = 'l2')
lr_w2v.fit(X_train_vectors_w2v, y_train)  #model

#Predict y value for test dataset
y_predict = lr_w2v.predict(X_val_vectors_w2v)
y_prob = lr_w2v.predict_proba(X_val_vectors_w2v)[:,1]

print(classification_report(y_val,y_predict))
print('Confusion Matrix:',confusion_matrix(y_val, y_predict))
 
fpr, tpr, thresholds = roc_curve(y_val, y_prob)
roc_auc = auc(fpr, tpr)
print('AUC:', roc_auc) 


# In[30]:


df_test = pd.read_csv('~/Desktop/test.csv', engine='python')


# In[31]:


df_test.info()


# In[32]:


#Testing with the Model 1 (LR)
df_test['clean_text'] = df_test['text'].apply(lambda x: finalpreprocess(x)) #preprocess the data
X_test=df_test['clean_text'] 
X_vector=tfidf_vectorizer.transform(X_test) #converting X_test to vector
y_predict = lr_tfidf.predict(X_vector)      #use the trained model on X_vector
y_prob = lr_tfidf.predict_proba(X_vector)[:,1]
df_test['predict_prob_LR']= y_prob
df_test['label LR']= y_predict
print(df_test.head())
final=df_test[['label check','label LR']].reset_index(drop=True)
final.to_csv('submission.csv')


# In[33]:


df_test['label LR']


# In[34]:


df_test['predict_prob_LR']


# In[35]:


#Testing with Model 2 (NB)
df_test['clean_text'] = df_test['text'].apply(lambda x: finalpreprocess(x)) #preprocess the data
X_test=df_test['clean_text'] 
X_vector=tfidf_vectorizer.transform(X_test)


# In[36]:


df_test.info()


# In[37]:


nb_tfidf = MultinomialNB()
nb_tfidf.fit(X_train_vectors_tfidf, y_train)  
#Predict y value for test dataset
y_predict = nb_tfidf.predict(X_vector)
y_prob = nb_tfidf.predict_proba(X_vector)[:,1]
df_test['predict_prob_NB']= y_prob
df_test['label NB']= y_predict
print(df_test.head())


# In[38]:


df_test['label NB']


# In[39]:


df_test['predict_prob_NB']

