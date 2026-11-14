---
title: "qwtgraphic(3)"
name: "qwtgraphic"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtgraphic/"
description: "QwtGraphic –"
---

<p>QwtGraphic &#8211; </p>
<p> A paint device for scalable graphics.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_graphic.h&gt; </p>
<p> Inherits <code>QwtNullPaintDevice</code>.</p>
<h3>Public Types</h3>
<p>enum <code>RenderHint</code> { <code>RenderPensUnscaled</code> = 0x1 } </p>
<p> typedef QFlags&lt; <code>RenderHint</code> &gt; <code>RenderHints</code><br />
 <i>Render hints. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtGraphic</code> ()<br />
 <i>Constructor. </i><br />
 <code>QwtGraphic</code> (const <code>QwtGraphic</code> &amp;)<br />
 <i>Copy constructor. </i><br />
 virtual <code>~QwtGraphic</code> ()<br />
 <i>Destructor. </i><br />
 <code>QwtGraphic</code> &amp; <code>operator=</code> (const <code>QwtGraphic</code> &amp;)<br />
 <i>Assignment operator. </i><br />
 void <code>reset</code> ()<br />
 <i>Clear all stored commands. </i><br />
 bool <code>isNull</code> () const </p>
<p> bool <code>isEmpty</code> () const </p>
<p> void <code>render</code> (QPainter *) const<br />
 <i>Replay all recorded painter commands. </i><br />
 void <code>render</code> (QPainter *, const QSizeF &amp;, Qt::AspectRatioMode=Qt::IgnoreAspectRatio) const<br />
 <i>Replay all recorded painter commands. </i><br />
 void <code>render</code> (QPainter *, const QRectF &amp;, Qt::AspectRatioMode=Qt::IgnoreAspectRatio) const<br />
 <i>Replay all recorded painter commands. </i><br />
 void <code>render</code> (QPainter *, const QPointF &amp;, Qt::Alignment=Qt::AlignTop|Qt::AlignLeft) const<br />
 <i>Replay all recorded painter commands. </i><br />
 QPixmap <code>toPixmap</code> () const<br />
 <i>Convert the graphic to a QPixmap. </i><br />
 QPixmap <code>toPixmap</code> (const QSize &amp;, Qt::AspectRatioMode=Qt::IgnoreAspectRatio) const<br />
 <i>Convert the graphic to a QPixmap. </i><br />
 QImage <code>toImage</code> () const<br />
 <i>Convert the graphic to a QImage. </i><br />
 QImage <code>toImage</code> (const QSize &amp;, Qt::AspectRatioMode=Qt::IgnoreAspectRatio) const<br />
 <i>Convert the graphic to a QImage. </i><br />
 QRectF <code>scaledBoundingRect</code> (double sx, double sy) const<br />
 <i>Calculate the target rectangle for scaling the graphic. </i><br />
 QRectF <code>boundingRect</code> () const </p>
<p> QRectF <code>controlPointRect</code> () const </p>
<p> const QVector<br />
 &lt; <code>QwtPainterCommand</code> &gt; &amp; <code>commands</code> () const &quot; </p>
<p> void <code>setCommands</code> (QVector&lt; <code>QwtPainterCommand</code> &gt; &amp;)<br />
 <i>Append paint commands. </i><br />
 void <code>setDefaultSize</code> (const QSizeF &amp;)<br />
 <i>Set a default size. </i><br />
 QSizeF <code>defaultSize</code> () const<br />
 <i>Default size. </i><br />
 void <code>setRenderHint</code> (<code>RenderHint</code>, bool on=true) </p>
<p> bool <code>testRenderHint</code> (<code>RenderHint</code>) const </p>
<h3>Protected Member Functions</h3>
<p>virtual QSize <code>sizeMetrics</code> () const </p>
<p> virtual void <code>drawPath</code> (const QPainterPath &amp;) </p>
<p> virtual void <code>drawPixmap</code> (const QRectF &amp;, const QPixmap &amp;, const QRectF &amp;)<br />
 <i>Store a pixmap command in the command list. </i><br />
 virtual void <code>drawImage</code> (const QRectF &amp;, const QImage &amp;, const QRectF &amp;, Qt::ImageConversionFlags)<br />
 <i>Store a image command in the command list. </i><br />
 virtual void <code>updateState</code> (const QPaintEngineState &amp;state)<br />
 <i>Store a state command in the command list. </i></p>
<h2>Detailed Description</h2>
<p>A paint device for scalable graphics. </p>
<p> <code>QwtGraphic</code> is the representation of a graphic that is tailored for scalability. Like QPicture it will be initialized by QPainter operations and can be replayed later to any target paint device. </p>
<p> While the usual image representations QImage and QPixmap are not scalable Qt offers two paint devices, that might be candidates for representing a vector graphic: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>QPicture </p>
<p>&nbsp;<wbr>Unfortunately QPicture had been forgotten, when Qt4 introduced floating point based render engines. Its API is still on integers, what make it unusable for proper scaling.</p>
<dt>&bull;</p>
<dd>QSvgRenderer/QSvgGenerator </p>
<p>&nbsp;<wbr>Unfortunately QSvgRenderer hides to much information about its nodes in internal APIs, that are necessary for proper layout calculations. Also it is derived from QObject and can&#8217;t be copied like QImage/QPixmap.</dl>
<p> <code>QwtGraphic</code> maps all scalable drawing primitives to a QPainterPath and stores them together with the painter state changes ( pen, brush, transformation &#8230; ) in a list of QwtPaintCommands. For being a complete QPaintDevice it also stores pixmaps or images, what is somehow against the idea of the class, because these objects can&#8217;t be scaled without a loss in quality. </p>
<p> The main issue about scaling a <code>QwtGraphic</code> object are the pens used for drawing the outlines of the painter paths. While non cosmetic pens ( QPen::isCosmetic() ) are scaled with the same ratio as the path, cosmetic pens have a fixed width. A graphic might have paths with different pens &#8211; cosmetic and non-cosmetic. </p>
<p> <code>QwtGraphic</code> caches 2 different rectangles: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>control point rectangle </p>
<p>&nbsp;<wbr>The control point rectangle is the bounding rectangle of all control point rectangles of the painter paths, or the target rectangle of the pixmaps/images.</p>
<dt>&bull;</p>
<dd>bounding rectangle </p>
<p>&nbsp;<wbr>The bounding rectangle extends the control point rectangle by what is needed for rendering the outline with an unscaled pen.</dl>
<p> Because the offset for drawing the outline depends on the shape of the painter path ( the peak of a triangle is different than the flat side ) scaling with a fixed aspect ratio always needs to be calculated from the control point rectangle. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPainterCommand</code></dl>
<h2>Member Typedef Documentation</h2>
<h3>typedef QFlags&lt;<code>RenderHint</code>&gt; <code>QwtGraphic::RenderHints</code></h3>
<p>Render hints. The default setting is to disable all hints</p>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtGraphic::RenderHint</code></h3>
<p>Hint how to render a graphic </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setRenderHint()</code>, <code>testRenderHint()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>RenderPensUnscaled </i></p>
<dd>When rendering a <code>QwtGraphic</code> a specific scaling between the <code>controlPointRect()</code> and the coordinates of the target rectangle is set up internally in <code>render()</code>.</dl>
<p> When RenderPensUnscaled is set this specific scaling is applied for the control points only, but not for the pens. All other painter transformations ( set up by application code ) are supposed to work like usual. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>render()</code>;</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtGraphic::QwtGraphic ()</h3>
<p>Constructor. Initializes a null graphic </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isNull()</code></dl>
<h3>QwtGraphic::QwtGraphic (const <code>QwtGraphic</code> &amp;other)</h3>
<p>Copy constructor. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>other</i> Source</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>operator=()</code></dl>
<h2>Member Function Documentation</h2>
<h3>QRectF QwtGraphic::boundingRect () const</h3>
<p>The bounding rectangle is the <code>controlPointRect()</code> extended by the areas needed for rendering the outlines with unscaled pens. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Bounding rectangle of the graphic</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>controlPointRect()</code>, <code>scaledBoundingRect()</code></dl>
<h3>const QVector&lt; <code>QwtPainterCommand</code> &gt; &amp; QwtGraphic::commands () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>List of recorded paint commands</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setCommands()</code></dl>
<h3>QRectF QwtGraphic::controlPointRect () const</h3>
<p>The control point rectangle is the bounding rectangle of all control points of the paths and the target rectangles of the images/pixmaps. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Control point rectangle</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>boundingRect()</code>, <code>scaledBoundingRect()</code></dl>
<h3>QSizeF QwtGraphic::defaultSize () const</h3>
<p>Default size. When a non empty size has been assigned by <code>setDefaultSize()</code> this size will be returned. Otherwise the default size is the size of the bounding rectangle. </p>
<p> The default size is used in all methods rendering the graphic, where no size is explicitly specified. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Default size</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setDefaultSize()</code>, <code>boundingRect()</code></dl>
<h3>void QwtGraphic::drawImage (const QRectF &amp;rect, const QImage &amp;image, const QRectF &amp;subRect, Qt::ImageConversionFlagsflags) [protected], [virtual]</h3>
<p>Store a image command in the command list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rect</i> traget rectangle<br />
 <i>image</i> Image to be painted<br />
 <i>subRect</i> Reactangle of the pixmap to be painted<br />
 <i>flags</i> Image conversion flags</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>QPaintEngine::drawImage()</dl>
<p> Reimplemented from <code>QwtNullPaintDevice</code>.</p>
<h3>void QwtGraphic::drawPath (const QPainterPath &amp;path) [protected], [virtual]</h3>
<p>Store a path command in the command list </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>path</i> Painter path</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>QPaintEngine::drawPath()</dl>
<p> Reimplemented from <code>QwtNullPaintDevice</code>.</p>
<h3>void QwtGraphic::drawPixmap (const QRectF &amp;rect, const QPixmap &amp;pixmap, const QRectF &amp;subRect) [protected], [virtual]</h3>
<p>Store a pixmap command in the command list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rect</i> target rectangle<br />
 <i>pixmap</i> Pixmap to be painted<br />
 <i>subRect</i> Reactangle of the pixmap to be painted</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>QPaintEngine::drawPixmap()</dl>
<p> Reimplemented from <code>QwtNullPaintDevice</code>.</p>
<h3>bool QwtGraphic::isEmpty () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, when the bounding rectangle is empty</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>boundingRect()</code>, <code>isNull()</code></dl>
<h3>bool QwtGraphic::isNull () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, when no painter commands have been stored</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isEmpty()</code>, <code>commands()</code></dl>
<h3><code>QwtGraphic</code> &amp; QwtGraphic::operator= (const <code>QwtGraphic</code> &amp;other)</h3>
<p>Assignment operator. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>other</i> Source</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A reference of this object</dl>
<h3>void QwtGraphic::render (QPainter *painter) const</h3>
<p>Replay all recorded painter commands. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Qt painter</dl>
<h3>void QwtGraphic::render (QPainter *painter, const QSizeF &amp;size, Qt::AspectRatioModeaspectRatioMode = Qt::IgnoreAspectRatio) const</h3>
<p>Replay all recorded painter commands. The graphic is scaled to fit into the rectangle of the given size starting at ( 0, 0 ). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Qt painter<br />
 <i>size</i> Size for the scaled graphic<br />
 <i>aspectRatioMode</i> Mode how to scale &#8211; See Qt::AspectRatioMode</dl>
<h3>void QwtGraphic::render (QPainter *painter, const QRectF &amp;rect, Qt::AspectRatioModeaspectRatioMode = Qt::IgnoreAspectRatio) const</h3>
<p>Replay all recorded painter commands. The graphic is scaled to fit into the given rectangle </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Qt painter<br />
 <i>rect</i> Rectangle for the scaled graphic<br />
 <i>aspectRatioMode</i> Mode how to scale &#8211; See Qt::AspectRatioMode</dl>
<h3>void QwtGraphic::render (QPainter *painter, const QPointF &amp;pos, Qt::Alignmentalignment = Qt::AlignTop | Qt::AlignLeft) const</h3>
<p>Replay all recorded painter commands. The graphic is scaled to the <code>defaultSize()</code> and aligned to a position. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Qt painter<br />
 <i>pos</i> Reference point, where to render<br />
 <i>alignment</i> Flags how to align the target rectangle to pos.</dl>
<h3>void QwtGraphic::reset ()</h3>
<p>Clear all stored commands. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isNull()</code></dl>
<h3>QRectF QwtGraphic::scaledBoundingRect (doublesx, doublesy) const</h3>
<p>Calculate the target rectangle for scaling the graphic. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>sx</i> Horizontal scaling factor<br />
 <i>sy</i> Vertical scaling factor</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>In case of paths that are painted with a cosmetic pen ( see QPen::isCosmetic() ) the target rectangle is different to multiplying the bounding rectangle.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Scaled bounding rectangle</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>boundingRect()</code>, <code>controlPointRect()</code></dl>
<h3>void QwtGraphic::setCommands (QVector&lt; <code>QwtPainterCommand</code> &gt; &amp;commands)</h3>
<p>Append paint commands. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>commands</i> Paint commands</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>commands()</code></dl>
<h3>void QwtGraphic::setDefaultSize (const QSizeF &amp;size)</h3>
<p>Set a default size. The default size is used in all methods rendering the graphic, where no size is explicitly specified. Assigning an empty size means, that the default size will be calculated from the bounding rectangle. </p>
<p> The default setting is an empty size. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>size</i> Default size</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>defaultSize()</code>, <code>boundingRect()</code></dl>
<h3>void QwtGraphic::setRenderHint (<code>RenderHint</code>hint, boolon = true)</h3>
<p>Toggle an render hint </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>hint</i> Render hint<br />
 <i>on</i> true/false</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>testRenderHint()</code>, <code>RenderHint</code></dl>
<h3>QSize QwtGraphic::sizeMetrics () const [protected], [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Ceiled <code>defaultSize()</code></dl>
<p> Implements <code>QwtNullPaintDevice</code>.</p>
<h3>bool QwtGraphic::testRenderHint (<code>RenderHint</code>hint) const</h3>
<p>Test a render hint </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>hint</i> Render hint</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true/false</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setRenderHint()</code>, <code>RenderHint</code></dl>
<h3>QImage QwtGraphic::toImage () const</h3>
<p>Convert the graphic to a QImage. All pixels of the image get initialized by 0 ( transparent ) before the graphic is scaled and rendered on it. </p>
<p> The format of the image is QImage::Format_ARGB32_Premultiplied. </p>
<p> The size of the image is the default size ( ceiled to integers ) of the graphic. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The graphic as image in default size</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>defaultSize()</code>, <code>toPixmap()</code>, <code>render()</code></dl>
<h3>QImage QwtGraphic::toImage (const QSize &amp;size, Qt::AspectRatioModeaspectRatioMode = Qt::IgnoreAspectRatio) const</h3>
<p>Convert the graphic to a QImage. All pixels of the image get initialized by 0 ( transparent ) before the graphic is scaled and rendered on it. </p>
<p> The format of the image is QImage::Format_ARGB32_Premultiplied. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>size</i> Size of the image<br />
 <i>aspectRatioMode</i> Aspect ratio how to scale the graphic</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The graphic as image</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>toPixmap()</code>, <code>render()</code></dl>
<h3>QPixmap QwtGraphic::toPixmap () const</h3>
<p>Convert the graphic to a QPixmap. All pixels of the pixmap get initialized by Qt::transparent before the graphic is scaled and rendered on it. </p>
<p> The size of the pixmap is the default size ( ceiled to integers ) of the graphic. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The graphic as pixmap in default size</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>defaultSize()</code>, <code>toImage()</code>, <code>render()</code></dl>
<h3>QPixmap QwtGraphic::toPixmap (const QSize &amp;size, Qt::AspectRatioModeaspectRatioMode = Qt::IgnoreAspectRatio) const</h3>
<p>Convert the graphic to a QPixmap. All pixels of the pixmap get initialized by Qt::transparent before the graphic is scaled and rendered on it. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>size</i> Size of the image<br />
 <i>aspectRatioMode</i> Aspect ratio how to scale the graphic</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The graphic as pixmap</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>toImage()</code>, <code>render()</code></dl>
<h3>void QwtGraphic::updateState (const QPaintEngineState &amp;state) [protected], [virtual]</h3>
<p>Store a state command in the command list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>state</i> State to be stored</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>QPaintEngine::updateState()</dl>
<p> Reimplemented from <code>QwtNullPaintDevice</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
