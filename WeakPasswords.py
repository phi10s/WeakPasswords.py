#!/usr/bin/env python3
# WeakPasswords.py - David Lane @phi10s - Scorpion Labs
# Based on weakpass_generator.py by @nyxgeek - TrustedSec

# Generates weak passwords based on the current date, company name, and other names.
# Allows minimum length restrictions for various password policies.

import datetime
from datetime import datetime, timedelta
import argparse

# Define our Months and Keywords for Prefixes
monthDictionary = {
    "January": ["January", "Winter"],
    "February": ["February", "Winter"],
    "March": ["March", "Winter", "Spring", "Springishere", "Springtime"],
    "April": ["April", "Spring", "Springishere", "Springtime"],
    "May": ["May", "Spring", "Springishere", "Springtime"],
    "June": ["June", "Summer", "Summertime"],
    "July": ["July", "Summer", "Summertime"],
    "August": ["August", "Summer", "Fall", "Autumn"],
    "September": ["September", "Fall", "Autumn"],
    "October": ["October", "Fall", "Autumn", "Winter"],
    "November": ["November", "Fall", "Autumn", "Winter", "Thanksgiving"],
    "December": ["December", "Winter", "Christmas"]
}

standardList = ["password", "Password", "Password1", "Password1!", "Password123", "Password123!", "P@$$w0rd"]

OUTPUT_LIST = []

def create_passwords(tempdate, company_name, other_names, thorough, min_length):
    global OUTPUT_LIST

    for password in standardList:
        if len(password) >= min_length:
            OUTPUT_LIST.append("%s" % password)

    year_short = tempdate.strftime("%y")
    year_long = tempdate.strftime("%Y")
    current_month = tempdate.strftime("%B")

    SUFFIX_ARRAY = [year_short, year_long, "@" + year_short, "@" + year_short + "!", "@" + year_long, "@" + year_long + "!", year_short + "!", year_long + "!", "1", "123"]

    for month_prefix in monthDictionary[current_month]:
        for password_suffix in SUFFIX_ARRAY:
            if len(month_prefix + password_suffix) >= min_length:
                OUTPUT_LIST.append("%s%s" % (month_prefix, password_suffix))
            if company_name:
                if len(company_name + password_suffix) >= min_length:
                    OUTPUT_LIST.append("%s%s" % (company_name, password_suffix))
                if thorough and len(company_name + month_prefix + password_suffix) >= min_length:
                    OUTPUT_LIST.append("%s%s%s" % (company_name, month_prefix, password_suffix))
            for name in other_names:
                if len(name + password_suffix) >= min_length:
                    OUTPUT_LIST.append("%s%s" % (name, password_suffix))
                if thorough and len(name + month_prefix + password_suffix) >= min_length:
                    OUTPUT_LIST.append("%s%s%s" % (name, month_prefix, password_suffix))

def main():
    parser = argparse.ArgumentParser(description='Generate weak passwords based on current date and optional parameters.')
    parser.add_argument('-c', '--company', type=str, help='Optional company name to include in passwords')
    parser.add_argument('-t', '--thorough', action='store_true', help='Include thorough combinations of company name, month prefix, and suffix')
    parser.add_argument('-n', '--names', type=str, nargs='*', help='List of other names to include in passwords')
    parser.add_argument('-m', '--min_length', type=int, default=0, help='Minimum length of the output passwords')
    args = parser.parse_args()

    company_name = args.company if args.company else ""
    other_names = args.names if args.names else []
    thorough = args.thorough
    min_length = args.min_length

    for numberofdays in range(1, 90):
        tempdate = datetime.now() - timedelta(days=numberofdays)
        create_passwords(tempdate, company_name, other_names, thorough, min_length)

    # Print the unique ones
    #print("Here are the results:")

    OUTPUT_LIST.sort()
    output_set = sorted(set(OUTPUT_LIST))

    # Open file to write to
    with open("latest_passwords.txt", "w") as outfile:
        for candidate_password in output_set:
            print(candidate_password)
            outfile.write(candidate_password + "\n")


if __name__ == "__main__":
    main()
