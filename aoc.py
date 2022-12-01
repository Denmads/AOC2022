import loader
import sys

def main(day: str, part: str):
    task = loader.load_task(day)
    input_txt = loader.load_input(day)

    if part == "a":
        task.run_a(input_txt)
    elif part == "b":
        task.run_b(input_txt)
    else:
        print("Part can only be 'a' or 'b'")


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: aoc.py <day> <part>")
        exit()
    
    main(sys.argv[1], sys.argv[2])