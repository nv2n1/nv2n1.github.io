---
title: "qwtplotdirectpainter(3)"
name: "qwtplotdirectpainter"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtplotdirectpainter/"
description: "QwtPlotDirectPainter –"
---

<p>QwtPlotDirectPainter &#8211; </p>
<p> Painter object trying to paint incrementally.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_plot_directpainter.h&gt; </p>
<p> Inherits QObject.</p>
<h3>Public Types</h3>
<p>enum <code>Attribute</code> { <code>AtomicPainter</code> = 0x01, <code>FullRepaint</code> = 0x02, <code>CopyBackingStore</code> = 0x04 }<br />
 <i>Paint attributes. </i><br />
 typedef QFlags&lt; <code>Attribute</code> &gt; <code>Attributes</code><br />
 <i>Paint attributes. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtPlotDirectPainter</code> (QObject *parent=NULL)<br />
 <i>Constructor. </i><br />
 virtual <code>~QwtPlotDirectPainter</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setAttribute</code> (<code>Attribute</code>, bool on) </p>
<p> bool <code>testAttribute</code> (<code>Attribute</code>) const </p>
<p> void <code>setClipping</code> (bool) </p>
<p> bool <code>hasClipping</code> () const </p>
<p> void <code>setClipRegion</code> (const QRegion &amp;)<br />
 <i>Assign a clip region and enable clipping. </i><br />
 QRegion <code>clipRegion</code> () const </p>
<p> void <code>drawSeries</code> (<code>QwtPlotSeriesItem</code> *, int from, int to)<br />
 <i>Draw a set of points of a seriesItem. </i><br />
 void <code>reset</code> ()<br />
 <i>Close the internal QPainter. </i><br />
 virtual bool <code>eventFilter</code> (QObject *, QEvent *)<br />
 <i>Event filter. </i></p>
<h2>Detailed Description</h2>
<p>Painter object trying to paint incrementally. </p>
<p> Often applications want to display samples while they are collected. When there are too many samples complete replots will be expensive to be processed in a collection cycle. </p>
<p> <code>QwtPlotDirectPainter</code> offers an API to paint subsets ( f.e all additions points ) without erasing/repainting the plot canvas. </p>
<p> On certain environments it might be important to calculate a proper clip region before painting. F.e. for Qt Embedded only the clipped part of the backing store will be copied to a ( maybe unaccelerated ) frame buffer. </p>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>Incremental painting will only help when no replot is triggered by another operation ( like changing scales ) and nothing needs to be erased.</dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtPlotDirectPainter::Attribute</code></h3>
<p>Paint attributes. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setAttribute()</code>, <code>testAttribute()</code>, <code>drawSeries()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>AtomicPainter </i></p>
<dd>Initializing a QPainter is an expensive operation. When AtomicPainter is set each call of <code>drawSeries()</code> opens/closes a temporary QPainter. Otherwise <code>QwtPlotDirectPainter</code> tries to use the same QPainter as long as possible.</p>
<dt><i>FullRepaint </i></p>
<dd>When FullRepaint is set the plot canvas is explicitly repainted after the samples have been rendered.</p>
<dt><i>CopyBackingStore </i></p>
<dd>When <code>QwtPlotCanvas::BackingStore</code> is enabled the painter has to paint to the backing store and the widget. In certain situations/environments it might be faster to paint to the backing store only and then copy the backing store to the canvas. This flag can also be useful for settings, where Qt fills the the clip region with the widget background.</dl>
<h2>Member Function Documentation</h2>
<h3>QRegion QwtPlotDirectPainter::clipRegion () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Currently set clip region.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setClipRegion()</code>, <code>setClipping()</code>, <code>hasClipping()</code></dl>
<h3>void QwtPlotDirectPainter::drawSeries (<code>QwtPlotSeriesItem</code> *seriesItem, intfrom, intto)</h3>
<p>Draw a set of points of a seriesItem. When observing an measurement while it is running, new points have to be added to an existing seriesItem. <code>drawSeries()</code> can be used to display them avoiding a complete redraw of the canvas. </p>
<p> Setting plot()-&gt;canvas()-&gt;setAttribute(Qt::WA_PaintOutsidePaintEvent, true); will result in faster painting, if the paint engine of the canvas widget supports this feature. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>seriesItem</i> Item to be painted<br />
 <i>from</i> Index of the first point to be painted<br />
 <i>to</i> Index of the last point to be painted. If to &lt; 0 the series will be painted to its last point.</dl>
<h3>bool QwtPlotDirectPainter::hasClipping () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>true, when clipping is enabled</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setClipping()</code>, <code>clipRegion()</code>, <code>setClipRegion()</code></dl>
<h3>void QwtPlotDirectPainter::setAttribute (<code>Attribute</code>attribute, boolon)</h3>
<p>Change an attribute </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>attribute</i> Attribute to change<br />
 <i>on</i> On/Off</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>Attribute</code>, <code>testAttribute()</code></dl>
<h3>void QwtPlotDirectPainter::setClipping (boolenable)</h3>
<p>En/Disables clipping </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>enable</i> Enables clipping is true, disable it otherwise</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>hasClipping()</code>, <code>clipRegion()</code>, <code>setClipRegion()</code></dl>
<h3>void QwtPlotDirectPainter::setClipRegion (const QRegion &amp;region)</h3>
<p>Assign a clip region and enable clipping. Depending on the environment setting a proper clip region might improve the performance heavily. F.e. on Qt embedded only the clipped part of the backing store will be copied to a ( maybe unaccelerated ) frame buffer device. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>region</i> Clip region</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>clipRegion()</code>, <code>hasClipping()</code>, <code>setClipping()</code></dl>
<h3>bool QwtPlotDirectPainter::testAttribute (<code>Attribute</code>attribute) const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, when attribute is enabled</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>attribute</i> Attribute to be tested</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>Attribute</code>, <code>setAttribute()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
