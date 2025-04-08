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

    def handle_umidita_media(self, e):
        self._view.lst_result.clean()
        month = self._mese
        if month is None or month == 0:
            self._view.create_alert("Select a month")
            self._view.update_page()
            return
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
        for day in self._model.get_sequence(month):
            self._view.lst_result.controls.append(ft.Text(f"Day {day[0]}: {day[1]}"))
        self._view.update_page()

    def read_mese(self, e):
        self._mese = int(e.control.value)

