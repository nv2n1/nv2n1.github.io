---
title: "qwtroundscaledraw(3)"
name: "qwtroundscaledraw"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtroundscaledraw/"
description: "QwtRoundScaleDraw –"
---

<p>QwtRoundScaleDraw &#8211; </p>
<p> A class for drawing round scales.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_round_scale_draw.h&gt; </p>
<p> Inherits <code>QwtAbstractScaleDraw</code>. </p>
<p> Inherited by QwtAnalogClockScaleDraw, and <code>QwtCompassScaleDraw</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtRoundScaleDraw</code> ()<br />
 <i>Constructor. </i><br />
 virtual <code>~QwtRoundScaleDraw</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setRadius</code> (double <code>radius</code>) </p>
<p> double <code>radius</code> () const </p>
<p> void <code>moveCenter</code> (double x, double y)<br />
 <i>Move the center of the scale draw, leaving the radius unchanged. </i><br />
 void <code>moveCenter</code> (const QPointF &amp;) </p>
<p> QPointF <code>center</code> () const<br />
 <i>Get the center of the scale. </i><br />
 void <code>setAngleRange</code> (double angle1, double angle2)<br />
 <i>Adjust the baseline circle segment for round scales. </i><br />
 virtual double <code>extent</code> (const QFont &amp;) const </p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>drawTick</code> (QPainter *, double val, double len) const </p>
<p> virtual void <code>drawBackbone</code> (QPainter *) const </p>
<p> virtual void <code>drawLabel</code> (QPainter *, double val) const </p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p>A class for drawing round scales. </p>
<p> <code>QwtRoundScaleDraw</code> can be used to draw round scales. The circle segment can be adjusted by <code>setAngleRange()</code>. The geometry of the scale can be specified with <code>moveCenter()</code> and <code>setRadius()</code>. </p>
<p> After a scale division has been specified as a <code>QwtScaleDiv</code> object using <code>QwtAbstractScaleDraw::setScaleDiv(const QwtScaleDiv &amp;s)</code>, the scale can be drawn with the <code>QwtAbstractScaleDraw::draw()</code> member.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtRoundScaleDraw::QwtRoundScaleDraw ()</h3>
<p>Constructor. The range of the scale is initialized to [0, 100], The center is set to (50, 50) with a radius of 50. The angle range is set to [-135, 135].</p>
<h2>Member Function Documentation</h2>
<h3>void QwtRoundScaleDraw::drawBackbone (QPainter *painter) const [protected], [virtual]</h3>
<p>Draws the baseline of the scale </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>drawTick()</code>, <code>drawLabel()</code></dl>
<p> Implements <code>QwtAbstractScaleDraw</code>.</p>
<h3>void QwtRoundScaleDraw::drawLabel (QPainter *painter, doublevalue) const [protected], [virtual]</h3>
<p>Draws the label for a major scale tick </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>value</i> Value</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>drawTick()</code>, <code>drawBackbone()</code></dl>
<p> Implements <code>QwtAbstractScaleDraw</code>.</p>
<h3>void QwtRoundScaleDraw::drawTick (QPainter *painter, doublevalue, doublelen) const [protected], [virtual]</h3>
<p>Draw a tick </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>value</i> Value of the tick<br />
 <i>len</i> Lenght of the tick</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>drawBackbone()</code>, <code>drawLabel()</code></dl>
<p> Implements <code>QwtAbstractScaleDraw</code>.</p>
<h3>double QwtRoundScaleDraw::extent (const QFont &amp;font) const [virtual]</h3>
<p>Calculate the extent of the scale </p>
<p> The extent is the distance between the baseline to the outermost pixel of the scale draw. <code>radius()</code> + <code>extent()</code> is an upper limit for the radius of the bounding circle. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>font</i> Font used for painting the labels</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Calculated extent</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setMinimumExtent()</code>, <code>minimumExtent()</code></dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The implemented algorithm is not too smart and calculates only an upper limit, that might be a few pixels too large</dl>
<p> Implements <code>QwtAbstractScaleDraw</code>.</p>
<h3>void QwtRoundScaleDraw::moveCenter (const QPointF &amp;center)</h3>
<p>Move the center of the scale draw, leaving the radius unchanged </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>center</i> New center</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setRadius()</code></dl>
<h3>double QwtRoundScaleDraw::radius () const</h3>
<p>Get the radius </p>
<p> Radius is the radius of the backbone without ticks and labels. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Radius of the scale</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setRadius()</code>, <code>extent()</code></dl>
<h3>void QwtRoundScaleDraw::setAngleRange (doubleangle1, doubleangle2)</h3>
<p>Adjust the baseline circle segment for round scales. The baseline will be drawn from min(angle1,angle2) to max(angle1, angle2). The default setting is [ -135, 135 ]. An angle of 0 degrees corresponds to the 12 o&#8217;clock position, and positive angles count in a clockwise direction. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>angle1</i><br />
 <i>angle2</i> boundaries of the angle interval in degrees.</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&bull;</p>
<dd>The angle range is limited to [-360, 360] degrees. Angles exceeding this range will be clipped.</p>
<dt>&bull;</p>
<dd>For angles more or equal than 360 degrees above or below min(angle1, angle2), scale marks will not be drawn.</p>
<dt>&bull;</p>
<dd>If you need a counterclockwise scale, use <code>QwtScaleDiv::setInterval()</code></dl>
</dl>
<h3>void QwtRoundScaleDraw::setRadius (doubleradius)</h3>
<p>Change of radius the scale </p>
<p> Radius is the radius of the backbone without ticks and labels. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>radius</i> New Radius</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>moveCenter()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
