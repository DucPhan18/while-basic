# in stn từ 1 đến 100
k = 0
while k < 100:
    k = k + 1
    print(k, end=" ")

# in các chữ từ A đến Z
i = 0 
k = 65 #bắt đầu từ số thứ tự của chữ cái A
while k < 91:
    i = i + 1
    if i%10 == 0:
        print (chr(k))
    else:
        print(chr(k), end="")
    k = k + 1

# in các số tự nhiên từ 1 đến 100 ra màn hình thành 10 hàng
for i in range(10):
    for k in range(1,11):
         print(i*10+k,end=" ")
    print("\n")

# cho dãy số 1,4,7,10,... in ra phần tử lớn nhất của dãy nhưng nhỏ hơn 100
i = 1
while i<100:
    i=i+3
i=i-3
print("Giá trị lớn nhất của dãy nhỏ hơn 100 là:", i)

# đếm trong dãy 100 số tự nhiên đầu tiên, in ra số thoã đk chia hết cho 5 hoặc chia 3 dư 1
i = 0
count = 0
while i < 100:
    if i%5 == 0 or i%3 == 1:
        count = count + 1
    i = i + 1
print (count)