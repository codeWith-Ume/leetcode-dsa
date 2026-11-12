s = input("Enter input: ")

longest = ""

i = 0

while i < len(s):

    j = i + 1

    while j <= len(s):

        substring = s[i:j]

        reverse = substring[::-1]

        if substring == reverse:

            if len(substring) > len(longest):
                longest = substring

        j += 1

    i += 1

print(longest)

# substring = "b"
# reverse = substring[::-1]
# print(reverse)