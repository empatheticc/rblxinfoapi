import requests
import re

# Made by NeminolObelyn with the assistance of ChatGPT(for more difficult levels like number and letter patterns)
# <3

print("""´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´
´´´´´´¶¶´´´´¶¶¶¶¶´´¶¶¶¶´¶¶¶¶´´
´´´´´´¶´´´´´´´´´´¶¶¶¶´¶¶´´´´¶´
´´´´´´¶´´´´´´´´´´¶´¶¶¶¶¶¶´´´¶´
´´´´´¶´´´´´´´´´´¶¶¶¶¶´´´¶¶¶¶¶´
´´´´¶´´´´´´´´´´´´´´´´¶¶¶¶¶¶¶¶´
´´´¶´´´´´´´´´´´´´´´´´´´¶¶¶¶¶´´
´¶¶¶´´´´´¶´´´´´´´´´´´´´´´´´¶´´
´´´¶´´´´¶¶´´´´´´´´´´´´´´´´´¶´´
´´´¶¶´´´´´´´´´´´´´´´´¶¶´´´´¶´´
´´¶¶¶´´´´´´´´´¶¶¶´´´´¶¶´´´¶¶´´
´´´´´¶¶´´´´´´´´´´´´´´´´´´¶¶¶´´
´´´´´´´¶¶¶´´´´´´´´´´´´´¶¶¶´´´´
´´´¶¶¶¶¶´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´
´´´¶´´´´¶¶¶¶¶´´´´¶¶¶¶´´´¶´´´´´
´´´¶´´´´¶¶¶´¶¶¶¶¶¶¶¶´´´¶¶¶´´´´
´´´¶¶¶¶¶¶¶¶¶¶¶¶¶´´¶¶¶¶¶´´´¶¶´´
´´¶´´´´´´¶¶¶¶¶¶¶¶¶¶¶´´´´´´´¶´´
´¶´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´´¶´´
´´¶´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´´¶´´
´´¶¶´´´´´´´¶¶´´´´¶¶´´´´´´¶¶´´´
´´´´¶¶¶¶¶¶¶´´´´´´´´¶¶¶¶¶¶´´´´´
    \n""")
print("- made by neminolobelyn\n")

def is_alt_account(username):
    alt_keywords = ["alt", "alternate", "backup", "acc"]
    excess_numbers_pattern = re.compile(r'\D*\d\D*\d\D*\d\D*')
    gibberish_letters_pattern = re.compile(r'\d*[^a-zA-Z\d]+\D*[^a-zA-Z\d]+\D*[^a-zA-Z\d]+\D*')
    has_alt_keyword = any(keyword in username.lower() for keyword in alt_keywords)
    has_excess_numbers = bool(excess_numbers_pattern.search(username))
    has_gibberish_letters = bool(gibberish_letters_pattern.search(username))
    return has_alt_keyword or has_excess_numbers or has_gibberish_letters


def get_account_info(account_id):
    url = f"https://users.roblox.com/v1/users/{account_id}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        account_info = response.json()
        return account_info
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None

def get_groups(account_id):
    url = f"https://groups.roblox.com/v1/users/{account_id}/groups/roles"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        groups_info = response.json()
        return groups_info
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None

def write_groups_to_file(groups_info, filename):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"<3 - neminolobelyn \n")
            for group in groups_info["data"]:
                file.write(f"Group Name: {group['group']['name']}\n")
                file.write(f"Group ID: {group['group']['id']}\n")
                file.write(f"Role in Group: {group['role']['name']}\n")
                file.write("-----\n")
        
        print(f"Group information has been written to {filename} successfully.")
    except IOError as e:
        print(f"Error occurred while writing to file: {e}")

if __name__ == "__main__":
    account_id = int(input("Insert the account ID you want to fetch information for: \n"))
    account_info = get_account_info(account_id)
    groups_info = get_groups(account_id)
    
    if account_info:
        print(f"\nAccount Information for ID {account_id}:\n")

        print("Username:", account_info["name"])
        print("Display Name:", account_info["displayName"])
        print("Description:", account_info["description"])
        print("Date of Creation:", account_info["created"])
        print("Banned:", account_info["isBanned"])
        print("")

        is_alt = is_alt_account(account_info["name"])
        if is_alt:
            print("This account might be an alternate account.")
        else:
            print("This account may be a legitimate account, however, do remember to check the profile.")
            print(f"Go to https://www.roblox.com/users/{account_id}/profile to verify my claims. Again, I'm just a silly .py file with limited access to the creme de la creme that is Roblox API.")
        
    else:
        print("Failed to retrieve account information.")

    if groups_info:
        write_groups_to_file(groups_info, "group_info.txt")
    else:
        print("Failed to retrieve group information.")
