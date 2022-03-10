#coding:utf-8

# In = 1/n - 5In-1

import math

if __name__ == "__main__":

    I = [math.log(1.2)] # n = 0

    for i in range(1,10):
        I.append(1.0/i - 5 * I[i-1])

    print(I)