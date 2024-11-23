from pathlib import Path
from . import Env
import collections.abc as types

RD_INVALID: tuple[str, bool] = ('', Env.EXCLUDED)
RD_GOT_NOTHING: tuple[str, bool] = ('', Env.INCLUDED)

PF_T = tuple[str, bool]

def Rd(l: str) -> PF_T:
    if l.startswith('#include'):
        TAR: str = l.replace(' ', '')
        PATH_GET: str = TAR[len('#include')::].replace(' ', '')
        FLAG: bool
        RET_STR: str

        match PATH_GET[0]:
            case '<': 
                FLAG = Env.INCLUDED
                RET_STR = PATH_GET.split('<')[1].split('>')[0]
            case '"': 
                FLAG = Env.EXCLUDED
                RET_STR = PATH_GET.split('"')[1]
            case _: 
                return RD_INVALID

        return (RET_STR, FLAG)
    else: 
        return RD_GOT_NOTHING

def Fnd(fname: str, include: types.Iterable[str]) -> tuple[str, list[str]]:
    for PATH in include:
        path_obj = Path(PATH) / fname
        if not path_obj.is_file():
            continue
        with path_obj.open('r') as F:
            return (path_obj.parent.as_posix(), F.readlines())

    return ('', [])
