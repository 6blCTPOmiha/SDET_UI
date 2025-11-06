import random


class StaticFunctions:
    def __init__(self):
        pass


    @staticmethod
    def post_code_gen():
        post_code = ''.join(str(random.randint(0, 9)) for _ in range(10))
        return post_code


    @staticmethod
    def first_name_calc(post_code):
        chunks = [post_code[i:i + 2] for i in range(0, 10, 2)]
        letters = ''
        for chunk in chunks:
            good_number = int(chunk) % 26
            letters += chr(97 + good_number)  # 97 - код буквы 'a' в ASCII
        return letters


    @staticmethod
    def chunks_to_names(customers):
        customer_count = len(customers)
        names = []
        for i in range(0, customer_count, 3):
            names.append(customers[i].text)
        return names


    @staticmethod
    def math_round(x):
        return round(x + 0.05 if x >= 0 else x - 0.05, 1)


    @staticmethod
    def calc_sr_ar(names):
        k = 0
        summ = 0
        for name in names:
            k += 1
            summ += len(name)
        return summ / k


    @staticmethod
    def calc_mid_len_name(names, sr_ar):
        length = []
        for i in range(len(names)):
            length.append(len(names[i]))
        diff = [abs(l - sr_ar) for l in length]
        min_dif = min(diff)
        right_i = diff.index(min_dif)
        return right_i
