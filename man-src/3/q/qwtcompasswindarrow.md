---
title: "qwtcompasswindarrow(3)"
name: "qwtcompasswindarrow"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtcompasswindarrow/"
description: "QwtCompassWindArrow –"
---

<p>QwtCompassWindArrow &#8211; </p>
<p> An indicator for the wind direction.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_dial_needle.h&gt; </p>
<p> Inherits <code>QwtDialNeedle</code>.</p>
<h3>Public Types</h3>
<p>enum <code>Style</code> { <code>Style1</code>, <code>Style2</code> }<br />
 <i>Style of the arrow. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtCompassWindArrow</code> (<code>Style</code>, const QColor &amp;light=Qt::white, const QColor &amp;dark=Qt::gray) </p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>drawNeedle</code> (QPainter *, double length, QPalette::ColorGroup) const </p>
<h2>Detailed Description</h2>
<p>An indicator for the wind direction. </p>
<p> <code>QwtCompassWindArrow</code> shows the direction where the wind comes from. </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>QPalette::Light </p>
<p>&nbsp;<wbr>Used for Style1, or the light half of Style2</p>
<dt>&bull;</p>
<dd>QPalette::Dark </p>
<p>&nbsp;<wbr>Used for the dark half of Style2</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtDial</code>, <code>QwtCompass</code></dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtCompassWindArrow::Style</code></h3>
<p>Style of the arrow. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>Style1 </i></p>
<dd>A needle pointing to the center.</p>
<dt><i>Style2 </i></p>
<dd>A needle pointing to the center.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtCompassWindArrow::QwtCompassWindArrow (<code>Style</code>style, const QColor &amp;light = Qt::white, const QColor &amp;dark = Qt::gray)</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>style</i> Arrow style<br />
 <i>light</i> Light color<br />
 <i>dark</i> Dark color</dl>
<h2>Member Function Documentation</h2>
<h3>void QwtCompassWindArrow::drawNeedle (QPainter *painter, doublelength, QPalette::ColorGroupcolorGroup) const [protected], [virtual]</h3>
<p>Draw the needle </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>length</i> Length of the needle<br />
 <i>colorGroup</i> Color group, used for painting</dl>
<p> Implements <code>QwtDialNeedle</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
