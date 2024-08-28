import json
import os

#Giovana Sierpinski Pascoal da Silva | Materia: DevOps | Projeto Organizador de Atividades da Faculdade

def load_tasks(filename="tasks.json"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks, task_name, subject):
    tasks.append({"name": task_name, "subject": subject, "completed": False})
    save_tasks(tasks)
    print(f"Atividade '{task_name}' de '{subject}' adicionada.")

def list_tasks(tasks):
    if not tasks:
        print("Nenhuma atividade foi encontrada.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✓" if task["completed"] else "ㄨ"
            print(f"{i}. {task['name']} - {task['subject']} [{status}]")

def complete_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        save_tasks(tasks)
        print(f"Atividade '{tasks[task_index]['name']}' de '{tasks[task_index]['subject']}' marcada como concluída.")
    else:
        print("Opção inválida.")

#Para remover
def remove_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f"Atividade '{removed_task['name']}' de '{removed_task['subject']}' removida.")
    else:
        print("Opção inválida.")

# Menu de exibição
def main():
    tasks = load_tasks()

    while True:
        print("\nOrganizador de Atividades da Faculdade")
        print("----------------𓆩✧𓆪------------------")
        print("1. Adicionar atividade")
        print("2. Listar atividades")
        print("3. Marcar atividade como concluída")
        print("4. Remover atividade")
        print("5. Sair")
        print("✧︶︶︶✧︶︶︶✧︶︶︶✧︶︶︶✧︶︶︶✧")

        choice = input("Digite o número de uma opção: ")

        if choice == "1":
            task_name = input("Digite o nome da atividade: ")
            subject = input("Digite a matéria: ")
            add_task(tasks, task_name, subject)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            list_tasks(tasks)
            task_index = int(input("Digite o número da atividade a ser concluída: ")) - 1
            complete_task(tasks, task_index)
        elif choice == "4":
            list_tasks(tasks)
            task_index = int(input("Digite o número da atividade a ser removida: ")) - 1
            remove_task(tasks, task_index)
        elif choice == "5":
            break
        else:
            print("Opção inválida.")
 
if __name__ == "__main__":
    main()

