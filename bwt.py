# python3
import sys


# this function takes in Text and returns the Burrows-Wheeler Transform (BWT)
# example:
# input: 'AGACATA$'
# output: ATG$CAAA
# the BWT matrix built from Text
# $ A G A C A T A
# A $ A G A C A T
# A C A T A $ A G
# A G A C A T A $
# A T A $ A G A C
# C A T A $ A G A
# G A C A T A $ A
# T A $ A G A C A
#               ^
#               |
#              BWT = last columnn = ATG$CAAA
def BWT(text):
    '''
    build a Burrows-Wheeler Transform (BWT) from Text
    '''
    # build a BWT matrix by sorting all cyclic rotations of Text
    bwt_matrix = []
    n = len(text)
    for i in range(n):
        rota = text[i:n+1] + text[0:i]
        bwt_matrix.append(rota)
    bwt_matrix.sort()

    # create the BWT from the BWT matrix by extracting the matrix's last column
    bwt = ''
    for i in range(n):
        bwt = bwt + bwt_matrix[i][-1]

    return bwt


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))
