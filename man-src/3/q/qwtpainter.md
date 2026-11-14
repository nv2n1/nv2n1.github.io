---
title: "qwtpainter(3)"
name: "qwtpainter"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtpainter/"
description: "QwtPainter –"
---

<p>QwtPainter &#8211; </p>
<p> A collection of QPainter workarounds.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_painter.h&gt;</p>
<h3>Static Public Member Functions</h3>
<p>static void <code>setPolylineSplitting</code> (bool)<br />
 <i>En/Disable line splitting for the raster paint engine. </i><br />
 static bool <code>polylineSplitting</code> () </p>
<p> static void <code>setRoundingAlignment</code> (bool) </p>
<p> static bool <code>roundingAlignment</code> () </p>
<p> static bool <code>roundingAlignment</code> (QPainter *) </p>
<p> static void <code>drawText</code> (QPainter *, double x, double y, const QString &amp;)<br />
 <i>Wrapper for QPainter::drawText() </i><br />
 static void <code>drawText</code> (QPainter *, const QPointF &amp;, const QString &amp;)<br />
 <i>Wrapper for QPainter::drawText() </i><br />
 static void <code>drawText</code> (QPainter *, double x, double y, double w, double h, int flags, const QString &amp;)<br />
 <i>Wrapper for QPainter::drawText() </i><br />
 static void <code>drawText</code> (QPainter *, const QRectF &amp;, int flags, const QString &amp;)<br />
 <i>Wrapper for QPainter::drawText() </i><br />
 static void <code>drawSimpleRichText</code> (QPainter *, const QRectF &amp;, int flags, const QTextDocument &amp;) </p>
<p> static void <code>drawRect</code> (QPainter *, double x, double y, double w, double h)<br />
 <i>Wrapper for QPainter::drawRect() </i><br />
 static void <code>drawRect</code> (QPainter *, const QRectF &amp;rect)<br />
 <i>Wrapper for QPainter::drawRect() </i><br />
 static void <code>fillRect</code> (QPainter *, const QRectF &amp;, const QBrush &amp;)<br />
 <i>Wrapper for QPainter::fillRect() </i><br />
 static void <code>drawEllipse</code> (QPainter *, const QRectF &amp;)<br />
 <i>Wrapper for QPainter::drawEllipse() </i><br />
 static void <code>drawPie</code> (QPainter *, const QRectF &amp;r, int a, int alen)<br />
 <i>Wrapper for QPainter::drawPie() </i><br />
 static void <code>drawLine</code> (QPainter *, double x1, double y1, double x2, double y2)<br />
 <i>Wrapper for QPainter::drawLine() </i><br />
 static void <code>drawLine</code> (QPainter *, const QPointF &amp;p1, const QPointF &amp;p2)<br />
 <i>Wrapper for QPainter::drawLine() </i><br />
 static void <code>drawLine</code> (QPainter *, const QLineF &amp;)<br />
 <i>Wrapper for QPainter::drawLine() </i><br />
 static void <code>drawPolygon</code> (QPainter *, const QPolygonF &amp;)<br />
 <i>Wrapper for QPainter::drawPolygon() </i><br />
 static void <code>drawPolyline</code> (QPainter *, const QPolygonF &amp;)<br />
 <i>Wrapper for QPainter::drawPolyline() </i><br />
 static void <code>drawPolyline</code> (QPainter *, const QPointF *, int pointCount)<br />
 <i>Wrapper for QPainter::drawPolyline() </i><br />
 static void <code>drawPolygon</code> (QPainter *, const QPolygon &amp;)<br />
 <i>Wrapper for QPainter::drawPolygon() </i><br />
 static void <code>drawPolyline</code> (QPainter *, const QPolygon &amp;)<br />
 <i>Wrapper for QPainter::drawPolyline() </i><br />
 static void <code>drawPolyline</code> (QPainter *, const QPoint *, int pointCount)<br />
 <i>Wrapper for QPainter::drawPolyline() </i><br />
 static void <code>drawPoint</code> (QPainter *, const QPoint &amp;)<br />
 <i>Wrapper for QPainter::drawPoint() </i><br />
 static void <code>drawPoints</code> (QPainter *, const QPolygon &amp;)<br />
 <i>Wrapper for QPainter::drawPoints() </i><br />
 static void <code>drawPoints</code> (QPainter *, const QPoint *, int pointCount)<br />
 <i>Wrapper for QPainter::drawPoints() </i><br />
 static void <code>drawPoint</code> (QPainter *, double x, double y)<br />
 <i>Wrapper for QPainter::drawPoint() </i><br />
 static void <code>drawPoint</code> (QPainter *, const QPointF &amp;)<br />
 <i>Wrapper for QPainter::drawPoint() </i><br />
 static void <code>drawPoints</code> (QPainter *, const QPolygonF &amp;)<br />
 <i>Wrapper for QPainter::drawPoints() </i><br />
 static void <code>drawPoints</code> (QPainter *, const QPointF *, int pointCount)<br />
 <i>Wrapper for QPainter::drawPoints() </i><br />
 static void <code>drawPath</code> (QPainter *, const QPainterPath &amp;)<br />
 <i>Wrapper for QPainter::drawPath() </i><br />
 static void <code>drawImage</code> (QPainter *, const QRectF &amp;, const QImage &amp;)<br />
 <i>Wrapper for QPainter::drawImage() </i><br />
 static void <code>drawPixmap</code> (QPainter *, const QRectF &amp;, const QPixmap &amp;)<br />
 <i>Wrapper for QPainter::drawPixmap() </i><br />
 static void <code>drawRoundFrame</code> (QPainter *, const QRectF &amp;, const QPalette &amp;, int lineWidth, int frameStyle) </p>
<p> static void <code>drawRoundedFrame</code> (QPainter *, const QRectF &amp;, double xRadius, double yRadius, const QPalette &amp;, int lineWidth, int frameStyle) </p>
<p> static void <code>drawFrame</code> (QPainter *, const QRectF &amp;rect, const QPalette &amp;palette, QPalette::ColorRole foregroundRole, int lineWidth, int midLineWidth, int frameStyle) </p>
<p> static void <code>drawFocusRect</code> (QPainter *, const QWidget *)<br />
 <i>Draw a focus rectangle on a widget using its style. </i><br />
 static void <code>drawFocusRect</code> (QPainter *, const QWidget *, const QRect &amp;)<br />
 <i>Draw a focus rectangle on a widget using its style. </i><br />
 static void <code>drawColorBar</code> (QPainter *painter, const <code>QwtColorMap</code> &amp;, const <code>QwtInterval</code> &amp;, const <code>QwtScaleMap</code> &amp;, Qt::Orientation, const QRectF &amp;) </p>
<p> static bool <code>isAligning</code> (QPainter *painter) </p>
<p> static bool <code>isX11GraphicsSystem</code> () </p>
<p> static void <code>fillPixmap</code> (const QWidget *, QPixmap &amp;, const QPoint &amp;offset=QPoint()) </p>
<p> static void <code>drawBackgound</code> (QPainter *painter, const QRectF &amp;rect, const QWidget *widget) </p>
<p> static QPixmap <code>backingStore</code> (QWidget *, const QSize &amp;) </p>
<h2>Detailed Description</h2>
<p>A collection of QPainter workarounds.</p>
<h2>Member Function Documentation</h2>
<h3>QPixmap QwtPainter::backingStore (QWidget *widget, const QSize &amp;size) [static]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>A pixmap that can be used as backing store</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>widget</i> Widget, for which the backinstore is intended<br />
 <i>size</i> Size of the pixmap</dl>
<h3>void QwtPainter::drawBackgound (QPainter *painter, const QRectF &amp;rect, const QWidget *widget) [static]</h3>
<p>Fill rect with the background of a widget </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>rect</i> Rectangle to be filled<br />
 <i>widget</i> Widget</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>QStyle::PE_Widget, QWidget::backgroundRole()</dl>
<h3>void QwtPainter::drawColorBar (QPainter *painter, const <code>QwtColorMap</code> &amp;colorMap, const <code>QwtInterval</code> &amp;interval, const <code>QwtScaleMap</code> &amp;scaleMap, Qt::Orientationorientation, const QRectF &amp;rect) [static]</h3>
<p>Draw a color bar into a rectangle </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>colorMap</i> Color map<br />
 <i>interval</i> Value range<br />
 <i>scaleMap</i> Scale map<br />
 <i>orientation</i> Orientation<br />
 <i>rect</i> Traget rectangle</dl>
<h3>void QwtPainter::drawFrame (QPainter *painter, const QRectF &amp;rect, const QPalette &amp;palette, QPalette::ColorRoleforegroundRole, intframeWidth, intmidLineWidth, intframeStyle) [static]</h3>
<p>Draw a rectangular frame </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>rect</i> Frame rectangle<br />
 <i>palette</i> Palette<br />
 <i>foregroundRole</i> Foreground role used for QFrame::Plain<br />
 <i>frameWidth</i> Frame width<br />
 <i>midLineWidth</i> Used for QFrame::Box<br />
 <i>frameStyle</i> bitwise OR´ed value of QFrame::Shape and QFrame::Shadow</dl>
<h3>void QwtPainter::drawRoundedFrame (QPainter *painter, const QRectF &amp;rect, doublexRadius, doubleyRadius, const QPalette &amp;palette, intlineWidth, intframeStyle) [static]</h3>
<p>Draw a rectangular frame with rounded borders </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>rect</i> Frame rectangle<br />
 <i>xRadius</i> x-radius of the ellipses defining the corners<br />
 <i>yRadius</i> y-radius of the ellipses defining the corners<br />
 <i>palette</i> QPalette::WindowText is used for plain borders QPalette::Dark and QPalette::Light for raised or sunken borders<br />
 <i>lineWidth</i> Line width<br />
 <i>frameStyle</i> bitwise OR´ed value of QFrame::Shape and QFrame::Shadow</dl>
<h3>void QwtPainter::drawRoundFrame (QPainter *painter, const QRectF &amp;rect, const QPalette &amp;palette, intlineWidth, intframeStyle) [static]</h3>
<p>Draw a round frame </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>rect</i> Frame rectangle<br />
 <i>palette</i> QPalette::WindowText is used for plain borders QPalette::Dark and QPalette::Light for raised or sunken borders<br />
 <i>lineWidth</i> Line width<br />
 <i>frameStyle</i> bitwise OR´ed value of QFrame::Shape and QFrame::Shadow</dl>
<h3>void QwtPainter::drawSimpleRichText (QPainter *painter, const QRectF &amp;rect, intflags, const QTextDocument &amp;text) [static]</h3>
<p>Draw a text document into a rectangle </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>rect</i> Traget rectangle<br />
 <i>flags</i> Alignments/Text flags, see QPainter::drawText()<br />
 <i>text</i> Text document</dl>
<h3>void QwtPainter::fillPixmap (const QWidget *widget, QPixmap &amp;pixmap, const QPoint &amp;offset = QPoint()) [static]</h3>
<p>Fill a pixmap with the content of a widget </p>
<p> In Qt &gt;= 5.0 QPixmap::fill() is a nop, in Qt 4.x it is buggy for backgrounds with gradients. Thus <code>fillPixmap()</code> offers an alternative implementation. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>widget</i> Widget<br />
 <i>pixmap</i> Pixmap to be filled<br />
 <i>offset</i> Offset</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>QPixmap::fill()</dl>
<h3>bool QwtPainter::isAligning (QPainter *painter) [static]</h3>
<p>Check if the painter is using a paint engine, that aligns coordinates to integers. Today these are all paint engines beside QPaintEngine::Pdf and QPaintEngine::SVG. </p>
<p> If we have an integer based paint engine it is also checked if the painter has a transformation matrix, that rotates or scales. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true, when the painter is aligning</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setRoundingAlignment()</code></dl>
<h3>bool QwtPainter::isX11GraphicsSystem () [static]</h3>
<p>Check is the application is running with the X11 graphics system that has some special capabilities that can be used for incremental painting to a widget. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>True, when the graphics system is X11</dl>
<h3>bool QwtPainter::polylineSplitting () [inline], [static]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, when line splitting for the raster paint engine is enabled.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPolylineSplitting()</code></dl>
<h3>bool QwtPainter::roundingAlignment () [inline], [static]</h3>
<p>Check whether coordinates should be rounded, before they are painted to a paint engine that rounds to integer values. For other paint engines ( PDF, SVG ), this flag has no effect. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>True, when rounding is enabled</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setRoundingAlignment()</code>, <code>isAligning()</code></dl>
<h3>bool QwtPainter::roundingAlignment (QPainter *painter) [inline], [static]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd><code>roundingAlignment()</code> &amp;&amp; isAligning(painter);</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter</dl>
<h3>void QwtPainter::setPolylineSplitting (boolenable) [static]</h3>
<p>En/Disable line splitting for the raster paint engine. In some Qt versions the raster paint engine paints polylines of many points much faster when they are split in smaller chunks: f.e all supported Qt versions &gt;= Qt 5.0 when drawing an antialiased polyline with a pen width &gt;=2. </p>
<p> The default setting is true. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>polylineSplitting()</code></dl>
<h3>void QwtPainter::setRoundingAlignment (boolenable) [static]</h3>
<p>Enable whether coordinates should be rounded, before they are painted to a paint engine that floors to integer values. For other paint engines this ( PDF, SVG ), this flag has no effect. <code>QwtPainter</code> stores this flag only, the rounding itself is done in the painting code ( f.e the plot items ). </p>
<p> The default setting is true. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>roundingAlignment()</code>, <code>isAligning()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
