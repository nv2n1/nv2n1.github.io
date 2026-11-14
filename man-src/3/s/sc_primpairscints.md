---
title: "sc_primpairscints(3)"
name: "sc_primpairscints"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_primpairscints/"
description: "sc::PrimPairsCints –"
---

<p>sc::PrimPairsCints &#8211; </p>
<p> <code>PrimPairsCints</code> contains primitive pair data.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;primpairs.h&gt;</code></pre>
<p> Inherits <code>sc::RefCount</code>.</p>
<h3>Public Member Functions</h3>
<p><code>PrimPairsCints</code> (const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;) </p>
<p> <code>prim_pair_t</code> * <code>prim_pair</code> (int p1, int p2) const </p>
<p> double <code>P</code> (int p1, int p2, int xyz) const </p>
<p> double <code>gamma</code> (int p1, int p2) const </p>
<p> double <code>ovlp</code> (int p1, int p2) const</p>
<h2>Detailed Description</h2>
<p><code>PrimPairsCints</code> contains primitive pair data.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
