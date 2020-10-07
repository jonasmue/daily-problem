def number_of_rooms(timeslots):
    start_times = sorted([item[0] for item in timeslots])
    end_times = sorted([item[1] for item in timeslots])

    rooms = 0
    while len(start_times):
        start_time = start_times.pop(0)

        if end_times[0] <= start_time:
            end_times.pop(0)
        else:
            rooms += 1

    return rooms


print(number_of_rooms([(30, 75), (0, 50), (60, 150)]))