---
title: "sc_connollyshape(3)"
name: "sc_connollyshape"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_connollyshape/"
description: "sc::ConnollyShape –"
---

<p>sc::ConnollyShape &#8211; </p>
<p> <code>DiscreteConnollyShape</code> and <code>ConnollyShape</code> should produce the same result.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;molshape.h&gt;</code></pre>
<p> Inherits <code>sc::Shape</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>ConnollyShape (const Ref&lt; KeyVal &gt; &amp;)



void initialize (const Ref&lt; Molecule &gt; &amp;, double probe_radius)



void clear ()



double distance_to_surface (const SCVector3 &amp;r, SCVector3 *grad=0) const



void boundingbox (double valuemin, double valuemax, SCVector3 &amp;p1, SCVector3 &amp;p2)



Static Public Member Functions
static void print_counts (std::ostream &amp;=ExEnv::out0())</code></pre>
<h2>Detailed Description</h2>
<p><code>DiscreteConnollyShape</code> and <code>ConnollyShape</code> should produce the same result. </p>
<p> The discrete version is a shape union of discrete subshapes and is slower. These classes describe the solvent accessible surface of a molecule.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
