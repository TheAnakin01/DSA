height_str, width_str = input().split()
height = int(height_str)
width = int(width_str)
pattern = ".|."
upper_pattern = []
for i in range(height//2):
    count = i * 2 + 1
    upper_pattern.append(((pattern * count).center(width, "-")))
for pat in upper_pattern:
    print(pat)
print(("WELCOME").center(width, "-"))
for pat in reversed(upper_pattern):
    print(pat)


