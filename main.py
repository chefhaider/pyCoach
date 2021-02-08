#!/usr/bin/env python
# coding: utf-8

# In[15]:


try:
    from requests import get
    from bs4 import BeautifulSoup
    from googlesearch import search 
except:
    print('Error: Try installing prerequisite libraries for this package first')

    
import sys
import traceback
import IPython



def displaySol(query1,query2):


    query2 = query2.split('\n')[1]
    
    query1 += query1 + ' stackoverflow'
    query2 += query2 + ' stackoverflow'
    
    
    links = [val for val in search(query1, tld="com", num=4, stop=4, pause=0)]
    
    res = get(links[0])
    data = BeautifulSoup(res.text)
    print('Similar Problem:\n')
    print( data.find('div', class_='s-prose js-post-body').text.strip(),'\n\n\n')
    i=1
    for val in data.find_all('div',{'class' :'answer'}):
        print('Solution',i)
        print( val.find('div', class_='s-prose js-post-body').text.strip(),'\n')
        i+=1

    print("Didn't find your Soultion? Try out these links")
    for val in links[1:]:
        print(val)
    
    for val in search(query2, tld="com", num=2, stop=2, pause=0):
        print(val)
        
        
        
def showtraceback(self,running_compiled_code = True):
    traceback_lines = traceback.format_exception(*sys.exc_info())
    del traceback_lines[1]
    message = ''.join(traceback_lines)
    
    print(message)
    print('Fetching Solution...','\n')
    displaySol(traceback_lines[2],traceback_lines[1])



def activate_solution():
    IPython.core.interactiveshell.InteractiveShell.showtraceback = showtraceback

if __name__ == "__main__":
    activate_solution()

