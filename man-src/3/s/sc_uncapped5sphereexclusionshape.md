---
title: "sc_uncapped5sphereexclusionshape(3)"
name: "sc_uncapped5sphereexclusionshape"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_uncapped5sphereexclusionshape/"
description: "sc::Uncapped5SphereExclusionShape –"
---

<p>sc::Uncapped5SphereExclusionShape &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::Shape</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>const SCVector3 A () const



const SCVector3 B () const



const SCVector3 C () const



double rA () const



double rB () const



double rC () const



double r () const



int solution_exists () const



double distance_to_surface (const SCVector3 &amp;r, SCVector3 *grad=0) const



int is_outside (const SCVector3 &amp;) const



void boundingbox (double valuemin, double valuemax, SCVector3 &amp;p1, SCVector3 &amp;p2)



int gradient_implemented () const



Static Public Member Functions
static Uncapped5SphereExclusionShape * newUncapped5SphereExclusionShape (double r, const SphereShape &amp;, const SphereShape &amp;, const SphereShape &amp;)



Protected Member Functions</code></pre>
<p> <code>Uncapped5SphereExclusionShape</code> (double r, const <code>SphereShape</code> &amp;, const <code>SphereShape</code> &amp;, const <code>SphereShape</code> &amp;) </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
