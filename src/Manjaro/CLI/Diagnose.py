from systemd import journal
from Manjaro.CLI import color

debug_info = journal.Reader()
debug_info.this_boot()
print(dir(journal))

def _msg(debug_info, level):
    color.action(f"Showing all {level} messages in your system")
    for err in debug_info:
        try:
            if level == "error":
                color.red(err["SYSLOG_IDENTIFIER"])
            elif level == "warning":
                color.yellow(err["SYSLOG_IDENTIFIER"])
            elif level == "info" or level == "debug":
                color.cyan(err["SYSLOG_IDENTIFIER"])
            
        except KeyError:
            pass
        color.white(err["MESSAGE"])

def debug():
    debug_info.log_level(journal.LOG_DEBUG)
    _msg(debug_info, "debug")

def warning():
    debug_info.log_level(journal.LOG_WARNING)
    _msg(debug_info, "warning")

def info():
    debug_info.log_level(journal.LOG_INFO)
    _msg(debug_info, "info")

def error():
    debug_info.log_level(journal.LOG_ERR)
    _msg(debug_info, "error")
    