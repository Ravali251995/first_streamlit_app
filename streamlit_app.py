import streamlit
streamlit.title("My parents New Healthy Diner")
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)

# Display the table on the page.
# lets put a quick pick list here so they can pick the fruits they want to include;
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


import requests

fruit_choice = streamlit.text_input('What fruit would you like information about?')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)
streamlit.header("Fruityvice Fruit Advice!")
#streamlit.text(fruityvice_response.json())

# normalizing the output to convert to a table
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# print the normalized output
streamlit.dataframe(fruityvice_normalized)
#dont run anything post this command while we troubleshoot
streamlit.stop()
import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from pc_rivery_db.public.fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_rows)
fruit_added = streamlit.text_input('What fruit would you like to add?')
streamlit.write('Thanks for adding ', fruit_added)
my_cur.execute("insert into fruit_load_list values('from streamlit')")
