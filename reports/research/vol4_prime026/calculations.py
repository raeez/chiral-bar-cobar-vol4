from pathlib import Path
from math import comb, lcm
import json
import platform
import mpmath as mp

report = Path(__file__).resolve().parent
finite = []
for n in range(1, 513):
    central = comb(2*n, n)
    common = lcm(*range(1, 2*n+1))
    assert common % central == 0
    assert central * (2*n+1) >= 4**n
    finite.append(n)

mp.mp.dps = 70
# Differentiate the theta integral at zero. No zeta derivative enters this integral.
theta_integrand = lambda x: mp.fsum(mp.exp(-mp.pi*n*n*x) for n in range(1, 9)) * (1+mp.sqrt(x))/x
theta_B = -mp.quad(theta_integrand, [1, 2, 5, 10, 25, 55])
formula_B = -1-mp.euler/2+mp.log(4*mp.pi)/2
assert abs(theta_B-formula_B) < mp.mpf('1e-65')
# The half-line Fourier transform has these separately determined signs.
epsilon = mp.mpf('0.02')
u = mp.mpf('1.25')
laplace_density = 1/(epsilon+1j*u)
assert abs(mp.re(laplace_density)-epsilon/(epsilon**2+u**2)) < mp.mpf('1e-65')
assert abs(mp.im(laplace_density)+u/(epsilon**2+u**2)) < mp.mpf('1e-65')
result = {
    'python': platform.python_version(), 'mpmath': mp.__version__,
    'exact_finite_checks': {'central_binomial_divides_lcm': len(finite), 'central_binomial_mean_bound': len(finite)},
    'numerical_diagnostics': {'decimal_precision': mp.mp.dps, 'theta_B': str(theta_B),
                             'formula_B': str(formula_B), 'absolute_difference': str(abs(theta_B-formula_B)),
                             'half_line_boundary_signs': True, 'quadrature_error_certified': False},
    'scope': 'Integer checks verify only n=1,...,512. Numerical quadrature checks signs and constants, not a general theorem. The review supplies the general proofs.'
}
(report / 'calculation-results.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
