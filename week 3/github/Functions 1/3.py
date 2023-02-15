def puzzle(legs, heads):
    for i in range(1, heads + 1):
        if (i * 4) + (heads - i) * 2 == legs:
            n = f"{i} rabbits,{heads - i} chickens"
            return n

legs = int(input())

heads = int(input())
print(puzzle(legs, heads))