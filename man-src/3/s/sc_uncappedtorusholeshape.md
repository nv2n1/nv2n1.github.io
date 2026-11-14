---
title: "sc_uncappedtorusholeshape(3)"
name: "sc_uncappedtorusholeshape"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_uncappedtorusholeshape/"
description: "sc::UncappedTorusHoleShape –"
---

<p>sc::UncappedTorusHoleShape &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::Shape</code>. Inherited by <code>sc::NonreentrantUncappedTorusHoleShape</code>, and <code>sc::ReentrantUncappedTorusHoleShape</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>const SphereShape &amp; sphere (int i) const



const SCVector3 A () const



const SCVector3 B () const



double radius () const



void print (std::ostream &amp;o=ExEnv::out0()) const


Print information about the object.


void boundingbox (double valuemin, double valuemax, SCVector3 &amp;p1, SCVector3 &amp;p2)



int gradient_implemented () const



Static Public Member Functions
static UncappedTorusHoleShape * newUncappedTorusHoleShape (double r, const SphereShape &amp;, const SphereShape &amp;)



Protected Member Functions
void in_plane_sphere (const SCVector3 &amp;point, SCVector3 &amp;origin) const



UncappedTorusHoleShape (double r, const SphereShape &amp;, const SphereShape &amp;)
</code></pre>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
