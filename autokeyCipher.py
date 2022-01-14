import string

class autokeyCipher :
    LETTERS = { str(index):letter for index, letter in enumerate(string.ascii_lowercase, start=0)} 

    def generateKey(self , plainText , key) :
        plainText = plainText.replace(" " , "")
        key = key.replace(" " , "")

        if len(plainText) == len(key):
            return(key)

        i = 0
        while True:
            if len(key) == len(plainText):
                break
            if plainText[i] == ' ':
                i += 1
            else:
                key += plainText[i]
                i += 1
        
        return key
        
        # return("" . join(key))





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
        newKey = ""

        index = 0
        for i in range(len(cipherText)) :
            index += 1

            if index <= len(key) :

                plainTextPosition = (  string.ascii_lowercase.index(cipherText[i]) -  (string.ascii_lowercase.index(key[i]) )) % 26
                plainText += (self.LETTERS[str(plainTextPosition)] )

            else :
                newKey = key + plainText + plainText
                plainTextPosition = (  string.ascii_lowercase.index(cipherText[i]) -  (string.ascii_lowercase.index(newKey[i]) )) % 26
                plainText += (self.LETTERS[str(plainTextPosition)] )

        return plainText
      



if __name__ == '__main__':

    x = int(input("enter 1 to encrypt , 2 to decrypt"))

    if x == 1 :
        plainText = "butthemanthere"
        keyword = "split"
        key = autokeyCipher().generateKey(plainText , keyword)
        cipherText = autokeyCipher().encrypt(plainText , key)
        print(cipherText)

    elif x == 2 :

        cipherText = "lvqsfgkmwxpwiswe"
        keyword = "link"
        key = autokeyCipher().generateKey(cipherText , keyword)

        plainText = autokeyCipher().decrypt(cipherText , keyword)
        print(plainText)

    else : 
        print( "wrong input" )


