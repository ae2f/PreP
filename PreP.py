from . import In
from . import Env
import collections.abc as types

def Include_Imp(ret : list[str], src: types.Iterable[str], currdir: str, include: types.Iterable[str] = []) -> tuple[str, list[str]]:
    for LINE in src:
        PATH, FLAG = In.Rd(LINE)
        if(PATH == ''):
            if(FLAG == In.RD_GOT_NOTHING[1]):
                ret.append(LINE if LINE.endswith('\n') else LINE)
            continue

        FND = In.Fnd(PATH, [currdir] if FLAG == Env.EXCLUDED else [currdir] + include)
        if(FND[1] == []): continue
        else: return FND

    return ("", []) 

def Include(src: types.Iterable[str], currdir: str, include: types.Iterable[str] = []) -> list[str]:
    ret = []

    got = Include_Imp(ret, src, currdir, include)
    while(got[1] != []):
        got = Include_Imp(ret, src, got[0], got[1])

    return ret