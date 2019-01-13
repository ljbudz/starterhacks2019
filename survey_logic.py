def my_data(my_dict):
    my_list = []

    for key, value in my_dict.items():
        my_list.append(value)

    # my_str = ""

    #for item in my_list:
    #    my_str += item + ' '

    class Mentor:

        def __init__(self, name, q1, q2, q3, q4):
            self.name = name
            self.q1 = q1
            self.q2 = q2
            self.q3 = q3
            self.q4 = q4

        def get_attributes(self):
            return [self.q1, self.q2, self.q3, self.q4]

    mentor1 = Mentor("Laurel", "Math", "I love working in teams!", "I prefer to use a logical approach", "From home")
    mentor2 = Mentor("Benjamin", "Arts", "I prefer to work alone", "I prefer to go with my gut", "From home")
    mentor3 = Mentor("Steven", "English", "Working in teams is okay", "I prefer to go with my gut", "In an office")
    mentor4 = Mentor("Sarah", "Math", "I love working in teams!", "I prefer to use a logical approach", "In an office")
    mentor5 = Mentor("Amanda", "Science", "Working in teams is okay", "I prefer to use a logical approach", "Outside")
    mentor6 = Mentor("Joshua", "Science", "I prefer to work alone", "I prefer to go with my gut", "Outside")

    mentors = [mentor1, mentor2, mentor3, mentor4, mentor5, mentor6]
    scores = [0]*6

    for person in range(0,6):
        for item in range(0,4):
            if my_list[item] in mentors[person].get_attributes():
                scores[person] += 1

    return mentors[scores.index(max(scores))].name
