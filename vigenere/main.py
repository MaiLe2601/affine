import mahoa,giaima
# ngăn người dùng nhập sai số
while True:
    mode = int(input("Chọn chế độ bạn muốn(1-Mã hóa, 2-Giải mã:"))
    if (mode == 1 or mode == 2):
        break

#  message = input("Nhập thông điệp: ")
# mở file text để đọc
with open ("../vigenere/messages.txt", "r") as file:
    message = file.read()
key = input("Nhập khóa: ")

if (mode == 1):
	print('<----------Đang mã hóa------------>')	
	text = mahoa.mahoa(message, key)
	print("Bản rõ: ", message)
	print('Bản mã: ', text)
else:
	print('<----------Đang giải mã----------->')
	text = giaima.giaima(message, key)
	print("Bản mã: ", message)
	print('Bản rõ: ', text)
# mở file text để ghi
with open ("../vigenere/messages.txt", "w") as file:
    file.write(text)
print("Saving text to file messages.")