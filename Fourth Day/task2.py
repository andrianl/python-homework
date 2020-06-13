
email=input('Введіть ваш email:')
email_secure=input('Підтвердіть ваш email:')

email=email.split()
email=''.join(email)

email_secure=email_secure.split()
email_secure=''.join(email_secure)
email.lower()
email_secure.lower()
if email == email_secure:
    print('OK!')
    pass
else:
    print("Пошти не співпадають!")
