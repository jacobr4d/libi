#!/usr/bin/env python3

import sys
import os


rootp = os.path.dirname(__file__)
tmpp = os.path.join(rootp, 'temp')
textp = os.path.join(tmpp, 'text')
audp = os.path.join(tmpp, 'aud')

for p in [tmpp, textp, audp]:
    os.system('mktemp -d -q ' + p)
    os.system('rm ' + p + '/*')

bi, cb, cc, cout = 0, None, None, None

for l in sys.stdin:

    l = l.strip()
    if l == '.':
        continue
    rh, rs, rc = l.rfind('--'), l.rfind(' '), l.rfind(':')
    t, b, c, v = l[:rh - 1], l[rh + 3:rs], l[rs + 1:rc], l[rc+1:]

    if b != cb:
        bi += 1
        cb = b

    if c != cc:
        cout = os.path.join(textp, 'enasb.b' + f'{bi:03}' + '.c' + c.zfill(3))
        with open(cout, 'a') as f:
            f.write(b + ', chapter: ' + c + '\n')
        cc = c

    with open(cout, 'a') as f:
        f.write(t)
        f.write(' ')
