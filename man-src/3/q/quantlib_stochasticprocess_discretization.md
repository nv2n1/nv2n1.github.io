---
title: "quantlib_stochasticprocess_discretization(3)"
name: "quantlib_stochasticprocess_discretization"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_stochasticprocess_discretization/"
description: "QuantLib::StochasticProcess::discretization – discretization of a stochastic process over a given time interval"
---

<p>QuantLib::StochasticProcess::discretization &#8211; <code>discretization</code> of a stochastic process over a given time interval </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/stochasticprocess.hpp&gt; </p>
<p> Inherited by <code>EndEulerDiscretization</code>, and <code>EulerDiscretization</code>. </p>
<h3>Public Member Functions</h3>
<p>virtual <code>Disposable</code>&lt; <code>Array</code> &gt; <code>drift</code> (const <code>StochasticProcess</code> &amp;, Time t0, const <code>Array</code> &amp;x0, Time dt) const =0 </p>
<p> virtual <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>diffusion</code> (const <code>StochasticProcess</code> &amp;, Time t0, const <code>Array</code> &amp;x0, Time dt) const =0 </p>
<p> virtual <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>covariance</code> (const <code>StochasticProcess</code> &amp;, Time t0, const <code>Array</code> &amp;x0, Time dt) const =0 </p>
<h2>Detailed Description</h2>
<p><code>discretization</code> of a stochastic process over a given time interval </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
