---
title: "quantlib_lfmcovarianceparameterization(3)"
name: "quantlib_lfmcovarianceparameterization"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_lfmcovarianceparameterization/"
description: "QuantLib::LfmCovarianceParameterization – Libor market model parameterization"
---

<p>QuantLib::LfmCovarianceParameterization &#8211; Libor market model parameterization </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/legacy/libormarketmodels/lfmcovarparam.hpp&gt; </p>
<p> Inherited by <code>LfmCovarianceProxy</code>, and <code>LfmHullWhiteParameterization</code>. </p>
<h3>Public Member Functions</h3>
<p><code>LfmCovarianceParameterization</code> (Size size, Size factors) </p>
<p> Size <code>size</code> () const </p>
<p> Size <code>factors</code> () const </p>
<p> virtual <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>diffusion</code> (Time t, const <code>Array</code> &amp;x=<code>Null</code>&lt; <code>Array</code> &gt;()) const =0 </p>
<p> virtual <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>covariance</code> (Time t, const <code>Array</code> &amp;x=<code>Null</code>&lt; <code>Array</code> &gt;()) const </p>
<p> virtual <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>integratedCovariance</code> (Time t, const <code>Array</code> &amp;x=<code>Null</code>&lt; <code>Array</code> &gt;()) const </p>
<h3>Protected Attributes</h3>
<p>const Size <code>size_</code> </p>
<p> const Size <code>factors_</code> </p>
<h2>Detailed Description</h2>
<p>Libor market model parameterization </p>
<p> Brigo, Damiano, Mercurio, Fabio, Morini, Massimo, 2003, Different Covariance Parameterizations of the <code>Libor</code> Market Model and Joint Caps/Swaptions Calibration (&lt;<a rel="nofollow" href="http://www.exoticderivatives.com/Files/Papers/brigomercuriomorini.pdf">http://www.exoticderivatives.com/Files/Papers/brigomercuriomorini.pdf</a>&gt;) </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
