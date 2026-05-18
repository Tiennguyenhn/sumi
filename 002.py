import streamlit as st
import random
st.header("Don't be late to AP Statistics!!")
st.image(
    "https://highered.collegeboard.org/media/images/media/ap-logo-780x439.jpg"
)
st.write("Rules")
st.write(
    "Generate a random door twice to determine if you're late to Ms. Hallock's class or not."
)
# ---------------------------
# DATA
# ---------------------------
first_doors = {
    1: (
        "Purple Door",
        "https://static.vecteezy.com/system/resources/thumbnails/068/390/415/small/purple-front-door-with-golden-handle-and-mail-slot-representing-home-entrance-vector.jpg",
    ),
    2: (
        "Red Door",
        "https://static.vecteezy.com/system/resources/previews/009/000/768/non_2x/red-door-cartoon-illustration-vector.jpg",
    ),
    3: (
        "Blue Door",
        "https://static.vecteezy.com/system/resources/previews/006/074/215/non_2x/illustration-graphics-of-a-closed-blue-door-free-vector.jpg",
    ),
    4: (
        "Green Door",
        "https://static.vecteezy.com/system/resources/previews/014/801/701/non_2x/green-door-icon-cartoon-front-home-vector.jpg",
    ),
}

second_doors = {
    1: (
        "Red Door",
        "https://static.vecteezy.com/system/resources/previews/024/293/479/non_2x/red-door-illustration-free-vector.jpg",
    ),
    2: (
        "Green Door",
        "https://static.vecteezy.com/system/resources/previews/014/801/701/non_2x/green-door-icon-cartoon-front-home-vector.jpg",
    ),
}
# ---------------------------
# FIRST DOOR
# ---------------------------
if st.button("Generate First Door"):
    st.session_state.r1 = random.randint(1, 4)
    # reset second door
    st.session_state.r2 = None
    name, image_url = first_doors[st.session_state.r1]
    st.image(image_url)
    st.info(f"You got a {name}!")
# ---------------------------
# SECOND DOOR
# ---------------------------
if st.button("Generate Second Door"):
    # Prevent error
    if "r1" not in st.session_state:
        st.warning("Generate the first door first!")
    else:
        st.session_state.r2 = random.randint(1, 2)
        name, image_url = second_doors[st.session_state.r2]
        st.image(image_url)
        st.info(f"You got a {name}!")
        st.markdown("## Result")
        r1 = st.session_state.r1
        r2 = st.session_state.r2
        # ---------------------------
        # RESULTS
        # ---------------------------
        if (r1 == 1 and r2 == 1) or (r1 == 1 and r2 == 2):
            st.info("You are on time to Ms. Hallock's class :))")
            st.image(
                "https://ih1.redbubble.net/image.5374364575.4046/tst,small,845x845-pad,1000x1000,f8f8f8.jpg"
            )
        elif r1 == 2 and r2 == 1:
            st.warning(
                "You are late. Ms. Hallock is gonna deduct 3 points from you."
            )
            st.image(
                "https://media.tenor.com/JYyzR_1h77MAAAAe/angry-emoji.png"
            )
        elif r1 == 2 and r2 == 2:
            st.info("You are on time to Ms. Hallock's class :))")
            st.image(
                "https://ih1.redbubble.net/image.5374364575.4046/tst,small,845x845-pad,1000x1000,f8f8f8.jpg"
            )
        elif r1 == 3 and r2 == 1:
            st.success(
                "You are early to class! Ms. Hallock rewards you with 3 points. You will get a 5 in AP Stats!"
            )
            st.image(
                "https://pbs.twimg.com/media/F0oqrGSX0AAd44b.jpg"
            )
        elif r1 == 3 and r2 == 2:
            st.warning(
                "You are late. Ms. Hallock is gonna deduct 3 points from you."
            )
            st.image(
                "https://media.tenor.com/JYyzR_1h77MAAAAe/angry-emoji.png"
            )
        elif r1 == 4 and r2 == 1:
            st.info("You are on time to Ms. Hallock's class :))")
            st.image(
                "https://ih1.redbubble.net/image.5374364575.4046/tst,small,845x845-pad,1000x1000,f8f8f8.jpg"
            )
        elif r1 == 4 and r2 == 2:
            st.success(
                "You are early to class! Ms. Hallock rewards you with 3 points. You will get a 5 in AP Stats!"
            )
            st.image(
                "https://pbs.twimg.com/media/F0oqrGSX0AAd44b.jpg"
            )
