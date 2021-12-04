Napisać program, który zapyta użytkownika o imię i datę urodzenia, a następnie wypisze na ekran te dane oraz informacje
czy osoba jest pełnoletnia, a jeśli nie jest, informację za ile lat, miesięcy i dni będzie. Dzisiejszą datę w formacie '
YYYY-MM-DD' można pobrać z komputera za pomocą modułu „datetime”

```
from datetime import datetime
dzisiaj=datetime.date(datetime.now()).isoformat())
```