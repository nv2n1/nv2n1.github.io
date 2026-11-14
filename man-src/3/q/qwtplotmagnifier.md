---
title: "qwtplotmagnifier(3)"
name: "qwtplotmagnifier"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtplotmagnifier/"
description: "QwtPlotMagnifier –"
---

<p>QwtPlotMagnifier &#8211; </p>
<p> <code>QwtPlotMagnifier</code> provides zooming, by magnifying in steps.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_plot_magnifier.h&gt; </p>
<p> Inherits <code>QwtMagnifier</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtPlotMagnifier</code> (QWidget *) </p>
<p> virtual <code>~QwtPlotMagnifier</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setAxisEnabled</code> (int axis, bool on)<br />
 <i>En/Disable an axis. </i><br />
 bool <code>isAxisEnabled</code> (int axis) const </p>
<p> QWidget * <code>canvas</code> ()<br />
 <i>Return observed plot canvas. </i><br />
 const QWidget * <code>canvas</code> () const<br />
 <i>Return Observed plot canvas. </i><br />
 <code>QwtPlot</code> * <code>plot</code> ()<br />
 <i>Return plot widget, containing the observed plot canvas. </i><br />
 const <code>QwtPlot</code> * <code>plot</code> () const<br />
 <i>Return plot widget, containing the observed plot canvas. </i></p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>rescale</code> (double factor) </p>
<h2>Detailed Description</h2>
<p><code>QwtPlotMagnifier</code> provides zooming, by magnifying in steps. </p>
<p> Using <code>QwtPlotMagnifier</code> a plot can be zoomed in/out in steps using keys, the mouse wheel or moving a mouse button in vertical direction. </p>
<p> Together with <code>QwtPlotZoomer</code> and <code>QwtPlotPanner</code> it is possible to implement individual and powerful navigation of the plot canvas. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlotZoomer</code>, <code>QwtPlotPanner</code>, <code>QwtPlot</code></dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPlotMagnifier::QwtPlotMagnifier (QWidget *canvas) [explicit]</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>canvas</i> Plot canvas to be magnified</dl>
<h2>Member Function Documentation</h2>
<h3>bool QwtPlotMagnifier::isAxisEnabled (intaxis) const</h3>
<p>Test if an axis is enabled </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axis</i> Axis, see <code>QwtPlot::Axis</code></dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>True, if the axis is enabled</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setAxisEnabled()</code></dl>
<h3>void QwtPlotMagnifier::rescale (doublefactor) [protected], [virtual]</h3>
<p>Zoom in/out the axes scales </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>factor</i> A value &lt; 1.0 zooms in, a value &gt; 1.0 zooms out.</dl>
<p> Implements <code>QwtMagnifier</code>.</p>
<h3>void QwtPlotMagnifier::setAxisEnabled (intaxis, boolon)</h3>
<p>En/Disable an axis. Only Axes that are enabled will be zoomed. All other axes will remain unchanged. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axis</i> Axis, see <code>QwtPlot::Axis</code><br />
 <i>on</i> On/Off</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isAxisEnabled()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
