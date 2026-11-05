s = "A race car, $ a"

delete_chars = " 1234567890!@#$%^&*"
table = str.maketrans("", "", delete_chars)

new_str = s.translate(table)

rev_str = new_str.reverse()

print(rev_str)