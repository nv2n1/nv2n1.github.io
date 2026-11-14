---
title: "quantlib_stochasticprocessarray(3)"
name: "quantlib_stochasticprocessarray"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_stochasticprocessarray/"
description: "QuantLib::StochasticProcessArray – Array of correlated 1-D stochastic processes"
---

<p>QuantLib::StochasticProcessArray &#8211; Array of correlated 1-D stochastic processes </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/processes/stochasticprocessarray.hpp&gt; </p>
<p> Inherits <code>QuantLib::StochasticProcess</code>. </p>
<h3>Public Member Functions</h3>
<p><code>StochasticProcessArray</code> (const std::vector&lt; boost::shared_ptr&lt; <code>StochasticProcess1D</code> &gt; &gt; &amp;, const <code>Matrix</code> &amp;correlation) </p>
<p> Size <code>size</code> () const<br />
 <i>returns the number of dimensions of the stochastic process </i><br />
 <code>Disposable</code>&lt; <code>Array</code> &gt; <code>initialValues</code> () const<br />
 <i>returns the initial values of the state variables </i><br />
 <code>Disposable</code>&lt; <code>Array</code> &gt; <code>drift</code> (Time t, const <code>Array</code> &amp;x) const<br />
 <i>returns the drift part of the equation, i.e., $ mu(t, mathrm{x}_t) $ </i><br />
 <code>Disposable</code>&lt; <code>Array</code> &gt; <code>expectation</code> (Time t0, const <code>Array</code> &amp;x0, Time dt) const </p>
<p> <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>diffusion</code> (Time t, const <code>Array</code> &amp;x) const<br />
 <i>returns the diffusion part of the equation, i.e. $ igma(t, mathrm{x}_t) $ </i><br />
 <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>covariance</code> (Time t0, const <code>Array</code> &amp;x0, Time dt) const </p>
<p> <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>stdDeviation</code> (Time t0, const <code>Array</code> &amp;x0, Time dt) const </p>
<p> <code>Disposable</code>&lt; <code>Array</code> &gt; <code>apply</code> (const <code>Array</code> &amp;x0, const <code>Array</code> &amp;dx) const </p>
<p> <code>Disposable</code>&lt; <code>Array</code> &gt; <code>evolve</code> (Time t0, const <code>Array</code> &amp;x0, Time dt, const <code>Array</code> &amp;dw) const </p>
<p> Time <code>time</code> (const <code>Date</code> &amp;) const </p>
<p> const boost::shared_ptr&lt; <code>StochasticProcess1D</code> &gt; &amp; <code>process</code> (Size i) const </p>
<p> <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>correlation</code> () const </p>
<h3>Protected Attributes</h3>
<p>std::vector&lt; boost::shared_ptr&lt; <code>StochasticProcess1D</code> &gt; &gt; <code>processes_</code> </p>
<p> <code>Matrix</code> <code>sqrtCorrelation_</code> </p>
<h2>Detailed Description</h2>
<p>Array of correlated 1-D stochastic processes </p>
<h2>Member Function Documentation</h2>
<h3><code>Disposable</code>&lt;<code>Array</code>&gt; expectation (Time t0, const <code>Array</code> &amp; x0, Time dt) const [virtual]</h3>
<p>returns the expectation $ E(mathrm{x}_{t_0 + Delta t} | mathrm{x}_{t_0} = mathrm{x}_0) $ of the process after a time interval $ Delta t $ according to the given discretization. This method can be overridden in derived classes which want to hard-code a particular discretization. </p>
<p> Reimplemented from <code>StochasticProcess</code>.</p>
<h3><code>Disposable</code>&lt;<code>Matrix</code>&gt; covariance (Time t0, const <code>Array</code> &amp; x0, Time dt) const [virtual]</h3>
<p>returns the covariance $ V(mathrm{x}_{t_0 + Delta t} | mathrm{x}_{t_0} = mathrm{x}_0) $ of the process after a time interval $ Delta t $ according to the given discretization. This method can be overridden in derived classes which want to hard-code a particular discretization. </p>
<p> Reimplemented from <code>StochasticProcess</code>.</p>
<h3><code>Disposable</code>&lt;<code>Matrix</code>&gt; stdDeviation (Time t0, const <code>Array</code> &amp; x0, Time dt) const [virtual]</h3>
<p>returns the standard deviation $ S(mathrm{x}_{t_0 + Delta t} | mathrm{x}_{t_0} = mathrm{x}_0) $ of the process after a time interval $ Delta t $ according to the given discretization. This method can be overridden in derived classes which want to hard-code a particular discretization. </p>
<p> Reimplemented from <code>StochasticProcess</code>.</p>
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
