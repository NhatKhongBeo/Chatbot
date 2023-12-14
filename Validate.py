from unidecode import unidecode
import re
def validat_binary_answer(answer):
    acceptance_answers = ["1", "y", "Y", "yes", "có", "co"]
    decline_answers = ["0", "n", "N", "no", "không", "khong"]
    a = answer.lower()
    if any(unidecode(a)==unidecode(x) for x in acceptance_answers):
        return True
    elif any(unidecode(a)== unidecode(x) for x in decline_answers):
        return False
    else:
        return None


def check_int(input):
    try:
        return int(input)
    except ValueError:
        return ValueError("Vui lòng nhập số nguyên.")


def check_float(input):
    try:
        return float(input)
    except ValueError:
        return ValueError("Vui lòng nhập số thực.")


def check_name(input):
    try:
        if any(char.isdigit() for char in input):
            raise ValueError("Lỗi: Tên không được chứa số.")
        
        # if not re.match(r"[a-zA-ZàáâãèéêềếưửữôốơờớụủưứựA-ZÀÁÂÃÈÉÊỀẾƯỬỮÔỐƠỜỚỤỦƯỨỰ]", input):
        #     raise ValueError("Lỗi: Tên không được chứa kí tự đặc biệt.")
        if re.search(r'[!@#$%^&*(),.?":{}|<>]',input):
            raise ValueError("Lỗi: Tên không được chứa kí tự đặc biệt.")
        return input
    except ValueError as ve:
        return str(ve)
    except Exception as e:
        return e


# def check_age(input):
#     age = check_int(input)
#     if age is not None:
#         try:
#             if age < 15 or age > 60:
#                 raise ValueError("Lỗi: Tuổi không hợp lệ.")
#             return age
#         except ValueError as ve:
#             return None
def check_age(input):
    try:
        age = check_int(input)
        if isinstance(age, ValueError):
            raise ValueError("Vui lòng nhập số nguyên.")
        elif age < 15 or age > 60:
            raise ValueError("Tuổi phải lớn hơn hoặc bằng 15 và nhỏ hơn hoặc bằng 60.")
        else:
            return age
    except ValueError as ve:
        return str(ve)



def check_weight(input):
    try:
        weight = check_float(input)
        if isinstance(weight, ValueError):
            raise ValueError("Vui lòng nhập số thực.")
        elif weight < 30 or weight > 130:
                raise ValueError("Cân năng phải lớn hơn hoặc bằng 30 và nhỏ hơn hoặc bằng 130.")
        else:
            return weight
    except ValueError as ve:
        return str(ve)


def check_height(input):
    try:
        height = check_float(input)
        if isinstance(height, ValueError):
            raise ValueError("Vui lòng nhập số thực.")
        elif height < 130 or height > 220:
                raise ValueError("Chiều cao phải lớn hơn hoặc bằng 130 và nhỏ hơn hoặc bằng 220.")
        else:
            return height
    except ValueError as ve:
        return str(ve)
