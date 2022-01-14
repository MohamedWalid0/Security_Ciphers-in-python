import string

class vigenereCipher :
    LETTERS = { str(index):letter for index, letter in enumerate(string.ascii_lowercase, start=0)} 

    def generateKey(self , plainText , key) :
        plainText = plainText.replace(" " , "")
        key = key.replace(" " , "")

        print(plainText)
        if len(plainText) == len(key):
            return(key)

        else:
            for i in range(len(plainText) - len(key)):
                key += (key[i % len(key)])

        return("" . join(key))


    def encrypt(self , plainText , key) :
        plainText = plainText.lower().replace(" " , "")
        key = key.lower()
        cipherText = ""

        for i in range(len(plainText)) :

            cipherTextPosition = (string.ascii_lowercase.index(plainText[i]) + string.ascii_lowercase.index(key[i]) ) % 26
            cipherText += (self.LETTERS[str(cipherTextPosition)] )
            
        return cipherText



    def decrypt(self, cipherText , key) :

        cipherText = cipherText.lower().replace(" " , "")
        key = key.lower()
        plainText = ""

        for i in range(len(cipherText)) :

            plainTextPosition = (string.ascii_lowercase.index(cipherText[i]) - string.ascii_lowercase.index(key[i]) ) % 26
            plainText += (self.LETTERS[str(plainTextPosition)] )
            
        return plainText





if __name__ == '__main__':

    x = int(input("enter 1 to encrypt , 2 to decrypt"))

    if x == 1 :
        plainText = "GEEKSFORGEEKS"
        keyword = "AYUSH"
        key = vigenereCipher().generateKey(plainText , keyword)
        cipherText = vigenereCipher().encrypt(plainText , key)
        print(cipherText)

    elif x == 2 :

        cipherText = "pcbxsdawaaxh"
        keyword = "hand"
        key = vigenereCipher().generateKey(cipherText , keyword)

        plainText = vigenereCipher().decrypt(cipherText , key)
        print(plainText)

    else : 
        print( "wrong input" )


