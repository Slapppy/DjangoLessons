from board.advertisement.models import Musician , Membership

member = Membership(name='ACDC', date_joined='27.05.2003', invite_reason='Good Player')
member.save()