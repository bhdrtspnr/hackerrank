def stringSimilarity(s):
    testStrings = []
    
    count = 0

    for j in range(len(s)):
        testStrings.append(s[j:])
    
    i=0


    for strings in testStrings:
        i=0
        while i<len(strings):
            if strings[i] == s[i]:
                count +=1
                print("Successfull "+str(i) + "th iteration" + " for substring " + strings+ " count is currently " + str(count))
            else:
                print("Failure "+ str(i) + "th iteration" + " for substring " + strings + " count is currently: "+str(count))
                i += 100
            i +=1

    return count




if __name__ == '__main__':
    testCase = "ababaa"
    
    print(stringSimilarity(testCase))
