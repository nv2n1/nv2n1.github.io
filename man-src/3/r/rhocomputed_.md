---

title: "rhocomputed_(3)"
name: "rhocomputed_"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rhocomputed_/"
description: "QuantLib::SingleAssetOption – Black-Scholes-Merton option."
---

<p>QuantLib::SingleAssetOption &#8211; Black-Scholes-Merton option. </p>

<p> <br/>
 </p>
<p>#include &lt;ql/legacy/pricers/singleassetoption.hpp&gt; </p>
<p>Inherited by <code>DiscreteGeometricASO</code>. </p>
<h3>Public Member Functions</h3>
<p> <br/>
 <code>SingleAssetOption</code> (Option::Type type, Real underlying, Real strike, <code>Spread</code> dividendYield, <code>Rate</code> riskFreeRate, <code>Time</code> residualTime, <code>Volatility</code> volatility) <br/>
 <br/>
 virtual void <code>setVolatility</code> (<code>Volatility</code> newVolatility) <br/>
 <br/>
 virtual void <code>setRiskFreeRate</code> (<code>Rate</code> newRate) <br/>
 <br/>
 virtual void <code>setDividendYield</code> (<code>Rate</code> newDividendYield) <br/>
 <br/>
 virtual Real <code>value</code> () const =0 <br/>
 <br/>
 virtual Real <code>delta</code> () const =0 <br/>
 <br/>
 virtual Real <code>gamma</code> () const =0 <br/>
 <br/>
 virtual Real <code>theta</code> () const <br/>
 <br/>
 virtual Real <code>vega</code> () const <br/>
 <br/>
 virtual Real <code>rho</code> () const <br/>
 <br/>
 virtual Real <code>dividendRho</code> () const <br/>
 <br/>
 <code>Volatility</code> <code>impliedVolatility</code> (Real targetValue, Real accuracy=1e-4, Size maxEvaluations=100, Volatility minVol=1.0e-7, Volatility maxVol=4.0) const <br/>
 <br/>
 <code>Spread</code> <code>impliedDivYield</code> (Real targetValue, Real accuracy=1e-4, Size maxEvaluations=100, Spread minYield=1.0e-7, Spread maxYield=4.0) const <br/>
 <br/>
 virtual boost::shared_ptr&lt; <code>SingleAssetOption</code> &gt; <code>clone</code> () const =0 <br/>
  </p>
<h3>Protected Attributes</h3>
<p> <br/>
 Real <code>underlying_</code> <br/>
 <br/>
 <code>PlainVanillaPayoff</code> <code>payoff_</code> <br/>
 <br/>
 <code>Spread</code> <code>dividendYield_</code> <br/>
 <br/>
 <code>Rate</code> <code>riskFreeRate_</code> <br/>
 <br/>
 <code>Time</code> <code>residualTime_</code> <br/>
 <br/>
 <code>Volatility</code> <code>volatility_</code> <br/>
 <br/>
 bool <code>hasBeenCalculated_</code> <br/>
 <br/>
 Real <code>rho_</code> <br/>
 <br/>
 Real <code>dividendRho_</code> <br/>
 <br/>
 Real <code>vega_</code> <br/>
 <br/>
 Real <code>theta_</code> <br/>
 <br/>
 bool <code>rhoComputed_</code> <br/>
 <br/>
 bool <code>dividendRhoComputed_</code> <br/>
 <br/>
 bool <code>vegaComputed_</code> <br/>
 <br/>
 bool <code>thetaComputed_</code> <br/>
  </p>
<h3>Static Protected Attributes</h3>
<p> <br/>
 static const Real <code>dVolMultiplier_</code> <br/>
 <br/>
 static const Real <code>dRMultiplier_</code> <br/>
  </p>
<h3>Friends</h3>
<p> <br/>
 class <code>VolatilityFunction</code> <br/>
 <br/>
 class <code>DivYieldFunction</code> <br/>
  </p>
<h2>Detailed Description</h2>
<p>Black-Scholes-Merton option.  </p>
<h2>Member Function Documentation</h2>
<code></code><code></code><code></code><h3>Volatility impliedVolatility (Real targetValue, Real accuracy = 1e-4, Size maxEvaluations = 100, Volatility minVol = 1.0e-7, Volatility maxVol = 4.0) const</h3>
<p> <code>Warning</code> </p>
<dl>
<dd> <p> Options with a gamma that changes sign have values that are <code>not</code> monotonic in the volatility, e.g binary options. In these cases impliedVolatility can fail and in any case is meaningless. Another possible source of failure is to have a targetValue that is not attainable with any volatility, e.g. a targetValue lower than the intrinsic value in the case of American options. </p>
 </dd></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code. </p>
