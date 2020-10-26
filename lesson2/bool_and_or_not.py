"""
    Логические операторы: and (и), or (или), not (не)
"""

# Выражение с успользованием оператора and истинно только тогда,
# когда истинны все операнды.

print(1 < 2 and 2 < 3)  # True
# 1 < 2 - True и 2 < 3 - True

print(1 < 2 and 2 < 3 and 3 > 4)  # False
# 1 < 2 - True и 2 < 3 - True и 3 > 4 - False


# Выражение с успользованием оператора or истинно тогда,
# когда хоть один операнд - истина.

a = 10

print(a < 0 or a == 10)  # True
# a < 0 - False или a == 10 - True

print(a == 0 or a + 2 < 3 or a > 1)  # True
# a == 0 - False или a + 2 < 3 - False или a > 1 - True


# Оператор not (не) меняет булевое значение на противоположное

print(not False)  # True
print(not True)  # False

b = -10 * 2
c = 'python'

print(not b == 20 and b < 1)  # True
# not b == 20 (екв. b != 20) - True и b < 1 - True

print(b ** 2 < 0 or not bool(c))  # False
# b ** 2 < 0 - False или not bool(c) - False

tmp_var = None
print(bool(tmp_var))  # False
print(tmp_var is None)  # True
