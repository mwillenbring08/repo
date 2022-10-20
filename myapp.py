import streamlit as st
import pandas as pd
from datetime import date
import openpyxl
import random

today = date.today()
born = date(2022,10,19)
diff = born - today


st.set_page_config(page_icon='🎂',  layout="centered", initial_sidebar_state="auto", menu_items=None)
#st.markdown("<h1 style='text-align: center; color: black;'>EMILY'S WEBSITE OF FUN!</h1>", unsafe_allow_html=True)
#st.set_page_config(page_title = 'Happy Birthday Emily Christine Herman!', page_icon='🎂',  layout="centered", initial_sidebar_state="auto", menu_items=None)
st.title('Emily\'s Website of Fun')
st.image('IMG_2330.JPG')


tab1, tab3, quiz, tab4, tab2, tab5= st.tabs(["Welcome", "FOOOD",  "Emily Quiz", "Next Birthday", "Memory Lane", "A Message from our Sponser"])

with tab1:
    st.balloons()
   #st.header("Welcome!")
    col1, col2= st.columns(2)
    
    with col2:
        st.write("Welcome to my website. This is a place where you can get to know a little bit more about who this Emily Herman girl is. I am gonna tell you all kinds of things about what makes her great, the things she loves to do, and the amazing people in her life. Thanks for stoping by!")
    with col1:
        st.image("Screen Shot 2022-10-05 at 8.28.15 AM.png")

with tab3:
   st.header("Hungry Time")
   st.subheader("If you are anything like Emily, or Matthew, you are always hungry! Sometimes it is hard to know where to eat though! \nHere is a list of some of Emily and Matthew\'s favorite places to eat. Hope this helps out on the \'idk what I want but not that\' times")
   df = pd.read_excel('Restaurants.xlsx')
   genre = st.multiselect('Cuisine',options = ['American','Asian','Breakfast','Tacos','Mexican','Italian', 'Pizza', 'Misc'], default = ['American','Asian','Breakfast','Tacos','Mexican','Italian', 'Pizza', 'Misc'])
   area = st.multiselect('Location',options = ['North','Central','Downtown','South','East','West'], default = ['North','Central','Downtown','South','East','West'])
   price_low, price_high = st.select_slider('Price',options = ['$','$$','$$$','$$$$'], value = ('$','$$$$'))
   deck = ['$','$$','$$$','$$$$']

   if price_low == '$' and price_high == '$$':
        deck = ['$','$$']
   if price_low == '$' and price_high == '$$$':
        deck = ['$','$$','$$$']
   if price_low == '$' and price_high == '$$$$':
        deck = ['$','$$','$$$','$$$$']
   if price_low == '$$' and price_high == '$$$':
        deck = ['$$','$$$']
   if price_low == '$$' and price_high == '$$$$':
        deck = ['$$','$$$','$$$$']
   if price_low == '$$$' and price_high == '$$$$':
        deck = ['$$$','$$$$']
    
   filter = df[df['Genre'].isin(genre)] 
   filter = filter[filter['Location'].isin(area)]
   filter = filter[filter['Price'].isin(deck)]

   if st.button('Choose Where I should eat!'):
        try:
            st.write(filter.sample())
        except:
            st.write('Couldn\'t find a reastaurant in that criteria, try adjusting those filters!!')
        
   if st.button('Show me all my options!'):
        try:
            st.write(filter)
        except:
            st.write('Couldn\'t find a reastaurant in that criteria, try adjusting those filters!!')
    

with quiz:
    st.header("Put your knowledge of Emily to the test! Are you a fake friend???")
    st.empty()
    grade = 'nan'
    with st.form('quiz'):
        movie = st.radio('What is my favorite genre of TV/Movies?',('Reality TV','Rom Com','True Crime','Horror','Fantasy'))
        twin = st.radio("Am I the older or younger twin?",('Older','Younger','We were birthed at the exact same time'))
        travel = st.radio("If I could travel anywhere in the world, where would I go?", ('Spain','Houston','Australia','Maldives','Dubai'))
        matthew = st.radio("Where did I meet Matthew?", ("Target", "Downtown", "Boat","Church","Class"))
        bowl = st.radio("What is my favorite bowl place?",('Cabo Bob\'s','Honest Mary\'s', 'Cava','Chipotle'))
        cal = st.radio("What is my favorite calender?",('Paper','Google','Outlook','Apple'))
        
        st.form_submit_button('Check my answers!')
        key = ['Rom Com','Younger','Maldives','Church','Honest Mary\'s','Google']
        ans = [movie,twin,travel,matthew,bowl,cal]
        total = 0
        for i in range(len(ans)):
            if key[i] == ans[i]:
                total = total + 1

        grade = (total/6)*100
        st.write('Your Score: ' + str(grade) + '%')

        if int(grade) == 100:
            st.write("WOW. YOU ARE SO COOL, You know Emily better than she knows herself!!")
            st.image("https://media.giphy.com/media/h2P01cZLZzMK4/giphy.gif")

        if int(grade) > 65 and int(grade) < 100:
            st.write("Might wanna schedule a hangout soon! Need to know her a bit more!!")
            st.image("https://media.giphy.com/media/NRXleEopnqL3a/giphy.gif")

        if int(grade) <= 65 and int(grade) > 0:
            st.write('Yikes....Thats a tuffff look!')
            st.image("https://media.giphy.com/media/l46CyJmS9KUbokzsI/giphy.gif")
        

with tab4:
   st.header("Days till Emily's Next Birthday:")
   yes = st.button("Calculate")
   if yes:
    if diff.days < 0:
         st.header(365 + diff.days)
    else:
         st.header(diff.days)
    st.image("https://media.giphy.com/media/26BRL7YrutHKsVtJK/giphy.gif", width=800)
    st.balloons()
    st.snow()


with tab2:
   st.header("Some of my Favorite Pictures, People and Things to do!")
   go = st.button('Show me something')
   pictures = ['Car.JPG','Swim.jpeg','3bf.JPG','pool.JPG','matteo.JPEG','bday.PNG','truck.JPG','boat.JPG','mask.JPG','tbird.JPG','barge.jpeg','len.jpeg','neil.jpeg','3b.jpg','young.jpg','cousin.JPEG','pink.JPEG','golf.JPEG']
   comment = ['A bunch of mechanics:)','Big boi matthew swimming','THE 3 BEST FRIENDS','Hangin out by the pool','Matthew with baby hehe','Music out for matt bday','Roadtripping','Enjoying our time with Kevin','nightmare fuel','In the bird','THE 3 bestest of friends','the beginning hanging at the pool, so awk','papa neil so cute','The 3 bestest of ever friendies','baby matthew','the fam','bloop','where it all began']
   #co,col = st.columns(2)
   if go:
        num = random.randint(0,len(pictures)-1)
        #with co:
        st.image(pictures[num])
        #with col:
        st.write(comment[num])
    
with tab5:
    st.header("A True Thank You")
    password = st.text_input('Password:')
    
    if password == 'beloved':
        st.video('final.mp4')
