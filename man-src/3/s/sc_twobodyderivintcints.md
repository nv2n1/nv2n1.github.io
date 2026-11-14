---
title: "sc_twobodyderivintcints(3)"
name: "sc_twobodyderivintcints"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_twobodyderivintcints/"
description: "sc::TwoBodyDerivIntCints –"
---

<p>sc::TwoBodyDerivIntCints &#8211; </p>
<p> This implements electron repulsion derivative integrals in the IntV3 library.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;tbintcints.h&gt;</code></pre>
<p> Inherits <code>sc::TwoBodyDerivInt</code>.</p>
<h3>Public Member Functions</h3>
<p><code>TwoBodyDerivIntCints</code> (<code>Integral</code> *integral, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b1, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b2, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b3, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b4, size_t storage, tbinteval int2etype) </p>
<p> int <code>log2_shell_bound</code> (int, int, int, int)<br />
 <i>Return log base 2 of the maximum magnitude of any integral in a shell block. </i><br />
 void <code>compute_shell</code> (int, int, int, int, <code>DerivCenters</code> &amp;)<br />
 <i>Given for shell indices, this will cause the integral buffer to be filled in. </i><br />
 size_t <code>used_storage</code> () const</p>
<h3>Protected Attributes</h3>
<p><code>Ref</code>&lt; <code>Int2eCints</code> &gt; <code>int2ecints_</code></p>
<h2>Detailed Description</h2>
<p>This implements electron repulsion derivative integrals in the IntV3 library.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::TwoBodyDerivIntCints::compute_shell (int, int, int, int, <code>DerivCenters</code> &amp;) [virtual]</h3>
<p>Given for shell indices, this will cause the integral buffer to be filled in. </p>
<p> Implements <code>sc::TwoBodyDerivInt</code>.</p>
<h3>int sc::TwoBodyDerivIntCints::log2_shell_bound (int, int, int, int) [virtual]</h3>
<p>Return log base 2 of the maximum magnitude of any integral in a shell block. An index of -1 for any argument indicates any shell. </p>
<p> Implements <code>sc::TwoBodyDerivInt</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
