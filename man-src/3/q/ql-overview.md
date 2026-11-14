---
title: "ql-overview(3)"
name: "ql-overview"
section: "3"
letter: "q"
url: "/docs/linux/man/3-ql-overview/"
description: "overview – Project overview The QuantLib project is at this time in beta status. The following list is a (possibly outdated) overview of the existing code base. The QuantLib-users and QuantLib-dev ..."
---

<p>overview &#8211; Project overview The QuantLib project is at this time in <i>beta</i> status. The following list is a (possibly outdated) overview of the existing code base. The QuantLib-users and QuantLib-dev mailing lists are the preferred forum for proposals, suggestions and contributions regarding the future development of the library. <code>Date, calendars, and day count conventions</code></p>
<dl>
<dt>*</p>
<dd>Date class.</p>
<dt>*</p>
<dd>Weekday, month, frequency, time unit enumerations.</p>
<dt>*</p>
<dd>Period class (eg. 1y, 30d, 2m, etc.)</p>
<dt>*</p>
<dd>IMM calculation.</p>
<dt>*</p>
<dd>More than 30 business calendars.</p>
<dt>*</p>
<dd>NullCalendar (no holidays) for theoretical calculations.</p>
<dt>*</p>
<dd>Joint calendars made up as holiday union or intersection of base calendars.</p>
<dt>*</p>
<dd>Rolling conventions: Preceding, ModifiedPreceding, Following, ModifiedFollowing, MonthEndReference.</p>
<dt>*</p>
<dd>Schedule class for date stream generation.</p>
<dt>*</p>
<dd>Day count conventions: Actual360, Actual365Fixed, ActualActual (Bond, ISDA, AFB), 30/360 (US, European, Italian), 1/1.</dl>
<p> <code>Math</code></p>
<dl>
<dt>*</p>
<dd>Linear, log-linear, and cubic spline interpolation.</p>
<dt>*</p>
<dd>Primitive, first and second derivative functions of cubic and linear interpolators.</p>
<dt>*</p>
<dd>Cubic spline end conditions: first derivative value, second derivative value, not-a-knot.</p>
<dt>*</p>
<dd>Monotone cubic spline with Hyman non-restrictive filter.</p>
<dt>*</p>
<dd>Bicubic spline and bilinear interpolations.</p>
<dt>*</p>
<dd>N-dimensional cubic spline interpolation.</p>
<dt>*</p>
<dd>Normal and cumulative normal distributions.</p>
<dt>*</p>
<dd>Inverse cumulative normal distribution: Moro and Acklam approximations.</p>
<dt>*</p>
<dd>Bivariate cumulative normal distribution.</p>
<dt>*</p>
<dd>Binomial coefficients, binomial distribution, cumulative binomial distribution, and Peizer-Pratt inversion (method 2.)</p>
<dt>*</p>
<dd>Chi square and non-central chi square distributions.</p>
<dt>*</p>
<dd>Beta functions.</p>
<dt>*</p>
<dd>Poisson and cumulative Poisson distributions.</p>
<dt>*</p>
<dd>Incomplete gamma functions.</p>
<dt>*</p>
<dd>Gamma distribution.</p>
<dt>*</p>
<dd>Factorials.</p>
<dt>*</p>
<dd>Integration algorithms: segment, trapezoid, mid-point trapezoid, Simpson, Gauss-Kronrod.</p>
<dt>*</p>
<dd>Error function.</p>
<dt>*</p>
<dd>General 1-D statistics: mean, variance, standard deviation, skewness, kurtosis, error estimation, min, max.</p>
<dt>*</p>
<dd>Multi-dimensional (sequence) statistics: all the 1-D methods plus covariance, correlation, L2-discrepancy calculation, etc.</p>
<dt>*</p>
<dd>Risk measures for Gaussian and empirical distributions: semi-variance, regret, percentile, top percentile, value-at-risk, upside potential, shorfall, average shorfall, expected shortfall.</p>
<dt>*</p>
<dd>Array and matrix classes for algebra.</p>
<dt>*</p>
<dd>Singular value decomposition.</p>
<dt>*</p>
<dd>Eigenvalues, eigenvectors for symmetric matrices.</p>
<dt>*</p>
<dd>Cholesky decomposition.</p>
<dt>*</p>
<dd>Schur decomposition.</p>
<dt>*</p>
<dd>Spectral rank-reduced square root, spectral pseudo-square root.</dl>
<p> <code>1-dimensional solvers</code></p>
<dl>
<dt>*</p>
<dd>Bisection, false position, Newton, bounded Newton, Ridder, secant, Brent.</dl>
<p> <code>Optimization</code></p>
<dl>
<dt>*</p>
<dd>Conjugate gradient, simplex, steepest descent, line search, Armijo line search, least squares.</p>
<dt>*</p>
<dd>Constrained (positive, boundary, etc.) and unconstrained optimization</dl>
<p> <code>Random-number generation</code></p>
<dl>
<dt>*</p>
<dd>Uniform pseudo-random sequences: Knuth, L&#8217;Ecuyer, Mersenne twister.</p>
<dt>*</p>
<dd>Uniform quasi-random (low-discrepancy) sequences: Halton, Faure, Sobol up to dimension 21,200 (8,129,334 if you really want) with unit, Jäckel, Bradley-Fox, and Lemieux-Cieslak-Luttmer initialization numbers.</p>
<dt>*</p>
<dd>Randomized quasi-random sequences (in progress)</p>
<dt>*</p>
<dd>Randomized (shifted) low-discrepancy sequences.</p>
<dt>*</p>
<dd>Primitive polynomials modulo 2 up to dimension 18 (available up to dimension 27)</p>
<dt>*</p>
<dd>Gaussian random numbers from uniform random numbers using different algorithms: central limit theorem, Box-Muller, inverse cumulative (Moro and Acklam algorithms)</dl>
<p> <code>Patterns</code></p>
<dl>
<dt>*</p>
<dd>Bridge, composite, lazy object, observer/observable, singleton, strategy, visitor.</dl>
<p> <code>Finite differences</code></p>
<dl>
<dt>*</p>
<dd>Mixed theta, implicit, explicit, and Crank-Nicolson 1-dimensional schemes.</p>
<dt>*</p>
<dd>Differential operators: $ D_{0} $, $ D_{+} $, $ D_{-} $, $ D_{+}D_{-} $.</p>
<dt>*</p>
<dd>Shout, Bermudan and American exercises.</dl>
<p> <code>Lattices</code></p>
<dl>
<dt>*</p>
<dd>Binomial trees: Cox-Ross-Rubinstein, Jarrow-Rudd, additive equiprobabilities, Trigeorgis, Tian, Leisen-Reimer.</p>
<dt>*</p>
<dd>Trinomial (interest-rate) tree.</p>
<dt>*</p>
<dd>Discretized asset.</p>
<dt>*</p>
<dd>Richardson extrapolation</dl>
<p> <code>Monte Carlo</code></p>
<dl>
<dt>*</p>
<dd>One-factor and multi-factor path classes.</p>
<dt>*</p>
<dd>Path-generator classes: incremental and Brownian-bridge one-factor path generation, incremental multi-factor path generation.</p>
<dt>*</p>
<dd>General-purpose Monte Carlo model based on traits for path samples.</p>
<dt>*</p>
<dd>Antithetic variance-reduction technique.</p>
<dt>*</p>
<dd>Control variate technique.</dl>
<p> <code>Pricing engines</code></p>
<dl>
<dt>*</p>
<dd>Analytic Black formula (plus greeks) for different payoffs.</p>
<dt>*</p>
<dd>Analytic formula for American-style digital options with payoff at expiry.</p>
<dt>*</p>
<dd>Analytic formula for American-style digital options with payoff at hit.</p>
<dt>*</p>
<dd>Monte Carlo simulation base engine.</p>
<dt>*</p>
<dd>Lattice short rate model base engine.</p>
<dt>*</p>
<dd>Engines for options described by &#8216;vanilla&#8217; set of parameters: analytic digital American, analytic discrete-dividend European, analytic European, Barone-Adesi and Whaley approximation for American, Ju approximation for American, binomial (Cox-Ross-Rubinstein, Jarrow-Rudd, additive equiprobabilities, Trigeorgis, Tian, Leisen-Reimer), Bjerksund and Stensland approximation for American, integral European, Merton 76 jump-diffusion, Monte Carlo digital, Monte Carlo European, Bates and Heston models, finite-difference European, Bermudan and American.</p>
<dt>*</p>
<dd>Engines for options described by &#8216;barrier&#8217; set of parameters: analytic down/up in/out, Monte Carlo down/up in/out</p>
<dt>*</p>
<dd>Engines for Asian options: analytic discrete geometric average-price, analytic continuous geometric average-price, Monte Carlo discrete arithmetic average-price, Monte Carlo discrete geometric average-price.</p>
<dt>*</p>
<dd>Engines for options described by &#8216;cliquet&#8217; set of parameters: analytic, analytic performance.</p>
<dt>*</p>
<dd>Forward and forward-performance compound engines.</p>
<dt>*</p>
<dd>Quanto compound engine.</p>
<dt>*</p>
<dd>Quanto-forward and Quanto-forward-performance compound engines.</p>
<dt>*</p>
<dd>Basket engine: analytic Stulz engine for max/min on two assets, Monte Carlo engine (in progress).</p>
<dt>*</p>
<dd>Black model base class for vanilla interest rate derivatives</p>
<dt>*</p>
<dd>Cap/floor pricing engines: analytic Black model, analytic affine models, tree based engine.</p>
<dt>*</p>
<dd>Swaption pricing engines: analytic Black model, analytic affine models (Jamshidian), tree based engine.</dl>
<p> <code>Pricers</code></p>
<dl>
<dt>*</p>
<dd>Cliquet option</p>
<dt>*</p>
<dd>Analytic discrete geometric average-price option (European exercise).</p>
<dt>*</p>
<dd>Analytic discrete geometric average-strike option (European exercise).</p>
<dt>*</p>
<dd>Monte Carlo cliquet option.</p>
<dt>*</p>
<dd>Monte Carlo discrete arithmetic average-price option.</p>
<dt>*</p>
<dd>Monte Carlo discrete arithmetic average-strike option.</p>
<dt>*</p>
<dd>Monte Carlo Everest option.</p>
<dt>*</p>
<dd>Monte Carlo Himalaya option.</p>
<dt>*</p>
<dd>Monte Carlo max basket option.</p>
<dt>*</p>
<dd>Monte Carlo pagoda option.</p>
<dt>*</p>
<dd>Monte Carlo forward performance option.</dl>
<p> <code>Financial Instruments</code></p>
<dl>
<dt>*</p>
<dd>Instrument base class: npv(), isExpired(), etc.</p>
<dt>*</p>
<dd>Interest-rate swap.</p>
<dt>*</p>
<dd>Swaption.</p>
<dt>*</p>
<dd>Cap/floor.</p>
<dt>*</p>
<dd>Zero-coupon, fixed-rate coupon, and floating-rate coupon bond.</p>
<dt>*</p>
<dd>Convertible bond.</p>
<dt>*</p>
<dd>Stock.</p>
<dt>*</p>
<dd>One-asset option base class.</p>
<dt>*</p>
<dd>Asian option.</p>
<dt>*</p>
<dd>Barrier option.</p>
<dt>*</p>
<dd>Cliquet option.</p>
<dt>*</p>
<dd>Forward vanilla option.</p>
<dt>*</p>
<dd>Quanto vanilla option.</p>
<dt>*</p>
<dd>Quanto-forward vanilla option.</p>
<dt>*</p>
<dd>Vanilla option.</p>
<dt>*</p>
<dd>Multi-asset option base class.</p>
<dt>*</p>
<dd>Basket option.</p>
<dt>*</p>
<dd>More&#8230;</dl>
<p> <code>Yield term structures</code></p>
<dl>
<dt>*</p>
<dd>Term structure common interface.</p>
<dt>*</p>
<dd>Term structure classes based on discount, zero, or forward underlying description.</p>
<dt>*</p>
<dd>Term structure based on linear interpolation of zero yields.</p>
<dt>*</p>
<dd>Term structure based on log-linear interpolation of discounts.</p>
<dt>*</p>
<dd>Term structure based on constant flat forward.</p>
<dt>*</p>
<dd>Term structure based on piecewise-constant flat forwards with libor-futures-swap bootstrapping algorithm.</p>
<dt>*</p>
<dd>Spreaded term structures.</p>
<dt>*</p>
<dd>Forward-date implied term structure.</dl>
<p> <code>Volatility</code></p>
<dl>
<dt>*</p>
<dd>Interface for cap/floor Black volatility term structures (unstable).</p>
<dt>*</p>
<dd>Interface for swaption Black volatility term structures (unstable).</p>
<dt>*</p>
<dd>Interface for equity Black volatility term structures based on volatility or variance underlying description: constant, time-dependant curve, time-strike surface, forward date implied term structure.</p>
<dt>*</p>
<dd>Interface for equity local volatility term structures: constant, time-dependant curve, time-asset level surface (Gatheral&#8217;s formula).</dl>
<p> <code>Short rate models</code></p>
<dl>
<dt>*</p>
<dd>Single factor models: Hull-White, Black-Karasinski, Vasichek (untested), CIR (untested), Extended CIR (untested).</p>
<dt>*</p>
<dd>Two factor models: G2 (untested).</dl>
<p> <code>Test suite</code> Implemented by means of the Boost unit-test framework. More than 300 automated tests. <code>Miscellanea</code></p>
<dl>
<dt>*</p>
<dd>Index classes for handling of fixed-income libor indexes (fixings, forecasting, etc.)</p>
<dt>*</p>
<dd>Cash-flow class.</p>
<dt>*</p>
<dd>Currency class and enumeration.</p>
<dt>*</p>
<dd>Money class with automatic exchange-rate capabilities.</p>
<dt>*</p>
<dd>Output data formatters: long integers, Ordinal numerals, power of two, exponential, fixed digit, sequences, dates, etc.</p>
<dt>*</p>
<dd>Input data parsers.</p>
<dt>*</p>
<dd>Error classes and error handling.</p>
<dt>*</p>
<dd>Exercise classes: European, Bermudan, American</p>
<dt>*</p>
<dd>Payoff classes: plain, gap, asset-or-nothing, cash-or-nothing</p>
<dt>*</p>
<dd>Grid classes for handling of equally and unequally spaced grids.</p>
<dt>*</p>
<dd>History class for handling of historical data.</p>
<dt>*</p>
<dd>Quote class for mutable data.</p>
<dt>*</p>
<dd>Null types.</p>
<dt>*</p>
<dd>User-configurable flag to disable usage of deprecated classes.</dl>
<p> <code>Documentation</code></p>
<dl>
<dt>*</p>
<dd>Documentation automatically generated with Doxygen</dl>
