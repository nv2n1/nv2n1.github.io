---
title: "xend_(3)"
name: "xend_"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xend_/"
description: "QuantLib::Interpolation::templateImpl – basic template implementation"
---

<p>QuantLib::Interpolation::templateImpl &#8211; basic template implementation </p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/math/interpolation.hpp&gt;</code></pre>
<p> Inherits <code>QuantLib::Interpolation::Impl</code>.</p>
<h3>Public Member Functions</h3>
<p><code>templateImpl</code> (const I1 &amp;xBegin, const I1 &amp;xEnd, const I2 &amp;yBegin) </p>
<p> Real <code>xMin</code> () const </p>
<p> Real <code>xMax</code> () const </p>
<p> std::vector&lt; Real &gt; <code>xValues</code> () const </p>
<p> std::vector&lt; Real &gt; <code>yValues</code> () const </p>
<p> bool <code>isInRange</code> (Real x) const</p>
<h3>Protected Member Functions</h3>
<p>Size <code>locate</code> (Real x) const</p>
<h3>Protected Attributes</h3>
<p>I1 <code>xBegin_</code> </p>
<p> I1 <code>xEnd_</code> </p>
<p> I2 <code>yBegin_</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;class I1, class I2&gt; class QuantLib::Interpolation::templateImpl&lt; I1, I2 &gt;</h3>
<p>basic template implementation</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
