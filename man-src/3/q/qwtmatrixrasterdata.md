---
title: "qwtmatrixrasterdata(3)"
name: "qwtmatrixrasterdata"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtmatrixrasterdata/"
description: "QwtMatrixRasterData –"
---

<p>QwtMatrixRasterData &#8211; </p>
<p> A class representing a matrix of values as raster data.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_matrix_raster_data.h&gt; </p>
<p> Inherits <code>QwtRasterData</code>.</p>
<h3>Public Types</h3>
<p>enum <code>ResampleMode</code> { <code>NearestNeighbour</code>, <code>BilinearInterpolation</code> }<br />
 <i>Resampling algorithm The default setting is NearestNeighbour;. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtMatrixRasterData</code> ()<br />
 <i>Constructor. </i><br />
 virtual <code>~QwtMatrixRasterData</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setResampleMode</code> (<code>ResampleMode</code> mode)<br />
 <i>Set the resampling algorithm. </i><br />
 <code>ResampleMode</code> <code>resampleMode</code> () const </p>
<p> virtual void <code>setInterval</code> (Qt::Axis, const <code>QwtInterval</code> &amp;)<br />
 <i>Assign the bounding interval for an axis. </i><br />
 void <code>setValueMatrix</code> (const QVector&lt; double &gt; &amp;values, int <code>numColumns</code>)<br />
 <i>Assign a value matrix. </i><br />
 const QVector&lt; double &gt; <code>valueMatrix</code> () const </p>
<p> void <code>setValue</code> (int row, int col, double <code>value</code>)<br />
 <i>Change a single value in the matrix. </i><br />
 int <code>numColumns</code> () const </p>
<p> int <code>numRows</code> () const </p>
<p> virtual QRectF <code>pixelHint</code> (const QRectF &amp;) const<br />
 <i>Calculate the pixel hint. </i><br />
 virtual double <code>value</code> (double x, double y) const </p>
<h2>Detailed Description</h2>
<p>A class representing a matrix of values as raster data. </p>
<p> <code>QwtMatrixRasterData</code> implements an interface for a matrix of equidistant values, that can be used by a <code>QwtPlotRasterItem</code>. It implements a couple of resampling algorithms, to provide values for positions, that or not on the value matrix.</p>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtMatrixRasterData::ResampleMode</code></h3>
<p>Resampling algorithm The default setting is NearestNeighbour;. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>NearestNeighbour </i></p>
<dd>Return the value from the matrix, that is nearest to the the requested position.</p>
<dt><i>BilinearInterpolation </i></p>
<dd>Interpolate the value from the distances and values of the 4 surrounding values in the matrix,</dl>
<h2>Member Function Documentation</h2>
<h3>int QwtMatrixRasterData::numColumns () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Number of columns of the value matrix</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>valueMatrix()</code>, <code>numRows()</code>, <code>setValueMatrix()</code></dl>
<h3>int QwtMatrixRasterData::numRows () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Number of rows of the value matrix</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>valueMatrix()</code>, <code>numColumns()</code>, <code>setValueMatrix()</code></dl>
<h3>QRectF QwtMatrixRasterData::pixelHint (const QRectF &amp;area) const [virtual]</h3>
<p>Calculate the pixel hint. <code>pixelHint()</code> returns the geometry of a pixel, that can be used to calculate the resolution and alignment of the plot item, that is representing the data. </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>NearestNeighbour </p>
<p>&nbsp;<wbr><code>pixelHint()</code>&nbsp;<wbr>returns the surrounding pixel of the top left value in the matrix.</p>
<dt>&bull;</p>
<dd>BilinearInterpolation </p>
<p>&nbsp;<wbr>Returns an empty rectangle recommending to render in target device&nbsp;<wbr>(&nbsp;<wbr>f.e. screen&nbsp;<wbr>)&nbsp;<wbr>resolution.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>area</i> Requested area, ignored</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Calculated hint</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>ResampleMode</code>, setMatrix(), <code>setInterval()</code></dl>
<p> Reimplemented from <code>QwtRasterData</code>.</p>
<h3><code>QwtMatrixRasterData::ResampleMode</code> QwtMatrixRasterData::resampleMode () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>resampling algorithm</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setResampleMode()</code>, <code>value()</code></dl>
<h3>void QwtMatrixRasterData::setInterval (Qt::Axisaxis, const <code>QwtInterval</code> &amp;interval) [virtual]</h3>
<p>Assign the bounding interval for an axis. Setting the bounding intervals for the X/Y axis is mandatory to define the positions for the values of the value matrix. The interval in Z direction defines the possible range for the values in the matrix, what is f.e used by <code>QwtPlotSpectrogram</code> to map values to colors. The Z-interval might be the bounding interval of the values in the matrix, but usually it isn&#8217;t. ( f.e a interval of 0.0-100.0 for values in percentage ) </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>axis</i> X, Y or Z axis<br />
 <i>interval</i> Interval</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtRasterData::interval()</code>, <code>setValueMatrix()</code></dl>
<p> Reimplemented from <code>QwtRasterData</code>.</p>
<h3>void QwtMatrixRasterData::setResampleMode (<code>ResampleMode</code>mode)</h3>
<p>Set the resampling algorithm. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>mode</i> Resampling mode</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>resampleMode()</code>, <code>value()</code></dl>
<h3>void QwtMatrixRasterData::setValue (introw, intcol, doublevalue)</h3>
<p>Change a single value in the matrix. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>row</i> Row index<br />
 <i>col</i> Column index<br />
 <i>value</i> New value</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>value()</code>, <code>setValueMatrix()</code></dl>
<h3>void QwtMatrixRasterData::setValueMatrix (const QVector&lt; double &gt; &amp;values, intnumColumns)</h3>
<p>Assign a value matrix. The positions of the values are calculated by dividing the bounding rectangle of the X/Y intervals into equidistant rectangles ( pixels ). Each value corresponds to the center of a pixel. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>values</i> Vector of values<br />
 <i>numColumns</i> Number of columns</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>valueMatrix()</code>, <code>numColumns()</code>, <code>numRows()</code>, <code>setInterval()</code>()</dl>
<h3>double QwtMatrixRasterData::value (doublex, doubley) const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the value at a raster position</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>x</i> X value in plot coordinates<br />
 <i>y</i> Y value in plot coordinates</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>ResampleMode</code></dl>
<p> Implements <code>QwtRasterData</code>.</p>
<h3>const QVector&lt; double &gt; QwtMatrixRasterData::valueMatrix () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Value matrix</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setValueMatrix()</code>, <code>numColumns()</code>, <code>numRows()</code>, <code>setInterval()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
