---
title: "sc_onebodyderivintcca(3)"
name: "sc_onebodyderivintcca"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_onebodyderivintcca/"
description: "sc::OneBodyDerivIntCCA –"
---

<p>sc::OneBodyDerivIntCCA &#8211; </p>
<p> This implements one body derivative integrals.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;obintcca.h&gt;</code></pre>
<p> Inherits <code>sc::OneBodyDerivInt</code>.</p>
<h3>Public Member Functions</h3>
<p><code>OneBodyDerivIntCCA</code> (<code>Integral</code> *, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;, IntegralEvaluatorFactory, bool, string) </p>
<p> void <code>compute_shell</code> (int, int, <code>DerivCenters</code> &amp;)<br />
 <i></i><code>Compute</code> the derivative integrals and place the result in the buffer returned by <code>buffer()</code>.<br />
 void <code>compute_shell</code> (int, int, int)<br />
 <i></i><code>Compute</code> the derivative integrals with respect to the given center and place the result in the buffer returned by <code>buffer()</code>.</p>
<h3>Protected Types</h3>
<p>typedef void(Int1eCCA::* <code>IntegralFunction</code> )(int, int, <code>DerivCenters</code> &amp;)</p>
<h3>Protected Attributes</h3>
<p><code>Ref</code>&lt; <code>Int1eCCA</code> &gt; <code>int1ecca_</code></p>
<h2>Detailed Description</h2>
<p>This implements one body derivative integrals. </p>
<p> It is given a function pointer to the <code>Int1eCCA</code> member that computes the particular integral of interest.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::OneBodyDerivIntCCA::compute_shell (int ish, int jsh, int center) [virtual]</h3>
<p><code>Compute</code> the derivative integrals with respect to the given center and place the result in the buffer returned by <code>buffer()</code>. </p>
<p> Implements <code>sc::OneBodyDerivInt</code>.</p>
<h3>void sc::OneBodyDerivIntCCA::compute_shell (int ish, int jsh, <code>DerivCenters</code> &amp;) [virtual]</h3>
<p><code>Compute</code> the derivative integrals and place the result in the buffer returned by <code>buffer()</code>. </p>
<p> Implements <code>sc::OneBodyDerivInt</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
