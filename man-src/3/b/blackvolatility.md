---
title: "blackvolatility(3)"
name: "blackvolatility"
section: "3"
letter: "b"
url: "/docs/linux/man/3-blackvolatility/"
description: "QuantLib::GeneralizedBlackScholesProcess – Generalized Black-Scholes stochastic process."
---

<p>QuantLib::GeneralizedBlackScholesProcess &#8211; Generalized Black-Scholes stochastic process. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/processes/blackscholesprocess.hpp&gt; </p>
<p> Inherits <code>QuantLib::StochasticProcess1D</code>. </p>
<p> Inherited by <code>BlackProcess</code>, <code>BlackScholesMertonProcess</code>, <code>BlackScholesProcess</code>, <code>ExtendedBlackScholesMertonProcess</code>, and <code>GarmanKohlagenProcess</code>. </p>
<h3>Public Member Functions</h3>
<p><code>GeneralizedBlackScholesProcess</code> (const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;x0, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;dividendTS, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;riskFreeTS, const <code>Handle</code>&lt; <code>BlackVolTermStructure</code> &gt; &amp;blackVolTS, const boost::shared_ptr&lt; <code>discretization</code> &gt; &amp;d=boost::shared_ptr&lt; <code>discretization</code> &gt;(new <code>EulerDiscretization</code>)) </p>
<p> Time <code>time</code> (const <code>Date</code> &amp;) const </p>
<p> <code>StochasticProcess1D interface</code> </p>
<p> Real <code>x0</code> () const<br />
 <i>returns the initial value of the state variable </i><br />
 Real <code>drift</code> (Time t, Real x) const </p>
<p> Real <code>diffusion</code> (Time t, Real x) const </p>
<p> Real <code>apply</code> (Real x0, Real dx) const </p>
<p> <code>Observer interface</code> </p>
<p> void <code>update</code> () </p>
<p> <code>Inspectors</code> </p>
<p> const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp; <code>stateVariable</code> () const </p>
<p> const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp; <code>dividendYield</code> () const </p>
<p> const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp; <code>riskFreeRate</code> () const </p>
<p> const <code>Handle</code>&lt; <code>BlackVolTermStructure</code> &gt; &amp; <code>blackVolatility</code> () const </p>
<p> const <code>Handle</code>&lt; <code>LocalVolTermStructure</code> &gt; &amp; <code>localVolatility</code> () const </p>
<h2>Detailed Description</h2>
<p>Generalized Black-Scholes stochastic process. </p>
<p> This class describes the stochastic process governed by [ dS(t, S) = (r(t) &#8211; q(t) &#8211; ac{igma(t, S)^2}{2}) dt + igma dW_t. ]</p>
<h2>Member Function Documentation</h2>
<h3>Real drift (Time t, Real x) const [virtual]</h3>
<p><code>Possible enhancements</code></p>
<dl COMPACT>
<dd>revise extrapolation</dl>
<p> Implements <code>StochasticProcess1D</code>. </p>
<p> Reimplemented in <code>ExtendedBlackScholesMertonProcess</code>.</p>
<h3>Real diffusion (Time t, Real x) const [virtual]</h3>
<p><code>Possible enhancements</code></p>
<dl COMPACT>
<dd>revise extrapolation</dl>
<p> Implements <code>StochasticProcess1D</code>. </p>
<p> Reimplemented in <code>ExtendedBlackScholesMertonProcess</code>.</p>
<h3>Real apply (Real x0, Real dx) const [virtual]</h3>
<p>applies a change to the asset value. By default, it returns $ x + Delta x $. </p>
<p> Reimplemented from <code>StochasticProcess1D</code>.</p>
<h3>Time time (const <code>Date</code> &amp;) const [virtual]</h3>
<p>returns the time value corresponding to the given date in the reference system of the stochastic process. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>As a number of processes might not need this functionality, a default implementation is given which raises an exception.</dl>
<p> Reimplemented from <code>StochasticProcess</code>.</p>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Reimplemented from <code>StochasticProcess</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
