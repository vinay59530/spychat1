from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('vinay','Mr.',24,4)

friend_one = Spy('sahil','Mr.',27,4.9)
friend_two = Spy('nimita','Ms.',21,4.3)
friend_three = Spy('dang','Dr.',37,3.7)


friends = [friend_one, friend_two, friend_three]