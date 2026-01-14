#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  while(x<5):
    print(x)
    x+=1


  # define a for loop
  for x in range(5,11):
    print(x)

  # use the break and continue statements
  for x in range(11,51):
    if (x == 30) : break
    if (x % 2 == 0) : continue
    print(x)

  # use a for loop over a collection
  days = ["Monday", "Thuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  for d in days:
    print(d)
 

  #using the enumerate() function to get index 
  months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
  for i,m in enumerate(months):
    print(i+1, m)


if __name__ == "__main__":
  main()
