---
title: "ql-todo(3)"
name: "ql-todo"
section: "3"
letter: "q"
url: "/docs/linux/man/3-ql-todo/"
description: "todo – Possible Enhancements"
---

<p>todo &#8211; Possible Enhancements<br/>
&nbsp;<wbr></p>
<dl>
<dt><code>Class AmericanCondition</code></dt>
<dd>unify the intrinsicValues/Payoff thing</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class AmericanExercise</code></dt>
<dd>check that everywhere the American condition is applied from earliestDate and not earlier</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class AmericanPayoffAtExpiry</code></dt>
<dd>calculate greeks</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class AmericanPayoffAtHit</code></dt>
<dd>calculate greeks</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class AnalyticContinuousGeometricAveragePriceAsianEngine</code></dt>
<dd>handle seasoned options</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class AnalyticDigitalAmericanEngine</code></dt>
<dd>add more greeks (as of now only delta and rho available)</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class AnalyticDiscreteGeometricAveragePriceAsianEngine</code></dt>
<dd>implement correct theta, rho, and dividend-rho calculation</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class BicubicSpline</code></dt>
<dd>revise end conditions</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class BinomialVanillaEngine&lt; T &gt;</code></dt>
<dd>Greeks are not overly accurate. They could be improved by building a tree so that it has three points at the current time. The value would be fetched from the middle one, while the two side points would be used for estimating partial derivatives.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class BivariateCumulativeNormalDistributionDr78</code></dt>
<dd>check accuracy of this algorithm and compare with: 1) Drezner, Z, (1978), Computation of the bivariate normal integral, Mathematics of Computation 32, pp. 277-279. 2) Drezner, Z. and Wesolowsky, G. O. (1990) `On the Computation of the Bivariate Normal Integral&#8217;, Journal of Statistical Computation and Simulation 35, pp. 101-107. 3) Drezner, Z (1992) Computation of the Multivariate Normal Integral, ACM Transactions on Mathematics Software 18, pp. 450-460. 4) Drezner, Z (1994) Computation of the Trivariate Normal Integral, Mathematics of Computation 62, pp. 289-294. 5) Genz, A. (1992) `Numerical Computation of the Multivariate Normal Probabilities&#8217;, J. Comput. Graph. Stat. 1, pp. 141-150.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class BlackCallableFixedRateBondEngine</code></dt>
<dd>set additionalResults (e.g. vega, fairStrike, etc.)</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class BlackVarianceCurve</code></dt>
<dd>check time extrapolation</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class BlackVarianceSurface</code></dt>
<dd>check time extrapolation</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::BoundaryCondition::Side</code></dt>
<dd>Generalize for n-dimensional conditions</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class CallableBond</code></dt>
<dd>models/shortrate/calibrationHelpers</dd></dl>
<p> OAS/OAD floating rate callable bonds ?<br/>
&nbsp;<wbr></p>
<dl>
<dt><code>Class CashFlows</code></dt>
<dd>add tests</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class CDO</code></dt>
<dd>Investigate and fix cases $ E_{i+1} &lt; E_i. $</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Cdor</code></dt>
<dd>check settlement days, end-of-month adjustment, and day-count convention.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class CdsOption</code></dt>
<dd>take premium accrual into account</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class CdsOption</code></dt>
<dd>allow expiry to be different from CDS start date</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class CliquetOption</code></dt>
<dd>
</dd><dt>*</dt>
<dd>add local/global caps/floors</dd>
<dt>*</dt>
<dd>add accrued coupon and last fixing</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class ContinuousAveragingAsianOption</code></dt>
<dd>add running average</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class CubicInterpolation</code></dt>
<dd>implement missing schemes (FourthOrder and ModifiedParabolic) and missing boundary conditions (Periodic and Lagrange).</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class DirichletBC</code></dt>
<dd>generalize to time-dependent conditions.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class ExplicitEuler&lt; Operator &gt;</code></dt>
<dd>add Richardson extrapolation</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class FDDividendEngineBase</code></dt>
<dd>The dividend class really needs to be made more sophisticated to distinguish between fixed dividends and fractional dividends</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class FittedBondDiscountCurve</code></dt>
<dd>refactor the bond helper class so that it is pure virtual and returns a generic bond or its cash flows. Derived classes would include helpers for fixed-rate and zero-coupon bonds. In this way, both bonds and bills can be used to fit a discount curve using the exact same machinery. At present, only fixed-coupon bonds are supported. An even better way to move forward might be to get rate helpers to return cashflows, in which case this class could be used to fit any set of cash flows, not just bonds.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class FittedBondDiscountCurve</code></dt>
<dd>add more fitting diagnostics: smoothness, standard deviation, student-t test, etc. Generic smoothness method may be useful for smoothing splines fitting. See Fisher, M., D. Nychka and D. Zervos: &#8216;Fitting the term structure of interest rates with smoothing splines.&#8217; Board of Governors of the Federal Reserve System, Federal Resere Board Working Paper, 95-1.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class FittedBondDiscountCurve</code></dt>
<dd>add extrapolation routines</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class FittingMethod</code></dt>
<dd>derive the special-case class LinearFittingMethods from FittingMethod. A linear fitting to a set of basis functions $ b_i(t) $ is any fitting of the form [ d(t) = um_{i=0} c_i b_i(t) ] i.e., linear in the unknown coefficients $ c_i $. Such a fitting can be reduced to a linear algebra problem $ Ax = b $, and for large numbers of bonds, would typically be much faster computationally than the generic non-linear fitting method.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class FixedRateBondForward</code></dt>
<dd>Add preconditions and tests</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class FixedRateBondForward</code></dt>
<dd>Create switch- if coupon goes to seller is toggled on, don&#8217;t consider income in the $ P_{DirtyFwd}(t) $ calculation.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class FixedRateBondForward</code></dt>
<dd>Verify this works when the underlying is paper (in which case ignore all AI.)</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Forward</code></dt>
<dd>Add preconditions and tests</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::GeneralizedBlackScholesProcess::drift</code>(Time t, Real x) const</dt>
<dd>revise extrapolation</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::GeneralizedBlackScholesProcess::diffusion</code>(Time t, Real x) const</dt>
<dd>revise extrapolation</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class GenericRiskStatistics&lt; S &gt;</code></dt>
<dd>add historical annualized volatility</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class IntegralEngine</code></dt>
<dd>define tolerance for calculate()</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class InterestRateIndex</code></dt>
<dd>add methods returning InterestRate</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class InverseCumulativeStudent</code></dt>
<dd>Find/implement an efficient algorithm for evaluating the cumulative Student t-distribution, replacing the Newton iteration</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Jibar</code></dt>
<dd>check settlement days and day-count convention.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class MCVarianceSwapEngine&lt; RNG, S &gt;</code></dt>
<dd>define tolerance of numerical integral and incorporate it in errorEstimate</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class MixedScheme&lt; Operator &gt;</code></dt>
<dd>
</dd><dt>*</dt>
<dd>derive variable theta schemes</dd>
<dt>*</dt>
<dd>introduce multi time-level schemes.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class MultiCubicSpline&lt; i &gt;</code></dt>
<dd>
</dd><dt>*</dt>
<dd>allow extrapolation as for the other interpolations</dd>
<dt>*</dt>
<dd>investigate if and how to implement Hyman filters and different boundary conditions</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class NeumannBC</code></dt>
<dd>generalize to time-dependent conditions.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class OneFactorCopula</code></dt>
<dd>Improve on simple Euler integration</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class OneFactorGaussianStudentCopula</code></dt>
<dd>Improve performance/accuracy of the calculation of inverse cumulative Y. Tabulate and store it for selected correlations?</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class OneFactorStudentCopula</code></dt>
<dd>Improve performance/accuracy of the calculation of inverse cumulative Y. Tabulate and store it for selected correlations?</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class OneFactorStudentGaussianCopula</code></dt>
<dd>Improve performance/accuracy of the calculation of inverse cumulative Y. Tabulate and store it for selected correlations?</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class RandomizedLDS&lt; LDS, PRS &gt;</code></dt>
<dd>implement the other randomization algorithms</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::SampledCurve::valueAtCenter</code>() const</dt>
<dd>replace or complement with a more general function valueAt(spot)</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::SampledCurve::firstDerivativeAtCenter</code>() const</dt>
<dd>replace or complement with a more general function firstDerivativeAt(spot)</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member QuantLib::SampledCurve::secondDerivativeAtCenter</code>() const</dt>
<dd>replace or complement with a more general function secondDerivativeAt(spot)</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Solver1D&lt; Impl &gt;</code></dt>
<dd>
</dd><dt>*</dt>
<dd>clean up the interface so that it is clear whether the accuracy is specified for $ x $ or $ f(x) $.</dd>
<dt>*</dt>
<dd>add target value (now the target value is 0.0)</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class SwapRateHelper</code></dt>
<dd>use input SwapIndex to create the swap</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Swaption</code></dt>
<dd>add greeks and explicit exercise lag</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class SyntheticCDO</code></dt>
<dd>Investigate and fix cases $ E_{i+1} &lt; E_i. $</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Tibor</code></dt>
<dd>check settlement days and end-of-month adjustment.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class TimeGrid</code></dt>
<dd>what was the rationale for limiting the grid to positive times? Investigate and see whether we can use it for negative ones as well.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class TRLibor</code></dt>
<dd>check end-of-month adjustment.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class UnitedKingdom</code></dt>
<dd>add LIFFE</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class YieldTermStructure</code></dt>
<dd>add derived class ParSwapTermStructure similar to ZeroYieldTermStructure, DiscountStructure, ForwardRateStructure</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Zibor</code></dt>
<dd>check settlement days, end-of-month adjustment, and day-count convention.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>File syntheticcdoengines.hpp</code></dt>
<dd>Add further engines for analytical expected tranche loss cases &#8211; large homogeneous pool with Normal Inverse Gaussian, Gamma copula</dd></dl>
