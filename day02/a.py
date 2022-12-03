scores = {'X': 1, 'Y': 2, 'Z': 3}
wins = {'A': 'Y', 'B': 'Z', 'C':'X'}
losses = {'A':'Z', 'B':'X', 'C':'Y'}
score = 0
with open('input.txt') as f:
    for l in f:
        O, M = l.strip().split()
        outcome = 6 if M == wins[O] else (0 if M == losses[O] else 3)
        score += scores[M] + outcome
        print(outcome)
print(score)
