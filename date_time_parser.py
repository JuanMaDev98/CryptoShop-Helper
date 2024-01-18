def date_time_decode(time):
    time = str(time)
    return f"{time[:4]}-{time[4:6]}-{time[6:]}"


def date_time_encode(time):
    time = time.replace("-", "")
    return int(time)