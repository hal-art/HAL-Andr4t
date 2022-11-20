class Utils:
    def int_try_parse(value: str) -> tuple(bool, int):
        try:
            int_value = int(str)
            return (True, int_value)
        except:
            return (False, -1)