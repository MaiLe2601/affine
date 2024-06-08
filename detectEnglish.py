UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

#đọc file dictionary.text
#lưu danh sách từ vựng vào biến ENGLISH_WORDS
def loadDictionary():
    dictionaryFile = open("../affine/dictionary.txt")
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = None
    dictionaryFile.close()
    return englishWords

ENGLISH_WORDS = loadDictionary()

#loại bỏ các kí tự không nằm trong danh sách LETTERS_AND_SPACE
def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)

#đếm số từ hợp lệ trong chuỗi message
#trả về giá trị là phần trăm số từ hợp lệ trên tổng số từ của message
def getEnglishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()
    
    if possibleWords == []:
        return 0.0 #không có từ nào thì trả về 0.0

    count = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            count += 1
    return float(count) / len(possibleWords)

#kiểm tra chuỗi message có phải là chuỗi Tiếng Anh không
#kết quả trả về True hoặc False
def isEnglish(message, wordPercentage=20, letterPercentage=85):
    wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch