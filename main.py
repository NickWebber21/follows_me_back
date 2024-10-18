import csv

def load_usernames(filename):
    with open(filename, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        next(reader, None)
        usernames = set()
        for row in reader:
            if row:
                if len(row) > 1:
                    username = row[1].strip()
                else:
                    username = row[0].strip()
                if username and username != "Followers username":
                    usernames.add(username)
    return usernames

followers = load_usernames('followers.csv')
following = load_usernames('following.csv')

not_following_back = following - followers

print('People not following me back:')
for user in not_following_back:
    print(user)

print(f"\nTotal following: {len(following)}")
print(f"Total followers: {len(followers)}")
print(f"Number of users not following back: {len(not_following_back)}")

with open('followers.csv', 'r', encoding='utf-8-sig') as f:
    followers_rows = sum(1 for row in f) - 1  # Subtract 1 for header

with open('following.csv', 'r', encoding='utf-8-sig') as f:
    following_rows = sum(1 for row in f) - 1  # Subtract 1 for header

print(f"\nTotal rows in followers.csv: {followers_rows}")
print(f"Total rows in following.csv: {following_rows}")
