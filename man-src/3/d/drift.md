---
title: "drift(3)"
name: "drift"
section: "3"
letter: "d"
url: "/docs/linux/man/3-drift/"
description: "QuantLib::ExtendedBlackScholesMertonProcess – experimental Black-Scholes-Merton stochastic process"
---

<h2 class="name">NAME</h2>
<p> QuantLib::ExtendedBlackScholesMertonProcess &#8211; experimental Black-Scholes-Merton stochastic process </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/experimental/processes/extendedblackscholesprocess.hpp&gt; </p>
<p> Inherits <code>QuantLib::GeneralizedBlackScholesProcess</code>. </p>
<h3>Public Types</h3>
<p> enum <code>Discretization</code> { <code>Euler</code>, <code>Milstein</code>, <code>PredictorCorrector</code> } </p>
<h3>Public Member Functions</h3>
<p> <code>ExtendedBlackScholesMertonProcess</code> (const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;x0, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;dividendTS, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;riskFreeTS, const <code>Handle</code>&lt; <code>BlackVolTermStructure</code> &gt; &amp;blackVolTS, const boost::shared_ptr&lt; <code>discretization</code> &gt; &amp;d=boost::shared_ptr&lt; <code>discretization</code> &gt;(new <code>EulerDiscretization</code>), Discretization evolDisc=Milstein) </p>
<p> Real <code>drift</code> (Time t, Real x) const </p>
<p> Real <code>diffusion</code> (Time t, Real x) const </p>
<p> Real <code>evolve</code> (Time t0, Real x0, Time dt, Real dw) const </p>
<h2>Detailed Description</h2>
<p> experimental Black-Scholes-Merton stochastic process </p>
<p> This class allows to choose a built-in discretization scheme</p>
<h2>Member Function Documentation</h2>
<h3>Real drift (Time t, Real x) const [virtual]</h3>
<p> <code>Possible enhancements</code></p>
<dl>
<dt>
<dd> revise extrapolation</dl>
<p> Reimplemented from <code>GeneralizedBlackScholesProcess</code>.</p>
<h3>Real diffusion (Time t, Real x) const [virtual]</h3>
<p> <code>Possible enhancements</code></p>
<dl>
<dt>
<dd> revise extrapolation</dl>
<p> Reimplemented from <code>GeneralizedBlackScholesProcess</code>.</p>
<h3>Real evolve (Time t0, Real x0, Time dt, Real dw) const [virtual]</h3>
<p> returns the asset value after a time interval $ Delta t $ according to the given discretization. By default, it returns [ E(x_0,t_0,Delta t) + S(x_0,t_0,Delta t) dot Delta w ] where $ E $ is the expectation and $ S $ the standard deviation. </p>
<p> Reimplemented from <code>StochasticProcess1D</code>. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
