from main import Invitee

# Invitee objects have a name (str), a subjective likelyhood to attend (bool) / 
# and a number of guests they bring along (int)

family = [
    Invitee("homer_simpson", True, 0),
    Invitee("marge_simpson", True, 0),
    Invitee("lisa_simpson", True, 2),
    Invitee("bart_simpson", True, 1)
]

friends = [
    Invitee("barney_gumble", True, 0),
    Invitee("moe_szyslak", False, 0),
    Invitee("chief_wiggum", False, 1),
    Invitee("seymor_skinner", True, 1),
    Invitee("ned_flanders", True, 3),
]