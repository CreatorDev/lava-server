SCHEDULER_DAEMON_OPTIONS = {
    'LOG_FILE_PATH': None,
    'LOG_LEVEL': "WARNING",
    # 500 megs should be enough for anyone
    'LOG_FILE_SIZE_LIMIT': 500 * 1024 * 1024,
    # Jobs always specify a timeout, but I suspect its often too low.
    # So we don't let it go below this value, which defaults to a day.
    'MIN_JOB_TIMEOUT': 24 * 60 * 60,
}

# ZMQ events
EVENT_NOTIFICATION = False
INTERNAL_EVENT_SOCKET = "ipc:///tmp/lava.events"
EVENT_SOCKET = "tcp://*:5500"
EVENT_ADDITIONAL_SOCKETS = []
EVENT_TOPIC = "org.linaro.validation"
