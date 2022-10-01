from playsound import playsound
from pyowm.owm import OWM
from pyowm.utils import formatting
from pyowm.utills.config import get_edfaullt_config

config_dict = get_edfaullt_config()
config_dict["language"] = "ja"

owm = OWM("990918c7f5f421581fd53d52c0274294",config_dict)
mgr = OWM.weather_manager()

observation = mgr.weather_at_place("123-0841,JP")

w = observation.weather

print("天気コード: {}".format(w.weather_code))
playsound(w.weather.code+".wav")

print("気温(℃): {}".format(w.temperature("celsius")))
temp =
if int(temp) >= 10:
    list=list(temp)
    playsound(list[0]+".wav")
    playsound("x10.wav")
    playsound(list[1]+".wav")

print("気圧(hPa): {}".format(w.barometric_pressure()))
pre = int()
if pre > 1015:
    playsound("prehigh.wav")
elif pre >= 1010 and pre <=1015:
    playsound("preaverage.wav")
elif pre <1010:
    playsound("prelow.wav")