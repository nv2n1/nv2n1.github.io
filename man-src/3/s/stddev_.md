---
title: "stddev_(3)"
name: "stddev_"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stddev_/"
description: "QuantLib::BlackCalculator – Black 1976 calculator class."
---

<p>QuantLib::BlackCalculator &#8211; Black 1976 calculator class. </p>
<h2>Synopsis</h2>
<pre><code>BlackCalculator (const boost::shared_ptr&lt; StrikedTypePayoff &gt; &amp;payoff, Real forward, Real stdDev, Real discount=1.0)



Real value () const



Real deltaForward () const



virtual Real delta (Real spot) const



Real elasticityForward () const



virtual Real elasticity (Real spot) const



Real gammaForward () const



virtual Real gamma (Real spot) const



virtual Real theta (Real spot, Time maturity) const



virtual Real thetaPerDay (Real spot, Time maturity) const



Real vega (Time maturity) const



Real rho (Time maturity) const



Real dividendRho (Time maturity) const



Real itmCashProbability () const



Real itmAssetProbability () const



Real strikeSensitivity () const



Real alpha () const



Real beta () const



Protected Attributes</code></pre>
<p> Inherited by <code>BlackScholesCalculator</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>BlackCalculator (const boost::shared_ptr&lt; StrikedTypePayoff &gt; &amp;payoff, Real forward, Real stdDev, Real discount=1.0)



Real value () const



Real deltaForward () const



virtual Real delta (Real spot) const



Real elasticityForward () const



virtual Real elasticity (Real spot) const



Real gammaForward () const



virtual Real gamma (Real spot) const



virtual Real theta (Real spot, Time maturity) const



virtual Real thetaPerDay (Real spot, Time maturity) const



Real vega (Time maturity) const



Real rho (Time maturity) const



Real dividendRho (Time maturity) const



Real itmCashProbability () const



Real itmAssetProbability () const



Real strikeSensitivity () const



Real alpha () const



Real beta () const



Protected Attributes</code></pre>
<p> <code>Real</code> <code>strike_</code> </p>
<p> <code>Real</code> <code>forward_</code> </p>
<p> <code>Real</code> <code>stdDev_</code> </p>
<p> <code>Real</code> <code>discount_</code> </p>
<p> <code>Real</code> <code>variance_</code> </p>
<p> <code>Real</code> <code>D1_</code> </p>
<p> <code>Real</code> <code>D2_</code> </p>
<p> <code>Real</code> <code>alpha_</code> </p>
<p> <code>Real</code> <code>beta_</code> </p>
<p> <code>Real</code> <code>DalphaDd1_</code> </p>
<p> <code>Real</code> <code>DbetaDd2_</code> </p>
<p> <code>Real</code> <code>n_d1_</code> </p>
<p> <code>Real</code> <code>cum_d1_</code> </p>
<p> <code>Real</code> <code>n_d2_</code> </p>
<p> <code>Real</code> <code>cum_d2_</code> </p>
<p> <code>Real</code> <code>X_</code> </p>
<p> <code>Real</code> <code>DXDs_</code> </p>
<p> <code>Real</code> <code>DXDstrike_</code></p>
<h3>Friends</h3>
<p>class <code>Calculator</code></p>
<h2>Detailed Description</h2>
<p>Black 1976 calculator class. </p>
<p> <code>Bug</code></p>
<dl>
<dd>When the variance is null, division by zero occur during the calculation of delta, delta forward, gamma, gamma forward, rho, dividend rho, vega, and strike sensitivity.</dl>
<p> <code>Examples: </code> </p>
<p> <code>DiscreteHedging.cpp</code>.</p>
<h2>Member Function Documentation</h2>
<h3><code>Real</code> deltaForward () const</h3>
<p>Sensitivity to change in the underlying forward price.</p>
<h3>virtual <code>Real</code> delta (<code>Real</code> spot) const [virtual]</h3>
<p>Sensitivity to change in the underlying spot price.</p>
<h3><code>Real</code> elasticityForward () const</h3>
<p>Sensitivity in percent to a percent change in the underlying forward price.</p>
<h3>virtual <code>Real</code> elasticity (<code>Real</code> spot) const [virtual]</h3>
<p>Sensitivity in percent to a percent change in the underlying spot price.</p>
<h3><code>Real</code> gammaForward () const</h3>
<p>Second order derivative with respect to change in the underlying forward price.</p>
<h3>virtual <code>Real</code> gamma (<code>Real</code> spot) const [virtual]</h3>
<p>Second order derivative with respect to change in the underlying spot price.</p>
<h3>virtual <code>Real</code> theta (<code>Real</code> spot, <code>Time</code> maturity) const [virtual]</h3>
<p>Sensitivity to time to maturity.</p>
<h3>virtual <code>Real</code> thetaPerDay (<code>Real</code> spot, <code>Time</code> maturity) const [virtual]</h3>
<p>Sensitivity to time to maturity per day, assuming 365 day per year.</p>
<h3><code>Real</code> vega (<code>Time</code> maturity) const</h3>
<p>Sensitivity to volatility.</p>
<h3><code>Real</code> rho (<code>Time</code> maturity) const</h3>
<p>Sensitivity to discounting rate.</p>
<h3><code>Real</code> dividendRho (<code>Time</code> maturity) const</h3>
<p>Sensitivity to dividend/growth rate.</p>
<h3><code>Real</code> itmCashProbability () const</h3>
<p>Probability of being in the money in the bond martingale measure, i.e. N(d2). It is a risk-neutral probability, not the real world one.</p>
<h3><code>Real</code> itmAssetProbability () const</h3>
<p>Probability of being in the money in the asset martingale measure, i.e. N(d1). It is a risk-neutral probability, not the real world one.</p>
<h3><code>Real</code> strikeSensitivity () const</h3>
<p>Sensitivity to strike.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
