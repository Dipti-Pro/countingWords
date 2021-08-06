introString=input("Enter string:")
characterCount=0
wordCount=1
for i in introString:
      characterCount=characterCount+1
      #mandatory to give space on betwen the ' '
      if(i==' '):
            wordCount=wordCount+1
print("Number of word in the string:")
print(wordCount)
print("Number of character in the string:")
print(characterCount)
