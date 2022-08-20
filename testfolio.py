"""
	=======================		PRE-PREPARATION FOR PORTFOLIO PROJECT	=================================
"""

#	Function to record member contributions
def recordDues():
	memberName = "Full name: "
	paidAmount = "Amount: GHS"
	
	records = {}
	
	terminator = ["#", "/", ""]
	
	while True:
		quest1 = input(memberName)
		quest2 = input(paidAmount)
		
		if quest1 in terminator or quest2 in terminator:
			break
		
		# records[memberName] = paidAmount
		records.update({quest1: quest2})	#	Update record with new information

	return records



#	TESTING WORK AREA

dues = recordDues()
print(dues)


