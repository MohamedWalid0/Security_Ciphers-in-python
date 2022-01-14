import math

class railfenceCipher :


    def buildMatrixForEncryption(self , plainText , rows , cols) :

        matrix = [['' for j in range(cols)] for i in range(rows)]
        row = 0
        col = 0

        for character in plainText :

            matrix[row][col] = character
            
            if row >= rows-1 :
                row = 0
                col += 1
            else :
                row +=1

        cipherText = [ y for x in matrix for y in x]
        return "".join(map(str,cipherText))


    def encrypt(self , plainText , depth) :
        
        rows = depth 
        p = len(plainText)
        cols = math.ceil(p/rows) 
        return self.buildMatrixForEncryption(plainText,rows , cols)




    def buildMatrixForDecryption(self , cipherText , rows , cols , numOfCompletedRows) :
        matrix = [['' for j in range(cols)] for i in range(rows)]
        row = 0
        col = 0
        flag = True

        for character in cipherText :

            if numOfCompletedRows != 0 :
                if row+1 > numOfCompletedRows and flag == True :
                    cols = cols-1
                    flag = False

            matrix[row][col] = character

            if col >= cols-1 :
                col = 0
                row += 1
            else :
                col +=1
        plainTextMatrix = [ [matrix[r][c] for r in range(rows)] for c in range(cols) ]
        plainText = ''
        for i in plainTextMatrix : 
            for j in i :
                plainText+=j
        return plainText

    def decrypt(self , cipherText , depth) :

        rows = depth 
        p = len(cipherText)
        cols = math.ceil(p/rows) 
        numOfCompletedRows = p % depth
        return self.buildMatrixForDecryption(cipherText,rows , cols , numOfCompletedRows)
        








if __name__ == '__main__':

    x = int(input("enter 1 to encrypt , 2 to decrypt"))

    if x == 1 :
        plainText = "itisathousandlevelsgiveortakeafewiwill"
        depth = 9
        cipherText = railfenceCipher().encrypt(plainText , depth)
        print(cipherText)

    elif x == 2 :

        # cipherText = "iratnrtchdehciwmeesaedpjsmatotbyeboeidal"
        # depth = 8
        # cipherText = "isskltageliniasdvfaleeteowhvrioetwulai"
        # depth = 9

        # special case 
        cipherText = "thlhedesnrceeoefpoerweotu"
        depth = 10 
        
        plainText = railfenceCipher().decrypt(cipherText , depth)
        print(plainText)

    else : 
        print( "wrong input" )


