---
title: "findclosest(3)"
name: "findclosest"
section: "3"
letter: "f"
url: "/docs/linux/man/3-findclosest/"
description: "QuantLib::SphereCylinderOptimizer –"
---

<p>QuantLib::SphereCylinderOptimizer &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/optimization/spherecylinder.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>SphereCylinderOptimizer</code> (<code>Real</code> r, <code>Real</code> s, <code>Real</code> alpha, <code>Real</code> z1, <code>Real</code> z2, <code>Real</code> z3, <code>Real</code> zweight=1.0) </p>
<p> bool <code>isIntersectionNonEmpty</code> () const </p>
<p> void <code>findClosest</code> (Size maxIterations, <code>Real</code> tolerance, <code>Real</code> &amp;y1, <code>Real</code> &amp;y2, <code>Real</code> &amp;y3) const </p>
<p> bool <code>findByProjection</code> (<code>Real</code> &amp;y1, <code>Real</code> &amp;y2, <code>Real</code> &amp;y3) const </p>
<h2>Detailed Description</h2>
<dl COMPACT>
<dt>*</dt>
<dd>we are in r^3 sphere centred at O radius r</dd>
<dt> *</dt>
<dd>vertical cylinder centred at (alpha,0) radius s</dd>
<dt> *</dt>
<dd>Z some point in R3</dd>
<dt> *</dt>
<dd>find point on intersection that is closest to Z</dd></dl>
<p> the intersection may be empty! </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
