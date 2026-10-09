from Binomial_Theorem import BinomialTheorem

def _expand_names(names, n):
    if len(names) == 1:
        return [(1, ((names[0], n),))]
    if len(names) == 2:
        coefs = BinomialTheorem(1, 1, n).terms()  # [C(n,0), ..., C(n,n)]
        return [(coefs[k], ((names[0], k), (names[1], n - k)))
                for k in range(n + 1)]
    a1, rest = names[0], names[1:]
    coefs = BinomialTheorem(1, 1, n).terms()
    out = []
    for k in range(n + 1):
        for c, factors in _expand_names(rest, n - k):
            out.append((coefs[k] * c, ((a1, k),) + factors))
    return out

def _format_term(coef, factors):
    mono = "".join(name if e == 1 else f"{name}^{e}"
                   for name, e in factors if e > 0)
    if not mono:
        return str(coef)
    return mono if coef == 1 else f"{coef}{mono}"

def multinomial_value(coeffs, n):
    if all(isinstance(c, str) for c in coeffs):
        terms = _expand_names(list(coeffs), n)
        return " + ".join(_format_term(c, f) for c, f in terms)
    if len(coeffs) == 0:
        return None
    if len(coeffs) == 1:
        return coeffs[0] ** n
    if len(coeffs) == 2:
        return BinomialTheorem(coeffs[0], coeffs[1], n).value()
    a1, rest = coeffs[0], coeffs[1:]
    binom_coefs = BinomialTheorem(1, 1, n).terms()
    return sum(binom_coefs[k] * (a1 ** k) * multinomial_value(rest, n - k)
               for k in range(n + 1))


def multinomial_coef(n, ks):
    ks = tuple(ks)
    if sum(ks) != n:
        return 0
    if len(ks) == 1:
        return 1
    if len(ks) == 2:
        return BinomialTheorem(1, 1, n).terms()[ks[0]]
    return (BinomialTheorem(1, 1, n).terms()[ks[0]]
            * multinomial_coef(n - ks[0], ks[1:]))

def term_count(n,r):
    return BinomialTheorem(1, 1, n + r - 1).terms()[r - 1]

if __name__ == "__main__":
    print("(1+2)^3       =", multinomial_value([1, 2], 3))
    print("(1+2+3+4)^2     =", multinomial_value([1, 2, 3, 4], 2))
    print("(0.2+0.3+0.5)^4 =", multinomial_value([0.2, 0.3, 0.5], 4))
    print()
    print("(a+b)^4   =", multinomial_value(["a", "b"], 4))
    print("(a+b+c)^2 =", multinomial_value(["a", "b", "c"], 2))

    
