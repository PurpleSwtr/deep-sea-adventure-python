def print_sea_map_info(sea_map: list[str]):

    overflow = 0
    padding = 1
    first = True
    print("""
                                |_
                          _____|~ |____
                         (  --         ~~~~--_,
                          ~~~~~~~~~~~~~~~~~~~'`
    """, end='')
    for tile in sea_map:

        to_print = f' [{tile}] '
        if first:
            print(f'{' '*26}{to_print}')
            first = False
            continue
        if overflow < 7: 
            print(to_print, end='')
            overflow += 1
        else:
            print()
            if padding % 2 == 0:
                print(f'{' '*30}{to_print}')
            else:
                print(to_print)
            overflow = 0
            padding += 1