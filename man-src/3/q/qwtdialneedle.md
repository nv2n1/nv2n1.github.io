---
title: "qwtdialneedle(3)"
name: "qwtdialneedle"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtdialneedle/"
description: "QwtDialNeedle –"
---

<p>QwtDialNeedle &#8211; </p>
<p> Base class for needles that can be used in a <code>QwtDial</code>.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_dial_needle.h&gt; </p>
<p> Inherited by <code>QwtCompassMagnetNeedle</code>, <code>QwtCompassWindArrow</code>, and <code>QwtDialSimpleNeedle</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtDialNeedle</code> ()<br />
 <i>Constructor. </i><br />
 virtual <code>~QwtDialNeedle</code> ()<br />
 <i>Destructor. </i><br />
 virtual void <code>setPalette</code> (const QPalette &amp;) </p>
<p> const QPalette &amp; <code>palette</code> () const </p>
<p> virtual void <code>draw</code> (QPainter *painter, const QPointF &amp;center, double length, double direction, QPalette::ColorGroup=QPalette::Active) const </p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>drawNeedle</code> (QPainter *painter, double length, QPalette::ColorGroup colorGroup) const =0<br />
 <i>Draw the needle. </i><br />
 virtual void <code>drawKnob</code> (QPainter *, double width, const QBrush &amp;, bool sunken) const<br />
 <i>Draw the knob. </i></p>
<h2>Detailed Description</h2>
<p>Base class for needles that can be used in a <code>QwtDial</code>. </p>
<p> <code>QwtDialNeedle</code> is a pointer that indicates a value by pointing to a specific direction. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtDial</code>, <code>QwtCompass</code></dl>
<h2>Member Function Documentation</h2>
<h3>void QwtDialNeedle::draw (QPainter *painter, const QPointF &amp;center, doublelength, doubledirection, QPalette::ColorGroupcolorGroup = QPalette::Active) const [virtual]</h3>
<p>Draw the needle </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>center</i> Center of the dial, start position for the needle<br />
 <i>length</i> Length of the needle<br />
 <i>direction</i> Direction of the needle, in degrees counter clockwise<br />
 <i>colorGroup</i> Color group, used for painting</dl>
<h3>virtual void QwtDialNeedle::drawNeedle (QPainter *painter, doublelength, QPalette::ColorGroupcolorGroup) const [protected], [pure virtual]</h3>
<p>Draw the needle. The origin of the needle is at position (0.0, 0.0 ) pointing in direction 0.0 ( = east ). </p>
<p> The painter is already initialized with translation and rotation. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>length</i> Length of the needle<br />
 <i>colorGroup</i> Color group, used for painting</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPalette()</code>, <code>palette()</code></dl>
<p> Implemented in <code>QwtCompassWindArrow</code>, <code>QwtCompassMagnetNeedle</code>, and <code>QwtDialSimpleNeedle</code>.</p>
<h3>const QPalette &amp; QwtDialNeedle::palette () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the palette of the needle.</dl>
<h3>void QwtDialNeedle::setPalette (const QPalette &amp;palette) [virtual]</h3>
<p>Sets the palette for the needle. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>palette</i> New Palette</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
