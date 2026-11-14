---
title: "sc_integralstorer(3)"
name: "sc_integralstorer"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_integralstorer/"
description: "sc::IntegralStorer –"
---

<p>sc::IntegralStorer &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::DescribedClass</code>.</p>
<h3>Public Member Functions</h3>
<p><code>IntegralStorer</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> void <code>init</code> (int nbytes) </p>
<p> void <code>done</code> () </p>
<p> <code>IntegralLink</code> * <code>find</code> (<code>IntegralKey</code> &amp;) </p>
<p> int <code>should_store</code> (int cost, int actualsize) </p>
<p> void <code>store</code> (<code>IntegralKey</code> &amp;key, const double *buf, int size, int cost, int actualsize) </p>
<p> void <code>print_stats</code> () </p>
<p> int <code>table_size</code> () const </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
