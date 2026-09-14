from pathlib import Path
import json
import platform
import sympy as s

root = Path(__file__).resolve().parent
x = s.symbols('x', nonzero=True)
assert s.expand((1-x)*(1-1/x)) == 2-x-1/x
polar = s.Matrix([[0, 1], [1, 0]])
assert polar.eigenvals() == {-1: 1, 1: 1}
a = s.symbols('a', positive=True)
e = s.Matrix([s.Rational(3, 5), s.Rational(4, 5)])
projector = e*e.T
assert projector*projector == projector
A = s.diag(s.Rational(9, 4), s.Rational(11, 4))
B = A+a*projector
assert s.trace(B-A) == a
assert s.trace(-B+A) == -a
r = s.symbols('r')
for n in range(1, 33):
    polynomial = s.expand(1-(1-r)**n)
    assert polynomial.coeff(r, 0) == 0
    assert polynomial.coeff(r, 1) == n
result = {
    'python': platform.python_version(), 'sympy': s.__version__,
    'exact_checks': {'translated_autocorrelation_coefficients': [2, -1, -1],
                     'polar_form_eigenvalues': [-1, 1], 'rank_one_projection': True,
                     'rank_one_trace_difference': 'a', 'negative_linear_test_difference': '-a',
                     'Li_leading_coefficient_checks': 32},
    'scope': 'Finite algebra checks verify coefficients and signs. The source proofs establish smooth-test, modular, domain, trace-norm, and infinite-sum statements.'
}
(root / 'calculation-results.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
