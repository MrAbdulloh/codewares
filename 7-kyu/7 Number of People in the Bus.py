# first method
def number(bus_stops: list):
    xx = 0
    for bus in bus_stops:
        xx += bus[0] - bus[1]

    return xx


print(number([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]]))


# secend method
def numbers(bus_stops: list):
    return sum([bus[0] - bus[1] for bus in bus_stops])


print(numbers([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]]))
