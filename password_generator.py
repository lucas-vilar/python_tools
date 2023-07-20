import random
import string

valores = string.ascii_letters + string.digits + "!@#$%&?"

print(f"The password is: {''.join(random.SystemRandom().choice(valores) for i in range(0,16))}")