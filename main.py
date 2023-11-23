from Person import Person
from Validate import validat_binary_answer
from tenforflow.keras.model import load_model

person = Person()


def Activity():
    print("Tên của bạn là gì?")
    person.setName(input())
    print(f"{person.getName()} bao nhiêu tuổi?")
    person.setAge(int(input()))
    print(f"{person.getName()} nặng bao nhiêu kg?")
    print("Nhập số kg")
    person.setWeight(float(input()))
    print(f"{person.getName()} cao bao nhiêu cm?")
    person.setHight(float(input()))
    person.setBMI()
    print(f"Chỉ số BMI của {person.getName()} là {person.getBMI()}")
    print("Trước đây bạn tập luyện thể thao với mức độ nào?")
    print("Nhập số tương ứng với lựa chọn")
    print("1. Tôi chưa tập luyện thể thao")
    print("2. Tôi tập luyện thể thao với mức độ thấp")
    print("3. Tôi tập luyện thể thao với mức độ trung bình")
    print("4. Tôi tập luyện thể thao với mức độ cao")
    person.setIntensity(int(input()))
    print("Bạn muốn tập luyện với mục đích gì?")
    print("Nhập số tương ứng với lựa chọn")
    print("1. Giảm cân")
    print("2. Giảm cân nhanh")
    print("3. Tăng cân")
    print("4. Giữ cân")
    print("5. Tăng cơ")
    person.setPhase(int(input()))
    print("Bạn muốn tư vấn về cái gì?")
    print("1. Chế độ dinh dưỡng")
    print("2. Chế độ luyện tập")
    print("3. Cả hai")
    tuvan = int(input())
    return tuvan


def predict():
    model_exe = load_model(".\model_exe.h5")
    model_diet = load_model(".\model_diet.h5")

    x = [
        person.getHight(),
        person.getWeight(),
        person.getBMI(),
        person.getIntensity(),
        person.getPhase(),
    ]

    y_exe = model_exe.predict(x)
    y_diet = model_diet.predict(x)

    return y_exe, y_diet


def recommend_exe(calo_exe, phase):
    if calo_exe < 1000 and calo_exe > 700:
        a = 1
    elif calo_exe < 1300 and calo_exe > 1000 and phase == "Maintenance":
        a = 2
    elif (
        calo_exe < 1400 and calo_exe > 1200 and phase in ["Muscle gain", "Weight gain"]
    ):
        a = 3
    elif calo_exe < 1600 and calo_exe > 1300:
        a = 4
    elif calo_exe < 1300 and calo_exe > 1100:
        a = 5
    elif calo_exe < 1600 and calo_exe > 1400:
        a = 6


def recommend_diet(calo_diet):
    if calo_diet < 2000 and calo_diet > 1700:
        a = 1
    elif calo_diet < 2300 and calo_diet > 2000:
        a = 2
    elif calo_diet < 2500 and calo_diet > 2300:
        a = 3
    elif calo_diet < 1700 and calo_diet > 1400:
        a = 4
    elif calo_diet < 1500 and calo_diet > 1300:
        a = 5


def main():
    print(
        "Xin chào, tôi là chatbot tư vấn chế độ dinh dưỡng và luyện tập cho người tập gym"
    )
    print("Để thực hiện việc tư vấn tôi cần biết một số thông tin của bạn")
    provide_info = input("Bạn có sẵn sàng cung cấp thông tin cho tôi không?")

    while True:
        if validat_binary_answer(provide_info):
            tuvan = Activity()

            calo_exe, calo_diet = predict()

            if tuvan == 1:
                b = 1
            elif tuvan == 2:
                b = 2
            else:
                b = 3

        elif not validat_binary_answer(provide_info):
            b = 1
        else:
            print("Câu trả lời không phù hợp.Bạn vui lòng nhập lại")
