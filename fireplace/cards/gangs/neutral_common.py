from ..utils import *

##
# Minions

class CFM_060:
	"Red Mana Wyrm"
	events = OWN_SPELL_PLAY.on(Buff(SELF, "CFM_060e"))

CFM_060e = buff(+2)

class CFM_063:
	"Kooky Chemist"
	play = Buff(TARGET, "CFM_063e")

CFM_063e = AttackHealthSwapBuff()

#class CFM_067:
#	"Hozen Healer"

#class CFM_120:
#	"Mistress of Mixtures"

#class CFM_619:
#	"Kabal Chemist"

#class CFM_646:
#	"Backstreet Leper"

#class CFM_647:
#	"Blowgill Sniper"

#class CFM_648:
#	"Big-Time Racketeer"

#class CFM_651:
#	"Naga Corsair"

#class CFM_653:
#	"Hired Gun"

#class CFM_654:
#	"Friendly Bartender"

#class CFM_655:
#	"Toxic Sewer Ooze"

#class CFM_656:
#	"Streetwise Investigator"

#class CFM_659:
#	"Gadgetzan Socialite"

#class CFM_665:
#	"Worgen Greaser"

#class CFM_666:
#	"Grook Fu Master"

#class CFM_715:
#	"Jade Spirit"

#class CFM_809:
#	"Tanaris Hogchopper"

#class CFM_851:
#	"Daring Reporter"

#class CFM_853:
#	"Grimestreet Smuggler"

#class CFM_854:
#	"Ancient of Blossoms"

