from utils import TwosComp

def four_bit_adder(*inputs) -> (*TwosComp, bool):
    assert len(inputs) == 9
    x = inputs[0:4]
    y = inputs[4:8]
    carry_in = inputs[8]

    carry = carry_in
    out = tuple()
    for bit in range(4):
        out_bit, carry = one_bit_adder(x[3 - bit], y[3 - bit], carry)
        out = (out_bit, *out)

    return *out, carry

def one_bit_adder(left, right, carry_in) -> (bool, bool):
    out = left ^ right ^ carry_in
    carry = (left & right) | (left & carry_in) | (right & carry_in)

    return out, carry

# --- TESTING ---
def test():
    o = one_bit_adder
    a = four_bit_adder
    from utils import to_twos_comp as t, _from_str as s

    assert o(False, False, False) == (False, False)
    assert o(False, False, True) == (True, False)
    assert o(False, True, False) == (True, False)
    assert o(False, True, True) == (False, True)
    assert o(True, False, False) == (True, False)
    assert o(True, False, True) == (False, True)
    assert o(True, True, False) == (False, True)
    assert o(True, True, True) == (True, True)

    assert a(*t(2), *t(-4), False) == (*t(-2), False)
    assert a(*t(2), *t(-1), False) == (*t(1), True)
    assert a(*t(0), *t(0), True) == (*t(1), False)
    assert a(*t(3), *t(3), True) == (*t(7), False)
    assert a(*t(2), *t(-2), True) == (*t(1), True)

if __name__ == "__main__":
    test()
