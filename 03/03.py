with open("03.in", "r") as f:
    input = [list(line) for line in f.read().strip().splitlines()]
    
M, N = len(input), len(input[0])
directions = [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1)]    
in_bounds = lambda x, y: 0 <= x < M and 0 <= y < N

part_numbers, gear_ratios = 0, 0
for i in range(M):
    for j in range(N):
        if input[i][j] != '.' and not input[i][j].isdigit():
            part_numbers_around, seen_positions = [], set()
            # look for digits around
            for di, dj in directions:
                x, y = i + di, j + dj
                if in_bounds(x, y) and input[x][y].isdigit():
                    # search for the full number to the left or to the right
                    buffer = [(input[x][y], (x, y))]
                    a, b = x, y - 1                    
                    while in_bounds(a, b) and input[a][b].isdigit():
                        buffer = [(input[a][b], (a, b))] + buffer
                        a, b = a, b - 1
                        
                    a, b = x, y + 1
                    while in_bounds(a, b) and input[a][b].isdigit():
                        buffer = buffer + [(input[a][b], (a, b))]
                        a, b = a, b + 1
                        
                    # check if we added already the same number
                    some_current_position = buffer[0][1]
                    if some_current_position not in seen_positions:
                        seen_positions.update([position for _, position in buffer])
                        part_numbers_around.append(int(''.join(digit for digit, _ in buffer)))

            part_numbers += sum(part_numbers_around)
            if input[i][j] == '*' and len(part_numbers_around) == 2:
                gear_ratios += part_numbers_around[0] * part_numbers_around[1]
                
print(part_numbers)
print(gear_ratios)