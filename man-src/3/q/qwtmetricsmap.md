---
title: "qwtmetricsmap(3)"
name: "qwtmetricsmap"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtmetricsmap/"
description: "QwtMetricsMap – A Map to translate between layout, screen and paint device metrics."
---

<p>QwtMetricsMap &#8211; A Map to translate between layout, screen and paint device metrics. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/qwt_layout_metrics.h">qwt_layout_metrics.h</a>&gt; </p>
<h3>Public Member Functions</h3>
<p>bool <code>isIdentity</code> () const </p>
<p> void <code>setMetrics</code> (const QPaintDevice *layoutMetrics, const QPaintDevice *deviceMetrics) </p>
<p> int <code>layoutToDeviceX</code> (int x) const </p>
<p> int <code>deviceToLayoutX</code> (int x) const </p>
<p> int <code>screenToLayoutX</code> (int x) const </p>
<p> int <code>layoutToScreenX</code> (int x) const </p>
<p> int <code>layoutToDeviceY</code> (int y) const </p>
<p> int <code>deviceToLayoutY</code> (int y) const </p>
<p> int <code>screenToLayoutY</code> (int y) const </p>
<p> int <code>layoutToScreenY</code> (int y) const </p>
<p> QPoint <code>layoutToDevice</code> (const QPoint &amp;, const QPainter *=NULL) const </p>
<p> QPoint <code>deviceToLayout</code> (const QPoint &amp;, const QPainter *=NULL) const </p>
<p> QPoint <code>screenToLayout</code> (const QPoint &amp;) const </p>
<p> QPoint <code>layoutToScreen</code> (const QPoint &amp;point) const </p>
<p> QSize <code>layoutToDevice</code> (const QSize &amp;) const </p>
<p> QSize <code>deviceToLayout</code> (const QSize &amp;) const </p>
<p> QSize <code>screenToLayout</code> (const QSize &amp;) const </p>
<p> QSize <code>layoutToScreen</code> (const QSize &amp;) const </p>
<p> QRect <code>layoutToDevice</code> (const QRect &amp;, const QPainter *=NULL) const </p>
<p> QRect <code>deviceToLayout</code> (const QRect &amp;, const QPainter *=NULL) const </p>
<p> QRect <code>screenToLayout</code> (const QRect &amp;) const </p>
<p> QRect <code>layoutToScreen</code> (const QRect &amp;) const </p>
<p> QwtPolygon <code>layoutToDevice</code> (const QwtPolygon &amp;, const QPainter *=NULL) const </p>
<p> QwtPolygon <code>deviceToLayout</code> (const QwtPolygon &amp;, const QPainter *=NULL) const </p>
<h3>Static Public Member Functions</h3>
<p>static QwtPolygon <code>translate</code> (const QMatrix &amp;, const QwtPolygon &amp;) </p>
<p> static QRect <code>translate</code> (const QMatrix &amp;, const QRect &amp;) </p>
<h2>Detailed Description</h2>
<p>A Map to translate between layout, screen and paint device metrics. </p>
<p> Qt3 supports painting in integer coordinates only. Therefore it is not possible to scale the layout in screen coordinates to layouts in higher resolutions ( f.e printing ) without losing the higher precision. <code>QwtMetricsMap</code> is used to incorporate the various widget attributes ( always in screen resolution ) into the layout/printing code of <code>QwtPlot</code>. </p>
<p> Qt4 is able to paint floating point based coordinates, what makes it possible always to render in screen coordinates ( with a common scale factor ). <code>QwtMetricsMap</code> will be obsolete as soon as Qt3 support has been dropped ( Qwt 6.x ).</p>
<h2>Member Function Documentation</h2>
<h3>QRect QwtMetricsMap::translate (const QMatrix &amp; m, const QRect &amp; rect) [static]</h3>
<p>Wrapper for QMatrix::mapRect. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>m</i> Matrix<br />
 <i>rect</i> Rectangle to translate</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Translated rectangle</dl>
<h3>QwtPolygon QwtMetricsMap::translate (const QMatrix &amp; m, const QwtPolygon &amp; pa) [static]</h3>
<p>Wrapper for QMatrix::map. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>m</i> Matrix<br />
 <i>pa</i> Polygon to translate</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Translated polygon</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
