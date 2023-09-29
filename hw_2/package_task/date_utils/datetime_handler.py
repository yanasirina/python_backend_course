import datetime
from typing import Optional


def rus_to_datetime(datetime_rus: str) -> Optional[datetime.datetime]:
    """
        метод преобразует строку (ДД.ММ.ГГГГ ЧЧ:ММ:СС) в объект datetime.datetime
    """
    if datetime_rus:
        try:
            return datetime.datetime.strptime(datetime_rus, '%d.%m.%Y %H:%M:%S')
        except Exception:
            return None
    else:
        return None


def datetime_to_rus(dt: datetime.datetime):
    """
        метод преобразует объект datetime.datetime python в строку (ДД.ММ.ГГГГ ЧЧ:ММ)
    """
    if dt:
        try:
            return dt.strftime('%d.%m.%Y %H:%M')
        except Exception:
            return dt
    else:
        return ""


if __name__ == '__main__':
    """Проверим работу модуля"""
    assert rus_to_datetime('14.05.2008 21:15:04') == datetime.datetime(2008, 5, 14, 21, 15, 4)
    assert datetime_to_rus(datetime.datetime(2008, 5, 14, 21, 15, 4)) == '14.05.2008 21:15'
