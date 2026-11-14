---
title: "quantlib_batesprocess(3)"
name: "quantlib_batesprocess"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_batesprocess/"
description: "QuantLib::BatesProcess – Square-root stochastic-volatility Bates process."
---

<p>QuantLib::BatesProcess &#8211; Square-root stochastic-volatility Bates process. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/processes/batesprocess.hpp&gt; </p>
<p> Inherits <code>QuantLib::HestonProcess</code>. </p>
<h3>Public Member Functions</h3>
<p><code>BatesProcess</code> (const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;riskFreeRate, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;dividendYield, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;s0, <code>Real</code> v0, <code>Real</code> kappa, <code>Real</code> theta, <code>Real</code> sigma, <code>Real</code> rho, <code>Real</code> lambda, <code>Real</code> nu, <code>Real</code> delta, HestonProcess::Discretization d=HestonProcess::FullTruncation) </p>
<p> Size <code>factors</code> () const<br />
 <i>returns the number of independent factors of the process </i><br />
 <code>Disposable</code>&lt; <code>Array</code> &gt; <code>drift</code> (Time t, const <code>Array</code> &amp;x) const<br />
 <i>returns the drift part of the equation, i.e., $ mu(t, mathrm{x}_t) $ </i><br />
 <code>Disposable</code>&lt; <code>Array</code> &gt; <code>evolve</code> (Time t0, const <code>Array</code> &amp;x0, Time dt, const <code>Array</code> &amp;dw) const </p>
<p> <code>Real</code> <code>lambda</code> () const </p>
<p> <code>Real</code> <code>nu</code> () const </p>
<p> <code>Real</code> <code>delta</code> () const </p>
<h2>Detailed Description</h2>
<p>Square-root stochastic-volatility Bates process. </p>
<p> This class describes the square root stochastic volatility process incl jumps governed by [ ^J &#8211; 1) S dN \ dv(t, S) &amp;=&amp; ppa ( heta &#8211; v) dt + igma qrt{v} dW_2 \ dW_1 dW_2 &amp;=&amp; ho dt \ ber Function Documentation&quot; </p>
<h3><code>Disposable</code>&lt;<code>Array</code>&gt; evolve (Time t0, const <code>Array</code> &amp; x0, Time dt, const <code>Array</code> &amp; dw) const [virtual]</h3>
<p>returns the asset value after a time interval $ Delta t $ according to the given discretization. By default, it returns [ E(mathrm{x}_0,t_0,Delta t) + S(mathrm{x}_0,t_0,Delta t) dot Delta mathrm{w} ] where $ E $ is the expectation and $ S $ the standard deviation. </p>
<p> Reimplemented from <code>HestonProcess</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
