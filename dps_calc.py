def calculate_tower_damage(damage, attack_speed, towers):
    if damage < 0:
        raise ValueError("El daño debe ser un número positivo.")
    if attack_speed <= 0:
        raise ValueError("La velocidad de ataque debe ser mayor que cero.")
    if towers <= 0:
        raise ValueError("El número de torres debe ser mayor que cero.")
    
    dps_per_tower = damage / attack_speed
    total_dps = dps_per_tower * towers
    
    return {
        'dps_per_tower': dps_per_tower,
        'total_dps': total_dps
    }

def calculate_dps_needed(boss_hp, towers, time_limit):
    if towers <= 0:
        raise ValueError("El número de torres debe ser mayor que cero.")
    if boss_hp <= 0:
        raise ValueError("La vida del jefe debe ser mayor que cero.")
    if time_limit <= 0:
        raise ValueError("El tiempo límite debe ser mayor que cero.")
    
    required_dps = boss_hp / (time_limit * towers)
    return required_dps


    