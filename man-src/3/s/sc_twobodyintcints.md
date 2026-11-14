---
title: "sc_twobodyintcints(3)"
name: "sc_twobodyintcints"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_twobodyintcints/"
description: "sc::TwoBodyIntCints –"
---

<p>sc::TwoBodyIntCints &#8211; </p>
<p> This implements electron repulsion integrals in the IntCints library.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;tbintcints.h&gt;</code></pre>
<p> Inherits <code>sc::TwoBodyInt</code>.</p>
<h3>Public Member Functions</h3>
<p><code>TwoBodyIntCints</code> (<code>Integral</code> *integral, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b1, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b2, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b3, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b4, size_t storage, tbinteval int2etype) </p>
<p> int <code>log2_shell_bound</code> (int, int, int, int)<br />
 <i>Return log base 2 of the maximum magnitude of any integral in a shell block obtained from compute_shell. </i><br />
 void <code>compute_shell</code> (int, int, int, int)<br />
 <i>Given four shell indices, integrals will be computed and placed in the buffer. </i><br />
 size_t <code>used_storage</code> () const </p>
<p> void <code>set_integral_storage</code> (size_t storage)<br />
 <i>This storage is used to cache computed integrals. </i><br />
 const double * <code>buffer</code> (<code>tbint_type</code> te_type) const<br />
 <i>The computed shell integrals will be put in the buffer returned by this member. </i></p>
<h3>Protected Attributes</h3>
<p><code>Ref</code>&lt; <code>Int2eCints</code> &gt; <code>int2ecints_</code></p>
<h2>Detailed Description</h2>
<p>This implements electron repulsion integrals in the IntCints library.</p>
<h2>Member Function Documentation</h2>
<h3>const double* sc::TwoBodyIntCints::buffer (<code>tbint_type</code> type) const [inline, virtual]</h3>
<p>The computed shell integrals will be put in the buffer returned by this member. Some <code>TwoBodyInt</code> specializations have more than one buffer: The type arguments selects which buffer is returned. If the requested type is not supported, then 0 is returned. </p>
<p> Reimplemented from <code>sc::TwoBodyInt</code>.</p>
<h3>void sc::TwoBodyIntCints::compute_shell (int, int, int, int) [virtual]</h3>
<p>Given four shell indices, integrals will be computed and placed in the buffer. The first two indices correspond to electron 1 and the second two indices correspond to electron 2. </p>
<p> Implements <code>sc::TwoBodyInt</code>.</p>
<h3>int sc::TwoBodyIntCints::log2_shell_bound (int, int, int, int) [virtual]</h3>
<p>Return log base 2 of the maximum magnitude of any integral in a shell block obtained from compute_shell. An index of -1 for any argument indicates any shell. </p>
<p> Implements <code>sc::TwoBodyInt</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
