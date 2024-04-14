print('LIST GENERATOR')

start = int(input("Start at: "))
end = int(input('End at: '))
inc = int(input('Increment value: '))

for i in range(start, end + 1, inc):
  print("\033[35m",i)