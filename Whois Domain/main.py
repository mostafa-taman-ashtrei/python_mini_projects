import whois
from prettytable import PrettyTable

checking_urls = True

while checking_urls:
    print("Enter the url you want to look up or press q to exit:")
    user_input = input("")

    if user_input == 'q':
        checking_urls = False

    else:
        table = [
            ["Url", "Organization", "Domains", "Country",  "Creation Date"],
            [
                user_input,
                whois.whois(user_input).org,
                whois.whois(user_input).domain_name,
                whois.whois(user_input).country,
                whois.whois(user_input).creation_date,
            ],
        ]

        pretty_table = PrettyTable(table[0])
        pretty_table.add_rows(table[1:])

        print(pretty_table)
