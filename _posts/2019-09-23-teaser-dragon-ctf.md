---
layout : post 
title : Teaser Dragon CTF RsaChain 
--- 

Trong kì thi có 1 bài crypto duy nhất và cũng là bài duy nhất mình làm được.  Các bạn có thể dowload challenge tại [đây](https://github.com/hacmao/hacmao.github.io/tree/master/Crypto/ctf/teaser_dragon)

# Enryption  

Đây là một bài rsa 😬😬😬. Trước tiên nó thiết lập 4 key :  

```python
# rsa1: p - 700 bits q - 1400 bits

p = genPrime(700)
q = genPrime(1400)

n = p*q
phi = (p-1)*(q-1)
d = gmpy2.powmod(e, -1, phi)

rsa1 = (n, d)
``` 

Mấy key còn lại tương tự nhưng có thay đổi một chút. 😁  
Sau đó thì nó có hàm encrypt flag 4 lớp rồi in ra flag encrypt :  

```python 

for n, d in rsa:
    print 'pubkey:', n, d % (2**1050)
    flag = pow(flag, e, n)

print 'encrypted flag', flag
``` 
Đồng thời chúng ta có được từng module và partial private key d.  
Đến đây ta đã biết rõ được kiểu tấn công của bài này là ```Partial Key Exposure Attack```. Có thể đọc paper ở [đây](Partial Key Exposure Attack). Mục 4.5.   

# Partial Key Exposure Attack 

Trong mục 4.5 kia ta chú ý phần này :  

![](/Crypto/ctf/teaser_dragon/hinh1.PNG)  

Phần đầu tiên trong kiểu attack này là recovery lại một phần p hoặc q. Ta làm trường hợp đơn giản trước là n = p * q.  
Do ```ed = 1 [mod phi]``` nên tồn tại một số k thỏa mãn phương trình trên. Cùng với đó, ta có d < phi(n) nên k < e.  
Gọi kb là số bits đã biết d0 của d.Ta có :  

```python
    e * d0 - k*(N - p - q + 1) = 1 [mod 2^kb] 
->  e * d0 * p - k * (N * p - p^2 - N + p) = p [mod 2^kb]   # Nhan ca hai ve voi p 
```

Tại sao lại nhân cả hai về với p. Vì khi đó chúng ta chỉ còn lại một biến chưa biết là ```p```. Ta có phương trình đồng dư bậc hai.  
Có thể dễ dàng giải được bằng [Hennsel lift](https://github.com/gmossessian/Hensel).  
Nói chung cũng không cần hiểu rõ cách hoạt động của hennsel lift. Dùng code chạy giải ra nghiệm là được. Hennsel lift là cách giải tối ưu nhất cho những phương trình đa thức đồng dư một p^k.  

Nhưng đương nhiên bài này không thể áp dụng trực tiếp kiểu tấn công kia. Vì kiểu tấn công kia dành cho ```n = p*q```. 



