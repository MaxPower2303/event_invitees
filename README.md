The purpose is calculating total attendance for a planned event considering different scenarios. 

Currently the code only takes lists of Invitee-objects. They have a name (:str), a (subjective) likelyhood to attend (:bool) and a number of guests they possibly bring along, like wives or children (:int). 
I considered making these another class with fewer attributes (guests shouldnt bring even more guests!), but we possibly even do not care about the names of all the guests of our invitees, so these are just ints for simplification. 
