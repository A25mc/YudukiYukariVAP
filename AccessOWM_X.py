from playsound import playsound
from pyowm.owm import OWM
from pyowm.utils import formatting
from pyowm.utils.config import get_default_config


config_dict = get_default_config()
config_dict["language"] = "ja"

owm = OWM("990918c7f5f421581fd53d52c0274294",config_dict)
mgr = owm.weather_manager()

observation = mgr.weather_at_place("123-0841,JP")

w = observation.weather


playsound("Goodmorning.wav")


print("天気コード: {}".format(w.weather_code))
playsound(w.weather.code+".wav")


playsound("tamprature.wav")


print("気温(℃): {}".format(round(w.temperature("celsius"))))
temp = w.temperature("celsius")['temp']

#   10以下、もしくは10で割り切れる場合は直接読み上げ
if int(temp) <= 10 or int(temp) / 10 >= 1:
    playsound(temp + ".wav")

#   11~19の場合は10の位1の位をそれぞれリストに入れて、10発音+1の位発音
elif int(temp) > 10 and int(temp) < 20:
    list=list(temp)
    playsound("10.wav")
    playsound(list[1] + ".wav")

#   20以上の場合は10の位1の位をそれぞれリストに入れて、直接読み上げ+1の位発音
elif int(temp) >= 20:
    list=list(temp)
    playsound(list[0] + "0.wav")
    playsound(list[1] + ".wav")


playsound("pressure.wav")


print("気圧(hPa): {}".format(w.barometric_pressure()))
pre = int(w.barometric_pressure())
if pre > 1015:
    playsound("pre_high.wav")

elif pre >= 1010 and pre <=1015:
    playsound("pre_average.wav")

elif pre <1010:
    playsound("pre_low.wav")