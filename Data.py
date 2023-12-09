import mysql.connector
import json
import re
import time

mydb = mysql.connector.connect(
    host="127.0.0.1", user="root", password="Nhattu3004", database="chatbot"
)


def generate_message(message):
    for line in message.split("\n"):
        for char in line:
            print(char, end="", flush=True)
            time.sleep(0.01)
        print()


class Data:
    def __init__(self) -> None:
        self.cacbaitap = []
        self.chedoan = []

    def converBaitap(self, baitap):
        """Lấy dữ liệu bài tập từ database"""
        db = mydb.cursor()
        query = "SELECT duongdan FROM chatbot.baitap WHERE chedo = %s"
        db.execute(query, (baitap,))
        baitap = db.fetchall()
        for i in baitap:
            self.cacbaitap.append(i[0])

    def converChedoan(self, chedoan):
        """Lấy dữ liệu chế độ ăn từ database"""
        db = mydb.cursor()
        query = "SELECT duongdan FROM chatbot.thucdon WHERE matd = %s"
        db.execute(query, (chedoan,))
        chedoan = db.fetchall()
        for i in chedoan:
            self.chedoan.append(i[0])

    def getCacbaitap(self):
        return self.cacbaitap

    def getChedoan(self):
        return self.chedoan


def getThetrang(mathetrang):
    """Lấy dữ liệu thể trạng từ database"""
    db = mydb.cursor()
    query = "SELECT thetrang FROM chatbot.thetrang WHERE math = %s"
    db.execute(query, (mathetrang,))
    thetrang = db.fetchall()
    return thetrang[0][0]


def getTapLuyen():
    """Lấy dữ liệu tập luyện từ database"""
    db = mydb.cursor()
    query = "SELECT mota FROM chatbot.muctapluyen"
    db.execute(query)
    tapluyen = db.fetchall()

    generate_message("Trước đây bạn tập luyện thể thao với mức độ nào?")
    generate_message("Nhập số tương ứng với lựa chọn")

    count = 1
    while count <= len(tapluyen):
        generate_message(f"{count}. {tapluyen[count-1][0]}")
        count += 1
    while True:
        try:
            tmp = int(input())
            if tmp > 0 and tmp <= len(tapluyen):
                return tmp
            else:
                generate_message("Bạn đã nhập sai, vui lòng nhập lại")
        except:
            generate_message("Bạn đã nhập sai, vui lòng nhập lại")


def getMucDich():
    """Lấy dữ liệu mục đích từ database"""
    db = mydb.cursor()
    query = "SELECT mota FROM chatbot.mucdich"
    db.execute(query)
    mucdich = db.fetchall()

    generate_message("Bạn muốn tập luyện với mục đích gì?")
    generate_message("Nhập số tương ứng với lựa chọn")

    count = 1
    while count <= len(mucdich):
        generate_message(f"{count}. {mucdich[count-1][0]}")
        count += 1
    while True:
        try:
            tmp = int(input())
            if tmp > 0 and tmp <= len(mucdich):
                return tmp
            else:
                generate_message("Bạn đã nhập sai, vui lòng nhập lại")
        except:
            generate_message("Bạn đã nhập sai, vui lòng nhập lại")
