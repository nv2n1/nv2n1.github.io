---
title: "qwtsimplecompassrose(3)"
name: "qwtsimplecompassrose"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtsimplecompassrose/"
description: "QwtSimpleCompassRose –"
---

<p>QwtSimpleCompassRose &#8211; </p>
<p> A simple rose for <code>QwtCompass</code>.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_compass_rose.h&gt; </p>
<p> Inherits <code>QwtCompassRose</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtSimpleCompassRose</code> (int <code>numThorns</code>=8, int <code>numThornLevels</code>=-1) </p>
<p> virtual <code>~QwtSimpleCompassRose</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setWidth</code> (double w) </p>
<p> double <code>width</code> () const </p>
<p> void <code>setNumThorns</code> (int count) </p>
<p> int <code>numThorns</code> () const </p>
<p> void <code>setNumThornLevels</code> (int count) </p>
<p> int <code>numThornLevels</code> () const </p>
<p> void <code>setShrinkFactor</code> (double factor) </p>
<p> double <code>shrinkFactor</code> () const </p>
<p> virtual void <code>draw</code> (QPainter *, const QPointF &amp;center, double radius, double north, QPalette::ColorGroup=QPalette::Active) const </p>
<h3>Static Public Member Functions</h3>
<p>static void <code>drawRose</code> (QPainter *, const QPalette &amp;, const QPointF &amp;center, double radius, double origin, double <code>width</code>, int <code>numThorns</code>, int <code>numThornLevels</code>, double <code>shrinkFactor</code>) </p>
<h2>Detailed Description</h2>
<p>A simple rose for <code>QwtCompass</code>.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtSimpleCompassRose::QwtSimpleCompassRose (intnumThorns = 8, intnumThornLevels = -1)</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>numThorns</i> Number of thorns<br />
 <i>numThornLevels</i> Number of thorn levels</dl>
<h2>Member Function Documentation</h2>
<h3>void QwtSimpleCompassRose::draw (QPainter *painter, const QPointF &amp;center, doubleradius, doublenorth, QPalette::ColorGroupcg = QPalette::Active) const [virtual]</h3>
<p>Draw the rose </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>center</i> Center point<br />
 <i>radius</i> Radius of the rose<br />
 <i>north</i> Position<br />
 <i>cg</i> Color group</dl>
<p> Implements <code>QwtCompassRose</code>.</p>
<h3>void QwtSimpleCompassRose::drawRose (QPainter *painter, const QPalette &amp;palette, const QPointF &amp;center, doubleradius, doublenorth, doublewidth, intnumThorns, intnumThornLevels, doubleshrinkFactor) [static]</h3>
<p>Draw the rose </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>palette</i> Palette<br />
 <i>center</i> Center of the rose<br />
 <i>radius</i> Radius of the rose<br />
 <i>north</i> Position pointing to north<br />
 <i>width</i> Width of the rose<br />
 <i>numThorns</i> Number of thorns<br />
 <i>numThornLevels</i> Number of thorn levels<br />
 <i>shrinkFactor</i> Factor to shrink the thorns with each level</dl>
<h3>int QwtSimpleCompassRose::numThornLevels () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Number of thorn levels</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setNumThorns()</code>, <code>setNumThornLevels()</code></dl>
<h3>int QwtSimpleCompassRose::numThorns () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Number of thorns</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setNumThorns()</code>, <code>setNumThornLevels()</code></dl>
<h3>void QwtSimpleCompassRose::setNumThornLevels (intnumThornLevels)</h3>
<p>Set the of thorns levels </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>numThornLevels</i> Number of thorns levels</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setNumThorns()</code>, <code>numThornLevels()</code></dl>
<h3>void QwtSimpleCompassRose::setNumThorns (intnumThorns)</h3>
<p>Set the number of thorns on one level The number is aligned to a multiple of 4, with a minimum of 4 </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>numThorns</i> Number of thorns</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>numThorns()</code>, <code>setNumThornLevels()</code></dl>
<h3>void QwtSimpleCompassRose::setShrinkFactor (doublefactor)</h3>
<p>Set the Factor how to shrink the thorns with each level The default value is 0.9. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>factor</i> Shrink factor</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>shrinkFactor()</code></dl>
<h3>void QwtSimpleCompassRose::setWidth (doublewidth)</h3>
<p>Set the width of the rose heads. Lower value make thinner heads. The range is limited from 0.03 to 0.4. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>width</i> Width</dl>
<h3>double QwtSimpleCompassRose::shrinkFactor () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Factor how to shrink the thorns with each level</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setShrinkFactor()</code></dl>
<h3>double QwtSimpleCompassRose::width () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Width of the rose</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setWidth()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
