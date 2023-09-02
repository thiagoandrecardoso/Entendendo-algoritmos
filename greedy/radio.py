states_cover = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}

stations = {"k1": {"id", "nv", "ut"},
            "k2": {"wa", "id", "mt"},
            "k3": {"or", "nv", "ca"},
            "k4": {"nv", "ut"},
            "k5": {"ca", "az"}}

final_stations = set()

while states_cover:
    best_station = None
    states_covered = set()
    for station, state_by_stations in stations.items():
        covered = states_cover & state_by_stations
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_cover -= states_covered
    final_stations.add(best_station)


print(final_stations)

