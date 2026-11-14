---
title: "jumpintensity(3)"
name: "jumpintensity"
section: "3"
letter: "j"
url: "/docs/linux/man/3-jumpintensity/"
description: "QuantLib::Merton76Process – Merton-76 jump-diffusion process."
---

<p>QuantLib::Merton76Process &#8211; Merton-76 jump-diffusion process. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/processes/merton76process.hpp&gt; </p>
<p> Inherits <code>QuantLib::StochasticProcess1D</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Merton76Process</code> (const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;stateVariable, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;dividendTS, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;riskFreeTS, const <code>Handle</code>&lt; <code>BlackVolTermStructure</code> &gt; &amp;blackVolTS, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;jumpInt, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;logJMean, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;logJVol, const boost::shared_ptr&lt; <code>discretization</code> &gt; &amp;d=boost::shared_ptr&lt; <code>discretization</code> &gt;(new <code>EulerDiscretization</code>)) </p>
<p> Time <code>time</code> (const <code>Date</code> &amp;) const </p>
<p> <code>StochasticProcess1D interface</code> </p>
<p> Real <code>x0</code> () const<br />
 <i>returns the initial value of the state variable </i><br />
 Real <code>drift</code> (Time, Real) const<br />
 <i>returns the drift part of the equation, i.e. $ mu(t, x_t) $ </i><br />
 Real <code>diffusion</code> (Time, Real) const<br />
 <i>returns the diffusion part of the equation, i.e. $ igma(t, x_t) $ </i><br />
 Real <code>apply</code> (Real, Real) const </p>
<p> <code>Inspectors</code> </p>
<p> const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp; <code>stateVariable</code> () const </p>
<p> const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp; <code>dividendYield</code> () const </p>
<p> const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp; <code>riskFreeRate</code> () const </p>
<p> const <code>Handle</code>&lt; <code>BlackVolTermStructure</code> &gt; &amp; <code>blackVolatility</code> () const </p>
<p> const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp; <code>jumpIntensity</code> () const </p>
<p> const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp; <code>logMeanJump</code> () const </p>
<p> const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp; <code>logJumpVolatility</code> () const </p>
<h2>Detailed Description</h2>
<p>Merton-76 jump-diffusion process. </p>
<h2>Member Function Documentation</h2>
<h3>Real apply (Real x0, Real dx) const [virtual]</h3>
<p>applies a change to the asset value. By default, it returns $ x + Delta x $. </p>
<p> Reimplemented from <code>StochasticProcess1D</code>.</p>
<h3>Time time (const <code>Date</code> &amp;) const [virtual]</h3>
<p>returns the time value corresponding to the given date in the reference system of the stochastic process. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>As a number of processes might not need this functionality, a default implementation is given which raises an exception.</dl>
<p> Reimplemented from <code>StochasticProcess</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
