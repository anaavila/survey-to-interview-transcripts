import csv

fileToRead = "survey.csv"
folderName = "transcripts/transcript_"
# opening and reading a CSV file
f = open(fileToRead, 'r')
print("Opening " + fileToRead + "...")
reader = csv.reader(f)
allData = list(reader)
print("Opened " + fileToRead)
print("Closing " + fileToRead+ "...")
f.close()
print("Closed " + fileToRead)

questions = allData[0]
transcriptDoc = ""

participants = []
print(len(allData))
for p in range(1,len(allData)):
	print(p)
	participants.append("Participant "+str(p))

print(participants)

personAnswers = []
for a in range(1,len(allData)):
	personAnswers.append(allData[a])

for i, participant in zip(range(len(personAnswers)), participants):
	fileToWrite = folderName + participant + ".txt"
	print("Opening " + fileToWrite + "...")
	writeFile = open(fileToWrite, 'w')
	print("Opened " + fileToWrite)
	writeFile.write(''.join("Interview transcript\n\nName: " + participant + "\n\nSituation: \n\n"))
	for j in range(len(personAnswers[i])):
		writeFile.write(''.join("[UX Researcher] " + questions[j] + "\n\n"))
		writeFile.write(''.join("[" + participant + "] " + personAnswers[i][j] + "\n\n"))
	print("Closing " + fileToWrite + "...")
	writeFile.close()
	print("Closed " + fileToWrite)
	
print(str(len(participants)) + " files were created.")

