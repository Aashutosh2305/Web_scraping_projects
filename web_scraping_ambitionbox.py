#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import requests 
from bs4 import BeautifulSoup


# In[17]:


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

webpage = requests.get("https://www.ambitionbox.com/list-of-companies?campaign=desktop_nav&page=1", headers=headers).text



# In[18]:


soup = BeautifulSoup(webpage, "lxml")


# In[20]:


print(soup.prettify)


# In[21]:


company_info = soup.find_all("div", class_ = "companyCardWrapper__primaryInformation")


# In[23]:


company_sinfo = soup.find_all("div", class_ = "companyCardWrapper__tertiaryInformation")


# In[66]:


names = []
rating = []
review = []
about = []


# In[67]:


for info in company_info:
    names.append(info.find("h2", class_ = "companyCardWrapper__companyName").text.strip())
    rating.append(info.find("span", class_ = "companyCardWrapper__companyRatingValue").text.strip())
    


# In[68]:


for info in company_sinfo:
    review.append(info.find("span", class_ = "companyCardWrapper__ActionCount").text.strip())


# In[69]:


company_ainfo = soup.find_all("div", class_ = "companyCardWrapper__secondaryInformation")


# In[70]:


for info in company_ainfo:
    about.append(info.find("span", class_ = "companyCardWrapper__interLinking").text.strip())
    


# In[71]:


about


# In[72]:


d = {"names": names, "rating": rating, "review": review, "about":about }
df = pd.DataFrame(d)
df


# In[73]:


df.shape


# In[ ]:


final = pd.DataFrame()


for j in range(0,501):
    
    url = "https://www.ambitionbox.com/list-of-companies?campaign=desktop_nav&page={}".format(j)
    headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }

    webpage = requests.get(url, headers=headers).text
    soup = BeautifulSoup(webpage, "lxml")
    
    company_info = soup.find_all("div", class_ = "companyCardWrapper__primaryInformation")
    company_sinfo = soup.find_all("div", class_ = "companyCardWrapper__tertiaryInformation")
    company_ainfo = soup.find_all("div", class_ = "companyCardWrapper__secondaryInformation")
    names = []
    rating = []
    review = []
    about = []
    
    for info in company_info:
        names.append(info.find("h2", class_ = "companyCardWrapper__companyName").text.strip())
        rating.append(info.find("span", class_ = "companyCardWrapper__companyRatingValue").text.strip())
        
        
    for info in company_sinfo:
        review.append(info.find("span", class_ = "companyCardWrapper__ActionCount").text.strip())
        
        
    for info in company_ainfo:
        about.append(info.find("span", class_ = "companyCardWrapper__interLinking").text.strip())
        
    
    d = {"names": names, "rating": rating, "review": review, "about":about }
    df = pd.DataFrame(d)
    
    final = pd.concat([final, df], ignore_index=True)

    
    
        
    


    
    


    


# In[78]:


final


# In[ ]:




