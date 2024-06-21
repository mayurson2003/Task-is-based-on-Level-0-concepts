def minion_game(string):
   
    kevin_count = 0
    stuart_count = 0
    for idx in range(len(string)):
        if string[idx].upper() in "AEIOU":
            kevin_count += len(string[idx:])
        else:
            stuart_count += len(string[idx:])

    if stuart_count > kevin_count:
        print("Stuart", stuart_count)
    if stuart_count < kevin_count:
        print("Kevin", kevin_count)
    if stuart_count == kevin_count:
        print("Draw")
        
if __name__ == '__main__' :
    string = input()
    minion_game(string)     