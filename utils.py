Unsigned = (bool, bool, bool)
TwosComp = (bool, ) + Unsigned

def to_twos_comp(num: int) -> TwosComp:
    assert num in range(-(2 ** 3), (2 ** 3))
    if num < 0:
        return True, *_to_unsigned((2 ** 3) + num)
    else:
        return False, *_to_unsigned(num)

def _from_str(string: str) -> TwosComp:
    assert len(string) == len(TwosComp) and all(c in "01" for c in string)
    return tuple(c == "1" for c in string)

def to_str(num: TwosComp) -> str:
    return "".join("1" if bit else "0" for bit in num)

def value(num: TwosComp) -> int:
    if num[0]:
        return -(2 ** 3) + _from_unsigned(num[1:4])
    else:
        return _from_unsigned(num[1:4])

def _from_unsigned(num: Unsigned) -> int:
    return (int(num[0]) << 2) + (int(num[1]) << 1) + int(num[2])

def _to_unsigned(num: int) -> Unsigned:
    assert num in range(0, (2 ** 3))
    lsb = bool(num & 0b1)
    middle = bool(num >> 1 & 0b1)
    msb = bool(num >> 2 & 0b1)
    return msb, middle, lsb

# only used for debugging
def debug(func):
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__} with {args} and {kwargs}")
        rv = func(*args, **kwargs)
        print(f"{func.__name__} returned {rv}")
        return rv
    wrapper.__name__ = func.__name__
    return wrapper

# --- TESTING ---

def test():
    t = to_twos_comp
    s = _from_str
    assert t(-8) == s("1000")
    assert t(-7) == s("1001")
    assert t(-6) == s("1010")
    assert t(-5) == s("1011")
    assert t(-4) == s("1100")
    assert t(-3) == s("1101")
    assert t(-2) == s("1110")
    assert t(-1) == s("1111")
    assert t( 0) == s("0000")
    assert t( 1) == s("0001")
    assert t( 2) == s("0010")
    assert t( 3) == s("0011")
    assert t( 4) == s("0100")
    assert t( 5) == s("0101")
    assert t( 6) == s("0110")
    assert t( 7) == s("0111")

    for num in range(-8, 8):
        assert value(t(num)) == num

if __name__ == "__main__":
    test()
