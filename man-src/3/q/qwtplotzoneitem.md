---
title: "qwtplotzoneitem(3)"
name: "qwtplotzoneitem"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtplotzoneitem/"
description: "QwtPlotZoneItem –"
---

<p>QwtPlotZoneItem &#8211; </p>
<p> A plot item, which displays a zone.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_plot_zoneitem.h&gt; </p>
<p> Inherits <code>QwtPlotItem</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtPlotZoneItem</code> ()<br />
 <i>Constructor. </i><br />
 virtual <code>~QwtPlotZoneItem</code> ()<br />
 <i>Destructor. </i><br />
 virtual int <code>rtti</code> () const </p>
<p> void <code>setOrientation</code> (Qt::Orientation)<br />
 <i>Set the orientation of the zone. </i><br />
 Qt::Orientation <code>orientation</code> () </p>
<p> void <code>setInterval</code> (double min, double max) </p>
<p> void <code>setInterval</code> (const <code>QwtInterval</code> &amp;) </p>
<p> <code>QwtInterval</code> <code>interval</code> () const </p>
<p> void <code>setPen</code> (const QColor &amp;, qreal width=0.0, Qt::PenStyle=Qt::SolidLine) </p>
<p> void <code>setPen</code> (const QPen &amp;)<br />
 <i>Assign a pen. </i><br />
 const QPen &amp; <code>pen</code> () const </p>
<p> void <code>setBrush</code> (const QBrush &amp;)<br />
 <i>Assign a brush. </i><br />
 const QBrush &amp; <code>brush</code> () const </p>
<p> virtual void <code>draw</code> (QPainter *, const <code>QwtScaleMap</code> &amp;, const <code>QwtScaleMap</code> &amp;, const QRectF &amp;) const </p>
<p> virtual QRectF <code>boundingRect</code> () const </p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p>A plot item, which displays a zone. </p>
<p> A horizontal zone highlights an interval of the y axis &#8211; a vertical zone an interval of the x axis &#8211; and is unbounded in the opposite direction. It is filled with a brush and its border lines are optionally displayed with a pen. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>For displaying an area that is bounded for x and y coordinates use <code>QwtPlotShapeItem</code></dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPlotZoneItem::QwtPlotZoneItem () [explicit]</h3>
<p>Constructor. Initializes the zone with no pen and a semi transparent gray brush </p>
<p> Sets the following item attributes: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd><code>QwtPlotItem::AutoScale</code>: false</p>
<dt>&bull;</p>
<dd><code>QwtPlotItem::Legend</code>: false</dl>
<p> The z value is initialized by 5 </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlotItem::setItemAttribute()</code>, <code>QwtPlotItem::setZ()</code></dl>
<h2>Member Function Documentation</h2>
<h3>QRectF QwtPlotZoneItem::boundingRect () const [virtual]</h3>
<p>The bounding rectangle is build from the interval in one direction and something invalid for the opposite direction. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An invalid rectangle with valid boundaries in one direction</dl>
<p> Reimplemented from <code>QwtPlotItem</code>.</p>
<h3>const QBrush &amp; QwtPlotZoneItem::brush () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Brush used to fill the zone</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPen()</code>, <code>brush()</code></dl>
<h3>void QwtPlotZoneItem::draw (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect) const [virtual]</h3>
<p>Draw the zone </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>xMap</i> x Scale Map<br />
 <i>yMap</i> y Scale Map<br />
 <i>canvasRect</i> Contents rectangle of the canvas in painter coordinates</dl>
<p> Implements <code>QwtPlotItem</code>.</p>
<h3><code>QwtInterval</code> QwtPlotZoneItem::interval () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Zone interval</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setInterval()</code>, <code>orientation()</code></dl>
<h3>Qt::Orientation QwtPlotZoneItem::orientation ()</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Orientation of the zone</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setOrientation()</code></dl>
<h3>const QPen &amp; QwtPlotZoneItem::pen () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Pen used to draw the border lines</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPen()</code>, <code>brush()</code></dl>
<h3>int QwtPlotZoneItem::rtti () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd><code>QwtPlotItem::Rtti_PlotZone</code></dl>
<p> Reimplemented from <code>QwtPlotItem</code>.</p>
<h3>void QwtPlotZoneItem::setBrush (const QBrush &amp;brush)</h3>
<p>Assign a brush. The brush is used to fill the zone </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>brush</i> Brush</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>pen()</code>, <code>setBrush()</code></dl>
<h3>void QwtPlotZoneItem::setInterval (doublemin, doublemax)</h3>
<p>Set the interval of the zone </p>
<p> For a horizontal zone the interval is related to the y axis, for a vertical zone it is related to the x axis. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>min</i> Minimum of the interval<br />
 <i>max</i> Maximum of the interval</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>interval()</code>, <code>setOrientation()</code></dl>
<h3>void QwtPlotZoneItem::setInterval (const <code>QwtInterval</code> &amp;interval)</h3>
<p>Set the interval of the zone </p>
<p> For a horizontal zone the interval is related to the y axis, for a vertical zone it is related to the x axis. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>interval</i> Zone interval</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>interval()</code>, <code>setOrientation()</code></dl>
<h3>void QwtPlotZoneItem::setOrientation (Qt::Orientationorientation)</h3>
<p>Set the orientation of the zone. A horizontal zone highlights an interval of the y axis, a vertical zone of the x axis. It is unbounded in the opposite direction. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>orientation()</code>, <code>QwtPlotItem::setAxes()</code></dl>
<h3>void QwtPlotZoneItem::setPen (const QColor &amp;color, qrealwidth = 0.0, Qt::PenStylestyle = Qt::SolidLine)</h3>
<p>Build and assign a pen </p>
<p> In Qt5 the default pen width is 1.0 ( 0.0 in Qt4 ) what makes it non cosmetic ( see QPen::isCosmetic() ). This method has been introduced to hide this incompatibility. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>color</i> Pen color<br />
 <i>width</i> Pen width<br />
 <i>style</i> Pen style</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>pen()</code>, <code>brush()</code></dl>
<h3>void QwtPlotZoneItem::setPen (const QPen &amp;pen)</h3>
<p>Assign a pen. The pen is used to draw the border lines of the zone </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pen</i> Pen</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>pen()</code>, <code>setBrush()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
