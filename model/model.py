from database.meteo_dao import MeteoDao
from model.situazione import Situazione
from datetime import datetime
from copy import deepcopy



class Model:
    def __init__(self):
        #self._minimum_cost_pattern = [] non serve, current attempt fa il suo lavoro
        self._current_attempt = []
        self._min_cost = float('inf')

    def get_mean_humidity(self, month):
        return MeteoDao.get_mean_humidity(month)

    def get_sequence(self, month):
        situations = MeteoDao.get_situations_month(month, 15)
        self._current_attempt = []
        self._min_cost = float('inf')
        self._get_minimum_cost_pattern([], deepcopy(situations), 0)
        for day in self._current_attempt:
            print(day)
        print(self._min_cost)

    def _get_minimum_cost_pattern(self, current_pattern, remaining, current_cost):
        if len(current_pattern) == 1:
            print()
        if len(current_pattern) == 2:
            print()
        if len(current_pattern) == 3:
            print()
        if len(current_pattern) == 4:
            print()
        if len(current_pattern) == 5:
            print()
        if len(current_pattern) == 6:
            print()
        if len(current_pattern) == 7:
            print()
        if len(current_pattern) == 8:
            print()
        if len(current_pattern) == 9:
            print()
        if len(current_pattern) == 10:
            print()
        if len(current_pattern) == 11:
            print()
        if len(current_pattern) == 12:
            print()
        if len(current_pattern) == 13:
            print()
        if len(current_pattern) == 14:
            print()
        if len(current_pattern) == 15:
            print()

        if not remaining:
            if current_cost < self._min_cost:
                self._current_attempt = deepcopy(current_pattern) # aggiunta qui deepcopy e sotto
                self._min_cost = current_cost
        else:
            for option in remaining[0]:
                options = self._get_alternatives(current_pattern, remaining, current_cost)
                if option in options:
                    change = False
                    if len(current_pattern) > 0 and option.localita != current_pattern[-1].localita:
                        current_cost += 100
                        change = True
                    current_pattern.append(option)
                    current_cost += option.umidita
                    new_remaining = deepcopy(remaining[1:])  #aggiunta qui
                    self._get_minimum_cost_pattern(current_pattern, new_remaining, current_cost)
                    current_pattern.pop()
                    current_cost -= option.umidita
                    if change:
                        current_cost -= 100

    def _get_alternatives(self, current_pattern, remaining, current_cost):
        #if current_cost > self._min_cost:
         #   return []
        if not current_pattern:
            return remaining[0]
        elif len(current_pattern) < 3:
            return [s for s in remaining[0] if s.localita == current_pattern[-1].localita]
        else:
            cnt_genova = len([s for s in current_pattern if s.localita == "Genova"])
            cnt_milano = len([s for s in current_pattern if s.localita == "Milano"])
            cnt_torino = len([s for s in current_pattern if s.localita == "Torino"])
            can_change = current_pattern[-1].localita == current_pattern[-2].localita == current_pattern[-3].localita
            if not can_change:
                if len([s for s in current_pattern if s.localita == current_pattern[-1].localita]) < 6:
                    return [s for s in remaining[0] if s.localita == current_pattern[-1].localita]
                else:
                    return []
            else:
                options = deepcopy(remaining[0]) # aggiunta qui
                to_remove = []
                if cnt_genova >= 6:
                    for option in options:
                        if option.localita == "Genova":
                            to_remove.append(option)
                            
                if cnt_milano >= 6:
                    for option in options:
                        if option.localita == "Milano":
                            to_remove.append(option)

                if cnt_torino >= 6:
                    for option in options:
                        if option.localita == "Torino":
                            to_remove.append(option)

                if len(to_remove) > 0:
                    for option in to_remove:
                        options.remove(option)

                return options
