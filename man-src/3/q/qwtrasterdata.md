---
title: "qwtrasterdata(3)"
name: "qwtrasterdata"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtrasterdata/"
description: "QwtRasterData –"
---

<p>QwtRasterData &#8211; </p>
<p> <code>QwtRasterData</code> defines an interface to any type of raster data.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_raster_data.h&gt; </p>
<p> Inherited by <code>QwtMatrixRasterData</code>.</p>
<h3>Public Types</h3>
<p>enum <code>ConrecFlag</code> { <code>IgnoreAllVerticesOnLevel</code> = 0x01, <code>IgnoreOutOfRange</code> = 0x02 }<br />
 <i>Flags to modify the contour algorithm. </i><br />
 typedef QMap&lt; double, QPolygonF &gt; <code>ContourLines</code><br />
 <i>Contour lines. </i><br />
 typedef QFlags&lt; <code>ConrecFlag</code> &gt; <code>ConrecFlags</code><br />
 <i>Flags to modify the contour algorithm. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtRasterData</code> ()<br />
 <i>Constructor. </i><br />
 virtual <code>~QwtRasterData</code> ()<br />
 <i>Destructor. </i><br />
 virtual void <code>setInterval</code> (Qt::Axis, const <code>QwtInterval</code> &amp;) </p>
<p> const <code>QwtInterval</code> &amp; <code>interval</code> (Qt::Axis) const </p>
<p> virtual QRectF <code>pixelHint</code> (const QRectF &amp;) const<br />
 <i>Pixel hint. </i><br />
 virtual void <code>initRaster</code> (const QRectF &amp;, const QSize &amp;raster)<br />
 <i>Initialize a raster. </i><br />
 virtual void <code>discardRaster</code> ()<br />
 <i>Discard a raster. </i><br />
 virtual double <code>value</code> (double x, double y) const =0 </p>
<p> virtual <code>ContourLines</code> <code>contourLines</code> (const QRectF &amp;rect, const QSize &amp;raster, const QList&lt; double &gt; &amp;levels, <code>ConrecFlags</code>) const </p>
<h2>Detailed Description</h2>
<p><code>QwtRasterData</code> defines an interface to any type of raster data. </p>
<p> <code>QwtRasterData</code> is an abstract interface, that is used by <code>QwtPlotRasterItem</code> to find the values at the pixels of its raster. </p>
<p> Often a raster item is used to display values from a matrix. Then the derived raster data class needs to implement some sort of resampling, that maps the raster of the matrix into the requested raster of the raster item ( depending on resolution and scales of the canvas ).</p>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtRasterData::ConrecFlag</code></h3>
<p>Flags to modify the contour algorithm. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>IgnoreAllVerticesOnLevel </i></p>
<dd>Ignore all vertices on the same level.</p>
<dt><i>IgnoreOutOfRange </i></p>
<dd>Ignore all values, that are out of range.</dl>
<h2>Member Function Documentation</h2>
<h3><code>QwtRasterData::ContourLines</code> QwtRasterData::contourLines (const QRectF &amp;rect, const QSize &amp;raster, const QList&lt; double &gt; &amp;levels, <code>ConrecFlags</code>flags) const [virtual]</h3>
<p>Calculate contour lines </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rect</i> Bounding rectangle for the contour lines<br />
 <i>raster</i> Number of data pixels of the raster data<br />
 <i>levels</i> List of limits, where to insert contour lines<br />
 <i>flags</i> Flags to customize the contouring algorithm</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Calculated contour lines</dl>
<p> An adaption of CONREC, a simple contouring algorithm. <a rel="nofollow" href="http://local.wasp.uwa.edu.au/~pbourke/papers/conrec/">http://local.wasp.uwa.edu.au/~pbourke/papers/conrec/</a></p>
<h3>void QwtRasterData::discardRaster () [virtual]</h3>
<p>Discard a raster. After the composition of an image <code>QwtPlotSpectrogram</code> calls <code>discardRaster()</code>. </p>
<p> The default implementation does nothing, but if data has been loaded in <code>initRaster()</code>, it could deleted now. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>initRaster()</code>, <code>value()</code></dl>
<h3>void QwtRasterData::initRaster (const QRectF &amp;area, const QSize &amp;raster) [virtual]</h3>
<p>Initialize a raster. Before the composition of an image <code>QwtPlotSpectrogram</code> calls <code>initRaster()</code>, announcing the area and its resolution that will be requested. </p>
<p> The default implementation does nothing, but for data sets that are stored in files, it might be good idea to reimplement <code>initRaster()</code>, where the data is resampled and loaded into memory. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>area</i> Area of the raster<br />
 <i>raster</i> Number of horizontal and vertical pixels</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>initRaster()</code>, <code>value()</code></dl>
<h3>const <code>QwtInterval</code> &amp; QwtRasterData::interval (Qt::Axisaxis) const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Bounding interval for a axis</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setInterval</code></dl>
<h3>QRectF QwtRasterData::pixelHint (const QRectF &amp;area) const [virtual]</h3>
<p>Pixel hint. <code>pixelHint()</code> returns the geometry of a pixel, that can be used to calculate the resolution and alignment of the plot item, that is representing the data. </p>
<p> Width and height of the hint need to be the horizontal and vertical distances between 2 neighbored points. The center of the hint has to be the position of any point ( it doesn&#8217;t matter which one ). </p>
<p> An empty hint indicates, that there are values for any detail level. </p>
<p> Limiting the resolution of the image might significantly improve the performance and heavily reduce the amount of memory when rendering a QImage from the raster data. </p>
<p> The default implementation returns an empty rectangle recommending to render in target device ( f.e. screen ) resolution. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>area</i> In most implementations the resolution of the data doesn&#8217;t depend on the requested area.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Bounding rectangle of a pixel</dl>
<p> Reimplemented in <code>QwtMatrixRasterData</code>.</p>
<h3>void QwtRasterData::setInterval (Qt::Axisaxis, const <code>QwtInterval</code> &amp;interval) [virtual]</h3>
<p>Set the bounding interval for the x, y or z coordinates. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axis</i> Axis<br />
 <i>interval</i> Bounding interval</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>interval()</code></dl>
<p> Reimplemented in <code>QwtMatrixRasterData</code>.</p>
<h3>virtual double QwtRasterData::value (doublex, doubley) const [pure virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the value at a raster position</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>x</i> X value in plot coordinates<br />
 <i>y</i> Y value in plot coordinates</dl>
<p> Implemented in <code>QwtMatrixRasterData</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
