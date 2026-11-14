---
title: "qwtplotzoomer(3)"
name: "qwtplotzoomer"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtplotzoomer/"
description: "QwtPlotZoomer –"
---

<p>QwtPlotZoomer &#8211; </p>
<p> <code>QwtPlotZoomer</code> provides stacked zooming for a plot widget.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_plot_zoomer.h&gt; </p>
<p> Inherits <code>QwtPlotPicker</code>.</p>
<h3>Public Slots</h3>
<p>void <code>moveBy</code> (double x, double y) </p>
<p> virtual void <code>moveTo</code> (const QPointF &amp;) </p>
<p> virtual void <code>zoom</code> (const QRectF &amp;)<br />
 <i>Zoom in. </i><br />
 virtual void <code>zoom</code> (int up)<br />
 <i>Zoom in or out. </i></p>
<h3>Signals</h3>
<p>void <code>zoomed</code> (const QRectF &amp;rect) </p>
<h3>Public Member Functions</h3>
<p><code>QwtPlotZoomer</code> (QWidget *, bool doReplot=true)<br />
 <i>Create a zoomer for a plot canvas. </i><br />
 <code>QwtPlotZoomer</code> (int <code>xAxis</code>, int <code>yAxis</code>, QWidget *, bool doReplot=true)<br />
 <i>Create a zoomer for a plot canvas. </i><br />
 virtual void <code>setZoomBase</code> (bool doReplot=true) </p>
<p> virtual void <code>setZoomBase</code> (const QRectF &amp;)<br />
 <i>Set the initial size of the zoomer. </i><br />
 QRectF <code>zoomBase</code> () const </p>
<p> QRectF <code>zoomRect</code> () const </p>
<p> virtual void <code>setAxis</code> (int <code>xAxis</code>, int <code>yAxis</code>) </p>
<p> void <code>setMaxStackDepth</code> (int)<br />
 <i>Limit the number of recursive zoom operations to depth. </i><br />
 int <code>maxStackDepth</code> () const </p>
<p> const QStack&lt; QRectF &gt; &amp; <code>zoomStack</code> () const </p>
<p> void <code>setZoomStack</code> (const QStack&lt; QRectF &gt; &amp;, int <code>zoomRectIndex</code>=-1)<br />
 <i>Assign a zoom stack. </i><br />
 uint <code>zoomRectIndex</code> () const </p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>rescale</code> () </p>
<p> virtual QSizeF <code>minZoomSize</code> () const<br />
 <i>Limit zooming by a minimum rectangle. </i><br />
 virtual void <code>widgetMouseReleaseEvent</code> (QMouseEvent *) </p>
<p> virtual void <code>widgetKeyPressEvent</code> (QKeyEvent *) </p>
<p> virtual void <code>begin</code> () </p>
<p> virtual bool <code>end</code> (bool ok=true) </p>
<p> virtual bool <code>accept</code> (QPolygon &amp;) const<br />
 <i>Check and correct a selected rectangle. </i></p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p><code>QwtPlotZoomer</code> provides stacked zooming for a plot widget. </p>
<p> <code>QwtPlotZoomer</code> selects rectangles from user inputs ( mouse or keyboard ) translates them into plot coordinates and adjusts the axes to them. The selection is supported by a rubber band and optionally by displaying the coordinates of the current mouse position. </p>
<p> Zooming can be repeated as often as possible, limited only by <code>maxStackDepth()</code> or <code>minZoomSize()</code>. Each rectangle is pushed on a stack. </p>
<p> The default setting how to select rectangles is a <code>QwtPickerDragRectMachine</code> with the following bindings: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd><code>QwtEventPattern::MouseSelect1</code> </p>
<p>&nbsp;<wbr>The first point of the zoom rectangle is selected by a mouse press, the second point from the position, where the mouse is released.</p>
<dt>&bull;</p>
<dd><code>QwtEventPattern::KeySelect1</code> </p>
<p>&nbsp;<wbr>The first key press selects the first, the second key press selects the second point.</p>
<dt>&bull;</p>
<dd><code>QwtEventPattern::KeyAbort</code> </p>
<p>&nbsp;<wbr>Discard the selection in the state, where the first point is selected.</dl>
<p> To traverse the zoom stack the following bindings are used: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd><code>QwtEventPattern::MouseSelect3</code>, <code>QwtEventPattern::KeyUndo</code> </p>
<p>&nbsp;<wbr>Zoom out one position on the zoom stack</p>
<dt>&bull;</p>
<dd><code>QwtEventPattern::MouseSelect6</code>, <code>QwtEventPattern::KeyRedo</code> </p>
<p>&nbsp;<wbr>Zoom in one position on the zoom stack</p>
<dt>&bull;</p>
<dd><code>QwtEventPattern::MouseSelect2</code>, <code>QwtEventPattern::KeyHome</code> </p>
<p>&nbsp;<wbr>Zoom to the zoom base</dl>
<p> The <code>setKeyPattern()</code> and <code>setMousePattern()</code> functions can be used to configure the zoomer actions. The following example shows, how to configure the &#8216;I&#8217; and &#8216;O&#8217; keys for zooming in and out one position on the zoom stack. The &#8216;Home&#8217; key is used to &#8216;unzoom&#8217; the plot. </p>
<pre>zoomer = new QwtPlotZoomer( plot );
zoomer-&gt;setKeyPattern( QwtEventPattern::KeyRedo, Qt::Key_I, Qt::ShiftModifier );
zoomer-&gt;setKeyPattern( QwtEventPattern::KeyUndo, Qt::Key_O, Qt::ShiftModifier );
zoomer-&gt;setKeyPattern( QwtEventPattern::KeyHome, Qt::Key_Home );</pre>
<p><code>QwtPlotZoomer</code> is tailored for plots with one x and y axis, but it is allowed to attach a second <code>QwtPlotZoomer</code> ( without rubber band and tracker ) for the other axes. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The realtime example includes an derived zoomer class that adds scrollbars to the plot canvas.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlotPanner</code>, <code>QwtPlotMagnifier</code></dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPlotZoomer::QwtPlotZoomer (QWidget *canvas, booldoReplot = true) [explicit]</h3>
<p>Create a zoomer for a plot canvas. The zoomer is set to those x- and y-axis of the parent plot of the canvas that are enabled. If both or no x-axis are enabled, the picker is set to <code>QwtPlot::xBottom</code>. If both or no y-axis are enabled, it is set to <code>QwtPlot::yLeft</code>. </p>
<p> The zoomer is initialized with a <code>QwtPickerDragRectMachine</code>, the tracker mode is set to <code>QwtPicker::ActiveOnly</code> and the rubber band is set to <code>QwtPicker::RectRubberBand</code> </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>canvas</i> Plot canvas to observe, also the parent object<br />
 <i>doReplot</i> Call <code>QwtPlot::replot()</code> for the attached plot before initializing the zoomer with its scales. This might be necessary, when the plot is in a state with pending scale changes.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlot::autoReplot()</code>, <code>QwtPlot::replot()</code>, <code>setZoomBase()</code></dl>
<h3>QwtPlotZoomer::QwtPlotZoomer (intxAxis, intyAxis, QWidget *canvas, booldoReplot = true) [explicit]</h3>
<p>Create a zoomer for a plot canvas. The zoomer is initialized with a <code>QwtPickerDragRectMachine</code>, the tracker mode is set to <code>QwtPicker::ActiveOnly</code> and the rubber band is set to <code>QwtPicker</code>;;RectRubberBand </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>xAxis</i> X axis of the zoomer<br />
 <i>yAxis</i> Y axis of the zoomer<br />
 <i>canvas</i> Plot canvas to observe, also the parent object<br />
 <i>doReplot</i> Call <code>QwtPlot::replot()</code> for the attached plot before initializing the zoomer with its scales. This might be necessary, when the plot is in a state with pending scale changes.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlot::autoReplot()</code>, <code>QwtPlot::replot()</code>, <code>setZoomBase()</code></dl>
<h2>Member Function Documentation</h2>
<h3>bool QwtPlotZoomer::accept (QPolygon &amp;pa) const [protected], [virtual]</h3>
<p>Check and correct a selected rectangle. Reject rectangles with a height or width &lt; 2, otherwise expand the selected rectangle to a minimum size of 11&#215;11 and accept it. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true If the rectangle is accepted, or has been changed to an accepted one.</dl>
<p> Reimplemented from <code>QwtPicker</code>.</p>
<h3>void QwtPlotZoomer::begin () [protected], [virtual]</h3>
<p>Rejects selections, when the stack depth is too deep, or the zoomed rectangle is <code>minZoomSize()</code>. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>minZoomSize()</code>, <code>maxStackDepth()</code></dl>
<p> Reimplemented from <code>QwtPicker</code>.</p>
<h3>bool QwtPlotZoomer::end (boolok = true) [protected], [virtual]</h3>
<p>Expand the selected rectangle to <code>minZoomSize()</code> and zoom in if accepted. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ok</i> If true, complete the selection and emit selected signals otherwise discard the selection.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>accept()</code>, <code>minZoomSize()</code></dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>True if the selection has been accepted, false otherwise</dl>
<p> Reimplemented from <code>QwtPlotPicker</code>.</p>
<h3>int QwtPlotZoomer::maxStackDepth () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Maximal depth of the zoom stack.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setMaxStackDepth()</code></dl>
<h3>QSizeF QwtPlotZoomer::minZoomSize () const [protected], [virtual]</h3>
<p>Limit zooming by a minimum rectangle. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd><code>zoomBase()</code>.width() / 10e4, <code>zoomBase()</code>.height() / 10e4</dl>
<h3>void QwtPlotZoomer::moveBy (doubledx, doubledy) [slot]</h3>
<p>Move the current zoom rectangle. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dx</i> X offset<br />
 <i>dy</i> Y offset</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The changed rectangle is limited by the zoom base</dl>
<h3>void QwtPlotZoomer::moveTo (const QPointF &amp;pos) [virtual], [slot]</h3>
<p>Move the the current zoom rectangle. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pos</i> New position</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>QRectF::moveTo()</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The changed rectangle is limited by the zoom base</dl>
<h3>void QwtPlotZoomer::rescale () [protected], [virtual]</h3>
<p>Adjust the observed plot to <code>zoomRect()</code> </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Initiates <code>QwtPlot::replot()</code></dl>
<h3>void QwtPlotZoomer::setAxis (intxAxis, intyAxis) [virtual]</h3>
<p>Reinitialize the axes, and set the zoom base to their scales. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>xAxis</i> X axis<br />
 <i>yAxis</i> Y axis</dl>
<p> Reimplemented from <code>QwtPlotPicker</code>.</p>
<h3>void QwtPlotZoomer::setMaxStackDepth (intdepth)</h3>
<p>Limit the number of recursive zoom operations to depth. A value of -1 set the depth to unlimited, 0 disables zooming. If the current zoom rectangle is below depth, the plot is unzoomed. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>depth</i> Maximum for the stack depth</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>maxStackDepth()</code></dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>depth doesn&#8217;t include the zoom base, so <code>zoomStack()</code>.count() might be <code>maxStackDepth()</code> + 1.</dl>
<h3>void QwtPlotZoomer::setZoomBase (booldoReplot = true) [virtual]</h3>
<p>Reinitialized the zoom stack with <code>scaleRect()</code> as base. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>doReplot</i> Call <code>QwtPlot::replot()</code> for the attached plot before initializing the zoomer with its scales. This might be necessary, when the plot is in a state with pending scale changes.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>zoomBase()</code>, <code>scaleRect()</code> <code>QwtPlot::autoReplot()</code>, <code>QwtPlot::replot()</code>.</dl>
<h3>void QwtPlotZoomer::setZoomBase (const QRectF &amp;base) [virtual]</h3>
<p>Set the initial size of the zoomer. base is united with the current <code>scaleRect()</code> and the zoom stack is reinitialized with it as zoom base. plot is zoomed to <code>scaleRect()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>base</i> Zoom base</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>zoomBase()</code>, <code>scaleRect()</code></dl>
<h3>void QwtPlotZoomer::setZoomStack (const QStack&lt; QRectF &gt; &amp;zoomStack, intzoomRectIndex = -1)</h3>
<p>Assign a zoom stack. In combination with other types of navigation it might be useful to modify to manipulate the complete zoom stack. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>zoomStack</i> New zoom stack<br />
 <i>zoomRectIndex</i> Index of the current position of zoom stack. In case of -1 the current position is at the top of the stack.</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The zoomed signal might be emitted.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>zoomStack()</code>, <code>zoomRectIndex()</code></dl>
<h3>void QwtPlotZoomer::widgetKeyPressEvent (QKeyEvent *ke) [protected], [virtual]</h3>
<p>Qt::Key_Plus zooms in, Qt::Key_Minus zooms out one position on the zoom stack, Qt::Key_Escape zooms out to the zoom base. </p>
<p> Changes the current position on the stack, but doesn&#8217;t pop any rectangle. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The keys codes can be changed, using <code>QwtEventPattern::setKeyPattern</code>: 3, 4, 5</dl>
<p> Reimplemented from <code>QwtPicker</code>.</p>
<h3>void QwtPlotZoomer::widgetMouseReleaseEvent (QMouseEvent *me) [protected], [virtual]</h3>
<p>Qt::MidButton zooms out one position on the zoom stack, Qt::RightButton to the zoom base. </p>
<p> Changes the current position on the stack, but doesn&#8217;t pop any rectangle. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The mouse events can be changed, using <code>QwtEventPattern::setMousePattern</code>: 2, 1</dl>
<p> Reimplemented from <code>QwtPicker</code>.</p>
<h3>void QwtPlotZoomer::zoom (const QRectF &amp;rect) [virtual], [slot]</h3>
<p>Zoom in. Clears all rectangles above the current position of the zoom stack and pushes the normalized rectangle on it. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>If the maximal stack depth is reached, zoom is ignored. </p>
<p> The zoomed signal is emitted.</dl>
<h3>void QwtPlotZoomer::zoom (intoffset) [virtual], [slot]</h3>
<p>Zoom in or out. Activate a rectangle on the zoom stack with an offset relative to the current position. Negative values of offset will zoom out, positive zoom in. A value of 0 zooms out to the zoom base. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>offset</i> Offset relative to the current position of the zoom stack.</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The zoomed signal is emitted.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>zoomRectIndex()</code></dl>
<h3>QRectF QwtPlotZoomer::zoomBase () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Initial rectangle of the zoomer</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setZoomBase()</code>, <code>zoomRect()</code></dl>
<h3>void QwtPlotZoomer::zoomed (const QRectF &amp;rect) [signal]</h3>
<p>A signal emitting the <code>zoomRect()</code>, when the plot has been zoomed in or out. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rect</i> Current zoom rectangle.</dl>
<h3>QRectF QwtPlotZoomer::zoomRect () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Rectangle at the current position on the zoom stack.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>zoomRectIndex()</code>, <code>scaleRect()</code>.</dl>
<h3>uint QwtPlotZoomer::zoomRectIndex () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Index of current position of zoom stack.</dl>
<h3>const QStack&lt; QRectF &gt; &amp; QwtPlotZoomer::zoomStack () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>The zoom stack. <code>zoomStack()</code>[0] is the zoom base, <code>zoomStack()</code>[1] the first zoomed rectangle.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setZoomStack()</code>, <code>zoomRectIndex()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
