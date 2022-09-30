from pyowm.owm import OWM
from pyowm.utils import formatting
from pyowm.utils.config import get_default_config

#Pyowmのコンフィグ設定

config_dict = get_default_config()
config_dict["language"] = "ja"

#Pyowmライブラリの初期化

owm = OWM('990918c7f5f421581fd53d52c0274294',config_dict)
mgr = owm.weather_manager()

#現在の気象データ取得

observation = mgr.weather_at_place("123-0841,JP")

w = observation.wweather
print("気象データの計測日次時間(unixTime): {}".format(w.ref_time))
print("気象データの計測日次時間(date): {}".format(formatting.to_date(w.ref_time)))
print("天気コード: {}".format(w.weather_code))
print("天気: {}".format(w.status))
print("天気詳細: {}".format(w.detailed_status))
print("気温(K): {}".format(w.temperature()))
print("気温(℃): {}".format(w.temperature("celsius")))
print("湿度(%): {}".format(w.humidity))
print("気圧(hPa): {}".format(w.barometric_pressure()))
print("風: {}".format(w.wind()))

print("雲量: {}".format(w.clouds))
print("雨量: {}".format(w.rain))
print("積雪量: {}".format(w.snow))
