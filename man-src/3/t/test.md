---
title: "test(3)"
name: "test"
section: "3"
letter: "t"
url: "/docs/linux/man/3-test/"
description: "test – Test Suite"
---

<p>test &#8211; Test Suite<br />
&nbsp;<wbr></p>
<dl>
<dt><code>Class ActualActual</code></dt>
<dd>the correctness of the results is checked against known good values.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class AnalyticBarrierEngine</code></dt>
<dd>the correctness of the returned value is tested by reproducing results available in literature.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class AnalyticBSMHullWhiteEngine</code></dt>
<dd>the correctness of the returned value is tested by reproducing results available in web/literature</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class AnalyticCliquetEngine</code></dt>
<dd>
</dd><dt>*</dt>
<dd>the correctness of the returned value is tested by reproducing results available in literature.</dd>
<dt>*</dt>
<dd>the correctness of the returned greeks is tested by reproducing numerical derivatives.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class AnalyticContinuousFixedLookbackEngine</code></dt>
<dd>returned values are verified against results from literature</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class AnalyticContinuousFloatingLookbackEngine</code></dt>
<dd>returned values verified against results from literature</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class AnalyticContinuousGeometricAveragePriceAsianEngine</code></dt>
<dd>
</dd><dt>*</dt>
<dd>the correctness of the returned value is tested by reproducing results available in literature, and results obtained using a discrete average approximation.</dd>
<dt>*</dt>
<dd>the correctness of the returned greeks is tested by reproducing numerical derivatives.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class AnalyticDigitalAmericanEngine</code></dt>
<dd>
</dd><dt>*</dt>
<dd>the correctness of the returned value in case of cash-or-nothing at-hit digital payoff is tested by reproducing results available in literature.</dd>
<dt>*</dt>
<dd>the correctness of the returned value in case of asset-or-nothing at-hit digital payoff is tested by reproducing results available in literature.</dd>
<dt>*</dt>
<dd>the correctness of the returned value in case of cash-or-nothing at-expiry digital payoff is tested by reproducing results available in literature.</dd>
<dt>*</dt>
<dd>the correctness of the returned value in case of asset-or-nothing at-expiry digital payoff is tested by reproducing results available in literature.</dd>
<dt>*</dt>
<dd>the correctness of the returned greeks in case of cash-or-nothing at-hit digital payoff is tested by reproducing numerical derivatives.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class AnalyticDiscreteGeometricAveragePriceAsianEngine</code></dt>
<dd>
</dd><dt>*</dt>
<dd>the correctness of the returned value is tested by reproducing results available in literature.</dd>
<dt>*</dt>
<dd>the correctness of the available greeks is tested against numerical calculations.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class AnalyticDividendEuropeanEngine</code></dt>
<dd>the correctness of the returned greeks is tested by reproducing numerical derivatives.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class AnalyticEuropeanEngine</code></dt>
<dd>
</dd><dt>*</dt>
<dd>the correctness of the returned value is tested by reproducing results available in literature.</dd>
<dt>*</dt>
<dd>the correctness of the returned greeks is tested by reproducing results available in literature.</dd>
<dt>*</dt>
<dd>the correctness of the returned greeks is tested by reproducing numerical derivatives.</dd>
<dt>*</dt>
<dd>the correctness of the returned implied volatility is tested by using it for reproducing the target value.</dd>
<dt>*</dt>
<dd>the implied-volatility calculation is tested by checking that it does not modify the option.</dd>
<dt>*</dt>
<dd>the correctness of the returned value in case of cash-or-nothing digital payoff is tested by reproducing results available in literature.</dd>
<dt>*</dt>
<dd>the correctness of the returned value in case of asset-or-nothing digital payoff is tested by reproducing results available in literature.</dd>
<dt>*</dt>
<dd>the correctness of the returned value in case of gap digital payoff is tested by reproducing results available in literature.</dd>
<dt>*</dt>
<dd>the correctness of the returned greeks in case of cash-or-nothing digital payoff is tested by reproducing numerical derivatives.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class AnalyticGJRGARCHEngine</code></dt>
<dd>the correctness of the returned value is tested by reproducing results available in the Duan et al&#8217;s 2006 paper.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class AnalyticHestonEngine</code></dt>
<dd>the correctness of the returned value is tested by reproducing results available in web/literature and comparison with Black pricing.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class AnalyticHestonHullWhiteEngine</code></dt>
<dd>the correctness of the returned value is tested by reproducing results available in web/literature, testing against QuantLib&#8217;s analytic Heston and Black-Scholes-Merton Hull-White engine</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class AnalyticPerformanceEngine</code></dt>
<dd>the correctness of the returned greeks is tested by reproducing numerical derivatives.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Array</code></dt>
<dd>construction of arrays is checked in a number of cases</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class BaroneAdesiWhaleyApproximationEngine</code></dt>
<dd>the correctness of the returned value is tested by reproducing results available in literature.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class BatesEngine</code></dt>
<dd>the correctness of the returned value is tested by reproducing results available in web/literature, testing against QuantLib&#8217;s jump diffusion engine and comparison with Black pricing.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class BatesModel</code></dt>
<dd>calibration is tested against known values.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class BinomialVanillaEngine&lt; T &gt;</code></dt>
<dd>the correctness of the returned values is tested by checking it against analytic results.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Bisection</code></dt>
<dd>the correctness of the returned values is tested by checking them against known good results.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class BivariateCumulativeNormalDistributionDr78</code></dt>
<dd>the correctness of the returned value is tested by checking it against known good results.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class BivariateCumulativeNormalDistributionWe04DP</code></dt>
<dd>the correctness of the returned value is tested by checking it against known good results.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class BjerksundStenslandApproximationEngine</code></dt>
<dd>the correctness of the returned value is tested by reproducing results available in literature.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Bond</code></dt>
<dd>
</dd><dt>*</dt>
<dd>price/yield calculations are cross-checked for consistency.</dd>
<dt>*</dt>
<dd>price/yield calculations are checked against known good values.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Brazil</code></dt>
<dd>the correctness of the returned results is tested against a list of known holidays.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Brent</code></dt>
<dd>the correctness of the returned values is tested by checking them against known good results.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Calendar</code></dt>
<dd>the methods for adding and removing holidays are tested by inspecting the calendar before and after their invocation.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class CapFloor</code></dt>
<dd>
</dd><dt>*</dt>
<dd>the correctness of the returned value is tested by checking that the price of a cap (resp. floor) decreases (resp. increases) with the strike rate.</dd>
<dt>*</dt>
<dd>the relationship between the values of caps, floors and the resulting collars is checked.</dd>
<dt>*</dt>
<dd>the put-call parity between the values of caps, floors and swaps is checked.</dd>
<dt>*</dt>
<dd>the correctness of the returned implied volatility is tested by using it for reproducing the target value.</dd>
<dt>*</dt>
<dd>the correctness of the returned value is tested by checking it against a known good value.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class CmsRateBond</code></dt>
<dd>calculations are tested by checking results against cached values.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class CompositeQuote&lt; BinaryFunction &gt;</code></dt>
<dd>the correctness of the returned values is tested by checking them against numerical calculations.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class CompoundForward</code></dt>
<dd>
</dd><dt>*</dt>
<dd>the correctness of the curve is tested by reproducing the input data.</dd>
<dt>*</dt>
<dd>the correctness of the curve is tested by checking the consistency between returned rates and swaps priced on the curve.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class ConvergenceStatistics&lt; T, U &gt;</code></dt>
<dd>results are tested against known good values.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class CovarianceDecomposition</code></dt>
<dd>cross checked with getCovariance</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class CubicInterpolation</code></dt>
<dd>to be adapted from old ones.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class CumulativePoissonDistribution</code></dt>
<dd>the correctness of the returned value is tested by checking it against known good results.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Date</code></dt>
<dd>self-consistency of dates, serial numbers, days of month, months, and weekdays is checked over the whole date range.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class DerivedQuote&lt; UnaryFunction &gt;</code></dt>
<dd>the correctness of the returned values is tested by checking them against numerical calculations.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class DigitalCoupon</code></dt>
<dd>
</dd><dt>*</dt>
<dd>the correctness of the returned value in case of Asset-or-nothing embedded option is tested by pricing the digital option with Cox-Rubinstein formula.</dd>
<dt>*</dt>
<dd>the correctness of the returned value in case of deep-in-the-money Asset-or-nothing embedded option is tested vs the expected values of coupon and option.</dd>
<dt>*</dt>
<dd>the correctness of the returned value in case of deep-out-of-the-money Asset-or-nothing embedded option is tested vs the expected values of coupon and option.</dd>
<dt>*</dt>
<dd>the correctness of the returned value in case of Cash-or-nothing embedded option is tested by pricing the digital option with Reiner-Rubinstein formula.</dd>
<dt>*</dt>
<dd>the correctness of the returned value in case of deep-in-the-money Cash-or-nothing embedded option is tested vs the expected values of coupon and option.</dd>
<dt>*</dt>
<dd>the correctness of the returned value in case of deep-out-of-the-money Cash-or-nothing embedded option is tested vs the expected values of coupon and option.</dd>
<dt>*</dt>
<dd>the correctness of the returned value is tested checking the correctness of the call-put parity relation.</dd>
<dt>*</dt>
<dd>the correctness of the returned value is tested by the relationship between prices in case of different replication types.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class DPlusDMinus</code></dt>
<dd>the correctness of the returned values is tested by checking them against numerical calculations.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class DZero</code></dt>
<dd>the correctness of the returned values is tested by checking them against numerical calculations.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class ExchangeRate</code></dt>
<dd>application of direct and derived exchange rate is tested against calculations.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class ExchangeRateManager</code></dt>
<dd>lookup of direct, triangulated, and derived exchange rates is tested.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Factorial</code></dt>
<dd>the correctness of the returned value is tested by checking it against numerical calculations.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class FalsePosition</code></dt>
<dd>the correctness of the returned values is tested by checking them against known good results.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class FaureRsg</code></dt>
<dd>the correctness of the returned values is tested by reproducing known good values.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class FdBlackScholesBarrierEngine</code></dt>
<dd>the correctness of the returned value is tested by reproducing results available in web/literature and comparison with Black pricing.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class FdBlackScholesVanillaEngine</code></dt>
<dd>the correctness of the returned value is tested by reproducing results available in web/literature and comparison with Black pricing.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class FDEuropeanEngine</code></dt>
<dd>the correctness of the returned value is tested by checking it against analytic results.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class FdHestonBarrierEngine</code></dt>
<dd>the correctness of the returned value is tested by reproducing results available in web/literature and comparison with Black pricing.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class FdHestonVanillaEngine</code></dt>
<dd>the correctness of the returned value is tested by reproducing results available in web/literature and comparison with Black pricing.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class FixedRateBond</code></dt>
<dd>calculations are tested by checking results against cached values.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class FloatingRateBond</code></dt>
<dd>calculations are tested by checking results against cached values.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class ForwardPerformanceVanillaEngine&lt; Engine &gt;</code></dt>
<dd>
</dd><dt>*</dt>
<dd>the correctness of the returned value is tested by reproducing results available in literature.</dd>
<dt>*</dt>
<dd>the correctness of the returned greeks is tested by reproducing numerical derivatives.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class ForwardSpreadedTermStructure</code></dt>
<dd>
</dd><dt>*</dt>
<dd>the correctness of the returned values is tested by checking them against numerical calculations.</dd>
<dt>*</dt>
<dd>observability against changes in the underlying term structure and in the added spread is checked.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class ForwardVanillaEngine&lt; Engine &gt;</code></dt>
<dd>
</dd><dt>*</dt>
<dd>the correctness of the returned value is tested by reproducing results available in literature.</dd>
<dt>*</dt>
<dd>the correctness of the returned greeks is tested by reproducing numerical derivatives.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class GammaFunction</code></dt>
<dd>the correctness of the returned value is tested by checking it against known good results.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class GaussianQuadrature</code></dt>
<dd>the correctness of the result is tested by checking it against known good values.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class GaussKronrodAdaptive</code></dt>
<dd>the correctness of the result is tested by checking it against known good values.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class GenericSequenceStatistics&lt; StatisticsType &gt;</code></dt>
<dd>the correctness of the returned values is tested by checking them against numerical calculations.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Germany</code></dt>
<dd>the correctness of the returned results is tested against a list of known holidays.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class GJRGARCHModel</code></dt>
<dd>calibration is not implemented for GJR-GARCH</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class HaltonRsg</code></dt>
<dd>
</dd><dt>*</dt>
<dd>the correctness of the returned values is tested by reproducing known good values.</dd>
<dt>*</dt>
<dd>the correctness of the returned values is tested by checking their discrepancy against known good values.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class HestonModel</code></dt>
<dd>calibration is tested against known good values.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class HullWhite</code></dt>
<dd>calibration results are tested against cached values</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class ImpliedTermStructure</code></dt>
<dd>
</dd><dt>*</dt>
<dd>the correctness of the returned values is tested by checking them against numerical calculations.</dd>
<dt>*</dt>
<dd>observability against changes in the underlying term structure is checked.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Instrument</code></dt>
<dd>observability of class instances is checked.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class InterestRate</code></dt>
<dd>Converted rates are checked against known good results</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class InverseCumulativePoisson</code></dt>
<dd>the correctness of the returned value is tested by checking it against known good results.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Italy</code></dt>
<dd>the correctness of the returned results is tested against a list of known holidays.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class JointCalendar</code></dt>
<dd>the correctness of the returned results is tested by reproducing the calculations.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class JumpDiffusionEngine</code></dt>
<dd>
</dd><dt>*</dt>
<dd>the correctness of the returned value is tested by reproducing results available in literature.</dd>
<dt>*</dt>
<dd>the correctness of the returned greeks is tested by reproducing numerical derivatives.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class JuQuadraticApproximationEngine</code></dt>
<dd>the correctness of the returned value is tested by reproducing results available in literature.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class LfmHullWhiteParameterization</code></dt>
<dd>the correctness is tested by Monte-Carlo reproduction of caplet &amp; ratchet npvs and comparison with Black pricing.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class LiborForwardModel</code></dt>
<dd>the correctness is tested using Monte-Carlo Simulation to reproduce swaption npvs, model calibration and exact cap pricing</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class LiborForwardModelProcess</code></dt>
<dd>the correctness is tested by Monte-Carlo reproduction of caplet &amp; ratchet NPVs and comparison with Black pricing.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class LinearLeastSquaresRegression&lt; ArgumentType &gt;</code></dt>
<dd>the correctness of the returned values is tested by checking their properties.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class LongstaffSchwartzPathPricer&lt; PathType &gt;</code></dt>
<dd>the correctness of the returned value is tested by reproducing results available in web/literature</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member pseudoSqrt</code></dt>
<dd>
</dd><dt>*</dt>
<dd>the correctness of the results is tested by reproducing known good data.</dd>
<dt>*</dt>
<dd>the correctness of the results is tested by checking returned values against numerical calculations.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class MCAmericanEngine&lt; RNG, S &gt;</code></dt>
<dd>the correctness of the returned value is tested by reproducing results available in web/literature</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class MCBarrierEngine&lt; RNG, S &gt;</code></dt>
<dd>the correctness of the returned value is tested by reproducing results available in literature.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class MCBasketEngine&lt; RNG, S &gt;</code></dt>
<dd>the correctness of the returned value is tested by reproducing results available in literature.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class MCDigitalEngine&lt; RNG, S &gt;</code></dt>
<dd>the correctness of the returned value in case of cash-or-nothing at-hit digital payoff is tested by reproducing known good results.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class MCDiscreteArithmeticAPEngine&lt; RNG, S &gt;</code></dt>
<dd>the correctness of the returned value is tested by reproducing results available in literature.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class MCDiscreteGeometricAPEngine&lt; RNG, S &gt;</code></dt>
<dd>the correctness of the returned value is tested by reproducing results available in literature.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class MCEuropeanEngine&lt; RNG, S &gt;</code></dt>
<dd>the correctness of the returned value is tested by checking it against analytic results.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class MCEuropeanGJRGARCHEngine&lt; RNG, S &gt;</code></dt>
<dd>the correctness of the returned value is tested by reproducing results available in web/literature</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class MCEuropeanHestonEngine&lt; RNG, S &gt;</code></dt>
<dd>the correctness of the returned value is tested by reproducing results available in web/literature</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class MCLongstaffSchwartzEngine&lt; GenericEngine, MC, RNG, S &gt;</code></dt>
<dd>the correctness of the returned value is tested by reproducing results available in web/literature</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class MCVarianceSwapEngine&lt; RNG, S &gt;</code></dt>
<dd>returned fair variances checked for consistency with implied volatility curve.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class MersenneTwisterUniformRng</code></dt>
<dd>the correctness of the returned values is tested by checking them against known good results.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Money</code></dt>
<dd>money arithmetic is tested with and without currency conversions.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class MultiCubicSpline&lt; i &gt;</code></dt>
<dd>interpolated values are checked against the original function.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class MultiPathGenerator&lt; GSG &gt;</code></dt>
<dd>the generated paths are checked against cached results</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Newton</code></dt>
<dd>the correctness of the returned values is tested by checking them against known good results.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class NewtonSafe</code></dt>
<dd>the correctness of the returned values is tested by checking them against known good results.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class NormalDistribution</code></dt>
<dd>the correctness of the returned value is tested by checking it against numerical calculations. Cross-checks are also performed against the CumulativeNormalDistribution and InverseCumulativeNormal classes.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class OperatorFactory</code></dt>
<dd>coefficients are tested against constant BSM operator</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class PathGenerator&lt; GSG &gt;</code></dt>
<dd>the generated paths are checked against cached results</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Period</code></dt>
<dd>self-consistency of algebra is checked.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class PiecewiseYieldCurve&lt; Traits, Interpolator, Bootstrap &gt;</code></dt>
<dd>
</dd><dt>*</dt>
<dd>the correctness of the returned values is tested by checking them against the original inputs.</dd>
<dt>*</dt>
<dd>the observability of the term structure is tested.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class PoissonDistribution</code></dt>
<dd>the correctness of the returned value is tested by checking it against known good results.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class QuantoEngine&lt; Instr, Engine &gt;</code></dt>
<dd>
</dd><dt>*</dt>
<dd>the correctness of the returned value is tested by reproducing results available in literature.</dd>
<dt>*</dt>
<dd>the correctness of the returned greeks is tested by reproducing numerical derivatives.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Quote</code></dt>
<dd>the observability of class instances is tested.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class RandomizedLDS&lt; LDS, PRS &gt;</code></dt>
<dd>correct initialization is tested.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class ReplicatingVarianceSwapEngine</code></dt>
<dd>returned variances verified against results from literature</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Ridder</code></dt>
<dd>the correctness of the returned values is tested by checking them against known good results.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Rounding</code></dt>
<dd>the correctness of the returned values is tested by checking them against known good results.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Secant</code></dt>
<dd>the correctness of the returned values is tested by checking them against known good results.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class SeedGenerator</code></dt>
<dd>correct initialization of the single instance is tested.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class SegmentIntegral</code></dt>
<dd>the correctness of the result is tested by checking it against known good values.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class SimpleDayCounter</code></dt>
<dd>the correctness of the results is checked against known good values.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class SimpsonIntegral</code></dt>
<dd>the correctness of the result is tested by checking it against known good values.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class SobolRsg</code></dt>
<dd>
</dd><dt>*</dt>
<dd>the correctness of the returned values is tested by reproducing known good values.</dd>
<dt>*</dt>
<dd>the correctness of the returned values is tested by checking their discrepancy against known good values.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class StulzEngine</code></dt>
<dd>the correctness of the returned value is tested by reproducing results available in literature.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class SVD</code></dt>
<dd>the correctness of the returned values is tested by checking their properties.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class Swaption</code></dt>
<dd>
</dd><dt>*</dt>
<dd>the correctness of the returned value is tested by checking that the price of a payer (resp. receiver) swaption decreases (resp. increases) with the strike.</dd>
<dt>*</dt>
<dd>the correctness of the returned value is tested by checking that the price of a payer (resp. receiver) swaption increases (resp. decreases) with the spread.</dd>
<dt>*</dt>
<dd>the correctness of the returned value is tested by checking it against that of a swaption on a swap with no spread and a correspondingly adjusted fixed rate.</dd>
<dt>*</dt>
<dd>the correctness of the returned value is tested by checking it against a known good value.</dd>
<dt>*</dt>
<dd>the correctness of the returned value of cash settled swaptions is tested by checking the modified annuity against a value calculated without using the Swaption class.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class SymmetricSchurDecomposition</code></dt>
<dd>the correctness of the returned values is tested by checking their properties.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class TARGET</code></dt>
<dd>the correctness of the returned results is tested against a list of known holidays.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class TqrEigenDecomposition</code></dt>
<dd>the correctness of the result is tested by checking it against known good values.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class TrapezoidIntegral&lt; IntegrationPolicy &gt;</code></dt>
<dd>the correctness of the result is tested by checking it against known good values.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class TreeSwaptionEngine</code></dt>
<dd>calculations are checked against cached results</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class TreeVanillaSwapEngine</code></dt>
<dd>calculations are checked against known good results</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class UnitedKingdom</code></dt>
<dd>the correctness of the returned results is tested against a list of known holidays.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class UnitedStates</code></dt>
<dd>the correctness of the returned results is tested against a list of known holidays.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class VanillaSwap</code></dt>
<dd>
</dd><dt>*</dt>
<dd>the correctness of the returned value is tested by checking that the price of a swap paying the fair fixed rate is null.</dd>
<dt>*</dt>
<dd>the correctness of the returned value is tested by checking that the price of a swap receiving the fair floating-rate spread is null.</dd>
<dt>*</dt>
<dd>the correctness of the returned value is tested by checking that the price of a swap decreases with the paid fixed rate.</dd>
<dt>*</dt>
<dd>the correctness of the returned value is tested by checking that the price of a swap increases with the received floating-rate spread.</dd>
<dt>*</dt>
<dd>the correctness of the returned value is tested by checking it against a known good value.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class YieldTermStructure</code></dt>
<dd>observability against evaluation date changes is checked.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class ZeroCouponBond</code></dt>
<dd>calculations are tested by checking results against cached values.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Class ZeroSpreadedTermStructure</code></dt>
<dd>
</dd><dt>*</dt>
<dd>the correctness of the returned values is tested by checking them against numerical calculations.</dd>
<dt>*</dt>
<dd>observability against changes in the underlying term structure and in the added spread is checked.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member FDAmericanEngine</code></dt>
<dd>
</dd><dt>*</dt>
<dd>the correctness of the returned value is tested by reproducing results available in literature.</dd>
<dt>*</dt>
<dd>the correctness of the returned greeks is tested by reproducing numerical derivatives.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member FDDividendAmericanEngine</code></dt>
<dd>
</dd><dt>*</dt>
<dd>the correctness of the returned greeks is tested by reproducing numerical derivatives.</dd>
<dt>*</dt>
<dd>the invariance of the results upon addition of null dividends is tested.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member FDDividendEuropeanEngine</code></dt>
<dd>
</dd><dt>*</dt>
<dd>the correctness of the returned greeks is tested by reproducing numerical derivatives.</dd>
<dt>*</dt>
<dd>the invariance of the results upon addition of null dividends is tested.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member FDShoutEngine</code></dt>
<dd>the correctness of the returned greeks is tested by reproducing numerical derivatives.</dd></dl>
<p>&nbsp;<wbr></p>
<dl>
<dt><code>Member BSMTermOperator</code></dt>
<dd>coefficients are tested against constant BSM operator</dd></dl>
