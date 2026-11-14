---
title: "quantlib_lmlinearexponentialvolatilitymodel(3)"
name: "quantlib_lmlinearexponentialvolatilitymodel"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_lmlinearexponentialvolatilitymodel/"
description: "QuantLib::LmLinearExponentialVolatilityModel – linear exponential volatility model"
---

<p>QuantLib::LmLinearExponentialVolatilityModel &#8211; linear exponential volatility model </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/legacy/libormarketmodels/lmlinexpvolmodel.hpp&gt; </p>
<p> Inherits <code>QuantLib::LmVolatilityModel</code>. </p>
<p> Inherited by <code>LmExtLinearExponentialVolModel</code>. </p>
<h3>Public Member Functions</h3>
<p><code>LmLinearExponentialVolatilityModel</code> (const std::vector&lt; Time &gt; &amp;fixingTimes, <code>Real</code> a, <code>Real</code> b, <code>Real</code> c, <code>Real</code> d) </p>
<p> <code>Disposable</code>&lt; <code>Array</code> &gt; <code>volatility</code> (Time t, const <code>Array</code> &amp;x=<code>Null</code>&lt; <code>Array</code> &gt;()) const </p>
<p> <code>Volatility</code> <code>volatility</code> (Size i, Time t, const <code>Array</code> &amp;x=<code>Null</code>&lt; <code>Array</code> &gt;()) const </p>
<p> <code>Real</code> <code>integratedVariance</code> (Size i, Size j, Time u, const <code>Array</code> &amp;x=<code>Null</code>&lt; <code>Array</code> &gt;()) const </p>
<h2>Detailed Description</h2>
<p>linear exponential volatility model </p>
<p> This class describes a linear-exponential volatility model </p>
<p> [ igma_i(t)=(a*(T_{i}-t)+d)*e^{-b(T_{i}-t)}+c ].PP References: </p>
<p> Damiano Brigo, Fabio Mercurio, Massimo Morini, 2003, Different Covariance Parameterizations of <code>Libor</code> Market Model and Joint Caps/Swaptions Calibration, (&lt;<a rel="nofollow" href="http://www.business.uts.edu.au/qfrc/conferences/qmf2001/Brigo_D.pdf">http://www.business.uts.edu.au/qfrc/conferences/qmf2001/Brigo_D.pdf</a>&gt;) </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
