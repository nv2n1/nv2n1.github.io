---
title: "sc_gpetite4(3)"
name: "sc_gpetite4"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_gpetite4/"
description: "sc::GPetite4 –"
---

<p>sc::GPetite4 &#8211; </p>
<p> This class provides a generalized four index petite list.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;gpetite.h&gt;</code></pre>
<p> Inherits <code>sc::GenPetite4</code>.</p>
<h3>Public Member Functions</h3>
<p><code>GPetite4</code> (const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b1, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b2, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b3, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b4, const C4 &amp;c) </p>
<p> int <code>in_p4</code> (int i, int j, int k, int l)</p>
<h2>Detailed Description</h2>
<h3>template&lt;class C4&gt; class sc::GPetite4&lt; C4 &gt;</h3>
<p>This class provides a generalized four index petite list. </p>
<p> The template argument is a class that computes an canonical offset given four indices for the particular shell loop structure employed. Example template class parameters are <code>canonical_aaaa</code>, <code>canonical_aabc</code>, <code>canonical_aabb</code>, and <code>canonical_abcd</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
