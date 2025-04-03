class Invitee:

    def __init__(self, name: str, will_likely_attend: bool, possible_guests: int):
        self.name = name
        self.will_likely_attend = will_likely_attend
        self.possible_guests = possible_guests

def count_invitees(family_list, friends_list):
    total_invitees = 0
    probable_with_guests = 0
    probable_without_guests = 0
    
    for invitee in family_list + friends_list:
        # Count for total_invitees
        total_invitees += 1 + invitee.possible_guests
        
        # Count for probable attendees
        if invitee.will_likely_attend:
            probable_without_guests += 1
            probable_with_guests += 1 + invitee.possible_guests
    
    return total_invitees, probable_with_guests, probable_without_guests

def main():

    try:
        from invitee_data import family, friends
    except ImportError:
        print("Data file not found, using empty lists")
        family = []
        friends = []
 
    total_invitees, probable_with_guests, probable_without_guests = count_invitees(family, friends)

    print("---------------------------")
    print(f"Total count of all attendees is >> {total_invitees} << if:")
    print(" - everyone comes regardless of distance or likelyhood")
    print(" - everyone brings all their guests")
    print("---------------------------")
    print(f"Total count of all attendees is >> {probable_with_guests} << if:")
    print(" - unlikely attending invitees are not coming")
    print(" - all guests of those probably showing up are brought")
    print("---------------------------")
    print(f"Total count of all attendees is >> {probable_without_guests} << if:")
    print(" - unlikely attending invitees are not coming")
    print(" - nobody brings any additional guests")
    print("---------------------------")

if __name__ == "__main__":
    main()




