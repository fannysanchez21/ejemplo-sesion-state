
import streamlit as st
st.title("Ejemplo para usar sesion_state")

if 'count' not in st.session_state:
   st.session_state['count'] = 0

if 'name' not in st.session_state:
   st.session_state['name'] = ''
   
if st.button('Click me'):
   st.session_state['count'] += 1

if st.button('Escribe tu nombre'):
   st.session_state['name'] = '' 
   
st.write(st.session_state)
