# Independent first-stage derivation

The target is the signed Fourier/digamma pairing, its Gaussian restriction,
the de Branges carrier comparison, and the two constants in a genus-one
determinant. This record precedes receipt of the native writer's proposal.
The source carrier is the frozen construction with aggregate
`be64a27b9fb1d475d6315bcc73958e8df6e59e69162f6c5f42d32ab84d44be10`.
The two directly checked files have SHA-256
`959caa71b54ef6d6041f98caeb8ff6193f46d4646afcc07fb293244db36a2422`
(weil-pairing.tex) and
`a223804ab1fc543234f72a7c0eee4e35a1b51f22c72fd3d061e38238f205c058`
(occupation-scattering.tex).

## Signed pairing derived from the digamma integral

Use F+f(u)=integral f(x) exp(iux) dx, and inverse measure du/(2*pi).
Let w(u)=log(pi)-Re psi(1/4+iu/2), C0=w(0), and
k(t)=exp(-t/2)/(1-exp(-2t)) for t>0.
The digamma difference identity gives

    w(u)=C0-2*integral_0^infty k(t)*(1-cos(ut)) dt.

For f,g in Schwartz space, with first variable linear,

    B_infty(f,g) = (1/(2*pi))*integral F+f(u)*conj(F+g(u))*w(u) du
      = C0*<f,g> - integral_0^infty k(t)*<tau_t f-f,tau_t g-g> dt.

Here tau_t f(x)=f(x-t). Near zero the translation product is O(t^2),
while k(t)=O(1/t). At infinity k decreases exponentially.
C0=log(pi)+EulerGamma+pi/2+3*log(2)>0.
For phi=f*g*, the equivalent distribution is

    W_infty(phi)=(log(pi)+EulerGamma)*phi(0)
      + integral_0^infty [exp(-t/2)*(phi(t)+phi(-t))
                         -2*exp(-2t)*phi(0)]/(1-exp(-2t)) dt.

These formulas retain the subtraction at zero. They exclude replacement
by an ordinary multiplicative logarithmic kernel without its distributional term.

## Gaussian calculation

For f_lambda(x)=exp(-pi*lambda*x^2), lambda>0,

    F+f_lambda(u)=lambda^(-1/2)*exp(-u^2/(4*pi*lambda)),
    ||f_lambda||_2^2=(2*lambda)^(-1/2),
    B_infty(f_lambda,f_lambda)/||f_lambda||_2^2
      = R(lambda)=C0-2*integral_0^infty k(t)*(1-exp(-pi*lambda*t^2/2)) dt.

R'(lambda)=-pi*integral_0^infty t^2*k(t)*exp(-pi*lambda*t^2/2) dt<0.
R tends to C0 as lambda decreases to zero, and to minus infinity as
lambda increases to infinity. Thus there is exactly one Gaussian sign
threshold, with positive pairing below it and negative pairing above it.
This is the sign of the archimedean summand alone. It does not imply any
zero-placement claim or positivity of the full Weil form.
Gaussians belong to Schwartz space, not C_c^infinity. Their Fourier
transforms have unbounded H^2 upper-half-plane norms, so direct multiplication
by a Hermite--Biehler E does not put them in H(E).

## de Branges finite model and constructive comparison

Put A(z)=z^m, E=A+iA'=z^(m-1)*(z+im), m>=1.
Then Theta=Esharp/E=(z-im)/(z+im) after cancellation, and
Theta'(0)=-2i/m. The model space has the normalized basis

    e_0(z)=i*sqrt(m/pi)/(z+im), e_0(0)=1/sqrt(pi*m).

For the xi choice A(z)=xi(1/2+iz), the same local calculation gives
Theta'(gamma)=-2i/m_gamma at a real zero of multiplicity m_gamma.
Under the real-zero hypothesis, the paired product for A gives
A'/A=sum_gamma m_gamma/(z-gamma), with symmetric grouping. Its imaginary
part is negative on the upper half-plane, so E=A+iA' is Hermite--Biehler.
The model kernel decomposes into the orthonormal basis

    e_gamma(z)=i*sqrt(m_gamma/pi)*A(z)/((z-gamma)*E(z)).

An explicit map on compact tests is

    Jf=sum_gamma sqrt(pi*m_gamma)*F+f(gamma)*e_gamma.

It satisfies <Jf,Jg>_L2=pi*sum_gamma m_gamma*F+f(gamma)*conj(F+g(gamma)).
Thus (E/sqrt(pi))*J is a de Branges realization of the zero form under
the real-zero hypothesis. This map is generally not f -> E*F+f.
The latter map is defined into H(E) only when F+f belongs to K(Theta).
The kernel expansion proves completeness and fixes the multiplicity and pi.

## Canonical determinant calculation

Assume a specified self-adjoint A has discrete real eigenvalues lambda_j,
with finite multiplicities and sum_j (1+lambda_j^2)^(-1)<infinity.
Define Theta=1/2+iA on D(A), rho_j=1/2+i*lambda_j, and T=Theta^(-1).
Then T is Hilbert--Schmidt and

    D(s)=det_2(I-s*T)=product_j (1-s/rho_j)*exp(s/rho_j),
    D(0)=1, D'(0)=0,
    (log D)'(s)=Tr((sI-Theta)^(-1)+Theta^(-1)),
    (log D)''(s)=-Tr((sI-Theta)^(-2)).

The first trace contains a trace-class difference, not two separately
defined traces. Eigenvalue identification is an additional hypothesis.
If the rho_j are exactly the zero divisor of the order-one entire xi,
Hadamard factorization and evaluation at zero give

    xi(s)=(1/2)*exp(B*s)*D(s),
    B=xi'(0)/xi(0)=log(2*sqrt(pi))-1-EulerGamma/2.

At any regular s0, the corresponding identity is

    xi(s)/xi(s0)=exp((s-s0)*xi'(s0)/xi(s0))
      *det_2(I+(s-s0)*(s0I-Theta)^(-1)).

Equal divisors alone do not fix the prefactor. In dimension one,
the spectral zeta determinant of s-rho is s-rho, whereas det_2 is
(1-s/rho)*exp(s/rho). A spectral cut and analytic continuation are separate
data. No zeta-determinant identity follows merely from the divisor.

## Source locators and limits

Primary formulas checked: NIST DLMF 5.7.6, 5.9.16, 5.11.2.
Suzuki, arXiv:2301.00421v3, Sections 2.3--2.4, equations (2.4), (2.7)--(2.9),
(3.5), Proposition 4.1, and Theorem 1.1 confirm the de Branges conventions
and the pi factor. Hartmann--Lesch, arXiv:2106.02444v2, Theorems 4.3 and 4.5,
equations (4.4)--(4.7), separate canonical Fredholm and zeta determinants.
Their self-adjoint bounded-below theorem is not asserted directly for
the non-self-adjoint normal translate Theta. The product proof above applies
directly to that translate.

A first numerical attempt with system python3 failed because mpmath was
unavailable. No numerical sign or threshold value is claimed in this record.
Full proof TeX, reproducible calculations, source freeze, and local render follow.
Independent acceptance remains external to this construction lane.
