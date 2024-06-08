## 1. Mã hóa
- E(x) = (ax + b) mod m
- Áp dụng bảng chữ cái tiếng anh nên m = 26
  
## 2. Giải mã
- D(y) = a^(-1).(y - b) mod m
- Điều kiện tồn tại a^(-1):
    + Nếu số nguyên dương x < n: x*a mod n = 1 thì x là nghịch đảo của a mod n, kí hiệu: a-1 mod n.
    + Ví dụ: powerpoint

## 3. Thám mã
- Vì UCLN(a, 26) =1 nên:
  + a € {1, 3, 5,7,9,11,15,17,19,21,23,25} gồm 12 số
  + b từ 0 đến 25: 26 số
- Vậy: 12*26 = 312 khóa (rất ít) nên với sức mạnh của máy tính, ta vẫn có thể dễ dàng thử hết các khả năng bằng thuật toán Brute-force (duyệt toàn các khả năng đến khi kết quả đầu ra có hơn 80% là từ nghĩa, là những từ có trong từ điển detectEnglish )
