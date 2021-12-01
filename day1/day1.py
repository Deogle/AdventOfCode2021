def solve(window_size):
    with open("./day1/input.txt") as file:
        lines = file.readlines()
        input = []
        for line in lines:
            input.append(int(line.strip()))

        result = 0
        windows = []
        for i in range(0, len(input)-window_size+1):
            window = input[i:i+window_size]
            windows.append(sum(window))

        for i in range(0, len(windows)):
            if(i == 0):
                continue
            diff = windows[i-1] - windows[i]
            if(diff < 0):
                result += 1
        print(result)


if __name__ == "__main__":
    solve(1)
    solve(3)
