def run_timing():
    runs = 0
    time = 0

    while True:
        run_time = input("Enter 10 km run time: ")
        if not run_time:
            break
        runs += 1
        time += float(runs)

    average = time / runs
    print(f"Average: {average}, Runs: {runs}")


run_timing()