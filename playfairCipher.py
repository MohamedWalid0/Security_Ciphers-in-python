class playfairCipher :

    def encrypt(self ,plainText , key) :
        plainText = self.preparePlainText(plainText)
        plainText = self.convertPlainTextToDiagraphs(plainText)

        key = self.prepareKey(key)
        keyMatrix = self.generateKeyMatrix(key)
        # return (keyMatrix)
        
        cipherText = []
        
        i=0
        
        while i < len(plainText):
            r1 , c1 = self.charPosition(keyMatrix , plainText[i])
            r2 , c2 = self.charPosition(keyMatrix , plainText[i+1])
            
            # if same row --> shift letter right
            if r1 == r2 :
                
                if c1 == 4 :
                    c1 = -1
                if c2 == 4 :
                    c2 = -1
                    
                cipherText.append(keyMatrix[r1][c1+1])   
                cipherText.append(keyMatrix[r1][c2+1])   
                
            # if same column --> shift letter down
            elif c1 == c2 :
                
                if r1 == 4 :
                    r1 = -1
                if r2 == 4 :
                    r2 = -1

                
                cipherText.append(keyMatrix[r1+1][c1])   
                cipherText.append(keyMatrix[r2+1][c2])   

                
            else :
                cipherText.append(keyMatrix[r1][c2])
                cipherText.append(keyMatrix[r2][c1])


            i += 2  

        return cipherText

    def convertPlainTextToDiagraphs (self ,plainText):

        for s in range(0,len(plainText)+1,2):
            
            if s<len(plainText)-1:
                
                if plainText[s]==plainText[s+1]:
                    plainText=plainText[:s+1]+'X'+plainText[s+1:]

        if len(plainText)%2 != 0:
            plainText = plainText[:]+'X'

        return plainText

    def generateKeyMatrix(self ,key) :
        
        # initialize 5x5 matrix
        matrix=[]
        
        for char in key:
            if char not in matrix:
                matrix.append(char)
                
        alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        for char in alphabet:
            if char not in matrix:
                matrix.append(char)	
                

        matrix5x5=[]
        
        for e in range(5):
            matrix5x5.append('')

        # initialize 5x5 matrix
        matrix5x5[0]=matrix[0:5]
        matrix5x5[1]=matrix[5:10]
        matrix5x5[2]=matrix[10:15]
        matrix5x5[3]=matrix[15:20]
        matrix5x5[4]=matrix[20:25]
        
        return matrix5x5

    def charPosition(self ,matrix , letter) :

        x=y=0
        
        for i in range(5):
            for j in range(5):
                if matrix[i][j]==letter:
                    x=i
                    y=j

        return x,y

    def preparePlainText(self ,plainText) :
        plainText = plainText.replace(" " , "").upper()
        return plainText

    def prepareKey(self ,key) :
        key = key.replace(" " , "").upper()
        return key

    def cipherToDigraphs(self ,cipher):
        
        i=0
        new=[]
        for x in range(len(cipher)//2):
            new.append(cipher[i:i+2])
            i=i+2
        return new

    def decrypt(self ,cipher ,key) :
        
        key = self.prepareKey(key)
        keyMatrix = self.generateKeyMatrix(key)
        plain=[]
        i=0
        
        while i < len(cipher):
            
            r1 , c1 = self.charPosition(keyMatrix , cipher[i])
            r2 , c2 = self.charPosition(keyMatrix , cipher[i+1])
            
            # if same row --> shift letter left
            if r1 == r2 :
                
                if c1 == 4 :
                    c1 = -1
                if c2 == 4 :
                    c2 = -1
                    
                plain.append(keyMatrix[r1][c1-1])   
                plain.append(keyMatrix[r1][c2-1])   
                
            # if same column --> shift letter up
            elif c1 == c2 :
                
                if r1 == 4 :
                    r1 = -1
                if r2 == 4 :
                    r2 = -1

                
                plain.append(keyMatrix[r1-1][c1])   
                plain.append(keyMatrix[r2-1][c2])   

                
            else :
                plain.append(keyMatrix[r1][c2])
                plain.append(keyMatrix[r2][c1])


            i += 2  




        for unused in range(len(plain)):
            if "X" in plain:
                plain.remove("X")

        return plain






if __name__ == '__main__':

    x = int(input("enter 1 to encrypt , 2 to decrypt"))

    if x == 1 :
        plainText = "THE CONFIDENTIALITY CONSIDERAT"
        keyword = "oneforone"
        cipherText = ''.join(playfairCipher().encrypt(plainText , keyword))
        print ("cipher text = " + cipherText)


    elif x == 2 :

        cipherText = "CMKMJBBSFBMBDSUVYMNBBSHWYUCU"

        keyword = "destroys"

        plainText = ''.join(playfairCipher().decrypt(cipherText , keyword))
        print(plainText)

    else : 
        print( "wrong input" )


