def convert(seconds):
    seconds = seconds % (12 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds)
      
# Driver program
n = 54876
print(convert(n))
