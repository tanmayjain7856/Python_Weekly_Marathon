print('Welcome to Love Calculator!')
name1 = input('What is your name?\n')
name2 = input("What is your partner's name?\n")
combinedName = name1 + name2
combinedNameLower = combinedName.lower()
t = combinedNameLower.count('t')
r = combinedNameLower.count('r')
u = combinedNameLower.count('u')
e = combinedNameLower.count('e')
true_score = t + r + u + e
l = combinedNameLower.count('l')
o = combinedNameLower.count('o')
v = combinedNameLower.count('v')
e = combinedNameLower.count('e')
love_score = l + o + v + e
total_score = int(str(true_score) + str(love_score))
if total_score <= 20:
    print(
        f'Your score is {total_score}% and you go together like coke and mentos.')
elif total_score > 20 and total_score <= 60:
    print(f'Your love score is {total_score}% and you are alright together.')
else:
    print(f'Your love score is {total_score}% and you are having a blast.')
