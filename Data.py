import mysql.connector
import json
import re


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="huyinit",
    database="chtdttt"
)

class Data:
    def __init__(self) -> None:
        self.cacbaitap=[]
        self.chedoan=[]

    def converBaitap(self, baitap):
        """Lấy dữ liệu bài tập từ database"""
        db=mydb.cursor()
        db.execute("SELECT baiitap FROM chatbot.baitap WHERE chedo = '{baitap}'")
        baitap=db.fetchall()

        for i in baitap:
            self.cacbaitap.append(i[2])
    
    def converChedoan(self, chedoan):
        """Lấy dữ liệu chế độ ăn từ database"""
        db=mydb.cursor()
        db.execute("SELECT chedoan FROM chatbot.chedoan WHERE chedo = '{chedoan}'")
        chedoan=db.fetchall()

        for i in chedoan:
            self.chedoan.append(i[2])
    
    def getCacbaitap(self):
        return self.cacbaitap
    
    def getChedoan(self):
        return self.chedoan

def getThetrang(mathetrang):
    """Lấy dữ liệu thể trạng từ database"""
    db=mydb.cursor()
    db.execute("SELECT thetrang FROM chatbot.thetrang where math='{mathetrang}'")
    thetrang=db.fetchall()
    return thetrang