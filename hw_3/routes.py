from typing import Callable, Dict
import handlers


app_routes: Dict[str, Callable] = {
    '': handlers.main,
    'repos': handlers.repos,
}
