from ..utils import *

##
# Minions

class CFM_062:
	"Grimestreet Protector"
	play = GiveDivineShield(SELF_ADJACENT)

class CFM_639:
	"Grimestreet Enforcer"
	events = OWN_TURN_END.on(Buff(FRIENDLY_HAND + MINION, "CFM_639e"))

CFM_639e = buff(+1, +1)

#class CFM_650:
#	"Grimscale Chum"

#class CFM_753:
#	"Grimestreet Outfitter"

#class CFM_759:
#	"Meanstreet Marshal"

#class CFM_815:
#	"Wickerflame Burnbristle"

##
# Spells

#class CFM_305:
#	"Smuggler's Run"

#class CFM_800:
#	"Getaway Kodo"

#class CFM_905:
#	"Small-Time Recruits"

