from datetime import datetime

wait_until = (datetime.now().second + 2) % 60
print(f"We start at {datetime.now().second} seconds")

while datetime.now().second != wait_until:
    pass
print(f"We area at {wait_until} seconds")

wait_until_2 = (datetime.now().second + 2)  % 60
print(f"We start at {datetime.now().second} seconds")

while True:
    if datetime.now().second < wait_until_2:
        continue
    break

print(f"We are at {wait_until_2} seconds")
