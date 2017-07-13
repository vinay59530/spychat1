from mymain import spy, Spy, ChatMessage, friends
from termcolor import colored
from steganography.steganography import Steganography
from datetime import datetime

# we have declared till start_app is true it will run app
start_app = True
while start_app:

    # to start virtualenv type new_env\Scripts\activate in terminal
    print 'Let\'s our app get started'
    # we are creating the variable for status messages
    status_messages = ['My name is vinay, vinay kumar', 'Shaken, not stirred.', 'Have a good day, Sir']

    # we are selecting if we are continuing as default user or new user
    question = 'Do you want to continue as ' + spy.salutation + ' ' + spy.name + '(Y/N)?'
    existing = raw_input(question)


    # we have created the add status function
    def add_status():
        updated_status_message = None

        if spy.current_status_message != None:
            print colored('Your current status message is %s \n' % (spy.current_status_message), 'blue')
        else:
            print "Currently you don't have any status message"

        default = raw_input("Do you want to select from the older status (Y/N)")

        if default.upper() == 'N':
            new_status_message = raw_input('What do you want to set a new status')
            # checking that the status is not empty
            if len(new_status_message) > 0:
                status_messages.append(new_status_message)
                updated_status_message = new_status_message
            else:
                print 'Please enter a valid status'

        elif default.upper() == 'Y':
            item_position = 1
            # chekcing for status in status_message list
            for message in status_messages:
                print '%d. %s' % (item_position, message)
                item_position = item_position + 1
            # selecting a status
            message_selection = int(raw_input('\nChoose from above messages'))

            if len(status_messages) >= message_selection:
                updated_status_message = status_messages[message_selection - 1]
            else:
                print ''
        else:
            print 'The option you choose is not valid! To proceed press either (Y/N)'

        if updated_status_message:
            print colored('your updated message is: %s' % (updated_status_message), 'blue')
        else:
            print 'You did not update your status'
        return updated_status_message


    # we are created the add friend function and we have created dictionary of new_friend and do code refactoring
    def add_friend():
        new_friend = Spy('', '', 0, 0.0)

        new_friend.name = raw_input("Please add your friend's name: ")
        new_friend.salutation = raw_input("Are the Mr. or Mrs.or any other else? : ")
        new_friend.name = new_friend.name + ' ' + new_friend.salutation
        new_friend.age = int(raw_input('Age?'))
        new_friend.rating = float(raw_input('enter your rating'))

        if len(new_friend.name) > 0 and 12 < new_friend.age < 50 and new_friend.rating >= spy.rating:
            friends.append(new_friend)
            print 'New Friend added'
        else:
            print "Sorry! Invaid entry. We can't add spy with the details you provided"
        # here this return len will return the no for frineds the user have means the no of elements in the list
        return len(friends)


    # here we are selecting the friend from friends list and then returning the index of selected friend
    def select_a_friend():
        item_number = 0
        # we have declare new variable friend in which we are taking value of friends
        # note :- friend is different from friends
        for friend in friends:
            print '%d %s aged %d with rating %.2f is online' % (item_number + 1, friend.name, friend.age, friend.rating)
            item_number = item_number + 1

        friend_choice = raw_input('choose from your friends')
        friend_choice_position = int(friend_choice) - 1
        return friend_choice_position


    # here we are encrypting our message and sending it
    def send_message():
        # friend_choice is getting the friend to which we want to send message
        # select a friend () is giveng the index of selected friend
        friend_choice = select_a_friend()
        original_image = raw_input("What is the name of the image?")
        output_path = "output.jpg"
        text = raw_input(colored('Enter your message?', 'red'))
        if text:
            if len(text) < 100:
                Steganography.encode(original_image, output_path, text)
            else:
                print 'the length of message shoud not exceed 100'
        else:
            print 'empty string not allowed'
        new_chat = ChatMessage(text, True)

        friends[friend_choice].chats.append(new_chat)
        print 'your secret message is ready!'


    # here we are decrypting our message and sending it
    def read_message():
        # here we are selecting a friend to which messages we want to read
        # select a friend return the index of selected friend from friend function
        sender = select_a_friend()
        output_path = raw_input("What is the name of the file?")
        secret_text = Steganography.decode(output_path)
        print colored(secret_text, 'red')

        new_chat = ChatMessage(secret_text, False)

        friends[sender].chats.append(new_chat)

        print "Your secret message has been saved!"


    # show the chat history for the selected user
    def read_chat_history():
        read_for = select_a_friend()
        print '\n6'
        # read for return the index of selected friend for whom you want to read the messages
        # .chat is list which store the chat for the user
        for chat in friends[read_for].chats:
            if chat.sent_by_me:
                print colored('[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'you said:', chat.message), 'blue')
            else:
                print colored(
                    '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message), 'blue')


    # we are created the chat function in which all the validations are done
    def start_chat(spy):
        current_status_message = None

        spy.name = spy.salutation + ' ' + spy.name

        if 12 < spy.age < 50:
            print 'Authentication complete. Welcome ' + spy.name + ' age: ' + str(spy.age) + ' and rating of: ' + str(
                spy.rating) + ' Proud to have you onboard'

            if spy.rating > 4.5:
                print 'Great ace!'
            elif spy.rating > 3.5 and spy.rating <= 4.5:
                print 'You are one of the good ones.'
            elif spy.rating >= 2.5 and spy.rating <= 3.5:
                print 'You can always do better'
            else:
                print 'We can always use somebody to help in the office.'

            show_menu = True
            # we have created the menu
            while show_menu:
                menu_choices = raw_input(colored(
                    'what do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. send a secret message \n 4. read a secret message \n 5. Read Chats from a user \n 6. close application\n ',
                    'green'))
                menu_choice = menu_choices
                if menu_choice.isdigit():
                    if len(menu_choice) > 0:
                        menu_choice = int(menu_choice)
                        # we are selecting the choices for menu
                        if menu_choice == 1:
                            print 'you choose to update the status'
                            spy.current_status_message = add_status()

                        elif menu_choice == 2:
                            print 'You choose to add a friend'
                            # we got the no of friends from the user
                            number_of_friends = add_friend()
                            print 'You have %d friends' % number_of_friends

                        elif menu_choice == 3:
                            print 'You choose to send a secret message'
                            send_message()

                        elif menu_choice == 4:
                            print 'You choose to read message from user'
                            read_message()

                        elif menu_choice == 5:
                            print 'you choose to read chat history'
                            read_chat_history()

                        else:
                            show_menu = False
                    else:
                        print 'enter a valid input'
                else:
                    print 'enter only a valid input'
        else:
            print 'sorry you are not of the valid age'


    # our actual program start from here and create dictionay of name spy and do code refactoring
    if existing.upper() == 'Y':
        start_chat(spy)
        startapp = False
    elif existing.upper() == 'N':
        spy = Spy('', '', 0, 0.0)
        spy.name = raw_input('Welcome to spy chat, Enter your spyname first')
        # checking for the valid name
        if spy.name.isalpha():
            if len(spy.name) > 0:
                spy.salutation = raw_input('Should we call you a Mr. or Miss.or Dr. or anything else')
                spy.age = raw_input('Please enter your age')
                # checking for the valid age
                if spy.age.isdigit():
                    spy.age = int(spy.age)
                    spy.rating = float(raw_input('Enter your spy rating'))
                    start_chat(spy)
                else:
                    print 'enter age only in valid datatype'
            else:
                print 'Please enter a spyname only in character no spaces are allowed and try again'
        else:
            print 'Please enter only characters and no spaces alllowed and try again'
        start_app = False
    else:
        print "please enter a valid response in 'Y' or 'N'"
