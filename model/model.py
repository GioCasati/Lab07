from database.meteo_dao import MeteoDao


class Model:
    def __init__(self):
        pass

    def get_mean_humidity(self, month):
        return MeteoDao.get_mean_humidity(month)

    def get_sequence(self, month):
        situations = MeteoDao.get_situations_month(month)
        print(situations)
        return [[1, "Genova"]]