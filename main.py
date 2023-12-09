import sys

original_stdout = sys.stdout
original_stderr = sys.stderr


class DummyFile:
    def write(self, x):
        pass
    def flush(self):
        pass
    def close(self):
        pass

sys.stdout = DummyFile()
sys.stderr = DummyFile()

from Person import Person
from Validate import *
import os

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import warnings

warnings.filterwarnings("ignore")
warnings.filterwarnings("ignore", category=DeprecationWarning, module="tensorflow")

from tensorflow.keras.models import load_model
from Data import *
import time

import tensorflow as tf

person = Person()
data = Data()
sys.stdout = original_stdout
sys.stderr = original_stderr


def generate_message(message):
    for line in message.split("\n"):
        for char in line:
            print(char, end="", flush=True)
            time.sleep(0.01)
        print()


def Activity():
    generate_message("Tên của bạn là gì?")
    while True:
        name = input()
        if check_name(name) == name:
            person.setName(name)
            break
        else:
            generate_message("Tên nhập không hợp vệ, vui lòng nhập lại")
    generate_message(f"{person.getName()} bao nhiêu tuổi?")
    while True:
        age = check_age(input())
        if age is not None:
            person.setAge(age)
            break
        else:
            generate_message("Tuổi nhập không hợp vệ, vui lòng nhập lại")
    generate_message(f"{person.getName()} nặng bao nhiêu kg?")
    while True:
        generate_message("Nhập số kg")
        weight = check_weight(input())
        if weight is not None:
            person.setWeight(weight)
            break
        else:
            generate_message("Cân nặng nhập không hợp vệ, vui lòng nhập lại")
    generate_message(f"{person.getName()} cao bao nhiêu cm?")
    while True:
        height = check_height(input())
        if height is not None:
            person.setHight(height)
            break
        else:
            time.sleep(1)
            generate_message("Chiều cao nhập không hợp vệ, vui lòng nhập lại")

    person.setBMI()

    generate_message(f"Chỉ số BMI của {person.getName()} là {person.getBMI():.2f}")
    matt = mathetrang(person.getBMI())
    time.sleep(1)
    generate_message(f"{person.getName()} đang có thể trạng là: {getThetrang(matt)}")

    tmp = getTapLuyen()
    person.setIntensity(tmp)

    tmp = getMucDich()
    person.setPhase(tmp)
    time.sleep(1)
    generate_message(
        """Bạn muốn tư vấn về vấn đề gì?
1. Chế độ dinh dưỡng
2. Chế độ luyện tập
3. Cả hai
"""
    )
    tuvan = int(input())
    return tuvan


def mathetrang(bmi):
    if bmi < 18.5:
        return "TT01"
    elif bmi < 25:
        return "TT02"
    elif bmi < 30:
        return "TT03"
    elif bmi < 35:
        return "TT04"
    elif bmi < 40:
        return "TT05"
    else:
        return "TT06"


def predict():
    model_exe = load_model(".\model_exe.h5")
    model_diet = load_model(".\model_diet.h5")

    x = [
        [
            person.getHight(),
            person.getWeight(),
            person.getBMI(),
            person.getIntensity(),
            person.getPhase(),
        ]
    ]

    y_exe = model_exe.predict(x, verbose=0)
    y_diet = model_diet.predict(x, verbose=0)

    return y_exe, y_diet


# def recommend_exe(calo_exe, phase):
#     if calo_exe < 1100:
#         che_do_exe = "TL01"
#     elif calo_exe < 1300 and calo_exe > 1000 and phase == "Maintenance":
#         che_do_exe = "TL04"
#     elif (
#         calo_exe < 1400 and calo_exe > 1200 and phase in ["Muscle gain", "Weight gain"]
#     ):
#         che_do_exe = "TL03"
#     elif calo_exe < 1500 and calo_exe > 1300:
#         che_do_exe = "TL03"
#     elif calo_exe < 1300 and calo_exe > 1100:
#         che_do_exe = "TL02"
#     elif calo_exe > 1600:
#         che_do_exe = "TL05"


#     data.converBaitap(che_do_exe)
#     list_exe = []
#     for i in data.getCacbaitap():
#         with open(i, "r") as f:
#             list_exe.append(f.read())
#     return list_exe
def recommend_exe(calo_exe, phase):
    if calo_exe < 1100:
        che_do_exe = "TL01"
    elif 1100 < calo_exe < 1300 and phase == "Maintenance":
        che_do_exe = "TL04"
    elif 1200 < calo_exe < 1400 and phase in ["Muscle gain", "Weight gain"]:
        che_do_exe = "TL03"
    elif 1300 < calo_exe < 1500:
        che_do_exe = "TL03"
    elif 1100 < calo_exe < 1300:
        che_do_exe = "TL02"
    elif calo_exe > 1500:
        che_do_exe = "TL05"

    data.converBaitap(che_do_exe)
    list_exe = []
    for i in data.getCacbaitap():
        with open(i, "r", encoding="utf-8", errors="replace") as f:
            list_exe.append(f.read())
    return list_exe


def recommend_diet(calo_diet):
    if calo_diet < 2300 and calo_diet > 1800:
        diet = "DI04"
    elif calo_diet < 2600 and calo_diet > 2300:
        diet = "DI03"
    elif calo_diet < 1800 and calo_diet > 1600:
        diet = "DI02"
    elif calo_diet < 1600 and calo_diet > 1400:
        diet = "DI01"

    data.converChedoan(diet)

    list_diet = []
    for i in data.getChedoan():
        with open(i, "r", encoding="utf-8", errors="replace") as f:
            list_diet.append(f.read())
    return list_diet


def Recommend_respon_diet(chedoan):
    generate_message(
        """Theo như thông tin bạn cung cấp, tôi đã tìm được 
chế độ ăn phù hợp cho bạn như sau:"""
    )
    while len(chedoan) > 0:
        chedo = chedoan.pop()
        generate_message(chedo)
        generate_message("Bạn đã hài lòng với thực đơn này chưa?")
        generate_message("1. Rồi")
        generate_message("2. Tôi muốn xem thực đơn khác")
        if int(input()) == 1:
            generate_message("Cảm ơn bạn đã sử dụng dịch vụ của chúng tôi")
            return
    generate_message("Hiện tại chúng tôi đã hết những thực đơn phù hợp với bạn")
    generate_message("Xin lỗi vì không thể đáp ứng được nhu cầu của bạn")
    generate_message("Cảm ơn bạn đã sử dụng dịch vụ của chúng tôi")


def Recommend_respon_exe(cacbaitap):
    generate_message(
        """Theo như thông tin bạn cung cấp, tôi đã tìm được 
chế độ tập luyện phù hợp cho bạn như sau:"""
    )
    while len(cacbaitap) > 0:
        baitap = cacbaitap.pop()
        generate_message(baitap)
        generate_message("Bạn có thấy bài tập này phù hợp với bạn không?")
        generate_message("1. Rồi")
        generate_message("2. Tôi muốn xem lịch tập khác")
        if int(input()) == 1:
            generate_message("Cảm ơn bạn đã sử dụng dịch vụ của chúng tôi")
            return
    generate_message("Hiện tại chúng tôi đã hết những thực đơn phù hợp với bạn")
    generate_message("Xin lỗi vì không thể đáp ứng được nhu cầu của bạn")
    generate_message("Cảm ơn bạn đã sử dụng dịch vụ của chúng tôi")


def Recommend_respon_both(cacbaitap, chedoan):
    generate_message(
        """Theo như thông tin bạn cung cấp, tôi đã tìm được
chế độ tập luyện và chế độ ăn uống phù hợp cho bạn như sau:"""
    )
    tmp = 1
    chedo = """"""
    baitap = """"""
    while len(cacbaitap) > 0 or not len(chedoan) > 0:
        if tmp == 1:
            try:
                baitap = cacbaitap.pop()
                chedo = chedoan.pop()
            except IndexError:
                generate_message(
                    "Hiện tại chúng tôi đã hết những thực đơn và bài tập phù hợp với bạn"
                )
                generate_message("Xin lỗi vì không thể đáp ứng được nhu cầu của bạn")
                break
        if tmp == 2:
            try:
                baitap = cacbaitap.pop()
            except IndexError:
                generate_message(
                    "Hiện tại chúng tôi đã hết những bài tập phù hợp với bạn"
                )
                generate_message("Xin lỗi vì không thể đáp ứng được nhu cầu của bạn")
                break
        if tmp == 3:
            try:
                chedo = chedoan.pop()
            except IndexError:
                generate_message(
                    "Hiện tại chúng tôi đã hết những thực đơn phù hợp với bạn"
                )
                generate_message("Xin lỗi vì không thể đáp ứng được nhu cầu của bạn")
                break
        generate_message(baitap)
        generate_message(chedo)
        # generate_message(baitap)
        # generate_message(chedo)
        generate_message("Bạn có hài lòng với sự tư vấn không")
        generate_message("1. Rồi")
        generate_message("2. Tôi muốn xem lịch tập khác")
        generate_message("3. Tôi muốn xem thực đơn khác")
        i = int(input())
        if i == 1:
            generate_message("Cảm ơn bạn đã sử dụng dịch vụ của chúng tôi")
            break
        elif i == 2:
            tmp = 2
        elif i == 3:
            tmp = 3
    generate_message("Cảm ơn quý khách đã sử dụng dịch vụ của chúng tôi")


def main():
    data = Data()
    person = Person()
    while True:
        generate_message(
            "Xin chào, tôi là chatbot tư vấn chế độ dinh dưỡng và luyện tập cho người tập gym"
        )
        generate_message(
            "Để thực hiện việc tư vấn tôi cần biết một số thông tin của bạn"
        )
        generate_message("Bạn có sẵn sàng cung cấp thông tin cho tôi không?")
        provide_info = input()
        if validat_binary_answer(provide_info):
            tuvan = Activity()
            calo_exe, calo_diet = predict()
            cacbaitap = recommend_exe(calo_exe, person.getPhase())
            chedoan = recommend_diet(calo_diet)
            if tuvan == 1:
                Recommend_respon_diet(chedoan)
            elif tuvan == 2:
                Recommend_respon_exe(cacbaitap)
            else:
                Recommend_respon_both(cacbaitap, chedoan)
            break
        elif not validat_binary_answer(provide_info):
            tmp = """Nếu không cung cấp thông tin, chung tôi sẽ không thể tư vấn cho bạn
Xin cảm ơn bạn đã đến với hệ thống của chúng thôi
Chúc bạn một ngày tốt lành"""
            generate_message(tmp)
            break
        else:
            generate_message("Câu trả lời không phù hợp.Bạn vui lòng nhập lại")


if __name__ == "__main__":
    main()
