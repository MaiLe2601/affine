import mahoa, giaima, thamma
# ngăn người dùng nhập sai số
while True:
    mode = int(input("Chọn chế độ bạn muốn(1-Mã hóa, 2-Giải mã, 3-Thám mã):"))
    if (mode == 1 or mode == 2 or mode == 3):
        break

# mở file messages để đọc
with open ("../affine/messages.txt", "r") as file:
    message = file.read()
    
if (mode == 3):
    print("---------Đang thám mã-----------")
    keya, keyb, text = thamma.hackAffine(message)
    if text != None:
        print("Ciphertext: ", message)
        print(f"Key: a = {keya}, b = {keyb}")
        print("Plaintext: ", text)
    else:
        print('Failed to hack encryption.')
else:
    a = int(input("Nhập khóa a:"))
    b = int(input("Nhập khóa b:"))
    if (mode == 1):
        print("--------Đang mã hóa------------")
        text = mahoa.affine_encode(message, a, b)
        print("Plaintext: ", message)
        print("Ciphertext: ", text)
    else: 
        print("--------Đang giải mã------------")
        text = giaima.affine_decrypt(message, a, b)
        print("Ciphertext: ", message)
        print("Plaintext: ", text)
    
# ghi vào file messages
with open ("../affine/messages.txt", "w") as file:
    file.write(text)
print("Saving text to file messages.")      
