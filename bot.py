from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import sqlite3
import difflib
import os

TOKEN = os.getenv("TOKEN")

# 🔹 إنشاء قاعدة البيانات والاتصال
conn = sqlite3.connect("genshin.db", check_same_thread=False)
cursor = conn.cursor()

# 🔹 إنشاء جدول الشخصيات إذا مش موجود
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

# 🔹 إضافة الشخصيات تلقائياً إذا الجدول فارغ
cursor.execute("SELECT COUNT(*) FROM characters")
if cursor.fetchone()[0] == 0:
    import add_characters  # هذا الملف مسؤول عن إضافة الشخصيات مرة واحدة فقط

# 🔹 تحديد نوع الطلب
def get_type(text):
    text = text.lower()
    if any(word in text for word in ["بيلد", "build"]):
        return "build"
    elif any(word in text for word in ["كونس", "cons"]):
        return "cons"
    elif any(word in text for word in ["باسيف", "passive"]):
        return "passive"
    elif any(word in text for word in ["موارد", "materials"]):
        return "materials"
    return None

# 🔹 جلب الأسماء
def get_names():
    cursor.execute("SELECT name, name_ar FROM characters")
    rows = cursor.fetchall()
    names = []
    for en, ar in rows:
        names.append(en)
        names.append(ar)
    return names

# 🔹 البحث الذكي
def find_character(text):
    names = get_names()
    words = text.split()
    for word in words:
        match = difflib.get_close_matches(word, names, n=1, cutoff=0.6)
        if match:
            return match[0]
    return None

# 🔹 جلب البيانات
def get_data(name):
    cursor.execute("""
    SELECT build, cons, passive, materials
    FROM characters
    WHERE name=? OR name_ar=?
    """, (name, name))
    return cursor.fetchone()

# 🔹 الرد
async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    req = get_type(text)
    if not req:
        return

    char = find_character(text)
    if not char:
        await update.message.reply_text("❌ ما فهمت اسم الشخصية")
        return

    data = get_data(char)
    if not data:
        await update.message.reply_text("❌ الشخصية مش موجودة")
        return

    index = ["build", "cons", "passive", "materials"].index(req)
    link = data[index]

    if link:
        await update.message.reply_photo(link)
    else:
        await update.message.reply_text("❌ ما ضفت صورة لهالمطلب")

# 🔹 تشغيل البوت
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle))
app.run_polling()
