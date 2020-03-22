import os

os.system("tput setaf 4")

print(""" \t\t\t your welcome to TUI project
1. to check date/time
2. to enable computer to speak something
3. to check calander
4. to configure web server
5. to configure yum 
""")

choice = int(input())

if(choice ==1):
	date()
elif (choice ==2):
	speak()
elif(choice==3):
	calender()
elif(choice==4):
	

os.system("tput setaf 7")


def date():
	choice = int(input(""" 1. date
	2. time""")
	if(choice==1):
		os.system("date +%D")
	elif(choice==2):
		os.system("date +%T")
		
def calander():
	os.system("cal()")
	
def speak():
	say=input("What you want computer to speak for you")
	os.system("espeak "+say)
	