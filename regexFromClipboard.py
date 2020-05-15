import re, pyperclip

# Collects phone numbers
phoneRegex = re.compile(r'''
# number types: 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 21345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?    # area code (optional)
(\s|-)                      # first separator
\d\d\d                      # first 3 digits
-                           # second separator
\d\d\d\d                    # last 4 digits
(((ext(\.)?\s)|x)           # extension word (optional)
 (\d{2,5}))?                # extension number (optional)
)
''', re.VERBOSE)

# Collects email addresses
emailRegex = re.compile(r'''
# some.+_thing@(\d{2,5}))?.com

[a-zA-z0-9_.+]+         # First part of email
@                       # @ symbol
[a-zA-z0-9_.+]+         # Domain name

''', re.VERBOSE)

# pull copied items out of the clipboard
text = pyperclip.paste()

# search the pasted text for our designated Regex
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

# append all the phone numbers into one list
allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# take all the emails and place them into one gigantic string
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
# send that gigantic string to the clipboard to be pasted elsewhere
pyperclip.copy(results)