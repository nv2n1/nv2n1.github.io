---
title: "ql-todo(3)"
name: "ql-todo"
section: "3"
letter: "q"
url: "/docs/linux/man/3-ql-todo/"
description: "todo – Possible Enhancements"
---

<p>todo &#8211; Possible Enhancements<br />
&nbsp;<wbr></p>
<dl>
<dt><code>Class AmericanCondition</code></p>
<dd>unify the intrinsicValues/Payoff thing</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class AmericanExercise</code></p>
<dd>check that everywhere the American condition is applied from earliestDate and not earlier</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class AmericanPayoffAtExpiry</code></p>
<dd>calculate greeks</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class AmericanPayoffAtHit</code></p>
<dd>calculate greeks</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class AnalyticContinuousGeometricAveragePriceAsianEngine</code></p>
<dd>handle seasoned options</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class AnalyticDigitalAmericanEngine</code></p>
<dd>add more greeks (as of now only delta and rho available)</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class AnalyticDiscreteGeometricAveragePriceAsianEngine</code></p>
<dd>implement correct theta, rho, and dividend-rho calculation</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class BicubicSpline</code></p>
<dd>revise end conditions</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class BinomialVanillaEngine&lt; T &gt;</code></p>
<dd>Greeks are not overly accurate. They could be improved by building a tree so that it has three points at the current time. The value would be fetched from the middle one, while the two side points would be used for estimating partial derivatives.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class BivariateCumulativeNormalDistributionDr78</code></p>
<dd>check accuracy of this algorithm and compare with: 1) Drezner, Z, (1978), Computation of the bivariate normal integral, Mathematics of Computation 32, pp. 277-279. 2) Drezner, Z. and Wesolowsky, G. O. (1990) `On the Computation of the Bivariate Normal Integral&#8217;, Journal of Statistical Computation and Simulation 35, pp. 101-107. 3) Drezner, Z (1992) Computation of the Multivariate Normal Integral, ACM Transactions on Mathematics Software 18, pp. 450-460. 4) Drezner, Z (1994) Computation of the Trivariate Normal Integral, Mathematics of Computation 62, pp. 289-294. 5) Genz, A. (1992) `Numerical Computation of the Multivariate Normal Probabilities&#8217;, J. Comput. Graph. Stat. 1, pp. 141-150.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class BlackCallableFixedRateBondEngine</code></p>
<dd>set additionalResults (e.g. vega, fairStrike, etc.)</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class BlackVarianceCurve</code></p>
<dd>check time extrapolation</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class BlackVarianceSurface</code></p>
<dd>check time extrapolation</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::BoundaryCondition::Side</code></p>
<dd>Generalize for n-dimensional conditions</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class CallableBond</code></p>
<dd>models/shortrate/calibrationHelpers</dl>
<p> OAS/OAD floating rate callable bonds ?<br />
&nbsp;<wbr></p>
<dl>
<dt><code>Class CashFlows</code></p>
<dd>add tests</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class CDO</code></p>
<dd>Investigate and fix cases $ E_{i+1} &lt; E_i. $</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Cdor</code></p>
<dd>check settlement days, end-of-month adjustment, and day-count convention.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class CdsOption</code></p>
<dd>take premium accrual into account</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class CdsOption</code></p>
<dd>allow expiry to be different from CDS start date</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class CliquetOption</code></p>
<dd>
<dt>*</p>
<dd>add local/global caps/floors</p>
<dt>*</p>
<dd>add accrued coupon and last fixing</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class ContinuousAveragingAsianOption</code></p>
<dd>add running average</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class CubicInterpolation</code></p>
<dd>implement missing schemes (FourthOrder and ModifiedParabolic) and missing boundary conditions (Periodic and Lagrange).</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class DirichletBC</code></p>
<dd>generalize to time-dependent conditions.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class ExplicitEuler&lt; Operator &gt;</code></p>
<dd>add Richardson extrapolation</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class FDDividendEngineBase</code></p>
<dd>The dividend class really needs to be made more sophisticated to distinguish between fixed dividends and fractional dividends</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class FittedBondDiscountCurve</code></p>
<dd>refactor the bond helper class so that it is pure virtual and returns a generic bond or its cash flows. Derived classes would include helpers for fixed-rate and zero-coupon bonds. In this way, both bonds and bills can be used to fit a discount curve using the exact same machinery. At present, only fixed-coupon bonds are supported. An even better way to move forward might be to get rate helpers to return cashflows, in which case this class could be used to fit any set of cash flows, not just bonds.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class FittedBondDiscountCurve</code></p>
<dd>add more fitting diagnostics: smoothness, standard deviation, student-t test, etc. Generic smoothness method may be useful for smoothing splines fitting. See Fisher, M., D. Nychka and D. Zervos: &#8216;Fitting the term structure of interest rates with smoothing splines.&#8217; Board of Governors of the Federal Reserve System, Federal Resere Board Working Paper, 95-1.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class FittedBondDiscountCurve</code></p>
<dd>add extrapolation routines</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class FittingMethod</code></p>
<dd>derive the special-case class LinearFittingMethods from FittingMethod. A linear fitting to a set of basis functions $ b_i(t) $ is any fitting of the form [ d(t) = um_{i=0} c_i b_i(t) ] i.e., linear in the unknown coefficients $ c_i $. Such a fitting can be reduced to a linear algebra problem $ Ax = b $, and for large numbers of bonds, would typically be much faster computationally than the generic non-linear fitting method.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class FixedRateBondForward</code></p>
<dd>Add preconditions and tests</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class FixedRateBondForward</code></p>
<dd>Create switch- if coupon goes to seller is toggled on, don&#8217;t consider income in the $ P_{DirtyFwd}(t) $ calculation.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class FixedRateBondForward</code></p>
<dd>Verify this works when the underlying is paper (in which case ignore all AI.)</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Forward</code></p>
<dd>Add preconditions and tests</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::GeneralizedBlackScholesProcess::drift</code>(Time t, Real x) const</p>
<dd>revise extrapolation</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::GeneralizedBlackScholesProcess::diffusion</code>(Time t, Real x) const</p>
<dd>revise extrapolation</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class GenericRiskStatistics&lt; S &gt;</code></p>
<dd>add historical annualized volatility</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class IntegralEngine</code></p>
<dd>define tolerance for calculate()</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class InterestRateIndex</code></p>
<dd>add methods returning InterestRate</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class InverseCumulativeStudent</code></p>
<dd>Find/implement an efficient algorithm for evaluating the cumulative Student t-distribution, replacing the Newton iteration</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Jibar</code></p>
<dd>check settlement days and day-count convention.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class MCVarianceSwapEngine&lt; RNG, S &gt;</code></p>
<dd>define tolerance of numerical integral and incorporate it in errorEstimate</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class MixedScheme&lt; Operator &gt;</code></p>
<dd>
<dt>*</p>
<dd>derive variable theta schemes</p>
<dt>*</p>
<dd>introduce multi time-level schemes.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class MultiCubicSpline&lt; i &gt;</code></p>
<dd>
<dt>*</p>
<dd>allow extrapolation as for the other interpolations</p>
<dt>*</p>
<dd>investigate if and how to implement Hyman filters and different boundary conditions</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class NeumannBC</code></p>
<dd>generalize to time-dependent conditions.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class OneFactorCopula</code></p>
<dd>Improve on simple Euler integration</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class OneFactorGaussianStudentCopula</code></p>
<dd>Improve performance/accuracy of the calculation of inverse cumulative Y. Tabulate and store it for selected correlations?</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class OneFactorStudentCopula</code></p>
<dd>Improve performance/accuracy of the calculation of inverse cumulative Y. Tabulate and store it for selected correlations?</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class OneFactorStudentGaussianCopula</code></p>
<dd>Improve performance/accuracy of the calculation of inverse cumulative Y. Tabulate and store it for selected correlations?</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class RandomizedLDS&lt; LDS, PRS &gt;</code></p>
<dd>implement the other randomization algorithms</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::SampledCurve::valueAtCenter</code>() const</p>
<dd>replace or complement with a more general function valueAt(spot)</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::SampledCurve::firstDerivativeAtCenter</code>() const</p>
<dd>replace or complement with a more general function firstDerivativeAt(spot)</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::SampledCurve::secondDerivativeAtCenter</code>() const</p>
<dd>replace or complement with a more general function secondDerivativeAt(spot)</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Solver1D&lt; Impl &gt;</code></p>
<dd>
<dt>*</p>
<dd>clean up the interface so that it is clear whether the accuracy is specified for $ x $ or $ f(x) $.</p>
<dt>*</p>
<dd>add target value (now the target value is 0.0)</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class SwapRateHelper</code></p>
<dd>use input SwapIndex to create the swap</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Swaption</code></p>
<dd>add greeks and explicit exercise lag</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class SyntheticCDO</code></p>
<dd>Investigate and fix cases $ E_{i+1} &lt; E_i. $</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Tibor</code></p>
<dd>check settlement days and end-of-month adjustment.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class TimeGrid</code></p>
<dd>what was the rationale for limiting the grid to positive times? Investigate and see whether we can use it for negative ones as well.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class TRLibor</code></p>
<dd>check end-of-month adjustment.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class UnitedKingdom</code></p>
<dd>add LIFFE</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class YieldTermStructure</code></p>
<dd>add derived class ParSwapTermStructure similar to ZeroYieldTermStructure, DiscountStructure, ForwardRateStructure</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Zibor</code></p>
<dd>check settlement days, end-of-month adjustment, and day-count convention.</dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>File syntheticcdoengines.hpp</code></p>
<dd>Add further engines for analytical expected tranche loss cases &#8211; large homogeneous pool with Normal Inverse Gaussian, Gamma copula</dl>
