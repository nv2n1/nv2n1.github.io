---
title: "lambda(3)"
name: "lambda"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lambda/"
description: "QuantLib::BatesModel – Bates stochastic-volatility model."
---

<h2 class="name">NAME</h2>
<p> QuantLib::BatesModel &#8211; Bates stochastic-volatility model. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/models/equity/batesmodel.hpp&gt; </p>
<p> Inherits <code>QuantLib::HestonModel</code>. </p>
<p> Inherited by BatesDetJumpModel. </p>
<h3>Public Member Functions</h3>
<p> <code>BatesModel</code> (const boost::shared_ptr&lt; <code>HestonProcess</code> &gt; &amp;process, <code>Real</code> lambda=0.1, <code>Real</code> nu=0.0, <code>Real</code> delta=0.1) </p>
<p> <code>Real</code> <code>nu</code> () const </p>
<p> <code>Real</code> <code>delta</code> () const </p>
<p> <code>Real</code> <code>lambda</code> () const </p>
<h2>Detailed Description</h2>
<p> Bates stochastic-volatility model. </p>
<p> extended versions of Heston model for the stochastic volatility of an asset including jumps. </p>
<p> References: A. Sepp, Pricing European-Style Options under Jump Diffusion Processes with Stochastic Volatility: Applications of Fourier Transform (&lt;<a rel="nofollow" href="http://math.ut.ee/~spartak/papers/stochjumpvols.pdf">http://math.ut.ee/~spartak/papers/stochjumpvols.pdf</a>&gt;) </p>
<p> <code>Tests</code></p>
<dl>
<dt>
<dd> calibration is tested against known values.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
