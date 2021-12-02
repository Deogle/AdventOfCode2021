def solve(part):
    with open("./day2/input.txt") as file:
        # parsing
        lines = file.readlines()
        input = []
        for line in lines:
            input.append(line.strip().split(" "))
        # solving
        horizontal = 0
        depth = 0
        aim = 0
        for instruction in input:
            dir = instruction[0]
            val = int(instruction[1])
            if(dir == "forward"):
                horizontal += val
                if(part == 2):
                    depth += aim * val
            if(dir == "down"):
                if(part == 1):
                    depth += val
                else:
                    aim += val
            elif(dir == "up"):
                if(part == 1):
                    depth -= val
                else:
                    aim -= val
        print(horizontal * depth)


solve(1)
solve(2)
