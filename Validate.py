def validat_binary_answer(answer):
    acceptance_answers = ['1','y','Y','yes','có','co']
    decline_answers = ['0','n','N','no','không','khong']
    answer = answer.lower()
    if answer in acceptance_answers:
        return True
    elif answer in decline_answers:
        return False
    else:
        return None
    