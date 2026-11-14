---
title: "qwtplotmarker(3)"
name: "qwtplotmarker"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtplotmarker/"
description: "QwtPlotMarker –"
---

<p>QwtPlotMarker &#8211; </p>
<p> A class for drawing markers.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_plot_marker.h&gt; </p>
<p> Inherits <code>QwtPlotItem</code>.</p>
<h3>Public Types</h3>
<p>enum <code>LineStyle</code> { <code>NoLine</code>, <code>HLine</code>, <code>VLine</code>, <code>Cross</code> } </p>
<h3>Public Member Functions</h3>
<p><code>QwtPlotMarker</code> (const QString &amp;<code>title</code>=QString::null)<br />
 <i>Sets alignment to Qt::AlignCenter, and style to </i><code>QwtPlotMarker::NoLine</code>.<br />
 <code>QwtPlotMarker</code> (const <code>QwtText</code> &amp;<code>title</code>)<br />
 <i>Sets alignment to Qt::AlignCenter, and style to </i><code>QwtPlotMarker::NoLine</code>.<br />
 virtual <code>~QwtPlotMarker</code> ()<br />
 <i>Destructor. </i><br />
 virtual int <code>rtti</code> () const </p>
<p> double <code>xValue</code> () const<br />
 <i>Return x Value. </i><br />
 double <code>yValue</code> () const<br />
 <i>Return y Value. </i><br />
 QPointF <code>value</code> () const<br />
 <i>Return Value. </i><br />
 void <code>setXValue</code> (double)<br />
 <i>Set X Value. </i><br />
 void <code>setYValue</code> (double)<br />
 <i>Set Y Value. </i><br />
 void <code>setValue</code> (double, double)<br />
 <i>Set Value. </i><br />
 void <code>setValue</code> (const QPointF &amp;)<br />
 <i>Set Value. </i><br />
 void <code>setLineStyle</code> (<code>LineStyle</code> st)<br />
 <i>Set the line style. </i><br />
 <code>LineStyle</code> <code>lineStyle</code> () const </p>
<p> void <code>setLinePen</code> (const QColor &amp;, qreal width=0.0, Qt::PenStyle=Qt::SolidLine) </p>
<p> void <code>setLinePen</code> (const QPen &amp;p) </p>
<p> const QPen &amp; <code>linePen</code> () const </p>
<p> void <code>setSymbol</code> (const <code>QwtSymbol</code> *)<br />
 <i>Assign a symbol. </i><br />
 const <code>QwtSymbol</code> * <code>symbol</code> () const </p>
<p> void <code>setLabel</code> (const <code>QwtText</code> &amp;)<br />
 <i>Set the label. </i><br />
 <code>QwtText</code> <code>label</code> () const </p>
<p> void <code>setLabelAlignment</code> (Qt::Alignment)<br />
 <i>Set the alignment of the label. </i><br />
 Qt::Alignment <code>labelAlignment</code> () const </p>
<p> void <code>setLabelOrientation</code> (Qt::Orientation)<br />
 <i>Set the orientation of the label. </i><br />
 Qt::Orientation <code>labelOrientation</code> () const </p>
<p> void <code>setSpacing</code> (int)<br />
 <i>Set the spacing. </i><br />
 int <code>spacing</code> () const </p>
<p> virtual void <code>draw</code> (QPainter *p, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;) const </p>
<p> virtual QRectF <code>boundingRect</code> () const </p>
<p> virtual <code>QwtGraphic</code> <code>legendIcon</code> (int index, const QSizeF &amp;) const </p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>drawLines</code> (QPainter *, const QRectF &amp;, const QPointF &amp;) const </p>
<p> virtual void <code>drawLabel</code> (QPainter *, const QRectF &amp;, const QPointF &amp;) const </p>
<h2>Detailed Description</h2>
<p>A class for drawing markers. </p>
<p> A marker can be a horizontal line, a vertical line, a symbol, a label or any combination of them, which can be drawn around a center point inside a bounding rectangle. </p>
<p> The <code>setSymbol()</code> member assigns a symbol to the marker. The symbol is drawn at the specified point. </p>
<p> With <code>setLabel()</code>, a label can be assigned to the marker. The <code>setLabelAlignment()</code> member specifies where the label is drawn. All the Align*-constants in Qt::AlignmentFlags (see Qt documentation) are valid. The interpretation of the alignment depends on the marker&#8217;s line style. The alignment refers to the center point of the marker, which means, for example, that the label would be printed left above the center point if the alignment was set to Qt::AlignLeft | Qt::AlignTop. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd><code>QwtPlotTextLabel</code> is intended to align a text label according to the geometry of canvas ( unrelated to plot coordinates )</dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtPlotMarker::LineStyle</code></h3>
<p>Line styles. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLineStyle()</code>, <code>lineStyle()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>NoLine </i></p>
<dd>No line.</p>
<dt><i>HLine </i></p>
<dd>A horizontal line.</p>
<dt><i>VLine </i></p>
<dd>A vertical line.</p>
<dt><i>Cross </i></p>
<dd>A crosshair.</dl>
<h2>Member Function Documentation</h2>
<h3>QRectF QwtPlotMarker::boundingRect () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>An invalid bounding rect: QRectF(1.0, 1.0, -2.0, -2.0)</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>A width or height &lt; 0.0 is ignored by the autoscaler</dl>
<p> Reimplemented from <code>QwtPlotItem</code>.</p>
<h3>void QwtPlotMarker::draw (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect) const [virtual]</h3>
<p>Draw the marker </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>xMap</i> x Scale Map<br />
 <i>yMap</i> y Scale Map<br />
 <i>canvasRect</i> Contents rectangle of the canvas in painter coordinates</dl>
<p> Implements <code>QwtPlotItem</code>.</p>
<h3>void QwtPlotMarker::drawLabel (QPainter *painter, const QRectF &amp;canvasRect, const QPointF &amp;pos) const [protected], [virtual]</h3>
<p>Align and draw the text label of the marker </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>canvasRect</i> Contents rectangle of the canvas in painter coordinates<br />
 <i>pos</i> Position of the marker, translated into widget coordinates</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>drawLabel()</code>, <code>QwtSymbol::drawSymbol()</code></dl>
<h3>void QwtPlotMarker::drawLines (QPainter *painter, const QRectF &amp;canvasRect, const QPointF &amp;pos) const [protected], [virtual]</h3>
<p>Draw the lines marker </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>canvasRect</i> Contents rectangle of the canvas in painter coordinates<br />
 <i>pos</i> Position of the marker, translated into widget coordinates</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>drawLabel()</code>, <code>QwtSymbol::drawSymbol()</code></dl>
<h3><code>QwtText</code> QwtPlotMarker::label () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the label</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLabel()</code></dl>
<h3>Qt::Alignment QwtPlotMarker::labelAlignment () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the label alignment</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLabelAlignment()</code>, <code>setLabelOrientation()</code></dl>
<h3>Qt::Orientation QwtPlotMarker::labelOrientation () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the label orientation</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLabelOrientation()</code>, <code>labelAlignment()</code></dl>
<h3><code>QwtGraphic</code> QwtPlotMarker::legendIcon (intindex, const QSizeF &amp;size) const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Icon representing the marker on the legend</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>index</i> Index of the legend entry ( usually there is only one )<br />
 <i>size</i> Icon size</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLegendIconSize()</code>, <code>legendData()</code></dl>
<p> Reimplemented from <code>QwtPlotItem</code>.</p>
<h3>const QPen &amp; QwtPlotMarker::linePen () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the line pen</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLinePen()</code></dl>
<h3><code>QwtPlotMarker::LineStyle</code> QwtPlotMarker::lineStyle () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the line style</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLineStyle()</code></dl>
<h3>int QwtPlotMarker::rtti () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd><code>QwtPlotItem::Rtti_PlotMarker</code></dl>
<p> Reimplemented from <code>QwtPlotItem</code>.</p>
<h3>void QwtPlotMarker::setLabel (const <code>QwtText</code> &amp;label)</h3>
<p>Set the label. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>label</i> Label text</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>label()</code></dl>
<h3>void QwtPlotMarker::setLabelAlignment (Qt::Alignmentalign)</h3>
<p>Set the alignment of the label. In case of <code>QwtPlotMarker::HLine</code> the alignment is relative to the y position of the marker, but the horizontal flags correspond to the canvas rectangle. In case of <code>QwtPlotMarker::VLine</code> the alignment is relative to the x position of the marker, but the vertical flags correspond to the canvas rectangle. </p>
<p> In all other styles the alignment is relative to the marker&#8217;s position. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>align</i> Alignment.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>labelAlignment()</code>, <code>labelOrientation()</code></dl>
<h3>void QwtPlotMarker::setLabelOrientation (Qt::Orientationorientation)</h3>
<p>Set the orientation of the label. When orientation is Qt::Vertical the label is rotated by 90.0 degrees ( from bottom to top ). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>orientation</i> Orientation of the label</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>labelOrientation()</code>, <code>setLabelAlignment()</code></dl>
<h3>void QwtPlotMarker::setLinePen (const QColor &amp;color, qrealwidth = 0.0, Qt::PenStylestyle = Qt::SolidLine)</h3>
<p>Build and assign a line pen </p>
<p> In Qt5 the default pen width is 1.0 ( 0.0 in Qt4 ) what makes it non cosmetic ( see QPen::isCosmetic() ). This method has been introduced to hide this incompatibility. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>color</i> Pen color<br />
 <i>width</i> Pen width<br />
 <i>style</i> Pen style</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>pen(), brush()</dl>
<h3>void QwtPlotMarker::setLinePen (const QPen &amp;pen)</h3>
<p>Specify a pen for the line. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pen</i> New pen</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>linePen()</code></dl>
<h3>void QwtPlotMarker::setLineStyle (<code>LineStyle</code>style)</h3>
<p>Set the line style. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>style</i> Line style.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>lineStyle()</code></dl>
<h3>void QwtPlotMarker::setSpacing (intspacing)</h3>
<p>Set the spacing. When the label is not centered on the marker position, the spacing is the distance between the position and the label. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>spacing</i> Spacing</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>spacing()</code>, <code>setLabelAlignment()</code></dl>
<h3>void QwtPlotMarker::setSymbol (const <code>QwtSymbol</code> *symbol)</h3>
<p>Assign a symbol. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>symbol</i> New symbol</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>symbol()</code></dl>
<h3>int QwtPlotMarker::spacing () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the spacing</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setSpacing()</code></dl>
<h3>const <code>QwtSymbol</code> * QwtPlotMarker::symbol () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the symbol</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setSymbol()</code>, <code>QwtSymbol</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
