"""Recursive computation of the binomial theorem: (a+b)^n = Σ_{k=0}^{n} C(n,k) a^k b^{n-k}.

Principle — Pascal's identity (combinatorial argument):
    C(n, k) = C(n-1, k-1) + C(n-1, k)
Choose k out of n distinct objects; focus on the n-th object:
  take it → choose the remaining k-1 from n-1: C(n-1, k-1);
  skip it → choose all k from n-1: C(n-1, k).
The two cases are mutually exclusive and exhaustive — a natural recursion.
"""


class BinomialTheorem:
    """All parameters defined in __init__; computation done by inner helpers."""

    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n
        self._memo = {}  # memoization: cache computed C(n, k) to avoid redundant recursion

    # ---------- helper 1: recursive combination ----------
    def _comb(self, n, k):
        if k < 0 or k > n:      # invalid: choosing more than available
            return 0
        if k == 0 or k == n:    # base case: take all or none, exactly 1 way
            return 1
        key = (n, k)
        if key not in self._memo:  # recurse only if not computed before
            self._memo[key] = self._comb(n - 1, k - 1) + self._comb(n - 1, k)
        return self._memo[key]

    # ---------- helper 2: k-th term of the expansion ----------
    def _term(self, k):
        return self._comb(self.n, k) * (self.a ** k) * (self.b ** (self.n - k))

    # ---------- helper 3: recursive summation ----------
    def _sum_from(self, k):
        if k > self.n:          # base case: k past n, nothing left to sum
            return 0
        return self._term(k) + self._sum_from(k + 1)  # k-th term + the rest

    # ---------- public interface ----------
    def value(self):
        """Evaluate (a+b)^n via the binomial expansion."""
        return self._sum_from(0)

    def terms(self):
        """Return each term's value (for inspection/debugging)."""
        return [self._term(k) for k in range(self.n + 1)]

    def verify(self):
        """Cross-check against direct (a+b)**n; return (expanded, direct)."""
        return self.value(), (self.a + self.b) ** self.n
