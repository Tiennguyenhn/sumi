import streamlit as st
from sklearn.linear_model import LinearRegression
import feedparser
import random
import time

st.sidebar.title("danh sánh nghệ sĩ")
selected_artist = st.sidebar.radio("Chọn nghệ sĩ:", ["Đen Vâu", "Hà Anh Tuấn", "Sơn Tùng M-TP", "Những bản nhạc giúp tâm trạng vui vẻ hơn"])

videos = {
    "Đen Vâu": [
        ("Nấu ăn cho em", "https://www.youtube.com/watch?v=ukHK1GVyr0I"),
        ("Mang tiền về cho mẹ", "https://www.youtube.com/watch?v=UVbv-PJXm14"),
        ("Trời hôm nay nhiều mây cực!", "https://www.youtube.com/watch?v=MBaF0l-PcRY"),
        ("Hai triệu năm", "https://www.youtube.com/watch?v=LSMDNL4n0kM")        
    ],
    "Hà Anh Tuấn": [
        ("Tuyết rơi mùa hè", "https://www.youtube.com/watch?v=pTh3KCD7Euc"),
        ("Nước ngoài", "https://www.youtube.com/watch?v=pU3O9Lnp-Z0"),
        ("Tháng tư là lời nói dối của em", "https://www.youtube.com/watch?v=UCXao7aTDQM"),
        ("Xuân thì", "https://www.youtube.com/watch?v=3s1r_g_jXNs")
    ],
    "Sơn Tùng M-TP": [
        ("Lạc trôi", "https://www.youtube.com/watch?v=Llw9Q6akRo4"),
        ("Chúng ta không thuộc về nhau", "https://www.youtube.com/watch?v=qGRU3sRbaYw"),
        ("Muộn rồi mà sao còn", "https://www.youtube.com/watch?v=xypzmu5mMPY"),
        ("Hãy trao cho anh", "https://www.youtube.com/watch?v=knW7-x7Y7RE")
    ],
    "Những bản nhạc giúp tâm trạng vui vẻ hơn":[
        ("Những bản nhạc giúp tâm trạng vui vẻ hơn", "https://www.youtube.com/watch?v=SlsH6PbDJZk&t=898s"),
        ("Lỡ Duyên", "https://www.youtube.com/watch?v=fq_H4A3HgD4&list=RDfq_H4A3HgD4&start_radio=1&rv=fq_H4A3HgD4"),
        ("Bài hat về tình yêu quê hương đất nước", "https://www.youtube.com/watch?v=GOMGeUetqlI&list=RDSlsH6PbDJZk&index=3"),
        ("Đi giữa trời rực rỡ", "https://www.youtube.com/watch?v=D1Uf9vREh6Q&list=RDSlsH6PbDJZk&index=3"),
        ("STAY HOME, STAY HAPPY, STAY HÀANHTUẤN", "https://www.youtube.com/watch?v=MMgPOQ9gJhM&list=RDEMrx5Xy48sg-WCr9qiaw1hhg&index=2"),
        ("Focus Time", "https://www.youtube.com/watch?v=Lcmlq9utGYk")
    ]    
}
st.title(" ứng dụng giải trí và sức khỏe")
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["MV yêu thích ", "Suc khoe", "doc bao", "Giai tri", "DISC", "ung dung suc khoe"])
with tab1:
    st.header(f"Các bài hát của {selected_artist}")
    for title, url in videos[selected_artist]:
        st.subheader(title)
        st.video(url)
with tab2:
    tabA, tabB, tabC, tabD = st.tabs(["du doan gio di ngu moi dem", "kiem tra BMI", "nuoc", "so buoc di"])
    with tabA:
        st.header("Dự đoán giờ đi ngủ mỗi đêm ")
    #Tuổi, mức độ hoạt động thể chất, thời gian dùng máy tính
        x = [
            [10, 1, 8],
            [20, 5, 6],
            [25, 8, 3],
            [30, 6, 5],
            [35, 2, 9],
            [40, 4, 3],
        ]
        y = [10, 8, 6, 7, 9.5, 9]
        model = LinearRegression()
        model.fit(x, y)
        st.write("Nhập thông tin cá nhân: ")
        age = st.number_input("Tuổi của bạn", min_value=5, max_value=100, value=5)
        activity = st.slider("Mức độ hoạt động thể chất (1 = ít, 10 = rất nhiều)", 1, 10, 5)
        screen_time = st.number_input("Thời gian dùng màn hình trong 1 ngày (giờ)", min_value=0, max_value=24, value=6)
        if st.button("Dự đoán ngay"):
            input_data = [[age, activity, screen_time]]
            result = model.predict(input_data)[0]
            st.success(f"Bạn nên ngủ khoảng {result: .1f} giờ mỗi đêm")

            if result < 6.5:
                st.warning("có thể bạn cần nghỉ ngơi nhiều hơn để cái thiện sức khỏe. ")
            elif result > 9:
                st.info("có thể bạn đang vận động nhiều, bạn cần ngủ bù hợp lý nhé")
            else:
                st.success("Lượng ngủ lý tưởng, hãy giữ thói quan tốt ")
    with tabB:
        st.header("📊 Kiểm tra chỉ số BMI của bạn")

        can_nang = st.number_input("Nhập cân nặng của bạn (kg)", min_value=10.0, max_value=200.0, value=60.0, step=0.1)
        chieu_cao = st.number_input("Nhập chiều cao của bạn (m)", min_value=1.0, max_value=2.5, value=1.7, step=0.01)

        if st.button("📏 Tính BMI"):
            bmi = can_nang / (chieu_cao ** 2)
            st.success(f"Chỉ số BMI của bạn là: {bmi:.2f}")

        # Ngưỡng BMI
            bmi_min = 18.5
            bmi_max = 24.9

        # Cân nặng tương ứng
            can_nang_min = bmi_min * (chieu_cao ** 2)
            can_nang_max = bmi_max * (chieu_cao ** 2)

            if bmi < 18.5:
                st.warning("Bạn đang thiếu cân, nên ăn uống đầy đủ và dinh dưỡng hơn.")
                can_tang = can_nang_min - can_nang
                st.info(f"👉 Bạn cần **tăng ít nhất {can_tang:.2f} kg** để đạt mức cân nặng tối thiểu bình thường.")

            elif 18.5 <= bmi < 25:
                st.info("Bạn có cân nặng bình thường. Hãy tiếp tục duy trì lối sống lành mạnh.")
                st.success("👍 Bạn không cần tăng hoặc giảm cân.")

            elif 25 <= bmi < 30:
                st.warning("Bạn đang thừa cân. Nên cân đối chế độ ăn và tập thể dục.")
                can_giam = can_nang - can_nang_max
                st.info(f"👉 Bạn cần **giảm ít nhất {can_giam:.2f} kg** để quay về mức bình thường.")

            else:
                st.error("Bạn đang béo phì. Nên gặp chuyên gia dinh dưỡng hoặc bác sĩ để được tư vấn.")
                can_giam = can_nang - can_nang_max
                st.info(f"👉 Bạn cần **giảm ít nhất {can_giam:.2f} kg** để về ngưỡng cân nặng bình thường.")
    with tabC:
        age = st.number_input("Nhập tuổi của bạn: ", min_value=1, max_value=100, value=18, step=1)
        if st.button("Kiểm tra lượng nước cần uống "):
            if age < 4:
                st.info("Khuyến nghị: 1.3 lít/ngày ")
            elif 4 <= age <= 8:
                st.info("Khuyến nghị: 1.7 lít/ngày ")
            elif 9 <= age <= 13:
                st.info("Khuyến nghị: 2.1 đến 2.4 lít/ngày ")
            elif 14 <= age <= 18:
                st.info("Khuyến nghị: 2.3 đến 3.3 lít/ngày ")
            elif 19 <= age <= 50:
                st.info("Khuyến nghị: 2.7 lít/ngày đối với nữ, 3.7 lít/ ngày đối với nam ")
            elif age > 50:
                st.info("khuyến nghị: khoảng 2.5lit/ngay đến 3 lít/ngày (phụ thuộc vào sức khỏe và mức độ vận động")
            else:
                st.warning("Vui lòng nhập độ tuổi hợp lệ")
    with tabD:
        st.header("Kiểm tra số bước đi phù hợp mỗi ngày ")
        age2 = st.number_input("Nhập tuổi của bạn: ", min_value=0.0, max_value=130.0, value=18.0, step=1.0)
        if st.button("Kiểm tra số bước "):
            st.success(f"tuổi của bạn: {age2: .0f}")
            if age2 < 18:
                st.info("bạn nên đi 12000 - 15000 bước mỗi ngày ")
            elif 17 < age2 <=39:
                st.info("Bạn nên đi 8000 - 10000 bước mỗi ngày ")
            elif 39 < age2 <= 64:
                st.info("Bạn nên đi từ 7000 - 9000 bước mỗi ngày ")
            elif age2 > 64:
                st.info("bạn nên đi 6000 đến 8000 bước mỗi ngày ")
            else:
                st.error("có lỗi xảy ra . Vui lòng kiểm tra lại thông tin ")
with tab3:
    tabA, tabB = st.tabs(["cap nhat gia vang tu Vietnamnet", "tinh tuc moi nhat"])
    with tabA:
        st.header("cập nhật giá vàng từ Vietnamnet")
        feed = feedparser.parse("https://vietnamnet.vn/rss/kinh-doanh.rss")
        gold_news = [entry for entry in feed.entries if "vàng" in entry.title.lower() or "giá vàng" in entry.summary.lower()]
        if gold_news:
            for entry in gold_news[:5]: #hiển thị 5 bài báo gần nhất
                st.subheader(entry.title)
                st.write(entry.published)
                st.write(entry.link)
    with tabB:
        st.header("tin tức mới nhất")
        feed = feedparser.parse("https://vnexpress.net/rss/tin-moi-nhat.rss")
        for entry in feed.entries[:5]:
            st.subheader(entry.title)
            st.write(entry.published)
            st.write(entry.link)
with tab4:
    tabA, tabB, tabC, tabD, tabE = st.tabs(["Game tung xúc sắc", "Game đoán số", "Kéo - búa - bao", "Quay so may man", "game quay so"])
    with tabA:
        st.header("🤖Game tung xúc sắc")
        st.image("https://thumb.ac-illust.com/11/11208a7f39207d32b1cff1a66d22dd75_t.jpeg")
        st.write("Luật chơi")
        st.write("Bấm lắc xúc sắc để được một số ngẫu nhiên từ 1 đến 6 ")
        if st.button(" 🎲 Lắc xúc sắc"):
            roll = random.randint(1, 6)
            st.success(f"Bạn tung được số {roll} !!!!")
            if roll == 1:
                st.image(
                    "http://www.clker.com/cliparts/m/v/m/J/4/V/dice-1-md.png"
                )
            if roll == 2:
                st.image(
                "https://www.clker.com/cliparts/a/Y/E/o/z/t/dice-2-md.png"
            )
            if roll == 3:
                st.image(
                "https://www.clker.com/cliparts/O/I/r/9/W/x/dice-3-md.png"
            )
            if roll == 4:
                st.image(
                "https://www.clker.com/cliparts/r/z/d/a/L/V/dice-4-md.png"
            )
            if roll == 5:
                st.image(
                "https://www.clker.com/cliparts/U/N/J/F/T/x/dice-5-md.png"
            )
            if roll == 6:
                st.image(
                "https://www.clker.com/cliparts/l/6/4/3/K/H/dice-6-md.png"
            )
    with tabB:
        st.header("Game đoán số bí mật 1 - 100")
        st.image("https://m.media-amazon.com/images/I/71Agu95C-jL._AC_UF894,1000_QL80_.jpg")
        st.write("Luật chơi")
        st.write("Đoán số bất kì từ 1 đến 100, nhập số để biết được số chính xác lớn hơn hay nhỏ hơn số đã nhập, cố gắng đoán trong ít lần thử nhất có thể." \
        "bấm chơi lại sau khi đoán đúng để được chơi lại")
        if "secret" not in st.session_state:
            st.session_state.secret = random.randint(1, 100)
            st.session_state.tries = 0
        guess = st.number_input("Nhập số dự đoán 1 - 100", min_value=1, max_value=100, step=1)
        if st.button("Đoán !!!!"):
            st.session_state.tries += 1
            if guess < st.session_state.secret:
                st.warning("Lớn hơn")
                st.image("https://i.kym-cdn.com/editorials/icons/original/000/013/755/mon.jpg")
            elif guess > st.session_state.secret:
                st.warning("Nhỏ hơn")
                st.image("https://i.kym-cdn.com/editorials/icons/original/000/013/755/mon.jpg")
            else:
                st.success(f"Chính xác ! Bạn đoán đúng sau {st.session_state.tries} lần")
                st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2pBfdCwgvKb7E8RBYkSluf3u3EdNxv54GuQ&s")
        if st.button("chơi lại"):
            st.session_state.secret = random.randint(1, 100)
            st.session_state.tries = 0
    with tabC:
        st.header("keo - bua - bao")
        st.image("https://static.tvtropes.org/trope_videos_transcoded/images/sd/q7uwxt.jpg")
        st.write("luat choi")
        st.write("ban bam nut de ra mot trong keo, bua, hoac bao. Hay co gang thang con bot!")
        st.write("keo thang bao")
        st.write("bua thang keo")
        st.write("bao thang bua")
        user = st.selectbox("ban chon: ", ["keo", "bua", "bao"])
        bot = random.choice(["keo", "bua", "bao"])
        if st.button("ra tay nao!"):
            st.write(f"bot chon: {bot}")
            if user == bot:
                st.warning("hoa!")
                st.image("https://i1.sndcdn.com/artworks-ecyyzfetWzmHLDpo-X7ICfQ-t500x500.jpg")
            elif((user == "keo" and bot == "bao") or (user == "bao" and bot == "bua") or (user == "bua" and bot == "keo")):
                st.success("ban chien thang!")
                st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1MBsQ9GnV0RNq9b_rJA63UN8m4e0Xq6HpGQ&s")
            else:
                st.error("ban thua!")
                st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGlF-k_0Gsm39dJSSZCSEJUF-UsSkm_SAkHg&s")
    with tabD:
        st.header("quay so may man")
        if "prizes" not in st.session_state:
            st.session_state.prizes = []
        new_prize = st.text_input("nhap phan thuong")
        if st.button("them phan thuong"):
            if new_prize:
                st.session_state.prizes.append(new_prize)
        st.write("danh sach phan thuong: ", st.session_state.prizes)
        if st.button("quay so"):
            if st.session_state.prizes:
                result = random.choice(st.session_state.prizes)
                st.success(f"ban quay trung: {result}")
                st.sesson_state.prizes.remove(result)
            else:
                st.warning("chua co phan thuong")
        if st.button("reset"):
            st.session_state.prizes = []
    with tabE:
        st.title("game quay so")
        if "new_prizes" not in st.session_state:
            st.session_state.new_prizes = []
        if "weights" not in st.session_state:
            st.session_state.weights = []
        st.subheader("them phan thuong")
        col1, col2 = st.columns(2)
        with col1:
            new_prize = st.text_input("ten phan thuong")
        with col2:
            weight = st.number_input("ty le trung %", 1, 100, 1)
            if st.button("them_phan thuong"):
                if new_prize:
                    st.session_state.newprizes.append(new_prize)
                    st.session_state.weights.append(weight)
                    st.success("da them: {new_prize}")
            st.subheader("danh sach phan thuong ")
            if st.session_state.new_prizes:
                for i, prize in enumerate(st.session_state.new_prizes):
                    st.write(
                        f"{i + 1}. {print} | ty le {st.session_state.weights[i]} %"
                    )
            else:
                st.info("chua co phan thuong")
            st.subheader("quay so ")
            if st.button("quay ngay "):
                if st.session_state.new_prizes:
                    spin_placeholder = st.empty()
                    for i in range(15):
                        spin_placeholder.markdown(
                            f"dang quay ...{random.choice[st.session_state.new_prizes]}"
                        )
                        time.sleep(0.1)
                    result = random.choice(
                        st.session_state.new_prizes,
                        weights = st.session_state.weights,
                        k = 1
                    )[0]
                    spin_placeholder.empty()
                    st.balloons()
                    st.success(f"chuc mung ban da trung: {result}")
                else:
                    st.warning("chua co phan thuong")
            if st.button("reset game"):
                st.session_state.new_prizes = []
                st.session_state.weights = []
                st.success("da reset ")
    with tab5:
        st.header("kiem tra tinh cach theo DISC")
        st.markdown("chon mot mo ta dung nhat va mot mo ta it dung nhat trong tung nhom")
        groups = [
            {
                "D": "toi quyet doan va thich tinh kiem soat",
                "I": "toi thich than thien va noi chuyen de dang",
                "S": "toi thich kien nhan va dang tinh cay",
                "C": "toi chinh xac va co he thong",
            },
            {
                "D": "toi thich thu thach va hanh dong nhanh",
                "I": "toi thich tran day nang luong va lac quan",
                "S": "toi thich on dinh va ho tro nguoi khac",
                "C": "toi thich lam viec theo quy tac ro rang",
            },
            {
                "D": "toi thich kiem soat ket qua",
                "I": "toi thich duoc cong nhan",
                "S": "toi uu tien su hai huoc",
                "C": "toi chu y den viec chi tiet va phan thich"
            }
        ]
        scores = {"D": 0, "I": 0, "S": 0, "C": 0}
        for idx, group in enumerate(groups):
            st.markdown(f"### nhom {idx + 1}")
            options = list(group.values())
            keys = list(group.keys())
            most = st.radio("mo ta dung nhat voi ban ", options, key = f"most_{idx}")
            least = st.radio("mo ta it dung nhat ve ban ", options, key = f"least_{idx}")
            for key, val in group.items():
                if val == most:
                    scores[key] += 1
                if val == least:
                    scores[key] -= 1
        if st.button("xem xet ket qua DISC"):
            st.header("ket qua cua ban ")
            max_type = max(scores, key = scores.get)
            for style, score in scores.items():
                st.write(f"{style}: {score} diem")
            st.markdown(f"tinh cach noi bat nhat cua ban la: {max_type}**")
            description = {
                "D": "quyet doan, dinh huong ket qua va thich kiem soat",
                "I": "giao tieps tot, tran day nang luong va truyen cam hung",
                "S": "kien nhan, dang tin cay va ho tro nguoi khac",
                "C": "chinh xac, tuan thu quy trinh va thich phan tich logic"
            }
            st.info(description[max_type])
            st.markdown("____")
            st.markdown("mo ta chi tiet cac nhom DISC")
            st.markdown("""
            - **D**: nguoi lanh dao, chu dong, thich canh tranh
            - **I**: nguoi truyen cam hung, thich giao tiep, co suc hut
            - **S**: nguoi ho tro, trung thanh, kien tri
            - **C**: nguoi phan tich, ti mi
            """)
            st.caption("day chi la bai tham khao ve chi so DISC")
with tab6:
    st.set_page_config(page_title="ung dung suc khoe nang cao ", layout="centered")
    st.title("ung dung theo doi suc khoe nang cao ")
    st.header("nhap thong tin ca nhan")
    name = st.text_input("ho va ten")
    age = st.number_input("tuoi: ", min_value=0, max_value=120, step=1)
    gender = st.radio("gioi tinh: ", ("nam", "nu"))
    height = st.number_input("chieu cao(cm): ", min_value=50.0, max_value=250.0, step=0.1)
    weight = st.number_input("can nang (kg): ", min_value=10.0, max_value=250.0, step=0.1)
    activity_level = st.selectbox("muc do hoat dong the chat: ", [
        "it van dong",
        "van dong nhe (1-3 buoi/tuan)",
        "van dong vua (3-5 buoi/tuan)",
        "van dong nhieu (6-7 buoi/tuan)",
        "van dong rat nhieu (2 lan/ngay)"
    ])
    if st.button("phan tich suc khoe "):
        if height > 0 and weight > 0:
            height_m = height/100
            bmi = weight / (height_m ** 2)
            if gender == "nam":
                bmi = 10*weight +6.25*height-5*age+5
            else:
                bmr = 10*weight +6.25*height-5*age - 161
            activity_factors = {
                "it van dong": 1.2,
                "van dong nhe (1-3 buoi/tuan)": 1.375,
                "van dong vua (3-5 buoi/tuan)": 1.55,
                "van dong nhieu (6-7 buoi/tuan)": 1.725,
                "van dong rat nhieu (2 lan/ngay)": 1.9
            }
            activity_factor = activity_factors[activity_level]
            tdee = bmr * activity_factor
            water_intake = weight * 35/1000
            st.subheader("ket qua phan tich")
            st.write(f"** xin chao {name}!**")
            st.write(f"** chi so bmi:** '{bmi: .2f}' kcal/ngay**")
            st.write(f"** chi so bmr:** '{bmr: .0f}' kcal/ngay**")
            st.write(f"** tdee(nang luong tieu hoa moi ngay):** '{tdee:.0f}' kcal/ngay")
            st.write(f"**luong nuoc nen uong moi ngay:** '{water_intake:.0f}' lit**")
            st.markdown("### danh gia chi so bmi: ")
            if bmi < 18.5:
                st.warning(f"ban dang thieu can. ban nen tang {round(((18.5 - bmi)*(height_m **2)),2)} kg")
            elif 18.5 <= bmi < 25.9:
                st.success("ban cos can nang binh thuong.")
            elif 25 <= bmi < 29.9:
                st.warning(f"ban dang thua can. ban nen giam {round(((bmi - 14.9)*(height_m ** 2)),2)} kg")
            else:
                st.error(f"ban dg beo phi. can tham khoa chuyen gia de kiem tra suc khoe. ban nen giam {round(((bmi - 24.9) * (height_m * 2))), 2} kg")
            st.markdown("goi y che do an theo muc tieu: ")
            col1, col2 = st.columns(2)
            with col1:
                st.info("duy tri can nag")
                st.write(f" an khoang '{tdee-300: .0f}' ka/ngay")
            with col2:
                st.info("giam can nhe: ")
                st.write(f" an khoang '{tdee-300: .0f}' kal/ngay")
            st.markdown("goi y thuc don: ")
            st.markdown("""
            -sang : trung luoc, banh mi nguyen cam, trai cay
            -trua : com gao nut, uc ga, rau luoc, canh
            -toi: salad rau xanh, ca hap, trai cay it ngot
            -snack: hat kho, sua chua it duong
            """)
    st.header("theo doi suc khoe ve nhip tim ")
    sys = st.number_input("huyet ap tam thu(mmhg) :", min_value=50, max_value=250, step=1)
    dia = st.number_input("huyet ap tam truong(mmhg) : ",min_value=30, max_value=150,step=1)
    heart_rate = st.number_input("nhip tim khi nghi ngoi(bpm): ", min_value=30, max_value=200, step=1)
    if st.button("phan tich nhip tim"):
        st.header("ket qua phan tich tim mach")
        if sys<90 or dia<60:
            st.warning("huyet ap thap ")
        elif 90<= sys <= 120 and 60<=dia<=80:
            st.success("huyet ap bthg")
        elif 120<= sys <= 139 and 80<=dia<=89:
            st.success("tien huyet ap")
        elif 140<= sys <= 159 and 90<=dia<=99:
            st.success("tang huyet ap do 1")
        elif 160<= sys <= 179 and 90<=dia<=109:
            st.success("tang huyet ap do 2")
        else:
            st.error("tang huyet ap do 3")
        if heart_rate < 60:
            st.warning("nhip tim cham")
        elif 60 <= heart_rate <=100:
            st.success("nhip tim bthg")
        else:
            st.success("nhip tim cao")
    st.markdown("nhip tim theo do tuoi")
    st.markdown("""
        - Công thức nhịp tim tối đa: 220 - tuổi  
        - Vùng tập luyện hiệu quả: *50% - 85% nhịp tim tối đa*
        | Tuổi | Tối đa (bpm) | 50-85% (bpm) |
        |------|--------------|--------------|
        | 20   | 200          | 100 - 170    |
        | 30   | 190          | 95 - 162     |
        | 40   | 180          | 90 - 153     |
        | 50   | 170          | 85 - 145     |
        | 60   | 160          | 80 - 136     |
        | 70   | 150          | 75 - 128     |
        """)
    st.header("phat trien chieu cao")
    if age > 0:
        st.subheader("phan tich tiem nang phat trien chieu cao")
        if gender == "nam":
            max_growth_age = 21
        else:
            max_growth_age = 19
        if age >= max_growth_age:
            st.info("""o tuoi hien tai, kha nang tang chieu cao tu nhien gan nhu laf ko con.
                    ban nen tap luyen va bo sung dinh duong de giu voc dang can doi.
            """)
        else:
            remaining_years = max_growth_age - age
            st.write(f"ban van con khoang {remaining_years} nam de phat trien chieu cao toi uu")
            if activity_level == "it van dong ":
                growth_potential = "thap"
                st.warning("muc do van dong thap co the lam han che phat trien chieu cao. hay co gang van dong nhieu hon moi ngay")
            if activity_level == ["van dong nhe (1-3 buoi/tuan)"]:
                growth_potential = "trung binh"
                st.info("muc do van dong kha tot, ban nen bo sung them cac bai tap")
            else:
                growth_potential = "cao"
                st.success("rat tot, muc do van dong cao giup kich thich hormone tang truong, ho tro phat trien chieu cao toi da")
            st.markdown(f"tiem nang phat trien chieu cao cua ban: {growth_potential}")
            st.markdown("goi y phat trien chieu cao toi da")
            with st.expander("che do dinh duong nen bo sung"):
                st.markdown("""
                - protein: thit nac, ca, trung, dau phu
                - canxi: sua, pho mai, sua chua, ca hoi, rau xanh dam
                - vitamin d: phoi nang 15 den 20 phut hoac an trung, ca
                - kem va magie: co trong hai san, ngu coc nguyen hat
                - tranh: nuoc ngot co ga, do an nhanh, do chien ran  
                """)
            with st.expander("Bài tập hỗ trợ phát triển chiều cao "):
                st.markdown("""
                    -Tập hàng ngày: Bơi lội, nhảy dây, bóng rổ, đu xà, yoga kéo dãn
                    -Buổi sáng: Kéo dãn cơ thể, vươn vai, hít thở sâu ngoài trời
                    -Thói quen: Giữ lưng thẳng khi ngồi và đứng, tránh gù lưng
                """)
            with st.expander("Thói quen sinh hoạt và giấc ngủ "):
                st.markdown("""
                    -Ngủ đủ 8 - 10 tiếng/ngày, đặc biệt ngử từ 22h đến 6h sáng
                    -Hạn chế thức khuya, dùng điện thoại trước khi ngủ
                    -Uống đủ nước(theo khuyến nghị ở phần trên)
                    -Duy trì cân nặng hợp lý để không ảnh hưởng đến hormone tăng trưởng
                """)
            if gender == "Nam":
                avg_height = 175
            else:
                avg_height = 162
            potential_height = height + remaining_years * 0.8
            if potential_height > avg_height:
                potential_height = avg_height + 2
            st.markdown(f"Chiều cao tiềm năng ước tính: {potential_height: .1f} cm")
    else:
        st.warning("Vui lòng nhập thông tin cá nhân ở phần đầu (tuổi, giới tính, chiều cao...) trước khi phân tích")
