import logging
import logging.config
from os import makedirs
from os.path import join

def configurar_logging(level="INFO"):
    log_dir="app/logs"
    makedirs(log_dir,exist_ok=True) 
    
    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,  
        'formatters': {
            'default': {
                'format': '[%(asctime)s] [%(levelname)s]: %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S' #formato do horario
            },
        },
        'handlers': { #configura o logger pro console
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'default', # a formatacao
                'level': level,
                'stream': 'ext://sys.stdout', #configura pra sair no console
            },
            'file': {
                'class': 'logging.FileHandler', 
                'formatter': 'default', # a formatacao
                'level': level,
                'filename': join(log_dir, 'app.log'), #configura pra criar um arquivo de log
                'encoding': 'utf-8',
                'mode': 'a',  # append no arquivo
            },
        },
        'root': {
            'level': level,
            'handlers': ['console', 'file'], #define quais handlers usar
        },
        'loggers': {
        'werkzeug': {
            'level': 'WARNING',  # ou 'ERROR', ou 'CRITICAL', ou 'NOTSET'
            'handlers': [],      # vazio para não herdar seus próprios handlers
            'propagate': False
        },
        'flask': {
            'level': 'WARNING',
            'handlers': [],
            'propagate': False
        }}
    }
    logging.config.dictConfig(logging_config)