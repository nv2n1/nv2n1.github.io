---
title: "sc_volume(3)"
name: "sc_volume"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_volume/"
description: "sc::Volume –"
---

<p>sc::Volume &#8211; </p>
<p> A <code>Volume</code> is a <code>Function</code> of three variables.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;volume.h&gt;</code></pre>
<p> Inherits <code>sc::Function</code>. Inherited by <code>sc::BatchElectronDensity</code>, <code>sc::ElectronDensity</code>, <code>sc::Orbital</code>, and <code>sc::Shape</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>Volume (const Ref&lt; KeyVal &gt; &amp;)



void set_gradient (const SCVector3 &amp;g)



void set_gradient (RefSCVector &amp;g)



void get_gradient (SCVector3 &amp;g)



void set_x (const SCVector3 &amp;x)



void set_x (const RefSCVector &amp;x)


Set and retrieve the coordinate values.


void get_x (SCVector3 &amp;x)



virtual void boundingbox (double valuemin, double valuemax, SCVector3 &amp;p1, SCVector3 &amp;p2)=0



virtual void interpolate (const SCVector3 &amp;p1, const SCVector3 &amp;p2, double value, SCVector3 &amp;result)



virtual void solve (const SCVector3 &amp;p, const SCVector3 &amp;grad, double value, SCVector3 &amp;result)



Protected Member Functions
double &amp; interpolation_accuracy ()



virtual void compute ()=0


Recompute at least the results that have compute true and are not already computed.


virtual void failure (const char *)</code></pre>
<h2>Detailed Description</h2>
<p>A <code>Volume</code> is a <code>Function</code> of three variables.</p>
<h2>Member Function Documentation</h2>
<h3>virtual void sc::Volume::compute () [protected, pure virtual]</h3>
<p>Recompute at least the results that have compute true and are not already computed. This should only be called by Result&#8217;s members. </p>
<p> Implements <code>sc::Compute</code>. </p>
<p> Implemented in <code>sc::ElectronDensity</code>, <code>sc::BatchElectronDensity</code>, <code>sc::Orbital</code>, and <code>sc::Shape</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
