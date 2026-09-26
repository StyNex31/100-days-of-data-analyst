#
#
#
# def is_adult(age):
#     if age >= 18:
#         return True
#     else:
#         return False
#
# print(is_adult(30))
#
#


def discount_price(price, percent):
    discount = price * (1 - (percent/100))
    return discount

print(discount_price(100, 10))