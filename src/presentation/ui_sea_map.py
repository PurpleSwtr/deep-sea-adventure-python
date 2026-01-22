def transform_list(lst: list) -> list:
    result = []
    reverse_next = True
    i = 0
    while i < len(lst):
        if reverse_next:
            result.append(lst[i])
            block = lst[i+1:i+8]
            result.extend(reversed(block))
            i += 8
        else:
            block = lst[i:i+8]
            result.extend(block)
            i += 8
        reverse_next = not reverse_next
    return result

def print_sea_map_info(sea_map: list[str]):

    copy_sea_map = sea_map
    copy_sea_map = transform_list(copy_sea_map)
    overflow = 0
    padding = 1
    first = True
    print("""
                                |_
                          _____|~ |____
                         (  --         ~~~~--_,
                          ~~~~~~~~~~~~~~~~~~~'`
    """, end='')
    for tile in copy_sea_map:

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