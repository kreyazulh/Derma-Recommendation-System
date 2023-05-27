import streamlit as st
import pickle
import pandas as pd
from imageFinder import image_look

products_dict = pickle.load(open('product_dict.pkl','rb'))
products = pd.DataFrame(products_dict)
recommender = pickle.load(open('recommend.pkl', 'rb'))


def recommend(product):
    product_index = products[products['value'] == product].index[0]
    product_list = recommender[product_index]

    recommended_prod= []
    company =[]
    image_url = []

    for i in product_list:
        recommended_prod.append(products.iloc[i[0]].names)
        company.append(products.iloc[i[0]].company)
        image_url.append(image_look(products.iloc[i[0]].value))
    return recommended_prod, company, image_url

st.set_page_config(page_title="Derma", page_icon='💆🏻‍♀️', layout="wide", initial_sidebar_state="auto", menu_items=None)
st.title('Derma')

selected_product = st.selectbox(
    'Please type your desired product name',
    products['value'].values)

st.write('We are looking for recommendations based on your product: ')
product_index = products[products['value'] == selected_product].index[0]
st.write(products.iloc[product_index].company + " - " + selected_product)


if st.button('Ask for recommendations'):
    names, company, path = recommend(selected_product)
    col1, col2, col3, col4, col5 = st.columns(5, gap='small')

    with col1:
        st.text(company[0])
        st.text(names[0])
        type(path[0])
        st.image(path[0])

    with col2:
        st.text(company[1])
        st.text(names[1])
        st.image(path[1])

    with col3:
        st.text(company[2])
        st.text(names[2])
        st.image(path[2])

    with col4:
        st.text(company[3])
        st.text(names[3])
        st.image(path[3])

    with col5:
        st.text(company[4])
        st.text(names[4])
        st.image(path[4])




