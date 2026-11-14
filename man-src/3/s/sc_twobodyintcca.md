---
title: "sc_twobodyintcca(3)"
name: "sc_twobodyintcca"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_twobodyintcca/"
description: "sc::TwoBodyIntCCA –"
---

<p>sc::TwoBodyIntCCA &#8211; </p>
<p> This implements two body integrals through the CCA interface.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;tbintcca.h&gt;</code></pre>
<p> Inherits <code>sc::TwoBodyInt</code>.</p>
<h3>Public Member Functions</h3>
<p><code>TwoBodyIntCCA</code> (<code>Integral</code> *, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b1, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b2, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b3, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b4, size_t storage, IntegralEvaluatorFactory, bool, string) </p>
<p> int <code>log2_shell_bound</code> (int, int, int, int)<br />
 <i>Return log base 2 of the maximum magnitude of any integral in a shell block obtained from compute_shell. </i><br />
 void <code>compute_shell</code> (int, int, int, int)<br />
 <i>Given four shell indices, integrals will be computed and placed in the buffer. </i><br />
 size_t <code>storage_used</code> () </p>
<p> void <code>set_integral_storage</code> (size_t storage)<br />
 <i>This storage is used to cache computed integrals. </i><br />
 int <code>redundant</code> () const<br />
 <i>If redundant is true, then keep redundant integrals in the buffer. </i><br />
 void <code>set_redundant</code> (int i)<br />
 <i>See </i><code>redundant()</code>.</p>
<h3>Protected Attributes</h3>
<p><code>Ref</code>&lt; <code>Int2eCCA</code> &gt; <code>int2ecca_</code></p>
<h2>Detailed Description</h2>
<p>This implements two body integrals through the CCA interface.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::TwoBodyIntCCA::compute_shell (int, int, int, int) [virtual]</h3>
<p>Given four shell indices, integrals will be computed and placed in the buffer. The first two indices correspond to electron 1 and the second two indices correspond to electron 2. </p>
<p> Implements <code>sc::TwoBodyInt</code>.</p>
<h3>int sc::TwoBodyIntCCA::log2_shell_bound (int, int, int, int) [virtual]</h3>
<p>Return log base 2 of the maximum magnitude of any integral in a shell block obtained from compute_shell. An index of -1 for any argument indicates any shell. </p>
<p> Implements <code>sc::TwoBodyInt</code>.</p>
<h3>int sc::TwoBodyIntCCA::redundant () const [inline, virtual]</h3>
<p>If redundant is true, then keep redundant integrals in the buffer. The default is true. </p>
<p> Reimplemented from <code>sc::TwoBodyInt</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
