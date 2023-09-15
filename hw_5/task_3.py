# Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии


name = ['Алексей', 'Андрей', 'Игорь']
rate = [1000, 2000, 1500]
prem = ['12%', '15.5%', '9.5']


dict_ = {name[i]: rate[i]*float(prem[i][:-1])/100 for i in range(len(name))}
print(dict_)
