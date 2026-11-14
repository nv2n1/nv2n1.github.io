---
title: "qwtabstractscaledraw(3)"
name: "qwtabstractscaledraw"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtabstractscaledraw/"
description: "QwtAbstractScaleDraw –"
---

<p>QwtAbstractScaleDraw &#8211; </p>
<p> A abstract base class for drawing scales.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_abstract_scale_draw.h&gt; </p>
<p> Inherited by <code>QwtRoundScaleDraw</code>, and <code>QwtScaleDraw</code>.</p>
<h3>Public Types</h3>
<p>enum <code>ScaleComponent</code> { <code>Backbone</code> = 0x01, <code>Ticks</code> = 0x02, <code>Labels</code> = 0x04 } </p>
<p> typedef QFlags&lt; <code>ScaleComponent</code> &gt; <code>ScaleComponents</code><br />
 <i>Scale components. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtAbstractScaleDraw</code> ()<br />
 <i>Constructor. </i><br />
 virtual <code>~QwtAbstractScaleDraw</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setScaleDiv</code> (const <code>QwtScaleDiv</code> &amp;s) </p>
<p> const <code>QwtScaleDiv</code> &amp; <code>scaleDiv</code> () const </p>
<p> void <code>setTransformation</code> (<code>QwtTransform</code> *) </p>
<p> const <code>QwtScaleMap</code> &amp; <code>scaleMap</code> () const </p>
<p> <code>QwtScaleMap</code> &amp; <code>scaleMap</code> () </p>
<p> void <code>enableComponent</code> (<code>ScaleComponent</code>, bool enable=true) </p>
<p> bool <code>hasComponent</code> (<code>ScaleComponent</code>) const </p>
<p> void <code>setTickLength</code> (<code>QwtScaleDiv::TickType</code>, double length) </p>
<p> double <code>tickLength</code> (<code>QwtScaleDiv::TickType</code>) const </p>
<p> double <code>maxTickLength</code> () const </p>
<p> void <code>setSpacing</code> (double margin)<br />
 <i>Set the spacing between tick and labels. </i><br />
 double <code>spacing</code> () const<br />
 <i>Get the spacing. </i><br />
 void <code>setPenWidth</code> (int width)<br />
 <i>Specify the width of the scale pen. </i><br />
 int <code>penWidth</code> () const </p>
<p> virtual void <code>draw</code> (QPainter *, const QPalette &amp;) const<br />
 <i>Draw the scale. </i><br />
 virtual <code>QwtText</code> <code>label</code> (double) const<br />
 <i>Convert a value into its representing label. </i><br />
 virtual double <code>extent</code> (const QFont &amp;font) const =0 </p>
<p> void <code>setMinimumExtent</code> (double)<br />
 <i>Set a minimum for the extent. </i><br />
 double <code>minimumExtent</code> () const </p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>drawTick</code> (QPainter *painter, double value, double len) const =0 </p>
<p> virtual void <code>drawBackbone</code> (QPainter *painter) const =0 </p>
<p> virtual void <code>drawLabel</code> (QPainter *painter, double value) const =0 </p>
<p> void <code>invalidateCache</code> () </p>
<p> const <code>QwtText</code> &amp; <code>tickLabel</code> (const QFont &amp;, double value) const<br />
 <i>Convert a value into its representing label and cache it. </i></p>
<h2>Detailed Description</h2>
<p>A abstract base class for drawing scales. </p>
<p> <code>QwtAbstractScaleDraw</code> can be used to draw linear or logarithmic scales. </p>
<p> After a scale division has been specified as a <code>QwtScaleDiv</code> object using <code>setScaleDiv()</code>, the scale can be drawn with the <code>draw()</code> member.</p>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtAbstractScaleDraw::ScaleComponent</code></h3>
<p>Components of a scale </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>enableComponent()</code>, <code>hasComponent</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>Backbone </i></p>
<dd>Backbone = the line where the ticks are located.</p>
<dt><i>Ticks </i></p>
<dd>Ticks.</p>
<dt><i>Labels </i></p>
<dd>Labels.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtAbstractScaleDraw::QwtAbstractScaleDraw ()</h3>
<p>Constructor. The range of the scale is initialized to [0, 100], The spacing (distance between ticks and labels) is set to 4, the tick lengths are set to 4,6 and 8 pixels</p>
<h2>Member Function Documentation</h2>
<h3>void QwtAbstractScaleDraw::draw (QPainter *painter, const QPalette &amp;palette) const [virtual]</h3>
<p>Draw the scale. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> The painter<br />
 <i>palette</i> Palette, text color is used for the labels, foreground color for ticks and backbone</dl>
<h3>virtual void QwtAbstractScaleDraw::drawBackbone (QPainter *painter) const [protected], [pure virtual]</h3>
<p>Draws the baseline of the scale </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>drawTick()</code>, <code>drawLabel()</code></dl>
<p> Implemented in <code>QwtScaleDraw</code>, and <code>QwtRoundScaleDraw</code>.</p>
<h3>virtual void QwtAbstractScaleDraw::drawLabel (QPainter *painter, doublevalue) const [protected], [pure virtual]</h3>
<p>Draws the label for a major scale tick </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>value</i> Value</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>drawTick()</code>, <code>drawBackbone()</code></dl>
<p> Implemented in <code>QwtScaleDraw</code>, and <code>QwtRoundScaleDraw</code>.</p>
<h3>virtual void QwtAbstractScaleDraw::drawTick (QPainter *painter, doublevalue, doublelen) const [protected], [pure virtual]</h3>
<p>Draw a tick </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>value</i> Value of the tick<br />
 <i>len</i> Length of the tick</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>drawBackbone()</code>, <code>drawLabel()</code></dl>
<p> Implemented in <code>QwtScaleDraw</code>, and <code>QwtRoundScaleDraw</code>.</p>
<h3>void QwtAbstractScaleDraw::enableComponent (<code>ScaleComponent</code>component, boolenable = true)</h3>
<p>En/Disable a component of the scale </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>component</i> Scale component<br />
 <i>enable</i> On/Off</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>hasComponent()</code></dl>
<h3>virtual double QwtAbstractScaleDraw::extent (const QFont &amp;font) const [pure virtual]</h3>
<p>Calculate the extent </p>
<p> The extent is the distance from the baseline to the outermost pixel of the scale draw in opposite to its orientation. It is at least <code>minimumExtent()</code> pixels. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>font</i> Font used for drawing the tick labels</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Number of pixels</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setMinimumExtent()</code>, <code>minimumExtent()</code></dl>
<p> Implemented in <code>QwtScaleDraw</code>, and <code>QwtRoundScaleDraw</code>.</p>
<h3>bool QwtAbstractScaleDraw::hasComponent (<code>ScaleComponent</code>component) const</h3>
<p>Check if a component is enabled </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>component</i> Component type</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true, when component is enabled</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>enableComponent()</code></dl>
<h3>void QwtAbstractScaleDraw::invalidateCache () [protected]</h3>
<p>Invalidate the cache used by <code>tickLabel()</code> </p>
<p> The cache is invalidated, when a new <code>QwtScaleDiv</code> is set. If the labels need to be changed. while the same <code>QwtScaleDiv</code> is set, <code>invalidateCache()</code> needs to be called manually.</p>
<h3><code>QwtText</code> QwtAbstractScaleDraw::label (doublevalue) const [virtual]</h3>
<p>Convert a value into its representing label. The value is converted to a plain text using QLocale().toString(value). This method is often overloaded by applications to have individual labels. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Value</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Label string.</dl>
<p> Reimplemented in <code>QwtDateScaleDraw</code>, and <code>QwtCompassScaleDraw</code>.</p>
<h3>double QwtAbstractScaleDraw::maxTickLength () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Length of the longest tick</dl>
<p> Useful for layout calculations </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>tickLength()</code>, <code>setTickLength()</code></dl>
<h3>double QwtAbstractScaleDraw::minimumExtent () const</h3>
<p>Get the minimum extent </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Minimum extent</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>extent()</code>, <code>setMinimumExtent()</code></dl>
<h3>int QwtAbstractScaleDraw::penWidth () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Scale pen width</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPenWidth()</code></dl>
<h3>const <code>QwtScaleDiv</code> &amp; QwtAbstractScaleDraw::scaleDiv () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>scale division</dl>
<h3>const <code>QwtScaleMap</code> &amp; QwtAbstractScaleDraw::scaleMap () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Map how to translate between scale and pixel values</dl>
<h3><code>QwtScaleMap</code> &amp; QwtAbstractScaleDraw::scaleMap ()</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Map how to translate between scale and pixel values</dl>
<h3>void QwtAbstractScaleDraw::setMinimumExtent (doubleminExtent)</h3>
<p>Set a minimum for the extent. The extent is calculated from the components of the scale draw. In situations, where the labels are changing and the layout depends on the extent (f.e scrolling a scale), setting an upper limit as minimum extent will avoid jumps of the layout. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>minExtent</i> Minimum extent</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>extent()</code>, <code>minimumExtent()</code></dl>
<h3>void QwtAbstractScaleDraw::setPenWidth (intwidth)</h3>
<p>Specify the width of the scale pen. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>width</i> Pen width</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>penWidth()</code></dl>
<h3>void QwtAbstractScaleDraw::setScaleDiv (const <code>QwtScaleDiv</code> &amp;scaleDiv)</h3>
<p>Change the scale division </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>scaleDiv</i> New scale division</dl>
<h3>void QwtAbstractScaleDraw::setSpacing (doublespacing)</h3>
<p>Set the spacing between tick and labels. The spacing is the distance between ticks and labels. The default spacing is 4 pixels. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>spacing</i> Spacing</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>spacing()</code></dl>
<h3>void QwtAbstractScaleDraw::setTickLength (<code>QwtScaleDiv::TickType</code>tickType, doublelength)</h3>
<p>Set the length of the ticks </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>tickType</i> Tick type<br />
 <i>length</i> New length</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>the length is limited to [0..1000]</dl>
<h3>void QwtAbstractScaleDraw::setTransformation (<code>QwtTransform</code> *transformation)</h3>
<p>Change the transformation of the scale </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>transformation</i> New scale transformation</dl>
<h3>double QwtAbstractScaleDraw::spacing () const</h3>
<p>Get the spacing. The spacing is the distance between ticks and labels. The default spacing is 4 pixels. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Spacing</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setSpacing()</code></dl>
<h3>const <code>QwtText</code> &amp; QwtAbstractScaleDraw::tickLabel (const QFont &amp;font, doublevalue) const [protected]</h3>
<p>Convert a value into its representing label and cache it. The conversion between value and label is called very often in the layout and painting code. Unfortunately the calculation of the label sizes might be slow (really slow for rich text in Qt4), so it&#8217;s necessary to cache the labels. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>font</i> Font<br />
 <i>value</i> Value</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Tick label</dl>
<h3>double QwtAbstractScaleDraw::tickLength (<code>QwtScaleDiv::TickType</code>tickType) const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Length of the ticks</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setTickLength()</code>, <code>maxTickLength()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
