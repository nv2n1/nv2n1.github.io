---
title: "qwtlinearcolormap(3)"
name: "qwtlinearcolormap"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtlinearcolormap/"
description: "QwtLinearColorMap –"
---

<p>QwtLinearColorMap &#8211; </p>
<p> <code>QwtLinearColorMap</code> builds a color map from color stops.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_color_map.h&gt; </p>
<p> Inherits <code>QwtColorMap</code>.</p>
<h3>Public Types</h3>
<p>enum <code>Mode</code> { <code>FixedColors</code>, <code>ScaledColors</code> } </p>
<h3>Public Member Functions</h3>
<p><code>QwtLinearColorMap</code> (<code>QwtColorMap::Format</code>=<code>QwtColorMap::RGB</code>) </p>
<p> <code>QwtLinearColorMap</code> (const QColor &amp;from, const QColor &amp;to, <code>QwtColorMap::Format</code>=<code>QwtColorMap::RGB</code>) </p>
<p> virtual <code>~QwtLinearColorMap</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setMode</code> (<code>Mode</code>)<br />
 <i>Set the mode of the color map. </i><br />
 <code>Mode</code> <code>mode</code> () const </p>
<p> void <code>setColorInterval</code> (const QColor &amp;<code>color1</code>, const QColor &amp;<code>color2</code>) </p>
<p> void <code>addColorStop</code> (double value, const QColor &amp;) </p>
<p> QVector&lt; double &gt; <code>colorStops</code> () const </p>
<p> QColor <code>color1</code> () const </p>
<p> QColor <code>color2</code> () const </p>
<p> virtual QRgb <code>rgb</code> (const <code>QwtInterval</code> &amp;, double value) const </p>
<p> virtual unsigned char <code>colorIndex</code> (const <code>QwtInterval</code> &amp;, double value) const<br />
 <i>Map a value of a given interval into a color index. </i></p>
<h2>Detailed Description</h2>
<p><code>QwtLinearColorMap</code> builds a color map from color stops. </p>
<p> A color stop is a color at a specific position. The valid range for the positions is [0.0, 1.0]. When mapping a value into a color it is translated into this interval according to <code>mode()</code>.</p>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtLinearColorMap::Mode</code></h3>
<p>Mode of color map </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setMode()</code>, <code>mode()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>FixedColors </i></p>
<dd>Return the color from the next lower color stop.</p>
<dt><i>ScaledColors </i></p>
<dd>Interpolating the colors of the adjacent stops.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtLinearColorMap::QwtLinearColorMap (<code>QwtColorMap::Format</code>format = <code>QwtColorMap::RGB</code>)</h3>
<p>Build a color map with two stops at 0.0 and 1.0. The color at 0.0 is Qt::blue, at 1.0 it is Qt::yellow. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>format</i> Preferred format of the color map</dl>
<h3>QwtLinearColorMap::QwtLinearColorMap (const QColor &amp;color1, const QColor &amp;color2, <code>QwtColorMap::Format</code>format = <code>QwtColorMap::RGB</code>)</h3>
<p>Build a color map with two stops at 0.0 and 1.0. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>color1</i> Color used for the minimum value of the value interval<br />
 <i>color2</i> Color used for the maximum value of the value interval<br />
 <i>format</i> Preferred format for the color map</dl>
<h2>Member Function Documentation</h2>
<h3>void QwtLinearColorMap::addColorStop (doublevalue, const QColor &amp;color)</h3>
<p>Add a color stop </p>
<p> The value has to be in the range [0.0, 1.0]. F.e. a stop at position 17.0 for a range [10.0,20.0] must be passed as: (17.0 &#8211; 10.0) / (20.0 &#8211; 10.0) </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Value between [0.0, 1.0]<br />
 <i>color</i> Color stop</dl>
<h3>QColor QwtLinearColorMap::color1 () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the first color of the color range</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setColorInterval()</code></dl>
<h3>QColor QwtLinearColorMap::color2 () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the second color of the color range</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setColorInterval()</code></dl>
<h3>unsigned char QwtLinearColorMap::colorIndex (const <code>QwtInterval</code> &amp;interval, doublevalue) const [virtual]</h3>
<p>Map a value of a given interval into a color index. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>interval</i> Range for all values<br />
 <i>value</i> Value to map into a color index</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Index, between 0 and 255</dl>
<p> Implements <code>QwtColorMap</code>.</p>
<h3>QVector&lt; double &gt; QwtLinearColorMap::colorStops () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Positions of color stops in increasing order</dl>
<h3><code>QwtLinearColorMap::Mode</code> QwtLinearColorMap::mode () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Mode of the color map</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setMode()</code></dl>
<h3>QRgb QwtLinearColorMap::rgb (const <code>QwtInterval</code> &amp;interval, doublevalue) const [virtual]</h3>
<p>Map a value of a given interval into a RGB value </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>interval</i> Range for all values<br />
 <i>value</i> Value to map into a RGB value</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>RGB value for value</dl>
<p> Implements <code>QwtColorMap</code>.</p>
<h3>void QwtLinearColorMap::setColorInterval (const QColor &amp;color1, const QColor &amp;color2)</h3>
<p>Set the color range </p>
<p> Add stops at 0.0 and 1.0. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>color1</i> Color used for the minimum value of the value interval<br />
 <i>color2</i> Color used for the maximum value of the value interval</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>color1()</code>, <code>color2()</code></dl>
<h3>void QwtLinearColorMap::setMode (<code>Mode</code>mode)</h3>
<p>Set the mode of the color map. FixedColors means the color is calculated from the next lower color stop. ScaledColors means the color is calculated by interpolating the colors of the adjacent stops. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>mode()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
