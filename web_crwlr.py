
# coding: utf-8

# In[10]:


from bs4 import BeautifulSoup


# In[11]:


import urllib
import requests


# In[12]:


ostr = "Bandra west"
str = ostr.replace(' ','+')
str = "+"+str
print( str)
x= "https://www.google.co.in/search?biw=1366&bih=662&ei=o6JuW_7AGJmurQGNwqmwAg&q=top+rated+places+near"+str+"&oq=top+rated+places+near"+str+"&gs_l=psy-ab.3..35i39k1.22898.26899.0.27124.22.16.0.0.0.0.224.2080.0j9j3.12.0....0...1c.1.64.psy-ab..11.11.1857...0j0i22i30k1.0.Wz_2DZI3RUA"
print(x)


# In[13]:


url = (x)
r = requests.get(url)
#r.content


# In[14]:


soup = BeautifulSoup(r.content)
print (soup.prettify())


# In[15]:


'''for link in soup.find_all("a"):
    print(link.text,link.get("href"))'''
    #print("<a href='%s'>%s</a>"%(link.get("href"), link.text))


# In[16]:


gdata = soup.find_all("div",{"class": "kR1eme gsrt rllt__wrap-on-expand"})
gdata


# In[17]:


for item in gdata:
      print(item.text)


# In[18]:


for i in soup.select('.BTtC6e'):
    print(i.text)

