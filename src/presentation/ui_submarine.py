from utils.color_print import cprint

def print_submarine_info(oxygen: int) -> None:

    max_oxygen = 25

    if oxygen < 0:
        oxygen = 0
    if oxygen > max_oxygen:
        oxygen = max_oxygen
    index = max_oxygen - oxygen
    offset = 1

    for i in range(index):
        num = max_oxygen - i
        if num >= 10:
            offset += 5
        else:
            offset += 4

    symbols_len = 119

    cprint('\n' + '='*symbols_len, fg='green',)

    cprint(' ' * offset + '↓', fg='yellow', style='bright')

    [cprint(f'|{max_oxygen-num}| ', end='', fg='green', style='dim') for num in range(max_oxygen-oxygen)]
    [cprint(f'|{oxygen-num}| ', end='', fg='green', style='bright') for num in range(max_oxygen+oxygen) if oxygen-num >= 0]
    print()
    cprint(' ' * offset + '^', fg='yellow', style='bright')

    
    cprint('='*symbols_len, fg='green',)