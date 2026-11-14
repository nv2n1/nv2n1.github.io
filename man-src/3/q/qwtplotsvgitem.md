---
title: "qwtplotsvgitem(3)"
name: "qwtplotsvgitem"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtplotsvgitem/"
description: "QwtPlotSvgItem –"
---

<p>QwtPlotSvgItem &#8211; </p>
<p> A plot item, which displays data in Scalable Vector Graphics (SVG) format.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_plot_svgitem.h&gt; </p>
<p> Inherits <code>QwtPlotItem</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtPlotSvgItem</code> (const QString &amp;<code>title</code>=QString::null)<br />
 <i>Constructor. </i><br />
 <code>QwtPlotSvgItem</code> (const <code>QwtText</code> &amp;<code>title</code>)<br />
 <i>Constructor. </i><br />
 virtual <code>~QwtPlotSvgItem</code> ()<br />
 <i>Destructor. </i><br />
 bool <code>loadFile</code> (const QRectF &amp;, const QString &amp;fileName) </p>
<p> bool <code>loadData</code> (const QRectF &amp;, const QByteArray &amp;) </p>
<p> virtual QRectF <code>boundingRect</code> () const<br />
 <i>Bounding rectangle of the item. </i><br />
 virtual void <code>draw</code> (QPainter *p, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;rect) const </p>
<p> virtual int <code>rtti</code> () const </p>
<h3>Protected Member Functions</h3>
<p>const QSvgRenderer &amp; <code>renderer</code> () const </p>
<p> QSvgRenderer &amp; <code>renderer</code> () </p>
<p> void <code>render</code> (QPainter *painter, const QRectF &amp;<code>viewBox</code>, const QRectF &amp;rect) const </p>
<p> QRectF <code>viewBox</code> (const QRectF &amp;area) const </p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p>A plot item, which displays data in Scalable Vector Graphics (SVG) format. </p>
<p> SVG images are often used to display maps</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPlotSvgItem::QwtPlotSvgItem (const QString &amp;title = QString::null) [explicit]</h3>
<p>Constructor. Sets the following item attributes:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd><code>QwtPlotItem::AutoScale</code>: true</p>
<dt>&bull;</p>
<dd><code>QwtPlotItem::Legend</code>: false</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>title</i> Title</dl>
<h3>QwtPlotSvgItem::QwtPlotSvgItem (const <code>QwtText</code> &amp;title) [explicit]</h3>
<p>Constructor. Sets the following item attributes:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd><code>QwtPlotItem::AutoScale</code>: true</p>
<dt>&bull;</p>
<dd><code>QwtPlotItem::Legend</code>: false</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>title</i> Title</dl>
<h2>Member Function Documentation</h2>
<h3>void QwtPlotSvgItem::draw (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect) const [virtual]</h3>
<p>Draw the SVG item </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>xMap</i> X-Scale Map<br />
 <i>yMap</i> Y-Scale Map<br />
 <i>canvasRect</i> Contents rect of the plot canvas</dl>
<p> Implements <code>QwtPlotItem</code>.</p>
<h3>bool QwtPlotSvgItem::loadData (const QRectF &amp;rect, const QByteArray &amp;data)</h3>
<p>Load SVG data </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rect</i> Bounding rectangle<br />
 <i>data</i> in SVG format</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true, if the SVG data could be loaded</dl>
<h3>bool QwtPlotSvgItem::loadFile (const QRectF &amp;rect, const QString &amp;fileName)</h3>
<p>Load a SVG file </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rect</i> Bounding rectangle<br />
 <i>fileName</i> SVG file name</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true, if the SVG file could be loaded</dl>
<h3>void QwtPlotSvgItem::render (QPainter *painter, const QRectF &amp;viewBox, const QRectF &amp;rect) const [protected]</h3>
<p>Render the SVG data </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>viewBox</i> View Box, see QSvgRenderer::viewBox()<br />
 <i>rect</i> Target rectangle on the paint device</dl>
<h3>const QSvgRenderer &amp; QwtPlotSvgItem::renderer () const [protected]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Renderer used to render the SVG data</dl>
<h3>QSvgRenderer &amp; QwtPlotSvgItem::renderer () [protected]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Renderer used to render the SVG data</dl>
<h3>int QwtPlotSvgItem::rtti () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd><code>QwtPlotItem::Rtti_PlotSVG</code></dl>
<p> Reimplemented from <code>QwtPlotItem</code>.</p>
<h3>QRectF QwtPlotSvgItem::viewBox (const QRectF &amp;rect) const [protected]</h3>
<p>Calculate the view box from rect and <code>boundingRect()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rect</i> Rectangle in scale coordinates</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>View box, see QSvgRenderer::viewBox()</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
