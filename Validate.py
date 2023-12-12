from unidecode import unidecode

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
        return None


def check_float(input):
    try:
        return float(input)
    except ValueError:
        return None


def check_name(input):
    try:
        if any(char.isdigit() for char in input):
            raise ValueError("Lỗi: Tên không được chứa số.")
        return input
    except ValueError as ve:
        return ve
    except Exception as e:
        return e


def check_age(input):
    age = check_int(input)
    if age is not None:
        try:
            if age < 15 or age > 60:
                raise ValueError("Lỗi: Tuổi không hợp lệ.")
            return age
        except ValueError as ve:
            return None


def check_weight(input):
    weight = check_float(input)
    if weight is not None:
        try:
            if weight < 30 or weight > 180:
                raise ValueError("Lỗi: Cân nặng không hợp lệ.")
            return weight
        except ValueError as ve:
            return None


def check_height(input):
    height = check_float(input)
    if height is not None:
        try:
            if height < 130 or height > 220:
                raise ValueError("Lỗi: Chiều cao không hợp lệ.")
            return height
        except ValueError as ve:
            return None
