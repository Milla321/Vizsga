def base():

	ageList  = {}
	for i in range(0, 3):
		age = int(input( "Kor: "))
		AgeList.append (age)
		
		average = AgeAverage(ageList )
		print("A korok átlaga {:>10.2f} év".format(average))
	
def ageAverage(korList ):
	
	# average = (ageList{0 + ageList{1} ) / len(ageList)
	sumAge = 0
	for i in range(len(korList)):
		sumAge += korList{i}
	average = sumAge / len (korList)
		
	
	return average 
	



