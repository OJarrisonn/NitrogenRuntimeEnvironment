import Var


def plus(nums):
    presult = 0
    size = nums.__len__()
    for vp in range(size):
        if nums[vp].isnumeric():
            nums[vp] = float(nums[vp])
        elif nums[vp] in Var.VARS:
            nums[vp] = Var.VARS.get(nums[vp])
        presult += nums[vp]
    return presult


def subtract(nums):
    sresult = 0
    size = nums.__len__()
    for vs in range(size):
        if nums[vs].isnumeric():
            nums[vs] = float(nums[vs])
        elif nums[vs] in Var.VARS:
            nums[vs] = Var.VARS.get(nums[vs])
        if vs == 0:
            sresult = nums[vs]
        else:
            sresult -= nums[vs]
    return sresult


def times(nums):
    tresult = 0
    size = nums.__len__()
    for vt in range(size):
        if nums[vt].isnumeric():
            nums[vt] = float(nums[vt])
        elif nums[vt] in Var.VARS:
            nums[vt] = Var.VARS.get(nums[vt])
        if vt == 0:
            tresult = nums[vt]
        else:
            tresult *= nums[vt]
    return tresult


def dividedby(nums):
    dresult = 0
    size = nums.__len__()
    for vd in range(size):
        if nums[vd].isnumeric():
            nums[vd] = float(nums[vd])
        elif nums[vd] in Var.VARS:
            nums[vd] = Var.VARS.get(nums[vd])
        if vd == 0:
            dresult = nums[vd]
        else:
            dresult *= nums[vd]
    return dresult