n = int(input())
l = []
for x in range(n):
    state = input()
    percent_cigarette_smokers = float(input())
    cases = float(input())
    tup = (state , percent_cigarette_smokers , cases)
    l += [tup]


sum_x = 0
sum_y = 0
sum_x_square = 0
sum_y_square = 0
sum_xy = 0

for i in l:
    sum_x += i[1]
    sum_y += i[2]
    sum_x_square += i[1]**2
    sum_y_square += i[2]**2
    sum_xy += i[1]*i[2]



p = (n*sum_xy - sum_x*sum_y)/(((n*sum_x_square) - (sum_x)**2)*((n*sum_y_square) - (sum_y)**2))**(1/2)
print(str(p)[0:4])
