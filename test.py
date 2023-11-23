import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1", user="root", password="Nhattu3004", database="chatbot"
)
baitap = "TL01"
db = mydb.cursor()
query = "SELECT duongdan FROM chatbot.baitap WHERE chedo = %s"
db.execute(query, (baitap,))
baitap = db.fetchall()
file_path = baitap[0][0]
print(file_path)
try:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"Tệp tin {file_path} không tồn tại.")
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")
