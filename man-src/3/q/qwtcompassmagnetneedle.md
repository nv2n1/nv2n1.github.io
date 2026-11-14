---
title: "qwtcompassmagnetneedle(3)"
name: "qwtcompassmagnetneedle"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtcompassmagnetneedle/"
description: "QwtCompassMagnetNeedle –"
---

<p>QwtCompassMagnetNeedle &#8211; </p>
<p> A magnet needle for compass widgets.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_dial_needle.h&gt; </p>
<p> Inherits <code>QwtDialNeedle</code>.</p>
<h3>Public Types</h3>
<p>enum <code>Style</code> { <code>TriangleStyle</code>, <code>ThinStyle</code> }<br />
 <i>Style of the needle. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtCompassMagnetNeedle</code> (<code>Style</code>=<code>TriangleStyle</code>, const QColor &amp;light=Qt::white, const QColor &amp;dark=Qt::red)<br />
 <i>Constructor. </i></p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>drawNeedle</code> (QPainter *, double length, QPalette::ColorGroup) const </p>
<h2>Detailed Description</h2>
<p>A magnet needle for compass widgets. </p>
<p> A magnet needle points to two opposite directions indicating north and south. </p>
<p> The following colors are used:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>QPalette::Light </p>
<p>&nbsp;<wbr>Used for pointing south</p>
<dt>&bull;</p>
<dd>QPalette::Dark </p>
<p>&nbsp;<wbr>Used for pointing north</p>
<dt>&bull;</p>
<dd>QPalette::Base </p>
<p>&nbsp;<wbr>Knob&nbsp;<wbr>(ThinStyle only)</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtDial</code>, <code>QwtCompass</code></dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtCompassMagnetNeedle::Style</code></h3>
<p>Style of the needle. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>TriangleStyle </i></p>
<dd>A needle with a triangular shape.</p>
<dt><i>ThinStyle </i></p>
<dd>A thin needle.</dl>
<h2>Member Function Documentation</h2>
<h3>void QwtCompassMagnetNeedle::drawNeedle (QPainter *painter, doublelength, QPalette::ColorGroupcolorGroup) const [protected], [virtual]</h3>
<p>Draw the needle </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>length</i> Length of the needle<br />
 <i>colorGroup</i> Color group, used for painting</dl>
<p> Implements <code>QwtDialNeedle</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
