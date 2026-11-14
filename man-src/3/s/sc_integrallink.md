---
title: "sc_integrallink(3)"
name: "sc_integrallink"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_integrallink/"
description: "sc::IntegralLink –"
---

<p>sc::IntegralLink &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Member Functions</h3>
<p><code>IntegralLink</code> (<code>IntegralKey</code> &amp;key, int cost, int size) </p>
<p> int <code>actualsize</code> () const </p>
<p> int <code>hash</code> () const </p>
<p> int <code>cost</code> () const </p>
<p> void <code>print</code> () </p>
<p> double * <code>buffer</code> () </p>
<p> void * <code>operator new</code> (size_t, int) </p>
<p> void <code>operator delete</code> (void *, int) </p>
<p> void <code>operator delete</code> (void *)</p>
<h3>Static Public Member Functions</h3>
<pre><code>static int size_to_actualsize (int size)



static int shells_to_hash (int, int, int, int)



Public Attributes</code></pre>
<p> <code>EAVLMMapNode</code>&lt; <code>IntegralKey</code>, <code>IntegralLink</code> &gt; <code>intlist</code> </p>
<p> <code>EAVLMMapNode</code>&lt; int, <code>IntegralLink</code> &gt; <code>costlist</code> </p>
<p> int <code>size</code> </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
