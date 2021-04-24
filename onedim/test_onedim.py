from onedim import OneDim
import numpy as np

def initialise():
    od = OneDim()
    return od

def testInitial(gen):
    first_row = np.zeros(gen.map.shape[1])
    first_row[len(first_row) // 2] = 1
    print(first_row)
    print(gen.map[-1])
    assert np.allclose(first_row, gen.map[-1])

def test_gen(gen, other_gen):
    assert np.allclose(gen, np.array(other_gen).reshape(100, 100))


if __name__ == '__main__':
    od = initialise()
    testInitial(od)
    print(od)
    rule = 30
    ruleset = [int(b) for b in format(rule, 'b').zfill(8)]
    od.next_gen(ruleset)
    print(od.get_map()[-2])
    print(od.get_map()[-1])