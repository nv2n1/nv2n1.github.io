---
title: "gjrgarchprocess(3)"
name: "gjrgarchprocess"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gjrgarchprocess/"
description: "QuantLib::GJRGARCHProcess – Stochastic-volatility GJR-GARCH(1,1) process."
---

<p>QuantLib::GJRGARCHProcess &#8211; Stochastic-volatility GJR-GARCH(1,1) process. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/processes/gjrgarchprocess.hpp&gt; </p>
<p> Inherits <code>QuantLib::StochasticProcess</code>. </p>
<h3>Public Types</h3>
<p>enum <code>Discretization</code> { <code>PartialTruncation</code>, <code>FullTruncation</code>, <code>Reflection</code> } </p>
<h3>Public Member Functions</h3>
<p><code>GJRGARCHProcess</code> (const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;riskFreeRate, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;dividendYield, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;s0, <code>Real</code> v0, <code>Real</code> omega, <code>Real</code> alpha, <code>Real</code> beta, <code>Real</code> gamma, <code>Real</code> lambda, <code>Real</code> daysPerYear=252.0, Discretization d=FullTruncation) </p>
<p> Size <code>size</code> () const<br />
 <i>returns the number of dimensions of the stochastic process </i><br />
 <code>Disposable</code>&lt; <code>Array</code> &gt; <code>initialValues</code> () const<br />
 <i>returns the initial values of the state variables </i><br />
 <code>Disposable</code>&lt; <code>Array</code> &gt; <code>drift</code> (Time t, const <code>Array</code> &amp;x) const<br />
 <i>returns the drift part of the equation, i.e., $ mu(t, mathrm{x}_t) $ </i><br />
 <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>diffusion</code> (Time t, const <code>Array</code> &amp;x) const<br />
 <i>returns the diffusion part of the equation, i.e. $ igma(t, mathrm{x}_t) $ </i><br />
 <code>Disposable</code>&lt; <code>Array</code> &gt; <code>apply</code> (const <code>Array</code> &amp;x0, const <code>Array</code> &amp;dx) const </p>
<p> <code>Disposable</code>&lt; <code>Array</code> &gt; <code>evolve</code> (Time t0, const <code>Array</code> &amp;x0, Time dt, const <code>Array</code> &amp;dw) const </p>
<p> <code>Real</code> <code>v0</code> () const </p>
<p> <code>Real</code> <code>lambda</code> () const </p>
<p> <code>Real</code> <code>omega</code> () const </p>
<p> <code>Real</code> <code>alpha</code> () const </p>
<p> <code>Real</code> <code>beta</code> () const </p>
<p> <code>Real</code> <code>gamma</code> () const </p>
<p> <code>Real</code> <code>daysPerYear</code> () const </p>
<p> const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp; <code>s0</code> () const </p>
<p> const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp; <code>dividendYield</code> () const </p>
<p> const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp; <code>riskFreeRate</code> () const </p>
<p> Time <code>time</code> (const <code>Date</code> &amp;) const </p>
<h2>Detailed Description</h2>
<p>Stochastic-volatility GJR-GARCH(1,1) process. </p>
<p> This class describes the stochastic volatility process governed by [ r Function Documentation&quot; </p>
<h3><code>Disposable</code>&lt;<code>Array</code>&gt; apply (const <code>Array</code> &amp; x0, const <code>Array</code> &amp; dx) const [virtual]</h3>
<p>applies a change to the asset value. By default, it returns $ mathrm{x} + Delta mathrm{x} $. </p>
<p> Reimplemented from <code>StochasticProcess</code>.</p>
<h3><code>Disposable</code>&lt;<code>Array</code>&gt; evolve (Time t0, const <code>Array</code> &amp; x0, Time dt, const <code>Array</code> &amp; dw) const [virtual]</h3>
<p>returns the asset value after a time interval $ Delta t $ according to the given discretization. By default, it returns [ E(mathrm{x}_0,t_0,Delta t) + S(mathrm{x}_0,t_0,Delta t) dot Delta mathrm{w} ] where $ E $ is the expectation and $ S $ the standard deviation. </p>
<p> Reimplemented from <code>StochasticProcess</code>.</p>
<h3>Time time (const <code>Date</code> &amp;) const [virtual]</h3>
<p>returns the time value corresponding to the given date in the reference system of the stochastic process. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>As a number of processes might not need this functionality, a default implementation is given which raises an exception.</dl>
<p> Reimplemented from <code>StochasticProcess</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
