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
        db.execute(
            "SELECT duongdan FROM chatbot.thucdon WHERE matd = '{}'".format(chedoan)
        )
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
    db.execute(
        "SELECT thetrang FROM chatbot.thetrang where math='{}'".format(mathetrang)
    )
    thetrang = db.fetchall()
    return thetrang[0][0]
