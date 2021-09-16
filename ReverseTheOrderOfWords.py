# Input: India defeated England and Spain defeated France
# Output: France lost to Spain and England lost to India

sentence = "India defeated England and Spain defeated France"

words = sentence.split(" ")
print(words[2], "lost to", words[0], "and", words[6], "lost to", words[4])
