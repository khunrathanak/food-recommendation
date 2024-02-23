
import streamlit as st 
import sqlite3

# Set Streamlit page configuration
st.set_page_config(page_title="FOODEE.com", layout="centered", page_icon="🍔", initial_sidebar_state="collapsed")


st.markdown(
    """
    <style>
        /*  text color */
        body {
            color: #F0ECE5;
        }
        /* Set background color */
        .stApp {
            background-color: #31304D; /*  background color */
        }
        h1, .css-1vzv12a, .stMarkdown {
            color: #F0ECE5; /* Purple color for title */
        }
        /* Image border */
        img {
            border: 2px solid #F0ECE5; /* border for images */
            border-radius: 5px; /* Rounded border */
            padding: 5px; /* Padding around images */
        }
       
        /* Button style */
        .stButton button {
            background-color: #F99417; /*  button background */
            color: white; /* White button text */
        }
        .stTitle {
            text-align: center; /* Center-align Streamlit title */
            margin-bottom: 0; /* Remove default margin to optimize alignment */
        }
        /* Centering the button */
        .stButton button {
            display: block;
            margin: 0 auto;
        }
        /* Add more CSS styles as needed */
    </style>
    """,
    unsafe_allow_html=True
)




#title of the website
coll1, coll2, coll3 = st.columns(3)
with coll2:
    st.markdown("<h1 style='text-align: center;'>FOODEE</h1>", unsafe_allow_html=True)

# first question
st.write("Please select spicy level of the food:")
spicy_level = st.slider("Spiciness level", 1, 3, 1, label_visibility='collapsed')





st.write("---")
# second question
st.write('Note: 1 means easy, 2 means medium and 3 means difficult')
st.write('Please select difficulty level of the food:')
difficulty = st.slider("difficulty", 1, 3, 1, label_visibility='collapsed')

# make a list that will store user answer 
user_answer = [spicy_level, difficulty]

#database of food and method to find the food

connection = sqlite3.connect("database.db")
connection = sqlite3.connect("recipe_database.db")
cursor = connection.cursor()

cursor.execute("create table if not exists database(spicy_level integer, difficulty integer, name text, link text)")



# Define food list with cuisines, ratings, dishes, and image links
Food_list = [
    ( 3, 3, 'Somlor Korko', 'https://upload.wikimedia.org/wikipedia/commons/a/aa/Somlorkoko.jpg'),
    ( 3, 2, 'Amok', 'https://spicebreeze.com/wp-content/uploads/2018/11/amok.jpg'),
    ( 2, 1, 'Bai Sach Chrouk', 'https://www.thidaskitchen.com/wp-content/uploads/2022/07/Bai-Sach-Chrouk.jpg'),
    ( 3, 1, 'Nom Banh Chok', 'https://www.thidaskitchen.com/wp-content/uploads/2022/12/Nom-Banh-Chok.jpg'),
    ( 3, 2, 'Bai Cha', 'https://d13jio720g7qcs.cloudfront.net/images/guides/origin/654c5918827b9.jpg'),
    ( 3, 1, 'Bok La hong', 'https://www.196flavors.com/wp-content/uploads/2018/08/bok-lahong-3-FP.jpg'),
    ( 3, 3, 'Prahok Kties', 'https://www.thidaskitchen.com/wp-content/uploads/2022/10/prahok-ktiss-served-with-vegetables.jpg'),
    ( 3, 3, 'Lok Lak', 'https://www.simplyrecipes.com/thmb/zb1rbkgxDQT3SfEPZiKncciphp8=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Simply-Recipes-Lok-Lak-Mustard-LEAD-05-a0d8c2c5cd064e9c8c31af93a81b51f0.jpg'),
    ( 3, 3, 'Sach Ko Ang', 'https://i.pinimg.com/736x/78/ff/61/78ff61467c19847e3d6365f1330ea2eb.jpg'),
    ( 3, 2, 'Cha kdav', 'https://www.foodbuzz.site/wp-content/uploads/2019/01/RAK_9827.jpg'),
    ( 3, 1, 'Mee Kola', 'https://grantourismotravels.com/wp-content/uploads/2020/09/Mee-Kola-Recipe-Vegetarian-Noodles-Cambodia-Kola-People-Copyright-2022-Terence-Carter-Grantourismo-T.jpg'),
    ( 3, 1, 'Kung Pao Chicken', 'https://www.kitchensanctuary.com/wp-content/uploads/2019/10/Kung-Pao-Chicken-square-FS-39-new.jpg'),
    ( 3, 2, 'Sweet and Sour Pork', 'https://www.kitchensanctuary.com/wp-content/uploads/2021/01/Sweet-and-Sour-Pork-square-FS.jpg'),
    ( 2, 3, 'Mapo Tofu', 'https://www.cookwithmanali.com/wp-content/uploads/2021/03/Vegan-Mapo-Tofu.jpg'),
    ( 2, 3, 'Chow Mein', 'https://tiffycooks.com/wp-content/uploads/2023/09/188E6766-B4B4-48FB-80F9-9E7EBA5B6278-scaled.jpg'),
    ( 2, 3, 'Peking Duck', 'https://www.foodandwine.com/thmb/da3kQ5oyv9lEU0lyaWlCyBI11Sk=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/peking-duck-FT-RECIPE0821-401d953c2b64446dbd8ddbfdb57a1f68.jpg'),
    ( 2, 3, 'Spring Rolls', 'https://redhousespice.com/wp-content/uploads/2021/12/whole-spring-rolls-and-halved-ones-scaled.jpg'),
    ( 2, 2, 'Hot Pot', 'https://iamafoodblog.b-cdn.net/wp-content/uploads/2020/12/hot-pot-8281w-500x500.jpg'),
    ( 2, 2, 'Baozi', 'https://www.chinasichuanfood.com/wp-content/uploads/2014/01/mapo-tofu-baozi-4.jpg'),
    ( 2, 2, 'Szechuan Beef', 'https://www.theroastedroot.net/wp-content/uploads/2021/02/Szechuan-Beef-recipe-7.jpg'),
    ( 2, 2, 'General Tso Chicken', 'https://www.recipetineats.com/wp-content/uploads/2020/10/General-Tsao-Chicken_1-SQ.jpg'),
    ( 2, 1, 'Scallion Pancakes', 'https://healthynibblesandbits.com/wp-content/uploads/2018/05/Scallion-Pancakes-FF.jpg'),
    ( 2, 1, 'Cantonese Dim Sum', 'https://www.thefoodranger.com/wp-content/uploads/2019/05/best-dim-sum-in-hong-kong-2.jpg'),
    ( 2, 1, 'Wontons', 'https://therecipecritic.com/wp-content/uploads/2023/01/wontons.jpg'),
    ( 1, 1, 'Bulgogi', 'https://hips.hearstapps.com/hmg-prod/images/bulgogi1-1659544883.jpg?crop=0.684xw:1.00xh;0.179xw,0&resize=1200:*'),
    ( 1, 1, 'Bibimbap', 'https://recipetineats.com/wp-content/uploads/2019/05/Bibimbap_3.jpg'),
    ( 1, 1, 'Japchae', 'https://www.recipetineats.com/wp-content/uploads/2023/07/Japchae-Korean-noodles_9.jpg'),
    ( 1, 1, 'Tteokbokki', 'https://fullofplants.com/wp-content/uploads/2023/08/Vegan-Jjajang-Tteokbokki-Non-Spicy-Korean-Dish-thumb.jpg'),
    ( 1, 2, 'Samgyeopsal', 'https://i2.wp.com/seonkyounglongest.com/wp-content/uploads/2019/06/samgyeopsal-7.jpg?fit=1300%2C867&ssl=1'),
    ( 1, 2, 'Galbi', 'https://i2.wp.com/seonkyounglongest.com/wp-content/uploads/2020/08/LA-Galbi-09-mini.jpg?fit=1000%2C667&ssl=1'),
    ( 1, 2, 'Jajangmyeon', 'https://www.spoonforkbacon.com/wp-content/uploads/2021/03/Jajangmyeon-recipe-card.jpg'),
    ( 1, 2, 'Sundubu-jjigae', 'https://i0.wp.com/travelandmunchies.com/wp-content/uploads/2022/11/IMG_3641-scaled.jpg?fit=2560%2C1829&ssl=1'),
    ( 1, 3, 'Haemul Pajeon', 'https://food.fnr.sndimg.com/content/dam/images/food/fullset/2016/12/21/0/FNK_Haemul-Pajeon-2_s4x3.jpg.rend.hgtvcom.616.462.suffix/1482354070138.jpeg'),
    ( 1, 3, 'Kimbap', 'https://www.koreanbapsang.com/wp-content/uploads/2018/09/DSC8399-2-e1696691292303.jpg'),
    ( 1, 3, 'Yangnyeom Chicken', 'https://i.ytimg.com/vi/XnLWBoZn710/maxresdefault.jpg?meta=og:image'),
    ( 1, 3, 'Yukgaejang', 'https://mykoreankitchen.com/wp-content/uploads/2021/02/1.-Yukgaejang.jpg')]

cursor.executemany("insert into database values(?,?,?,?)", Food_list)



 # create two list that will store recommended food and its url
recommend_food = []
recommend_food_url = []

# function to get the food and url
def get_food_name():  
    placeholders = ', '.join(['?' for _ in range (len(user_answer))])
    cursor.execute("SELECT DISTINCT name FROM database WHERE spicy_level=? AND difficulty=?", user_answer)
    result = cursor.fetchall()
    for row in result:
        recommend_food.append(row[0])
        

get_food_name()

def get_food_image_link(): 
    placeholders = ', '.join(['?' for _ in range (len(user_answer))]) 
    cursor.execute("SELECT DISTINCT link FROM database WHERE spicy_level=? AND difficulty=?", user_answer)
    result = cursor.fetchall()
    for row in result:
        recommend_food_url.append(row[0])
        

get_food_image_link()

st.write('---')

cursor.execute("CREATE TABLE IF NOT EXISTS recipe_database (name TEXT, ingredients TEXT, instructions TEXT)")
# Define recipe list with cuisines, ratings, dishes, and image links
recipe_data = [
    ('Somlor Korko', 'pumpkin, pork, lemongrass, galangal, kaffir lime leaves, fish sauce, garlic, shallots, chili', 'https://www.youtube.com/embed/XuQxqP-JnfI'),
    ('Amok', 'fish fillets, coconut cream, lemongrass, galangal, kaffir lime leaves, turmeric, garlic, shallots, palm sugar, fish sauce', 'https://www.youtube.com/embed/mlngdPqXi10'),
    ('Bai Sach Chrouk', 'pork slices, coconut milk, garlic, shallots, palm sugar, fish sauce, black pepper','https://www.youtube.com/embed/sa0inXURh90'),
    ('Nom Banh Chok', 'rice noodles, fish-based curry sauce, bean sprouts, cucumber, water spinach, mint leaves, green beans, banana blossom','https://www.youtube.com/embed/regiflNIs-0'),
    ('Bai Cha', 'beef, lemongrass, kaffir lime leaves, galangal, garlic, shallots, palm sugar, fish sauce, black pepper','https://www.youtube.com/embed/zZNhVv7fmSE'),
    ('Bok La hong', 'green papaya, fish sauce, lime juice, garlic, birds eye chili, palm sugar, cherry tomatoes, green beans','https://www.youtube.com/watch?v=wtiwBydlrps'),
    ('Prahok Kties', 'prahok, pork belly, coconut milk, lemongrass, kaffir lime leaves, galangal, garlic, shallots, palm sugar, fish sauce','https://www.youtube.com/embed/-ZspDSPTrrw '),
    ('Mee Kola', 'rice noodles, pork slices, coconut milk, lemongrass, kaffir lime leaves, galangal, garlic, shallots, palm sugar, fish sauce', ' https://www.youtube.com/watch?v=eVIgHF9qG78'),
    ('Lok Lak', 'beef, lime juice, fish sauce, oyster sauce, garlic, shallots, sugar, black pepper, lettuce, tomatoes',' https://www.youtube.com/watch?v=9tB9AmYY4Tw '),
    ('Sach Ko Ang', 'beef slices, lemongrass, garlic, shallots, palm sugar, fish sauce, black pepper','https://www.youtube.com/watch?v=r50xpPUZe_A'),
    ('Cha kdav', 'chicken, lemongrass, kaffir lime leaves, galangal, garlic, shallots, palm sugar, fish sauce, black pepper',' https://www.youtube.com/watch?v=cj3H6cXFoN8 '),
    
    ('Kung Pao Chicken', 'chicken, peanuts, bell peppers, dried red chilies, garlic, ginger, soy sauce, rice vinegar, sugar',' https://www.youtube.com/watch?v=YT8oN4U7Vm8'),
    ('Sweet and Sour Pork', 'pork, pineapple, bell peppers, onion, ketchup, vinegar, sugar, soy sauce, cornstarch',' https://www.youtube.com/watch?v=_4fFSKXIsBs'),
    ('Mapo Tofu', 'tofu, ground pork, doubanjiang (spicy bean paste), fermented black beans, garlic, ginger, green onions, soy sauce, chicken broth, cornstarch',' https://www.youtube.com/watch?v=3XSXygYEJos'),
    ('Chow Mein', 'egg noodles, chicken, shrimp, carrots, celery, napa cabbage, bean sprouts, soy sauce, oyster sauce, sesame oil','https://www.youtube.com/watch?v=AiIwtzGcUM0'),
    ('Peking Duck', 'whole duck, hoisin sauce, soy sauce, rice vinegar, ginger, garlic, honey, green onions, pancakes',' https://www.youtube.com/watch?v=eyjSPg3Bzz0 '),
    ('Spring Rolls', 'spring roll wrappers, shrimp, pork, vermicelli noodles, carrots, cabbage, garlic, soy sauce, sesame oil',' https://www.youtube.com/watch?v=Eeuo9iWH9DU '),
    ('Hot Pot', 'sliced meat (beef, lamb, or pork), assorted vegetables, tofu, mushrooms, noodles, hot pot broth, dipping sauces',' https://www.youtube.com/watch?v=WLAY-LIOKYI '),
    ('Baozi', 'flour, yeast, pork, cabbage, ginger, garlic, soy sauce, sesame oil','https://m.youtube.com/watch?v=lGr3H7XVmng'),
    ('Szechuan Beef', 'beef, cornstarch, soy sauce, hoisin sauce, rice vinegar, sugar, garlic, ginger, dried red chilies','https://www.youtube.com/watch?v=YHEyXNx3vMQ'),
    ('General Tso Chicken', 'chicken, cornstarch, egg, soy sauce, rice vinegar, sugar, garlic, ginger, dried red chilies','https://www.youtube.com/watch?v=mJ8RMyPOZRQ'),
    ('Scallion Pancakes', 'flour, scallions, water, sesame oil, salt',' https://www.youtube.com/watch?v=CCl4vgq1zYU'),
    ('Cantonese Dim Sum', 'shrimp, pork, wonton wrappers, soy sauce, sesame oil, garlic, green onions',' https://www.youtube.com/watch?v=cjnMxtknxG4'),
    ('Wontons', 'ground pork, shrimp, wonton wrappers, soy sauce, sesame oil, garlic, ginger, green onions',' https://www.youtube.com/watch?v=F-h1NaCUivA'),
    
    ('Bulgogi', 'beef, soy sauce, sesame oil, garlic, ginger, brown sugar, pear juice',' https://www.youtube.com/watch?v=_BhDaFe_ZQ0'),
    ('Bibimbap', 'cooked rice, beef, vegetables (spinach, carrots, bean sprouts, mushrooms), eggs, gochujang (red chili paste), sesame oil',' https://www.youtube.com/watch?v=6QQ67F8y2b8'),
    ('Japchae', 'sweet potato noodles, beef, spinach, carrots, onion, garlic, soy sauce, sesame oil, sugar',' https://www.youtube.com/watch?v=i1djfV9uigc'),
    ('Tteokbokki', 'rice cakes, fish cakes, gochujang (red chili paste), soy sauce, sugar, garlic, green onions','https://www.youtube.com/watch?v=UxpWM7ISoUM'),
    ('Samgyeopsal', 'pork belly, lettuce leaves, garlic, green onions, ssamjang (soybean paste), kimchi','https://www.youtube.com/embed/2D6HZ9Bdjvs'),
    ('Galbi', 'beef short ribs, soy sauce, pear juice, garlic, sesame oil, brown sugar','https://www.youtube.com/watch?v=vtGzj6cUn7Q'),
    ('Jajangmyeon', 'black bean paste, pork, onions, potatoes, zucchini, cucumber, sugar, starch noodles','https://www.youtube.com/watch?v=F4Cm75Qvk4A'),
    ('Sundubu-jjigae', 'soft tofu, clams or seafood, mushrooms, zucchini, onions, garlic, gochugaru (red pepper flakes), soy sauce','https://www.youtube.com/watch?v=BvZ9m3Bikuw'),
    ('Haemul Pajeon', 'flour, seafood (shrimp, squid, or mussels), green onions, eggs, garlic, soy sauce','https://www.youtube.com/embed/bnYr77vOyM0'),
    ('Kimbap', 'sushi rice, seaweed sheets, carrots, spinach, eggs, pickled radish, imitation crab, ham','https://www.youtube.com/watch?v=sC-gDNA8YJ8'),
    ('Yangnyeom Chicken', 'chicken wings, cornstarch, flour, oil for frying, soy sauce, gochujang (red chili paste), garlic, ginger, rice syrup or honey','https://www.youtube.com/embed/XnLWBoZn710'),
    ('Yukgaejang', 'beef brisket or flank, soy sauce, gochugaru (red pepper flakes), garlic, green onions, bean sprouts, fernbrake (gosari), eggs','https://www.youtube.com/embed/FxSmBbXSDl0')
]




cursor.executemany("INSERT INTO recipe_database VALUES (?, ?, ?)", recipe_data)

# get the dish ingredients and instruction url coressponding to recommend_food


class GetIngriInstruct:
    def __init__(self, recommend_food):
        self.recommend_food = recommend_food

    def get_food_ingredients(self):
        placeholders = ', '.join(['?' for _ in range(len(self.recommend_food))])
        query = f"SELECT DISTINCT ingredients FROM recipe_database WHERE name IN ({placeholders})"
        cursor.execute(query, self.recommend_food)
        result = cursor.fetchall()
        # food_ingredients = [row[0] for row in result]
        food_ingredients = []
        for row in result:
            food_ingredients.append(row)
        return food_ingredients

    def get_instruction_links(self):
        placeholders = ', '.join(['?' for _ in range(len(self.recommend_food))])
        query = f"SELECT DISTINCT instructions FROM recipe_database WHERE name IN ({placeholders})"
        cursor.execute(query, self.recommend_food)
        result = cursor.fetchall()
        instruction_links = [row[0] for row in result]  # Extracting the first element from each tuple
        return instruction_links

get_ingri_instruction = GetIngriInstruct(recommend_food)

food_ingredients = get_ingri_instruction.get_food_ingredients()
instruction_links = get_ingri_instruction.get_instruction_links()


#  code for recommendation
first_food_image = recommend_food_url[0]
second_food_image = recommend_food_url[1]
third_food_image = recommend_food_url[2]
fourth_food_image = recommend_food_url[3]
# link for instruction video

first_food_instruction = instruction_links[0]
second_food_instruction = instruction_links[1]
third_food_instruction = instruction_links[2]
fourth_food_instruction = instruction_links[3]


## to do make a clickable button or images instead of this one above

def clickable_image(food_image, instruction_url):
    image = f'<a href="{instruction_url}" target="_blank"><img src="{food_image}" width="150" height="150" style="object-fit: cover;"></a>'
    st.markdown(image, unsafe_allow_html=True)
if st.button("Recommend me"):
   st.write("Click on the food image to see the instruction videos")
   st.write('---')
   col1, col2, col3, col4 = st.columns(4)
   with col1:
    first_food = clickable_image(first_food_image,first_food_instruction )
    st.write( recommend_food[0])
    st.write('---')
    st.write('ingredients:')
    st.markdown('\n'.join(['- ' + ingredient for ingredient in food_ingredients[0]]))
   with col2:
    second_food = clickable_image(second_food_image,second_food_instruction )
    st.write(recommend_food[1])
    st.write('---')
    st.write('ingredients:')
    st.markdown('\n'.join(['- ' + ingredient for ingredient in food_ingredients[1]]))
   with col3:
    third_food = clickable_image(third_food_image,third_food_instruction )
    st.write(recommend_food[2])
    st.write('---')
    st.write('ingredients:')
    st.markdown('\n'.join(['- ' + ingredient for ingredient in food_ingredients[2]]))
   with col4:
    fourth_food = clickable_image(fourth_food_image,fourth_food_instruction)
    st.write( recommend_food[3])
    st.write('---')
    st.write('ingredients:')
    st.markdown('\n'.join(['- ' + ingredient for ingredient in food_ingredients[3]]))
    


connection.commit()
connection.close()
