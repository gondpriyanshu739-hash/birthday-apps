import streamlit as st
import time

# 🌟 पेज का मुख्य सेटअप
st.set_page_config(page_title="Special Birthday Surprise 🎁", page_icon="👑", layout="centered")

# CSS की मदद से ऐप को और भी खूबसूरत (Premium Look) बनाना
st.markdown("""
    <style>
    .main { background-color: #f7f9fc; }
    .stButton>button {
        background: linear-gradient(45deg, #FF4B4B, #FF8E53);
        color: white;
        font-size: 20px;
        font-weight: bold;
        border-radius: 20px;
        padding: 10px 25px;
        border: none;
        box-shadow: 0px 4px 15px rgba(255, 75, 75, 0.3);
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0px 6px 20px rgba(255, 75, 75, 0.5);
    }
    .card {
        background-color: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 25px rgba(0,0,0,0.05);
        text-align: center;
        border-left: 5px solid #FF4B4B;
    }
    </style>
""", unsafe_allow_html=True)

# 🗺️ साइडबार (Sidebar) में 3 अलग-अलग पेजेस का मेनू बनाना
st.sidebar.title("🎈 Birthday Menu")
page = st.sidebar.radio("पेज चुनें:", ["🏠 Welcome Setup", "🎂 Magical Wish", "📸 Memory Lane"])

# ==========================================
# PAGE 1: WELCOME SETUP
# ==========================================
if page == "🏠 Welcome Setup":
    st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>👑 Welcome to the Birthday Palace 👑</h1>", unsafe_allow_html=True)
    st.write("---")
    
    st.markdown("""
    <div class='card'>
        <h2 style='color: #2C3E50;'>🎉 एक जादुई सरप्राइज आपका इंतज़ार कर रहा है!</h2>
        <p style='font-size: 16px; color: #7F8C8D;'>यह ऐप विशेष रूप से आज के दिन को यादगार बनाने के लिए डिज़ाइन की गई है।</p>
        <p style='font-size: 18px; font-weight: bold; color: #FF8E53;'>शुरू करने के लिए बाएं (Left Sidebar) से "Magical Wish" पेज पर जाएं!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # सजावट के लिए इमेज होल्डर
    st.image("https://unsplash.com", caption="Let's celebrate this beautiful day!", use_container_width=True)

# ==========================================
# PAGE 2: MAGICAL WISH
# ==========================================
elif page == "🎂 Magical Wish":
    st.markdown("<h1 style='text-align: center; color: #1E88E5;'>✨ The Magic Screen ✨</h1>", unsafe_allow_html=True)
    
    # नाम इनपुट
    name = st.text_input("किसका जन्मदिन है? नाम लिखें:", value="vishu")
    
    if st.button("🎁 सरप्राइज अनलॉक करें! 🎁", use_container_width=True):
        if not name.strip():
            st.warning("कृपया एक नाम टाइप करें!")
        else:
            # गुब्बारे उड़ाना
            st.balloons()
            
            # प्रीमियम प्रोग्रेस बार एनिमation
            progress_text = st.empty()
            progress_bar = st.progress(0)
            
            wishes_loading = [
                "🛸 खुशियों के सिग्नल ढूंढे जा रहे हैं...",
                "💖 आपके लिए ढेर सारा प्यार पैक किया जा रहा है...",
                "🎂 डिजिटल केक पर मोमबत्तियां जलाई जा रही हैं..."
            ]
            for percent_complete in range(100):
                time.sleep(0.02)
                progress_bar.progress(percent_complete + 1)
                if percent_complete < 33:
                    progress_text.markdown(f"**{wishes_loading[0]}**")
                elif percent_complete < 66:
                    progress_text.markdown(f"**{wishes_loading[1]}**")
                else:
                    progress_text.markdown(f"**{wishes_loading[2]}**")
                    
            progress_text.empty()
            progress_bar.empty()
            
            # फाइनल विश कार्ड
            st.markdown(f"""
            <div class='card' style='border-left: 5px solid #1E88E5; background: linear-gradient(135deg, #ffffff, #eef2f7);'>
                <h1 style='color: #FF4B4B; font-size: 40px; margin-bottom: 10px;'>🎉 HAPPY BIRTHDAY 🎉</h1>
                <h1 style='color: #1E88E5; font-size: 45px; text-transform: uppercase;'>👑 {name} 👑</h1>
                <hr style='border-top: 2px dashed #1E88E5;'>
                <p style='font-size: 20px; font-style: italic; color: #34495E; line-height: 1.6;'>
                    "सूरज रोशनी लेकर आया, और चिड़ियों ने गाना गाया,<br>
                    फूलों ने हंस-हंस कर बोला, मुबारक हो आपका जनमदिन आया!"
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # केक
            st.markdown("<h3 style='text-align: center; margin-top: 20px;'>🎂 आपका डिजिटल बर्थडे केक 🎂</h3>", unsafe_allow_html=True)
            st.code("""
                 _______   _______

                |       | |       |
              __|_______|_|_______|__

             |                       |
             |     🕯️  🕯️  🕯️  🕯️  🕯️     |
             |   ~ HAPPY BIRTHDAY ~  |
             |_______________________|
            """, language="text")
            
            st.snow()
# ==========================================
# PAGE 3: MEMORY LANE
# ==========================================
elif page == "📸 Memory Lane":
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📸 Memory Lane & Wishes 📸</h1>", unsafe_allow_html=True)
    st.write("---")
    
    st.markdown("### 💌 दोस्तों की तरफ से प्यारे संदेश:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style='background-color: white; padding: 20px; border-radius: 15px; border-left: 5px solid #4CAF50; min-height: 180px; display: flex; flex-direction: column; justify-content: flex-start; box-shadow: 0px 4px 10px rgba(0,0,0,0.1); margin-bottom: 15px;'>
            <h4 style='color: #1E293B; margin-top: 0; margin-bottom: 10px;'>💭 बेस्ट फ्रेंड का मैसेज</h4>
            <p style='color: #334155; font-size: 15px; margin-bottom: 15px; line-height: 1.4;'>“भाई तू हमेशा ऐसे ही हंसता रहे, पार्टी कब दे रहा है ये बता? जन्मदिन की बहुत-बहुत बधाई!”</p>
            <p style='color: #4CAF50; font-weight: bold; margin-top: auto; margin-bottom: 0;'>— PRIYANSHU</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div style='background-color: white; padding: 20px; border-radius: 15px; border-left: 5px solid #9C27B0; min-height: 180px; display: flex; flex-direction: column; justify-content: flex-start; box-shadow: 0px 4px 10px rgba(0,0,0,0.1); margin-bottom: 15px;'>
            <h4 style='color: #1E293B; margin-top: 0; margin-bottom: 10px;'>🌸 खास दुआ</h4>
            <p style='color: #334155; font-size: 15px; margin-bottom: 15px; line-height: 1.4;'>“भगवान करे आपकी हर वो ख्वाहिश पूरी हो जो आपके दिल में है। कामयाबी हमेशा आपके कदम चूमे।”</p>
            <p style='color: #9C27B0; font-weight: bold; margin-top: auto; margin-bottom: 0;'>— Bro we deserve a party</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("### ✨ आज का दिन खास है!")
    st.image("friend.00.jpg", caption="हमारी सबसे प्यारी यादें! 📸", use_container_width=True)
 

