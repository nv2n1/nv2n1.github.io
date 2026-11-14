---
title: "statevariable(3)"
name: "statevariable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-statevariable/"
description: "QuantLib::GeneralizedBlackScholesProcess – Generalized Black-Scholes stochastic process."
---

<p>QuantLib::GeneralizedBlackScholesProcess &#8211; Generalized Black-Scholes stochastic process. </p>
<h2>Synopsis</h2>
<pre><code>const Handle&lt; Quote &gt; &amp; stateVariable () const



const Handle&lt; YieldTermStructure &gt; &amp; dividendYield () const



const Handle&lt; YieldTermStructure &gt; &amp; riskFreeRate () const



const Handle&lt; BlackVolTermStructure &gt; &amp; blackVolatility () const



const Handle&lt; LocalVolTermStructure &gt; &amp; localVolatility () const</code></pre>
<p> Inherits <code>QuantLib::StochasticProcess1D</code>. Inherited by <code>BlackProcess</code>, <code>BlackScholesMertonProcess</code>, <code>BlackScholesProcess</code>, <code>ExtendedBlackScholesMertonProcess</code>, and <code>GarmanKohlagenProcess</code>.</p>
<h3>Public Member Functions</h3>
<p>const Handle&lt; Quote &gt; &amp; stateVariable () const</p>
<p>const Handle&lt; YieldTermStructure &gt; &amp; dividendYield () const</p>
<p>const Handle&lt; YieldTermStructure &gt; &amp; riskFreeRate () const</p>
<p>const Handle&lt; BlackVolTermStructure &gt; &amp; blackVolatility () const</p>
<p>const Handle&lt; LocalVolTermStructure &gt; &amp; localVolatility () const <code>StochasticProcess1D interface</code> </p>
<p> Real <code>x0</code> () const<br />
 <i>returns the initial value of the state variable </i><br />
 Real <code>drift</code> (Time t, Real x) const </p>
<p> Real <code>diffusion</code> (Time t, Real x) const </p>
<p> Real <code>apply</code> (Real x0, Real dx) const<br />
 <code>Observer interface</code><br />
 const Handle&lt; Quote &gt; &amp; stateVariable () const</p>
<p>const Handle&lt; YieldTermStructure &gt; &amp; dividendYield () const</p>
<p>const Handle&lt; YieldTermStructure &gt; &amp; riskFreeRate () const</p>
<p>const Handle&lt; BlackVolTermStructure &gt; &amp; blackVolatility () const</p>
<p>const Handle&lt; LocalVolTermStructure &gt; &amp; localVolatility () const <code>Inspectors</code> </p>
<pre><code>const Handle&lt; Quote &gt; &amp; stateVariable () const



const Handle&lt; YieldTermStructure &gt; &amp; dividendYield () const



const Handle&lt; YieldTermStructure &gt; &amp; riskFreeRate () const



const Handle&lt; BlackVolTermStructure &gt; &amp; blackVolatility () const



const Handle&lt; LocalVolTermStructure &gt; &amp; localVolatility () const</code></pre>
<h2>Detailed Description</h2>
<p>Generalized Black-Scholes stochastic process. </p>
<p> This class describes the stochastic process governed by [ dS(t, S) = (r(t) &#8211; q(t) &#8211; ac{igma(t, S)^2}{2}) dt + igma dW_t. ]</p>
<h2>Member Function Documentation</h2>
<h3>Real drift (Time t, Real x) const [virtual]</h3>
<p><code>Possible enhancements</code></p>
<dl>
<dd>revise extrapolation</dl>
<p> Implements <code>StochasticProcess1D</code>. </p>
<p> Reimplemented in <code>ExtendedBlackScholesMertonProcess</code>.</p>
<h3>Real diffusion (Time t, Real x) const [virtual]</h3>
<p><code>Possible enhancements</code></p>
<dl>
<dd>revise extrapolation</dl>
<p> Implements <code>StochasticProcess1D</code>. </p>
<p> Reimplemented in <code>ExtendedBlackScholesMertonProcess</code>.</p>
<h3>Real apply (Real x0, Real dx) const [virtual]</h3>
<p>applies a change to the asset value. By default, it returns $ x + Delta x $. </p>
<p> Reimplemented from <code>StochasticProcess1D</code>.</p>
<h3>Time time (const <code>Date</code> &amp;) const [virtual]</h3>
<p>returns the time value corresponding to the given date in the reference system of the stochastic process. </p>
<p> <code>Note:</code></p>
<dl>
<dd>As a number of processes might not need this functionality, a default implementation is given which raises an exception.</dl>
<p> Reimplemented from <code>StochasticProcess</code>.</p>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Reimplemented from <code>StochasticProcess</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
