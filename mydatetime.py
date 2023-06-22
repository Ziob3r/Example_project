from datetime import datetime

class MyDateTime(datetime):
    def formatted(self):
        return self.strftime('%Y-%m-%d %H:%M:%S')
