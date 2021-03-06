# Log-Shot

A simplified log tool with some custom features that allows to manage loggers across multiple python files, with a root logger that is easy to enable or disable whenever it is necessary from any file.

### Installation
```
pip install logshot
```

### Usage Example
```
# -- Global logger config
title = "log-file"
logs_dir = 'logs'
if not os.path.exists(logs_dir):
    os.mkdir(logs_dir)
logging.config_log_capture(logs_dir, logfile_title=title)
logging.root_level = logging.DEBUG;
logging.start_log_capture()
# -- Logger
logger = logging.Logger(module_name=__name__)
logger.level = logging.DEBUG
...
logger.info("Opening example path...")
try:
    with open('C:\\Users\\example\\of\\logshot\\package', 'r') as file:
        ...
except Exception as err:
    logger.error(err); exit(1)
```

### File Output
```
2022-01-24 00:59:32.138305
[INFO] __main__: Opening example path...

2022-01-24 00:59:40.446509
[ERROR] __main__: [WinError 3] The system cannot find the path specified: 'C:\\Users\\example\\of\\logshot\\package'
```
