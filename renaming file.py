#!/usr/bin/env python
# coding: utf-8

# In[1]:


# In this project, you are to build a python script to rename files in the dogs folder (part of this repository) to ‘dogs’ plus a number such that filenames will appear as follows: dog01, dog02, dog03, …, dog15. Note that you should use the os module to implement this bulk file renamer. Find the documentation here.

# On completion, you can now use this script to rename some of those numerous files on your desktop that you have been struggling to rename in bulk.


# In[2]:


import os


# In[3]:


# os.rename(src, dst)
# src: Source is the name of the file or directory. It should must already exist.

# dst: Destination is the new name of the file or directory you want to change.


# In[4]:


def renaming_files(directory, newname):
    files =os.listdir(directory)
    counter=0
    for file in files:
        filetype= file.split(".")[-1]
        os.rename(directory+ "/" +file, directory+ "/"+ newname+ str(counter)+ "."+ filetype)
        print("Renaming " +file + " to "+ newname+ str(counter)+ "."+ filetype)
        counter+=1


# In[5]:


renaming_files(r"C:\Users\HP\Desktop\Renaming Python", "success0")


# ### Endswith

# In[21]:


def renaming_files(directory, ending, newname):
    files =os.listdir(directory)
    counter=0
    for file in files:
        if file.endswith(ending):
            filetype= file.split(".")[-1]
            os.rename(directory+ "/" +file, directory+ "/"+ newname+ str(counter)+ "."+ filetype)
            print("Renaming " +file + " to "+ newname+ str(counter)+ "."+ filetype)
            counter+=1


# In[22]:


renaming_files(r"C:\Users\HP\Desktop\Renaming Python","docx" ,"datascience")


# In[ ]:





# In[20]:


get_ipython().system('git init')
get_ipython().system('git add renaming file.ipynb')
get_ipython().system('git commit -m "Renaming Files in your computer"')
get_ipython().system('git branch -M main')
get_ipython().system('git remote add origin https://github.com/Mugambi99/Renaming-files-.git')
get_ipython().system('git push -u origin main')


# In[ ]:




