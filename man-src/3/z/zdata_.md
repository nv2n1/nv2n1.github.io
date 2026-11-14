---
title: "zdata_(3)"
name: "zdata_"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zdata_/"
description: "QuantLib::Interpolation2D::templateImpl – basic template implementation"
---

<p>QuantLib::Interpolation2D::templateImpl &#8211; basic template implementation </p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/math/interpolations/interpolation2d.hpp&gt;</code></pre>
<p> Inherits <code>QuantLib::Interpolation2D::Impl</code>.</p>
<h3>Public Member Functions</h3>
<p><code>templateImpl</code> (const I1 &amp;xBegin, const I1 &amp;xEnd, const I2 &amp;yBegin, const I2 &amp;yEnd, const M &amp;zData) </p>
<p> Real <code>xMin</code> () const </p>
<p> Real <code>xMax</code> () const </p>
<p> std::vector&lt; Real &gt; <code>xValues</code> () const </p>
<p> Real <code>yMin</code> () const </p>
<p> Real <code>yMax</code> () const </p>
<p> std::vector&lt; Real &gt; <code>yValues</code> () const </p>
<p> const <code>Matrix</code> &amp; <code>zData</code> () const </p>
<p> bool <code>isInRange</code> (Real x, Real y) const</p>
<h3>Protected Member Functions</h3>
<p>Size <code>locateX</code> (Real x) const </p>
<p> Size <code>locateY</code> (Real y) const</p>
<h3>Protected Attributes</h3>
<p>I1 <code>xBegin_</code> </p>
<p> I1 <code>xEnd_</code> </p>
<p> I2 <code>yBegin_</code> </p>
<p> I2 <code>yEnd_</code> </p>
<p> const M &amp; <code>zData_</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;class I1, class I2, class M&gt; class QuantLib::Interpolation2D::templateImpl&lt; I1, I2, M &gt;</h3>
<p>basic template implementation</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
