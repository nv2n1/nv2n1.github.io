---
title: "sc_sphereshape(3)"
name: "sc_sphereshape"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_sphereshape/"
description: "sc::SphereShape –"
---

<p>sc::SphereShape &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::Shape</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>SphereShape (const SCVector3 &amp;, double)



SphereShape (const Ref&lt; KeyVal &gt; &amp;)



SphereShape (const SphereShape &amp;)



void boundingbox (double minvalue, double maxvalue, SCVector3 &amp;p1, SCVector3 &amp;p2)



double radius () const



const SCVector3 &amp; origin () const



double distance_to_surface (const SCVector3 &amp;r, SCVector3 *grad=0) const



void print (std::ostream &amp;o=ExEnv::out0()) const


Print information about the object.


double radius (double r)



const SCVector3 &amp; origin (const SCVector3 &amp;o)



int gradient_implemented () const
</code></pre>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
