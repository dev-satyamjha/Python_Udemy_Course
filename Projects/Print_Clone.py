from typing import Any
def print_func(
    *values: Any,
    sep: str | None =  '',
    end: str | None = '\n',
    caps: bool = False,
    count: bool = False,
    include_types: bool = False) -> None:

        new_vals: list[Any] = []
        for value in values:
            if isinstance(value, str) and caps:
                new_vals.append(value.upper())
            else:
                new_vals.append(value)

        values_with_types: list[Any] = []
        if include_types:
            for value in values:
                values_with_types.append((value, type(value)))
            print(*values_with_types, sep=sep, end=end)
        else:
            print(new_vals, sep=sep, end=end)

        if count:
            print(f"\nTotal entries: {len(values)}", end=end)

print_func('satyam', 'allu arjun', caps= True, sep = ',')
print_func('satyam', 'allu arjun', 12, include_types=True, caps= True, sep = ',')

print_func('[System, Hang, Roman]','satyam', 'allu arjun', False, (2,4,6,8,10), 12, include_types=True, caps= True, sep = ',', end='!')
print_func('[System, Hang, Roman]','satyam', 'allu arjun', False, (2,4,6,8,10), 12, count=True, caps= True, sep = ',', end='.')
