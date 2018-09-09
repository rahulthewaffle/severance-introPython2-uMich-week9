# 9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

fileName = input("Enter file name: ")

if len(fileName) < 1 :
    fileName = "mbox-short.txt"

fileHandle = open(fileName)

senderCount = dict()

for line in fileHandle :
    if line.startswith("From ") :
        sentence = line.split()
        sender = sentence[1]
        senderCount[sender] = senderCount.get(sender, 0) + 1

maxCount = None
maxSender = None

for sender,count in senderCount.items() :
    if maxCount is None or count > maxCount :
        maxCount = count
        maxSender = sender

print(maxSender, maxCount)
