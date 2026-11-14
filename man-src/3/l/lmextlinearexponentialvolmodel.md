---
title: "lmextlinearexponentialvolmodel(3)"
name: "lmextlinearexponentialvolmodel"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lmextlinearexponentialvolmodel/"
description: "QuantLib::LmExtLinearExponentialVolModel – extended linear exponential volatility model"
---

<p>QuantLib::LmExtLinearExponentialVolModel &#8211; extended linear exponential volatility model </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/legacy/libormarketmodels/lmextlinexpvolmodel.hpp&gt; </p>
<p> Inherits <code>QuantLib::LmLinearExponentialVolatilityModel</code>. </p>
<h3>Public Member Functions</h3>
<p><code>LmExtLinearExponentialVolModel</code> (const std::vector&lt; Time &gt; &amp;fixingTimes, <code>Real</code> a, <code>Real</code> b, <code>Real</code> c, <code>Real</code> d) </p>
<p> <code>Disposable</code>&lt; <code>Array</code> &gt; <code>volatility</code> (Time t, const <code>Array</code> &amp;x=<code>Null</code>&lt; <code>Array</code> &gt;()) const </p>
<p> <code>Volatility</code> <code>volatility</code> (Size i, Time t, const <code>Array</code> &amp;x=<code>Null</code>&lt; <code>Array</code> &gt;()) const </p>
<p> <code>Real</code> <code>integratedVariance</code> (Size i, Size j, Time u, const <code>Array</code> &amp;x=<code>Null</code>&lt; <code>Array</code> &gt;()) const </p>
<h2>Detailed Description</h2>
<p>extended linear exponential volatility model </p>
<p> This class describes an extended linear-exponential volatility model </p>
<p> [ igma_i(t)=k_i*((a*(T_{i}-t)+d)*e^{-b(T_{i}-t)}+c) ].PP References: </p>
<p> Damiano Brigo, Fabio Mercurio, Massimo Morini, 2003, Different Covariance Parameterizations of <code>Libor</code> Market Model and Joint Caps/Swaptions Calibration, (&lt;<a rel="nofollow" href="http://www.business.uts.edu.au/qfrc/conferences/qmf2001/Brigo_D.pdf">http://www.business.uts.edu.au/qfrc/conferences/qmf2001/Brigo_D.pdf</a>&gt;) </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
