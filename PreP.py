from . import In
from . import Env
import collections.abc as types

def Include(src: types.Iterable[str], currdir: str, include: types.Iterable[str] = []) -> str:
    ret = ''
    for LINE in src:
        PATH, FLAG = In.Rd(LINE)
        if(PATH == ''):
            if(FLAG == In.RD_GOT_NOTHING[1]):
                ret += LINE + '\n'
            continue

        FND_PATH, FND_SRC = In.Fnd(PATH, [currdir] if FLAG == Env.EXCLUDED else [currdir] + include)
        if(FND_SRC == []): continue
        ret += Include(FND_SRC, FND_PATH, include)

        pass

    return ret + '\n'