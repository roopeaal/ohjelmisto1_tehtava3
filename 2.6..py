import random

def generate_three_digit_code():
    code = ""
    for _ in range(3):
        digit = random.randint(0, 9)
        code += str(digit)
    return code

kolmenumeroinen_koodi = generate_three_digit_code()

print(f"Kolmenumeroisen koodi: {kolmenumeroinen_koodi}")

