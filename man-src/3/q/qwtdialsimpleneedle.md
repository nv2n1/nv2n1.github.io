---
title: "qwtdialsimpleneedle(3)"
name: "qwtdialsimpleneedle"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtdialsimpleneedle/"
description: "QwtDialSimpleNeedle –"
---

<p>QwtDialSimpleNeedle &#8211; </p>
<p> A needle for dial widgets.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_dial_needle.h&gt; </p>
<p> Inherits <code>QwtDialNeedle</code>.</p>
<h3>Public Types</h3>
<p>enum <code>Style</code> { <code>Arrow</code>, <code>Ray</code> }<br />
 <i>Style of the needle. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtDialSimpleNeedle</code> (<code>Style</code>, bool hasKnob=true, const QColor &amp;mid=Qt::gray, const QColor &amp;base=Qt::darkGray) </p>
<p> void <code>setWidth</code> (double <code>width</code>) </p>
<p> double <code>width</code> () const </p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>drawNeedle</code> (QPainter *, double length, QPalette::ColorGroup) const </p>
<h2>Detailed Description</h2>
<p>A needle for dial widgets. </p>
<p> The following colors are used: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>QPalette::Mid </p>
<p>&nbsp;<wbr>Pointer</p>
<dt>&bull;</p>
<dd>QPalette::Base </p>
<p>&nbsp;<wbr>Knob</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtDial</code>, <code>QwtCompass</code></dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtDialSimpleNeedle::Style</code></h3>
<p>Style of the needle. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>Arrow </i></p>
<dd>Arrow.</p>
<dt><i>Ray </i></p>
<dd>A straight line from the center.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtDialSimpleNeedle::QwtDialSimpleNeedle (<code>Style</code>style, boolhasKnob = true, const QColor &amp;mid = Qt::gray, const QColor &amp;base = Qt::darkGray)</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>style</i> Style<br />
 <i>hasKnob</i> With/Without knob<br />
 <i>mid</i> Middle color<br />
 <i>base</i> Base color</dl>
<h2>Member Function Documentation</h2>
<h3>void QwtDialSimpleNeedle::drawNeedle (QPainter *painter, doublelength, QPalette::ColorGroupcolorGroup) const [protected], [virtual]</h3>
<p>Draw the needle </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>length</i> Length of the needle<br />
 <i>colorGroup</i> Color group, used for painting</dl>
<p> Implements <code>QwtDialNeedle</code>.</p>
<h3>void QwtDialSimpleNeedle::setWidth (doublewidth)</h3>
<p>Set the width of the needle </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>width</i> Width</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>width()</code></dl>
<h3>double QwtDialSimpleNeedle::width () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the width of the needle</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setWidth()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
