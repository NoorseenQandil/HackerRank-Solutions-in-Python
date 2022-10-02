import re

def fun(string):
    # return True if s is a valid email, else return False
    if string.count("@") == 1 and string.count('.') ==1:
        esplit = string.split('@')
        user =esplit[0]
        web = esplit[1].split('.')[0]
        ext = esplit[1].split('.')[1]
        return all([check_user(user),check_web(web),check_ext(ext)])
    else:
        return False


def check_user(strg, search=re.compile(r'[^a-zA-Z0-9-_]').search):
    lenght = True if len(strg)>0 else False
    return all([lenght,not(bool(search(strg)))])

def check_web(strg,search=re.compile(r'[^a-zA-Z0-9]').search):
    lenght = True if len(strg)>0 else False
    return all([lenght,not(bool(search(strg)))])

def check_ext(strg):
    lenght = False
    if len(strg) <= 3 and len(strg)>0:
        lenght = True
    return lenght
    

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
