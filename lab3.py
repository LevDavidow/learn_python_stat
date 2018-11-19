import numpy
import matplotlib.pyplot as plt
import math 

X = [2, 6, 7 ,2, 6, 10]
Y = [2, 3, 7, 4, 6, 8]

square_X = [i * i for i in X]
square_Y = [i * i for i in Y]
XY = [X[i] * Y[i] for i in range(len(X))]

matrix = numpy.array([[sum(square_X), sum(X)], [sum(X), len(X)]])
result = numpy.array([sum(XY), sum(Y)])

answer = numpy.linalg.solve(matrix, result)

print('Функция: y = {k}x + {b}'.format(k=answer[0], b=answer[1]))

# Visual validation
# plt.plot(X, Y, 'o')
# func = lambda x: x * answer[0] + answer[1]
# plt.plot([func(i) for i in range(max(X))], '-')
# plt.show()

top = (len(X) * sum(XY) - sum(X) * sum(Y))
left = math.sqrt(len(X) * sum(square_X) - sum(X) ** 2)
right = math.sqrt(len(Y) * sum(square_Y) - sum(Y) ** 2)
r =  top / (left * right)
print('Коэфицент корелляции: {r}'.format(r=r))
