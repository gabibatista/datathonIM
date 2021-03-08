import unicodedata, nltk, numpy, re

from sklearn.cluster import MiniBatchKMeans
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt')
nltk.download('stopwords')

def strip(text):
    stopwords = get_stopwords()
    text = unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode('utf-8')
    text = re.sub('[^a-z0-9 ]+', '', str(text).lower())
    text = re.sub(' +', ' ', text)
    text = re.sub('vez', '', text)
    text = nltk.tokenize.word_tokenize(text, language='portuguese')
    return ' '.join([w for w in text if not w in stopwords])

def get_stopwords():
    sw = nltk.corpus.stopwords.words('portuguese')
    sw = list(set(
        [unicodedata.normalize('NFD', w).encode('ascii', 'ignore').decode('utf-8') for w in sw]
    ))
    return sw

def pooler(documents, iters, min_df=5, max_df=0.7, ngram=(1, 2), max_features=1000):
    # documents vectorizer
    vectorizer = TfidfVectorizer(
        min_df=min_df,
        max_df=max_df,
        ngram_range=ngram,
        max_features=max_features
    ).fit(documents)
    
    vectorized = vectorizer.transform(documents)
    
    # pooler model
    sse = []
    models = []
    for k in iters:
        
        model = MiniBatchKMeans(
            n_clusters=k,
            init_size=128,
            batch_size=128,
            random_state=42
        ).fit(vectorized)
        
        models.append(model)
        sse.append(model.inertia_)
        model.predict(vectorized)
        
    return models, sse, vectorizer

def get_model(models, k):
    c = ((k - 2) // 2)
    return models[c]

def sort_best_binds(key, model, vectorized):
    # calculate similarities
    similarities = []
    centroid = model.cluster_centers_[key]
    for v in vectorized:
        similarities.append(cosine_similarity([centroid], v))

    # best binds
    indexes = numpy.array([s[0][0] for s in similarities])
    indexes = numpy.argsort(indexes)[::-1]
    
    return indexes