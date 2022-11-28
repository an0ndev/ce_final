from utils import TwosComp
from adder import four_bit_adder

def four_bit_or(*bits):
    assert len(bits) == 4
    return tuple(not bit for bit in bits)

def four_bit_subtractor(*inputs) -> (*TwosComp, bool):
    assert len(inputs) == 8
    left = inputs[0:4]
    right_inv = four_bit_or(*inputs[4:8])
    out = four_bit_adder(*left, *right_inv, True)[0:4]
    left_sign, right_sign, out_sign = left[0], right_inv[0], out[0]
    overflow = (not (left_sign ^ right_sign)) and (left_sign ^ out_sign)
    return *out, overflow

# --- TESTING ---
def test():
    from utils import _from_str as s, to_twos_comp as t

    assert four_bit_or(*s("0000")) == s("1111")
    assert four_bit_or(*s("1010")) == s("0101")

    assert four_bit_subtractor(*t(2), *t(1)) == (*t(1), False)
    assert four_bit_subtractor(*t(2), *t(-1)) == (*t(3), False)
    assert four_bit_subtractor(*t(-8), *t(7))[4]
    assert not four_bit_subtractor(*t(-8), *t(-8))[4]
