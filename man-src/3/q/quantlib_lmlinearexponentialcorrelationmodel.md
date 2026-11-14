---
title: "quantlib_lmlinearexponentialcorrelationmodel(3)"
name: "quantlib_lmlinearexponentialcorrelationmodel"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_lmlinearexponentialcorrelationmodel/"
description: "QuantLib::LmLinearExponentialCorrelationModel – linear exponential correlation model"
---

<p>QuantLib::LmLinearExponentialCorrelationModel &#8211; linear exponential correlation model </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/legacy/libormarketmodels/lmlinexpcorrmodel.hpp&gt; </p>
<p> Inherits <code>QuantLib::LmCorrelationModel</code>. </p>
<h3>Public Member Functions</h3>
<p><code>LmLinearExponentialCorrelationModel</code> (Size size, <code>Real</code> rho, <code>Real</code> beta, Size factors=<code>Null</code>&lt; Size &gt;()) </p>
<p> <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>correlation</code> (Time t, const <code>Array</code> &amp;x=<code>Null</code>&lt; <code>Array</code> &gt;()) const </p>
<p> <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>pseudoSqrt</code> (Time t, const <code>Array</code> &amp;x=<code>Null</code>&lt; <code>Array</code> &gt;()) const </p>
<p> <code>Real</code> <code>correlation</code> (Size i, Size j, Time t, const <code>Array</code> &amp;x) const </p>
<p> Size <code>factors</code> () const </p>
<p> bool <code>isTimeIndependent</code> () const </p>
<h3>Protected Member Functions</h3>
<p>void <code>generateArguments</code> () </p>
<h2>Detailed Description</h2>
<p>linear exponential correlation model </p>
<p> This class describes a exponential correlation model </p>
<p> [ ho_{i,j}=rho + (1-rho)*e^{(-ferences: </p>
<p> Damiano Brigo, Fabio Mercurio, Massimo Morini, 2003, Different Covariance Parameterizations of <code>Libor</code> Market Model and Joint Caps/Swaptions Calibration, (&lt;<a rel="nofollow" href="http://www.business.uts.edu.au/qfrc/conferences/qmf2001/Brigo_D.pdf">http://www.business.uts.edu.au/qfrc/conferences/qmf2001/Brigo_D.pdf</a>&gt;) </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
