heading = "Message:"
detail = "Welcome to brainzima"

print(heading, detail)

# left just
print(heading.ljust(30),detail)

# right just
print(heading, detail.rjust(30))


# ljust with str
print(heading.ljust(30, '-'), detail)