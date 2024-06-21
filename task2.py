from itertools import groupby


def main(string):
    

    for k, c in groupby(string):
        
   
        print("(%d, %d)" % (len(list(c)), int(k)), end=' ')
        

main(input())
        

        
