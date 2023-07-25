def log(level, msg, status, ex=None):
    print({"level": str(level), "msg": str(msg.encode("utf-8")), "status": str(status), "exception": str(ex)})