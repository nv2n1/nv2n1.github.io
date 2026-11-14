---
title: "qwtplotrasteritem(3)"
name: "qwtplotrasteritem"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtplotrasteritem/"
description: "QwtPlotRasterItem –"
---

<p>QwtPlotRasterItem &#8211; </p>
<p> A class, which displays raster data.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_plot_rasteritem.h&gt; </p>
<p> Inherits <code>QwtPlotItem</code>. </p>
<p> Inherited by <code>QwtPlotSpectrogram</code>.</p>
<h3>Public Types</h3>
<p>enum <code>CachePolicy</code> { <code>NoCache</code>, <code>PaintCache</code> }<br />
 <i>Cache policy The default policy is NoCache. </i><br />
 enum <code>PaintAttribute</code> { <code>PaintInDeviceResolution</code> = 1 } </p>
<p> typedef QFlags&lt; <code>PaintAttribute</code> &gt; <code>PaintAttributes</code><br />
 <i>Paint attributes. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtPlotRasterItem</code> (const QString &amp;<code>title</code>=QString::null)<br />
 <i>Constructor. </i><br />
 <code>QwtPlotRasterItem</code> (const <code>QwtText</code> &amp;<code>title</code>)<br />
 <i>Constructor. </i><br />
 virtual <code>~QwtPlotRasterItem</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setPaintAttribute</code> (<code>PaintAttribute</code>, bool on=true) </p>
<p> bool <code>testPaintAttribute</code> (<code>PaintAttribute</code>) const </p>
<p> void <code>setAlpha</code> (int <code>alpha</code>)<br />
 <i>Set an alpha value for the raster data. </i><br />
 int <code>alpha</code> () const </p>
<p> void <code>setCachePolicy</code> (<code>CachePolicy</code>) </p>
<p> <code>CachePolicy</code> <code>cachePolicy</code> () const </p>
<p> void <code>invalidateCache</code> () </p>
<p> virtual void <code>draw</code> (QPainter *p, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;rect) const<br />
 <i>Draw the raster data. </i><br />
 virtual QRectF <code>pixelHint</code> (const QRectF &amp;) const<br />
 <i>Pixel hint. </i><br />
 virtual <code>QwtInterval</code> <code>interval</code> (Qt::Axis) const </p>
<p> virtual QRectF <code>boundingRect</code> () const </p>
<h3>Protected Member Functions</h3>
<p>virtual QImage <code>renderImage</code> (const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;area, const QSize &amp;imageSize) const =0<br />
 <i>Render an image. </i><br />
 virtual <code>QwtScaleMap</code> <code>imageMap</code> (Qt::Orientation, const <code>QwtScaleMap</code> &amp;map, const QRectF &amp;area, const QSize &amp;imageSize, double pixelSize) const<br />
 <i>Calculate a scale map for painting to an image. </i></p>
<h2>Detailed Description</h2>
<p>A class, which displays raster data. </p>
<p> Raster data is a grid of pixel values, that can be represented as a QImage. It is used for many types of information like spectrograms, cartograms, geographical maps &#8230; </p>
<p> Often a plot has several types of raster data organized in layers. ( f.e a geographical map, with weather statistics ). Using <code>setAlpha()</code> raster items can be stacked easily. </p>
<p> <code>QwtPlotRasterItem</code> is only implemented for images of the following formats: QImage::Format_Indexed8, QImage::Format_ARGB32. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlotSpectrogram</code></dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtPlotRasterItem::CachePolicy</code></h3>
<p>Cache policy The default policy is NoCache. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>NoCache </i></p>
<dd><code>renderImage()</code> is called each time the item has to be repainted</p>
<dt><i>PaintCache </i></p>
<dd><code>renderImage()</code> is called, whenever the image cache is not valid, or the scales, or the size of the canvas has changed.</dl>
<p> This type of cache is useful for improving the performance of hide/show operations or manipulations of the alpha value. All other situations are handled by the canvas backing store.</p>
<h3>enum <code>QwtPlotRasterItem::PaintAttribute</code></h3>
<p>Attributes to modify the drawing algorithm. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPaintAttribute()</code>, <code>testPaintAttribute()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>PaintInDeviceResolution </i></p>
<dd>When the image is rendered according to the data pixels ( <code>QwtRasterData::pixelHint()</code> ) it can be expanded to paint device resolution before it is passed to QPainter. The expansion algorithm rounds the pixel borders in the same way as the axis ticks, what is usually better than the scaling algorithm implemented in Qt. Disabling this flag might make sense, to reduce the size of a document/file. If this is possible for a document format depends on the implementation of the specific QPaintEngine.</dl>
<h2>Member Function Documentation</h2>
<h3>int QwtPlotRasterItem::alpha () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Alpha value of the raster item</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setAlpha()</code></dl>
<h3>QRectF QwtPlotRasterItem::boundingRect () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Bounding rectangle of the data</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlotRasterItem::interval()</code></dl>
<p> Reimplemented from <code>QwtPlotItem</code>.</p>
<h3><code>QwtPlotRasterItem::CachePolicy</code> QwtPlotRasterItem::cachePolicy () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Cache policy</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>CachePolicy</code>, <code>setCachePolicy()</code></dl>
<h3>void QwtPlotRasterItem::draw (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect) const [virtual]</h3>
<p>Draw the raster data. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>xMap</i> X-Scale Map<br />
 <i>yMap</i> Y-Scale Map<br />
 <i>canvasRect</i> Contents rectangle of the plot canvas</dl>
<p> Implements <code>QwtPlotItem</code>. </p>
<p> Reimplemented in <code>QwtPlotSpectrogram</code>.</p>
<h3><code>QwtScaleMap</code> QwtPlotRasterItem::imageMap (Qt::Orientationorientation, const <code>QwtScaleMap</code> &amp;map, const QRectF &amp;area, const QSize &amp;imageSize, doublepixelSize) const [protected], [virtual]</h3>
<p>Calculate a scale map for painting to an image. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>orientation</i> Orientation, Qt::Horizontal means a X axis<br />
 <i>map</i> Scale map for rendering the plot item<br />
 <i>area</i> Area to be painted on the image<br />
 <i>imageSize</i> Image size<br />
 <i>pixelSize</i> Width/Height of a data pixel</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Calculated scale map</dl>
<h3><code>QwtInterval</code> QwtPlotRasterItem::interval (Qt::Axisaxis) const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Bounding interval for an axis</dl>
<p> This method is intended to be reimplemented by derived classes. The default implementation returns an invalid interval. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axis</i> X, Y, or Z axis</dl>
<p> Reimplemented in <code>QwtPlotSpectrogram</code>.</p>
<h3>void QwtPlotRasterItem::invalidateCache ()</h3>
<p>Invalidate the paint cache </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setCachePolicy()</code></dl>
<h3>QRectF QwtPlotRasterItem::pixelHint (const QRectF &amp;area) const [virtual]</h3>
<p>Pixel hint. The geometry of a pixel is used to calculated the resolution and alignment of the rendered image. </p>
<p> Width and height of the hint need to be the horizontal and vertical distances between 2 neighbored points. The center of the hint has to be the position of any point ( it doesn&#8217;t matter which one ). </p>
<p> Limiting the resolution of the image might significantly improve the performance and heavily reduce the amount of memory when rendering a QImage from the raster data. </p>
<p> The default implementation returns an empty rectangle (QRectF()), meaning, that the image will be rendered in target device ( f.e screen ) resolution. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>area</i> In most implementations the resolution of the data doesn&#8217;t depend on the requested area.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Bounding rectangle of a pixel</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>render(), <code>renderImage()</code></dl>
<p> Reimplemented in <code>QwtPlotSpectrogram</code>.</p>
<h3>virtual QImage QwtPlotRasterItem::renderImage (const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;area, const QSize &amp;imageSize) const [protected], [pure virtual]</h3>
<p>Render an image. An implementation of render() might iterate over all pixels of imageRect. Each pixel has to be translated into the corresponding position in scale coordinates using the maps. This position can be used to look up a value in a implementation specific way and to map it into a color. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>xMap</i> X-Scale Map<br />
 <i>yMap</i> Y-Scale Map<br />
 <i>area</i> Requested area for the image in scale coordinates<br />
 <i>imageSize</i> Requested size of the image</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Rendered image</dl>
<p> Implemented in <code>QwtPlotSpectrogram</code>.</p>
<h3>void QwtPlotRasterItem::setAlpha (intalpha)</h3>
<p>Set an alpha value for the raster data. Often a plot has several types of raster data organized in layers. ( f.e a geographical map, with weather statistics ). Using <code>setAlpha()</code> raster items can be stacked easily. </p>
<p> The alpha value is a value [0, 255] to control the transparency of the image. 0 represents a fully transparent color, while 255 represents a fully opaque color. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>alpha</i> Alpha value</dl>
<dl COMPACT>
<dt>&bull;</p>
<dd>alpha &gt;= 0 </p>
<p>&nbsp;<wbr>All alpha values of the pixels returned by&nbsp;<wbr><code>renderImage()</code>&nbsp;<wbr>will be set to alpha, beside those with an alpha value of 0&nbsp;<wbr>(invalid pixels).</p>
<dt>&bull;</p>
<dd>alpha &lt; 0 The alpha values returned by <code>renderImage()</code> are not changed.</dl>
<p> The default alpha value is -1. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>alpha()</code></dl>
<h3>void QwtPlotRasterItem::setCachePolicy (<code>QwtPlotRasterItem::CachePolicy</code>policy)</h3>
<p>Change the cache policy </p>
<p> The default policy is NoCache </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>policy</i> Cache policy</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>CachePolicy</code>, <code>cachePolicy()</code></dl>
<h3>void QwtPlotRasterItem::setPaintAttribute (<code>PaintAttribute</code>attribute, boolon = true)</h3>
<p>Specify an attribute how to draw the raster item </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>attribute</i> Paint attribute<br />
 <i>on</i> On/Off /sa PaintAttribute, <code>testPaintAttribute()</code></dl>
<h3>bool QwtPlotRasterItem::testPaintAttribute (<code>PaintAttribute</code>attribute) const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, when attribute is enabled</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PaintAttribute</code>, <code>setPaintAttribute()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
