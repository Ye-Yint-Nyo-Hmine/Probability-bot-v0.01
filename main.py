# 0 = True, 1 = False

print('Vanila or Chocolate??')

cubic1 = int(input('Do you like super delicious smell?, 1 = True and 0 = False: '))
cubic2 = int(input('Do you like white-yellow or normal-white color?, 1 = white-yellow and 0 = normal-white: '))
cubic3 = int(input('Do you like coffee?, 0 = True and 1 = False: '))

cubic4 = int(input('Do you like crunchy cookie?, 0 = True and 1 = False: '))
cubic5 = int(input('Do you like pen or pencil?, 0 = pen and 1 = pencil: '))
cubic6 = int(input('Do you like a lot of cream in cake?, 0 = True and 1 = False: '))

cubic7 = int(input('Do you like coke or sprite?, 0 = coke and 1 = sprite: '))
cubic8 = int(input('Do you like wearing mask?, 0 = True and 1 = False: '))
cubic9 = int(input('Are you hardworking(answer this honestly!)?, 0 = True and 1 = False: '))

# cubicA

cubicA = 0

if cubic1 + cubic2 + cubic3 <= 1:
    cubicA += 0
if cubic1 + cubic2 + cubic3 >= 2:
    cubicA += 1

# cubicB

cubicB = 0

if cubic4 + cubic5 + cubic6 <= 1:
    cubicB += 0
if cubic4 + cubic5 + cubic6 >= 2:
    cubicB += 1

# cubicC

cubicC = 0

if cubic7 + cubic8 + cubic9 <= 1:
    cubicC += 0
if cubic7 + cubic8 + cubic9 >= 2:
    cubicC += 1

# cubicZ

cubicZ = 0

if cubicA + cubicB + cubicC <= 1:
    cubicZ += 0
if cubicA + cubicB + cubicC >= 2:
    cubicZ += 1

print(cubic1, cubic2, cubic3, cubicA)
print(cubic4, cubic5, cubic6, cubicB)
print(cubic7, cubic8, cubic9, cubicC)
print(cubicA, cubicB, cubicC, cubicZ)

if cubicZ == 0:
    print('There is more probability that you like chocolate ice cream')
if cubicZ == 1:
    print('There is more probability that you like vanilla ice-cream')

