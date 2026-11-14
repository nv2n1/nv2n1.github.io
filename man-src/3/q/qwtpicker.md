---
title: "qwtpicker(3)"
name: "qwtpicker"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtpicker/"
description: "QwtPicker –"
---

<p>QwtPicker &#8211; </p>
<p> <code>QwtPicker</code> provides selections on a widget.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_picker.h&gt; </p>
<p> Inherits QObject, and <code>QwtEventPattern</code>. </p>
<p> Inherited by <code>QwtPlotPicker</code>.</p>
<h3>Public Types</h3>
<p>enum <code>RubberBand</code> { <code>NoRubberBand</code> = 0, <code>HLineRubberBand</code>, <code>VLineRubberBand</code>, <code>CrossRubberBand</code>, <code>RectRubberBand</code>, <code>EllipseRubberBand</code>, <code>PolygonRubberBand</code>, <code>UserRubberBand</code> = 100 } </p>
<p> enum <code>DisplayMode</code> { <code>AlwaysOff</code>, <code>AlwaysOn</code>, <code>ActiveOnly</code> }<br />
 <i>Display mode. </i><br />
 enum <code>ResizeMode</code> { <code>Stretch</code>, <code>KeepSize</code> } </p>
<h3>Public Slots</h3>
<p>void <code>setEnabled</code> (bool)<br />
 <i>En/disable the picker. </i></p>
<h3>Signals</h3>
<p>void <code>activated</code> (bool on) </p>
<p> void <code>selected</code> (const QPolygon &amp;polygon) </p>
<p> void <code>appended</code> (const QPoint &amp;pos) </p>
<p> void <code>moved</code> (const QPoint &amp;pos) </p>
<p> void <code>removed</code> (const QPoint &amp;pos) </p>
<p> void <code>changed</code> (const QPolygon &amp;<code>selection</code>) </p>
<h3>Public Member Functions</h3>
<p><code>QwtPicker</code> (QWidget *parent) </p>
<p> <code>QwtPicker</code> (<code>RubberBand</code> <code>rubberBand</code>, <code>DisplayMode</code> <code>trackerMode</code>, QWidget *) </p>
<p> virtual <code>~QwtPicker</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setStateMachine</code> (<code>QwtPickerMachine</code> *) </p>
<p> const <code>QwtPickerMachine</code> * <code>stateMachine</code> () const </p>
<p> <code>QwtPickerMachine</code> * <code>stateMachine</code> () </p>
<p> void <code>setRubberBand</code> (<code>RubberBand</code>) </p>
<p> <code>RubberBand</code> <code>rubberBand</code> () const </p>
<p> void <code>setTrackerMode</code> (<code>DisplayMode</code>)<br />
 <i>Set the display mode of the tracker. </i><br />
 <code>DisplayMode</code> <code>trackerMode</code> () const </p>
<p> void <code>setResizeMode</code> (<code>ResizeMode</code>)<br />
 <i>Set the resize mode. </i><br />
 <code>ResizeMode</code> <code>resizeMode</code> () const </p>
<p> void <code>setRubberBandPen</code> (const QPen &amp;) </p>
<p> QPen <code>rubberBandPen</code> () const </p>
<p> void <code>setTrackerPen</code> (const QPen &amp;) </p>
<p> QPen <code>trackerPen</code> () const </p>
<p> void <code>setTrackerFont</code> (const QFont &amp;) </p>
<p> QFont <code>trackerFont</code> () const </p>
<p> bool <code>isEnabled</code> () const </p>
<p> bool <code>isActive</code> () const </p>
<p> virtual bool <code>eventFilter</code> (QObject *, QEvent *)<br />
 <i>Event filter. </i><br />
 QWidget * <code>parentWidget</code> ()<br />
 <i>Return the parent widget, where the selection happens. </i><br />
 const QWidget * <code>parentWidget</code> () const<br />
 <i>Return the parent widget, where the selection happens. </i><br />
 virtual QPainterPath <code>pickArea</code> () const </p>
<p> virtual void <code>drawRubberBand</code> (QPainter *) const </p>
<p> virtual void <code>drawTracker</code> (QPainter *) const </p>
<p> virtual QRegion <code>rubberBandMask</code> () const </p>
<p> virtual <code>QwtText</code> <code>trackerText</code> (const QPoint &amp;pos) const<br />
 <i>Return the label for a position. </i><br />
 QPoint <code>trackerPosition</code> () const </p>
<p> virtual QRect <code>trackerRect</code> (const QFont &amp;) const </p>
<p> QPolygon <code>selection</code> () const </p>
<h3>Protected Member Functions</h3>
<p>virtual QPolygon <code>adjustedPoints</code> (const QPolygon &amp;) const<br />
 <i>Map the </i><code>pickedPoints()</code> into a <code>selection()</code><br />
 virtual void <code>transition</code> (const QEvent *) </p>
<p> virtual void <code>begin</code> () </p>
<p> virtual void <code>append</code> (const QPoint &amp;) </p>
<p> virtual void <code>move</code> (const QPoint &amp;) </p>
<p> virtual void <code>remove</code> () </p>
<p> virtual bool <code>end</code> (bool ok=true)<br />
 <i>Close a selection setting the state to inactive. </i><br />
 virtual bool <code>accept</code> (QPolygon &amp;) const<br />
 <i>Validate and fix up the selection. </i><br />
 virtual void <code>reset</code> () </p>
<p> virtual void <code>widgetMousePressEvent</code> (QMouseEvent *) </p>
<p> virtual void <code>widgetMouseReleaseEvent</code> (QMouseEvent *) </p>
<p> virtual void <code>widgetMouseDoubleClickEvent</code> (QMouseEvent *) </p>
<p> virtual void <code>widgetMouseMoveEvent</code> (QMouseEvent *) </p>
<p> virtual void <code>widgetWheelEvent</code> (QWheelEvent *) </p>
<p> virtual void <code>widgetKeyPressEvent</code> (QKeyEvent *) </p>
<p> virtual void <code>widgetKeyReleaseEvent</code> (QKeyEvent *) </p>
<p> virtual void <code>widgetEnterEvent</code> (QEvent *) </p>
<p> virtual void <code>widgetLeaveEvent</code> (QEvent *) </p>
<p> virtual void <code>stretchSelection</code> (const QSize &amp;oldSize, const QSize &amp;newSize) </p>
<p> virtual void <code>updateDisplay</code> ()<br />
 <i>Update the state of rubber band and tracker label. </i><br />
 const <code>QwtWidgetOverlay</code> * <code>rubberBandOverlay</code> () const </p>
<p> const <code>QwtWidgetOverlay</code> * <code>trackerOverlay</code> () const </p>
<p> const QPolygon &amp; <code>pickedPoints</code> () const </p>
<h2>Detailed Description</h2>
<p><code>QwtPicker</code> provides selections on a widget. </p>
<p> <code>QwtPicker</code> filters all enter, leave, mouse and keyboard events of a widget and translates them into an array of selected points. </p>
<p> The way how the points are collected depends on type of state machine that is connected to the picker. Qwt offers a couple of predefined state machines for selecting: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>Nothing </p>
<p>&nbsp;<wbr><code>QwtPickerTrackerMachine</code></p>
<dt>&bull;</p>
<dd>Single points </p>
<p>&nbsp;<wbr><code>QwtPickerClickPointMachine</code>,&nbsp;<wbr><code>QwtPickerDragPointMachine</code></p>
<dt>&bull;</p>
<dd>Rectangles </p>
<p>&nbsp;<wbr><code>QwtPickerClickRectMachine</code>,&nbsp;<wbr><code>QwtPickerDragRectMachine</code></p>
<dt>&bull;</p>
<dd>Polygons </p>
<p>&nbsp;<wbr><code>QwtPickerPolygonMachine</code></dl>
<p> While these state machines cover the most common ways to collect points it is also possible to implement individual machines as well. </p>
<p> <code>QwtPicker</code> translates the picked points into a selection using the <code>adjustedPoints()</code> method. <code>adjustedPoints()</code> is intended to be reimplemented to fix up the selection according to application specific requirements. (F.e. when an application accepts rectangles of a fixed aspect ratio only.) </p>
<p> Optionally <code>QwtPicker</code> support the process of collecting points by a rubber band and tracker displaying a text for the current mouse position. </p>
<p> <code>Example</code></p>
<dl COMPACT>
<dd>
<pre>#include &lt;qwt_picker.h&gt;
#include &lt;qwt_picker_machine.h&gt;
QwtPicker *picker = new QwtPicker(widget);
picker-&gt;setStateMachine(new QwtPickerDragRectMachine);
picker-&gt;setTrackerMode(QwtPicker::ActiveOnly);
picker-&gt;setRubberBand(QwtPicker::RectRubberBand); </pre>
<p>&nbsp;<wbr>The state machine triggers the following commands:</dl>
<dl COMPACT>
<dt>&bull;</p>
<dd><code>begin()</code> </p>
<p>&nbsp;<wbr>Activate/Initialize the selection.</p>
<dt>&bull;</p>
<dd><code>append()</code> </p>
<p>&nbsp;<wbr>Add a new point</p>
<dt>&bull;</p>
<dd><code>move()</code> </p>
<p>&nbsp;<wbr>Change the position of the last point.</p>
<dt>&bull;</p>
<dd><code>remove()</code> </p>
<p>&nbsp;<wbr>Remove the last point.</p>
<dt>&bull;</p>
<dd><code>end()</code> </p>
<p>&nbsp;<wbr>Terminate the selection and call accept to validate the picked points.</dl>
<p> The picker is active (<code>isActive()</code>), between <code>begin()</code> and <code>end()</code>. In active state the rubber band is displayed, and the tracker is visible in case of trackerMode is ActiveOnly or AlwaysOn. </p>
<p> The cursor can be moved using the arrow keys. All selections can be aborted using the abort key. (<code>QwtEventPattern::KeyPatternCode</code>) </p>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>In case of QWidget::NoFocus the focus policy of the observed widget is set to QWidget::WheelFocus and mouse tracking will be manipulated while the picker is active, or if <code>trackerMode()</code> is AlwayOn.</dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtPicker::DisplayMode</code></h3>
<p>Display mode. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setTrackerMode()</code>, <code>trackerMode()</code>, <code>isActive()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>AlwaysOff </i></p>
<dd>Display never.</p>
<dt><i>AlwaysOn </i></p>
<dd>Display always.</p>
<dt><i>ActiveOnly </i></p>
<dd>Display only when the selection is active.</dl>
<h3>enum <code>QwtPicker::ResizeMode</code></h3>
<p>Controls what to do with the selected points of an active selection when the observed widget is resized. </p>
<p> The default value is <code>QwtPicker::Stretch</code>. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setResizeMode()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>Stretch </i></p>
<dd>All points are scaled according to the new size,.</p>
<dt><i>KeepSize </i></p>
<dd>All points remain unchanged.</dl>
<h3>enum <code>QwtPicker::RubberBand</code></h3>
<p>Rubber band style </p>
<p> The default value is <code>QwtPicker::NoRubberBand</code>. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setRubberBand()</code>, <code>rubberBand()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>NoRubberBand </i></p>
<dd>No rubberband.</p>
<dt><i>HLineRubberBand </i></p>
<dd>A horizontal line ( only for <code>QwtPickerMachine::PointSelection</code> )</p>
<dt><i>VLineRubberBand </i></p>
<dd>A vertical line ( only for <code>QwtPickerMachine::PointSelection</code> )</p>
<dt><i>CrossRubberBand </i></p>
<dd>A crosshair ( only for <code>QwtPickerMachine::PointSelection</code> )</p>
<dt><i>RectRubberBand </i></p>
<dd>A rectangle ( only for <code>QwtPickerMachine::RectSelection</code> )</p>
<dt><i>EllipseRubberBand </i></p>
<dd>An ellipse ( only for <code>QwtPickerMachine::RectSelection</code> )</p>
<dt><i>PolygonRubberBand </i></p>
<dd>A polygon ( only for <code>QwtPickerMachine::PolygonSelection</code> )</p>
<dt><i>UserRubberBand </i></p>
<dd>Values &gt;= UserRubberBand can be used to define additional rubber bands.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPicker::QwtPicker (QWidget *parent) [explicit]</h3>
<p>Constructor </p>
<p> Creates an picker that is enabled, but without a state machine. rubber band and tracker are disabled. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>parent</i> Parent widget, that will be observed</dl>
<h3>QwtPicker::QwtPicker (<code>RubberBand</code>rubberBand, <code>DisplayMode</code>trackerMode, QWidget *parent) [explicit]</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rubberBand</i> Rubber band style<br />
 <i>trackerMode</i> Tracker mode<br />
 <i>parent</i> Parent widget, that will be observed</dl>
<h2>Member Function Documentation</h2>
<h3>bool QwtPicker::accept (QPolygon &amp;selection) const [protected], [virtual]</h3>
<p>Validate and fix up the selection. Accepts all selections unmodified </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>selection</i> Selection to validate and fix up</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true, when accepted, false otherwise</dl>
<p> Reimplemented in <code>QwtPlotZoomer</code>.</p>
<h3>void QwtPicker::activated (boolon) [signal]</h3>
<p>A signal indicating, when the picker has been activated. Together with <code>setEnabled()</code> it can be used to implement selections with more than one picker. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>on</i> True, when the picker has been activated</dl>
<h3>QPolygon QwtPicker::adjustedPoints (const QPolygon &amp;points) const [protected], [virtual]</h3>
<p>Map the <code>pickedPoints()</code> into a <code>selection()</code> <code>adjustedPoints()</code> maps the points, that have been collected on the <code>parentWidget()</code> into a <code>selection()</code>. The default implementation simply returns the points unmodified. </p>
<p> The reason, why a <code>selection()</code> differs from the picked points depends on the application requirements. F.e. : </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>A rectangular selection might need to have a specific aspect ratio only. </p>
<dt>&bull;</p>
<dd>A selection could accept non intersecting polygons only. </p>
<dt>&bull;</p>
<dd>&#8230; </p>
<p>&nbsp;<wbr>The example below is for a rectangular selection, where the first point is the center of the selected rectangle.&nbsp;<wbr></dl>
<p> <code>Example</code></p>
<dl COMPACT>
<dd>
<pre>QPolygon MyPicker::adjustedPoints(const QPolygon &amp;points) const
{
 QPolygon adjusted;
 if ( points.size() == 2 )
 {
 const int width = qAbs(points[1].x() - points[0].x());
 const int height = qAbs(points[1].y() - points[0].y());
 QRect rect(0, 0, 2 * width, 2 * height);
 rect.moveCenter(points[0]);
 adjusted += rect.topLeft();
 adjusted += rect.bottomRight();
 }
 return adjusted;
}</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>points</i> Selected points</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Selected points unmodified</dl>
<h3>void QwtPicker::append (const QPoint &amp;pos) [protected], [virtual]</h3>
<p>Append a point to the selection and update rubber band and tracker. The <code>appended()</code> signal is emitted. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pos</i> Additional point</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isActive()</code>, <code>begin()</code>, <code>end()</code>, <code>move()</code>, <code>appended()</code></dl>
<p> Reimplemented in <code>QwtPlotPicker</code>.</p>
<h3>void QwtPicker::appended (const QPoint &amp;pos) [signal]</h3>
<p>A signal emitted when a point has been appended to the selection </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pos</i> Position of the appended point.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>append()</code>. <code>moved()</code></dl>
<h3>void QwtPicker::begin () [protected], [virtual]</h3>
<p>Open a selection setting the state to active </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isActive()</code>, <code>end()</code>, <code>append()</code>, <code>move()</code></dl>
<p> Reimplemented in <code>QwtPlotZoomer</code>.</p>
<h3>void QwtPicker::changed (const QPolygon &amp;selection) [signal]</h3>
<p>A signal emitted when the active selection has been changed. This might happen when the observed widget is resized. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>selection</i> Changed selection</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>stretchSelection()</code></dl>
<h3>void QwtPicker::drawRubberBand (QPainter *painter) const [virtual]</h3>
<p>Draw a rubber band, depending on <code>rubberBand()</code> </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter, initialized with a clip region</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>rubberBand()</code>, <code>RubberBand</code></dl>
<h3>void QwtPicker::drawTracker (QPainter *painter) const [virtual]</h3>
<p>Draw the tracker </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>trackerRect()</code>, <code>trackerText()</code></dl>
<h3>bool QwtPicker::end (boolok = true) [protected], [virtual]</h3>
<p>Close a selection setting the state to inactive. The selection is validated and maybe fixed by <code>accept()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ok</i> If true, complete the selection and emit a selected signal otherwise discard the selection.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true if the selection is accepted, false otherwise</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isActive()</code>, <code>begin()</code>, <code>append()</code>, <code>move()</code>, <code>selected()</code>, <code>accept()</code></dl>
<p> Reimplemented in <code>QwtPlotZoomer</code>, and <code>QwtPlotPicker</code>.</p>
<h3>bool QwtPicker::eventFilter (QObject *object, QEvent *event) [virtual]</h3>
<p>Event filter. When <code>isEnabled()</code> is true all events of the observed widget are filtered. Mouse and keyboard events are translated into widgetMouse- and widgetKey- and widgetWheel-events. Paint and Resize events are handled to keep rubber band and tracker up to date. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>object</i> Object to be filtered<br />
 <i>event</i> Event</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Always false.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>widgetEnterEvent()</code>, <code>widgetLeaveEvent()</code>, <code>widgetMousePressEvent()</code>, <code>widgetMouseReleaseEvent()</code>, <code>widgetMouseDoubleClickEvent()</code>, <code>widgetMouseMoveEvent()</code>, <code>widgetWheelEvent()</code>, <code>widgetKeyPressEvent()</code>, <code>widgetKeyReleaseEvent()</code>, QObject::installEventFilter(), QObject::event()</dl>
<h3>bool QwtPicker::isActive () const</h3>
<p>A picker is active between <code>begin()</code> and <code>end()</code>. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true if the selection is active.</dl>
<h3>bool QwtPicker::isEnabled () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>true when enabled, false otherwise</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setEnabled()</code>, <code>eventFilter()</code></dl>
<h3>void QwtPicker::move (const QPoint &amp;pos) [protected], [virtual]</h3>
<p>Move the last point of the selection The <code>moved()</code> signal is emitted. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pos</i> New position</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isActive()</code>, <code>begin()</code>, <code>end()</code>, <code>append()</code></dl>
<p> Reimplemented in <code>QwtPlotPicker</code>.</p>
<h3>void QwtPicker::moved (const QPoint &amp;pos) [signal]</h3>
<p>A signal emitted whenever the last appended point of the selection has been moved. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pos</i> Position of the moved last point of the selection.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>move()</code>, <code>appended()</code></dl>
<h3>QPainterPath QwtPicker::pickArea () const [virtual]</h3>
<p>Find the area of the observed widget, where selection might happen. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd><code>parentWidget()</code>-&gt;contentsRect()</dl>
<h3>const QPolygon &amp; QwtPicker::pickedPoints () const [protected]</h3>
<p>Return the points, that have been collected so far. The <code>selection()</code> is calculated from the <code>pickedPoints()</code> in <code>adjustedPoints()</code>. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Picked points</dl>
<h3>void QwtPicker::remove () [protected], [virtual]</h3>
<p>Remove the last point of the selection The <code>removed()</code> signal is emitted. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isActive()</code>, <code>begin()</code>, <code>end()</code>, <code>append()</code>, <code>move()</code></dl>
<h3>void QwtPicker::removed (const QPoint &amp;pos) [signal]</h3>
<p>A signal emitted whenever the last appended point of the selection has been removed. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pos</i> Position of the point, that has been removed</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>remove()</code>, <code>appended()</code></dl>
<h3>void QwtPicker::reset () [protected], [virtual]</h3>
<p>Reset the state machine and terminate ( end(false) ) the selection</p>
<h3><code>QwtPicker::ResizeMode</code> QwtPicker::resizeMode () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Resize mode</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setResizeMode()</code>, <code>ResizeMode</code></dl>
<h3><code>QwtPicker::RubberBand</code> QwtPicker::rubberBand () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Rubber band style</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setRubberBand()</code>, <code>RubberBand</code>, <code>rubberBandPen()</code></dl>
<h3>QRegion QwtPicker::rubberBandMask () const [virtual]</h3>
<p>Calculate the mask for the rubber band overlay </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Region for the mask</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>QWidget::setMask()</dl>
<h3>const <code>QwtWidgetOverlay</code> * QwtPicker::rubberBandOverlay () const [protected]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Overlay displaying the rubber band</dl>
<h3>QPen QwtPicker::rubberBandPen () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Rubber band pen</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setRubberBandPen()</code>, <code>rubberBand()</code></dl>
<h3>void QwtPicker::selected (const QPolygon &amp;polygon) [signal]</h3>
<p>A signal emitting the selected points, at the end of a selection. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>polygon</i> Selected points</dl>
<h3>QPolygon QwtPicker::selection () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Selected points</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>pickedPoints()</code>, <code>adjustedPoints()</code></dl>
<h3>void QwtPicker::setEnabled (boolenabled) [slot]</h3>
<p>En/disable the picker. When enabled is true an event filter is installed for the observed widget, otherwise the event filter is removed. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>enabled</i> true or false</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isEnabled()</code>, <code>eventFilter()</code></dl>
<h3>void QwtPicker::setResizeMode (<code>ResizeMode</code>mode)</h3>
<p>Set the resize mode. The resize mode controls what to do with the selected points of an active selection when the observed widget is resized. </p>
<p> Stretch means the points are scaled according to the new size, KeepSize means the points remain unchanged. </p>
<p> The default mode is Stretch. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>mode</i> Resize mode</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>resizeMode()</code>, <code>ResizeMode</code></dl>
<h3>void QwtPicker::setRubberBand (<code>RubberBand</code>rubberBand)</h3>
<p>Set the rubber band style </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rubberBand</i> Rubber band style The default value is NoRubberBand.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>rubberBand()</code>, <code>RubberBand</code>, <code>setRubberBandPen()</code></dl>
<h3>void QwtPicker::setRubberBandPen (const QPen &amp;pen)</h3>
<p>Set the pen for the rubberband </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pen</i> Rubber band pen</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>rubberBandPen()</code>, <code>setRubberBand()</code></dl>
<h3>void QwtPicker::setStateMachine (<code>QwtPickerMachine</code> *stateMachine)</h3>
<p>Set a state machine and delete the previous one </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>stateMachine</i> State machine</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>stateMachine()</code></dl>
<h3>void QwtPicker::setTrackerFont (const QFont &amp;font)</h3>
<p>Set the font for the tracker </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>font</i> Tracker font</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>trackerFont()</code>, <code>setTrackerMode()</code>, <code>setTrackerPen()</code></dl>
<h3>void QwtPicker::setTrackerMode (<code>DisplayMode</code>mode)</h3>
<p>Set the display mode of the tracker. A tracker displays information about current position of the cursor as a string. The display mode controls if the tracker has to be displayed whenever the observed widget has focus and cursor (AlwaysOn), never (AlwaysOff), or only when the selection is active (ActiveOnly). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>mode</i> Tracker display mode</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>In case of AlwaysOn, mouseTracking will be enabled for the observed widget.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>trackerMode()</code>, <code>DisplayMode</code></dl>
<h3>void QwtPicker::setTrackerPen (const QPen &amp;pen)</h3>
<p>Set the pen for the tracker </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pen</i> Tracker pen</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>trackerPen()</code>, <code>setTrackerMode()</code>, <code>setTrackerFont()</code></dl>
<h3>const <code>QwtPickerMachine</code> * QwtPicker::stateMachine () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Assigned state machine</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setStateMachine()</code></dl>
<h3><code>QwtPickerMachine</code> * QwtPicker::stateMachine ()</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Assigned state machine</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setStateMachine()</code></dl>
<h3>void QwtPicker::stretchSelection (const QSize &amp;oldSize, const QSize &amp;newSize) [protected], [virtual]</h3>
<p>Scale the selection by the ratios of oldSize and newSize The <code>changed()</code> signal is emitted. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>oldSize</i> Previous size<br />
 <i>newSize</i> Current size</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>ResizeMode</code>, <code>setResizeMode()</code>, <code>resizeMode()</code></dl>
<h3>QFont QwtPicker::trackerFont () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Tracker font</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setTrackerFont()</code>, <code>trackerMode()</code>, <code>trackerPen()</code></dl>
<h3><code>QwtPicker::DisplayMode</code> QwtPicker::trackerMode () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Tracker display mode</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setTrackerMode()</code>, <code>DisplayMode</code></dl>
<h3>const <code>QwtWidgetOverlay</code> * QwtPicker::trackerOverlay () const [protected]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Overlay displaying the tracker text</dl>
<h3>QPen QwtPicker::trackerPen () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Tracker pen</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setTrackerPen()</code>, <code>trackerMode()</code>, <code>trackerFont()</code></dl>
<h3>QPoint QwtPicker::trackerPosition () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Current position of the tracker</dl>
<h3>QRect QwtPicker::trackerRect (const QFont &amp;font) const [virtual]</h3>
<p>Calculate the bounding rectangle for the tracker text from the current position of the tracker </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>font</i> Font of the tracker text</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Bounding rectangle of the tracker text</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>trackerPosition()</code></dl>
<h3><code>QwtText</code> QwtPicker::trackerText (const QPoint &amp;pos) const [virtual]</h3>
<p>Return the label for a position. In case of HLineRubberBand the label is the value of the y position, in case of VLineRubberBand the value of the x position. Otherwise the label contains x and y position separated by a &#8216;,&#8217; . </p>
<p> The format for the string conversion is &#8216;%d&#8217;. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pos</i> Position</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Converted position as string</dl>
<p> Reimplemented in <code>QwtPlotPicker</code>.</p>
<h3>void QwtPicker::transition (const QEvent *event) [protected], [virtual]</h3>
<p>Passes an event to the state machine and executes the resulting commands. Append and Move commands use the current position of the cursor ( QCursor::pos() ). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Event</dl>
<h3>void QwtPicker::widgetEnterEvent (QEvent *event) [protected], [virtual]</h3>
<p>Handle a enter event for the observed widget. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Qt event</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>eventFilter()</code>, <code>widgetMousePressEvent()</code>, <code>widgetMouseReleaseEvent()</code>, <code>widgetMouseDoubleClickEvent()</code>, <code>widgetWheelEvent()</code>, <code>widgetKeyPressEvent()</code>, <code>widgetKeyReleaseEvent()</code></dl>
<h3>void QwtPicker::widgetKeyPressEvent (QKeyEvent *keyEvent) [protected], [virtual]</h3>
<p>Handle a key press event for the observed widget. </p>
<p> Selections can be completely done by the keyboard. The arrow keys move the cursor, the abort key aborts a selection. All other keys are handled by the current state machine. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>keyEvent</i> Key event</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>eventFilter()</code>, <code>widgetMousePressEvent()</code>, <code>widgetMouseReleaseEvent()</code>, <code>widgetMouseDoubleClickEvent()</code>, <code>widgetMouseMoveEvent()</code>, <code>widgetWheelEvent()</code>, <code>widgetKeyReleaseEvent()</code>, <code>stateMachine()</code>, <code>QwtEventPattern::KeyPatternCode</code></dl>
<p> Reimplemented in <code>QwtPlotZoomer</code>.</p>
<h3>void QwtPicker::widgetKeyReleaseEvent (QKeyEvent *keyEvent) [protected], [virtual]</h3>
<p>Handle a key release event for the observed widget. </p>
<p> Passes the event to the state machine. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>keyEvent</i> Key event</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>eventFilter()</code>, <code>widgetMousePressEvent()</code>, <code>widgetMouseReleaseEvent()</code>, <code>widgetMouseDoubleClickEvent()</code>, <code>widgetMouseMoveEvent()</code>, <code>widgetWheelEvent()</code>, <code>widgetKeyPressEvent()</code>, <code>stateMachine()</code></dl>
<h3>void QwtPicker::widgetLeaveEvent (QEvent *event) [protected], [virtual]</h3>
<p>Handle a leave event for the observed widget. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Qt event</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>eventFilter()</code>, <code>widgetMousePressEvent()</code>, <code>widgetMouseReleaseEvent()</code>, <code>widgetMouseDoubleClickEvent()</code>, <code>widgetWheelEvent()</code>, <code>widgetKeyPressEvent()</code>, <code>widgetKeyReleaseEvent()</code></dl>
<h3>void QwtPicker::widgetMouseDoubleClickEvent (QMouseEvent *mouseEvent) [protected], [virtual]</h3>
<p>Handle mouse double click event for the observed widget. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>mouseEvent</i> Mouse event</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>eventFilter()</code>, <code>widgetMousePressEvent()</code>, <code>widgetMouseReleaseEvent()</code>, <code>widgetMouseMoveEvent()</code>, <code>widgetWheelEvent()</code>, <code>widgetKeyPressEvent()</code>, <code>widgetKeyReleaseEvent()</code></dl>
<h3>void QwtPicker::widgetMouseMoveEvent (QMouseEvent *mouseEvent) [protected], [virtual]</h3>
<p>Handle a mouse move event for the observed widget. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>mouseEvent</i> Mouse event</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>eventFilter()</code>, <code>widgetMousePressEvent()</code>, <code>widgetMouseReleaseEvent()</code>, <code>widgetMouseDoubleClickEvent()</code>, <code>widgetWheelEvent()</code>, <code>widgetKeyPressEvent()</code>, <code>widgetKeyReleaseEvent()</code></dl>
<h3>void QwtPicker::widgetMousePressEvent (QMouseEvent *mouseEvent) [protected], [virtual]</h3>
<p>Handle a mouse press event for the observed widget. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>mouseEvent</i> Mouse event</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>eventFilter()</code>, <code>widgetMouseReleaseEvent()</code>, <code>widgetMouseDoubleClickEvent()</code>, <code>widgetMouseMoveEvent()</code>, <code>widgetWheelEvent()</code>, <code>widgetKeyPressEvent()</code>, <code>widgetKeyReleaseEvent()</code></dl>
<h3>void QwtPicker::widgetMouseReleaseEvent (QMouseEvent *mouseEvent) [protected], [virtual]</h3>
<p>Handle a mouse release event for the observed widget. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>mouseEvent</i> Mouse event</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>eventFilter()</code>, <code>widgetMousePressEvent()</code>, <code>widgetMouseDoubleClickEvent()</code>, <code>widgetMouseMoveEvent()</code>, <code>widgetWheelEvent()</code>, <code>widgetKeyPressEvent()</code>, <code>widgetKeyReleaseEvent()</code></dl>
<p> Reimplemented in <code>QwtPlotZoomer</code>.</p>
<h3>void QwtPicker::widgetWheelEvent (QWheelEvent *wheelEvent) [protected], [virtual]</h3>
<p>Handle a wheel event for the observed widget. </p>
<p> Move the last point of the selection in case of <code>isActive()</code> == true </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>wheelEvent</i> Wheel event</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>eventFilter()</code>, <code>widgetMousePressEvent()</code>, <code>widgetMouseReleaseEvent()</code>, <code>widgetMouseDoubleClickEvent()</code>, <code>widgetMouseMoveEvent()</code>, <code>widgetKeyPressEvent()</code>, <code>widgetKeyReleaseEvent()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
