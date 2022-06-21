def find_text(text, surname):
    surname_sp = surname.split(';')
    if text in surname_sp[0] == True:
        return True