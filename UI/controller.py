import flet as ft

from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        # other attributes
        self._mese = 0
        self.__calendar = {1:"gennaio", 2:"febbraio", 3:"marzo", 4:"aprile", 5:"maggio", 6:"giugno", 7:"luglio", 8:"agosto", 9:"settembre", 10:"ottobre", 11:"novembre", 12:"dicembre"}

    def handle_umidita_media(self, e):
        self._view.lst_result.clean()
        month = self._mese
        if month is None or month == 0:
            self._view.create_alert("Select a month")
            self._view.update_page()
            return
        self._view.lst_result.controls.append(ft.Text(f"Umidità medie per il mese di {self.__calendar[month]}:", weight=ft.FontWeight.BOLD, size=16))
        for record in self._model.get_mean_humidity(month):
            self._view.lst_result.controls.append(ft.Text(f"{record["Localita"]}: {record["Mean_humidity"]}"))
        self._view.update_page()


    def handle_sequenza(self, e):
        self._view.lst_result.clean()
        month = self._mese
        if month is None or month == 0:
            self._view.create_alert("Select a month")
            self._view.update_page()
            return
        (pattern, cost) = self._model.get_optimal_sequence(month)
        self._view.lst_result.controls.append(ft.Text(f"Pattern di minimo costo per il mese di {self.__calendar[month]}:", weight=ft.FontWeight.BOLD, size=16))
        for day in pattern:
            self._view.lst_result.controls.append(ft.Text(f"{day}"))
        self._view.lst_result.controls.append(ft.Text(f"Costo complessivo: {cost}€", weight=ft.FontWeight.BOLD))
        self._view.update_page()

    def read_mese(self, e):
        self._mese = int(e.control.value)

