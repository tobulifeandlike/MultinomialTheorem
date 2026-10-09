"""Test cases for the recursive binomial / multinomial theorem programs. Run: python3 test_theorems.py"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from Binomial_Theorem import BinomialTheorem
from Multinomial_Theorem import multinomial_value, multinomial_coef, term_count

passed, failed = 0, 0


def check(name, got, expected, tol=1e-9):
    global passed, failed
    ok = abs(got - expected) <= tol if isinstance(expected, float) else got == expected
    print(("PASS " if ok else "FAIL ") + f"{name}: got {got}, expected {expected}")
    if ok:
        passed += 1
    else:
        failed += 1


print("== binomial ==")
bt = BinomialTheorem(2, 3, 4)
check("(2+3)^4 value", bt.value(), 625)
check("(2+3)^4 terms", bt.terms(), [81, 216, 216, 96, 16])
check("n=0 -> 1", BinomialTheorem(5, 7, 0).value(), 1)
check("prob normalization (0.3+0.7)^10", BinomialTheorem(0.3, 0.7, 10).value(), 1.0)

print("== multinomial ==")
check("(1+2+3)^3", multinomial_value([1, 2, 3], 3), 216)
check("term count C(5,2)=10", term_count(3, 3), 10)
check("(1+2+3+4)^2", multinomial_value([1, 2, 3, 4], 2), 100)
check("prob normalization (0.2+0.3+0.5)^4", multinomial_value([0.2, 0.3, 0.5], 4), 1.0)
check("r=2 falls back to binomial", multinomial_value([2, 3], 4), bt.value())
check("single coeff 5^3", multinomial_value([5], 3), 125)
check("n=0 -> 1", multinomial_value([1, 2, 3], 0), 1)
check("coef of a^1b^1c^1 in (a+b+c)^3", multinomial_coef(3, (1, 1, 1)), 6)
check("coef of a^2b^1c^1 in (a+b+c)^4", multinomial_coef(4, (2, 1, 1)), 12)
check("coef of a^3 in (a+b+c)^3", multinomial_coef(3, (3, 0, 0)), 1)

print("== symbolic ==")
check('symbolic (a+b)^3',
      multinomial_value(["a", "b"], 3), "b^3 + 3ab^2 + 3a^2b + a^3")
check('symbolic (a+b+c)^2',
      multinomial_value(["a", "b", "c"], 2), "c^2 + 2bc + b^2 + 2ac + 2ab + a^2")
check('symbolic n=0 -> "1"', multinomial_value(["a", "b"], 0), "1")

print(f"\n{passed} passed, {failed} failed")
sys.exit(1 if failed else 0)
