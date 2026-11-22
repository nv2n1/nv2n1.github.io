---
title: "qwtpaintercommand(3)"
name: "qwtpaintercommand"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtpaintercommand/"
description: "QwtPainterCommand –"
---

<p>QwtPainterCommand &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_painter_command.h&gt;</p>
<h3>Classes</h3>
<p>struct <code>ImageData</code><br/>
 <i>Attributes how to paint a QImage. </i><br/>
 struct <code>PixmapData</code><br/>
 <i>Attributes how to paint a QPixmap. </i><br/>
 struct <code>StateData</code><br/>
 <i>Attributes of a state change. </i></p>
<h3>Public Types</h3>
<p>enum <code>Type</code> { <code>Invalid</code> = -1, <code>Path</code>, <code>Pixmap</code>, <code>Image</code>, <code>State</code> }<br/>
 <i>Type of the paint command. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtPainterCommand</code> ()<br/>
 <i>Construct an invalid command. </i><br/>
 <code>QwtPainterCommand</code> (const <code>QwtPainterCommand</code> &amp;) </p>
<p> <code>QwtPainterCommand</code> (const QPainterPath &amp;)<br/>
 <i>Copy constructor. </i><br/>
 <code>QwtPainterCommand</code> (const QRectF &amp;rect, const QPixmap &amp;, const QRectF &amp;subRect) </p>
<p> <code>QwtPainterCommand</code> (const QRectF &amp;rect, const QImage &amp;, const QRectF &amp;subRect, Qt::ImageConversionFlags) </p>
<p> <code>QwtPainterCommand</code> (const QPaintEngineState &amp;) </p>
<p> <code>~QwtPainterCommand</code> ()<br/>
 <i>Destructor. </i><br/>
 <code>QwtPainterCommand</code> &amp; <code>operator=</code> (const <code>QwtPainterCommand</code> &amp;) </p>
<p> <code>Type</code> <code>type</code> () const </p>
<p> QPainterPath * <code>path</code> () </p>
<p> const QPainterPath * <code>path</code> () const </p>
<p> PixmapData * <code>pixmapData</code> () </p>
<p> const PixmapData * <code>pixmapData</code> () const </p>
<p> ImageData * <code>imageData</code> () </p>
<p> const ImageData * <code>imageData</code> () const </p>
<p> StateData * <code>stateData</code> () </p>
<p> const StateData * <code>stateData</code> () const </p>
<h2>Detailed Description</h2>
<p><code>QwtPainterCommand</code> represents the attributes of a paint operation how it is used between QPainter and QPaintDevice </p>
<p> It is used by <code>QwtGraphic</code> to record and replay paint operations </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtGraphic::commands()</code></dd></dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtPainterCommand::Type</code></h3>
<p>Type of the paint command. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>Invalid </i></dt>
<dd>Invalid command.</dd>
<dt><i>Path </i></dt>
<dd>Draw a QPainterPath.</dd>
<dt><i>Pixmap </i></dt>
<dd>Draw a QPixmap.</dd>
<dt><i>Image </i></dt>
<dd>Draw a QImage.</dd>
<dt><i>State </i></dt>
<dd>QPainter state change.</dd></dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPainterCommand::QwtPainterCommand (const <code>QwtPainterCommand</code> &amp;other)</h3>
<p>Copy constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>other</i> Command to be copied</dd></dl>
<h3>QwtPainterCommand::QwtPainterCommand (const QRectF &amp;rect, const QPixmap &amp;pixmap, const QRectF &amp;subRect)</h3>
<p>Constructor for Pixmap paint operation </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rect</i> Target rectangle<br/>
 <i>pixmap</i> Pixmap<br/>
 <i>subRect</i> Rectangle inside the pixmap</dd></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>QPainter::drawPixmap()</dd></dl>
<h3>QwtPainterCommand::QwtPainterCommand (const QRectF &amp;rect, const QImage &amp;image, const QRectF &amp;subRect, Qt::ImageConversionFlagsflags)</h3>
<p>Constructor for Image paint operation </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rect</i> Target rectangle<br/>
 <i>image</i> Image<br/>
 <i>subRect</i> Rectangle inside the image<br/>
 <i>flags</i> Conversion flags</dd></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>QPainter::drawImage()</dd></dl>
<h3>QwtPainterCommand::QwtPainterCommand (const QPaintEngineState &amp;state)</h3>
<p>Constructor for State paint operation </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>state</i> Paint engine state</dd></dl>
<h2>Member Function Documentation</h2>
<h3>QwtPainterCommand::ImageData * QwtPainterCommand::imageData ()</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Attributes how to paint a QImage</dd></dl>
<h3>const QwtPainterCommand::ImageData * QwtPainterCommand::imageData () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Attributes how to paint a QImage</dd></dl>
<h3><code>QwtPainterCommand</code> &amp; QwtPainterCommand::operator= (const <code>QwtPainterCommand</code> &amp;other)</h3>
<p>Assignment operator </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>other</i> Command to be copied</dd></dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Modified command</dd></dl>
<h3>QPainterPath * QwtPainterCommand::path ()</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Painter path to be painted</dd></dl>
<h3>const QPainterPath * QwtPainterCommand::path () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Painter path to be painted</dd></dl>
<h3>QwtPainterCommand::PixmapData * QwtPainterCommand::pixmapData ()</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Attributes how to paint a QPixmap</dd></dl>
<h3>const QwtPainterCommand::PixmapData * QwtPainterCommand::pixmapData () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Attributes how to paint a QPixmap</dd></dl>
<h3>QwtPainterCommand::StateData * QwtPainterCommand::stateData ()</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Attributes of a state change</dd></dl>
<h3>const QwtPainterCommand::StateData * QwtPainterCommand::stateData () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Attributes of a state change</dd></dl>
<h3><code>QwtPainterCommand::Type</code> QwtPainterCommand::type () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Type of the command</dd></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
