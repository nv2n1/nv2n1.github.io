---
title: "qwtplotpanner(3)"
name: "qwtplotpanner"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtplotpanner/"
description: "QwtPlotPanner –"
---

<p>QwtPlotPanner &#8211; </p>
<p> <code>QwtPlotPanner</code> provides panning of a plot canvas.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_plot_panner.h&gt; </p>
<p> Inherits <code>QwtPanner</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtPlotPanner</code> (QWidget *)<br />
 <i>A panner for the canvas of a </i><code>QwtPlot</code>.<br />
 virtual <code>~QwtPlotPanner</code> ()<br />
 <i>Destructor. </i><br />
 QWidget * <code>canvas</code> ()<br />
 <i>Return observed plot canvas. </i><br />
 const QWidget * <code>canvas</code> () const<br />
 <i>Return Observed plot canvas. </i><br />
 <code>QwtPlot</code> * <code>plot</code> ()<br />
 <i>Return plot widget, containing the observed plot canvas. </i><br />
 const <code>QwtPlot</code> * <code>plot</code> () const<br />
 <i>Return plot widget, containing the observed plot canvas. </i><br />
 void <code>setAxisEnabled</code> (int axis, bool on)<br />
 <i>En/Disable an axis. </i><br />
 bool <code>isAxisEnabled</code> (int axis) const </p>
<h3>Protected Slots</h3>
<p>virtual void <code>moveCanvas</code> (int dx, int dy) </p>
<h3>Protected Member Functions</h3>
<p>virtual QBitmap <code>contentsMask</code> () const </p>
<p> virtual QPixmap <code>grab</code> () const </p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p><code>QwtPlotPanner</code> provides panning of a plot canvas. </p>
<p> <code>QwtPlotPanner</code> is a panner for a plot canvas, that adjusts the scales of the axes after dropping the canvas on its new position. </p>
<p> Together with <code>QwtPlotZoomer</code> and <code>QwtPlotMagnifier</code> powerful ways of navigating on a <code>QwtPlot</code> widget can be implemented easily. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The axes are not updated, while dragging the canvas</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlotZoomer</code>, <code>QwtPlotMagnifier</code></dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPlotPanner::QwtPlotPanner (QWidget *canvas) [explicit]</h3>
<p>A panner for the canvas of a <code>QwtPlot</code>. The panner is enabled for all axes </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>canvas</i> Plot canvas to pan, also the parent object</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setAxisEnabled()</code></dl>
<h2>Member Function Documentation</h2>
<h3>QBitmap QwtPlotPanner::contentsMask () const [protected], [virtual]</h3>
<p>Calculate a mask from the border path of the canvas </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Mask as bitmap</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlotCanvas::borderPath()</code></dl>
<p> Reimplemented from <code>QwtPanner</code>.</p>
<h3>QPixmap QwtPlotPanner::grab () const [protected], [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Pixmap with the content of the canvas</dl>
<p> Reimplemented from <code>QwtPanner</code>.</p>
<h3>bool QwtPlotPanner::isAxisEnabled (intaxis) const</h3>
<p>Test if an axis is enabled </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axis</i> Axis, see <code>QwtPlot::Axis</code></dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>True, if the axis is enabled</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setAxisEnabled()</code>, <code>moveCanvas()</code></dl>
<h3>void QwtPlotPanner::moveCanvas (intdx, intdy) [protected], [virtual], [slot]</h3>
<p>Adjust the enabled axes according to dx/dy </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dx</i> Pixel offset in x direction<br />
 <i>dy</i> Pixel offset in y direction</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPanner::panned()</code></dl>
<h3>void QwtPlotPanner::setAxisEnabled (intaxis, boolon)</h3>
<p>En/Disable an axis. Axes that are enabled will be synchronized to the result of panning. All other axes will remain unchanged. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axis</i> Axis, see <code>QwtPlot::Axis</code><br />
 <i>on</i> On/Off</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isAxisEnabled()</code>, <code>moveCanvas()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
