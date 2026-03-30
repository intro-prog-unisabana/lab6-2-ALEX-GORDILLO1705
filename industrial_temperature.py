def trigger_alarm(temperatures, threshold=80):
    result = []

    for sensor, temp in temperatures.items():
        if temp > threshold:
            result.append(sensor)

    return result