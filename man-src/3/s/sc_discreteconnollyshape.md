---
title: "sc_discreteconnollyshape(3)"
name: "sc_discreteconnollyshape"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_discreteconnollyshape/"
description: "sc::DiscreteConnollyShape –"
---

<p>sc::DiscreteConnollyShape &#8211; </p>
<p> <code>DiscreteConnollyShape</code> and <code>ConnollyShape</code> should produce the same result.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;molshape.h&gt;</code></pre>
<p> Inherits <code>sc::UnionShape</code>.</p>
<h3>Public Member Functions</h3>
<p><code>DiscreteConnollyShape</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> void <code>initialize</code> (const <code>Ref</code>&lt; <code>Molecule</code> &gt; &amp;, double probe_radius)</p>
<h2>Detailed Description</h2>
<p><code>DiscreteConnollyShape</code> and <code>ConnollyShape</code> should produce the same result. </p>
<p> The discrete version is a shape union of discrete subshapes and is slower. These classes describe the solvent accessible surface of a molecule.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
