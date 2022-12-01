import loader
import sys
import time

def main(day: str, part: str):

    if part != "a" and part != "b":
        print("Part can only be 'a' or 'b'")
        exit(1)

    task = loader.load_task(day)
    input_txt = loader.load_input(day)
    print("")

    start = time.perf_counter()
    if part == "a":
        task.run_a(input_txt)
    elif part == "b":
        task.run_b(input_txt)
    
    exec_time = time.perf_counter() - start
    print("----------------------")
    print(f"It took {exec_time} seconds to run!")
    print("")


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: aoc.py <day> <part>")
        exit()
    
    main(sys.argv[1], sys.argv[2])