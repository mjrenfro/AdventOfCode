#every hash must be checked in order such that
#a larger indexed key with a smaller quint match
#doesn't eclipse a smaller indexed key with a larger
#quint match.

import hashlib
import re

salt='ngcjuoqr'

def repeat_hash(seed):

    for _ in range(2017):
        seed=hashlib.md5(seed.encode('utf-8')).hexdigest()
    return seed

def solver():
    queue=[repeat_hash(salt+str(x)) for x in range(1001)]
    idx, n =0,0
    while queue:
        h=queue.pop(0)
        r=re.findall(r"(.)\1\1",h)
        if r:
            if [s for s in queue if r[0]*5 in s]:
                n+=1
                if n==64:
                    return idx
        idx+=1
        queue.append(repeat_hash(salt+str(idx+len(queue))))

print (solver())
