
# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col 

# Write directly to the app
session = get_active_session()
st.title(f"Customize Your Smoothie!")
st.write(
  """Replace this example with your own code!
  Custom smoothie!
  """
)






name = st.text_input('Name on smoothie')


my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
# st.dataframe(data = my_dataframe, use_container_width = True)

ingredients_list = st.multiselect(
    'Choose up to 5 ingredients:', 
    my_dataframe,
    max_selections = 5
)

if ingredients_list:

    ingredients_string = ''
    for fruit_chosen in ingredients_list: 
        ingredients_string += fruit_chosen + ' '


    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
                    values ('""" + ingredients_string + """', '""" + name + """')"""

    # st.write(my_insert_stmt)
    time_to_insert = st.button('Submit Order')

    

    if time_to_insert: 
        session.sql(my_insert_stmt).collect()

        st.success('Your Smoothies is ordered!')



















    
