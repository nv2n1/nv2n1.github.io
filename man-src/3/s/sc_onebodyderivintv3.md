---
title: "sc_onebodyderivintv3(3)"
name: "sc_onebodyderivintv3"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_onebodyderivintv3/"
description: "sc::OneBodyDerivIntV3 –"
---

<p>sc::OneBodyDerivIntV3 &#8211; </p>
<p> This implements one body derivative integrals in the IntV3 library.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;obintv3.h&gt;</code></pre>
<p> Inherits <code>sc::OneBodyDerivInt</code>.</p>
<h3>Public Member Functions</h3>
<p><code>OneBodyDerivIntV3</code> (<code>Integral</code> *, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;, IntegralFunction) </p>
<p> void <code>compute_shell</code> (int, int, <code>DerivCenters</code> &amp;)<br />
 <i></i><code>Compute</code> the derivative integrals and place the result in the buffer returned by <code>buffer()</code>.<br />
 void <code>compute_shell</code> (int, int, int)<br />
 <i></i><code>Compute</code> the derivative integrals with respect to the given center and place the result in the buffer returned by <code>buffer()</code>.</p>
<h3>Protected Types</h3>
<p>typedef void(Int1eV3::* <code>IntegralFunction</code> )(int, int, int, int)</p>
<h3>Protected Attributes</h3>
<p><code>Ref</code>&lt; <code>Int1eV3</code> &gt; <code>int1ev3_</code> </p>
<p> IntegralFunction <code>intfunc_</code></p>
<h2>Detailed Description</h2>
<p>This implements one body derivative integrals in the IntV3 library. </p>
<p> It is given a function pointer to the <code>Int1eV3</code> member that computes the particular integral of interest.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::OneBodyDerivIntV3::compute_shell (int ish, int jsh, int center) [virtual]</h3>
<p><code>Compute</code> the derivative integrals with respect to the given center and place the result in the buffer returned by <code>buffer()</code>. </p>
<p> Implements <code>sc::OneBodyDerivInt</code>.</p>
<h3>void sc::OneBodyDerivIntV3::compute_shell (int ish, int jsh, <code>DerivCenters</code> &amp;) [virtual]</h3>
<p><code>Compute</code> the derivative integrals and place the result in the buffer returned by <code>buffer()</code>. </p>
<p> Implements <code>sc::OneBodyDerivInt</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
