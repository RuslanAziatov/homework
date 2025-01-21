immutable_var = 1, 2, 3, "числа", True
print(immutable_var)
#immutable_var[0] = 7
print(immutable_var) # выдаст ошибку, т. к кортеж не поддерживает обращение по элементам

mutable_list = ["blue", "red", "green", "yellow"]

mutable_list[-1] = "orange"
mutable_list.extend(["white"])
mutable_list.remove("blue")
print(mutable_list)

