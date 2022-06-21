import logger as log
import data_provider as dt
import check_module as ch
import checking_file as chfl

number = (input('Для поиска контакта нажмите 1, для добавления нажмите 2: '))
number = ch.check(number)

contact = dt.get_contact(number)
# print (contact)

log.request_contact_logger(contact, number)

contact_list = chfl.check_file('guide.txt', contact)

print (contact_list)