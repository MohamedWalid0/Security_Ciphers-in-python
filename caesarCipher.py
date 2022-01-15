import string

class caesarCipher :

    LETTERS = { str(index):letter for index, letter in enumerate(string.ascii_lowercase, start=0)} 
    
    def __init__(self ,key, *,plainText=None , cipherText=None) :
        self.plainText = plainText and plainText.lower()
        self.key = key.lower()
        self.cipherText = cipherText and cipherText.lower()

    def encrypt(self ) :

        cipherText = ""

        for i in self.plainText :

            cipherTextPosition = (string.ascii_lowercase.index(i) + string.ascii_lowercase.index(self.key)) % 26
            cipherText += (self.LETTERS[str(cipherTextPosition)] )
            
        return cipherText


    def decrypt(self ) :

        plainText = ""

        for i in self.cipherText :
            plainTextPosition = (string.ascii_lowercase.index(i) - string.ascii_lowercase.index(self.key)) % 26
            plainText += (self.LETTERS[str(plainTextPosition)] )
            
        return plainText





if __name__ == '__main__':

    x = int(input("enter 1 to encrypt , 2 to decrypt"))

    if x == 1 :
        plainText = "uniFIed"
        key = "k"
        cipherText = caesarCipher(key, plainText=plainText).encrypt()
        print(cipherText)

    elif x == 2 :

        cipherText = "VGWKFGLHJGNAVWLZWKSEWDWNW"
        key = "s"
        plainText = caesarCipher(key, cipherText=cipherText).decrypt()
        print(plainText)

    else : 
        print( "wrong input" )

