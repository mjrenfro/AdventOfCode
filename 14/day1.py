#every hash must be checked in order such that
#a larger indexed key with a smaller quint match
#doesn't eclipse a smaller indexed key with a larger
#quint match.

import hashlib
import re

salt='ngcjuoqr'

def solver():
    queue=[hashlib.md5((salt+str(x)).encode('utf-8')).hexdigest() for x in range(1001)]
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
        queue.append(hashlib.md5((salt+str(idx+len(queue))).encode('utf-8')).hexdigest())

print (solver())
