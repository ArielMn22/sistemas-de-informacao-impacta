x = int(input())
y = int(input())

i = 0

btCount = 0
bdCount = 0
bnCount = 0

while (i < x):
  
  print('bom dia')
  bdCount += 1

  j = 0

  while (j < y):

    print('boa tarde')
    btCount += 1 
  
    j += 1

  i += 1

print('boa noite')
bnCount += 1

print("btCount", btCount)
print("bdCount", bdCount)
print("bnCount", bnCount)