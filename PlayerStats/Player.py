class player:

    # init method or constructor
    def __init__(self, first_name, last_name, opta_id, dob, age, height, citizenship, position, preferred_foot='None',
                 current_club='Without Club'):
        self.first_name = first_name
        self.last_name = last_name
        self.opta_id = opta_id
        self.full_name = "{} {}".format(first_name, last_name)
        self.dob = dob
        self.age = age
        self.height = height
        self.citizenship = citizenship
        self.preferred_foot = preferred_foot
        self.position = position
        self.current_club = current_club
