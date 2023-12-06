from Person import Person
from Validate import *
from tensorflow.keras.models import load_model
from Data import *

person = Person()
data = Data()


def Activity():
    print("Tên của bạn là gì?")
    while True:
        name = input()
        if check_name(name) == name:
            person.setName(name)
            break
        else:
            print("Tên nhập không hợp vệ, vui lòng nhập lại\n")

    print(f"{person.getName()} bao nhiêu tuổi?\n")
    while True:
        age = check_age(input())
        if age is not None:
            person.setAge(age)
            break
        else:
            print("Tuổi nhập không hợp vệ, vui lòng nhập lại\n")

    print(f"{person.getName()} nặng bao nhiêu kg?")
    while True:
        print("Nhập số kg\n")
        weight = check_weight(input())
        if weight is not None:
            person.setWeight(weight)
            break
        else:
            print("Cân nặng nhập không hợp vệ, vui lòng nhập lại\n")

    print(f"{person.getName()} cao bao nhiêu cm?")
    while True:
        height = check_height(input())
        if height is not None:
            person.setHight(height)
            break
        else:
            print("Chiều cao nhập không hợp vệ, vui lòng nhập lại\n")

    person.setBMI()
    print(f"Chỉ số BMI của {person.getName()} là {person.getBMI()}")
    matt = mathetrang(person.getBMI())
    print(f"{person.getName()} đang có thể trạng là: {getThetrang(matt)}")

    tmp = getTapLuyen()
    person.setIntensity(tmp)

    tmp = getMucDich()
    person.setPhase(tmp)

    print("Bạn muốn tư vấn về cái gì?")
    print("1. Chế độ dinh dưỡng")
    print("2. Chế độ luyện tập")
    print("3. Cả hai")
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

    y_exe = model_exe.predict(x)
    y_diet = model_diet.predict(x)

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
    print(
        """Theo như thông tin bạn cung cấp, tôi đã tìm được 
        chế độ ăn phù hợp cho bạn như sau:"""
    )
    while len(chedoan) > 0:
        chedo = chedoan.pop()
        print(chedo)
        print("Bạn đã hài lòng với thực đơn này chưa?")
        print("1. Rồi")
        print("2. Tôi muốn xem thực đơn khác")
        if int(input()) == 1:
            print("Cảm ơn bạn đã sử dụng dịch vụ của chúng tôi")
            break
    print("Hiện tại chúng tôi đã hết những thực đơn phù hợp với bạn")
    print("Xin lỗi vì không thể đáp ứng được nhu cầu của bạn")
    print("Cảm ơn bạn đã sử dụng dịch vụ của chúng tôi")


def Recommend_respon_exe(cacbaitap):
    print(
        """Theo như thông tin bạn cung cấp, tôi đã tìm được 
chế độ tập luyện phù hợp cho bạn như sau:"""
    )
    while len(cacbaitap) > 0:
        baitap = cacbaitap.pop()
        print(baitap)
        print("Bạn có thấy bài tập này phù hợp với bạn không?")
        print("1. Rồi")
        print("2. Tôi muốn xem lịch tập khác")
        if int(input()) == 1:
            print("Cảm ơn bạn đã sử dụng dịch vụ của chúng tôi")
            break
    print("Hiện tại chúng tôi đã hết những thực đơn phù hợp với bạn")
    print("Xin lỗi vì không thể đáp ứng được nhu cầu của bạn")
    print("Cảm ơn bạn đã sử dụng dịch vụ của chúng tôi")


def Recommend_respon_both(cacbaitap, chedoan):
    print(
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
                print(
                    "Hiện tại chúng tôi đã hết những thực đơn và bài tập phù hợp với bạn"
                )
                print("Xin lỗi vì không thể đáp ứng được nhu cầu của bạn")
                break
        if tmp == 2:
            try:
                baitap = cacbaitap.pop()
            except IndexError:
                print("Hiện tại chúng tôi đã hết những bài tập phù hợp với bạn")
                print("Xin lỗi vì không thể đáp ứng được nhu cầu của bạn")
                break
        if tmp == 3:
            try:
                chedo = chedoan.pop()
            except IndexError:
                print("Hiện tại chúng tôi đã hết những thực đơn phù hợp với bạn")
                print("Xin lỗi vì không thể đáp ứng được nhu cầu của bạn")
                break
        print(baitap)
        print(chedo)
        print("Bạn có hài lòng với sự tư vấn không")
        print("1. Rồi")
        print("2. Tôi muốn xem lịch tập khác")
        print("3. Tôi muốn xem thực đơn khác")
        i = int(input())
        if i == 1:
            print("Cảm ơn bạn đã sử dụng dịch vụ của chúng tôi")
            break
        elif i == 2:
            tmp = 2
        elif i == 3:
            tmp = 3
    print("Cảm ơn quý khách đã sử dụng dịch vụ của chúng tôi")
    


def main():
    data = Data()
    person= Person()
    while True:
        print(
        "Xin chào, tôi là chatbot tư vấn chế độ dinh dưỡng và luyện tập cho người tập gym"
    )
        print("Để thực hiện việc tư vấn tôi cần biết một số thông tin của bạn")
        provide_info = input("Bạn có sẵn sàng cung cấp thông tin cho tôi không?\n")
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

        elif not validat_binary_answer(provide_info):
            b = 1
        else:
            print("Câu trả lời không phù hợp.Bạn vui lòng nhập lại")


if __name__ == "__main__":
    main()
