---
title: "sc_efielddotvectorintv3(3)"
name: "sc_efielddotvectorintv3"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_efielddotvectorintv3/"
description: "sc::EfieldDotVectorIntV3 –"
---

<p>sc::EfieldDotVectorIntV3 &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::OneBodyInt</code>.</p>
<h3>Public Member Functions</h3>
<p><code>EfieldDotVectorIntV3</code> (<code>Integral</code> *, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;, const <code>Ref</code>&lt; <code>EfieldDotVectorData</code> &gt; &amp;) </p>
<p> void <code>compute_shell</code> (int, int)<br />
 <i>Computes the integrals between basis functions in the given shell pair. </i></p>
<h3>Protected Attributes</h3>
<p><code>Ref</code>&lt; <code>Int1eV3</code> &gt; <code>int1ev3_</code> </p>
<p> <code>Ref</code>&lt; <code>EfieldDotVectorData</code> &gt; <code>data_</code></p>
<h2>Member Function Documentation</h2>
<h3>void sc::EfieldDotVectorIntV3::compute_shell (int, int) [virtual]</h3>
<p>Computes the integrals between basis functions in the given shell pair. </p>
<p> Implements <code>sc::OneBodyInt</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
