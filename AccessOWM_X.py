import imp
from pyowm.owm import OWM
from pyowm.utils import formatting
from pyowm.utills.config import get_edfaullt_config

config_dict = get_edfaullt_config()
config_dict["language"] = "ja"

