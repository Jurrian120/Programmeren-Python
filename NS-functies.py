regulierePrijsPerKM = .80
zoneGrensAfstand = 50
startBedragLangeRit = 15.00
langRitPrijsPerKM = .60

maximaleJongerenLeeftijd = 12
minimaleOuderenLeeftijd = 65

weekdayDiscountRate = .7
weekendDiscountRate = .65
weekendRegularRate = .6

def standaardtarief(afstandKM):
	standaardRitPrijs= 0

	if afstandKM > zoneGrensAfstand:
		standaardRitPrijs = startBedragLangeRit + (langRitPrijsPerKM * afstandKM)
	else:
		standaardRitPrijs = afstandKM * regulierePrijsPerKM
	return standaardRitPrijs

def ritprijs(leeftijd, isEenReisInHetWeekend, afstandKM):
	standaardRitPrijs = standaardtarief(afstandKM)

	returnValue = standaardRitPrijs

	hasAgeDiscount = ((leeftijd < maximaleJongerenLeeftijd) or (leeftijd >= minimaleOuderenLeeftijd))
	if not isEenReisInHetWeekend and hasAgeDiscount:
		returnValue = standaardRitPrijs * weekdayDiscountRate
	elif isEenReisInHetWeekend and hasAgeDiscount:
		returnValue = standaardRitPrijs * weekendDiscountRate
	elif isEenReisInHetWeekend:
		returnValue = standaardRitPrijs * weekendRegularRate

	return returnValue

tests = [
	[11, True, 50],
	[12, False, 49],
	[64, True, 100],
	[65, False, 20],
	[40, False, 75.98], # float overflow lets go
	[41, False, 120.56],
	[41, False, -126]
]

for test in tests:
	print("test: €" + str( format( ritprijs( test[0], test[1], test[2] ), ".2f") ) + " --- standaard: €"+ str(standaardtarief(test[2])) )
