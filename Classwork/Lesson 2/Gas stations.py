def gas_stations(distance, tank_size, stations):
    stations.append(distance)
    visited_stations = []
    temp_stations = stations.copy()
    for i in range(len(stations)):
        if i+2 < len(stations):
            if tank_size < stations[i + 1]:
                visited_stations.append(temp_stations[i])
                stations[i+2] -= stations[i]
            else:
                continue

    if tank_size < stations[-1]:
        visited_stations.append(temp_stations[-2])
    return visited_stations


print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]))
print(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]))

# We are implementing a smart GPS software.
# • We are taking a long trip from Sofia to Plovdiv and we know the distance
# between the two cities.It is a positive integer and we mark it as distance.
# • We know how much our car can ride with a full tank of gas. It is a positive
# integer in kilometers. We mark it as tank_size.
# • We have a list of gas stations. We know the distance between Sofia and the
# current gas station. stations = [50, 80, 110, 180, 220, 290] The list is sorted!
# By using this information we will implement a function that returns the
# shortest list of gas stations that we have to visit in order to travel from Sofia to
# Plovdiv. Know that are allways starting with a full tank_size.

[70, 140, 210, 280, 350]