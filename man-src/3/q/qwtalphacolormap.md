---
title: "qwtalphacolormap(3)"
name: "qwtalphacolormap"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtalphacolormap/"
description: "QwtAlphaColorMap –"
---

<p>QwtAlphaColorMap &#8211; </p>
<p> <code>QwtAlphaColorMap</code> varies the alpha value of a color.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_color_map.h&gt; </p>
<p> Inherits <code>QwtColorMap</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtAlphaColorMap</code> (const QColor &amp;=QColor(Qt::gray)) </p>
<p> virtual <code>~QwtAlphaColorMap</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setColor</code> (const QColor &amp;) </p>
<p> QColor <code>color</code> () const </p>
<p> virtual QRgb <code>rgb</code> (const <code>QwtInterval</code> &amp;, double value) const<br />
 <i>Map a value of a given interval into a alpha value. </i></p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p><code>QwtAlphaColorMap</code> varies the alpha value of a color.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtAlphaColorMap::QwtAlphaColorMap (const QColor &amp;color = QColor( Qt::gray ))</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>color</i> Color of the map</dl>
<h2>Member Function Documentation</h2>
<h3>QColor QwtAlphaColorMap::color () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the color</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setColor()</code></dl>
<h3>QRgb QwtAlphaColorMap::rgb (const <code>QwtInterval</code> &amp;interval, doublevalue) const [virtual]</h3>
<p>Map a value of a given interval into a alpha value. alpha := (value &#8211; interval.minValue()) / interval.width(); </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>interval</i> Range for all values<br />
 <i>value</i> Value to map into a RGB value</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>RGB value, with an alpha value</dl>
<p> Implements <code>QwtColorMap</code>.</p>
<h3>void QwtAlphaColorMap::setColor (const QColor &amp;color)</h3>
<p>Set the color </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>color</i> Color</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>color()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
