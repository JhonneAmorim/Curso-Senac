# Try, except, else e finally

# a = 18
# b = 0
# c = a / b

# try:
#     a = 18
#     b = 0
#     # print(b[0])
#     # print('Linha 1'[1000])
#     c = a / b
#     print('Linha 2')
# except ZeroDivisionError as e:
#     print(e.__class__.__name__)
#     print(e)
# except NameError:
#     print('Nome b não está definido')
#     print('Linha 2')
# except (TypeError, IndexError) as error:
#     # print('Type Error + IndexError')
#     print('Nome', error.__class__.__name__)
# except Exception:
#     print('ERRO Desconhecido')


# print('Continuar')


try:
    print('Abrir Arquivo')
    # 8/0
except ZeroDivisionError as e:
    print(e)
else:
    print('Não deu error')
finally:
    print('Fechar Arquivo')
