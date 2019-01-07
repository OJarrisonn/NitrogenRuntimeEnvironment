def args(arg, notarg, split):
    args = arg.replace(notarg, '')
    tokens = args.split(split)
    return tokens
