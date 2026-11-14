---
title: "qwtplotprintfilter(3)"
name: "qwtplotprintfilter"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtplotprintfilter/"
description: "QwtPlotPrintFilter – A base class for plot print filters."
---

<p>QwtPlotPrintFilter &#8211; A base class for plot print filters. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/qwt_plot_printfilter.h">qwt_plot_printfilter.h</a>&gt; </p>
<h3>Public Types</h3>
<p>enum <code>Options</code> { <code>PrintMargin</code> = 1, <code>PrintTitle</code> = 2, <code>PrintLegend</code> = 4, <code>PrintGrid</code> = 8, <code>PrintBackground</code> = 16, <code>PrintFrameWithScales</code> = 32, <code>PrintAll</code> = ~PrintFrameWithScales } </p>
<p> enum <code>Item</code> { <code>Title</code>, <code>Legend</code>, <code>Curve</code>, <code>CurveSymbol</code>, <code>Marker</code>, <code>MarkerSymbol</code>, <code>MajorGrid</code>, <code>MinorGrid</code>, <code>CanvasBackground</code>, <code>AxisScale</code>, <code>AxisTitle</code>, <code>WidgetBackground</code> } </p>
<h3>Public Member Functions</h3>
<p><code>QwtPlotPrintFilter</code> () </p>
<p> virtual <code>~QwtPlotPrintFilter</code> () </p>
<p> virtual QColor <code>color</code> (const QColor &amp;, <code>Item</code> item) const </p>
<p> virtual QFont <code>font</code> (const QFont &amp;, <code>Item</code> item) const </p>
<p> void <code>setOptions</code> (int options) </p>
<p> int <code>options</code> () const </p>
<p> virtual void <code>apply</code> (<code>QwtPlot</code> *) const </p>
<p> virtual void <code>reset</code> (<code>QwtPlot</code> *) const </p>
<p> virtual void <code>apply</code> (<code>QwtPlotItem</code> *) const </p>
<p> virtual void <code>reset</code> (<code>QwtPlotItem</code> *) const </p>
<h2>Detailed Description</h2>
<p>A base class for plot print filters. </p>
<p> A print filter can be used to customize <code>QwtPlot::print()</code>. </p>
<p> <code>Deprecated</code></p>
<dl COMPACT>
<dd>In Qwt 5.0 the design of <code>QwtPlot</code> allows/recommends writing individual QwtPlotItems, that are not known to <code>QwtPlotPrintFilter</code>. So this concept is outdated and <code>QwtPlotPrintFilter</code> will be removed/replaced in Qwt 6.x.</dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtPlotPrintFilter::Item</code></h3>
<p>Print items. </p>
<h3>enum <code>QwtPlotPrintFilter::Options</code></h3>
<p>Print options. </p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPlotPrintFilter::QwtPlotPrintFilter () [explicit]</h3>
<p>Sets filter options to PrintAll</p>
<h3>QwtPlotPrintFilter::~QwtPlotPrintFilter () [virtual]</h3>
<p>Destructor. </p>
<h2>Member Function Documentation</h2>
<h3>void QwtPlotPrintFilter::apply (<code>QwtPlot</code> * plot) const [virtual]</h3>
<p>Change color and fonts of a plot </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>apply()</code></dl>
<h3>QColor QwtPlotPrintFilter::color (const QColor &amp; c, <code>Item</code> item) const [virtual]</h3>
<p>Modifies a color for printing. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>c</i> Color to be modified<br />
 <i>item</i> Type of item where the color belongs</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Modified color.</dl>
<p> In case of !(<code>QwtPlotPrintFilter::options()</code> &amp; PrintBackground) MajorGrid is modified to Qt::darkGray, MinorGrid to Qt::gray. All other colors are returned unmodified.</p>
<h3>QFont QwtPlotPrintFilter::font (const QFont &amp; f, <code>Item</code> item) const [virtual]</h3>
<p>Modifies a font for printing. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>f</i> Font to be modified<br />
 <i>item</i> Type of item where the font belongs</dl>
<p> All fonts are returned unmodified</p>
<h3>int QwtPlotPrintFilter::options () const</h3>
<p>Get plot print options. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>setOptions()</code></dl>
<h3>void QwtPlotPrintFilter::reset (<code>QwtPlot</code> * plot) const [virtual]</h3>
<p>Reset color and fonts of a plot </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>apply()</code></dl>
<h3>void QwtPlotPrintFilter::setOptions (int options)</h3>
<p>Set plot print options. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>options</i> Or&#8217;d <code>QwtPlotPrintFilter::Options</code> values</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>options()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
