---
title: "size_(3)"
name: "size_"
section: "3"
letter: "s"
url: "/docs/linux/man/3-size_/"
description: "QuantLib::LfmCovarianceParameterization – Libor market model parameterization"
---

<p>QuantLib::LfmCovarianceParameterization &#8211; Libor market model parameterization </p>
<h2>Synopsis</h2>
<pre><code>LfmCovarianceParameterization (Size size, Size factors)



Size size () const



Size factors () const



virtual Disposable&lt; Matrix &gt; diffusion (Time t, const Array &amp;x=Null&lt; Array &gt;()) const =0



virtual Disposable&lt; Matrix &gt; covariance (Time t, const Array &amp;x=Null&lt; Array &gt;()) const



virtual Disposable&lt; Matrix &gt; integratedCovariance (Time t, const Array &amp;x=Null&lt; Array &gt;()) const



Protected Attributes
const Size size_



const Size factors_</code></pre>
<p> Inherited by <code>LfmCovarianceProxy</code>, and <code>LfmHullWhiteParameterization</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>LfmCovarianceParameterization (Size size, Size factors)



Size size () const



Size factors () const



virtual Disposable&lt; Matrix &gt; diffusion (Time t, const Array &amp;x=Null&lt; Array &gt;()) const =0



virtual Disposable&lt; Matrix &gt; covariance (Time t, const Array &amp;x=Null&lt; Array &gt;()) const



virtual Disposable&lt; Matrix &gt; integratedCovariance (Time t, const Array &amp;x=Null&lt; Array &gt;()) const



Protected Attributes
const Size size_



const Size factors_</code></pre>
<h2>Detailed Description</h2>
<p>Libor market model parameterization </p>
<p> Brigo, Damiano, Mercurio, Fabio, Morini, Massimo, 2003, Different Covariance Parameterizations of the <code>Libor</code> Market Model and Joint Caps/Swaptions Calibration (&lt;<a rel="nofollow" href="http://www.exoticderivatives.com/Files/Papers/brigomercuriomorini.pdf">http://www.exoticderivatives.com/Files/Papers/brigomercuriomorini.pdf</a>&gt;)</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
