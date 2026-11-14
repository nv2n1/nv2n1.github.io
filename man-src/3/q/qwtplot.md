---
title: "qwtplot(3)"
name: "qwtplot"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtplot/"
description: "QwtPlot –"
---

<p>QwtPlot &#8211; </p>
<p> A 2-D plotting widget.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_plot.h&gt; </p>
<p> Inherits QFrame, and <code>QwtPlotDict</code>.</p>
<h3>Public Types</h3>
<p>enum <code>Axis</code> { <code>yLeft</code>, <code>yRight</code>, <code>xBottom</code>, <code>xTop</code>, <code>axisCnt</code> }<br />
 <i>Axis index. </i><br />
 enum <code>LegendPosition</code> { <code>LeftLegend</code>, <code>RightLegend</code>, <code>BottomLegend</code>, <code>TopLegend</code> } </p>
<h3>Public Slots</h3>
<p>virtual void <code>replot</code> ()<br />
 <i>Redraw the plot. </i><br />
 void <code>autoRefresh</code> ()<br />
 <i>Replots the plot if </i><code>autoReplot()</code> is true.</p>
<h3>Signals</h3>
<p>void <code>itemAttached</code> (<code>QwtPlotItem</code> *plotItem, bool on) </p>
<p> void <code>legendDataChanged</code> (const QVariant &amp;itemInfo, const QList&lt; <code>QwtLegendData</code> &gt; &amp;data) </p>
<h3>Public Member Functions</h3>
<p><code>QwtPlot</code> (QWidget *=NULL)<br />
 <i>Constructor. </i><br />
 <code>QwtPlot</code> (const <code>QwtText</code> &amp;<code>title</code>, QWidget *=NULL)<br />
 <i>Constructor. </i><br />
 virtual <code>~QwtPlot</code> ()<br />
 <i>Destructor. </i><br />
 void <code>applyProperties</code> (const QString &amp;) </p>
<p> QString <code>grabProperties</code> () const </p>
<p> void <code>setAutoReplot</code> (bool=true)<br />
 <i>Set or reset the autoReplot option. </i><br />
 bool <code>autoReplot</code> () const </p>
<p> void <code>setPlotLayout</code> (<code>QwtPlotLayout</code> *)<br />
 <i>Assign a new plot layout. </i><br />
 <code>QwtPlotLayout</code> * <code>plotLayout</code> () </p>
<p> const <code>QwtPlotLayout</code> * <code>plotLayout</code> () const </p>
<p> void <code>setTitle</code> (const QString &amp;) </p>
<p> void <code>setTitle</code> (const <code>QwtText</code> &amp;t) </p>
<p> <code>QwtText</code> <code>title</code> () const </p>
<p> <code>QwtTextLabel</code> * <code>titleLabel</code> () </p>
<p> const <code>QwtTextLabel</code> * <code>titleLabel</code> () const </p>
<p> void <code>setFooter</code> (const QString &amp;) </p>
<p> void <code>setFooter</code> (const <code>QwtText</code> &amp;t) </p>
<p> <code>QwtText</code> <code>footer</code> () const </p>
<p> <code>QwtTextLabel</code> * <code>footerLabel</code> () </p>
<p> const <code>QwtTextLabel</code> * <code>footerLabel</code> () const </p>
<p> void <code>setCanvas</code> (QWidget *)<br />
 <i>Set the drawing canvas of the plot widget. </i><br />
 QWidget * <code>canvas</code> () </p>
<p> const QWidget * <code>canvas</code> () const </p>
<p> void <code>setCanvasBackground</code> (const QBrush &amp;)<br />
 <i>Change the background of the plotting area. </i><br />
 QBrush <code>canvasBackground</code> () const </p>
<p> virtual <code>QwtScaleMap</code> <code>canvasMap</code> (int axisId) const </p>
<p> double <code>invTransform</code> (int axisId, int pos) const </p>
<p> double <code>transform</code> (int axisId, double value) const<br />
 <i>Transform a value into a coordinate in the plotting region. </i><br />
 <code>QwtScaleEngine</code> * <code>axisScaleEngine</code> (int axisId) </p>
<p> const <code>QwtScaleEngine</code> * <code>axisScaleEngine</code> (int axisId) const </p>
<p> void <code>setAxisScaleEngine</code> (int axisId, <code>QwtScaleEngine</code> *) </p>
<p> void <code>setAxisAutoScale</code> (int axisId, bool on=true)<br />
 <i>Enable autoscaling for a specified axis. </i><br />
 bool <code>axisAutoScale</code> (int axisId) const </p>
<p> void <code>enableAxis</code> (int axisId, bool tf=true)<br />
 <i>Enable or disable a specified axis. </i><br />
 bool <code>axisEnabled</code> (int axisId) const </p>
<p> void <code>setAxisFont</code> (int axisId, const QFont &amp;f)<br />
 <i>Change the font of an axis. </i><br />
 QFont <code>axisFont</code> (int axisId) const </p>
<p> void <code>setAxisScale</code> (int axisId, double min, double max, double step=0)<br />
 <i>Disable autoscaling and specify a fixed scale for a selected axis. </i><br />
 void <code>setAxisScaleDiv</code> (int axisId, const <code>QwtScaleDiv</code> &amp;)<br />
 <i>Disable autoscaling and specify a fixed scale for a selected axis. </i><br />
 void <code>setAxisScaleDraw</code> (int axisId, <code>QwtScaleDraw</code> *)<br />
 <i>Set a scale draw. </i><br />
 double <code>axisStepSize</code> (int axisId) const<br />
 <i>Return the step size parameter that has been set in setAxisScale. </i><br />
 <code>QwtInterval</code> <code>axisInterval</code> (int axisId) const<br />
 <i>Return the current interval of the specified axis. </i><br />
 const <code>QwtScaleDiv</code> &amp; <code>axisScaleDiv</code> (int axisId) const<br />
 <i>Return the scale division of a specified axis. </i><br />
 const <code>QwtScaleDraw</code> * <code>axisScaleDraw</code> (int axisId) const<br />
 <i>Return the scale draw of a specified axis. </i><br />
 <code>QwtScaleDraw</code> * <code>axisScaleDraw</code> (int axisId)<br />
 <i>Return the scale draw of a specified axis. </i><br />
 const <code>QwtScaleWidget</code> * <code>axisWidget</code> (int axisId) const </p>
<p> <code>QwtScaleWidget</code> * <code>axisWidget</code> (int axisId) </p>
<p> void <code>setAxisLabelAlignment</code> (int axisId, Qt::Alignment) </p>
<p> void <code>setAxisLabelRotation</code> (int axisId, double rotation) </p>
<p> void <code>setAxisTitle</code> (int axisId, const QString &amp;)<br />
 <i>Change the title of a specified axis. </i><br />
 void <code>setAxisTitle</code> (int axisId, const <code>QwtText</code> &amp;)<br />
 <i>Change the title of a specified axis. </i><br />
 <code>QwtText</code> <code>axisTitle</code> (int axisId) const </p>
<p> void <code>setAxisMaxMinor</code> (int axisId, int maxMinor) </p>
<p> int <code>axisMaxMinor</code> (int axisId) const </p>
<p> void <code>setAxisMaxMajor</code> (int axisId, int maxMajor) </p>
<p> int <code>axisMaxMajor</code> (int axisId) const </p>
<p> void <code>insertLegend</code> (<code>QwtAbstractLegend</code> *, <code>LegendPosition</code>=<code>QwtPlot::RightLegend</code>, double ratio=-1.0)<br />
 <i>Insert a legend. </i><br />
 <code>QwtAbstractLegend</code> * <code>legend</code> () </p>
<p> const <code>QwtAbstractLegend</code> * <code>legend</code> () const </p>
<p> void <code>updateLegend</code> () </p>
<p> void <code>updateLegend</code> (const <code>QwtPlotItem</code> *) </p>
<p> virtual QSize <code>sizeHint</code> () const </p>
<p> virtual QSize <code>minimumSizeHint</code> () const<br />
 <i>Return a minimum size hint. </i><br />
 virtual void <code>updateLayout</code> ()<br />
 <i>Adjust plot content to its current size. </i><br />
 virtual void <code>drawCanvas</code> (QPainter *) </p>
<p> void <code>updateAxes</code> ()<br />
 <i>Rebuild the axes scales. </i><br />
 void <code>updateCanvasMargins</code> ()<br />
 <i>Update the canvas margins. </i><br />
 virtual void <code>getCanvasMarginsHint</code> (const <code>QwtScaleMap</code> maps[], const QRectF &amp;canvasRect, double &amp;left, double &amp;top, double &amp;right, double &amp;bottom) const<br />
 <i>Calculate the canvas margins. </i><br />
 virtual bool <code>event</code> (QEvent *)<br />
 <i>Adds handling of layout requests. </i><br />
 virtual bool <code>eventFilter</code> (QObject *, QEvent *)<br />
 <i>Event filter. </i><br />
 virtual void <code>drawItems</code> (QPainter *, const QRectF &amp;, const <code>QwtScaleMap</code> maps[<code>axisCnt</code>]) const </p>
<p> virtual QVariant <code>itemToInfo</code> (<code>QwtPlotItem</code> *) const<br />
 <i>Build an information, that can be used to identify a plot item on the legend. </i><br />
 virtual <code>QwtPlotItem</code> * <code>infoToItem</code> (const QVariant &amp;) const<br />
 <i>Identify the plot item according to an item info object, that has bee generated from </i><code>itemToInfo()</code>.</p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>resizeEvent</code> (QResizeEvent *e) </p>
<h3>Static Protected Member Functions</h3>
<p>static bool <code>axisValid</code> (int axisId) </p>
<h3>Friends</h3>
<p>class <code>QwtPlotItem</code> </p>
<h2>Detailed Description</h2>
<p>A 2-D plotting widget. </p>
<p> <code>QwtPlot</code> is a widget for plotting two-dimensional graphs. An unlimited number of plot items can be displayed on its canvas. Plot items might be curves (<code>QwtPlotCurve</code>), markers (<code>QwtPlotMarker</code>), the grid (<code>QwtPlotGrid</code>), or anything else derived from <code>QwtPlotItem</code>. A plot can have up to four axes, with each plot item attached to an x- and a y axis. The scales at the axes can be explicitly set (<code>QwtScaleDiv</code>), or are calculated from the plot items, using algorithms (<code>QwtScaleEngine</code>) which can be configured separately for each axis. </p>
<p> The simpleplot example is a good starting point to see how to set up a plot widget. </p>
<p> <code>Example</code></p>
<dl COMPACT>
<dd>The following example shows (schematically) the most simple way to use <code>QwtPlot</code>. By default, only the left and bottom axes are visible and their scales are computed automatically. </p>
<pre>#include &lt;qwt_plot.h&gt;
#include &lt;qwt_plot_curve.h&gt;
QwtPlot *myPlot = new QwtPlot(&quot;Two Curves&quot;, parent);
// add curves
QwtPlotCurve *curve1 = new QwtPlotCurve(&quot;Curve 1&quot;);
QwtPlotCurve *curve2 = new QwtPlotCurve(&quot;Curve 2&quot;);
// connect or copy the data to the curves
curve1-&gt;setData(...);
curve2-&gt;setData(...);
curve1-&gt;attach(myPlot);
curve2-&gt;attach(myPlot);
// finally, refresh the plot
myPlot-&gt;replot();</pre>
<p>&nbsp;<wbr></dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtPlot::Axis</code></h3>
<p>Axis index. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>yLeft </i></p>
<dd>Y axis left of the canvas.</p>
<dt><i>yRight </i></p>
<dd>Y axis right of the canvas.</p>
<dt><i>xBottom </i></p>
<dd>X axis below the canvas.</p>
<dt><i>xTop </i></p>
<dd>X axis above the canvas.</p>
<dt><i>axisCnt </i></p>
<dd>Number of axes.</dl>
<h3>enum <code>QwtPlot::LegendPosition</code></h3>
<p>Position of the legend, relative to the canvas. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>insertLegend()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>LeftLegend </i></p>
<dd>The legend will be left from the <code>QwtPlot::yLeft</code> axis.</p>
<dt><i>RightLegend </i></p>
<dd>The legend will be right from the <code>QwtPlot::yRight</code> axis.</p>
<dt><i>BottomLegend </i></p>
<dd>The legend will be below the footer.</p>
<dt><i>TopLegend </i></p>
<dd>The legend will be above the title.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPlot::QwtPlot (QWidget *parent = NULL) [explicit]</h3>
<p>Constructor. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>parent</i> Parent widget</dl>
<h3>QwtPlot::QwtPlot (const <code>QwtText</code> &amp;title, QWidget *parent = NULL) [explicit]</h3>
<p>Constructor. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>title</i> Title text<br />
 <i>parent</i> Parent widget</dl>
<h2>Member Function Documentation</h2>
<h3>void QwtPlot::applyProperties (const QString &amp;)</h3>
<p>This method is intended for manipulating the plot widget from a specific editor in the Qwt designer plugin. </p>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The plot editor has never been implemented.</dl>
<h3>bool QwtPlot::autoReplot () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>true if the autoReplot option is set.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setAutoReplot()</code></dl>
<h3>bool QwtPlot::axisAutoScale (intaxisId) const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, if autoscaling is enabled</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axisId</i> Axis index</dl>
<h3>bool QwtPlot::axisEnabled (intaxisId) const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, if a specified axis is enabled</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axisId</i> Axis index</dl>
<h3>QFont QwtPlot::axisFont (intaxisId) const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>The font of the scale labels for a specified axis</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axisId</i> Axis index</dl>
<h3><code>QwtInterval</code> QwtPlot::axisInterval (intaxisId) const</h3>
<p>Return the current interval of the specified axis. This is only a convenience function for axisScaleDiv( axisId )-&gt;interval(); </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axisId</i> Axis index</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Scale interval</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtScaleDiv</code>, <code>axisScaleDiv()</code></dl>
<h3>int QwtPlot::axisMaxMajor (intaxisId) const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>The maximum number of major ticks for a specified axis</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axisId</i> Axis index</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setAxisMaxMajor()</code>, <code>QwtScaleEngine::divideScale()</code></dl>
<h3>int QwtPlot::axisMaxMinor (intaxisId) const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the maximum number of minor ticks for a specified axis</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axisId</i> Axis index</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setAxisMaxMinor()</code>, <code>QwtScaleEngine::divideScale()</code></dl>
<h3>const <code>QwtScaleDiv</code> &amp; QwtPlot::axisScaleDiv (intaxisId) const</h3>
<p>Return the scale division of a specified axis. axisScaleDiv(axisId).lowerBound(), axisScaleDiv(axisId).upperBound() are the current limits of the axis scale. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axisId</i> Axis index</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Scale division</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtScaleDiv</code>, <code>setAxisScaleDiv()</code>, <code>QwtScaleEngine::divideScale()</code></dl>
<h3>const <code>QwtScaleDraw</code> * QwtPlot::axisScaleDraw (intaxisId) const</h3>
<p>Return the scale draw of a specified axis. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axisId</i> Axis index</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Specified scaleDraw for axis, or NULL if axis is invalid.</dl>
<h3><code>QwtScaleDraw</code> * QwtPlot::axisScaleDraw (intaxisId)</h3>
<p>Return the scale draw of a specified axis. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axisId</i> Axis index</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Specified scaleDraw for axis, or NULL if axis is invalid.</dl>
<h3><code>QwtScaleEngine</code> * QwtPlot::axisScaleEngine (intaxisId)</h3>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axisId</i> Axis index</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Scale engine for a specific axis</dl>
<h3>const <code>QwtScaleEngine</code> * QwtPlot::axisScaleEngine (intaxisId) const</h3>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axisId</i> Axis index</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Scale engine for a specific axis</dl>
<h3>double QwtPlot::axisStepSize (intaxisId) const</h3>
<p>Return the step size parameter that has been set in setAxisScale. This doesn&#8217;t need to be the step size of the current scale. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axisId</i> Axis index</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>step size parameter value</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setAxisScale()</code>, <code>QwtScaleEngine::divideScale()</code></dl>
<h3><code>QwtText</code> QwtPlot::axisTitle (intaxisId) const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Title of a specified axis</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axisId</i> Axis index</dl>
<h3>bool QwtPlot::axisValid (intaxisId) [static], [protected]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>true if the specified axis exists, otherwise false</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axisId</i> axis index</dl>
<h3>const <code>QwtScaleWidget</code> * QwtPlot::axisWidget (intaxisId) const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Scale widget of the specified axis, or NULL if axisId is invalid.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axisId</i> Axis index</dl>
<h3><code>QwtScaleWidget</code> * QwtPlot::axisWidget (intaxisId)</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Scale widget of the specified axis, or NULL if axisId is invalid.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axisId</i> Axis index</dl>
<h3>QWidget * QwtPlot::canvas ()</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the plot&#8217;s canvas</dl>
<h3>const QWidget * QwtPlot::canvas () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the plot&#8217;s canvas</dl>
<h3>QBrush QwtPlot::canvasBackground () const</h3>
<p>Nothing else than: <code>canvas()</code>-&gt;palette().brush( QPalette::Normal, QPalette::Window); </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Background brush of the plotting area.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setCanvasBackground()</code></dl>
<h3><code>QwtScaleMap</code> QwtPlot::canvasMap (intaxisId) const [virtual]</h3>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axisId</i> Axis</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Map for the axis on the canvas. With this map pixel coordinates can translated to plot coordinates and vice versa.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtScaleMap</code>, <code>transform()</code>, <code>invTransform()</code></dl>
<h3>void QwtPlot::drawCanvas (QPainter *painter) [virtual]</h3>
<p>Redraw the canvas. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter used for drawing</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>drawCanvas calls drawItems what is also used for printing. Applications that like to add individual plot items better overload <code>drawItems()</code></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>drawItems()</code></dl>
<h3>void QwtPlot::drawItems (QPainter *painter, const QRectF &amp;canvasRect, const <code>QwtScaleMap</code>maps[axisCnt]) const [virtual]</h3>
<p>Redraw the canvas items. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter used for drawing<br />
 <i>canvasRect</i> Bounding rectangle where to paint<br />
 <i>maps</i> <code>QwtPlot::axisCnt</code> maps, mapping between plot and paint device coordinates</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Usually canvasRect is contentsRect() of the plot canvas. Due to a bug in Qt this rectangle might be wrong for certain frame styles ( f.e QFrame::Box ) and it might be necessary to fix the margins manually using QWidget::setContentsMargins()</dl>
<h3>void QwtPlot::enableAxis (intaxisId, booltf = true)</h3>
<p>Enable or disable a specified axis. When an axis is disabled, this only means that it is not visible on the screen. Curves, markers and can be attached to disabled axes, and transformation of screen coordinates into values works as normal. </p>
<p> Only xBottom and yLeft are enabled by default. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axisId</i> Axis index<br />
 <i>tf</i> true (enabled) or false (disabled)</dl>
<h3>bool QwtPlot::event (QEvent *event) [virtual]</h3>
<p>Adds handling of layout requests. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Event</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>See QFrame::event()</dl>
<h3>bool QwtPlot::eventFilter (QObject *object, QEvent *event) [virtual]</h3>
<p>Event filter. The plot handles the following events for the canvas: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>QEvent::Resize The canvas margins might depend on its size</p>
<dt>&bull;</p>
<dd>QEvent::ContentsRectChange The layout needs to be recalculated</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>object</i> Object to be filtered<br />
 <i>event</i> Event</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>See QFrame::eventFilter()</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>updateCanvasMargins()</code>, <code>updateLayout()</code></dl>
<h3><code>QwtText</code> QwtPlot::footer () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Text of the footer</dl>
<h3><code>QwtTextLabel</code> * QwtPlot::footerLabel ()</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Footer label widget.</dl>
<h3>const <code>QwtTextLabel</code> * QwtPlot::footerLabel () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Footer label widget.</dl>
<h3>void QwtPlot::getCanvasMarginsHint (const <code>QwtScaleMap</code>maps[], const QRectF &amp;canvasRect, double &amp;left, double &amp;top, double &amp;right, double &amp;bottom) const [virtual]</h3>
<p>Calculate the canvas margins. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>maps</i> <code>QwtPlot::axisCnt</code> maps, mapping between plot and paint device coordinates<br />
 <i>canvasRect</i> Bounding rectangle where to paint<br />
 <i>left</i> Return parameter for the left margin<br />
 <i>top</i> Return parameter for the top margin<br />
 <i>right</i> Return parameter for the right margin<br />
 <i>bottom</i> Return parameter for the bottom margin</dl>
<p> Plot items might indicate, that they need some extra space at the borders of the canvas by the <code>QwtPlotItem::Margins</code> flag. </p>
<p> <code>updateCanvasMargins()</code>, <code>QwtPlotItem::getCanvasMarginHint()</code></p>
<h3>QString QwtPlot::grabProperties () const</h3>
<p>This method is intended for manipulating the plot widget from a specific editor in the Qwt designer plugin. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>QString::null</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The plot editor has never been implemented.</dl>
<h3><code>QwtPlotItem</code> * QwtPlot::infoToItem (const QVariant &amp;itemInfo) const [virtual]</h3>
<p>Identify the plot item according to an item info object, that has bee generated from <code>itemToInfo()</code>. The default implementation simply tries to unwrap a <code>QwtPlotItem</code> pointer: </p>
<pre>if ( itemInfo.canConvert&lt;QwtPlotItem *&gt;() )
 return qvariant_cast&lt;QwtPlotItem *&gt;( itemInfo );</pre>
<p>&nbsp;<wbr> </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>itemInfo</i> Plot item</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A plot item, when successful, otherwise a NULL pointer.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>itemToInfo()</code></dl>
<h3>void QwtPlot::insertLegend (<code>QwtAbstractLegend</code> *legend, <code>QwtPlot::LegendPosition</code>pos = <code>QwtPlot::RightLegend</code>, doubleratio = -1.0)</h3>
<p>Insert a legend. If the position legend is <code>QwtPlot::LeftLegend</code> or <code>QwtPlot::RightLegend</code> the legend will be organized in one column from top to down. Otherwise the legend items will be placed in a table with a best fit number of columns from left to right. </p>
<p> <code>insertLegend()</code> will set the plot widget as parent for the legend. The legend will be deleted in the destructor of the plot or when another legend is inserted. </p>
<p> Legends, that are not inserted into the layout of the plot widget need to connect to the <code>legendDataChanged()</code> signal. Calling <code>updateLegend()</code> initiates this signal for an initial update. When the application code wants to implement its own layout this also needs to be done for rendering plots to a document ( see <code>QwtPlotRenderer</code> ). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>legend</i> Legend<br />
 <i>pos</i> The legend&#8217;s position. For top/left position the number of columns will be limited to 1, otherwise it will be set to unlimited.<br />
 <i>ratio</i> Ratio between legend and the bounding rectangle of title, canvas and axes. The legend will be shrunk if it would need more space than the given ratio. The ratio is limited to ]0.0 .. 1.0]. In case of &lt;= 0.0 it will be reset to the default ratio. The default vertical/horizontal ratio is 0.33/0.5.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>legend()</code>, <code>QwtPlotLayout::legendPosition()</code>, <code>QwtPlotLayout::setLegendPosition()</code></dl>
<h3>double QwtPlot::invTransform (intaxisId, intpos) const</h3>
<p>Transform the x or y coordinate of a position in the drawing region into a value. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axisId</i> Axis index<br />
 <i>pos</i> position</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Position as axis coordinate</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The position can be an x or a y coordinate, depending on the specified axis.</dl>
<h3>void QwtPlot::itemAttached (<code>QwtPlotItem</code> *plotItem, boolon) [signal]</h3>
<p>A signal indicating, that an item has been attached/detached </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>plotItem</i> Plot item<br />
 <i>on</i> Attached/Detached</dl>
<h3>QVariant QwtPlot::itemToInfo (<code>QwtPlotItem</code> *plotItem) const [virtual]</h3>
<p>Build an information, that can be used to identify a plot item on the legend. The default implementation simply wraps the plot item into a QVariant object. When overloading <code>itemToInfo()</code> usually <code>infoToItem()</code> needs to reimplemeted too. </p>
<pre>QVariant itemInfo;
qVariantSetValue( itemInfo, plotItem );</pre>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>plotItem</i> Plot item</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Plot item embedded in a QVariant</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>infoToItem()</code></dl>
<h3><code>QwtAbstractLegend</code> * QwtPlot::legend ()</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the plot&#8217;s legend</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>insertLegend()</code></dl>
<h3>const <code>QwtAbstractLegend</code> * QwtPlot::legend () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the plot&#8217;s legend</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>insertLegend()</code></dl>
<h3>void QwtPlot::legendDataChanged (const QVariant &amp;itemInfo, const QList&lt; <code>QwtLegendData</code> &gt; &amp;data) [signal]</h3>
<p>A signal with the attributes how to update the legend entries for a plot item. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>itemInfo</i> Info about a plot item, build from <code>itemToInfo()</code><br />
 <i>data</i> Attributes of the entries ( usually &lt;= 1 ) for the plot item.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>itemToInfo()</code>, <code>infoToItem()</code>, <code>QwtAbstractLegend::updateLegend()</code></dl>
<h3><code>QwtPlotLayout</code> * QwtPlot::plotLayout ()</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the plot&#8217;s layout</dl>
<h3>const <code>QwtPlotLayout</code> * QwtPlot::plotLayout () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the plot&#8217;s layout</dl>
<h3>void QwtPlot::replot () [virtual], [slot]</h3>
<p>Redraw the plot. If the autoReplot option is not set (which is the default) or if any curves are attached to raw data, the plot has to be refreshed explicitly in order to make changes visible. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>updateAxes()</code>, <code>setAutoReplot()</code></dl>
<h3>void QwtPlot::resizeEvent (QResizeEvent *e) [protected], [virtual]</h3>
<p>Resize and update internal layout </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> Resize event</dl>
<h3>void QwtPlot::setAutoReplot (booltf = true)</h3>
<p>Set or reset the autoReplot option. If the autoReplot option is set, the plot will be updated implicitly by manipulating member functions. Since this may be time-consuming, it is recommended to leave this option switched off and call <code>replot()</code> explicitly if necessary. </p>
<p> The autoReplot option is set to false by default, which means that the user has to call <code>replot()</code> in order to make changes visible. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>tf</i> true or false. Defaults to true.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>replot()</code></dl>
<h3>void QwtPlot::setAxisAutoScale (intaxisId, boolon = true)</h3>
<p>Enable autoscaling for a specified axis. This member function is used to switch back to autoscaling mode after a fixed scale has been set. Autoscaling is enabled by default. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axisId</i> Axis index<br />
 <i>on</i> On/Off</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setAxisScale()</code>, <code>setAxisScaleDiv()</code>, <code>updateAxes()</code></dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The autoscaling flag has no effect until <code>updateAxes()</code> is executed ( called by <code>replot()</code> ).</dl>
<h3>void QwtPlot::setAxisFont (intaxisId, const QFont &amp;font)</h3>
<p>Change the font of an axis. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axisId</i> Axis index<br />
 <i>font</i> Font</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>This function changes the font of the tick labels, not of the axis title.</dl>
<h3>void QwtPlot::setAxisLabelAlignment (intaxisId, Qt::Alignmentalignment)</h3>
<p>Change the alignment of the tick labels </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axisId</i> Axis index<br />
 <i>alignment</i> Or&#8217;d Qt::AlignmentFlags see &lt;qnamespace.h&gt;</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtScaleDraw::setLabelAlignment()</code></dl>
<h3>void QwtPlot::setAxisLabelRotation (intaxisId, doublerotation)</h3>
<p>Rotate all tick labels </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axisId</i> Axis index<br />
 <i>rotation</i> Angle in degrees. When changing the label rotation, the label alignment might be adjusted too.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtScaleDraw::setLabelRotation()</code>, <code>setAxisLabelAlignment()</code></dl>
<h3>void QwtPlot::setAxisMaxMajor (intaxisId, intmaxMajor)</h3>
<p>Set the maximum number of major scale intervals for a specified axis </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axisId</i> Axis index<br />
 <i>maxMajor</i> Maximum number of major steps</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>axisMaxMajor()</code></dl>
<h3>void QwtPlot::setAxisMaxMinor (intaxisId, intmaxMinor)</h3>
<p>Set the maximum number of minor scale intervals for a specified axis </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axisId</i> Axis index<br />
 <i>maxMinor</i> Maximum number of minor steps</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>axisMaxMinor()</code></dl>
<h3>void QwtPlot::setAxisScale (intaxisId, doublemin, doublemax, doublestepSize = 0)</h3>
<p>Disable autoscaling and specify a fixed scale for a selected axis. In <code>updateAxes()</code> the scale engine calculates a scale division from the specified parameters, that will be assigned to the scale widget. So updates of the scale widget usually happen delayed with the next replot. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axisId</i> Axis index<br />
 <i>min</i> Minimum of the scale<br />
 <i>max</i> Maximum of the scale<br />
 <i>stepSize</i> Major step size. If step == 0, the step size is calculated automatically using the maxMajor setting.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setAxisMaxMajor()</code>, <code>setAxisAutoScale()</code>, <code>axisStepSize()</code>, <code>QwtScaleEngine::divideScale()</code></dl>
<h3>void QwtPlot::setAxisScaleDiv (intaxisId, const <code>QwtScaleDiv</code> &amp;scaleDiv)</h3>
<p>Disable autoscaling and specify a fixed scale for a selected axis. The scale division will be stored locally only until the next call of <code>updateAxes()</code>. So updates of the scale widget usually happen delayed with the next replot. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axisId</i> Axis index<br />
 <i>scaleDiv</i> Scale division</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setAxisScale()</code>, <code>setAxisAutoScale()</code></dl>
<h3>void QwtPlot::setAxisScaleDraw (intaxisId, <code>QwtScaleDraw</code> *scaleDraw)</h3>
<p>Set a scale draw. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axisId</i> Axis index<br />
 <i>scaleDraw</i> Object responsible for drawing scales.</dl>
<p> By passing scaleDraw it is possible to extend <code>QwtScaleDraw</code> functionality and let it take place in <code>QwtPlot</code>. Please note that scaleDraw has to be created with new and will be deleted by the corresponding QwtScale member ( like a child object ). </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtScaleDraw</code>, <code>QwtScaleWidget</code></dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The attributes of scaleDraw will be overwritten by those of the previous <code>QwtScaleDraw</code>.</dl>
<h3>void QwtPlot::setAxisScaleEngine (intaxisId, <code>QwtScaleEngine</code> *scaleEngine)</h3>
<p>Change the scale engine for an axis </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axisId</i> Axis index<br />
 <i>scaleEngine</i> Scale engine</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>axisScaleEngine()</code></dl>
<h3>void QwtPlot::setAxisTitle (intaxisId, const QString &amp;title)</h3>
<p>Change the title of a specified axis. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axisId</i> Axis index<br />
 <i>title</i> axis title</dl>
<h3>void QwtPlot::setAxisTitle (intaxisId, const <code>QwtText</code> &amp;title)</h3>
<p>Change the title of a specified axis. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axisId</i> Axis index<br />
 <i>title</i> Axis title</dl>
<h3>void QwtPlot::setCanvas (QWidget *canvas)</h3>
<p>Set the drawing canvas of the plot widget. <code>QwtPlot</code> invokes methods of the canvas as meta methods ( see QMetaObject ). In opposite to using conventional C++ techniques like virtual methods they allow to use canvas implementations that are derived from QWidget or QGLWidget. </p>
<p> The following meta methods could be implemented: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd><code>replot()</code> When the canvas doesn&#8217;t offer a replot method, <code>QwtPlot</code> calls update() instead.</p>
<dt>&bull;</p>
<dd>borderPath() The border path is necessary to clip the content of the canvas When the canvas doesn&#8217;t have any special border ( f.e rounded corners ) it is o.k. not to implement this method.</dl>
<p> The default canvas is a <code>QwtPlotCanvas</code> </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>canvas</i> Canvas Widget</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>canvas()</code></dl>
<h3>void QwtPlot::setCanvasBackground (const QBrush &amp;brush)</h3>
<p>Change the background of the plotting area. Sets brush to QPalette::Window of all color groups of the palette of the canvas. Using <code>canvas()</code>-&gt;setPalette() is a more powerful way to set these colors. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>brush</i> New background brush</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>canvasBackground()</code></dl>
<h3>void QwtPlot::setFooter (const QString &amp;text)</h3>
<p>Change the text the footer </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>text</i> New text of the footer</dl>
<h3>void QwtPlot::setFooter (const <code>QwtText</code> &amp;text)</h3>
<p>Change the text the footer </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>text</i> New text of the footer</dl>
<h3>void QwtPlot::setPlotLayout (<code>QwtPlotLayout</code> *layout)</h3>
<p>Assign a new plot layout. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>layout</i> Layout()</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>plotLayout()</code></dl>
<h3>void QwtPlot::setTitle (const QString &amp;title)</h3>
<p>Change the plot&#8217;s title </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>title</i> New title</dl>
<h3>void QwtPlot::setTitle (const <code>QwtText</code> &amp;title)</h3>
<p>Change the plot&#8217;s title </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>title</i> New title</dl>
<h3>QSize QwtPlot::sizeHint () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Size hint for the plot widget</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>minimumSizeHint()</code></dl>
<h3><code>QwtText</code> QwtPlot::title () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Title of the plot</dl>
<h3><code>QwtTextLabel</code> * QwtPlot::titleLabel ()</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Title label widget.</dl>
<h3>const <code>QwtTextLabel</code> * QwtPlot::titleLabel () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Title label widget.</dl>
<h3>double QwtPlot::transform (intaxisId, doublevalue) const</h3>
<p>Transform a value into a coordinate in the plotting region. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axisId</i> Axis index<br />
 <i>value</i> value</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>X or Y coordinate in the plotting region corresponding to the value.</dl>
<h3>void QwtPlot::updateAxes ()</h3>
<p>Rebuild the axes scales. In case of autoscaling the boundaries of a scale are calculated from the bounding rectangles of all plot items, having the <code>QwtPlotItem::AutoScale</code> flag enabled ( <code>QwtScaleEngine::autoScale()</code> ). Then a scale division is calculated ( QwtScaleEngine::didvideScale() ) and assigned to scale widget. </p>
<p> When the scale boundaries have been assigned with <code>setAxisScale()</code> a scale division is calculated ( QwtScaleEngine::didvideScale() ) for this interval and assigned to the scale widget. </p>
<p> When the scale has been set explicitly by <code>setAxisScaleDiv()</code> the locally stored scale division gets assigned to the scale widget. </p>
<p> The scale widget indicates modifications by emitting a <code>QwtScaleWidget::scaleDivChanged()</code> signal. </p>
<p> <code>updateAxes()</code> is usually called by <code>replot()</code>. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setAxisAutoScale()</code>, <code>setAxisScale()</code>, <code>setAxisScaleDiv()</code>, <code>replot()</code> <code>QwtPlotItem::boundingRect()</code></dl>
<h3>void QwtPlot::updateCanvasMargins ()</h3>
<p>Update the canvas margins. Plot items might indicate, that they need some extra space at the borders of the canvas by the <code>QwtPlotItem::Margins</code> flag. </p>
<p> <code>getCanvasMarginsHint()</code>, <code>QwtPlotItem::getCanvasMarginHint()</code></p>
<h3>void QwtPlot::updateLayout () [virtual]</h3>
<p>Adjust plot content to its current size. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>resizeEvent()</code></dl>
<h3>void QwtPlot::updateLegend ()</h3>
<p>Emit <code>legendDataChanged()</code> for all plot item </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlotItem::legendData()</code>, <code>legendDataChanged()</code></dl>
<h3>void QwtPlot::updateLegend (const <code>QwtPlotItem</code> *plotItem)</h3>
<p>Emit <code>legendDataChanged()</code> for a plot item </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>plotItem</i> Plot item</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlotItem::legendData()</code>, <code>legendDataChanged()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
