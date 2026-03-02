# Глобальная переменная
global_var = 10

def demonstrate_scope():
    # Локальная переменная с тем же именем
    local_var = 20
    # Попытка изменить глобальную переменную без global
    global_var = 30
    print("Внутри функции:")
    print("  global_var (локальная, создана внутри):", global_var)
    print("  local_var (локальная):", local_var)

def change_global():
    # Указываем, что хотим использовать глобальную переменную
    global global_var
    # Теперь изменяем именно глобальную переменную
    global_var = 100
    print("Внутри функции change_global:")
    print("  global_var (глобальная, изменена):", global_var)

# Основная программа
if __name__ == "_main_":
    print("До вызова функций:")
    print("  global_var =", global_var)
    
    print("\n--- Вызов demonstrate_scope() ---")
    demonstrate_scope()
    print("После demonstrate_scope():")
    print("  global_var =", global_var)  # Не изменилась!
    
    print("\n--- Вызов change_global() ---")
    change_global()
    print("После change_global():")
    print("  global_var =", global_var)  # Изменилась!