scores = {'X': 1, 'Y': 2, 'Z': 3}
wins = {'A': 'Y', 'B': 'Z', 'C':'X'}
draws = {'A':'X', 'B':'Y', 'C':'Z'}
losses = {'A':'Z', 'B':'X', 'C':'Y'}

# A,X Rock, B,Y Paper, C,Z Scissors

score = 0
with open('input.txt') as f:
    for l in f:
        O, M = l.strip().split()

        if M == 'X':
            score += 0 + scores[losses[O]]
        elif M == 'Y':
            score += 3 + scores[draws[O]]
        elif M == 'Z':
            score += 6 + scores[wins[O]]
print(score)
