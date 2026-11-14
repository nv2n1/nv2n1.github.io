---
title: "qwtplotcurve(3)"
name: "qwtplotcurve"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtplotcurve/"
description: "QwtPlotCurve –"
---

<p>QwtPlotCurve &#8211; </p>
<p> A plot item, that represents a series of points.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_plot_curve.h&gt; </p>
<p> Inherits <code>QwtPlotSeriesItem</code>, and <code>QwtSeriesStore&lt; QPointF &gt;</code>.</p>
<h3>Public Types</h3>
<p>enum <code>CurveStyle</code> { <code>NoCurve</code> = -1, <code>Lines</code>, <code>Sticks</code>, <code>Steps</code>, <code>Dots</code>, <code>UserCurve</code> = 100 } </p>
<p> enum <code>CurveAttribute</code> { <code>Inverted</code> = 0x01, <code>Fitted</code> = 0x02 } </p>
<p> enum <code>LegendAttribute</code> { <code>LegendNoAttribute</code> = 0x00, <code>LegendShowLine</code> = 0x01, <code>LegendShowSymbol</code> = 0x02, <code>LegendShowBrush</code> = 0x04 } </p>
<p> enum <code>PaintAttribute</code> { <code>ClipPolygons</code> = 0x01, <code>FilterPoints</code> = 0x02, <code>MinimizeMemory</code> = 0x04, <code>ImageBuffer</code> = 0x08 } </p>
<p> typedef QFlags&lt; <code>CurveAttribute</code> &gt; <code>CurveAttributes</code><br />
 <i>Curve attributes. </i><br />
 typedef QFlags&lt; <code>LegendAttribute</code> &gt; <code>LegendAttributes</code><br />
 <i>Legend attributes. </i><br />
 typedef QFlags&lt; <code>PaintAttribute</code> &gt; <code>PaintAttributes</code><br />
 <i>Paint attributes. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtPlotCurve</code> (const QString &amp;<code>title</code>=QString::null) </p>
<p> <code>QwtPlotCurve</code> (const <code>QwtText</code> &amp;<code>title</code>) </p>
<p> virtual <code>~QwtPlotCurve</code> ()<br />
 <i>Destructor. </i><br />
 virtual int <code>rtti</code> () const </p>
<p> void <code>setPaintAttribute</code> (<code>PaintAttribute</code>, bool on=true) </p>
<p> bool <code>testPaintAttribute</code> (<code>PaintAttribute</code>) const </p>
<p> void <code>setLegendAttribute</code> (<code>LegendAttribute</code>, bool on=true) </p>
<p> bool <code>testLegendAttribute</code> (<code>LegendAttribute</code>) const </p>
<p> void <code>setRawSamples</code> (const double *xData, const double *yData, int size)<br />
 <i>Initialize the data by pointing to memory blocks which are not managed by </i><code>QwtPlotCurve</code>.<br />
 void <code>setSamples</code> (const double *xData, const double *yData, int size) </p>
<p> void <code>setSamples</code> (const QVector&lt; double &gt; &amp;xData, const QVector&lt; double &gt; &amp;yData)<br />
 <i>Initialize data with x- and y-arrays (explicitly shared) </i><br />
 void <code>setSamples</code> (const QVector&lt; QPointF &gt; &amp;) </p>
<p> void <code>setSamples</code> (<code>QwtSeriesData</code>&lt; QPointF &gt; *) </p>
<p> int <code>closestPoint</code> (const QPoint &amp;pos, double *dist=NULL) const </p>
<p> double <code>minXValue</code> () const<br />
 <i></i><code>boundingRect()</code>.left()<br />
 double <code>maxXValue</code> () const<br />
 <i></i><code>boundingRect()</code>.right()<br />
 double <code>minYValue</code> () const<br />
 <i></i><code>boundingRect()</code>.top()<br />
 double <code>maxYValue</code> () const<br />
 <i></i><code>boundingRect()</code>.bottom()<br />
 void <code>setCurveAttribute</code> (<code>CurveAttribute</code>, bool on=true) </p>
<p> bool <code>testCurveAttribute</code> (<code>CurveAttribute</code>) const </p>
<p> void <code>setPen</code> (const QColor &amp;, qreal width=0.0, Qt::PenStyle=Qt::SolidLine) </p>
<p> void <code>setPen</code> (const QPen &amp;) </p>
<p> const QPen &amp; <code>pen</code> () const </p>
<p> void <code>setBrush</code> (const QBrush &amp;)<br />
 <i>Assign a brush. </i><br />
 const QBrush &amp; <code>brush</code> () const </p>
<p> void <code>setBaseline</code> (double)<br />
 <i>Set the value of the baseline. </i><br />
 double <code>baseline</code> () const </p>
<p> void <code>setStyle</code> (<code>CurveStyle</code> <code>style</code>) </p>
<p> <code>CurveStyle</code> <code>style</code> () const </p>
<p> void <code>setSymbol</code> (<code>QwtSymbol</code> *)<br />
 <i>Assign a symbol. </i><br />
 const <code>QwtSymbol</code> * <code>symbol</code> () const </p>
<p> void <code>setCurveFitter</code> (<code>QwtCurveFitter</code> *) </p>
<p> <code>QwtCurveFitter</code> * <code>curveFitter</code> () const </p>
<p> virtual void <code>drawSeries</code> (QPainter *, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, int from, int to) const </p>
<p> virtual <code>QwtGraphic</code> <code>legendIcon</code> (int index, const QSizeF &amp;) const </p>
<h3>Protected Member Functions</h3>
<p>void <code>init</code> ()<br />
 <i>Initialize internal members. </i><br />
 virtual void <code>drawCurve</code> (QPainter *p, int <code>style</code>, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, int from, int to) const<br />
 <i>Draw the line part (without symbols) of a curve interval. </i><br />
 virtual void <code>drawSymbols</code> (QPainter *p, const <code>QwtSymbol</code> &amp;, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, int from, int to) const </p>
<p> virtual void <code>drawLines</code> (QPainter *p, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, int from, int to) const<br />
 <i>Draw lines. </i><br />
 virtual void <code>drawSticks</code> (QPainter *p, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, int from, int to) const </p>
<p> virtual void <code>drawDots</code> (QPainter *p, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, int from, int to) const </p>
<p> virtual void <code>drawSteps</code> (QPainter *p, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, int from, int to) const </p>
<p> virtual void <code>fillCurve</code> (QPainter *, const <code>QwtScaleMap</code> &amp;, const <code>QwtScaleMap</code> &amp;, const QRectF &amp;canvasRect, QPolygonF &amp;) const </p>
<p> void <code>closePolyline</code> (QPainter *, const <code>QwtScaleMap</code> &amp;, const <code>QwtScaleMap</code> &amp;, QPolygonF &amp;) const<br />
 <i>Complete a polygon to be a closed polygon including the area between the original polygon and the baseline. </i></p>
<h2>Detailed Description</h2>
<p>A plot item, that represents a series of points. </p>
<p> A curve is the representation of a series of points in the x-y plane. It supports different display styles, interpolation ( f.e. spline ) and symbols. </p>
<p> <code>Usage</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>a) Assign curve properties </code></p>
<dd>When a curve is created, it is configured to draw black solid lines with in <code>QwtPlotCurve::Lines</code> style and no symbols. You can change this by calling <code>setPen()</code>, <code>setStyle()</code> and <code>setSymbol()</code>.</p>
<dt><code>b) Connect/Assign data. </code></p>
<dd><code>QwtPlotCurve</code> gets its points using a <code>QwtSeriesData</code> object offering a bridge to the real storage of the points ( like QAbstractItemModel ). There are several convenience classes derived from <code>QwtSeriesData</code>, that also store the points inside ( like QStandardItemModel ). <code>QwtPlotCurve</code> also offers a couple of variations of <code>setSamples()</code>, that build <code>QwtSeriesData</code> objects from arrays internally.</p>
<dt><code>c) Attach the curve to a plot </code></p>
<dd>See <code>QwtPlotItem::attach()</code></dl>
</dl>
<p> <code>Example:</code></p>
<dl COMPACT>
<dd>see examples/bode</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPointSeriesData</code>, <code>QwtSymbol</code>, <code>QwtScaleMap</code></dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtPlotCurve::CurveAttribute</code></h3>
<p>Attribute for drawing the curve </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setCurveAttribute()</code>, <code>testCurveAttribute()</code>, <code>curveFitter()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>Inverted </i></p>
<dd>For <code>QwtPlotCurve::Steps</code> only. Draws a step function from the right to the left.</p>
<dt><i>Fitted </i></p>
<dd>Only in combination with <code>QwtPlotCurve::Lines</code> A <code>QwtCurveFitter</code> tries to interpolate/smooth the curve, before it is painted.</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Curve fitting requires temporary memory for calculating coefficients and additional points. If painting in <code>QwtPlotCurve::Fitted</code> mode is slow it might be better to fit the points, before they are passed to <code>QwtPlotCurve</code>.</dl>
<h3>enum <code>QwtPlotCurve::CurveStyle</code></h3>
<p>Curve styles. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setStyle()</code>, <code>style()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>NoCurve </i></p>
<dd>Don&#8217;t draw a curve. Note: This doesn&#8217;t affect the symbols.</p>
<dt><i>Lines </i></p>
<dd>Connect the points with straight lines. The lines might be interpolated depending on the &#8216;Fitted&#8217; attribute. Curve fitting can be configured using <code>setCurveFitter()</code>.</p>
<dt><i>Sticks </i></p>
<dd>Draw vertical or horizontal sticks ( depending on the <code>orientation()</code> ) from a baseline which is defined by <code>setBaseline()</code>.</p>
<dt><i>Steps </i></p>
<dd>Connect the points with a step function. The step function is drawn from the left to the right or vice versa, depending on the <code>QwtPlotCurve::Inverted</code> attribute.</p>
<dt><i>Dots </i></p>
<dd>Draw dots at the locations of the data points. Note: This is different from a dotted line (see <code>setPen()</code>), and faster as a curve in QwtPlotCurve::NoStyle style and a symbol painting a point.</p>
<dt><i>UserCurve </i></p>
<dd>Styles &gt;= <code>QwtPlotCurve::UserCurve</code> are reserved for derived classes of <code>QwtPlotCurve</code> that overload <code>drawCurve()</code> with additional application specific curve types.</dl>
<h3>enum <code>QwtPlotCurve::LegendAttribute</code></h3>
<p>Attributes how to represent the curve on the legend </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLegendAttribute()</code>, <code>testLegendAttribute()</code>, <code>QwtPlotItem::legendData()</code>, <code>legendIcon()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>LegendNoAttribute </i></p>
<dd><code>QwtPlotCurve</code> tries to find a color representing the curve and paints a rectangle with it.</p>
<dt><i>LegendShowLine </i></p>
<dd>If the <code>style()</code> is not <code>QwtPlotCurve::NoCurve</code> a line is painted with the curve <code>pen()</code>.</p>
<dt><i>LegendShowSymbol </i></p>
<dd>If the curve has a valid symbol it is painted.</p>
<dt><i>LegendShowBrush </i></p>
<dd>If the curve has a brush a rectangle filled with the curve <code>brush()</code> is painted.</dl>
<h3>enum <code>QwtPlotCurve::PaintAttribute</code></h3>
<p>Attributes to modify the drawing algorithm. The default setting enables ClipPolygons | FilterPoints </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPaintAttribute()</code>, <code>testPaintAttribute()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>ClipPolygons </i></p>
<dd>Clip polygons before painting them. In situations, where points are far outside the visible area (f.e when zooming deep) this might be a substantial improvement for the painting performance</p>
<dt><i>FilterPoints </i></p>
<dd>Tries to reduce the data that has to be painted, by sorting out duplicates, or paintings outside the visible area. Might have a notable impact on curves with many close points. Only a couple of very basic filtering algorithms are implemented.</p>
<dt><i>MinimizeMemory </i></p>
<dd>Minimize memory usage that is temporarily needed for the translated points, before they get painted. This might slow down the performance of painting</p>
<dt><i>ImageBuffer </i></p>
<dd>Render the points to a temporary image and paint the image. This is a very special optimization for Dots style, when having a huge amount of points. With a reasonable number of points QPainter::drawPoints() will be faster.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPlotCurve::QwtPlotCurve (const QString &amp;title = QString::null) [explicit]</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>title</i> Title of the curve</dl>
<h3>QwtPlotCurve::QwtPlotCurve (const <code>QwtText</code> &amp;title) [explicit]</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>title</i> Title of the curve</dl>
<h2>Member Function Documentation</h2>
<h3>double QwtPlotCurve::baseline () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Value of the baseline</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBaseline()</code></dl>
<h3>const QBrush &amp; QwtPlotCurve::brush () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Brush used to fill the area between lines and the baseline</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBrush()</code>, <code>setBaseline()</code>, <code>baseline()</code></dl>
<h3>void QwtPlotCurve::closePolyline (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, QPolygonF &amp;polygon) const [protected]</h3>
<p>Complete a polygon to be a closed polygon including the area between the original polygon and the baseline. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>xMap</i> X map<br />
 <i>yMap</i> Y map<br />
 <i>polygon</i> Polygon to be completed</dl>
<h3>int QwtPlotCurve::closestPoint (const QPoint &amp;pos, double *dist = NULL) const</h3>
<p>Find the closest curve point for a specific position </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pos</i> Position, where to look for the closest curve point<br />
 <i>dist</i> If dist != NULL, <code>closestPoint()</code> returns the distance between the position and the closest curve point</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Index of the closest curve point, or -1 if none can be found ( f.e when the curve has no points )</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd><code>closestPoint()</code> implements a dumb algorithm, that iterates over all points</dl>
<h3><code>QwtCurveFitter</code> * QwtPlotCurve::curveFitter () const</h3>
<p>Get the curve fitter. If curve fitting is disabled NULL is returned. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Curve fitter</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setCurveFitter()</code>, <code>Fitted</code></dl>
<h3>void QwtPlotCurve::drawCurve (QPainter *painter, intstyle, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, intfrom, intto) const [protected], [virtual]</h3>
<p>Draw the line part (without symbols) of a curve interval. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>style</i> curve style, see <code>QwtPlotCurve::CurveStyle</code><br />
 <i>xMap</i> x map<br />
 <i>yMap</i> y map<br />
 <i>canvasRect</i> Contents rectangle of the canvas<br />
 <i>from</i> index of the first point to be painted<br />
 <i>to</i> index of the last point to be painted</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>draw()</code>, <code>drawDots()</code>, <code>drawLines()</code>, <code>drawSteps()</code>, <code>drawSticks()</code></dl>
<h3>void QwtPlotCurve::drawDots (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, intfrom, intto) const [protected], [virtual]</h3>
<p>Draw dots </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>xMap</i> x map<br />
 <i>yMap</i> y map<br />
 <i>canvasRect</i> Contents rectangle of the canvas<br />
 <i>from</i> index of the first point to be painted<br />
 <i>to</i> index of the last point to be painted</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>draw()</code>, <code>drawCurve()</code>, <code>drawSticks()</code>, <code>drawLines()</code>, <code>drawSteps()</code></dl>
<h3>void QwtPlotCurve::drawLines (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, intfrom, intto) const [protected], [virtual]</h3>
<p>Draw lines. If the CurveAttribute Fitted is enabled a <code>QwtCurveFitter</code> tries to interpolate/smooth the curve, before it is painted. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>xMap</i> x map<br />
 <i>yMap</i> y map<br />
 <i>canvasRect</i> Contents rectangle of the canvas<br />
 <i>from</i> index of the first point to be painted<br />
 <i>to</i> index of the last point to be painted</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setCurveAttribute()</code>, <code>setCurveFitter()</code>, <code>draw()</code>, <code>drawLines()</code>, <code>drawDots()</code>, <code>drawSteps()</code>, <code>drawSticks()</code></dl>
<h3>void QwtPlotCurve::drawSeries (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, intfrom, intto) const [virtual]</h3>
<p>Draw an interval of the curve </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>xMap</i> Maps x-values into pixel coordinates.<br />
 <i>yMap</i> Maps y-values into pixel coordinates.<br />
 <i>canvasRect</i> Contents rectangle of the canvas<br />
 <i>from</i> Index of the first point to be painted<br />
 <i>to</i> Index of the last point to be painted. If to &lt; 0 the curve will be painted to its last point.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>drawCurve()</code>, <code>drawSymbols()</code>,</dl>
<p> Implements <code>QwtPlotSeriesItem</code>.</p>
<h3>void QwtPlotCurve::drawSteps (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, intfrom, intto) const [protected], [virtual]</h3>
<p>Draw step function </p>
<p> The direction of the steps depends on Inverted attribute. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>xMap</i> x map<br />
 <i>yMap</i> y map<br />
 <i>canvasRect</i> Contents rectangle of the canvas<br />
 <i>from</i> index of the first point to be painted<br />
 <i>to</i> index of the last point to be painted</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>CurveAttribute</code>, <code>setCurveAttribute()</code>, <code>draw()</code>, <code>drawCurve()</code>, <code>drawDots()</code>, <code>drawLines()</code>, <code>drawSticks()</code></dl>
<h3>void QwtPlotCurve::drawSticks (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, intfrom, intto) const [protected], [virtual]</h3>
<p>Draw sticks </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>xMap</i> x map<br />
 <i>yMap</i> y map<br />
 <i>canvasRect</i> Contents rectangle of the canvas<br />
 <i>from</i> index of the first point to be painted<br />
 <i>to</i> index of the last point to be painted</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>draw()</code>, <code>drawCurve()</code>, <code>drawDots()</code>, <code>drawLines()</code>, <code>drawSteps()</code></dl>
<h3>void QwtPlotCurve::drawSymbols (QPainter *painter, const <code>QwtSymbol</code> &amp;symbol, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, intfrom, intto) const [protected], [virtual]</h3>
<p>Draw symbols </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>symbol</i> Curve symbol<br />
 <i>xMap</i> x map<br />
 <i>yMap</i> y map<br />
 <i>canvasRect</i> Contents rectangle of the canvas<br />
 <i>from</i> Index of the first point to be painted<br />
 <i>to</i> Index of the last point to be painted</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setSymbol()</code>, <code>drawSeries()</code>, <code>drawCurve()</code></dl>
<h3>void QwtPlotCurve::fillCurve (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect, QPolygonF &amp;polygon) const [protected], [virtual]</h3>
<p>Fill the area between the curve and the baseline with the curve brush </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>xMap</i> x map<br />
 <i>yMap</i> y map<br />
 <i>canvasRect</i> Contents rectangle of the canvas<br />
 <i>polygon</i> Polygon &#8211; will be modified !</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBrush()</code>, <code>setBaseline()</code>, <code>setStyle()</code></dl>
<h3><code>QwtGraphic</code> QwtPlotCurve::legendIcon (intindex, const QSizeF &amp;size) const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Icon representing the curve on the legend</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>index</i> Index of the legend entry ( ignored as there is only one )<br />
 <i>size</i> Icon size</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlotItem::setLegendIconSize()</code>, <code>QwtPlotItem::legendData()</code></dl>
<p> Reimplemented from <code>QwtPlotItem</code>.</p>
<h3>const QPen &amp; QwtPlotCurve::pen () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Pen used to draw the lines</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPen()</code>, <code>brush()</code></dl>
<h3>int QwtPlotCurve::rtti () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd><code>QwtPlotItem::Rtti_PlotCurve</code></dl>
<p> Reimplemented from <code>QwtPlotItem</code>.</p>
<h3>void QwtPlotCurve::setBaseline (doublevalue)</h3>
<p>Set the value of the baseline. The baseline is needed for filling the curve with a brush or the Sticks drawing style. </p>
<p> The interpretation of the baseline depends on the <code>orientation()</code>. With Qt::Horizontal, the baseline is interpreted as a horizontal line at y = <code>baseline()</code>, with Qt::Vertical, it is interpreted as a vertical line at x = <code>baseline()</code>. </p>
<p> The default value is 0.0. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Value of the baseline</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>baseline()</code>, <code>setBrush()</code>, <code>setStyle()</code>, QwtPlotAbstractSeriesItem::orientation()</dl>
<h3>void QwtPlotCurve::setBrush (const QBrush &amp;brush)</h3>
<p>Assign a brush. In case of brush.style() != QBrush::NoBrush and <code>style()</code> != <code>QwtPlotCurve::Sticks</code> the area between the curve and the baseline will be filled. </p>
<p> In case !brush.color().isValid() the area will be filled by pen.color(). The fill algorithm simply connects the first and the last curve point to the baseline. So the curve data has to be sorted (ascending or descending). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>brush</i> New brush</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>brush()</code>, <code>setBaseline()</code>, <code>baseline()</code></dl>
<h3>void QwtPlotCurve::setCurveAttribute (<code>CurveAttribute</code>attribute, boolon = true)</h3>
<p>Specify an attribute for drawing the curve </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>attribute</i> Curve attribute<br />
 <i>on</i> On/Off</dl>
<p> /sa <code>testCurveAttribute()</code>, <code>setCurveFitter()</code></p>
<h3>void QwtPlotCurve::setCurveFitter (<code>QwtCurveFitter</code> *curveFitter)</h3>
<p>Assign a curve fitter </p>
<p> The curve fitter &#8216;smooths&#8217; the curve points, when the Fitted CurveAttribute is set. setCurveFitter(NULL) also disables curve fitting. </p>
<p> The curve fitter operates on the translated points ( = widget coordinates) to be functional for logarithmic scales. Obviously this is less performant for fitting algorithms, that reduce the number of points. </p>
<p> For situations, where curve fitting is used to improve the performance of painting huge series of points it might be better to execute the fitter on the curve points once and to cache the result in the <code>QwtSeriesData</code> object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i></i><code>curveFitter()</code> Curve fitter</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>Fitted</code></dl>
<h3>void QwtPlotCurve::setLegendAttribute (<code>LegendAttribute</code>attribute, boolon = true)</h3>
<p>Specify an attribute how to draw the legend icon </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>attribute</i> Attribute<br />
 <i>on</i> On/Off /sa <code>testLegendAttribute()</code>. <code>legendIcon()</code></dl>
<h3>void QwtPlotCurve::setPaintAttribute (<code>PaintAttribute</code>attribute, boolon = true)</h3>
<p>Specify an attribute how to draw the curve </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>attribute</i> Paint attribute<br />
 <i>on</i> On/Off</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>testPaintAttribute()</code></dl>
<h3>void QwtPlotCurve::setPen (const QColor &amp;color, qrealwidth = 0.0, Qt::PenStylestyle = Qt::SolidLine)</h3>
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
<h3>void QwtPlotCurve::setPen (const QPen &amp;pen)</h3>
<p>Assign a pen </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pen</i> New pen</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>pen()</code>, <code>brush()</code></dl>
<h3>void QwtPlotCurve::setRawSamples (const double *xData, const double *yData, intsize)</h3>
<p>Initialize the data by pointing to memory blocks which are not managed by <code>QwtPlotCurve</code>. setRawSamples is provided for efficiency. It is important to keep the pointers during the lifetime of the underlying <code>QwtCPointerData</code> class. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>xData</i> pointer to x data<br />
 <i>yData</i> pointer to y data<br />
 <i>size</i> size of x and y</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtCPointerData</code></dl>
<h3>void QwtPlotCurve::setSamples (const double *xData, const double *yData, intsize)</h3>
<p>Set data by copying x- and y-values from specified memory blocks. Contrary to <code>setRawSamples()</code>, this function makes a &#8216;deep copy&#8217; of the data. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>xData</i> pointer to x values<br />
 <i>yData</i> pointer to y values<br />
 <i>size</i> size of xData and yData</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPointArrayData</code></dl>
<h3>void QwtPlotCurve::setSamples (const QVector&lt; double &gt; &amp;xData, const QVector&lt; double &gt; &amp;yData)</h3>
<p>Initialize data with x- and y-arrays (explicitly shared) </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>xData</i> x data<br />
 <i>yData</i> y data</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPointArrayData</code></dl>
<h3>void QwtPlotCurve::setSamples (const QVector&lt; QPointF &gt; &amp;samples)</h3>
<p>Initialize data with an array of points. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>samples</i> Vector of points</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>QVector is implicitly shared </p>
<p> QPolygonF is derived from QVector&lt;QPointF&gt;</dl>
<h3>void QwtPlotCurve::setSamples (<code>QwtSeriesData</code>&lt; QPointF &gt; *data)</h3>
<p>Assign a series of points </p>
<p> <code>setSamples()</code> is just a wrapper for <code>setData()</code> without any additional value &#8211; beside that it is easier to find for the developer. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> Data</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The item takes ownership of the data object, deleting it when its not used anymore.</dl>
<h3>void QwtPlotCurve::setStyle (<code>CurveStyle</code>style)</h3>
<p>Set the curve&#8217;s drawing style </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>style</i> Curve style</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>style()</code></dl>
<h3>void QwtPlotCurve::setSymbol (<code>QwtSymbol</code> *symbol)</h3>
<p>Assign a symbol. The curve will take the ownership of the symbol, hence the previously set symbol will be delete by setting a new one. If symbol is NULL no symbol will be drawn. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>symbol</i> Symbol</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>symbol()</code></dl>
<h3><code>QwtPlotCurve::CurveStyle</code> QwtPlotCurve::style () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Style of the curve</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setStyle()</code></dl>
<h3>const <code>QwtSymbol</code> * QwtPlotCurve::symbol () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Current symbol or NULL, when no symbol has been assigned</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setSymbol()</code></dl>
<h3>bool QwtPlotCurve::testCurveAttribute (<code>CurveAttribute</code>attribute) const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>true, if attribute is enabled</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setCurveAttribute()</code></dl>
<h3>bool QwtPlotCurve::testLegendAttribute (<code>LegendAttribute</code>attribute) const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, when attribute is enabled</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLegendAttribute()</code></dl>
<h3>bool QwtPlotCurve::testPaintAttribute (<code>PaintAttribute</code>attribute) const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, when attribute is enabled</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPaintAttribute()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
