import streamlit as st
from datetime import date

today = date.today()
born = date(2023,10,19)
diff = born - today


st.set_page_config(page_title = 'Happy Birthday Emily!', page_icon='🎂',  layout="centered", initial_sidebar_state="auto", menu_items=None)
st.markdown("<h1 style='text-align: center; color: black;'>EMILY'S WEBSITE OF FUN!</h1>", unsafe_allow_html=True)
#st.set_page_config(page_title = 'Happy Birthday Emily Christine Herman!', page_icon='🎂',  layout="centered", initial_sidebar_state="auto", menu_items=None)
st.title('Emily\'s Website of Fun')
st.image('IMG_2330.JPG')


tab1, tab2, tab3, quiz, tab4, tab5= st.tabs(["Welcome", "Why I am Awesome", "My Favorite Things to Do",  "Emily Quiz", "Next Birthday", "A Message from our Sponser"])

with tab1:
    st.balloons()
   #st.header("Welcome!")
    col1, col2= st.columns(2)
    
    with col2:
        st.write("Welcome to my website. This is a place where you can get to know a little bit more about who this Emily Herman girl is. I am gonna tell you all kinds of things about what makes her great, the things she loves to do, and the amazing people in her life. Thanks for stoping by!")
    with col1:
        st.image("Screen Shot 2022-10-05 at 8.28.15 AM.png")

with tab2:
   st.header("My Best Attributes")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("What is fun")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

with quiz:
    st.header("Put your knowledge of Emily to the test! Are you a fake friend???")
    st.empty()
    grade = 'nan'
    with st.form('quiz'):
        movie = st.radio('What is my favorite genre of TV/Movies?',('Reality TV','Rom Com','True Crime','Horror','Fantasy'))
        twin = st.radio("Am I the older or younger twin?",('Older','Younger','We were birthed at the exact same time'))
        travel = st.radio("If I could travel anywhere in the world, where would I go?", ('Spain','Houston','Australia','Maldives','Dubai'))
        matthew = st.radio("Where did I meet the love of my life?", ("Target", "Downtown", "Boat","Church","Class"))
        bowl = st.radio("What is my favorite bowl place?",('Cabo Bob\'s','Honest Mary\'s', 'Cava','Chipotle'))
        cal = st.radio("What is my favorite calender?",('Paper','Google','Outlook','Apple'))
        
        st.form_submit_button('Check my answers!')
        key = ['Rom Com','Younger','Maldives','Church','Cava','Google']
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
    st.header(diff.days)
    st.image("https://media.giphy.com/media/26BRL7YrutHKsVtJK/giphy.gif", width=800)




with tab5:
    st.header("A True Thank You")
