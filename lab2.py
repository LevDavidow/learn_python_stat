import library 
from texttable import Texttable
import collections
import matplotlib.pyplot as plt
import math

sample = [9.58, 24.34, 14.63, 25.71, 17.96, 28, 24.29, 29.84, 18.27, 23.12, 17.5, 18.46, 15.76, 29.74, 1.57]

def step_1_2(sample, distribution_counter): 
	library.calculate_variations_order(sample)

	#по формуле Стерджесса
	count = int(math.ceil(math.log(len(sample), 2) + 1))
	grouped = [[] for _ in range(count)]
	
	sample_min = min(sample)
	sample_max = max(sample)

	interval_size = (sample_max - sample_min) / count

	for item in sample:
		if  item <= sample_min + interval_size:
			grouped[0].append(item)

		for i in range (1, count):
			if interval_size * i < item - sample_min <= interval_size * (i + 1):
				grouped[i].append(item)

	table = Texttable()
	table.add_row(['Интервал', 'Количество'])
	for i in range(count):
		value_min = sample_min + interval_size * i
		value_max = sample_min + interval_size * (i + 1)
		table.add_row(['{value_min} - {value_max}'.format(value_min=value_min, value_max=value_max), len(grouped[i])])

	print(table.draw())
	plt.hist(sample, count)
	plt.title("Histogram")
	plt.xlabel("Value")
	plt.ylabel("Frequency")

	plt.show()

def step_3_6(sample, distribution_counter): 
	library.calculate_sample_params(sample, distribution_counter)

print('Выборка:')
print(sample)
# keys - items
# values - count of item
distribution_counter =  collections.Counter(sample)

step_1_2(sample, distribution_counter)
step_3_6(sample, distribution_counter)
