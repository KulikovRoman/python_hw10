# Задание 44
# В ячейке ниже представлен код генерирующий DataFrame,
# которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид.
# Сможете ли вы это сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI'lst})
# data. Head() |

# импортируем нужные библиотеки
import random
import pandas as pd

# создаем список и перемешиваем его
lst = ["robot"] * 10
lst += ["human"] * 10
random.shuffle(lst)

# создаем DataFrame из списка
data = pd.DataFrame({"whoAmI": lst})

# создаем словарь для one hot encoding
one_hot_dict = {"robot": [1, 0], "human": [0, 1]}

# создаем новый DataFrame с one hot encoding
new_data = pd.DataFrame(
    data["whoAmI"].apply(lambda x: one_hot_dict[x]).tolist(), columns=["robot", "human"]
)

# объединяем старый и новый DataFrame
result = pd.concat([data, new_data], axis=1)

# выводим результат
print(result.head())


# Результат
#   whoAmI  robot  human
# 0  human      0      1
# 1  robot      1      0
# 2  human      0      1
# 3  robot      1      0
# 4  human      0      1
