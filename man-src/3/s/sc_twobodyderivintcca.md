---
title: "sc_twobodyderivintcca(3)"
name: "sc_twobodyderivintcca"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_twobodyderivintcca/"
description: "sc::TwoBodyDerivIntCCA –"
---

<p>sc::TwoBodyDerivIntCCA &#8211; </p>
<p> This implements two body derivative integrals through the CCA interface.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;tbintcca.h&gt;</code></pre>
<p> Inherits <code>sc::TwoBodyDerivInt</code>.</p>
<h3>Public Member Functions</h3>
<p><code>TwoBodyDerivIntCCA</code> (<code>Integral</code> *, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b1, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b2, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b3, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b4, size_t storage, IntegralEvaluatorFactory, bool, string) </p>
<p> int <code>log2_shell_bound</code> (int, int, int, int)<br />
 <i>Return log base 2 of the maximum magnitude of any integral in a shell block. </i><br />
 void <code>compute_shell</code> (int, int, int, int, <code>DerivCenters</code> &amp;)<br />
 <i>Given for shell indices, this will cause the integral buffer to be filled in. </i><br />
 size_t <code>storage_used</code> () </p>
<p> void <code>set_integral_storage</code> (size_t storage) </p>
<p> int <code>redundant</code> () const </p>
<p> void <code>set_redundant</code> (int i)</p>
<h3>Protected Attributes</h3>
<p><code>Ref</code>&lt; <code>Int2eCCA</code> &gt; <code>int2ecca_</code></p>
<h2>Detailed Description</h2>
<p>This implements two body derivative integrals through the CCA interface.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::TwoBodyDerivIntCCA::compute_shell (int, int, int, int, <code>DerivCenters</code> &amp;) [virtual]</h3>
<p>Given for shell indices, this will cause the integral buffer to be filled in. </p>
<p> Implements <code>sc::TwoBodyDerivInt</code>.</p>
<h3>int sc::TwoBodyDerivIntCCA::log2_shell_bound (int, int, int, int) [virtual]</h3>
<p>Return log base 2 of the maximum magnitude of any integral in a shell block. An index of -1 for any argument indicates any shell. </p>
<p> Implements <code>sc::TwoBodyDerivInt</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
