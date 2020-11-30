from datetime import datetime
f = open("testing.txt", "a")
f.write(f"{datetime.now()} is the new time \n")

f.close()
