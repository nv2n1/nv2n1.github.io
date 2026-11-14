---
title: "qwtnullpaintdevice(3)"
name: "qwtnullpaintdevice"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtnullpaintdevice/"
description: "QwtNullPaintDevice –"
---

<p>QwtNullPaintDevice &#8211; </p>
<p> A null paint device doing nothing.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_null_paintdevice.h&gt; </p>
<p> Inherits QPaintDevice. </p>
<p> Inherited by <code>QwtGraphic</code>, and QwtStyleSheetRecorder.</p>
<h3>Public Types</h3>
<p>enum <code>Mode</code> { <code>NormalMode</code>, <code>PolygonPathMode</code>, <code>PathMode</code> }<br />
 <i>Render mode. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtNullPaintDevice</code> ()<br />
 <i>Constructor. </i><br />
 virtual <code>~QwtNullPaintDevice</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setMode</code> (<code>Mode</code>) </p>
<p> <code>Mode</code> <code>mode</code> () const </p>
<p> virtual QPaintEngine * <code>paintEngine</code> () const<br />
 <i>See QPaintDevice::paintEngine() </i><br />
 virtual int <code>metric</code> (PaintDeviceMetric metric) const </p>
<p> virtual void <code>drawRects</code> (const QRect *, int)<br />
 <i>See QPaintEngine::drawRects() </i><br />
 virtual void <code>drawRects</code> (const QRectF *, int)<br />
 <i>See QPaintEngine::drawRects() </i><br />
 virtual void <code>drawLines</code> (const QLine *, int)<br />
 <i>See QPaintEngine::drawLines() </i><br />
 virtual void <code>drawLines</code> (const QLineF *, int)<br />
 <i>See QPaintEngine::drawLines() </i><br />
 virtual void <code>drawEllipse</code> (const QRectF &amp;)<br />
 <i>See QPaintEngine::drawEllipse() </i><br />
 virtual void <code>drawEllipse</code> (const QRect &amp;)<br />
 <i>See QPaintEngine::drawEllipse() </i><br />
 virtual void <code>drawPath</code> (const QPainterPath &amp;)<br />
 <i>See QPaintEngine::drawPath() </i><br />
 virtual void <code>drawPoints</code> (const QPointF *, int)<br />
 <i>See QPaintEngine::drawPoints() </i><br />
 virtual void <code>drawPoints</code> (const QPoint *, int)<br />
 <i>See QPaintEngine::drawPoints() </i><br />
 virtual void <code>drawPolygon</code> (const QPointF *, int, QPaintEngine::PolygonDrawMode)<br />
 <i>See QPaintEngine::drawPolygon() </i><br />
 virtual void <code>drawPolygon</code> (const QPoint *, int, QPaintEngine::PolygonDrawMode)<br />
 <i>See QPaintEngine::drawPolygon() </i><br />
 virtual void <code>drawPixmap</code> (const QRectF &amp;, const QPixmap &amp;, const QRectF &amp;)<br />
 <i>See QPaintEngine::drawPixmap() </i><br />
 virtual void <code>drawTextItem</code> (const QPointF &amp;, const QTextItem &amp;)<br />
 <i>See QPaintEngine::drawTextItem() </i><br />
 virtual void <code>drawTiledPixmap</code> (const QRectF &amp;, const QPixmap &amp;, const QPointF &amp;s)<br />
 <i>See QPaintEngine::drawTiledPixmap() </i><br />
 virtual void <code>drawImage</code> (const QRectF &amp;, const QImage &amp;, const QRectF &amp;, Qt::ImageConversionFlags)<br />
 <i>See QPaintEngine::drawImage() </i><br />
 virtual void <code>updateState</code> (const QPaintEngineState &amp;state)<br />
 <i>See QPaintEngine::updateState() </i></p>
<h3>Protected Member Functions</h3>
<p>virtual QSize <code>sizeMetrics</code> () const =0 </p>
<h2>Detailed Description</h2>
<p>A null paint device doing nothing. </p>
<p> Sometimes important layout/rendering geometries are not available or changeable from the public Qt class interface. ( f.e hidden in the style implementation ). </p>
<p> <code>QwtNullPaintDevice</code> can be used to manipulate or filter out this information by analyzing the stream of paint primitives. </p>
<p> F.e. <code>QwtNullPaintDevice</code> is used by <code>QwtPlotCanvas</code> to identify styled backgrounds with rounded corners.</p>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtNullPaintDevice::Mode</code></h3>
<p>Render mode. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setMode()</code>, <code>mode()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>NormalMode </i></p>
<dd>All vector graphic primitives are painted by the corresponding draw methods</p>
<dt><i>PolygonPathMode </i></p>
<dd>Vector graphic primitives ( beside polygons ) are mapped to a QPainterPath and are painted by drawPath. In PathMode mode only a few draw methods are called:</dl>
<dl COMPACT>
<dt>&bull;</p>
<dd><code>drawPath()</code></p>
<dt>&bull;</p>
<dd><code>drawPixmap()</code></p>
<dt>&bull;</p>
<dd><code>drawImage()</code></p>
<dt>&bull;</p>
<dd><code>drawPolygon()</code></dl>
<dl COMPACT>
<dt><i>PathMode </i></p>
<dd>Vector graphic primitives are mapped to a QPainterPath and are painted by drawPath. In PathMode mode only a few draw methods are called:</dl>
<dl COMPACT>
<dt>&bull;</p>
<dd><code>drawPath()</code></p>
<dt>&bull;</p>
<dd><code>drawPixmap()</code></p>
<dt>&bull;</p>
<dd><code>drawImage()</code></dl>
<h2>Member Function Documentation</h2>
<h3>int QwtNullPaintDevice::metric (PaintDeviceMetricdeviceMetric) const [virtual]</h3>
<p>See QPaintDevice::metric() </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>deviceMetric</i> Type of metric</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Metric information for the given paint device metric.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>sizeMetrics()</code></dl>
<h3><code>QwtNullPaintDevice::Mode</code> QwtNullPaintDevice::mode () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Render mode</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setMode()</code></dl>
<h3>void QwtNullPaintDevice::setMode (<code>Mode</code>mode)</h3>
<p>Set the render mode </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>mode</i> New mode</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>mode()</code></dl>
<h3>virtual QSize QwtNullPaintDevice::sizeMetrics () const [protected], [pure virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Size needed to implement <code>metric()</code></dl>
<p> Implemented in <code>QwtGraphic</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
