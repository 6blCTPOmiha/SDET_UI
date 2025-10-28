import random


class Functions:
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
