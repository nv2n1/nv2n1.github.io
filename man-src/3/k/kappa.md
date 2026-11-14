---
title: "kappa(3)"
name: "kappa"
section: "3"
letter: "k"
url: "/docs/linux/man/3-kappa/"
description: "QuantLib::HestonModel – Heston model for the stochastic volatility of an asset."
---

<h2 class="name">NAME</h2>
<p> QuantLib::HestonModel &#8211; Heston model for the stochastic volatility of an asset. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/models/equity/hestonmodel.hpp&gt; </p>
<p> Inherits <code>QuantLib::CalibratedModel</code>. </p>
<p> Inherited by BatesDoubleExpModel, and <code>BatesModel</code>. </p>
<h3>Public Member Functions</h3>
<p> <code>HestonModel</code> (const boost::shared_ptr&lt; <code>HestonProcess</code> &gt; &amp;process) </p>
<p> <code>Real</code> <code>theta</code> () const </p>
<p> <code>Real</code> <code>kappa</code> () const </p>
<p> <code>Real</code> <code>sigma</code> () const </p>
<p> <code>Real</code> <code>rho</code> () const </p>
<p> <code>Real</code> <code>v0</code> () const </p>
<p> boost::shared_ptr&lt; <code>HestonProcess</code> &gt; <code>process</code> () const </p>
<h3>Protected Member Functions</h3>
<p> void <code>generateArguments</code> () </p>
<h3>Protected Attributes</h3>
<p> boost::shared_ptr&lt; <code>HestonProcess</code> &gt; <code>process_</code> </p>
<h2>Detailed Description</h2>
<p> Heston model for the stochastic volatility of an asset. </p>
<p> References: </p>
<p> Heston, Steven L., 1993. A Closed-Form Solution for Options with Stochastic Volatility with Applications to <code>Bond</code> and <code>Currency</code> Options. The review of Financial Studies, Volume 6, Issue 2, 327-343. </p>
<p> <code>Tests</code></p>
<dl>
<dt>
<dd> calibration is tested against known good values.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
