---
title: "qwtplotrenderer(3)"
name: "qwtplotrenderer"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtplotrenderer/"
description: "QwtPlotRenderer –"
---

<p>QwtPlotRenderer &#8211; </p>
<p> Renderer for exporting a plot to a document, a printer or anything else, that is supported by QPainter/QPaintDevice.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_plot_renderer.h&gt; </p>
<p> Inherits QObject.</p>
<h3>Public Types</h3>
<p>enum <code>DiscardFlag</code> { <code>DiscardNone</code> = 0x00, <code>DiscardBackground</code> = 0x01, <code>DiscardTitle</code> = 0x02, <code>DiscardLegend</code> = 0x04, <code>DiscardCanvasBackground</code> = 0x08, <code>DiscardFooter</code> = 0x10, <code>DiscardCanvasFrame</code> = 0x20 }<br/>
 <i>Disard flags. </i><br/>
 enum <code>LayoutFlag</code> { <code>DefaultLayout</code> = 0x00, <code>FrameWithScales</code> = 0x01 }<br/>
 <i>Layout flags. </i><br/>
 typedef QFlags&lt; <code>DiscardFlag</code> &gt; <code>DiscardFlags</code><br/>
 <i>Disard flags. </i><br/>
 typedef QFlags&lt; <code>LayoutFlag</code> &gt; <code>LayoutFlags</code><br/>
 <i>Layout flags. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtPlotRenderer</code> (QObject *=NULL) </p>
<p> virtual <code>~QwtPlotRenderer</code> ()<br/>
 <i>Destructor. </i><br/>
 void <code>setDiscardFlag</code> (<code>DiscardFlag</code> flag, bool on=true) </p>
<p> bool <code>testDiscardFlag</code> (<code>DiscardFlag</code> flag) const </p>
<p> void <code>setDiscardFlags</code> (<code>DiscardFlags</code> flags) </p>
<p> <code>DiscardFlags</code> <code>discardFlags</code> () const </p>
<p> void <code>setLayoutFlag</code> (<code>LayoutFlag</code> flag, bool on=true) </p>
<p> bool <code>testLayoutFlag</code> (<code>LayoutFlag</code> flag) const </p>
<p> void <code>setLayoutFlags</code> (<code>LayoutFlags</code> flags) </p>
<p> <code>LayoutFlags</code> <code>layoutFlags</code> () const </p>
<p> void <code>renderDocument</code> (<code>QwtPlot</code> *, const QString &amp;fileName, const QSizeF &amp;sizeMM, int resolution=85) </p>
<p> void <code>renderDocument</code> (<code>QwtPlot</code> *, const QString &amp;fileName, const QString &amp;format, const QSizeF &amp;sizeMM, int resolution=85) </p>
<p> void <code>renderTo</code> (<code>QwtPlot</code> *, QPrinter &amp;) const<br/>
 <i>Render the plot to a QPrinter. </i><br/>
 void <code>renderTo</code> (<code>QwtPlot</code> *, QPaintDevice &amp;p) const<br/>
 <i>Render the plot to a </i>QPaintDevice.<br/>
 virtual void <code>render</code> (<code>QwtPlot</code> *, QPainter *, const QRectF &amp;rect) const </p>
<p> virtual void <code>renderTitle</code> (const <code>QwtPlot</code> *, QPainter *, const QRectF &amp;) const </p>
<p> virtual void <code>renderFooter</code> (const <code>QwtPlot</code> *, QPainter *, const QRectF &amp;) const </p>
<p> virtual void <code>renderScale</code> (const <code>QwtPlot</code> *, QPainter *, int axisId, int startDist, int endDist, int baseDist, const QRectF &amp;) const<br/>
 <i>Paint a scale into a given rectangle. Paint the scale into a given rectangle. </i><br/>
 virtual void <code>renderCanvas</code> (const <code>QwtPlot</code> *, QPainter *, const QRectF &amp;canvasRect, const <code>QwtScaleMap</code> *maps) const </p>
<p> virtual void <code>renderLegend</code> (const <code>QwtPlot</code> *, QPainter *, const QRectF &amp;) const </p>
<p> bool <code>exportTo</code> (<code>QwtPlot</code> *, const QString &amp;documentName, const QSizeF &amp;sizeMM=QSizeF(300, 200), int resolution=85)<br/>
 <i>Execute a file dialog and render the plot to the selected file. </i></p>
<h2>Detailed Description</h2>
<p>Renderer for exporting a plot to a document, a printer or anything else, that is supported by QPainter/QPaintDevice.</p>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtPlotRenderer::DiscardFlag</code></h3>
<p>Disard flags. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>DiscardNone </i></dt>
<dd>Render all components of the plot.</dd>
<dt><i>DiscardBackground </i></dt>
<dd>Don&#8217;t render the background of the plot.</dd>
<dt><i>DiscardTitle </i></dt>
<dd>Don&#8217;t render the title of the plot.</dd>
<dt><i>DiscardLegend </i></dt>
<dd>Don&#8217;t render the legend of the plot.</dd>
<dt><i>DiscardCanvasBackground </i></dt>
<dd>Don&#8217;t render the background of the canvas.</dd>
<dt><i>DiscardFooter </i></dt>
<dd>Don&#8217;t render the footer of the plot.</dd>
<dt><i>DiscardCanvasFrame </i></dt>
<dd>Don&#8217;t render the frame of the canvas</dd></dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>This flag has no effect when using style sheets, where the frame is part of the background</dd></dl>
<h3>enum <code>QwtPlotRenderer::LayoutFlag</code></h3>
<p>Layout flags. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLayoutFlag()</code>, <code>testLayoutFlag()</code></dd></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>DefaultLayout </i></dt>
<dd>Use the default layout as on screen.</dd>
<dt><i>FrameWithScales </i></dt>
<dd>Instead of the scales a box is painted around the plot canvas, where the scale ticks are aligned to.</dd></dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPlotRenderer::QwtPlotRenderer (QObject *parent = NULL) [explicit]</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>parent</i> Parent object</dd></dl>
<h2>Member Function Documentation</h2>
<h3><code>QwtPlotRenderer::DiscardFlags</code> QwtPlotRenderer::discardFlags () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Flags, indicating what to discard from rendering</dd></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>DiscardFlag</code>, <code>setDiscardFlags()</code>, <code>setDiscardFlag()</code>, <code>testDiscardFlag()</code></dd></dl>
<h3>bool QwtPlotRenderer::exportTo (<code>QwtPlot</code> *plot, const QString &amp;documentName, const QSizeF &amp;sizeMM = QSizeF( 300, 200 ), intresolution = 85)</h3>
<p>Execute a file dialog and render the plot to the selected file. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>plot</i> Plot widget<br/>
 <i>documentName</i> Default document name<br/>
 <i>sizeMM</i> Size for the document in millimeters.<br/>
 <i>resolution</i> Resolution in dots per Inch (dpi)</dd></dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>True, when exporting was successful</dd></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>renderDocument()</code></dd></dl>
<h3><code>QwtPlotRenderer::LayoutFlags</code> QwtPlotRenderer::layoutFlags () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Layout flags</dd></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>LayoutFlag</code>, <code>setLayoutFlags()</code>, <code>setLayoutFlag()</code>, <code>testLayoutFlag()</code></dd></dl>
<h3>void QwtPlotRenderer::render (<code>QwtPlot</code> *plot, QPainter *painter, const QRectF &amp;plotRect) const [virtual]</h3>
<p>Paint the contents of a <code>QwtPlot</code> instance into a given rectangle. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>plot</i> Plot to be rendered<br/>
 <i>painter</i> Painter<br/>
 <i>plotRect</i> Bounding rectangle</dd></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>renderDocument()</code>, <code>renderTo()</code>, <code>QwtPainter::setRoundingAlignment()</code></dd></dl>
<h3>void QwtPlotRenderer::renderCanvas (const <code>QwtPlot</code> *plot, QPainter *painter, const QRectF &amp;canvasRect, const <code>QwtScaleMap</code> *map) const [virtual]</h3>
<p>Render the canvas into a given rectangle. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>plot</i> Plot widget<br/>
 <i>painter</i> Painter<br/>
 <i>map</i> Maps mapping between plot and paint device coordinates<br/>
 <i>canvasRect</i> Canvas rectangle</dd></dl>
<h3>void QwtPlotRenderer::renderDocument (<code>QwtPlot</code> *plot, const QString &amp;fileName, const QSizeF &amp;sizeMM, intresolution = 85)</h3>
<p>Render a plot to a file </p>
<p> The format of the document will be auto-detected from the suffix of the file name. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>plot</i> Plot widget<br/>
 <i>fileName</i> Path of the file, where the document will be stored<br/>
 <i>sizeMM</i> Size for the document in millimeters.<br/>
 <i>resolution</i> Resolution in dots per Inch (dpi)</dd></dl>
<h3>void QwtPlotRenderer::renderDocument (<code>QwtPlot</code> *plot, const QString &amp;fileName, const QString &amp;format, const QSizeF &amp;sizeMM, intresolution = 85)</h3>
<p>Render a plot to a file </p>
<p> Supported formats are: </p>
<dl COMPACT>
<dt>&bull;</dt>
<dd>pdf </dd>
<p>&nbsp;<wbr>Portable Document Format PDF</p>
<dt>&bull;</dt>
<dd>ps </dd>
<p>&nbsp;<wbr>Postcript</p>
<dt>&bull;</dt>
<dd>svg </dd>
<p>&nbsp;<wbr>Scalable Vector Graphics SVG</p>
<dt>&bull;</dt>
<dd>all image formats supported by Qt </dd>
<p>&nbsp;<wbr>see QImageWriter::supportedImageFormats()</dl>
<p> Scalable vector graphic formats like PDF or SVG are superior to raster graphics formats. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>plot</i> Plot widget<br/>
 <i>fileName</i> Path of the file, where the document will be stored<br/>
 <i>format</i> Format for the document<br/>
 <i>sizeMM</i> Size for the document in millimeters.<br/>
 <i>resolution</i> Resolution in dots per Inch (dpi)</dd></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>renderTo()</code>, <code>render()</code>, <code>QwtPainter::setRoundingAlignment()</code></dd></dl>
<h3>void QwtPlotRenderer::renderFooter (const <code>QwtPlot</code> *plot, QPainter *painter, const QRectF &amp;rect) const [virtual]</h3>
<p>Render the footer into a given rectangle. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>plot</i> Plot widget<br/>
 <i>painter</i> Painter<br/>
 <i>rect</i> Bounding rectangle</dd></dl>
<h3>void QwtPlotRenderer::renderLegend (const <code>QwtPlot</code> *plot, QPainter *painter, const QRectF &amp;rect) const [virtual]</h3>
<p>Render the legend into a given rectangle. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>plot</i> Plot widget<br/>
 <i>painter</i> Painter<br/>
 <i>rect</i> Bounding rectangle</dd></dl>
<h3>void QwtPlotRenderer::renderScale (const <code>QwtPlot</code> *plot, QPainter *painter, intaxisId, intstartDist, intendDist, intbaseDist, const QRectF &amp;rect) const [virtual]</h3>
<p>Paint a scale into a given rectangle. Paint the scale into a given rectangle. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>plot</i> Plot widget<br/>
 <i>painter</i> Painter<br/>
 <i>axisId</i> Axis<br/>
 <i>startDist</i> Start border distance<br/>
 <i>endDist</i> End border distance<br/>
 <i>baseDist</i> Base distance<br/>
 <i>rect</i> Bounding rectangle</dd></dl>
<h3>void QwtPlotRenderer::renderTitle (const <code>QwtPlot</code> *plot, QPainter *painter, const QRectF &amp;rect) const [virtual]</h3>
<p>Render the title into a given rectangle. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>plot</i> Plot widget<br/>
 <i>painter</i> Painter<br/>
 <i>rect</i> Bounding rectangle</dd></dl>
<h3>void QwtPlotRenderer::renderTo (<code>QwtPlot</code> *plot, QPrinter &amp;printer) const</h3>
<p>Render the plot to a QPrinter. This function renders the contents of a <code>QwtPlot</code> instance to QPaintDevice object. The size is derived from the printer metrics. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>plot</i> Plot to be rendered<br/>
 <i>printer</i> Printer to paint on</dd></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>renderDocument()</code>, <code>render()</code>, <code>QwtPainter::setRoundingAlignment()</code></dd></dl>
<h3>void QwtPlotRenderer::renderTo (<code>QwtPlot</code> *plot, QPaintDevice &amp;paintDevice) const</h3>
<p>Render the plot to a QPaintDevice. This function renders the contents of a <code>QwtPlot</code> instance to QPaintDevice object. The target rectangle is derived from its device metrics. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>plot</i> Plot to be rendered<br/>
 <i>paintDevice</i> device to paint on, f.e a QImage</dd></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>renderDocument()</code>, <code>render()</code>, <code>QwtPainter::setRoundingAlignment()</code></dd></dl>
<h3>void QwtPlotRenderer::setDiscardFlag (<code>DiscardFlag</code>flag, boolon = true)</h3>
<p>Change a flag, indicating what to discard from rendering </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>flag</i> Flag to change<br/>
 <i>on</i> On/Off</dd></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>DiscardFlag</code>, <code>testDiscardFlag()</code>, <code>setDiscardFlags()</code>, <code>discardFlags()</code></dd></dl>
<h3>void QwtPlotRenderer::setDiscardFlags (<code>DiscardFlags</code>flags)</h3>
<p>Set the flags, indicating what to discard from rendering </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>flags</i> Flags</dd></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>DiscardFlag</code>, <code>setDiscardFlag()</code>, <code>testDiscardFlag()</code>, <code>discardFlags()</code></dd></dl>
<h3>void QwtPlotRenderer::setLayoutFlag (<code>LayoutFlag</code>flag, boolon = true)</h3>
<p>Change a layout flag </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>flag</i> Flag to change<br/>
 <i>on</i> On/Off</dd></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>LayoutFlag</code>, <code>testLayoutFlag()</code>, <code>setLayoutFlags()</code>, <code>layoutFlags()</code></dd></dl>
<h3>void QwtPlotRenderer::setLayoutFlags (<code>LayoutFlags</code>flags)</h3>
<p>Set the layout flags </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>flags</i> Flags</dd></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>LayoutFlag</code>, <code>setLayoutFlag()</code>, <code>testLayoutFlag()</code>, <code>layoutFlags()</code></dd></dl>
<h3>bool QwtPlotRenderer::testDiscardFlag (<code>DiscardFlag</code>flag) const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, if flag is enabled.</dd></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>flag</i> Flag to be tested</dd></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>DiscardFlag</code>, <code>setDiscardFlag()</code>, <code>setDiscardFlags()</code>, <code>discardFlags()</code></dd></dl>
<h3>bool QwtPlotRenderer::testLayoutFlag (<code>LayoutFlag</code>flag) const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, if flag is enabled.</dd></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>flag</i> Flag to be tested</dd></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>LayoutFlag</code>, <code>setLayoutFlag()</code>, <code>setLayoutFlags()</code>, <code>layoutFlags()</code></dd></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
