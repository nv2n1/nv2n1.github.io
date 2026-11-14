---
title: "sc_sphericaltransformiter(3)"
name: "sc_sphericaltransformiter"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_sphericaltransformiter/"
description: "sc::SphericalTransformIter –"
---

<p>sc::SphericalTransformIter &#8211; </p>
<p> This iterates through the components of a <code>SphericalTransform</code>.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;transform.h&gt;

Public Member Functions</code></pre>
<p> <code>SphericalTransformIter</code> (const <code>SphericalTransform</code> *) </p>
<p> void <code>begin</code> () </p>
<p> void <code>start</code> () </p>
<p> void <code>next</code> () </p>
<p> int <code>ready</code> () </p>
<p> <code>operator int</code> () </p>
<p> int <code>l</code> () </p>
<p> int <code>cartindex</code> () </p>
<p> int <code>pureindex</code> () </p>
<p> int <code>bfn</code> () </p>
<p> double <code>coef</code> () </p>
<p> int <code>a</code> () </p>
<p> int <code>b</code> () </p>
<p> int <code>c</code> () </p>
<p> int <code>l</code> (int i) </p>
<p> int <code>n</code> ()</p>
<h3>Protected Attributes</h3>
<pre><code>const SphericalTransform * transform_</code></pre>
<h2>Detailed Description</h2>
<p>This iterates through the components of a <code>SphericalTransform</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
