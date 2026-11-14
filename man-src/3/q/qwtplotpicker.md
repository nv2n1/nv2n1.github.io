---
title: "qwtplotpicker(3)"
name: "qwtplotpicker"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtplotpicker/"
description: "QwtPlotPicker –"
---

<p>QwtPlotPicker &#8211; </p>
<p> <code>QwtPlotPicker</code> provides selections on a plot canvas.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_plot_picker.h&gt; </p>
<p> Inherits <code>QwtPicker</code>. </p>
<p> Inherited by <code>QwtPlotZoomer</code>.</p>
<h3>Signals</h3>
<p>void <code>selected</code> (const QPointF &amp;pos) </p>
<p> void <code>selected</code> (const QRectF &amp;rect) </p>
<p> void <code>selected</code> (const QVector&lt; QPointF &gt; &amp;pa) </p>
<p> void <code>appended</code> (const QPointF &amp;pos) </p>
<p> void <code>moved</code> (const QPointF &amp;pos) </p>
<h3>Public Member Functions</h3>
<p><code>QwtPlotPicker</code> (QWidget *<code>canvas</code>)<br />
 <i>Create a plot picker. </i><br />
 virtual <code>~QwtPlotPicker</code> ()<br />
 <i>Destructor. </i><br />
 <code>QwtPlotPicker</code> (int <code>xAxis</code>, int <code>yAxis</code>, QWidget *) </p>
<p> <code>QwtPlotPicker</code> (int <code>xAxis</code>, int <code>yAxis</code>, <code>RubberBand</code> <code>rubberBand</code>, <code>DisplayMode</code> <code>trackerMode</code>, QWidget *) </p>
<p> virtual void <code>setAxis</code> (int <code>xAxis</code>, int <code>yAxis</code>) </p>
<p> int <code>xAxis</code> () const<br />
 <i>Return x axis. </i><br />
 int <code>yAxis</code> () const<br />
 <i>Return y axis. </i><br />
 <code>QwtPlot</code> * <code>plot</code> () </p>
<p> const <code>QwtPlot</code> * <code>plot</code> () const </p>
<p> QWidget * <code>canvas</code> () </p>
<p> const QWidget * <code>canvas</code> () const </p>
<h3>Protected Member Functions</h3>
<p>QRectF <code>scaleRect</code> () const </p>
<p> QRectF <code>invTransform</code> (const QRect &amp;) const </p>
<p> QRect <code>transform</code> (const QRectF &amp;) const </p>
<p> QPointF <code>invTransform</code> (const QPoint &amp;) const </p>
<p> QPoint <code>transform</code> (const QPointF &amp;) const </p>
<p> virtual <code>QwtText</code> <code>trackerText</code> (const QPoint &amp;) const </p>
<p> virtual <code>QwtText</code> <code>trackerTextF</code> (const QPointF &amp;) const<br />
 <i>Translate a position into a position string. </i><br />
 virtual void <code>move</code> (const QPoint &amp;) </p>
<p> virtual void <code>append</code> (const QPoint &amp;) </p>
<p> virtual bool <code>end</code> (bool ok=true) </p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p><code>QwtPlotPicker</code> provides selections on a plot canvas. </p>
<p> <code>QwtPlotPicker</code> is a <code>QwtPicker</code> tailored for selections on a plot canvas. It is set to a x-Axis and y-Axis and translates all pixel coordinates into this coordinate system.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPlotPicker::QwtPlotPicker (QWidget *canvas) [explicit]</h3>
<p>Create a plot picker. The picker is set to those x- and y-axis of the plot that are enabled. If both or no x-axis are enabled, the picker is set to <code>QwtPlot::xBottom</code>. If both or no y-axis are enabled, it is set to <code>QwtPlot::yLeft</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>canvas</i> Plot canvas to observe, also the parent object</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlot::autoReplot()</code>, <code>QwtPlot::replot()</code>, <code>scaleRect()</code></dl>
<h3>QwtPlotPicker::QwtPlotPicker (intxAxis, intyAxis, QWidget *canvas) [explicit]</h3>
<p>Create a plot picker </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>xAxis</i> Set the x axis of the picker<br />
 <i>yAxis</i> Set the y axis of the picker<br />
 <i>canvas</i> Plot canvas to observe, also the parent object</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlot::autoReplot()</code>, <code>QwtPlot::replot()</code>, <code>scaleRect()</code></dl>
<h3>QwtPlotPicker::QwtPlotPicker (intxAxis, intyAxis, <code>RubberBand</code>rubberBand, <code>DisplayMode</code>trackerMode, QWidget *canvas) [explicit]</h3>
<p>Create a plot picker </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>xAxis</i> X axis of the picker<br />
 <i>yAxis</i> Y axis of the picker<br />
 <i>rubberBand</i> Rubber band style<br />
 <i>trackerMode</i> Tracker mode<br />
 <i>canvas</i> Plot canvas to observe, also the parent object</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPicker</code>, QwtPicker::setSelectionFlags(), <code>QwtPicker::setRubberBand()</code>, <code>QwtPicker::setTrackerMode</code> </p>
<p> <code>QwtPlot::autoReplot()</code>, <code>QwtPlot::replot()</code>, <code>scaleRect()</code></dl>
<h2>Member Function Documentation</h2>
<h3>void QwtPlotPicker::append (const QPoint &amp;pos) [protected], [virtual]</h3>
<p>Append a point to the selection and update rubber band and tracker. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pos</i> Additional point</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isActive</code>, <code>begin()</code>, <code>end()</code>, <code>move()</code>, <code>appended()</code></dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The <code>appended(const QPoint &amp;)</code>, appended(const QDoublePoint &amp;) signals are emitted.</dl>
<p> Reimplemented from <code>QwtPicker</code>.</p>
<h3>void QwtPlotPicker::appended (const QPointF &amp;pos) [signal]</h3>
<p>A signal emitted when a point has been appended to the selection </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pos</i> Position of the appended point.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>append()</code>. <code>moved()</code></dl>
<h3>QWidget * QwtPlotPicker::canvas ()</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Observed plot canvas</dl>
<h3>const QWidget * QwtPlotPicker::canvas () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Observed plot canvas</dl>
<h3>bool QwtPlotPicker::end (boolok = true) [protected], [virtual]</h3>
<p>Close a selection setting the state to inactive. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ok</i> If true, complete the selection and emit selected signals otherwise discard the selection.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>True if the selection has been accepted, false otherwise</dl>
<p> Reimplemented from <code>QwtPicker</code>. </p>
<p> Reimplemented in <code>QwtPlotZoomer</code>.</p>
<h3>QRectF QwtPlotPicker::invTransform (const QRect &amp;rect) const [protected]</h3>
<p>Translate a rectangle from pixel into plot coordinates </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Rectangle in plot coordinates</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>transform()</code></dl>
<h3>QPointF QwtPlotPicker::invTransform (const QPoint &amp;pos) const [protected]</h3>
<p>Translate a point from pixel into plot coordinates </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Point in plot coordinates</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>transform()</code></dl>
<h3>void QwtPlotPicker::move (const QPoint &amp;pos) [protected], [virtual]</h3>
<p>Move the last point of the selection </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pos</i> New position</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isActive</code>, <code>begin()</code>, <code>end()</code>, <code>append()</code></dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The <code>moved(const QPoint &amp;)</code>, moved(const QDoublePoint &amp;) signals are emitted.</dl>
<p> Reimplemented from <code>QwtPicker</code>.</p>
<h3>void QwtPlotPicker::moved (const QPointF &amp;pos) [signal]</h3>
<p>A signal emitted whenever the last appended point of the selection has been moved. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pos</i> Position of the moved last point of the selection.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>move()</code>, <code>appended()</code></dl>
<h3><code>QwtPlot</code> * QwtPlotPicker::plot ()</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Plot widget, containing the observed plot canvas</dl>
<h3>const <code>QwtPlot</code> * QwtPlotPicker::plot () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Plot widget, containing the observed plot canvas</dl>
<h3>QRectF QwtPlotPicker::scaleRect () const [protected]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Normalized bounding rectangle of the axes</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlot::autoReplot()</code>, <code>QwtPlot::replot()</code>.</dl>
<h3>void QwtPlotPicker::selected (const QPointF &amp;pos) [signal]</h3>
<p>A signal emitted in case of <code>QwtPickerMachine::PointSelection</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pos</i> Selected point</dl>
<h3>void QwtPlotPicker::selected (const QRectF &amp;rect) [signal]</h3>
<p>A signal emitted in case of <code>QwtPickerMachine::RectSelection</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rect</i> Selected rectangle</dl>
<h3>void QwtPlotPicker::selected (const QVector&lt; QPointF &gt; &amp;pa) [signal]</h3>
<p>A signal emitting the selected points, at the end of a selection. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pa</i> Selected points</dl>
<h3>void QwtPlotPicker::setAxis (intxAxis, intyAxis) [virtual]</h3>
<p>Set the x and y axes of the picker </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>xAxis</i> X axis<br />
 <i>yAxis</i> Y axis</dl>
<p> Reimplemented in <code>QwtPlotZoomer</code>.</p>
<h3><code>QwtText</code> QwtPlotPicker::trackerText (const QPoint &amp;pos) const [protected], [virtual]</h3>
<p>Translate a pixel position into a position string </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pos</i> Position in pixel coordinates</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Position string</dl>
<p> Reimplemented from <code>QwtPicker</code>.</p>
<h3><code>QwtText</code> QwtPlotPicker::trackerTextF (const QPointF &amp;pos) const [protected], [virtual]</h3>
<p>Translate a position into a position string. In case of HLineRubberBand the label is the value of the y position, in case of VLineRubberBand the value of the x position. Otherwise the label contains x and y position separated by a &#8216;,&#8217; . </p>
<p> The format for the double to string conversion is &#8216;%.4f&#8217;. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pos</i> Position</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Position string</dl>
<h3>QRect QwtPlotPicker::transform (const QRectF &amp;rect) const [protected]</h3>
<p>Translate a rectangle from plot into pixel coordinates </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Rectangle in pixel coordinates</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>invTransform()</code></dl>
<h3>QPoint QwtPlotPicker::transform (const QPointF &amp;pos) const [protected]</h3>
<p>Translate a point from plot into pixel coordinates </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Point in pixel coordinates</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>invTransform()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
