#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      Administrator
#
# Created:     29/01/2021
# Copyright:   (c) Administrator 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():

# 计算资本成本率
    a = 2434
    b = 4546
    c = 0.07
    d = 0.25
    e = 0.09
###########################
    f = c*(1-d)*a/(a+b) + e*b/(a+b)

    print ("资本的总成本率（折现率）为%f\n"%f)

# 经营自由现金流折现
    g = 0.4
    h = 0.24
    w = 0.04
    i = 1000000
    j = 6
    k = 7
###########################
    sum = 0
    tem = i
    l1 = []
    l2 = []

# 第1阶段自由现金
    vq1 = (1+g)/(1+f)

    for ii in range(1,j+1):
        tem = i*(vq1**ii)
        l1.append(tem)
        sum += tem

    print("第1阶段现金流总额 %f"%sum)
    print (l1)

# 第2阶段自由现金
    i1 = tem
    vq2 = (1+h)/(1+f)

    for ii in range(1,k+1):
        tem = i1*(vq2**ii)
        l2.append(tem)
        sum += tem

    print("第2阶段现金流总额 %f"%sum)
    print (l2)

# 第3阶段自由现金
    i2 = tem
    vq3 = (1+w)/(1+f)
    sum  += (i2/(1-vq3))
    print("第3阶段现金流总额 %f  vq3 %f"%(sum,vq3))
    l = sum

# 少数股东权益占比
    m = 2
    n = 100
##########################
    o = m/(m+n)
    print("少数股东权益占比%f"%o)

# 公司股票价值
    p = 1234567
    q = 32345
    r = 222
    u = 30000000
###########################
    s = p+q+l-r
    t = s*(1-o)

    v = t/u
    print("公司股票价值 %f "%s)
    print("扣除少数股东权益的公司股票价值 %f "%t)
    print("每股股票价值 %f "%v)

    pass

if __name__ == '__main__':
    main()
