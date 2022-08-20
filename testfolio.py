"""
	=======================		PRE-PREPARATION FOR PORTFOLIO PROJECT	=================================

	DATE:						20-AUG-2022
	DEVELOPER:					EMMANUEL ENCHILL
	PROGRAMME NAME:				BASIC DUES COLLECTION APPLICATION
	PROGRAMME DESCRIPTION:		THIS IS A SIMPLE FINANCE MANAGEMENT APPLICATION. ITS SOLE CAPABILITY IS
								ACCEPTING ENTRIES OF MEMBER NAMES AND PAYMENT AMOUNTS. PROGRAMME INITIALY 
								LACK ERROR CHECKING CAPABILITIES; IT WILL CRASH WHEN A STRING IS PROVIDED AS
								THE AMOUNT VALUE. MORE FEATURES WILL BE ADDED AS DEVELOPMENT ADVANCES
"""

#	Function to record member contributions
def recordDues():
	memberName = "Full name: "
	paidAmount = "Amount: GHS"
	
	records = {}
	
	terminator = ["#", "/", ""]
	
	while True:
		quest1 = input(memberName)
		
		if quest1 in terminator:
			break
		
		quest2 = input(paidAmount)
		
		# records[memberName] = paidAmount
		records.update({quest1: quest2})	#	Update record with new information

	return records



#	TESTING WORK AREA

dues = recordDues()
print(dues)


