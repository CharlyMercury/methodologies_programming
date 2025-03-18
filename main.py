import sys
from src.generate_full_names import full_name
from src.ramdomcars import random_cars


def run(program_to_run):
    if program_to_run == "fullname":
        print(full_name("Carlos", "Antonio", "Tovar"))
    elif program_to_run == "ramdomcars":
        random_cars()
    

if __name__ == "__main__":
    if sys.argv[1] in ["fullname", "ramdomcars", "randomtrucks"]:
        run(sys.argv[1])
    else:
        print("La opción que ingresaste no es válida")