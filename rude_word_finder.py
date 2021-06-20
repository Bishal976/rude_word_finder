import string
#importing string module for the further operaitons 
rude_words = ["shit", "plot", "dict", "facilitated","2020"]
file = open("C:\\Users\\215073\\Desktop\\pnc.txt")
files= file.read()
contents = files.split(" ")
print(contents)
count = 0
for content in contents:
    content = content.strip(string.punctuation)
    if content in rude_words:
        print(f"there is a rude word in your file: {content}")
        count += 1
if count == 0:
    print("there is no rude word here")



# rude_words = ["shit", "plot", "dict","asr", "facilitated","hanuman"]
# file = open("C:\\Users\\215073\\Desktop\\pnc.txt")
# files = file.read()
# count = 0
# for content in rude_words:
#     if content in files:
#         print(f"there is a rude word in your file: {content}")
#         count += 1
# if count == 0:
#     print("there is no rude word here")
