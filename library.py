from texttable import Texttable
import math
from scipy import stats

samples = [
	[1, 1, 2, 4, 2, 3, 2, 3, 3, 0],
	[3, 3, 0, 3, 2, 4, 1, 2, 2, 2],
	[1, 3, 4, 1, 3, 4, 2, 4, 1, 2]
]

q_values_95 = {
	15: 0.46,
	30: 0.28
}

def calculate_variations_order(sample): 
	print('Вариационный ряд:')
	order = sample.copy()
	order.sort()
	print(order)

def calculate_sample_params(sample, distribution_counter):
	sample_mean = sum(sample) / len(sample)
	sample_variance = sum([(i - sample_mean) ** 2 for i in sample]) / (len(sample) - 1)
	sample_standart_deviation = math.sqrt(sample_variance)

	print('Выборочная средняя:')
	print(sample_mean)

	print('Мода:')
	print(distribution_counter.most_common(1)[0][0])

	print('Медиана:')
	# поскольку выборка четная по числу элементов, то полусуммы
	order = sample.copy()
	order.sort()

	if len(order) % 2 == 0:
		target = int(len(order) / 2)
		print((order[target] + order[target + 1]) / 2)
	else:
		print(order[len(order) - 1]  / 2)
		
	print('Выборочная дисперсия')
	
	print(sample_variance)

	print('Среднеквадратичное отклонение')
	print(sample_standart_deviation)

	print('Tочечные значения')
	print('Мат ожидание:')
	print(sample_mean)
	print('Выборочная дисперсия:')
	print(sample_variance)
	print('Среднеквадратичное отклонение:')
	print(sample_standart_deviation)

	print('Интервальная оценка математического ожидания:')
	# k = n - 1
	k = len(sample) - 1
	# Среднеквадратическое отклонение известно, y = 0.95, значит
	# t.ppf - квантиль распределения стьюдента
	max_error = stats.t.ppf(0.95, k * sample_standart_deviation / math.sqrt(len(sample)))
	print((sample_mean - max_error, sample_mean + max_error))	
	print('Интервальная оценка cреднеквадратического отклонения:')
	# t.chi2 - квантиль расспределинния x2
	q =  q_values_95.get(len(sample))
	print((sample_standart_deviation - q, sample_standart_deviation + q))
	print('\n')