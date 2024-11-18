
def run_task(task_number):
    try:
        task_module = f"tasks.task{task_number}"
        task = __import__(task_module, fromlist=[''])
        if hasattr(task, 'main'):
            task.main()
        else:
            print(f"Task {task_number} does not have a 'main()' function.")
    except ImportError:
        print(f"Task {task_number} does not exist.")

def main():
    print("Choose a task to run:")
    print("1. Vārdu biežuma analīze tekstā")
    print("2. Teksta valodas noteikšana")
    print("3. Vārdu sakritību pārbaude divos tekstos")
    print("4. Noskaņojuma analīze")
    print("5. Teksta tīrīšana un normalizēšana")
    print("6. Automātiska rezumēšana")
    print("7. Vārdu iegulšana")
    print("8. Frāžu atpazīšana")
    print("9. Teksta ģenerēšana")
    print("10. Tulkotājs")
    
    try:
        task_number = int(input("Enter task number: "))
        run_task(task_number)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
