---
title: "qwtplotshapeitem(3)"
name: "qwtplotshapeitem"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtplotshapeitem/"
description: "QwtPlotShapeItem –"
---

<p>QwtPlotShapeItem &#8211; </p>
<p> A plot item, which displays any graphical shape, that can be defined by a QPainterPath.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_plot_shapeitem.h&gt; </p>
<p> Inherits <code>QwtPlotItem</code>.</p>
<h3>Public Types</h3>
<p>enum <code>PaintAttribute</code> { <code>ClipPolygons</code> = 0x01 } </p>
<p> enum <code>LegendMode</code> { <code>LegendShape</code>, <code>LegendColor</code> }<br />
 <i>Mode how to display the item on the legend. </i><br />
 typedef QFlags&lt; <code>PaintAttribute</code> &gt; <code>PaintAttributes</code><br />
 <i>Paint attributes. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtPlotShapeItem</code> (const QString &amp;<code>title</code>=QString::null)<br />
 <i>Constructor. </i><br />
 <code>QwtPlotShapeItem</code> (const <code>QwtText</code> &amp;<code>title</code>)<br />
 <i>Constructor. </i><br />
 virtual <code>~QwtPlotShapeItem</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setPaintAttribute</code> (<code>PaintAttribute</code>, bool on=true) </p>
<p> bool <code>testPaintAttribute</code> (<code>PaintAttribute</code>) const </p>
<p> void <code>setLegendMode</code> (<code>LegendMode</code>) </p>
<p> <code>LegendMode</code> <code>legendMode</code> () const </p>
<p> void <code>setRect</code> (const QRectF &amp;)<br />
 <i>Set a path built from a rectangle. </i><br />
 void <code>setPolygon</code> (const QPolygonF &amp;)<br />
 <i>Set a path built from a polygon. </i><br />
 void <code>setShape</code> (const QPainterPath &amp;)<br />
 <i>Set the shape to be displayed. </i><br />
 QPainterPath <code>shape</code> () const </p>
<p> void <code>setPen</code> (const QColor &amp;, qreal width=0.0, Qt::PenStyle=Qt::SolidLine) </p>
<p> void <code>setPen</code> (const QPen &amp;)<br />
 <i>Assign a pen. </i><br />
 QPen <code>pen</code> () const </p>
<p> void <code>setBrush</code> (const QBrush &amp;) </p>
<p> QBrush <code>brush</code> () const </p>
<p> void <code>setRenderTolerance</code> (double)<br />
 <i>Set the tolerance for the weeding optimization. </i><br />
 double <code>renderTolerance</code> () const </p>
<p> virtual QRectF <code>boundingRect</code> () const<br />
 <i>Bounding rectangle of the shape. </i><br />
 virtual void <code>draw</code> (QPainter *p, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;rect) const </p>
<p> virtual <code>QwtGraphic</code> <code>legendIcon</code> (int index, const QSizeF &amp;) const </p>
<p> virtual int <code>rtti</code> () const </p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p>A plot item, which displays any graphical shape, that can be defined by a QPainterPath. </p>
<p> A QPainterPath is a shape composed from intersecting and uniting regions, rectangles, ellipses or irregular areas defined by lines, and curves. <code>QwtPlotShapeItem</code> displays a shape with a pen and brush. </p>
<p> <code>QwtPlotShapeItem</code> offers a couple of optimizations like clipping or weeding. These algorithms need to convert the painter path into polygons that might be less performant for paths built from curves and ellipses. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>QwtPlotZone</dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtPlotShapeItem::LegendMode</code></h3>
<p>Mode how to display the item on the legend. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>LegendShape </i></p>
<dd>Display a scaled down version of the shape.</p>
<dt><i>LegendColor </i></p>
<dd>Display a filled rectangle.</dl>
<h3>enum <code>QwtPlotShapeItem::PaintAttribute</code></h3>
<p>Attributes to modify the drawing algorithm. The default disables all attributes </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPaintAttribute()</code>, <code>testPaintAttribute()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>ClipPolygons </i></p>
<dd>Clip polygons before painting them. In situations, where points are far outside the visible area (f.e when zooming deep) this might be a substantial improvement for the painting performance</dl>
<p> But polygon clipping will convert the painter path into polygons what might introduce a negative impact on the performance of paths composed from curves or ellipses.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPlotShapeItem::QwtPlotShapeItem (const QString &amp;title = QString::null) [explicit]</h3>
<p>Constructor. Sets the following item attributes:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd><code>QwtPlotItem::AutoScale</code>: true</p>
<dt>&bull;</p>
<dd><code>QwtPlotItem::Legend</code>: false</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>title</i> Title</dl>
<h3>QwtPlotShapeItem::QwtPlotShapeItem (const <code>QwtText</code> &amp;title) [explicit]</h3>
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
<h3>QBrush QwtPlotShapeItem::brush () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Brush used to fill the shape</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBrush()</code>, <code>pen()</code></dl>
<h3>void QwtPlotShapeItem::draw (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect) const [virtual]</h3>
<p>Draw the shape item </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>xMap</i> X-Scale Map<br />
 <i>yMap</i> Y-Scale Map<br />
 <i>canvasRect</i> Contents rect of the plot canvas</dl>
<p> Implements <code>QwtPlotItem</code>.</p>
<h3><code>QwtGraphic</code> QwtPlotShapeItem::legendIcon (intindex, const QSizeF &amp;size) const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>A rectangle filled with the color of the brush ( or the pen )</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>index</i> Index of the legend entry ( usually there is only one )<br />
 <i>size</i> Icon size</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLegendIconSize()</code>, <code>legendData()</code></dl>
<p> Reimplemented from <code>QwtPlotItem</code>.</p>
<h3><code>QwtPlotShapeItem::LegendMode</code> QwtPlotShapeItem::legendMode () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Mode how to represent the item on the legend</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>legendMode()</code></dl>
<h3>QPen QwtPlotShapeItem::pen () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Pen used to draw the outline of the shape</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPen()</code>, <code>brush()</code></dl>
<h3>double QwtPlotShapeItem::renderTolerance () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Tolerance for the weeding optimization</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setRenderTolerance()</code></dl>
<h3>int QwtPlotShapeItem::rtti () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd><code>QwtPlotItem::Rtti_PlotShape</code></dl>
<p> Reimplemented from <code>QwtPlotItem</code>.</p>
<h3>void QwtPlotShapeItem::setBrush (const QBrush &amp;brush)</h3>
<p>Assign a brush. </p>
<p> The brush is used to fill the path </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>brush</i> Brush</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>brush()</code>, <code>pen()</code></dl>
<h3>void QwtPlotShapeItem::setLegendMode (<code>LegendMode</code>mode)</h3>
<p>Set the mode how to represent the item on the legend </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>mode</i> Mode</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>legendMode()</code></dl>
<h3>void QwtPlotShapeItem::setPaintAttribute (<code>PaintAttribute</code>attribute, boolon = true)</h3>
<p>Specify an attribute how to draw the shape </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>attribute</i> Paint attribute<br />
 <i>on</i> On/Off</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>testPaintAttribute()</code></dl>
<h3>void QwtPlotShapeItem::setPen (const QColor &amp;color, qrealwidth = 0.0, Qt::PenStylestyle = Qt::SolidLine)</h3>
<p>Build and assign a pen </p>
<p> In Qt5 the default pen width is 1.0 ( 0.0 in Qt4 ) what makes it non cosmetic ( see QPen::isCosmetic() ). This method has been introduced to hide this incompatibility. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>color</i> Pen color<br />
 <i>width</i> Pen width<br />
 <i>style</i> Pen style</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>pen()</code>, <code>brush()</code></dl>
<h3>void QwtPlotShapeItem::setPen (const QPen &amp;pen)</h3>
<p>Assign a pen. The pen is used to draw the outline of the shape </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pen</i> Pen</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>pen()</code>, <code>brush()</code></dl>
<h3>void QwtPlotShapeItem::setPolygon (const QPolygonF &amp;polygon)</h3>
<p>Set a path built from a polygon. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>polygon</i> Polygon</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setShape()</code>, <code>setRect()</code>, <code>shape()</code></dl>
<h3>void QwtPlotShapeItem::setRect (const QRectF &amp;rect)</h3>
<p>Set a path built from a rectangle. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rect</i> Rectangle</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setShape()</code>, <code>setPolygon()</code>, <code>shape()</code></dl>
<h3>void QwtPlotShapeItem::setRenderTolerance (doubletolerance)</h3>
<p>Set the tolerance for the weeding optimization. After translating the shape into target device coordinate ( usually widget geometries ) the painter path can be simplified by a point weeding algorithm ( Douglas-Peucker ). </p>
<p> For shapes built from curves and ellipses weeding might have the opposite effect because they have to be expanded to polygons. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>tolerance</i> Accepted error when reducing the number of points A value &lt;= 0.0 disables weeding.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>renderTolerance()</code>, <code>QwtWeedingCurveFitter</code></dl>
<h3>void QwtPlotShapeItem::setShape (const QPainterPath &amp;shape)</h3>
<p>Set the shape to be displayed. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>shape</i> Shape</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setShape()</code>, <code>shape()</code></dl>
<h3>QPainterPath QwtPlotShapeItem::shape () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Shape to be displayed</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setShape()</code></dl>
<h3>bool QwtPlotShapeItem::testPaintAttribute (<code>PaintAttribute</code>attribute) const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, when attribute is enabled</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPaintAttribute()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
