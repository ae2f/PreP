import os
import Env
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
            case '<': POST = '>'; FLAG = Env.INCLUDED; pass
            case '"': POST = '"'; FLAG = Env.EXCLUDED; pass
            case _: return RD_INVALID
        
        if(not PATH_GET.endswith(POST)): return RD_INVALID
        RET_STR : str = PATH_GET[0:len(PATH_GET)]
        return (RET_STR, FLAG)
    
    else: return RD_GOT_NOTHING

def Fnd(fname: str, include: types.Iterable[str]) -> tuple[str, list[str]]:
    for PATH in include:
        if(not os.path.isfile(PATH + "/" + fname)):
            return ('', [])

        with open(PATH + '/' + fname, 'r') as F:
            return (PATH, F.readlines())
        
    return ('', [])
    