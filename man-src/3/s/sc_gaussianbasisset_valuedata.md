---
title: "sc_gaussianbasisset_valuedata(3)"
name: "sc_gaussianbasisset_valuedata"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_gaussianbasisset_valuedata/"
description: "sc::GaussianBasisSet::ValueData –"
---

<p>sc::GaussianBasisSet::ValueData &#8211; </p>
<p> This holds scratch data needed to compute basis function values.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;gaussbas.h&gt;

Public Member Functions</code></pre>
<p> <code>ValueData</code> (const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;, const <code>Ref</code>&lt; <code>Integral</code> &gt; &amp;) </p>
<p> <code>CartesianIter</code> ** <code>civec</code> () </p>
<p> <code>SphericalTransformIter</code> ** <code>sivec</code> ()</p>
<h3>Protected Attributes</h3>
<p><code>CartesianIter</code> ** <code>civec_</code> </p>
<p> <code>SphericalTransformIter</code> ** <code>sivec_</code> </p>
<p> int <code>maxam_</code></p>
<h2>Detailed Description</h2>
<p>This holds scratch data needed to compute basis function values.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
