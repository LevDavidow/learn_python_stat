import library 
from texttable import Texttable
import collections
import matplotlib.pyplot as plt


sample = [1, 1, 2, 4, 2, 3, 2, 3, 3, 0, 3, 3, 0, 3, 2, 4, 1, 2, 2, 2, 1, 3, 4, 1, 3, 4, 2, 4, 1, 2]

def step_2_5(sample, distribution_counter):
	library.calculate_sample_params(sample, distribution_counter)


def step_1(sample, distribution_counter):
	library.calculate_variations_order(sample)
	print('Статистическое распределение выборки:')
	
	print('Абсолютное:')

	table = Texttable()

	table.add_row(distribution_counter.keys())
	table.add_row(distribution_counter.values())

	print(table.draw())

	print('Относительное:')
	table = Texttable()
	table.add_row(distribution_counter.keys())
	table.add_row([i / len(sample) for i in distribution_counter.values()])

	print(table.draw())

	# Генерация полигона частот
	plt.plot(distribution_counter.keys(), distribution_counter.values())
	# commented due to images
	# plt.show()


print('Выборка:')
print(sample)
# keys - items
# values - count of item
distribution_counter =  collections.Counter(sample)

step_1(sample, distribution_counter)
step_2_5(sample, distribution_counter)
