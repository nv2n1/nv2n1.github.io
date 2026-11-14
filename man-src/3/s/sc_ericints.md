---
title: "sc_ericints(3)"
name: "sc_ericints"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_ericints/"
description: "sc::EriCints –"
---

<p>sc::EriCints &#8211; </p>
<p> <code>EriCints</code> is a specialization of <code>Int2eCints</code> that computes electron repulsion integrals.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;eri.h&gt;</code></pre>
<p> Inherits <code>sc::Int2eCints</code>.</p>
<h3>Public Member Functions</h3>
<p><code>EriCints</code> (<code>Integral</code> *, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;, size_t storage) </p>
<p> double * <code>buffer</code> (<code>TwoBodyInt::tbint_type</code> te_type) const<br />
 <i>Returns the location of the buffer with target integrals. </i><br />
 void <code>compute_quartet</code> (int *, int *, int *, int *)<br />
 <i>Evaluate the target quartet of integrals. </i></p>
<h3>Static Public Member Functions</h3>
<pre><code>static size_t storage_required (const Ref&lt; GaussianBasisSet &gt; &amp;b1, const Ref&lt; GaussianBasisSet &gt; &amp;b2=0, const Ref&lt; GaussianBasisSet &gt; &amp;b3=0, const Ref&lt; GaussianBasisSet &gt; &amp;b4=0)</code></pre>
<h2>Detailed Description</h2>
<p><code>EriCints</code> is a specialization of <code>Int2eCints</code> that computes electron repulsion integrals.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
