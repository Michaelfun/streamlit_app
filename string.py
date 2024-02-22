import configparser
cpass = configparser.RawConfigParser()
cpass.add_section('cred')

with TelegramClient(StringSession(), xid, xhash) as client:
    xstring = (client.session.save())
    cpass.set('cred', 'string', xstring)

    setup = open('string.data', 'w')
    cpass.write(setup)
    setup.close()