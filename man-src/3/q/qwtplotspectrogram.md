---
title: "qwtplotspectrogram(3)"
name: "qwtplotspectrogram"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtplotspectrogram/"
description: "QwtPlotSpectrogram –"
---

<p>QwtPlotSpectrogram &#8211; </p>
<p> A plot item, which displays a spectrogram.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_plot_spectrogram.h&gt; </p>
<p> Inherits <code>QwtPlotRasterItem</code>.</p>
<h3>Public Types</h3>
<p>enum <code>DisplayMode</code> { <code>ImageMode</code> = 0x01, <code>ContourMode</code> = 0x02 } </p>
<p> typedef QFlags&lt; <code>DisplayMode</code> &gt; <code>DisplayModes</code><br />
 <i>Display modes. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtPlotSpectrogram</code> (const QString &amp;<code>title</code>=QString::null) </p>
<p> virtual <code>~QwtPlotSpectrogram</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setDisplayMode</code> (<code>DisplayMode</code>, bool on=true) </p>
<p> bool <code>testDisplayMode</code> (<code>DisplayMode</code>) const </p>
<p> void <code>setData</code> (<code>QwtRasterData</code> *<code>data</code>) </p>
<p> const <code>QwtRasterData</code> * <code>data</code> () const </p>
<p> <code>QwtRasterData</code> * <code>data</code> () </p>
<p> void <code>setColorMap</code> (<code>QwtColorMap</code> *) </p>
<p> const <code>QwtColorMap</code> * <code>colorMap</code> () const </p>
<p> virtual <code>QwtInterval</code> <code>interval</code> (Qt::Axis) const </p>
<p> virtual QRectF <code>pixelHint</code> (const QRectF &amp;) const<br />
 <i>Pixel hint. </i><br />
 void <code>setDefaultContourPen</code> (const QColor &amp;, qreal width=0.0, Qt::PenStyle=Qt::SolidLine) </p>
<p> void <code>setDefaultContourPen</code> (const QPen &amp;)<br />
 <i>Set the default pen for the contour lines. </i><br />
 QPen <code>defaultContourPen</code> () const </p>
<p> virtual QPen <code>contourPen</code> (double level) const<br />
 <i>Calculate the pen for a contour line. </i><br />
 void <code>setConrecFlag</code> (<code>QwtRasterData::ConrecFlag</code>, bool on) </p>
<p> bool <code>testConrecFlag</code> (<code>QwtRasterData::ConrecFlag</code>) const </p>
<p> void <code>setContourLevels</code> (const QList&lt; double &gt; &amp;) </p>
<p> QList&lt; double &gt; <code>contourLevels</code> () const </p>
<p> virtual int <code>rtti</code> () const </p>
<p> virtual void <code>draw</code> (QPainter *p, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;rect) const<br />
 <i>Draw the spectrogram. </i></p>
<h3>Protected Member Functions</h3>
<p>virtual QImage <code>renderImage</code> (const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;area, const QSize &amp;imageSize) const<br />
 <i>Render an image from data and color map. </i><br />
 virtual QSize <code>contourRasterSize</code> (const QRectF &amp;, const QRect &amp;) const<br />
 <i>Return the raster to be used by the CONREC contour algorithm. </i><br />
 virtual <code>QwtRasterData::ContourLines</code> <code>renderContourLines</code> (const QRectF &amp;rect, const QSize &amp;raster) const </p>
<p> virtual void <code>drawContourLines</code> (QPainter *p, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const <code>QwtRasterData::ContourLines</code> &amp;lines) const </p>
<p> void <code>renderTile</code> (const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRect &amp;imageRect, QImage *image) const<br />
 <i>Render a tile of an image. </i></p>
<h2>Detailed Description</h2>
<p>A plot item, which displays a spectrogram. </p>
<p> A spectrogram displays 3-dimensional data, where the 3rd dimension ( the intensity ) is displayed using colors. The colors are calculated from the values using a color map. </p>
<p> On multi-core systems the performance of the image composition can often be improved by dividing the area into tiles &#8211; each of them rendered in a different thread ( see <code>QwtPlotItem::setRenderThreadCount()</code> ). </p>
<p> In ContourMode contour lines are painted for the contour levels. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtRasterData</code>, <code>QwtColorMap</code>, <code>QwtPlotItem::setRenderThreadCount()</code></dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtPlotSpectrogram::DisplayMode</code></h3>
<p>The display mode controls how the raster data will be represented. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setDisplayMode()</code>, <code>testDisplayMode()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>ImageMode </i></p>
<dd>The values are mapped to colors using a color map.</p>
<dt><i>ContourMode </i></p>
<dd>The data is displayed using contour lines.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPlotSpectrogram::QwtPlotSpectrogram (const QString &amp;title = QString::null) [explicit]</h3>
<p>Sets the following item attributes:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd><code>QwtPlotItem::AutoScale</code>: true</p>
<dt>&bull;</p>
<dd><code>QwtPlotItem::Legend</code>: false</dl>
<p> The z value is initialized by 8.0. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>title</i> Title</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlotItem::setItemAttribute()</code>, <code>QwtPlotItem::setZ()</code></dl>
<h2>Member Function Documentation</h2>
<h3>const <code>QwtColorMap</code> * QwtPlotSpectrogram::colorMap () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Color Map used for mapping the intensity values to colors</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setColorMap()</code></dl>
<h3>QList&lt; double &gt; QwtPlotSpectrogram::contourLevels () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Levels of the contour lines.</dl>
<p> The levels are sorted in increasing order. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>contourLevels()</code>, <code>renderContourLines()</code>, <code>QwtRasterData::contourLines()</code></dl>
<h3>QPen QwtPlotSpectrogram::contourPen (doublelevel) const [virtual]</h3>
<p>Calculate the pen for a contour line. The color of the pen is the color for level calculated by the color map </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>level</i> Contour level</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Pen for the contour line</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>contourPen is only used if <code>defaultContourPen()</code>.style() == Qt::NoPen</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setDefaultContourPen()</code>, <code>setColorMap()</code>, <code>setContourLevels()</code></dl>
<h3>QSize QwtPlotSpectrogram::contourRasterSize (const QRectF &amp;area, const QRect &amp;rect) const [protected], [virtual]</h3>
<p>Return the raster to be used by the CONREC contour algorithm. A larger size will improve the precision of the CONREC algorithm, but will slow down the time that is needed to calculate the lines. </p>
<p> The default implementation returns rect.size() / 2 bounded to the resolution depending on pixelSize(). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>area</i> Rectangle, where to calculate the contour lines<br />
 <i>rect</i> Rectangle in pixel coordinates, where to paint the contour lines</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Raster to be used by the CONREC contour algorithm.</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The size will be bounded to rect.size().</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>drawContourLines()</code>, <code>QwtRasterData::contourLines()</code></dl>
<h3>const <code>QwtRasterData</code> * QwtPlotSpectrogram::data () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Spectrogram data</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setData()</code></dl>
<h3><code>QwtRasterData</code> * QwtPlotSpectrogram::data ()</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Spectrogram data</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setData()</code></dl>
<h3>QPen QwtPlotSpectrogram::defaultContourPen () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Default contour pen</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setDefaultContourPen()</code></dl>
<h3>void QwtPlotSpectrogram::draw (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;canvasRect) const [virtual]</h3>
<p>Draw the spectrogram. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>xMap</i> Maps x-values into pixel coordinates.<br />
 <i>yMap</i> Maps y-values into pixel coordinates.<br />
 <i>canvasRect</i> Contents rectangle of the canvas in painter coordinates</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setDisplayMode()</code>, <code>renderImage()</code>, <code>QwtPlotRasterItem::draw()</code>, <code>drawContourLines()</code></dl>
<p> Reimplemented from <code>QwtPlotRasterItem</code>.</p>
<h3>void QwtPlotSpectrogram::drawContourLines (QPainter *painter, const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const <code>QwtRasterData::ContourLines</code> &amp;contourLines) const [protected], [virtual]</h3>
<p>Paint the contour lines </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>xMap</i> Maps x-values into pixel coordinates.<br />
 <i>yMap</i> Maps y-values into pixel coordinates.<br />
 <i>contourLines</i> Contour lines</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>renderContourLines()</code>, <code>defaultContourPen()</code>, <code>contourPen()</code></dl>
<h3><code>QwtInterval</code> QwtPlotSpectrogram::interval (Qt::Axisaxis) const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Bounding interval for an axis</dl>
<p> The default implementation returns the interval of the associated raster data object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axis</i> X, Y, or Z axis</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtRasterData::interval()</code></dl>
<p> Reimplemented from <code>QwtPlotRasterItem</code>.</p>
<h3>QRectF QwtPlotSpectrogram::pixelHint (const QRectF &amp;area) const [virtual]</h3>
<p>Pixel hint. The geometry of a pixel is used to calculated the resolution and alignment of the rendered image. </p>
<p> The default implementation returns <code>data()</code>-&gt;pixelHint( rect ); </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>area</i> In most implementations the resolution of the data doesn&#8217;t depend on the requested area.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Bounding rectangle of a pixel</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlotRasterItem::pixelHint()</code>, <code>QwtRasterData::pixelHint()</code>, render(), <code>renderImage()</code></dl>
<p> Reimplemented from <code>QwtPlotRasterItem</code>.</p>
<h3><code>QwtRasterData::ContourLines</code> QwtPlotSpectrogram::renderContourLines (const QRectF &amp;rect, const QSize &amp;raster) const [protected], [virtual]</h3>
<p>Calculate contour lines </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rect</i> Rectangle, where to calculate the contour lines<br />
 <i>raster</i> Raster, used by the CONREC algorithm</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Calculated contour lines</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>contourLevels()</code>, <code>setConrecFlag()</code>, <code>QwtRasterData::contourLines()</code></dl>
<h3>QImage QwtPlotSpectrogram::renderImage (const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRectF &amp;area, const QSize &amp;imageSize) const [protected], [virtual]</h3>
<p>Render an image from data and color map. For each pixel of area the value is mapped into a color. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>xMap</i> X-Scale Map<br />
 <i>yMap</i> Y-Scale Map<br />
 <i>area</i> Requested area for the image in scale coordinates<br />
 <i>imageSize</i> Size of the requested image</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A QImage::Format_Indexed8 or QImage::Format_ARGB32 depending on the color map.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtRasterData::value()</code>, <code>QwtColorMap::rgb()</code>, <code>QwtColorMap::colorIndex()</code></dl>
<p> Implements <code>QwtPlotRasterItem</code>.</p>
<h3>void QwtPlotSpectrogram::renderTile (const <code>QwtScaleMap</code> &amp;xMap, const <code>QwtScaleMap</code> &amp;yMap, const QRect &amp;tile, QImage *image) const [protected]</h3>
<p>Render a tile of an image. Rendering in tiles can be used to composite an image in parallel threads. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>xMap</i> X-Scale Map<br />
 <i>yMap</i> Y-Scale Map<br />
 <i>tile</i> Geometry of the tile in image coordinates<br />
 <i>image</i> Image to be rendered</dl>
<h3>int QwtPlotSpectrogram::rtti () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd><code>QwtPlotItem::Rtti_PlotSpectrogram</code></dl>
<p> Reimplemented from <code>QwtPlotItem</code>.</p>
<h3>void QwtPlotSpectrogram::setColorMap (<code>QwtColorMap</code> *colorMap)</h3>
<p>Change the color map </p>
<p> Often it is useful to display the mapping between intensities and colors as an additional plot axis, showing a color bar. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>colorMap</i> Color Map</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>colorMap()</code>, <code>QwtScaleWidget::setColorBarEnabled()</code>, <code>QwtScaleWidget::setColorMap()</code></dl>
<h3>void QwtPlotSpectrogram::setConrecFlag (<code>QwtRasterData::ConrecFlag</code>flag, boolon)</h3>
<p>Modify an attribute of the CONREC algorithm, used to calculate the contour lines. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>flag</i> CONREC flag<br />
 <i>on</i> On/Off</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>testConrecFlag()</code>, <code>renderContourLines()</code>, <code>QwtRasterData::contourLines()</code></dl>
<h3>void QwtPlotSpectrogram::setContourLevels (const QList&lt; double &gt; &amp;levels)</h3>
<p>Set the levels of the contour lines </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>levels</i> Values of the contour levels</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>contourLevels()</code>, <code>renderContourLines()</code>, <code>QwtRasterData::contourLines()</code></dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>contourLevels returns the same levels but sorted.</dl>
<h3>void QwtPlotSpectrogram::setData (<code>QwtRasterData</code> *data)</h3>
<p>Set the data to be displayed </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> Spectrogram Data</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>data()</code></dl>
<h3>void QwtPlotSpectrogram::setDefaultContourPen (const QColor &amp;color, qrealwidth = 0.0, Qt::PenStylestyle = Qt::SolidLine)</h3>
<p>Build and assign the default pen for the contour lines </p>
<p> In Qt5 the default pen width is 1.0 ( 0.0 in Qt4 ) what makes it non cosmetic ( see QPen::isCosmetic() ). This method has been introduced to hide this incompatibility. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>color</i> Pen color<br />
 <i>width</i> Pen width<br />
 <i>style</i> Pen style</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>pen(), brush()</dl>
<h3>void QwtPlotSpectrogram::setDefaultContourPen (const QPen &amp;pen)</h3>
<p>Set the default pen for the contour lines. If the spectrogram has a valid default contour pen a contour line is painted using the default contour pen. Otherwise (pen.style() == Qt::NoPen) the pen is calculated for each contour level using <code>contourPen()</code>. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>defaultContourPen()</code>, <code>contourPen()</code></dl>
<h3>void QwtPlotSpectrogram::setDisplayMode (<code>DisplayMode</code>mode, boolon = true)</h3>
<p>The display mode controls how the raster data will be represented. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>mode</i> Display mode<br />
 <i>on</i> On/Off</dl>
<p> The default setting enables ImageMode. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>DisplayMode</code>, displayMode()</dl>
<h3>bool QwtPlotSpectrogram::testConrecFlag (<code>QwtRasterData::ConrecFlag</code>flag) const</h3>
<p>Test an attribute of the CONREC algorithm, used to calculate the contour lines. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>flag</i> CONREC flag</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true, is enabled</dl>
<p> The default setting enables <code>QwtRasterData::IgnoreAllVerticesOnLevel</code> </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>setConrecClag(), <code>renderContourLines()</code>, <code>QwtRasterData::contourLines()</code></dl>
<h3>bool QwtPlotSpectrogram::testDisplayMode (<code>DisplayMode</code>mode) const</h3>
<p>The display mode controls how the raster data will be represented. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>mode</i> Display mode</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true if mode is enabled</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
