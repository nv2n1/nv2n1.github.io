---
title: "qwtsymbol(3)"
name: "qwtsymbol"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtsymbol/"
description: "QwtSymbol –"
---

<p>QwtSymbol &#8211; </p>
<p> A class for drawing symbols.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_symbol.h&gt;</p>
<h3>Public Types</h3>
<p>enum <code>Style</code> { <code>NoSymbol</code> = -1, <code>Ellipse</code>, <code>Rect</code>, <code>Diamond</code>, <code>Triangle</code>, <code>DTriangle</code>, <code>UTriangle</code>, <code>LTriangle</code>, <code>RTriangle</code>, <code>Cross</code>, <code>XCross</code>, <code>HLine</code>, <code>VLine</code>, <code>Star1</code>, <code>Star2</code>, <code>Hexagon</code>, <code>Path</code>, <code>Pixmap</code>, <code>Graphic</code>, <code>SvgDocument</code>, <code>UserStyle</code> = 1000 } </p>
<p> enum <code>CachePolicy</code> { <code>NoCache</code>, <code>Cache</code>, <code>AutoCache</code> } </p>
<h3>Public Member Functions</h3>
<p><code>QwtSymbol</code> (<code>Style</code>=<code>NoSymbol</code>) </p>
<p> <code>QwtSymbol</code> (<code>Style</code>, const QBrush &amp;, const QPen &amp;, const QSize &amp;)<br />
 <i>Constructor. </i><br />
 <code>QwtSymbol</code> (const QPainterPath &amp;, const QBrush &amp;, const QPen &amp;)<br />
 <i>Constructor. </i><br />
 virtual <code>~QwtSymbol</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setCachePolicy</code> (<code>CachePolicy</code>) </p>
<p> <code>CachePolicy</code> <code>cachePolicy</code> () const </p>
<p> void <code>setSize</code> (const QSize &amp;) </p>
<p> void <code>setSize</code> (int width, int height=-1)<br />
 <i>Specify the symbol&#8217;s size. </i><br />
 const QSize &amp; <code>size</code> () const </p>
<p> void <code>setPinPoint</code> (const QPointF &amp;pos, bool enable=true)<br />
 <i>Set and enable a pin point. </i><br />
 QPointF <code>pinPoint</code> () const </p>
<p> void <code>setPinPointEnabled</code> (bool) </p>
<p> bool <code>isPinPointEnabled</code> () const </p>
<p> virtual void <code>setColor</code> (const QColor &amp;)<br />
 <i>Set the color of the symbol. </i><br />
 void <code>setBrush</code> (const QBrush &amp;b)<br />
 <i>Assign a brush. </i><br />
 const QBrush &amp; <code>brush</code> () const </p>
<p> void <code>setPen</code> (const QColor &amp;, qreal width=0.0, Qt::PenStyle=Qt::SolidLine) </p>
<p> void <code>setPen</code> (const QPen &amp;) </p>
<p> const QPen &amp; <code>pen</code> () const </p>
<p> void <code>setStyle</code> (<code>Style</code>) </p>
<p> <code>Style</code> <code>style</code> () const </p>
<p> void <code>setPath</code> (const QPainterPath &amp;)<br />
 <i>Set a painter path as symbol. </i><br />
 const QPainterPath &amp; <code>path</code> () const </p>
<p> void <code>setPixmap</code> (const QPixmap &amp;) </p>
<p> const QPixmap &amp; <code>pixmap</code> () const </p>
<p> void <code>setGraphic</code> (const <code>QwtGraphic</code> &amp;) </p>
<p> const <code>QwtGraphic</code> &amp; <code>graphic</code> () const </p>
<p> void <code>setSvgDocument</code> (const QByteArray &amp;) </p>
<p> void <code>drawSymbol</code> (QPainter *, const QRectF &amp;) const<br />
 <i>Draw the symbol into a rectangle. </i><br />
 void <code>drawSymbol</code> (QPainter *, const QPointF &amp;) const<br />
 <i>Draw the symbol at a specified position. </i><br />
 void <code>drawSymbols</code> (QPainter *, const QPolygonF &amp;) const<br />
 <i>Draw symbols at the specified points. </i><br />
 void <code>drawSymbols</code> (QPainter *, const QPointF *, int numPoints) const </p>
<p> virtual QRect <code>boundingRect</code> () const </p>
<p> void <code>invalidateCache</code> () </p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>renderSymbols</code> (QPainter *, const QPointF *, int numPoints) const </p>
<h2>Detailed Description</h2>
<p>A class for drawing symbols.</p>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtSymbol::CachePolicy</code></h3>
<p>Depending on the render engine and the complexity of the symbol shape it might be faster to render the symbol to a pixmap and to paint this pixmap. </p>
<p> F.e. the raster paint engine is a pure software renderer where in cache mode a draw operation usually ends in raster operation with the the backing store, that are usually faster, than the algorithms for rendering polygons. But the opposite can be expected for graphic pipelines that can make use of hardware acceleration. </p>
<p> The default setting is AutoCache </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setCachePolicy()</code>, <code>cachePolicy()</code></dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The policy has no effect, when the symbol is painted to a vector graphics format ( PDF, SVG ).</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>Since Qt 4.8 raster is the default backend on X11</dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>NoCache </i></p>
<dd>Don&#8217;t use a pixmap cache.</p>
<dt><i>Cache </i></p>
<dd>Always use a pixmap cache.</p>
<dt><i>AutoCache </i></p>
<dd>Use a cache when one of the following conditions is true:</dl>
<dl COMPACT>
<dt>&bull;</p>
<dd>The symbol is rendered with the software renderer ( QPaintEngine::Raster )</dl>
<h3>enum <code>QwtSymbol::Style</code></h3>
<p>Symbol Style </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setStyle()</code>, <code>style()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>NoSymbol </i></p>
<dd>No Style. The symbol cannot be drawn.</p>
<dt><i>Ellipse </i></p>
<dd>Ellipse or circle.</p>
<dt><i>Rect </i></p>
<dd>Rectangle.</p>
<dt><i>Diamond </i></p>
<dd>Diamond.</p>
<dt><i>Triangle </i></p>
<dd>Triangle pointing upwards.</p>
<dt><i>DTriangle </i></p>
<dd>Triangle pointing downwards.</p>
<dt><i>UTriangle </i></p>
<dd>Triangle pointing upwards.</p>
<dt><i>LTriangle </i></p>
<dd>Triangle pointing left.</p>
<dt><i>RTriangle </i></p>
<dd>Triangle pointing right.</p>
<dt><i>Cross </i></p>
<dd>Cross (+)</p>
<dt><i>XCross </i></p>
<dd>Diagonal cross (X)</p>
<dt><i>HLine </i></p>
<dd>Horizontal line.</p>
<dt><i>VLine </i></p>
<dd>Vertical line.</p>
<dt><i>Star1 </i></p>
<dd>X combined with +.</p>
<dt><i>Star2 </i></p>
<dd>Six-pointed star.</p>
<dt><i>Hexagon </i></p>
<dd>Hexagon.</p>
<dt><i>Path </i></p>
<dd>The symbol is represented by a painter path, where the origin ( 0, 0 ) of the path coordinate system is mapped to the position of the symbol.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPath()</code>, <code>path()</code></dl>
<dl COMPACT>
<dt><i>Pixmap </i></p>
<dd>The symbol is represented by a pixmap. The pixmap is centered or aligned to its pin point.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPinPoint()</code></dl>
<dl COMPACT>
<dt><i>Graphic </i></p>
<dd>The symbol is represented by a graphic. The graphic is centered or aligned to its pin point.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPinPoint()</code></dl>
<dl COMPACT>
<dt><i>SvgDocument </i></p>
<dd>The symbol is represented by a SVG graphic. The graphic is centered or aligned to its pin point.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPinPoint()</code></dl>
<dl COMPACT>
<dt><i>UserStyle </i></p>
<dd>Styles &gt;= QwtSymbol::UserSymbol are reserved for derived classes of <code>QwtSymbol</code> that overload <code>drawSymbols()</code> with additional application specific symbol types.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtSymbol::QwtSymbol (<code>Style</code>style = <code>NoSymbol</code>)</h3>
<p>Default Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>style</i> Symbol Style</dl>
<p> The symbol is constructed with gray interior, black outline with zero width, no size and style &#8216;NoSymbol&#8217;.</p>
<h3>QwtSymbol::QwtSymbol (<code>QwtSymbol::Style</code>style, const QBrush &amp;brush, const QPen &amp;pen, const QSize &amp;size)</h3>
<p>Constructor. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>style</i> Symbol Style<br />
 <i>brush</i> brush to fill the interior<br />
 <i>pen</i> outline pen<br />
 <i>size</i> size</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setStyle()</code>, <code>setBrush()</code>, <code>setPen()</code>, <code>setSize()</code></dl>
<h3>QwtSymbol::QwtSymbol (const QPainterPath &amp;path, const QBrush &amp;brush, const QPen &amp;pen)</h3>
<p>Constructor. The symbol gets initialized by a painter path. The style is set to <code>QwtSymbol::Path</code>, the size is set to empty ( the path is displayed unscaled ). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>path</i> painter path<br />
 <i>brush</i> brush to fill the interior<br />
 <i>pen</i> outline pen</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPath()</code>, <code>setBrush()</code>, <code>setPen()</code>, <code>setSize()</code></dl>
<h2>Member Function Documentation</h2>
<h3>QRect QwtSymbol::boundingRect () const [virtual]</h3>
<p>Calculate the bounding rectangle for a symbol at position (0,0). </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Bounding rectangle</dl>
<h3>const QBrush &amp; QwtSymbol::brush () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Brush</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBrush()</code></dl>
<h3><code>QwtSymbol::CachePolicy</code> QwtSymbol::cachePolicy () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Cache policy</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>CachePolicy</code>, <code>setCachePolicy()</code></dl>
<h3>void QwtSymbol::drawSymbol (QPainter *painter, const QRectF &amp;rect) const</h3>
<p>Draw the symbol into a rectangle. The symbol is painted centered and scaled into the target rectangle. It is always painted uncached and the pin point is ignored. </p>
<p> This method is primarily intended for drawing a symbol to the legend. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>rect</i> Target rectangle for the symbol</dl>
<h3>void QwtSymbol::drawSymbol (QPainter *painter, const QPointF &amp;pos) const [inline]</h3>
<p>Draw the symbol at a specified position. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>pos</i> Position of the symbol in screen coordinates</dl>
<h3>void QwtSymbol::drawSymbols (QPainter *painter, const QPolygonF &amp;points) const [inline]</h3>
<p>Draw symbols at the specified points. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>points</i> Positions of the symbols in screen coordinates</dl>
<h3>void QwtSymbol::drawSymbols (QPainter *painter, const QPointF *points, intnumPoints) const</h3>
<p>Render an array of symbols </p>
<p> Painting several symbols is more effective than drawing symbols one by one, as a couple of layout calculations and setting of pen/brush can be done once for the complete array. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>points</i> Array of points<br />
 <i>numPoints</i> Number of points</dl>
<h3>const <code>QwtGraphic</code> &amp; QwtSymbol::graphic () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Assigned graphic</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setGraphic()</code></dl>
<h3>void QwtSymbol::invalidateCache ()</h3>
<p>Invalidate the cached symbol pixmap </p>
<p> The symbol invalidates its cache, whenever an attribute is changed that has an effect ob how to display a symbol. In case of derived classes with individual styles ( &gt;= <code>QwtSymbol::UserStyle</code> ) it might be necessary to call <code>invalidateCache()</code> for attributes that are relevant for this style. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>CachePolicy</code>, <code>setCachePolicy()</code>, <code>drawSymbols()</code></dl>
<h3>bool QwtSymbol::isPinPointEnabled () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, when the pin point translation is enabled</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPinPoint()</code>, <code>setPinPointEnabled()</code></dl>
<h3>const QPainterPath &amp; QwtSymbol::path () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Painter path for displaying the symbol</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPath()</code></dl>
<h3>const QPen &amp; QwtSymbol::pen () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Pen</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPen()</code>, <code>brush()</code></dl>
<h3>QPointF QwtSymbol::pinPoint () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Pin point</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPinPoint()</code>, <code>setPinPointEnabled()</code></dl>
<h3>const QPixmap &amp; QwtSymbol::pixmap () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Assigned pixmap</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPixmap()</code></dl>
<h3>void QwtSymbol::renderSymbols (QPainter *painter, const QPointF *points, intnumPoints) const [protected], [virtual]</h3>
<p>Render the symbol to series of points </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Qt painter<br />
 <i>points</i> Positions of the symbols<br />
 <i>numPoints</i> Number of points</dl>
<h3>void QwtSymbol::setBrush (const QBrush &amp;brush)</h3>
<p>Assign a brush. The brush is used to draw the interior of the symbol. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>brush</i> Brush</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>brush()</code></dl>
<h3>void QwtSymbol::setCachePolicy (<code>QwtSymbol::CachePolicy</code>policy)</h3>
<p>Change the cache policy </p>
<p> The default policy is AutoCache </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>policy</i> Cache policy</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>CachePolicy</code>, <code>cachePolicy()</code></dl>
<h3>void QwtSymbol::setColor (const QColor &amp;color) [virtual]</h3>
<p>Set the color of the symbol. Change the color of the brush for symbol types with a filled area. For all other symbol types the color will be assigned to the pen. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>color</i> Color</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBrush()</code>, <code>setPen()</code>, <code>brush()</code>, <code>pen()</code></dl>
<h3>void QwtSymbol::setGraphic (const <code>QwtGraphic</code> &amp;graphic)</h3>
<p>Set a graphic as symbol </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>graphic</i> Graphic</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>graphic()</code>, <code>setPixmap()</code></dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>the <code>style()</code> is set to <code>QwtSymbol::Graphic</code> </p>
<p> <code>brush()</code> and <code>pen()</code> have no effect</dl>
<h3>void QwtSymbol::setPath (const QPainterPath &amp;path)</h3>
<p>Set a painter path as symbol. The symbol is represented by a painter path, where the origin ( 0, 0 ) of the path coordinate system is mapped to the position of the symbol. </p>
<p> When the symbol has valid size the painter path gets scaled to fit into the size. Otherwise the symbol size depends on the bounding rectangle of the path. </p>
<p> The following code defines a symbol drawing an arrow: </p>
<pre>#include &lt;qwt_symbol.h&gt;
QwtSymbol *symbol = new QwtSymbol();
QPen pen( Qt::black, 2 );
pen.setJoinStyle( Qt::MiterJoin );
symbol-&gt;setPen( pen );
symbol-&gt;setBrush( Qt::red );
QPainterPath path;
path.moveTo( 0, 8 );
path.lineTo( 0, 5 );
path.lineTo( -3, 5 );
path.lineTo( 0, 0 );
path.lineTo( 3, 5 );
path.lineTo( 0, 5 );
QTransform transform;
transform.rotate( -30.0 );
path = transform.map( path );
symbol-&gt;setPath( path );
symbol-&gt;setPinPoint( QPointF( 0.0, 0.0 ) );
setSize( 10, 14 );</pre>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>path</i> Painter path</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The style is implicitely set to <code>QwtSymbol::Path</code>.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>path()</code>, <code>setSize()</code></dl>
<h3>void QwtSymbol::setPen (const QColor &amp;color, qrealwidth = 0.0, Qt::PenStylestyle = Qt::SolidLine)</h3>
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
<h3>void QwtSymbol::setPen (const QPen &amp;pen)</h3>
<p>Assign a pen </p>
<p> The pen is used to draw the symbol&#8217;s outline. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pen</i> Pen</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>pen()</code>, <code>setBrush()</code></dl>
<h3>void QwtSymbol::setPinPoint (const QPointF &amp;pos, boolenable = true)</h3>
<p>Set and enable a pin point. The position of a complex symbol is not always aligned to its center ( f.e an arrow, where the peak points to a position ). The pin point defines the position inside of a Pixmap, Graphic, SvgDocument or PainterPath symbol where the represented point has to be aligned to. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pos</i> Position<br />
 <i>enable</i> En/Disable the pin point alignment</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>pinPoint()</code>, <code>setPinPointEnabled()</code></dl>
<h3>void QwtSymbol::setPinPointEnabled (boolon)</h3>
<p>En/Disable the pin point alignment </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>on</i> Enabled, when on is true</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPinPoint()</code>, <code>isPinPointEnabled()</code></dl>
<h3>void QwtSymbol::setPixmap (const QPixmap &amp;pixmap)</h3>
<p>Set a pixmap as symbol </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pixmap</i> Pixmap</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>pixmap()</code>, <code>setGraphic()</code></dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>the <code>style()</code> is set to <code>QwtSymbol::Pixmap</code> </p>
<p> <code>brush()</code> and <code>pen()</code> have no effect</dl>
<h3>void QwtSymbol::setSize (const QSize &amp;size)</h3>
<p>Set the symbol&#8217;s size </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>size</i> Size</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>size()</code></dl>
<h3>void QwtSymbol::setSize (intwidth, intheight = -1)</h3>
<p>Specify the symbol&#8217;s size. If the &#8216;h&#8217; parameter is left out or less than 0, and the &#8216;w&#8217; parameter is greater than or equal to 0, the symbol size will be set to (w,w). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>width</i> Width<br />
 <i>height</i> Height (defaults to -1)</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>size()</code></dl>
<h3>void QwtSymbol::setStyle (<code>QwtSymbol::Style</code>style)</h3>
<p>Specify the symbol style </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>style</i> Style</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>style()</code></dl>
<h3>void QwtSymbol::setSvgDocument (const QByteArray &amp;svgDocument)</h3>
<p>Set a SVG icon as symbol </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>svgDocument</i> SVG icon</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setGraphic()</code>, <code>setPixmap()</code></dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>the <code>style()</code> is set to <code>QwtSymbol::SvgDocument</code> </p>
<p> <code>brush()</code> and <code>pen()</code> have no effect</dl>
<h3>const QSize &amp; QwtSymbol::size () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Size</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setSize()</code></dl>
<h3><code>QwtSymbol::Style</code> QwtSymbol::style () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Current symbol style</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setStyle()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
