unit_name = ["BT1", "BT2", "BT3", "BT4", "BT5", "BT6", "دفتر مرکز"]
work_shift = ["شیفت اول", "شیفت دوم"]

employee_names = {
    "moradi": "محمدرضا مرادی",
    "rahmat_imanipour": "رحمت ایمانی پور",
    "hamid_khani": "حمید خانی",
    "mohammad_mohammadi": "محمد محمدی",
    "vahid_taleghani": "وحید طالقانی",
    "rasool_mohammadkhani": "رسول محمدخانی",
    "ebrahim_karimi": "ابراهیم کریمی",
    "behzad_mehdizadeh": "بهزاد مهدی زاده",
    "farshad_biglari": "فرشاد بیگلری",
    "beytolah_emami": "بیت الله امامی",
    "javad_kalhor": "جواد کلهر",
    "rasool_nasiri": "رسول نصیری",
    "mohsen_ariayi": "محسن آریایی",
    "reza_ghasemi": "رضا قاسمی",
    "ali_zamani": "علی زمانی",
    "mohammad_rahmani": "محمد رحمانی",
    "hasan_heydari": "حسن حیدری",
    "reza_rashvand": "رضا رشوند",
    "reza_hosseini": "رضا حسینی",
    "farhad_hashemkhani": "فرهاد هاشم خانی",
    "dariush_derakhshani": "داریوش درخشانی",
    "hamid_ghorbani": "حمید قربانی",
    "rahim_mohammadkhani": "رحیم محمدخانی",
    "javad_meghdadi": "جواد مقدادی",
    "hasan_ahmadi": "حسن احمدی",
    "davood_heydari": "داود حیدری",
    "mehdi_davoodi": "مهدی داوودی",
    "javad_hosseinalizadeh": "جواد حسین علیزاده",
    "ebrampour": "شهریار ابرام پور",
    "damerchi": "پرستو دمرچی",
    "sohrabi": "علی سهرابی"
}

work_type = [ "پروژه", "یدکی اصلاحی", "هفتگی", "متفرقه"]

categories = {
    "CNC": [
        "سنگ محور", "1000", "FIL", "720", "هرمله1", "هرمله2", "NEWAY"
    ],
    "برشکاری": [
        "هوابرش CNC", "اره نواري"
    ],
    "جوشکاری": [
        "ترانس جوش"
    ],
    "تراشکاری": [
        "تراش1", "تراش2", "تراش3", "تراش4"
    ],
    "کار دستی": [
        "پلیسه گیری", "سنگ زنی", "مونتاژ"
    ],
    "فرزکاری": [
        "فرز1", "فرز2", "فرز3", "فرز4", "فرز5", "فرز6", "اسپارک"
    ],
    "سوراخ کاری و قلاویزکاری": [
        "رادیال 1", "رادیال 2"
    ]
}

column_names_fa = {
    'id': 'شناسه',
    'person_name': 'نام کاربر',
    'unit': 'واحد',
    'shift': 'شیفت',
    'operation': 'عملیات',
    'machine': 'ماشین',
    'product': 'محصول',
    'work_type': 'نوع کار',
    'project_code': 'کد پروژه',
    'date': 'تاریخ',
    'operation_duration': 'مدت زمان کارکرد',
    'announced_duration': 'مدت زمان اعلام شده',
    'done_duration': 'مدت زمان انجام شده'
}

stoppage_list = [
    "عدم برنامه",
    "نبود مواد",
    "نبود ابزار",
    "آماده نبودن نقشه",
    "تعمیر و اصلاح دستگاه",
    "خرابی دستگاه",
    "توقف برقی",
    "مرخصی اپراتور",
    "کمبود اپراتور"
]

# Mapping operators to machine groups
operator_machine_group = {
    "behzad_mehdizadeh": ["CNC"],
    "ebrahim_karimi": ["CNC"],
    "hasan_heydari": ["فرزکاری", "تراشکاری"],
    "farhad_hashemkhani":  ["فرزکاری", "تراشکاری"],
    "mohammad_mohammadi": ["سوراخ کاری و قلاویزکاری"],
    "moradi": ["برشکاری", "جوشکاری"]
}

# Mapping operators to their workers
operator_workers = {
    "behzad_mehdizadeh": ["حمید قربانی",
                          "رسول نصیری",
                          "محسن آریایی",
                          "جواد کلهر",
                          "فرشاد بیگلری",
                          "بیت الله امامی",
                          ],

    "ebrahim_karimi": ["حمید قربانی",
                       "رسول نصیری",
                       "محسن آریایی",
                       "جواد کلهر",
                       "فرشاد بیگلری",
                       "بیت الله امامی",
                       ],

    "hasan_heydari": ["علی زمانی",
                      "رضا رشوند",
                      "رضا قاسمی",
                      "سید رضا حسینی",
                      "جواد حسین علیزاده",
                      "محمد رحمانی",
                      "حسن احمدی",
                      "مهدی داوودی",
                      "داریوش درخشان",
                      ],
    "farhad_hashemkhani": ["علی زمانی",
                           "رضا رشوند",
                           "رضا قاسمی",
                           "سید رضا حسینی",
                           "جواد حسین علیزاده",
                           "محمد رحمانی",
                           "حسن احمدی",
                           "مهدی داوودی",
                           "داریوش درخشان",
                           ],

    "mohammad_mohammadi": ["وحید طالقانی",
                           "داود حیدری",
                           "رسول محمدخانی"
                           ],

    "moradi": ["حمید خانی",
               "رحمت ایمانی پور",
               "جواد مقدادی",
               ],

}
