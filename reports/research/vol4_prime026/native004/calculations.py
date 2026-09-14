from fractions import Fraction as F
from pathlib import Path
import json,platform
import mpmath as m
m.mp.dps=50
report=Path(__file__).resolve().parent
# Exact two-dimensional arithmetic, with its positive scale suppressed.
B=((F(0),F(1)),(F(1),F(0)))
q=lambda v:sum(v[i]*B[i][j]*v[j] for i in range(2) for j in range(2))
assert q((F(1),F(1)))==2 and q((F(1),F(-1)))==-2
# A nonreal conjugate pair gives a signed self-adjoint operator.
z=(complex(2,.25),complex(2,-.25));J=((0,1),(1,0))
assert z[0]==z[1].conjugate()
# Diagnostic quadrature verifies the independently derived analytic series.
k0=m.log(m.pi)+m.euler+m.pi/2+3*m.log(2)
k=lambda u:m.log(m.pi)-m.re(m.digamma(m.mpf(1)/4+1j*u/2))
rows=[]
N=128
for lam in (m.mpf(1),m.mpf(16),m.mpf(128),m.mpf(1024)):
 H=m.quad(lambda v:m.exp(-v*v)*k(m.sqrt(lam)*v),[-m.inf,0,m.inf])/m.sqrt(m.pi)
 brackets=[]
 for n in range(N):
  c=m.mpf(n)+m.mpf(1)/4;x=2*c/m.sqrt(lam)
  brackets.append(1/c-2*m.sqrt(m.pi/lam)*m.exp(x*x)*m.erfc(x))
 partial=k0-sum(brackets)
 # From the proved bracket bound and the decreasing inverse-cube tail.
 bound=lam/8*(1/(m.mpf(N)+m.mpf(1)/4)**3+1/(2*(m.mpf(N)+m.mpf(1)/4)**2))
 assert all(x>=0 for x in brackets)
 assert 0<=partial-H<=bound
 rows.append(dict(lam=str(lam),H=str(H),partial=str(partial),proved_tail_bound=str(bound),observed_gap=str(partial-H)))
# Canonical determinant vs one-dimensional spectral zeta determinant.
rho=m.mpc(1,2);s=m.mpc('.2','.1')
d2=(1-s/rho)*m.exp(s/rho);ratio=(s-rho)/d2
assert abs(ratio-(-rho*m.exp(-s/rho)))<m.mpf('1e-45')
result=dict(python=platform.python_version(),mpmath=m.__version__,exact_matrix={'positive':str(q((F(1),F(1)))),'negative':str(q((F(1),F(-1))))},gamma_thresholds={'auxiliary_g':str(m.findroot(lambda x:2*m.log(m.pi)-k(x),(.8,.9))),'arithmetic_k':str(m.findroot(k,(6,7)))},gaussian_rows=rows,determinant_ratio_residual=str(abs(ratio-(-rho*m.exp(-s/rho)))),scope='Exact matrix identities establish only their finite models. Decimal quadrature and root estimates are diagnostic; the TeX supplies convergence, tail bounds, signs, and all general comparison proofs.')
(report/'calculation-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
