---
title: "initialvalues(3)"
name: "initialvalues"
section: "3"
letter: "i"
url: "/docs/linux/man/3-initialvalues/"
description: "QuantLib::LiborForwardModelProcess – libor-forward-model process"
---

<p>QuantLib::LiborForwardModelProcess &#8211; libor-forward-model process </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/legacy/libormarketmodels/lfmprocess.hpp&gt; </p>
<p> Inherits <code>QuantLib::StochasticProcess</code>. </p>
<h3>Public Member Functions</h3>
<p><code>LiborForwardModelProcess</code> (Size size, const boost::shared_ptr&lt; <code>IborIndex</code> &gt; &amp;index) </p>
<p> <code>Disposable</code>&lt; <code>Array</code> &gt; <code>initialValues</code> () const<br />
 <i>returns the initial values of the state variables </i><br />
 <code>Disposable</code>&lt; <code>Array</code> &gt; <code>drift</code> (Time t, const <code>Array</code> &amp;x) const<br />
 <i>returns the drift part of the equation, i.e., $ mu(t, mathrm{x}_t) $ </i><br />
 <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>diffusion</code> (Time t, const <code>Array</code> &amp;x) const<br />
 <i>returns the diffusion part of the equation, i.e. $ igma(t, mathrm{x}_t) $ </i><br />
 <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>covariance</code> (Time t0, const <code>Array</code> &amp;x0, Time dt) const </p>
<p> <code>Disposable</code>&lt; <code>Array</code> &gt; <code>apply</code> (const <code>Array</code> &amp;x0, const <code>Array</code> &amp;dx) const </p>
<p> <code>Disposable</code>&lt; <code>Array</code> &gt; <code>evolve</code> (Time t0, const <code>Array</code> &amp;x0, Time dt, const <code>Array</code> &amp;dw) const </p>
<p> Size <code>size</code> () const<br />
 <i>returns the number of dimensions of the stochastic process </i><br />
 Size <code>factors</code> () const<br />
 <i>returns the number of independent factors of the process </i><br />
 boost::shared_ptr&lt; <code>IborIndex</code> &gt; <code>index</code> () const </p>
<p> Leg <code>cashFlows</code> (<code>Real</code> amount=1.0) const </p>
<p> void <code>setCovarParam</code> (const boost::shared_ptr&lt; <code>LfmCovarianceParameterization</code> &gt; &amp;param) </p>
<p> boost::shared_ptr&lt; <code>LfmCovarianceParameterization</code> &gt; <code>covarParam</code> () const </p>
<p> Size <code>nextIndexReset</code> (Time t) const </p>
<p> const std::vector&lt; Time &gt; &amp; <code>fixingTimes</code> () const </p>
<p> const std::vector&lt; <code>Date</code> &gt; &amp; <code>fixingDates</code> () const </p>
<p> const std::vector&lt; Time &gt; &amp; <code>accrualStartTimes</code> () const </p>
<p> const std::vector&lt; Time &gt; &amp; <code>accrualEndTimes</code> () const </p>
<p> std::vector&lt; <code>DiscountFactor</code> &gt; <code>discountBond</code> (const std::vector&lt; <code>Rate</code> &gt; &amp;rates) const </p>
<h2>Detailed Description</h2>
<p>libor-forward-model process </p>
<p> stochastic process of a libor forward model using the rolling forward measure incl. predictor-corrector step </p>
<p> References: </p>
<p> Glasserman, Paul, 2004, Monte Carlo Methods in Financial Engineering, Springer, Section 3.7 </p>
<p> Antoon Pelsser, 2000, Efficient Methods for Valuing Interest Rate Derivatives, Springer, 8 </p>
<p> Hull, John, White, Alan, 1999, <code>Forward</code> Rate Volatilities, <code>Swap</code> Rate Volatilities and the Implementation of the <code>Libor</code> Market Model (&lt;<a rel="nofollow" href="http://www.rotman.utoronto.ca/~amackay/fin/libormktmodel2.pdf">http://www.rotman.utoronto.ca/~amackay/fin/libormktmodel2.pdf</a>&gt;) </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness is tested by Monte-Carlo reproduction of caplet &amp; ratchet NPVs and comparison with Black pricing.</dl>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>this class does not work correctly with Visual C++ 6.</dl>
<h2>Member Function Documentation</h2>
<h3><code>Disposable</code>&lt;<code>Matrix</code>&gt; covariance (Time t0, const <code>Array</code> &amp; x0, Time dt) const [virtual]</h3>
<p>returns the covariance $ V(mathrm{x}_{t_0 + Delta t} | mathrm{x}_{t_0} = mathrm{x}_0) $ of the process after a time interval $ Delta t $ according to the given discretization. This method can be overridden in derived classes which want to hard-code a particular discretization. </p>
<p> Reimplemented from <code>StochasticProcess</code>.</p>
<h3><code>Disposable</code>&lt;<code>Array</code>&gt; apply (const <code>Array</code> &amp; x0, const <code>Array</code> &amp; dx) const [virtual]</h3>
<p>applies a change to the asset value. By default, it returns $ mathrm{x} + Delta mathrm{x} $. </p>
<p> Reimplemented from <code>StochasticProcess</code>.</p>
<h3><code>Disposable</code>&lt;<code>Array</code>&gt; evolve (Time t0, const <code>Array</code> &amp; x0, Time dt, const <code>Array</code> &amp; dw) const [virtual]</h3>
<p>returns the asset value after a time interval $ Delta t $ according to the given discretization. By default, it returns [ E(mathrm{x}_0,t_0,Delta t) + S(mathrm{x}_0,t_0,Delta t) dot Delta mathrm{w} ] where $ E $ is the expectation and $ S $ the standard deviation. </p>
<p> Reimplemented from <code>StochasticProcess</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
