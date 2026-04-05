import sqlite3

conn = sqlite3.connect("genshin.db")
cursor = conn.cursor()

# 1. مسح البيانات القديمة لضمان التحديث
cursor.execute("DELETE FROM characters")

# 2. إدخال بيانات الشخصيات الجديدة بالصور (File IDs)
# الترتيب: (الاسم الإنجليزي، الاسم العربي، بيلد، كونس، باسيف، موارد)
characters_with_images = [
    # بيانات شخصية نيفير
    ("nevir", "نيفير", 
     "AgACAgQAAxkBAAIWjGnS0YFzLjT3xNdMhDRqSGvrlWOvAAKUDWsbpn-ZUtwCBzji__19AQADAgADcwADOwQ", # بيلد
     "AgACAgQAAxkBAAIWhWnS0WqJcPauJ_PvKs3TQc-RwO8_AAKTDWsbpn-ZUgHLwtfUXtN8AQADAgADcwADOwQ", # كونس
     "", # (باسيف - اتركها فارغة إذا لم يتوفر ID)
     "AgACAgQAAxkBAAIWg2nS0V9lKR3Y1UbjONi5WWdX79cqAAKSDWsbpn-ZUlH8H6nhgDP3AQADAgADcwADOwQ"  # موارد
    ),
    
    # بيانات شخصية لاوما
    ("lauma", "لاوما", 
     "AgACAgQAAxkBAAIWfmnS0SCfVWRyZV4H9Qb6OH5J3v5hAAKQDWsbpn-ZUstDI3FhHTTSAQADAgADcwADOwQ", # بيلد
     "AgACAgQAAxkBAAIWf2nS0SBWZGDD0EGtw0eE1BiaNplJAAKRDWsbpn-ZUmegzoDw42EtAQADAgADcwADOwQ", # كونس
     "", # (باسيف)
     "AgACAgQAAxkBAAIWfWnS0SDiWNZR34FzyIy7i30r3vw5AAKPDWsbpn-ZUj-gDNuoSQ3RAQADAgADcwADOwQ"  # موارد
    )
]

# 3. بقية قائمة الشخصيات (بدون صور حالياً)
other_characters = [
    ("aino", "آينو"), ("albedo", "ألبيدو"), ("alhaitham", "الهيثم"), ("amber", "امبر"),
    ("itto", "إيتو"), ("arlekino", "ارليكينو"), ("baizhu", "بايجو"), ("barbara", "باربارا"),
    ("beidou", "بيدو"), ("bennett", "بينت"), ("candace", "كانديس"), ("charlotte", "شارلوت"),
    ("chasca", "تشاسكا"), ("chiori", "شيوري"), ("chever", "شيفروز"), ("citlali", "سيتلالي"),
    ("chongyun", "تشونغيون"), ("collei", "كولي"), ("chlorine", "كلوريند"), ("columbina", "كولومبينا"),
    ("cyno", "ساينو"), ("dalia", "داليا"), ("dehya", "ديهيا"), ("dori", "دوري"),
    ("diluc", "ديلوك"), ("dorin", "دورين"), ("diona", "ديونا"), ("emily", "ايميلي"),
    ("escoffier", "إسكوفيير"), ("eula", "إيولا"), ("faruzan", "فاروزان"), ("flenz", "فلينز"),
    ("fischl", "فيشل"), ("furina", "فورينا"), ("ferment", "فيرمنت"), ("gamnj", "غامنج"),
    ("ganyu", "غانيو"), ("gorou", "غورو"), ("hutao", "هوتاو"), ("eva", "ايفا"),
    ("enifa", "إنيفا"), ("iloga", "إيلوغا"), ("iansan", "إيانسان"), ("jahuda", "جاهودا"),
    ("jean", "جين"), ("kazuha", "كازوها"), ("katchina", "كاتشينا"), ("kaeya", "كايا"),
    ("ayato", "أياتو"), ("ayaka", "أياكا"), ("kaveh", "كافيه"), ("keqing", "كيتشنغ"),
    ("kinich", "كينيتش"), ("klee", "كلي"), ("kirara", "كيرارا"), ("kujou_sara", "سارا"),
    ("kuki", "كوكي"), ("lanya", "لان يان"), ("layla", "ليلى"), ("linya", "لينيا"),
    ("lisa", "ليزا"), ("lyney", "ليني"), ("lynette", "لينت"), ("mavuika", "مافويكا"),
    ("mona", "مونا"), ("mika", "ميكا"), ("molani", "مولاني"), ("nahida", "ناهيدا"),
    ("navia", "نافيا"), ("neuvillette", "نيوفيليت"), ("noelle", "نويل"),
    ("nilou", "نيلو"), ("ningguang", "نينغ وانغ"), ("qiqi", "تشي تشي"), ("auroron", "اورورون"),
    ("raiden", "رايدن شوغن"), ("razor", "ريزر"), ("kokomi", "كوكومي"), ("rosaria", "روزاريا"),
    ("sithos", "سيثوس"), ("sayu", "سايو"), ("shenhe", "شينهي"), ("skirk", "سكيرك"),
    ("haizo", "هايزو"), ("sejuin", "سيجوين"), ("sucrose", "سكروز"), ("childe", "تشايلد"),
    ("tighnari", "تايناري"), ("thoma", "توما"), ("varka", "فاركا"), ("farisa", "فاريسا"),
    ("venti", "فينتي"), ("wanderer", "سكارا"), ("wriothesley", "ريزلي"), ("xiangling", "شانغلينغ"),
    ("shanion", "شانيون"), ("xiao", "شاو"), ("xingqiu", "شينغشو"), ("shilonin", "شيلونين"),
    ("miko", "ميكو"), ("xinyan", "شينيان"), ("yaoyao", "ياوياو"), ("yelan", "يلان"),
    ("yanfei", "يانفي"), ("yoimiya", "يويميا"), ("mizuki", "ميزوكي"), ("zhongli", "جونغلي"),
    ("yunjin", "يونجين"), ("zebai", "زيباي"),
]

# إدخال الشخصيات التي لها صور
for data in characters_with_images:
    cursor.execute("INSERT INTO characters VALUES (?, ?, ?, ?, ?, ?)", data)

# إدخال بقية الشخصيات بدون صور
for char in other_characters:
    cursor.execute("INSERT INTO characters VALUES (?, ?, '', '', '', '')", char)

conn.commit()
conn.close()

print("✅ تم تحديث بيانات نيفير ولاوما بنجاح!")
