import pandas as pd
import requests
import http.client
from urllib.request import urlopen
from bs4 import BeautifulSoup

def clean_text(text):
#     text = "".join([word.lower() for word in text if word not in string.punctuation])
#     tokens = re.split('\W+', text)
# #     text = [ps.stem(word) for word in tokens if word not in stopwords]
#     text = [wn.lemmatize(word) for word in tokens if word not in stopwords]
    text = " ".join([word for word in text if word in text])
    return text

url = 'https://www.alexa.com/topsites/category/Top/Science'
text = urlopen(url).read()
soup = BeautifulSoup(text)
data = soup.findAll('div',attrs={'class':'td DescriptionCell'})
list = []
for div in data:
    a = div.text
    mystring = a.replace('\n\n\n', ', ').replace('\r', '')
    result = [mystring.strip() for x in mystring.split(',')]
    list.append(result)
df = pd.DataFrame({'col':list})
df['clean_text'] = df['col'].apply(lambda x: clean_text(x))
# df['clean_text'].str.split(',', expand=True,columns = ['flips','row'])
df = pd.DataFrame(df['clean_text'].str.split(', ').tolist())
s = df.ix[:,0]
# df.iloc[:,0]
# df.to_csv('data_comp_name.csv')
fin_data = pd.DataFrame(s)
# fin_data.head()
fin_data.to_csv('data_comp_name_6.csv')