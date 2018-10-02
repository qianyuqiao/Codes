from datetime import datetime
import time
a = datetime.utcnow()
time.sleep(2)
b = datetime.utcnow()

print type(b - a)
