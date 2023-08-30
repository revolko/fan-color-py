import psutil


def get_avg_temperature():
    temps = psutil.sensors_temperatures()
    sensors_num = 0
    total_temp = 0

    for component, sensors in temps.items():
        for sensor in sensors:
            sensors_num += 1
            total_temp += sensor.current

    return int(total_temp / sensors_num)
