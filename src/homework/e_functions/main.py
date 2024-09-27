#clock program_epoch clock

import value_return

def main():
    
    hour = value_return.get_hour(13800)
    minutes = value_return.get_minutes(3800)
    seconds = value_return.get_seconds(3800)
    
    hour_epoch = value_return.get_hour(1727404787)
    minutes_epoch = value_return.get_minutes(1727404787)
    seconds_epoch = value_return.get_seconds(1727404787)

    print("the time is: ", '%02d'%hour, ":", '%02d'%minutes, ":", '%02d'%seconds)

    print("the epoch time is: ", '%02d'%hour_epoch, ":", '%02d'%minutes_epoch, ":", '%02d'%seconds_epoch)

main()