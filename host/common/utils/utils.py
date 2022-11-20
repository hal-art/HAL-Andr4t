class Utils:
    """
    Utilsクラス
    
    細かい共通処理などはここに記載する。
    
    """
    def int_try_parse(value: str) -> tuple(bool, int):
        """
        str -> intへの変換処理

        Args:
            value (str): 変換したい文字列

        Returns:
            bool: 変換できるかどうか
            int: 変換後の値
        """
        try:
            int_value = int(str)
            return (True, int_value)
        except:
            return (False, -1)