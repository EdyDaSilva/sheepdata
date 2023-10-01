import csv
import re


# create csv file
# with open("sheep_data.csv", "w+") as file:
#     myFile = csv.writer(file)
#     myFile.writerow(["ID Tag", "DOB", "Sex", "Other Info"])

def check_existing_id_tags():
    existing_id_tags = set()  # Create a set to store existing id_tags
    with open("sheep_data.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            existing_id_tags.add(int(row[0]))  # id_tag is in the first column (index 0)
    return existing_id_tags


def append_to_csv():
    existing_id_tags = check_existing_id_tags()

    while True:
        id_tag = input("Enter ID Tag: ")

        if id_tag.isdigit():
            id_tag = int(id_tag)
            if id_tag in existing_id_tags:
                print("ID Tag entered already exists. Please enter a different one.")
            else:
                break
        else:
            print("Please enter a valid number for ID Tag.")

    while True:
        dob = input("Enter DOB (YYYY-MM-DD): ")
        if re.match(r'^\d{4}-\d{2}-\d{2}$', dob):
            break
        else:
            print("Please enter a valid date in the format YYYY-MM-DD.")

    while True:
        sex = input("Enter Sex (M/F): ").upper()
        if sex in ['M', 'F']:
            break
        else:
            print("Please enter 'M' for male or 'F' for female.")

    other_info = input("Enter Other Info: ")
    if not other_info:
        other_info = "N/A"

    with open("sheep_data.csv", "a", newline="") as file:
        myFile = csv.writer(file)
        myFile.writerow([id_tag, dob, sex, other_info])



# append_to_csv()
'''
function to update other information field
'''
def update():
    f = open("sheep_data.csv", 'r', newline='\n')
    tag_to_find = input("Enter tag N to find: ")
    tag_found = 0
    r = csv.reader(f)
    tag_updated = []
    for rec in r:
        if rec[0] == tag_to_find:
            print("Tag to update is found: ", rec)
            rec[3] = input("Enter Other Info: ")
            if not rec[3]:
                rec[3] = "N/A"
            print("Updated Other Info: ", rec)
            tag_found = 1
        tag_updated.append(rec)

    if tag_found == 0:
        print("Tag does not exist")
        f.close()

    else:
        f = open("sheep_data.csv", 'w', newline='')
        w = csv.writer(f)
        w.writerows(tag_updated)
        f.close()
            

# update()

# Usage
# if __name__ == "__main__":
#     filename = "sheep_data.csv"
#     update(filename)


def choose_action():
    while True:
        choice = input("Enter 'A' to add new object or 'B' to update or 'Q' to quit: ").upper()
        if choice == "A":
            append_to_csv()
        elif choice == "B":
            update()
        elif choice == "Q":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 'a', 'b', or 'q'")


choose_action()
