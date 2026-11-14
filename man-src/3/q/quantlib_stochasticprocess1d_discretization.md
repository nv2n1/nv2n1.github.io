---
title: "quantlib_stochasticprocess1d_discretization(3)"
name: "quantlib_stochasticprocess1d_discretization"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_stochasticprocess1d_discretization/"
description: "QuantLib::StochasticProcess1D::discretization – discretization of a 1-D stochastic process"
---

<p>QuantLib::StochasticProcess1D::discretization &#8211; <code>discretization</code> of a 1-D stochastic process </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/stochasticprocess.hpp&gt; </p>
<p> Inherited by <code>EndEulerDiscretization</code>, and <code>EulerDiscretization</code>. </p>
<h3>Public Member Functions</h3>
<p>virtual Real <code>drift</code> (const <code>StochasticProcess1D</code> &amp;, Time t0, Real x0, Time dt) const =0 </p>
<p> virtual Real <code>diffusion</code> (const <code>StochasticProcess1D</code> &amp;, Time t0, Real x0, Time dt) const =0 </p>
<p> virtual Real <code>variance</code> (const <code>StochasticProcess1D</code> &amp;, Time t0, Real x0, Time dt) const =0 </p>
<h2>Detailed Description</h2>
<p><code>discretization</code> of a 1-D stochastic process </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
