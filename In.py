import os
from . import Env
import collections.abc as types

RD_INVALID: tuple[str, bool] = ('', Env.EXCLUDED)
RD_GOT_NOTHING : tuple[str, bool] = ('', Env.INCLUDED)

PF_T = tuple[str, bool]

def Rd(l: str) -> PF_T:
    if(l.startswith('#include')):
        TAR: str = l.replace(' ', '')
        PATH_GET: str = TAR[len('#include')::]
        FLAG : bool
        POST : str
        match(PATH_GET[0]):
            case '<': POST = '>\n'; FLAG = Env.INCLUDED; pass
            case '"': POST = '"\n'; FLAG = Env.EXCLUDED; pass
            case _: return RD_INVALID
        RET_STR : str = PATH_GET[1:len(PATH_GET) - 2]
        return (RET_STR, FLAG)
    
    else: return RD_GOT_NOTHING

def Fnd(fname: str, include: types.Iterable[str]) -> tuple[str, list[str]]:
    for PATH in include:
        if(not os.path.isfile(PATH + "/" + fname)):
            continue
        with open(PATH + '/' + fname, 'r') as F:
            return (PATH, F.readlines())
        
    return ('', [])
    