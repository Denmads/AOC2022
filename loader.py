import importlib
import os

class TaskInterface:
        
    @staticmethod
    def run(input: str) -> None:
        """Runs the task"""

def _import_task(name: str) -> TaskInterface:
    return importlib.import_module(name)

def load_task(task_id: str) -> TaskInterface:
    try: 
        task = _import_task(f"tasks.{task_id}")
        return task
    except ImportError as e:
        print(e)
        print(f"No task found with name: {task_id}.py")
        exit(1)

    
def load_input(task_id: str) -> str:
    day = task_id[:1] if len(task_id) == 2 else task_id[:2]
    
    try:
        with open(f"inputs/{day}.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"No input with name: {day}.txt")
        exit(1)
        