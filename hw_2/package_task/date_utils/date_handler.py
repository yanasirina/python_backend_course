import datetime
from typing import Optional


def rus_to_date(date_rus: str) -> Optional[datetime.date]:
    """
        метод преобразует строку (ДД.ММ.ГГГГ) в объект datetime.date
    """
    if date_rus:
        try:
            return datetime.datetime.strptime(date_rus, '%d.%m.%Y').date()
        except Exception:
            return None
    else:
        return None


def date_to_rus(date: datetime.date):
    """
        метод преобразует объект datetime.date в строку (ДД.ММ.ГГГГ)
    """
    if date:
        try:
            return date.strftime('%d.%m.%Y')
        except Exception:
            return date
    else:
        return ""


if __name__ == '__main__':
    """Проверим работу модуля"""
    assert rus_to_date('14.05.2008') == datetime.date(2008, 5, 14)
    assert date_to_rus(datetime.date(2008, 5, 14)) == '14.05.2008'
