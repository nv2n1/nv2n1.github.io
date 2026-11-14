---
title: "sc_onebodyintv3(3)"
name: "sc_onebodyintv3"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_onebodyintv3/"
description: "sc::OneBodyIntV3 –"
---

<p>sc::OneBodyIntV3 &#8211; </p>
<p> This implements most one body integrals in the IntV3 library.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;obintv3.h&gt;</code></pre>
<p> Inherits <code>sc::OneBodyInt</code>.</p>
<h3>Public Member Functions</h3>
<p><code>OneBodyIntV3</code> (<code>Integral</code> *, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;, IntegralFunction) </p>
<p> void <code>compute_shell</code> (int, int)<br />
 <i>Computes the integrals between basis functions in the given shell pair. </i><br />
 bool <code>cloneable</code> ()<br />
 <i>Return true if the clone member can be called. </i><br />
 <code>Ref</code>&lt; <code>OneBodyInt</code> &gt; <code>clone</code> ()<br />
 <i>Returns a clone of this. </i></p>
<h3>Protected Types</h3>
<p>typedef void(Int1eV3::* <code>IntegralFunction</code> )(int, int)</p>
<h3>Protected Attributes</h3>
<p><code>Ref</code>&lt; <code>Int1eV3</code> &gt; <code>int1ev3_</code> </p>
<p> IntegralFunction <code>intfunc_</code></p>
<h2>Detailed Description</h2>
<p>This implements most one body integrals in the IntV3 library. </p>
<p> It is given a function pointer to the <code>Int1eV3</code> member that computes the particular integral of interest.</p>
<h2>Member Function Documentation</h2>
<h3><code>Ref</code>&lt;<code>OneBodyInt</code>&gt; sc::OneBodyIntV3::clone () [virtual]</h3>
<p>Returns a clone of this. The default implementation throws an exception. </p>
<p> Reimplemented from <code>sc::OneBodyInt</code>.</p>
<h3>bool sc::OneBodyIntV3::cloneable () [virtual]</h3>
<p>Return true if the clone member can be called. The default implementation returns false. </p>
<p> Reimplemented from <code>sc::OneBodyInt</code>.</p>
<h3>void sc::OneBodyIntV3::compute_shell (int, int) [virtual]</h3>
<p>Computes the integrals between basis functions in the given shell pair. </p>
<p> Implements <code>sc::OneBodyInt</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
