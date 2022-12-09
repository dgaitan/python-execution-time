import datetime


class ExecutionTimer:

    def __init__(self):
        self.start_time = datetime.datetime.now()

    def completed(self) -> None:
        self.end_time = datetime.datetime.now()

    def humanize_delta(self, seconds: float) -> str:
        """
        Main Goal is to return the human friendly result
        of the estimated time of execution time of a python function.

        It should return something like:
        - 0.12 sec(s)
        - 12 sec(s)
        - 1 min(s) 23 sec(s)
        - 2 hour(s) 28 min(s)
        """
        if seconds == 0:
            return "0 seconds"
        
        result = []
        interval_settings = {
            "month": 2627424,
            "week": 604800,
            "day": 86400,
            "hour": 3600,
            "minute": 60,
            "second": 1
        }

        if seconds < 1:
            return "{} millisec(s)".format(int(seconds * 1000))

        for interval in interval_settings.keys():
            quotient, remainder = divmod(seconds, interval_settings[interval])
            
            if quotient == 0:
                continue
            
            seconds = remainder            
            result.append('{} {}(s)'.format(quotient, interval))

            if remainder == 0:
                break

        return " ".join(result)

    @property
    def execution_time(self) -> str:
        diff = self.end_time - self.start_time
        return self.humanize_delta(diff.total_seconds())