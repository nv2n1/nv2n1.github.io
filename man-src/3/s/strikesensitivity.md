---
title: "strikesensitivity(3)"
name: "strikesensitivity"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strikesensitivity/"
description: "QuantLib::OneAssetOption – Base class for options on a single asset."
---

<p>QuantLib::OneAssetOption &#8211; Base class for options on a single asset. </p>
<h2>Synopsis</h2>
<pre><code>void setupExpired () const



Protected Attributes</code></pre>
<p> Inherits <code>QuantLib::Option</code>. Inherited by <code>BarrierOption</code>, <code>CliquetOption</code>, <code>ContinuousAveragingAsianOption</code>, <code>ContinuousFixedLookbackOption</code>, <code>ContinuousFloatingLookbackOption</code>, option, <code>DiscreteAveragingAsianOption</code>, <code>DividendVanillaOption</code>, <code>ForwardVanillaOption</code>, <code>QuantoVanillaOption</code>, and <code>VanillaOption</code>.</p>
<h3>Classes</h3>
<p>class <code>results</code><br />
 <i>Results from single-asset option calculation </i></p>
<h3>Public Member Functions</h3>
<p><code>OneAssetOption</code> (const boost::shared_ptr&lt; <code>Payoff</code> &gt; &amp;, const boost::shared_ptr&lt; <code>Exercise</code> &gt; &amp;) </p>
<p> void <code>fetchResults</code> (const PricingEngine::results *) const<br />
 <code>Instrument interface</code> </p>
<p> bool <code>isExpired</code> () const<br />
 <i>returns whether the instrument is still tradable. </i> <code>greeks</code> </p>
<p> <code>Real</code> <code>delta</code> () const </p>
<p> <code>Real</code> <code>deltaForward</code> () const </p>
<p> <code>Real</code> <code>elasticity</code> () const </p>
<p> <code>Real</code> <code>gamma</code> () const </p>
<p> <code>Real</code> <code>theta</code> () const </p>
<p> <code>Real</code> <code>thetaPerDay</code> () const </p>
<p> <code>Real</code> <code>vega</code> () const </p>
<p> <code>Real</code> <code>rho</code> () const </p>
<p> <code>Real</code> <code>dividendRho</code> () const </p>
<p> <code>Real</code> <code>strikeSensitivity</code> () const </p>
<p> <code>Real</code> <code>itmCashProbability</code> () const</p>
<h3>Protected Member Functions</h3>
<pre><code>void setupExpired () const



Protected Attributes</code></pre>
<p> <code>Real</code> <code>delta_</code> </p>
<p> <code>Real</code> <code>deltaForward_</code> </p>
<p> <code>Real</code> <code>elasticity_</code> </p>
<p> <code>Real</code> <code>gamma_</code> </p>
<p> <code>Real</code> <code>theta_</code> </p>
<p> <code>Real</code> <code>thetaPerDay_</code> </p>
<p> <code>Real</code> <code>vega_</code> </p>
<p> <code>Real</code> <code>rho_</code> </p>
<p> <code>Real</code> <code>dividendRho_</code> </p>
<p> <code>Real</code> <code>strikeSensitivity_</code> </p>
<p> <code>Real</code> <code>itmCashProbability_</code></p>
<h2>Detailed Description</h2>
<p>Base class for options on a single asset.</p>
<h2>Member Function Documentation</h2>
<h3>void fetchResults (const PricingEngine::results * r) const [virtual]</h3>
<p>When a derived result structure is defined for an instrument, this method should be overridden to read from it. This is mandatory in case a pricing engine is used. </p>
<p> Reimplemented from <code>Instrument</code>. </p>
<p> Reimplemented in <code>ForwardVanillaOption</code>, <code>QuantoBarrierOption</code>, <code>QuantoForwardVanillaOption</code>, and <code>QuantoVanillaOption</code>.</p>
<h3>void setupExpired () const [protected, virtual]</h3>
<p>This method must leave the instrument in a consistent state when the expiration condition is met. </p>
<p> Reimplemented from <code>Instrument</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
