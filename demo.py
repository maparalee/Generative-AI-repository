#!/usr/bin/env python
# coding: utf-8

# ### Installation of streamlit

# In[9]:


# # !pip install streamlit
# !pip show streamlit


# ### Title

# In[10]:


import streamlit as st


# In[11]:


st.title('Machine-learning')


# ### Headerf

# In[12]:


st.header('Data science')


# ### Subheader

# In[13]:


st.subheader('This is a subheader')


# ### Text

# In[14]:


st.text('lets change the life of the students')


# ### Slider
# 

# In[15]:


age = st.slider("Select your age", 0, 100, 25)
st.write(f"Your age: {age}")


# ### Button
# 

# In[17]:


if st.button("Click me"):
    st.write("Button clicked!")


# ### selectobx

# In[16]:


option = st.selectbox("Choose a number", [1, 2, 3, 4, 5])
st.write(f"You selected: {option}")


# In[ ]:




