---
title: "qwtplotrescaler(3)"
name: "qwtplotrescaler"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtplotrescaler/"
description: "QwtPlotRescaler –"
---

<p>QwtPlotRescaler &#8211; </p>
<p> <code>QwtPlotRescaler</code> takes care of fixed aspect ratios for plot scales.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_plot_rescaler.h&gt; </p>
<p> Inherits QObject.</p>
<h3>Public Types</h3>
<p>enum <code>RescalePolicy</code> { <code>Fixed</code>, <code>Expanding</code>, <code>Fitting</code> } </p>
<p> enum <code>ExpandingDirection</code> { <code>ExpandUp</code>, <code>ExpandDown</code>, <code>ExpandBoth</code> } </p>
<h3>Public Member Functions</h3>
<p><code>QwtPlotRescaler</code> (QWidget *<code>canvas</code>, int <code>referenceAxis</code>=<code>QwtPlot::xBottom</code>, <code>RescalePolicy</code>=<code>Expanding</code>) </p>
<p> virtual <code>~QwtPlotRescaler</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setEnabled</code> (bool)<br />
 <i>En/disable the rescaler. </i><br />
 bool <code>isEnabled</code> () const </p>
<p> void <code>setRescalePolicy</code> (<code>RescalePolicy</code>) </p>
<p> <code>RescalePolicy</code> <code>rescalePolicy</code> () const </p>
<p> void <code>setExpandingDirection</code> (<code>ExpandingDirection</code>) </p>
<p> void <code>setExpandingDirection</code> (int axis, <code>ExpandingDirection</code>) </p>
<p> <code>ExpandingDirection</code> <code>expandingDirection</code> (int axis) const </p>
<p> void <code>setReferenceAxis</code> (int axis) </p>
<p> int <code>referenceAxis</code> () const </p>
<p> void <code>setAspectRatio</code> (double ratio) </p>
<p> void <code>setAspectRatio</code> (int axis, double ratio) </p>
<p> double <code>aspectRatio</code> (int axis) const </p>
<p> void <code>setIntervalHint</code> (int axis, const <code>QwtInterval</code> &amp;) </p>
<p> <code>QwtInterval</code> <code>intervalHint</code> (int axis) const </p>
<p> QWidget * <code>canvas</code> () </p>
<p> const QWidget * <code>canvas</code> () const </p>
<p> <code>QwtPlot</code> * <code>plot</code> () </p>
<p> const <code>QwtPlot</code> * <code>plot</code> () const </p>
<p> virtual bool <code>eventFilter</code> (QObject *, QEvent *)<br />
 <i>Event filter for the plot canvas. </i><br />
 void <code>rescale</code> () const<br />
 <i>Adjust the plot axes scales. </i></p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>canvasResizeEvent</code> (QResizeEvent *) </p>
<p> virtual void <code>rescale</code> (const QSize &amp;oldSize, const QSize &amp;newSize) const </p>
<p> virtual <code>QwtInterval</code> <code>expandScale</code> (int axis, const QSize &amp;oldSize, const QSize &amp;newSize) const </p>
<p> virtual <code>QwtInterval</code> <code>syncScale</code> (int axis, const <code>QwtInterval</code> &amp;reference, const QSize &amp;size) const </p>
<p> virtual void <code>updateScales</code> (<code>QwtInterval</code> intervals[<code>QwtPlot::axisCnt</code>]) const </p>
<p> Qt::Orientation <code>orientation</code> (int axis) const </p>
<p> <code>QwtInterval</code> <code>interval</code> (int axis) const </p>
<p> <code>QwtInterval</code> <code>expandInterval</code> (const <code>QwtInterval</code> &amp;, double width, <code>ExpandingDirection</code>) const </p>
<h2>Detailed Description</h2>
<p><code>QwtPlotRescaler</code> takes care of fixed aspect ratios for plot scales. </p>
<p> <code>QwtPlotRescaler</code> auto adjusts the axes of a <code>QwtPlot</code> according to fixed aspect ratios.</p>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtPlotRescaler::ExpandingDirection</code></h3>
<p>When <code>rescalePolicy()</code> is set to Expanding its direction depends on ExpandingDirection </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>ExpandUp </i></p>
<dd>The upper limit of the scale is adjusted.</p>
<dt><i>ExpandDown </i></p>
<dd>The lower limit of the scale is adjusted.</p>
<dt><i>ExpandBoth </i></p>
<dd>Both limits of the scale are adjusted.</dl>
<h3>enum <code>QwtPlotRescaler::RescalePolicy</code></h3>
<p>The rescale policy defines how to rescale the reference axis and their depending axes. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>ExpandingDirection</code>, <code>setIntervalHint()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>Fixed </i></p>
<dd>The interval of the reference axis remains unchanged, when the geometry of the canvas changes. All other axes will be adjusted according to their aspect ratio.</p>
<dt><i>Expanding </i></p>
<dd>The interval of the reference axis will be shrunk/expanded, when the geometry of the canvas changes. All other axes will be adjusted according to their aspect ratio.</dl>
<p> The interval, that is represented by one pixel is fixed.</p>
<dl COMPACT>
<dt><i>Fitting </i></p>
<dd>The intervals of the axes are calculated, so that all axes include their interval hint.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPlotRescaler::QwtPlotRescaler (QWidget *canvas, intreferenceAxis = <code>QwtPlot::xBottom</code>, <code>RescalePolicy</code>policy = <code>Expanding</code>) [explicit]</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>canvas</i> Canvas<br />
 <i>referenceAxis</i> Reference axis, see RescalePolicy<br />
 <i>policy</i> Rescale policy</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setRescalePolicy()</code>, <code>setReferenceAxis()</code></dl>
<h2>Member Function Documentation</h2>
<h3>double QwtPlotRescaler::aspectRatio (intaxis) const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Aspect ratio between an axis and the reference axis.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axis</i> Axis index ( see QwtPlot::AxisId )</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setAspectRatio()</code></dl>
<h3>QWidget * QwtPlotRescaler::canvas ()</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>plot canvas</dl>
<h3>const QWidget * QwtPlotRescaler::canvas () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>plot canvas</dl>
<h3>void QwtPlotRescaler::canvasResizeEvent (QResizeEvent *event) [protected], [virtual]</h3>
<p>Event handler for resize events of the plot canvas </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Resize event</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>rescale()</code></dl>
<h3><code>QwtPlotRescaler::ExpandingDirection</code> QwtPlotRescaler::expandingDirection (intaxis) const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Direction in which an axis should be expanded</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axis</i> Axis index ( see QwtPlot::AxisId )</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setExpandingDirection()</code></dl>
<h3><code>QwtInterval</code> QwtPlotRescaler::expandInterval (const <code>QwtInterval</code> &amp;interval, doublewidth, <code>ExpandingDirection</code>direction) const [protected]</h3>
<p>Expand the interval </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>interval</i> Interval to be expanded<br />
 <i>width</i> Distance to be added to the interval<br />
 <i>direction</i> Direction of the expand operation</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Expanded interval</dl>
<h3><code>QwtInterval</code> QwtPlotRescaler::expandScale (intaxis, const QSize &amp;oldSize, const QSize &amp;newSize) const [protected], [virtual]</h3>
<p>Calculate the new scale interval of a plot axis </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axis</i> Axis index ( see QwtPlot::AxisId )<br />
 <i>oldSize</i> Previous size of the canvas<br />
 <i>newSize</i> New size of the canvas</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Calculated new interval for the axis</dl>
<h3><code>QwtInterval</code> QwtPlotRescaler::interval (intaxis) const [protected]</h3>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axis</i> Axis index ( see QwtPlot::AxisId )</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Normalized interval of an axis</dl>
<h3><code>QwtInterval</code> QwtPlotRescaler::intervalHint (intaxis) const</h3>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axis</i> Axis, see <code>QwtPlot::Axis</code></dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Interval hint</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setIntervalHint()</code>, <code>RescalePolicy</code></dl>
<h3>bool QwtPlotRescaler::isEnabled () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>true when enabled, false otherwise</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setEnabled</code>, <code>eventFilter()</code></dl>
<h3>Qt::Orientation QwtPlotRescaler::orientation (intaxis) const [protected]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Orientation of an axis</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axis</i> Axis index ( see QwtPlot::AxisId )</dl>
<h3><code>QwtPlot</code> * QwtPlotRescaler::plot ()</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>plot widget</dl>
<h3>const <code>QwtPlot</code> * QwtPlotRescaler::plot () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>plot widget</dl>
<h3>int QwtPlotRescaler::referenceAxis () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Reference axis ( see RescalePolicy )</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setReferenceAxis()</code></dl>
<h3>void QwtPlotRescaler::rescale (const QSize &amp;oldSize, const QSize &amp;newSize) const [protected], [virtual]</h3>
<p>Adjust the plot axes scales </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>oldSize</i> Previous size of the canvas<br />
 <i>newSize</i> New size of the canvas</dl>
<h3><code>QwtPlotRescaler::RescalePolicy</code> QwtPlotRescaler::rescalePolicy () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Rescale policy</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setRescalePolicy()</code></dl>
<h3>void QwtPlotRescaler::setAspectRatio (doubleratio)</h3>
<p>Set the aspect ratio between the scale of the reference axis and the other scales. The default ratio is 1.0 </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ratio</i> Aspect ratio</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>aspectRatio()</code></dl>
<h3>void QwtPlotRescaler::setAspectRatio (intaxis, doubleratio)</h3>
<p>Set the aspect ratio between the scale of the reference axis and another scale. The default ratio is 1.0 </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axis</i> Axis index ( see QwtPlot::AxisId )<br />
 <i>ratio</i> Aspect ratio</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>aspectRatio()</code></dl>
<h3>void QwtPlotRescaler::setEnabled (boolon)</h3>
<p>En/disable the rescaler. When enabled is true an event filter is installed for the canvas, otherwise the event filter is removed. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>on</i> true or false</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isEnabled()</code>, <code>eventFilter()</code></dl>
<h3>void QwtPlotRescaler::setExpandingDirection (<code>ExpandingDirection</code>direction)</h3>
<p>Set the direction in which all axis should be expanded </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>direction</i> Direction</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>expandingDirection()</code></dl>
<h3>void QwtPlotRescaler::setExpandingDirection (intaxis, <code>ExpandingDirection</code>direction)</h3>
<p>Set the direction in which an axis should be expanded </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axis</i> Axis index ( see QwtPlot::AxisId )<br />
 <i>direction</i> Direction</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>expandingDirection()</code></dl>
<h3>void QwtPlotRescaler::setIntervalHint (intaxis, const <code>QwtInterval</code> &amp;interval)</h3>
<p>Set an interval hint for an axis </p>
<p> In Fitting mode, the hint is used as minimal interval that always needs to be displayed. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axis</i> Axis, see <code>QwtPlot::Axis</code><br />
 <i>interval</i> Axis</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>intervalHint()</code>, <code>RescalePolicy</code></dl>
<h3>void QwtPlotRescaler::setReferenceAxis (intaxis)</h3>
<p>Set the reference axis ( see RescalePolicy ) </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axis</i> Axis index ( <code>QwtPlot::Axis</code> )</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>referenceAxis()</code></dl>
<h3>void QwtPlotRescaler::setRescalePolicy (<code>RescalePolicy</code>policy)</h3>
<p>Change the rescale policy </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>policy</i> Rescale policy</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>rescalePolicy()</code></dl>
<h3><code>QwtInterval</code> QwtPlotRescaler::syncScale (intaxis, const <code>QwtInterval</code> &amp;reference, const QSize &amp;size) const [protected], [virtual]</h3>
<p>Synchronize an axis scale according to the scale of the reference axis </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axis</i> Axis index ( see QwtPlot::AxisId )<br />
 <i>reference</i> Interval of the reference axis<br />
 <i>size</i> Size of the canvas</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>New interval for axis</dl>
<h3>void QwtPlotRescaler::updateScales (<code>QwtInterval</code>intervals[QwtPlot::axisCnt]) const [protected], [virtual]</h3>
<p>Update the axes scales </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>intervals</i> Scale intervals</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
