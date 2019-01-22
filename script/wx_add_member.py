from time import sleep

from wxpy import *

bot = Bot()

group = bot.groups().search('幸福一家人')[0]


def query_add_member_msg(text):
    sleep(15)
    msgs = bot.messages
    return [msg for msg in msgs if msg.text == text]


def add_member(users, group):
    try:
        group.add_members(users, use_invitation=True)
        return group
    except ResponseError:
        return None


def query_add_friend_msg(text):
    sleep(15)
    msgs = bot.messages
    return [msg for msg in msgs if msg.text == text]


while True:
    add_friends = query_add_friend_msg('make friend')
    if add_friends:
        for msg in add_friends:
            new_user = msg.card
            bot.accept_friend(new_user)
            bot.messages.remove(msg)

    add_members = query_add_member_msg('add member')
    if add_members:
        for msg in add_members:
            this_user = msg.sender
            add_member(this_user, group)
            bot.messages.remove(msg)
