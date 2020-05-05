import sys, pyowm
from PyQt5 import QtCore, QtGui, QtWidgets
from test import Ui_Pogoda

app = QtWidgets.QApplication(sys.argv)

Pogoda = QtWidgets.QDialog()
ui = Ui_Pogoda()
ui.setupUi(Pogoda)
Pogoda.show()

def get_weather_city():
	owm = pyowm.OWM('2f1256aedd34bf6bf104b29bf3221699', language = "ru")
	what = ui.lineEdit.text()

	observation = owm.weather_at_place(what)
	w = observation.get_weather()
	temp = w.get_temperature('celsius')["temp"]
	wind = w.get_wind()['speed']
	humidity = w.get_humidity()
	status = w.get_detailed_status()
	ui.label.setText("Температура: " + str(temp) + " C")
	ui.label_2.setText("Ветер: " + str(wind) + " м/с")
	ui.label_3.setText("Влажность: " + str(humidity) + " %")
	ui.label_4.setText(status)

ui.pushButton.clicked.connect(get_weather_city)

sys.exit(app.exec_())