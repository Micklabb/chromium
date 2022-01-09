from collections import Counter
from chromium_db import ChromeDB

def likelihood(entries):
    entries = [str(i).lower() for i in entries if i]
    # If total of real samples is small dont rely on this
    total = len(entries)
    cnt = Counter(entries)
    likelihoods = {k: (v / total) for k, v in cnt.items()}
    return likelihoods

def get_profile(cursor, table):
    cursor.execute(f"SELECT * FROM {table}")
    entries = list(zip(*cursor.fetchall()))[1:]
    result = [likelihood(i) for i in entries]
    return result

def main():
    db_name = "Web Data"
    with ChromeDB(db_name) as db:
        email_profile = get_profile(db.cursor, "autofill_profile_emails")
        phone_profile = get_profile(db.cursor, "autofill_profile_phones")
        print(email_profile, phone_profile)
        

if __name__ == "__main__":
    main()

# phone fields: ['guid', 'number']
# autofill_profile_phones

# adress fields: ['guid', 'street_address', 'street_name', 'dependent_street_name', 'house_number', 'subpremise', 'premise_name', 'street_address_status', 'street_name_status', 'dependent_street_name_status', 'house_number_status', 'subpremise_status', 'premise_name_status', 'dependent_locality', 'city', 'state', 'zip_code', 'sorting_code', 'country_code', 'dependent_locality_status', 'city_status', 'state_status', 'zip_code_status', 'sorting_code_status', 'country_code_status', 'apartment_number', 'floor', 'apartment_number_status', 'floor_status']
# autofill_profile_addresses
    # There can be multiple adresses used.
    # use the most likely combination of things

# names fields: ['guid', 'first_name', 'middle_name', 'last_name', 'full_name', 'honorific_prefix', 'first_last_name', 'conjunction_last_name', 'second_last_name', 'honorific_prefix_status', 'first_name_status', 'middle_name_status', 'last_name_status', 'first_last_name_status', 'conjunction_last_name_status', 'second_last_name_status', 'full_name_status', 'full_name_with_honorific_prefix', 'full_name_with_honorific_prefix_status']
# autofill_profile_names

# email fields: ['guid', 'email']
# autofill_profile_emails