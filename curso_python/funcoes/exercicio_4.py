# 4 - Fizz Buzz - Se o parâmetro da função for divisivel por 3, retorne fizz, se o parâmetro da função
# for divisível por 5, retorne 5, retorne buzz. Se o parâmetro da função for divisível por 5 e por 3,
# retorne FizzBuzz, caso contrário, retorne o número enviado.

def divisor_tres_cinco(num):
  fizz = "Fizz"
  buzz = "Buzz"
  fizz_buzz = "fizz buzz"
  if num % 3 == 0 and num % 5 == 0:
    return fizz_buzz
  elif num % 3 == 0:
    return fizz
  elif num % 5 == 0:
    return buzz
  else:
    return num

print(divisor_tres_cinco(15))
print(divisor_tres_cinco(3))
print(divisor_tres_cinco(5))
print(divisor_tres_cinco(19))

