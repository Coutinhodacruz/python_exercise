# import math
#
# approx_pi = 0
# sign = 0
#
# for i in range(1, 200001):
#     approx_pi += sign * 4 / (2 * i - 1)
#     sign *= -1
#     if i == 1 or i % 10000 == 0:
#         print("Approximation after {} terms: {:.10f}".format(i, approx_pi))
#
# print("Value of π according to math.pi: {:.10f}".format(math.pi))



import math

approx_pi = 0
sign = 1

for i in range(1, 200001):
    approx_pi += sign * 4 / (2*i - 1)
    sign *= -1
    if str(approx_pi)[:7] == "3.14159":
        print("Approximation begins with 3.14159 after {} terms".format(i))
        break

print("Value of π according to math.pi: {:.10f}".format(math.pi))
