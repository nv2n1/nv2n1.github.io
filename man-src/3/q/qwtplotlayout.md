---
title: "qwtplotlayout(3)"
name: "qwtplotlayout"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtplotlayout/"
description: "QwtPlotLayout –"
---

<p>QwtPlotLayout &#8211; </p>
<p> Layout engine for <code>QwtPlot</code>.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_plot_layout.h&gt;</p>
<h3>Public Types</h3>
<p>enum <code>Option</code> { <code>AlignScales</code> = 0x01, <code>IgnoreScrollbars</code> = 0x02, <code>IgnoreFrames</code> = 0x04, <code>IgnoreLegend</code> = 0x08, <code>IgnoreTitle</code> = 0x10, <code>IgnoreFooter</code> = 0x20 } </p>
<p> typedef QFlags&lt; <code>Option</code> &gt; <code>Options</code><br />
 <i>Layout options. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtPlotLayout</code> ()<br />
 <i>Constructor. </i><br />
 virtual <code>~QwtPlotLayout</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setCanvasMargin</code> (int margin, int axis=-1) </p>
<p> int <code>canvasMargin</code> (int axis) const </p>
<p> void <code>setAlignCanvasToScales</code> (bool)<br />
 <i>Set the align-canvas-to-axis-scales flag for all axes. </i><br />
 void <code>setAlignCanvasToScale</code> (int axisId, bool) </p>
<p> bool <code>alignCanvasToScale</code> (int axisId) const </p>
<p> void <code>setSpacing</code> (int) </p>
<p> int <code>spacing</code> () const </p>
<p> void <code>setLegendPosition</code> (<code>QwtPlot::LegendPosition</code> pos, double ratio)<br />
 <i>Specify the position of the legend. </i><br />
 void <code>setLegendPosition</code> (<code>QwtPlot::LegendPosition</code> pos)<br />
 <i>Specify the position of the legend. </i><br />
 <code>QwtPlot::LegendPosition</code> <code>legendPosition</code> () const </p>
<p> void <code>setLegendRatio</code> (double ratio) </p>
<p> double <code>legendRatio</code> () const </p>
<p> virtual QSize <code>minimumSizeHint</code> (const <code>QwtPlot</code> *) const </p>
<p> virtual void <code>activate</code> (const <code>QwtPlot</code> *, const QRectF &amp;rect, <code>Options</code> options=0x00)<br />
 <i>Recalculate the geometry of all components. </i><br />
 virtual void <code>invalidate</code> () </p>
<p> QRectF <code>titleRect</code> () const </p>
<p> QRectF <code>footerRect</code> () const </p>
<p> QRectF <code>legendRect</code> () const </p>
<p> QRectF <code>scaleRect</code> (int axis) const </p>
<p> QRectF <code>canvasRect</code> () const </p>
<h3>Protected Member Functions</h3>
<p>void <code>setTitleRect</code> (const QRectF &amp;)<br />
 <i>Set the geometry for the title. </i><br />
 void <code>setFooterRect</code> (const QRectF &amp;)<br />
 <i>Set the geometry for the footer. </i><br />
 void <code>setLegendRect</code> (const QRectF &amp;)<br />
 <i>Set the geometry for the legend. </i><br />
 void <code>setScaleRect</code> (int axis, const QRectF &amp;)<br />
 <i>Set the geometry for an axis. </i><br />
 void <code>setCanvasRect</code> (const QRectF &amp;)<br />
 <i>Set the geometry for the canvas. </i><br />
 QRectF <code>layoutLegend</code> (<code>Options</code> options, const QRectF &amp;) const </p>
<p> QRectF <code>alignLegend</code> (const QRectF &amp;<code>canvasRect</code>, const QRectF &amp;<code>legendRect</code>) const </p>
<p> void <code>expandLineBreaks</code> (<code>Options</code> options, const QRectF &amp;rect, int &amp;dimTitle, int &amp;dimFooter, int dimAxes[<code>QwtPlot::axisCnt</code>]) const </p>
<p> void <code>alignScales</code> (<code>Options</code> options, QRectF &amp;<code>canvasRect</code>, QRectF <code>scaleRect</code>[<code>QwtPlot::axisCnt</code>]) const </p>
<h2>Detailed Description</h2>
<p>Layout engine for <code>QwtPlot</code>. </p>
<p> It is used by the <code>QwtPlot</code> widget to organize its internal widgets or by QwtPlot::print() to render its content to a QPaintDevice like a QPrinter, QPixmap/QImage or QSvgRenderer. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlot::setPlotLayout()</code></dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtPlotLayout::Option</code></h3>
<p>Options to configure the plot layout engine </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>activate()</code>, <code>QwtPlotRenderer</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>AlignScales </i></p>
<dd>Unused.</p>
<dt><i>IgnoreScrollbars </i></p>
<dd>Ignore the dimension of the scrollbars. There are no scrollbars, when the plot is not rendered to widgets.</p>
<dt><i>IgnoreFrames </i></p>
<dd>Ignore all frames.</p>
<dt><i>IgnoreLegend </i></p>
<dd>Ignore the legend.</p>
<dt><i>IgnoreTitle </i></p>
<dd>Ignore the title.</p>
<dt><i>IgnoreFooter </i></p>
<dd>Ignore the footer.</dl>
<h2>Member Function Documentation</h2>
<h3>void QwtPlotLayout::activate (const <code>QwtPlot</code> *plot, const QRectF &amp;plotRect, <code>Options</code>options = 0x00) [virtual]</h3>
<p>Recalculate the geometry of all components. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>plot</i> Plot to be layout<br />
 <i>plotRect</i> Rectangle where to place the components<br />
 <i>options</i> Layout options</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>invalidate()</code>, <code>titleRect()</code>, <code>footerRect()</code> <code>legendRect()</code>, <code>scaleRect()</code>, <code>canvasRect()</code></dl>
<h3>bool QwtPlotLayout::alignCanvasToScale (intaxisId) const</h3>
<p>Return the align-canvas-to-axis-scales setting. The canvas may:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>extend beyond the axis scale ends to maximize its size</p>
<dt>&bull;</p>
<dd>align with the axis scale ends to control its size.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axisId</i> Axis index</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>align-canvas-to-axis-scales setting</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setAlignCanvasToScale()</code>, <code>setAlignCanvasToScale()</code>, <code>setCanvasMargin()</code></dl>
<h3>QRectF QwtPlotLayout::alignLegend (const QRectF &amp;canvasRect, const QRectF &amp;legendRect) const [protected]</h3>
<p>Align the legend to the canvas </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>canvasRect</i> Geometry of the canvas<br />
 <i>legendRect</i> Maximum geometry for the legend</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Geometry for the aligned legend</dl>
<h3>void QwtPlotLayout::alignScales (<code>Options</code>options, QRectF &amp;canvasRect, QRectFscaleRect[QwtPlot::axisCnt]) const [protected]</h3>
<p>Align the ticks of the axis to the canvas borders using the empty corners. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>options</i> Layout options<br />
 <i>canvasRect</i> Geometry of the canvas ( IN/OUT )<br />
 <i>scaleRect</i> Geometries of the scales ( IN/OUT )</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>Options</code></dl>
<h3>int QwtPlotLayout::canvasMargin (intaxisId) const</h3>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axisId</i> Axis index</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Margin around the scale tick borders</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setCanvasMargin()</code></dl>
<h3>QRectF QwtPlotLayout::canvasRect () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Geometry for the canvas</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>activate()</code>, <code>invalidate()</code></dl>
<h3>void QwtPlotLayout::expandLineBreaks (<code>Options</code>options, const QRectF &amp;rect, int &amp;dimTitle, int &amp;dimFooter, intdimAxis[QwtPlot::axisCnt]) const [protected]</h3>
<p>Expand all line breaks in text labels, and calculate the height of their widgets in orientation of the text. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>options</i> Options how to layout the legend<br />
 <i>rect</i> Bounding rectangle for title, footer, axes and canvas.<br />
 <i>dimTitle</i> Expanded height of the title widget<br />
 <i>dimFooter</i> Expanded height of the footer widget<br />
 <i>dimAxis</i> Expanded heights of the axis in axis orientation.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>Options</code></dl>
<h3>QRectF QwtPlotLayout::footerRect () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Geometry for the footer</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>activate()</code>, <code>invalidate()</code></dl>
<h3>void QwtPlotLayout::invalidate () [virtual]</h3>
<p>Invalidate the geometry of all components. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>activate()</code></dl>
<h3>QRectF QwtPlotLayout::layoutLegend (<code>Options</code>options, const QRectF &amp;rect) const [protected]</h3>
<p>Find the geometry for the legend </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>options</i> Options how to layout the legend<br />
 <i>rect</i> Rectangle where to place the legend</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Geometry for the legend</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>Options</code></dl>
<h3><code>QwtPlot::LegendPosition</code> QwtPlotLayout::legendPosition () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Position of the legend</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLegendPosition()</code>, QwtPlot::setLegendPosition(), QwtPlot::legendPosition()</dl>
<h3>double QwtPlotLayout::legendRatio () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>The relative size of the legend in the plot.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLegendPosition()</code></dl>
<h3>QRectF QwtPlotLayout::legendRect () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Geometry for the legend</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>activate()</code>, <code>invalidate()</code></dl>
<h3>QSize QwtPlotLayout::minimumSizeHint (const <code>QwtPlot</code> *plot) const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Minimum size hint</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>plot</i> Plot widget</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlot::minimumSizeHint()</code></dl>
<h3>QRectF QwtPlotLayout::scaleRect (intaxis) const</h3>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axis</i> Axis index</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Geometry for the scale</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>activate()</code>, <code>invalidate()</code></dl>
<h3>void QwtPlotLayout::setAlignCanvasToScale (intaxisId, boolon)</h3>
<p>Change the align-canvas-to-axis-scales setting. The canvas may: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>extend beyond the axis scale ends to maximize its size,</p>
<dt>&bull;</p>
<dd>align with the axis scale ends to control its size.</dl>
<p> The axisId parameter is somehow confusing as it identifies a border of the plot and not the axes, that are aligned. F.e when <code>QwtPlot::yLeft</code> is set, the left end of the the x-axes ( <code>QwtPlot::xTop</code>, <code>QwtPlot::xBottom</code> ) is aligned. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axisId</i> Axis index<br />
 <i>on</i> New align-canvas-to-axis-scales setting</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setCanvasMargin()</code>, <code>alignCanvasToScale()</code>, <code>setAlignCanvasToScales()</code></dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>In case of on == true <code>canvasMargin()</code> will have no effect</dl>
<h3>void QwtPlotLayout::setAlignCanvasToScales (boolon)</h3>
<p>Set the align-canvas-to-axis-scales flag for all axes. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>on</i> True/False</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setAlignCanvasToScale()</code>, <code>alignCanvasToScale()</code></dl>
<h3>void QwtPlotLayout::setCanvasMargin (intmargin, intaxis = -1)</h3>
<p>Change a margin of the canvas. The margin is the space above/below the scale ticks. A negative margin will be set to -1, excluding the borders of the scales. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>margin</i> New margin<br />
 <i>axis</i> One of <code>QwtPlot::Axis</code>. Specifies where the position of the margin. -1 means margin at all borders.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>canvasMargin()</code></dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The margin will have no effect when <code>alignCanvasToScale()</code> is true</dl>
<h3>void QwtPlotLayout::setCanvasRect (const QRectF &amp;rect) [protected]</h3>
<p>Set the geometry for the canvas. This method is intended to be used from derived layouts overloading <code>activate()</code> </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>canvasRect()</code>, <code>activate()</code></dl>
<h3>void QwtPlotLayout::setFooterRect (const QRectF &amp;rect) [protected]</h3>
<p>Set the geometry for the footer. This method is intended to be used from derived layouts overloading <code>activate()</code> </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>footerRect()</code>, <code>activate()</code></dl>
<h3>void QwtPlotLayout::setLegendPosition (<code>QwtPlot::LegendPosition</code>pos, doubleratio)</h3>
<p>Specify the position of the legend. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pos</i> The legend&#8217;s position.<br />
 <i>ratio</i> Ratio between legend and the bounding rectangle of title, footer, canvas and axes. The legend will be shrunk if it would need more space than the given ratio. The ratio is limited to ]0.0 .. 1.0]. In case of &lt;= 0.0 it will be reset to the default ratio. The default vertical/horizontal ratio is 0.33/0.5.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>QwtPlot::setLegendPosition()</dl>
<h3>void QwtPlotLayout::setLegendPosition (<code>QwtPlot::LegendPosition</code>pos)</h3>
<p>Specify the position of the legend. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pos</i> The legend&#8217;s position. Valid values are <code>QwtPlot::LeftLegend</code>, <code>QwtPlot::RightLegend</code>, <code>QwtPlot::TopLegend</code>, <code>QwtPlot::BottomLegend</code>.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>QwtPlot::setLegendPosition()</dl>
<h3>void QwtPlotLayout::setLegendRatio (doubleratio)</h3>
<p>Specify the relative size of the legend in the plot </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ratio</i> Ratio between legend and the bounding rectangle of title, footer, canvas and axes. The legend will be shrunk if it would need more space than the given ratio. The ratio is limited to ]0.0 .. 1.0]. In case of &lt;= 0.0 it will be reset to the default ratio. The default vertical/horizontal ratio is 0.33/0.5.</dl>
<h3>void QwtPlotLayout::setLegendRect (const QRectF &amp;rect) [protected]</h3>
<p>Set the geometry for the legend. This method is intended to be used from derived layouts overloading <code>activate()</code> </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rect</i> Rectangle for the legend</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>legendRect()</code>, <code>activate()</code></dl>
<h3>void QwtPlotLayout::setScaleRect (intaxis, const QRectF &amp;rect) [protected]</h3>
<p>Set the geometry for an axis. This method is intended to be used from derived layouts overloading <code>activate()</code> </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axis</i> Axis index<br />
 <i>rect</i> Rectangle for the scale</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>scaleRect()</code>, <code>activate()</code></dl>
<h3>void QwtPlotLayout::setSpacing (intspacing)</h3>
<p>Change the spacing of the plot. The spacing is the distance between the plot components. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>spacing</i> New spacing</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setCanvasMargin()</code>, <code>spacing()</code></dl>
<h3>void QwtPlotLayout::setTitleRect (const QRectF &amp;rect) [protected]</h3>
<p>Set the geometry for the title. This method is intended to be used from derived layouts overloading <code>activate()</code> </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>titleRect()</code>, <code>activate()</code></dl>
<h3>int QwtPlotLayout::spacing () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Spacing</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>margin(), <code>setSpacing()</code></dl>
<h3>QRectF QwtPlotLayout::titleRect () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Geometry for the title</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>activate()</code>, <code>invalidate()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
