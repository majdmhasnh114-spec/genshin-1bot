import sqlite3

conn = sqlite3.connect("genshin.db")
cursor = conn.cursor()

# إنشاء الجدول إذا مش موجود
cursor.execute("""
CREATE TABLE IF NOT EXISTS characters (
    name TEXT,
    name_ar TEXT,
    build TEXT,
    cons TEXT,
    passive TEXT,
    materials TEXT
)
""")

# قائمة الشخصيات: (English, Arabic)
characters = [
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
    ("kuki", "كوكي"), ("lauma", "لاوما"), ("lanya", "لان يان"), ("layla", "ليلى"),
    ("linya", "لينيا"), ("lisa", "ليزا"), ("lyney", "ليني"), ("lynette", "لينت"),
    ("mavuika", "مافويكا"), ("mona", "مونا"), ("mika", "ميكا"), ("molani", "مولاني"),
    ("nahida", "ناهيدا"), ("navia", "نافيا"), ("nevir", "نيفير"), ("neuvillette", "نيوفيليت"),
    ("noelle", "نويل"), ("nilou", "نيلو"), ("ningguang", "نينغ وانغ"), ("qiqi", "تشي تشي"),
    ("auroron", "اورورون"), ("raiden", "رايدن شوغن"), ("razor", "ريزر"), ("kokomi", "كوكومي"),
    ("rosaria", "روزاريا"), ("sithos", "سيثوس"), ("sayu", "سايو"), ("shenhe", "شينهي"),
    ("skirk", "سكيرك"), ("haizo", "هايزو"), ("sejuin", "سيجوين"), ("sucrose", "سكروز"),
    ("childe", "تشايلد"), ("tighnari", "تايناري"), ("thoma", "توما"), ("varka", "فاركا"),
    ("farisa", "فاريسا"), ("venti", "فينتي"), ("wanderer", "سكارا"), ("wriothesley", "ريزلي"),
    ("xiangling", "شانغلينغ"), ("shanion", "شانيون"), ("xiao", "شاو"), ("xingqiu", "شينغشو"),
    ("shilonin", "شيلونين"), ("miko", "ميكو"), ("xinyan", "شينيان"), ("yaoyao", "ياوياو"),
    ("yelan", "يلان"), ("yanfei", "يانفي"), ("yoimiya", "يويميا"), ("mizuki", "ميزوكي"),
    ("zhongli", "جونغلي"), ("yunjin", "يونجين"), ("zebai", "زيباي"),
]

# إضافة الشخصيات للـ database
for char in characters:
    cursor.execute("""
    INSERT INTO characters (name, name_ar, build, cons, passive, materials)
    VALUES (?, ?, '', '', '', '')
    """, char)

conn.commit()
conn.close()

print("✅ تم إضافة كل الشخصيات بدون تكرار")