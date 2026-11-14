---
title: "qwtplotscaleitem(3)"
name: "qwtplotscaleitem"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtplotscaleitem/"
description: "QwtPlotScaleItem –"
---

<p>QwtPlotScaleItem &#8211; </p>
<p> A class which draws a scale inside the plot canvas.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_plot_scaleitem.h&gt; </p>
<p> Inherits <code>QwtPlotItem</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtPlotScaleItem</code> (<code>QwtScaleDraw::Alignment</code>=<code>QwtScaleDraw::BottomScale</code>, const double pos=0.0)<br />
 <i>Constructor for scale item at the position pos. </i><br />
 virtual <code>~QwtPlotScaleItem</code> ()<br />
 <i>Destructor. </i><br />
 virtual int <code>rtti</code> () const </p>
<p> void <code>setScaleDiv</code> (const <code>QwtScaleDiv</code> &amp;)<br />
 <i>Assign a scale division. </i><br />
 const <code>QwtScaleDiv</code> &amp; <code>scaleDiv</code> () const </p>
<p> void <code>setScaleDivFromAxis</code> (bool on) </p>
<p> bool <code>isScaleDivFromAxis</code> () const </p>
<p> void <code>setPalette</code> (const QPalette &amp;) </p>
<p> QPalette <code>palette</code> () const </p>
<p> void <code>setFont</code> (const QFont &amp;) </p>
<p> QFont <code>font</code> () const </p>
<p> void <code>setScaleDraw</code> (<code>QwtScaleDraw</code> *)<br />
 <i>Set a scale draw. </i><br />
 const <code>QwtScaleDraw</code> * <code>scaleDraw</code> () const </p>
<p> <code>QwtScaleDraw</code> * <code>scaleDraw</code> () </p>
<p> void <code>setPosition</code> (double pos) </p>
<p> double <code>position</code> () const </p>
<p> void <code>setBorderDistance</code> (int numPixels)<br />
 <i>Align the scale to the canvas. </i><br />
 int <code>borderDistance</code> () const </p>
<p> void <code>setAlignment</code> (<code>QwtScaleDraw::Alignment</code>) </p>
<p> virtual void <code>draw</code> (QPainter *p, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;rect) const<br />
 <i>Draw the scale. </i><br />
 virtual void <code>updateScaleDiv</code> (const <code>QwtScaleDiv</code> &amp;, const <code>QwtScaleDiv</code> &amp;)<br />
 <i>Update the item to changes of the axes scale division. </i></p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p>A class which draws a scale inside the plot canvas. </p>
<p> <code>QwtPlotScaleItem</code> can be used to draw an axis inside the plot canvas. It might by synchronized to one of the axis of the plot, but can also display its own ticks and labels. </p>
<p> It is allowed to synchronize the scale item with a disabled axis. In plots with vertical and horizontal scale items, it might be necessary to remove ticks at the intersections, by overloading <code>updateScaleDiv()</code>. </p>
<p> The scale might be at a specific position (f.e 0.0) or it might be aligned to a canvas border. </p>
<p> <code>Example</code></p>
<dl COMPACT>
<dd>The following example shows how to replace the left axis, by a scale item at the x position 0.0. </p>
<pre>QwtPlotScaleItem *scaleItem =
 new QwtPlotScaleItem(QwtScaleDraw::RightScale, 0.0);
scaleItem-&gt;setFont(plot-&gt;axisWidget(QwtPlot::yLeft)-&gt;font());
scaleItem-&gt;attach(plot);
plot-&gt;enableAxis(QwtPlot::yLeft, false);</pre>
<p>&nbsp;<wbr></dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPlotScaleItem::QwtPlotScaleItem (<code>QwtScaleDraw::Alignment</code>alignment = <code>QwtScaleDraw::BottomScale</code>, const doublepos = 0.0) [explicit]</h3>
<p>Constructor for scale item at the position pos. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>alignment</i> In case of <code>QwtScaleDraw::BottomScale</code> or <code>QwtScaleDraw::TopScale</code> the scale item is corresponding to the <code>xAxis()</code>, otherwise it corresponds to the <code>yAxis()</code>.<br />
 <i>pos</i> x or y position, depending on the corresponding axis.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPosition()</code>, <code>setAlignment()</code></dl>
<h2>Member Function Documentation</h2>
<h3>int QwtPlotScaleItem::borderDistance () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Distance from a canvas border</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBorderDistance()</code>, <code>setPosition()</code></dl>
<h3>QFont QwtPlotScaleItem::font () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>tick label font</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setFont()</code></dl>
<h3>bool QwtPlotScaleItem::isScaleDivFromAxis () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, if the synchronization of the scale division with the corresponding axis is enabled.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setScaleDiv()</code>, <code>setScaleDivFromAxis()</code></dl>
<h3>QPalette QwtPlotScaleItem::palette () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>palette</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPalette()</code></dl>
<h3>double QwtPlotScaleItem::position () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Position of the scale</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPosition()</code>, <code>setAlignment()</code></dl>
<h3>int QwtPlotScaleItem::rtti () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd><code>QwtPlotItem::Rtti_PlotScale</code></dl>
<p> Reimplemented from <code>QwtPlotItem</code>.</p>
<h3>const <code>QwtScaleDiv</code> &amp; QwtPlotScaleItem::scaleDiv () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Scale division</dl>
<h3>const <code>QwtScaleDraw</code> * QwtPlotScaleItem::scaleDraw () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Scale draw</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setScaleDraw()</code></dl>
<h3><code>QwtScaleDraw</code> * QwtPlotScaleItem::scaleDraw ()</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Scale draw</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setScaleDraw()</code></dl>
<h3>void QwtPlotScaleItem::setAlignment (<code>QwtScaleDraw::Alignment</code>alignment)</h3>
<p>Change the alignment of the scale </p>
<p> The alignment sets the orientation of the scale and the position of the ticks: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd><code>QwtScaleDraw::BottomScale</code>: horizontal, ticks below</p>
<dt>&bull;</p>
<dd><code>QwtScaleDraw::TopScale</code>: horizontal, ticks above</p>
<dt>&bull;</p>
<dd><code>QwtScaleDraw::LeftScale</code>: vertical, ticks left</p>
<dt>&bull;</p>
<dd><code>QwtScaleDraw::RightScale</code>: vertical, ticks right</dl>
<p> For horizontal scales the position corresponds to <code>QwtPlotItem::yAxis()</code>, otherwise to <code>QwtPlotItem::xAxis()</code>. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>scaleDraw()</code>, <code>QwtScaleDraw::alignment()</code>, <code>setPosition()</code></dl>
<h3>void QwtPlotScaleItem::setBorderDistance (intdistance)</h3>
<p>Align the scale to the canvas. If distance is &gt;= 0 the scale will be aligned to a border of the contents rectangle of the canvas. If alignment() is <code>QwtScaleDraw::LeftScale</code>, the scale will be aligned to the right border, if it is <code>QwtScaleDraw::TopScale</code> it will be aligned to the bottom (and vice versa), </p>
<p> If distance is &lt; 0 the scale will be at the <code>position()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>distance</i> Number of pixels between the canvas border and the backbone of the scale.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPosition()</code>, <code>borderDistance()</code></dl>
<h3>void QwtPlotScaleItem::setFont (const QFont &amp;font)</h3>
<p>Change the tick label font </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>font()</code></dl>
<h3>void QwtPlotScaleItem::setPalette (const QPalette &amp;palette)</h3>
<p>Set the palette </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtAbstractScaleDraw::draw()</code>, <code>palette()</code></dl>
<h3>void QwtPlotScaleItem::setPosition (doublepos)</h3>
<p>Change the position of the scale </p>
<p> The position is interpreted as y value for horizontal axes and as x value for vertical axes. </p>
<p> The border distance is set to -1. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pos</i> New position</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>position()</code>, <code>setAlignment()</code></dl>
<h3>void QwtPlotScaleItem::setScaleDiv (const <code>QwtScaleDiv</code> &amp;scaleDiv)</h3>
<p>Assign a scale division. When assigning a scaleDiv the scale division won&#8217;t be synchronized with the corresponding axis anymore. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>scaleDiv</i> Scale division</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>scaleDiv()</code>, <code>setScaleDivFromAxis()</code>, <code>isScaleDivFromAxis()</code></dl>
<h3>void QwtPlotScaleItem::setScaleDivFromAxis (boolon)</h3>
<p>Enable/Disable the synchronization of the scale division with the corresponding axis. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>on</i> true/false</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isScaleDivFromAxis()</code></dl>
<h3>void QwtPlotScaleItem::setScaleDraw (<code>QwtScaleDraw</code> *scaleDraw)</h3>
<p>Set a scale draw. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>scaleDraw</i> object responsible for drawing scales.</dl>
<p> The main use case for replacing the default <code>QwtScaleDraw</code> is to overload <code>QwtAbstractScaleDraw::label</code>, to replace or swallow tick labels. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>scaleDraw()</code></dl>
<h3>void QwtPlotScaleItem::updateScaleDiv (const <code>QwtScaleDiv</code> &amp;xScaleDiv, const <code>QwtScaleDiv</code> &amp;yScaleDiv) [virtual]</h3>
<p>Update the item to changes of the axes scale division. In case of <code>isScaleDivFromAxis()</code>, the scale draw is synchronized to the correspond axis. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>xScaleDiv</i> Scale division of the x-axis<br />
 <i>yScaleDiv</i> Scale division of the y-axis</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlot::updateAxes()</code></dl>
<p> Reimplemented from <code>QwtPlotItem</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
