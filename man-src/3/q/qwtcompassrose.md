---
title: "qwtcompassrose(3)"
name: "qwtcompassrose"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtcompassrose/"
description: "QwtCompassRose –"
---

<p>QwtCompassRose &#8211; </p>
<p> Abstract base class for a compass rose.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_compass_rose.h&gt; </p>
<p> Inherited by <code>QwtSimpleCompassRose</code>.</p>
<h3>Public Member Functions</h3>
<p>virtual <code>~QwtCompassRose</code> ()<br />
 <i>Destructor. </i><br />
 virtual void <code>setPalette</code> (const QPalette &amp;p)<br />
 <i>Assign a palette. </i><br />
 const QPalette &amp; <code>palette</code> () const </p>
<p> virtual void <code>draw</code> (QPainter *painter, const QPointF &amp;center, double radius, double north, QPalette::ColorGroup colorGroup=QPalette::Active) const =0 </p>
<h2>Detailed Description</h2>
<p>Abstract base class for a compass rose.</p>
<h2>Member Function Documentation</h2>
<h3>virtual void QwtCompassRose::draw (QPainter *painter, const QPointF &amp;center, doubleradius, doublenorth, QPalette::ColorGroupcolorGroup = QPalette::Active) const [pure virtual]</h3>
<p>Draw the rose </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>center</i> Center point<br />
 <i>radius</i> Radius of the rose<br />
 <i>north</i> Position<br />
 <i>colorGroup</i> Color group</dl>
<p> Implemented in <code>QwtSimpleCompassRose</code>.</p>
<h3>const QPalette&amp; QwtCompassRose::palette () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Current palette</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
