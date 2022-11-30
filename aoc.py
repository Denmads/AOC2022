import loader
import sys

def main(task_id: str):
    task = loader.load_task(task_id)
    input_txt = loader.load_input(task_id)
    task.run(input_txt)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: aoc.py <task_id, eg. 12b>")
        exit()
    
    main(sys.argv[1])