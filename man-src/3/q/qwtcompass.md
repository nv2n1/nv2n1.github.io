---
title: "qwtcompass(3)"
name: "qwtcompass"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtcompass/"
description: "QwtCompass –"
---

<p>QwtCompass &#8211; </p>
<p> A Compass Widget.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_compass.h&gt; </p>
<p> Inherits <code>QwtDial</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtCompass</code> (QWidget *parent=NULL)<br />
 <i>Constructor. </i><br />
 virtual <code>~QwtCompass</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setRose</code> (<code>QwtCompassRose</code> *<code>rose</code>) </p>
<p> const <code>QwtCompassRose</code> * <code>rose</code> () const </p>
<p> <code>QwtCompassRose</code> * <code>rose</code> () </p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>drawRose</code> (QPainter *, const QPointF &amp;center, double radius, double north, QPalette::ColorGroup) const </p>
<p> virtual void <code>drawScaleContents</code> (QPainter *, const QPointF &amp;center, double radius) const </p>
<p> virtual void <code>keyPressEvent</code> (QKeyEvent *) </p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p>A Compass Widget. </p>
<p> <code>QwtCompass</code> is a widget to display and enter directions. It consists of a scale, an optional needle and rose. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The examples/dials example shows how to use <code>QwtCompass</code>.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtCompass::QwtCompass (QWidget *parent = NULL) [explicit]</h3>
<p>Constructor. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>parent</i> Parent widget</dl>
<p> Create a compass widget with a scale, no needle and no rose. The default origin is 270.0 with no valid value. It accepts mouse and keyboard inputs and has no step size. The default mode is <code>QwtDial::RotateNeedle</code>.</p>
<h2>Member Function Documentation</h2>
<h3>void QwtCompass::drawRose (QPainter *painter, const QPointF &amp;center, doubleradius, doublenorth, QPalette::ColorGroupcg) const [protected], [virtual]</h3>
<p>Draw the compass rose </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>center</i> Center of the compass<br />
 <i>radius</i> of the circle, where to paint the rose<br />
 <i>north</i> Direction pointing north, in degrees counter clockwise<br />
 <i>cg</i> Color group</dl>
<h3>void QwtCompass::drawScaleContents (QPainter *painter, const QPointF &amp;center, doubleradius) const [protected], [virtual]</h3>
<p>Draw the contents of the scale </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>center</i> Center of the content circle<br />
 <i>radius</i> Radius of the content circle</dl>
<p> Reimplemented from <code>QwtDial</code>.</p>
<h3>void QwtCompass::keyPressEvent (QKeyEvent *kev) [protected], [virtual]</h3>
<p>Handles key events </p>
<p> Beside the keys described in <code>QwtDial::keyPressEvent</code> numbers from 1-9 (without 5) set the direction according to their position on the num pad. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isReadOnly()</code></dl>
<p> Reimplemented from <code>QwtAbstractSlider</code>.</p>
<h3>const <code>QwtCompassRose</code> * QwtCompass::rose () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>rose</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setRose()</code></dl>
<h3><code>QwtCompassRose</code> * QwtCompass::rose ()</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>rose</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setRose()</code></dl>
<h3>void QwtCompass::setRose (<code>QwtCompassRose</code> *rose)</h3>
<p>Set a rose for the compass </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rose</i> Compass rose</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The rose will be deleted, when a different rose is set or in ~QwtCompass</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>rose()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
