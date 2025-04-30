from dps_calc import calculate_tower_damage, calculate_dps_needed

def main():
    print("======================Bienvenido al calculador de DPS para torres y jefes======================\n")
    print("Este programa te ayudará a calcular el DPS de las torres y el DPS necesario para derrotar a un jefe.")
    print("Puedes elegir entre dos modos de cálculo:")
    print("Seleccione el modo de cálculo:")
    print("1. Calcular el DPS de las torres")
    print("2. Calcular el DPS necesario para derrotar a un jefe en un tiempo determinado")
    mode = input("Ingrese el número del modo (1 o 2): ")

    if mode == '1':
        print("\nModo 1: Calcular el DPS de las torres")
        try:
            damage = float(input("Ingrese el daño por ataque de una torre: "))
            attack_speed = float(input("Ingrese la velocidad de ataque (en segundos): "))
            towers = int(input("Ingrese el número de torres: "))
            
            result = calculate_tower_damage(damage, attack_speed, towers)
            print(f"\nDPS por torre: {result['dps_per_tower']:.2f}")
            print(f"DPS total: {result['total_dps']:.2f}")
        except ValueError as e:
            print(f"Error: {e}")

    elif mode == '2':
        print("\nModo 2: Calcular el DPS necesario para derrotar a un jefe")
        try:
            boss_hp = float(input("Ingrese la vida del jefe: "))
            towers = int(input("Ingrese el número de torres: "))
            time_limit = float(input("Ingrese el tiempo límite (en segundos): "))

            required_dps = calculate_dps_needed(boss_hp, towers, time_limit)
            print(f"\nDPS necesario por torre para derrotar al jefe en {int(time_limit)} segundos: {required_dps:.2f}")
        except ValueError as e:
            print(f"Error: {e}")

    else:
        print("Modo no válido. Saliendo del programa.")

if __name__ == "__main__":
    main()