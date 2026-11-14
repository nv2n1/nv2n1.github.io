---
title: "dividendrhocomputed_(3)"
name: "dividendrhocomputed_"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dividendrhocomputed_/"
description: "QuantLib::SingleAssetOption – Black-Scholes-Merton option."
---

<p>QuantLib::SingleAssetOption &#8211; Black-Scholes-Merton option. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/legacy/pricers/singleassetoption.hpp&gt; </p>
<p> Inherited by <code>DiscreteGeometricASO</code>. </p>
<h3>Public Member Functions</h3>
<p><code>SingleAssetOption</code> (Option::Type type, Real underlying, Real strike, <code>Spread</code> dividendYield, <code>Rate</code> riskFreeRate, <code>Time</code> residualTime, <code>Volatility</code> volatility) </p>
<p> virtual void <code>setVolatility</code> (<code>Volatility</code> newVolatility) </p>
<p> virtual void <code>setRiskFreeRate</code> (<code>Rate</code> newRate) </p>
<p> virtual void <code>setDividendYield</code> (<code>Rate</code> newDividendYield) </p>
<p> virtual Real <code>value</code> () const =0 </p>
<p> virtual Real <code>delta</code> () const =0 </p>
<p> virtual Real <code>gamma</code> () const =0 </p>
<p> virtual Real <code>theta</code> () const </p>
<p> virtual Real <code>vega</code> () const </p>
<p> virtual Real <code>rho</code> () const </p>
<p> virtual Real <code>dividendRho</code> () const </p>
<p> <code>Volatility</code> <code>impliedVolatility</code> (Real targetValue, Real accuracy=1e-4, Size maxEvaluations=100, Volatility minVol=1.0e-7, Volatility maxVol=4.0) const </p>
<p> <code>Spread</code> <code>impliedDivYield</code> (Real targetValue, Real accuracy=1e-4, Size maxEvaluations=100, Spread minYield=1.0e-7, Spread maxYield=4.0) const </p>
<p> virtual boost::shared_ptr&lt; <code>SingleAssetOption</code> &gt; <code>clone</code> () const =0 </p>
<h3>Protected Attributes</h3>
<p>Real <code>underlying_</code> </p>
<p> <code>PlainVanillaPayoff</code> <code>payoff_</code> </p>
<p> <code>Spread</code> <code>dividendYield_</code> </p>
<p> <code>Rate</code> <code>riskFreeRate_</code> </p>
<p> <code>Time</code> <code>residualTime_</code> </p>
<p> <code>Volatility</code> <code>volatility_</code> </p>
<p> bool <code>hasBeenCalculated_</code> </p>
<p> Real <code>rho_</code> </p>
<p> Real <code>dividendRho_</code> </p>
<p> Real <code>vega_</code> </p>
<p> Real <code>theta_</code> </p>
<p> bool <code>rhoComputed_</code> </p>
<p> bool <code>dividendRhoComputed_</code> </p>
<p> bool <code>vegaComputed_</code> </p>
<p> bool <code>thetaComputed_</code> </p>
<h3>Static Protected Attributes</h3>
<p>static const Real <code>dVolMultiplier_</code> </p>
<p> static const Real <code>dRMultiplier_</code> </p>
<h3>Friends</h3>
<p>class <code>VolatilityFunction</code> </p>
<p> class <code>DivYieldFunction</code> </p>
<h2>Detailed Description</h2>
<p>Black-Scholes-Merton option.</p>
<h2>Member Function Documentation</h2>
<h3><code>Volatility</code> impliedVolatility (Real targetValue, Real accuracy = 1e-4, Size maxEvaluations = 100, <code>Volatility</code> minVol = 1.0e-7, <code>Volatility</code> maxVol = 4.0) const</h3>
<p><code>Warning</code></p>
<dl COMPACT>
<dd>Options with a gamma that changes sign have values that are <code>not</code> monotonic in the volatility, e.g binary options. In these cases impliedVolatility can fail and in any case is meaningless. Another possible source of failure is to have a targetValue that is not attainable with any volatility, e.g. a targetValue lower than the intrinsic value in the case of American options.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
