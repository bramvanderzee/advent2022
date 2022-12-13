import sys

monkeys = {}
fn = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
with open(fn) as f:
    monkey = {}
    for l in f:
        line = l.strip()
        if line == '':
            monkey['insp'] = 0
            monkeys[monkey['num']] = monkey
            monkey = {}
        else:
            if line.startswith('Monkey'):
                num = line.split(':')
                monkey['num'] = int(num[0][7:])
            elif line.startswith('Starting'):
                monkey['items'] = [int(n) for n in line.split(':')[1].split(',')]
            elif line.startswith('Operation'):
                calc = line.split('=')[1]
                c1, op, c2 = calc.split()
                monkey['op'] = op
                monkey['c1'] = c1 if c1 == 'old' else int(c1)
                monkey['c2'] = c2 if c2 == 'old' else int(c2)
            elif line.startswith('Test'):
                monkey['test'] = int(line.split('divisible by ')[1])
            elif line.startswith('If'):
                b = line.split(':')[0][3:]
                to = int(line.split('monkey ')[1])
                monkey[b] = to
    monkey['insp'] = 0
    monkeys[monkey['num']] = monkey

print(monkeys)
for _ in range(20):
    for monkey_index in range(len(monkeys)):
        monkey = monkeys[monkey_index]
        for item in monkey['items']:
            monkey['insp'] += 1
            c1 = item if monkey['c1'] == 'old' else monkey['c1']
            c2 = item if monkey['c2'] == 'old' else monkey['c2']
            item = eval(str(c1) + monkey['op'] + str(c2))

            item = item // 3
            if item%monkey['test'] == 0:
                monkeys[monkey['true']]['items'].append(item)
            else:
                monkeys[monkey['false']]['items'].append(item)
                
        monkey['items'] = []

    print(monkeys)

inspections = []
for monkey in monkeys.values():
    inspections.append(monkey['insp'])
ans = sorted(inspections)
print(ans[-1]*ans[-2])
