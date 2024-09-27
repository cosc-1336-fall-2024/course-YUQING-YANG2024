#clock program_epoch clock

def get_hour(epoch_seconds):
    result = epoch_seconds // 3600
    hours = result % 24 #get the remainder by dividing by 24
    return hours

def get_minutes(epoch_seconds):
    result = epoch_seconds // 60
    minutes = result % 60 #get the remainder by dividing by 60
    return minutes

def get_seconds(epoch_seconds):
    result = epoch_seconds % 3600
    seconds = result % 60 #get the actual seconds by dividing the remaining seconds
    return seconds
