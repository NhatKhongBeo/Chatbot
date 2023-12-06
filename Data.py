import mysql.connector
import json
import re


mydb = mysql.connector.connect(
    host="127.0.0.1", user="root", password="Nhattu3004", database="chatbot"
)


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
        query = "SELECT duongdan FROM chatbot.thucdon WHERE chedo = %s"
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

    print("Trước đây bạn tập luyện thể thao với mức độ nào?")
    print("Nhập số tương ứng với lựa chọn")

    count = 1
    while count <= len(tapluyen):
        print(f"{count}. {tapluyen[count-1][0]}")
        count += 1
    while True:
        try:
            tmp = int(input())
            if tmp > 0 and tmp <= len(tapluyen):
                return tmp
            else:
                print("Bạn đã nhập sai, vui lòng nhập lại")
        except:
            print("Bạn đã nhập sai, vui lòng nhập lại")


def getMucDich():
    """Lấy dữ liệu mục đích từ database"""
    db = mydb.cursor()
    query = "SELECT mota FROM chatbot.mucdich"
    db.execute(query)
    mucdich = db.fetchall()

    print("Bạn muốn tập luyện với mục đích gì?")
    print("Nhập số tương ứng với lựa chọn")

    count = 1
    while count <= len(mucdich):
        print(f"{count}. {mucdich[count-1][0]}")
        count += 1
    while True:
        try:
            tmp = int(input())
            if tmp > 0 and tmp <= len(mucdich):
                return tmp
            else:
                print("Bạn đã nhập sai, vui lòng nhập lại")
        except:
            print("Bạn đã nhập sai, vui lòng nhập lại")
