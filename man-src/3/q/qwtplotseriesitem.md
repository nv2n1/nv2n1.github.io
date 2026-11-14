---
title: "qwtplotseriesitem(3)"
name: "qwtplotseriesitem"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtplotseriesitem/"
description: "QwtPlotSeriesItem –"
---

<p>QwtPlotSeriesItem &#8211; </p>
<p> Base class for plot items representing a series of samples.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_plot_seriesitem.h&gt; </p>
<p> Inherits <code>QwtPlotItem</code>, and <code>QwtAbstractSeriesStore</code>. </p>
<p> Inherited by <code>QwtPlotAbstractBarChart</code>, <code>QwtPlotCurve</code>, <code>QwtPlotHistogram</code>, <code>QwtPlotIntervalCurve</code>, <code>QwtPlotSpectroCurve</code>, and <code>QwtPlotTradingCurve</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtPlotSeriesItem</code> (const QString &amp;<code>title</code>=QString::null) </p>
<p> <code>QwtPlotSeriesItem</code> (const <code>QwtText</code> &amp;<code>title</code>) </p>
<p> virtual <code>~QwtPlotSeriesItem</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setOrientation</code> (Qt::Orientation) </p>
<p> Qt::Orientation <code>orientation</code> () const </p>
<p> virtual void <code>draw</code> (QPainter *p, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;) const<br />
 <i>Draw the complete series. </i><br />
 virtual void <code>drawSeries</code> (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, int from, int to) const =0 </p>
<p> virtual QRectF <code>boundingRect</code> () const </p>
<p> virtual void <code>updateScaleDiv</code> (const <code>QwtScaleDiv</code> &amp;, const <code>QwtScaleDiv</code> &amp;)<br />
 <i>Update the item to changes of the axes scale division. </i></p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>dataChanged</code> ()<br />
 <i></i><code>dataChanged()</code> indicates, that the series has been changed.</p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p>Base class for plot items representing a series of samples.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPlotSeriesItem::QwtPlotSeriesItem (const QString &amp;title = QString::null) [explicit]</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>title</i> Title of the curve</dl>
<h3>QwtPlotSeriesItem::QwtPlotSeriesItem (const <code>QwtText</code> &amp;title) [explicit]</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>title</i> Title of the curve</dl>
<h2>Member Function Documentation</h2>
<h3>QRectF QwtPlotSeriesItem::boundingRect () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>An invalid bounding rect: QRectF(1.0, 1.0, -2.0, -2.0)</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>A width or height &lt; 0.0 is ignored by the autoscaler</dl>
<p> Reimplemented from <code>QwtPlotItem</code>. </p>
<p> Reimplemented in <code>QwtPlotTradingCurve</code>, <code>QwtPlotIntervalCurve</code>, <code>QwtPlotHistogram</code>, <code>QwtPlotBarChart</code>, and <code>QwtPlotMultiBarChart</code>.</p>
<h3>void QwtPlotSeriesItem::draw (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect) const [virtual]</h3>
<p>Draw the complete series. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>xMap</i> Maps x-values into pixel coordinates.<br />
 <i>yMap</i> Maps y-values into pixel coordinates.<br />
 <i>canvasRect</i> Contents rectangle of the canvas</dl>
<p> Implements <code>QwtPlotItem</code>.</p>
<h3>virtual void QwtPlotSeriesItem::drawSeries (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, intfrom, intto) const [pure virtual]</h3>
<p>Draw a subset of the samples </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>xMap</i> Maps x-values into pixel coordinates.<br />
 <i>yMap</i> Maps y-values into pixel coordinates.<br />
 <i>canvasRect</i> Contents rectangle of the canvas<br />
 <i>from</i> Index of the first point to be painted<br />
 <i>to</i> Index of the last point to be painted. If to &lt; 0 the curve will be painted to its last point.</dl>
<p> Implemented in <code>QwtPlotCurve</code>, <code>QwtPlotTradingCurve</code>, <code>QwtPlotIntervalCurve</code>, <code>QwtPlotHistogram</code>, <code>QwtPlotBarChart</code>, <code>QwtPlotMultiBarChart</code>, and <code>QwtPlotSpectroCurve</code>.</p>
<h3>Qt::Orientation QwtPlotSeriesItem::orientation () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Orientation of the plot item</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setOrientation()</code></dl>
<h3>void QwtPlotSeriesItem::setOrientation (Qt::Orientationorientation)</h3>
<p>Set the orientation of the item. </p>
<p> The <code>orientation()</code> might be used in specific way by a plot item. F.e. a <code>QwtPlotCurve</code> uses it to identify how to display the curve int <code>QwtPlotCurve::Steps</code> or <code>QwtPlotCurve::Sticks</code> style. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>orientation()</code></dl>
<h3>void QwtPlotSeriesItem::updateScaleDiv (const <code>QwtScaleDiv</code> &amp;xScaleDiv, const <code>QwtScaleDiv</code> &amp;yScaleDiv) [virtual]</h3>
<p>Update the item to changes of the axes scale division. Update the item, when the axes of plot have changed. The default implementation does nothing, but items that depend on the scale division (like <code>QwtPlotGrid()</code>) have to reimplement <code>updateScaleDiv()</code> </p>
<p> <code>updateScaleDiv()</code> is only called when the ScaleInterest interest is enabled. The default implementation does nothing. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>xScaleDiv</i> Scale division of the x-axis<br />
 <i>yScaleDiv</i> Scale division of the y-axis</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlot::updateAxes()</code>, <code>ScaleInterest</code></dl>
<p> Reimplemented from <code>QwtPlotItem</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
