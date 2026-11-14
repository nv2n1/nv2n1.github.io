---
title: "qwtplotgrid(3)"
name: "qwtplotgrid"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtplotgrid/"
description: "QwtPlotGrid –"
---

<p>QwtPlotGrid &#8211; </p>
<p> A class which draws a coordinate grid.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_plot_grid.h&gt; </p>
<p> Inherits <code>QwtPlotItem</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtPlotGrid</code> ()<br />
 <i>Enables major grid, disables minor grid. </i><br />
 virtual <code>~QwtPlotGrid</code> ()<br />
 <i>Destructor. </i><br />
 virtual int <code>rtti</code> () const </p>
<p> void <code>enableX</code> (bool tf)<br />
 <i>Enable or disable vertical grid lines. </i><br />
 bool <code>xEnabled</code> () const </p>
<p> void <code>enableY</code> (bool tf)<br />
 <i>Enable or disable horizontal grid lines. </i><br />
 bool <code>yEnabled</code> () const </p>
<p> void <code>enableXMin</code> (bool tf)<br />
 <i>Enable or disable minor vertical grid lines. </i><br />
 bool <code>xMinEnabled</code> () const </p>
<p> void <code>enableYMin</code> (bool tf)<br />
 <i>Enable or disable minor horizontal grid lines. </i><br />
 bool <code>yMinEnabled</code> () const </p>
<p> void <code>setXDiv</code> (const <code>QwtScaleDiv</code> &amp;sx) </p>
<p> const <code>QwtScaleDiv</code> &amp; <code>xScaleDiv</code> () const </p>
<p> void <code>setYDiv</code> (const <code>QwtScaleDiv</code> &amp;sy) </p>
<p> const <code>QwtScaleDiv</code> &amp; <code>yScaleDiv</code> () const </p>
<p> void <code>setPen</code> (const QColor &amp;, qreal width=0.0, Qt::PenStyle=Qt::SolidLine) </p>
<p> void <code>setPen</code> (const QPen &amp;) </p>
<p> void <code>setMajorPen</code> (const QColor &amp;, qreal width=0.0, Qt::PenStyle=Qt::SolidLine) </p>
<p> void <code>setMajorPen</code> (const QPen &amp;) </p>
<p> const QPen &amp; <code>majorPen</code> () const </p>
<p> void <code>setMinorPen</code> (const QColor &amp;, qreal width=0.0, Qt::PenStyle=Qt::SolidLine) </p>
<p> void <code>setMinorPen</code> (const QPen &amp;p) </p>
<p> const QPen &amp; <code>minorPen</code> () const </p>
<p> virtual void <code>draw</code> (QPainter *p, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;rect) const<br />
 <i>Draw the grid. </i><br />
 virtual void <code>updateScaleDiv</code> (const <code>QwtScaleDiv</code> &amp;xMap, const <code>QwtScaleDiv</code> &amp;yMap) </p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p>A class which draws a coordinate grid. </p>
<p> The <code>QwtPlotGrid</code> class can be used to draw a coordinate grid. A coordinate grid consists of major and minor vertical and horizontal grid lines. The locations of the grid lines are determined by the X and Y scale divisions which can be assigned with <code>setXDiv()</code> and <code>setYDiv()</code>. The <code>draw()</code> member draws the grid within a bounding rectangle.</p>
<h2>Member Function Documentation</h2>
<h3>void QwtPlotGrid::draw (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect) const [virtual]</h3>
<p>Draw the grid. The grid is drawn into the bounding rectangle such that grid lines begin and end at the rectangle&#8217;s borders. The X and Y maps are used to map the scale divisions into the drawing region screen. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>xMap</i> X axis map<br />
 <i>yMap</i> Y axis<br />
 <i>canvasRect</i> Contents rectangle of the plot canvas</dl>
<p> Implements <code>QwtPlotItem</code>.</p>
<h3>void QwtPlotGrid::enableX (boolon)</h3>
<p>Enable or disable vertical grid lines. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>on</i> Enable (true) or disable</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>Minor grid lines can be enabled or disabled with <code>enableXMin()</code></dl>
<h3>void QwtPlotGrid::enableXMin (boolon)</h3>
<p>Enable or disable minor vertical grid lines. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>on</i> Enable (true) or disable</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>enableX()</code></dl>
<h3>void QwtPlotGrid::enableY (boolon)</h3>
<p>Enable or disable horizontal grid lines. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>on</i> Enable (true) or disable</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>Minor grid lines can be enabled or disabled with <code>enableYMin()</code></dl>
<h3>void QwtPlotGrid::enableYMin (boolon)</h3>
<p>Enable or disable minor horizontal grid lines. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>on</i> Enable (true) or disable</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>enableY()</code></dl>
<h3>const QPen &amp; QwtPlotGrid::majorPen () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the pen for the major grid lines</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setMajorPen()</code>, <code>setMinorPen()</code>, <code>setPen()</code></dl>
<h3>const QPen &amp; QwtPlotGrid::minorPen () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the pen for the minor grid lines</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setMinorPen()</code>, <code>setMajorPen()</code>, <code>setPen()</code></dl>
<h3>int QwtPlotGrid::rtti () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd><code>QwtPlotItem::Rtti_PlotGrid</code></dl>
<p> Reimplemented from <code>QwtPlotItem</code>.</p>
<h3>void QwtPlotGrid::setMajorPen (const QColor &amp;color, qrealwidth = 0.0, Qt::PenStylestyle = Qt::SolidLine)</h3>
<p>Build and assign a pen for both major grid lines </p>
<p> In Qt5 the default pen width is 1.0 ( 0.0 in Qt4 ) what makes it non cosmetic ( see QPen::isCosmetic() ). This method has been introduced to hide this incompatibility. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>color</i> Pen color<br />
 <i>width</i> Pen width<br />
 <i>style</i> Pen style</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>pen(), brush()</dl>
<h3>void QwtPlotGrid::setMajorPen (const QPen &amp;pen)</h3>
<p>Assign a pen for the major grid lines </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pen</i> Pen</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>majorPen()</code>, <code>setMinorPen()</code>, <code>setPen()</code></dl>
<h3>void QwtPlotGrid::setMinorPen (const QColor &amp;color, qrealwidth = 0.0, Qt::PenStylestyle = Qt::SolidLine)</h3>
<p>Build and assign a pen for the minor grid lines </p>
<p> In Qt5 the default pen width is 1.0 ( 0.0 in Qt4 ) what makes it non cosmetic ( see QPen::isCosmetic() ). This method has been introduced to hide this incompatibility. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>color</i> Pen color<br />
 <i>width</i> Pen width<br />
 <i>style</i> Pen style</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>pen(), brush()</dl>
<h3>void QwtPlotGrid::setMinorPen (const QPen &amp;pen)</h3>
<p>Assign a pen for the minor grid lines </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pen</i> Pen</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>minorPen()</code>, <code>setMajorPen()</code>, <code>setPen()</code></dl>
<h3>void QwtPlotGrid::setPen (const QColor &amp;color, qrealwidth = 0.0, Qt::PenStylestyle = Qt::SolidLine)</h3>
<p>Build and assign a pen for both major and minor grid lines </p>
<p> In Qt5 the default pen width is 1.0 ( 0.0 in Qt4 ) what makes it non cosmetic ( see QPen::isCosmetic() ). This method has been introduced to hide this incompatibility. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>color</i> Pen color<br />
 <i>width</i> Pen width<br />
 <i>style</i> Pen style</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>pen(), brush()</dl>
<h3>void QwtPlotGrid::setPen (const QPen &amp;pen)</h3>
<p>Assign a pen for both major and minor grid lines </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pen</i> Pen</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setMajorPen()</code>, <code>setMinorPen()</code></dl>
<h3>void QwtPlotGrid::setXDiv (const <code>QwtScaleDiv</code> &amp;scaleDiv)</h3>
<p>Assign an x axis scale division </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>scaleDiv</i> Scale division</dl>
<h3>void QwtPlotGrid::setYDiv (const <code>QwtScaleDiv</code> &amp;scaleDiv)</h3>
<p>Assign a y axis division </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>scaleDiv</i> Scale division</dl>
<h3>void QwtPlotGrid::updateScaleDiv (const <code>QwtScaleDiv</code> &amp;xScaleDiv, const <code>QwtScaleDiv</code> &amp;yScaleDiv) [virtual]</h3>
<p>Update the grid to changes of the axes scale division </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>xScaleDiv</i> Scale division of the x-axis<br />
 <i>yScaleDiv</i> Scale division of the y-axis</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlot::updateAxes()</code></dl>
<p> Reimplemented from <code>QwtPlotItem</code>.</p>
<h3>bool QwtPlotGrid::xEnabled () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>true if vertical grid lines are enabled</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>enableX()</code></dl>
<h3>bool QwtPlotGrid::xMinEnabled () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>true if minor vertical grid lines are enabled</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>enableXMin()</code></dl>
<h3>const <code>QwtScaleDiv</code> &amp; QwtPlotGrid::xScaleDiv () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the scale division of the x axis</dl>
<h3>bool QwtPlotGrid::yEnabled () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>true if horizontal grid lines are enabled</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>enableY()</code></dl>
<h3>bool QwtPlotGrid::yMinEnabled () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>true if minor horizontal grid lines are enabled</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>enableYMin()</code></dl>
<h3>const <code>QwtScaleDiv</code> &amp; QwtPlotGrid::yScaleDiv () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the scale division of the y axis</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
