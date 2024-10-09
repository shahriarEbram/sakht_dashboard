import pickle
from pathlib import Path

import streamlit_authenticator as stauth

staff_names = [
    "محمدرضا مرادی", "رحمت ایمانی پور", "حمید خانی", "محمد محمدی", "وحید طالقانی", "رسول محمدخانی",
    "ابراهیم کریمی", "بهزاد مهدی زاده", "فرشاد بیگلری", "بیت الله امامی", "جواد کلهر", "رسول نصیری",
    "محسن آریایی", "رضا قاسمی", "علی زمانی", "محمد رحمانی", "حسن حیدری", "رضا رشوند", "رضا حسینی",
    "فرهاد هاشم خانی", "داریوش درخشانی", "فاضل نوری", "رحیم محمدخانی", "جواد مقدادی", "حسن احمدی",
    "داود حیدری", "مهدی داوودی", "جواد حسین علیزاده", "شهریار ابرام پور", "پرستو دمرچی", "علی سهرابی"
]

usernames = [
    "moradi", "rahmat_imanipour", "hamid_khani", "mohammad_mohammadi", "vahid_taleghani",
    "rasool_mohammadkhani", "ebrahim_karimi", "behzad_mehdizadeh", "farshad_biglari", "beytolah_emami", "javad_kalhor",
    "rasool_nasiri", "mohsen_ariayi", "reza_qasemi", "ali_zamani", "mohammad_rahmani", "hasan_heydari",
    "reza_rashvand", "reza_hosseini", "farhad_hashemkhani", "dariush_derakhshani", "fazl_noori", "rahim_mohammadkhani",
    "javad_meghdadi", "hasan_ahmadi", "davood_heydari", "mehdi_davoodi", "javad_hosseinalizadeh", "ebrampour",
    "damerchi", "sohrabi"
]

passwords = ["123"] * len(staff_names)  # All passwords set to "123" for simplicity

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path("data/hashed_pw.pkl")
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)
