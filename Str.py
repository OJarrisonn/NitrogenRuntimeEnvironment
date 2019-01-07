import Var
import Math


def write(msgs):
    size = msgs.__len__()
    for m in range(size):
        if '[' in msgs[m] and ']' in msgs[m]:
            vs = msgs[m].find('[')
            ve = msgs[m].find(']')
            vr = msgs[m][vs+1:ve]
            if vr in Var.VARS:
                r = Var.VARS.get(vr)
            elif '+' in vr:
                nums = vr.split('+')
                r = Math.plus(nums)
            elif '-' in vr:
                nums = vr.split('-')
                r = Math.subtract(nums)
            elif '*' in vr:
                nums = vr.split('*')
                r = Math.times(nums)
            elif '/' in vr:
                nums = vr.split('/')
                r = Math.dividedby(nums)
            msgs[m] = msgs[m].replace('[{}]'.format(vr), str(r))
        print(msgs[m], end='')
