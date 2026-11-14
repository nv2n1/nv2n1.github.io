---
title: "qwtcolormap(3)"
name: "qwtcolormap"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtcolormap/"
description: "QwtColorMap –"
---

<p>QwtColorMap &#8211; </p>
<p> <code>QwtColorMap</code> is used to map values into colors.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_color_map.h&gt; </p>
<p> Inherited by <code>QwtAlphaColorMap</code>, and <code>QwtLinearColorMap</code>.</p>
<h3>Public Types</h3>
<p>enum <code>Format</code> { <code>RGB</code>, <code>Indexed</code> } </p>
<h3>Public Member Functions</h3>
<p><code>QwtColorMap</code> (<code>Format</code>=<code>QwtColorMap::RGB</code>)<br />
 <i>Constructor. </i><br />
 virtual <code>~QwtColorMap</code> ()<br />
 <i>Destructor. </i><br />
 <code>Format</code> <code>format</code> () const </p>
<p> virtual QRgb <code>rgb</code> (const <code>QwtInterval</code> &amp;interval, double value) const =0 </p>
<p> virtual unsigned char <code>colorIndex</code> (const <code>QwtInterval</code> &amp;interval, double value) const =0 </p>
<p> QColor <code>color</code> (const <code>QwtInterval</code> &amp;, double value) const </p>
<p> virtual QVector&lt; QRgb &gt; <code>colorTable</code> (const <code>QwtInterval</code> &amp;) const </p>
<h2>Detailed Description</h2>
<p><code>QwtColorMap</code> is used to map values into colors. </p>
<p> For displaying 3D data on a 2D plane the 3rd dimension is often displayed using colors, like f.e in a spectrogram. </p>
<p> Each color map is optimized to return colors for only one of the following image formats: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>QImage::Format_Indexed8 </p>
<dt>&bull;</p>
<dd>QImage::Format_ARGB32 </p>
<p>&nbsp;<wbr></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlotSpectrogram</code>, <code>QwtScaleWidget</code></dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtColorMap::Format</code></h3>
<p>Format for color mapping </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>rgb()</code>, <code>colorIndex()</code>, <code>colorTable()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>RGB </i></p>
<dd>The map is intended to map into RGB values.</p>
<dt><i>Indexed </i></p>
<dd>The map is intended to map into 8 bit values, that are indices into the color table.</dl>
<h2>Member Function Documentation</h2>
<h3>QColor QwtColorMap::color (const <code>QwtInterval</code> &amp;interval, doublevalue) const [inline]</h3>
<p>Map a value into a color </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>interval</i> Valid interval for values<br />
 <i>value</i> Value</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Color corresponding to value</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>This method is slow for Indexed color maps. If it is necessary to map many values, its better to get the color table once and find the color using <code>colorIndex()</code>.</dl>
<h3>virtual unsigned char QwtColorMap::colorIndex (const <code>QwtInterval</code> &amp;interval, doublevalue) const [pure virtual]</h3>
<p>Map a value of a given interval into a color index </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>interval</i> Range for the values<br />
 <i>value</i> Value</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>color index, corresponding to value</dl>
<p> Implemented in <code>QwtLinearColorMap</code>.</p>
<h3>QVector&lt; QRgb &gt; QwtColorMap::colorTable (const <code>QwtInterval</code> &amp;interval) const [virtual]</h3>
<p>Build and return a color map of 256 colors </p>
<p> The color table is needed for rendering indexed images in combination with using <code>colorIndex()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>interval</i> Range for the values</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A color table, that can be used for a QImage</dl>
<h3><code>QwtColorMap::Format</code> QwtColorMap::format () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Intended format of the color map</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>Format</code></dl>
<h3>virtual QRgb QwtColorMap::rgb (const <code>QwtInterval</code> &amp;interval, doublevalue) const [pure virtual]</h3>
<p>Map a value of a given interval into a RGB value. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>interval</i> Range for the values<br />
 <i>value</i> Value</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>RGB value, corresponding to value</dl>
<p> Implemented in <code>QwtAlphaColorMap</code>, and <code>QwtLinearColorMap</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
