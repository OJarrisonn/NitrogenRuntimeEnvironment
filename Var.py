import Math
VARS = {'TRUE': True, 'FALSE': False}


def var(args):
    name = args[0]
    value = args[1]
    if '\n' in value:
        value = value.replace('\n', '')
    if '+' in value:
        nums = value.split('+')
        value = Math.plus(nums)
    elif '-' in value:
        nums = value.split('-')
        value = Math.subtract(nums)
    elif '*' in value:
        nums = value.split('*')
        value = Math.times(nums)
    elif '/' in value:
        nums = value.split('/')
        value = Math.dividedby(nums)
    elif value in VARS:
        value = VARS.get(value)
    elif value.isnumeric():
        value = float(value)
    VARS[name] = value
