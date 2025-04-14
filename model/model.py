from database.meteo_dao import MeteoDao
from model.situazione import Situazione
from datetime import datetime
from copy import deepcopy



class Model:
    def __init__(self):
        self._optimal_pattern = []
        self._optimal_cost = float('inf')


    def get_mean_humidity(self, month):
        return MeteoDao.get_mean_humidity(month)


    def get_optimal_sequence(self, month):
        situations = MeteoDao.get_situations_month(month, 15)
        self._optimal_pattern = []
        self._optimal_cost = float('inf')
        self._recursion([], situations, 0)
        return self._optimal_pattern, self._optimal_cost


    def _recursion(self, current_pattern, situations, current_cost):
        if len(current_pattern) == len(situations):
            if current_cost < self._optimal_cost:
                self._optimal_pattern = deepcopy(current_pattern) # aggiunta qui deepcopy e sotto
                self._optimal_cost = current_cost
        else:
            for option in situations[len(current_pattern)]:
                if self._is_admissible(current_pattern, option, current_cost):
                    change = False
                    if len(current_pattern) > 0 and option.localita != current_pattern[-1].localita:
                        current_cost += 100
                        change = True
                    current_pattern.append(option)
                    current_cost += option.umidita
                    self._recursion(current_pattern, situations, current_cost)
                    current_pattern.pop()
                    current_cost -= option.umidita
                    if change:
                        current_cost -= 100


    def _is_admissible(self, current_pattern, option, current_cost):
        if current_cost > self._optimal_cost:
            return False
        if 0 < len(current_pattern) < 3:
            return option.localita == current_pattern[-1].localita
        elif len(current_pattern) >= 3:
            counter = 0
            for day in current_pattern:
                if day.localita == option.localita:
                    counter += 1
            return (counter < 6 and
                    (current_pattern[-1].localita == current_pattern[-2].localita == current_pattern[-3].localita or
                     option.localita == current_pattern[-1].localita))
        else:
            return True