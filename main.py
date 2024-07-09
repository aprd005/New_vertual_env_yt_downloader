def calculate_final_speed(initial_speed, inclinations):
    speed=initial_speed
    for inclines in inclinations:
        speed+= (-inclines)
        if speed<=0:
            return 0
    return speed    
print(calculate_final_speed(60, [0, 30, 0, -45, 0]))