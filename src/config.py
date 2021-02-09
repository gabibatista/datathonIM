from dynaconf import LazySettings, Validator
from dynaconf import Dynaconf

settings = Dynaconf(
    settings_files=["settings.toml", ".secrets.toml"],
    environments=True,
    load_dotenv=True,
)

settings.validators.register(
    Validator(
        "LANG",
        "LANGUAGE",
        "LC_ALL",
        "LOGGER_LEVEL",
        "LOGGER_FILE",
        is_type_of=(str)
    ),
    Validator(
        "HEADLESS",
        is_type_of=(bool)
    ),
    Validator(
        "WAIT_TIME",
        is_type_of=(int)
    )
)

# in case of error, interrupt the application
settings.validators.validate()
HEADLESS = settings.get('HEADLESS', True)
PATH_BROWSER = '/usr/bin/firefox'
LANG = settings.get('LANG', 'pt_BR.UTF-8')
LANGUAGE = settings.get('LANGUAGE', 'pt_BR.UTF-8')
LC_ALL = settings.get('LC_ALL', 'pt_BR.UTF-8')
WAIT_TIME = settings.get('WAIT_TIME', 30)
