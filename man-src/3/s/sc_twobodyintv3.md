---
title: "sc_twobodyintv3(3)"
name: "sc_twobodyintv3"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_twobodyintv3/"
description: "sc::TwoBodyIntV3 –"
---

<p>sc::TwoBodyIntV3 &#8211; </p>
<p> This implements electron repulsion integrals in the IntV3 library.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;tbintv3.h&gt;</code></pre>
<p> Inherits <code>sc::TwoBodyInt</code>.</p>
<h3>Public Member Functions</h3>
<p><code>TwoBodyIntV3</code> (<code>Integral</code> *integral, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b1, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b2, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b3, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b4, size_t storage) </p>
<p> int <code>log2_shell_bound</code> (int, int, int, int)<br />
 <i>Return log base 2 of the maximum magnitude of any integral in a shell block obtained from compute_shell. </i><br />
 void <code>compute_shell</code> (int, int, int, int)<br />
 <i>Given four shell indices, integrals will be computed and placed in the buffer. </i><br />
 size_t <code>storage_used</code> () </p>
<p> void <code>set_integral_storage</code> (size_t storage)<br />
 <i>This storage is used to cache computed integrals. </i></p>
<h3>Protected Attributes</h3>
<p><code>Ref</code>&lt; <code>Int2eV3</code> &gt; <code>int2ev3_</code></p>
<h2>Detailed Description</h2>
<p>This implements electron repulsion integrals in the IntV3 library.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::TwoBodyIntV3::compute_shell (int, int, int, int) [virtual]</h3>
<p>Given four shell indices, integrals will be computed and placed in the buffer. The first two indices correspond to electron 1 and the second two indices correspond to electron 2. </p>
<p> Implements <code>sc::TwoBodyInt</code>.</p>
<h3>int sc::TwoBodyIntV3::log2_shell_bound (int, int, int, int) [virtual]</h3>
<p>Return log base 2 of the maximum magnitude of any integral in a shell block obtained from compute_shell. An index of -1 for any argument indicates any shell. </p>
<p> Implements <code>sc::TwoBodyInt</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
