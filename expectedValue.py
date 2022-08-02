khanaen = [0,1,2,3,4,5,6,7,8,9,10] # ค่าคะแนน ไล่ตั้งแต่ 0 ถึง 10
mi = [7,0,1,0,9,11,5,6,7,3,1] # แต่ละคะแนนมีคนได้กี่คน
n = sum(mi) # จำนวนรวมมี 50 คน
X =[]
khanaen_ruam = 0
for i in range(11):
    khanaen_ruam += khanaen[i]*mi[i]
    # print(khanaen_ruam)
    X.append(khanaen[i])
E = khanaen_ruam/n
print('ค่าคาดหมาย =', E) # ได้ ค่าคาดหมาย = 5.16

# sum = x[i]*y[i]
# E = sum/n
    
print(X)

ruam = 0
for i in range(11):
    print("X-E(X)", i, khanaen[i]-E)
    print("X-E(X)**2 =", (khanaen[i]-E)**2)
    print((khanaen[i]-E)**2, "*", mi[i], "=", ((khanaen[i]-E)**2)*mi[i])
    ruam += ((khanaen[i]-E)**2)*mi[i]
    print("ruam=", ruam)
    print("")
V = ruam/n

# สมการ V(X) = E((X-E)**2)
# v = sum((x[i]-E)**2)*y[i]
# V = v**0.5

print('ความแปรปรวน =', V) # ได้ ความแปรปรวน = 7.1344
# ส่วนค่าส่วนเบี่ยงเบนมาตรฐาน มักเขียนแทนด้วย σ (ซิกมาเล็ก) คือรากที่สองของความแปรปรวน
σ = V**0.5
print('ส่วนเบี่ยงเบนมาตรฐาน =', σ) # ได้ ส่วนเบี่ยงเบนมาตรฐาน = 2.671029763967448

print(64**0.5)
print(σ**2)

import numpy as np
import math

print(math.log(1)) # 0.0
print(np.exp(math.log(1))) # 1.0

print(np.exp(math.log(1)*0.5)) # 1.0
print(np.exp(math.log(1**0.5))) # 1.0
print(1**0.5) # 1.0

