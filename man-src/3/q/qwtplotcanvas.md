---
title: "qwtplotcanvas(3)"
name: "qwtplotcanvas"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtplotcanvas/"
description: "QwtPlotCanvas –"
---

<p>QwtPlotCanvas &#8211; </p>
<p> Canvas of a <code>QwtPlot</code>.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_plot_canvas.h&gt; </p>
<p> Inherits QFrame.</p>
<h3>Public Types</h3>
<p>enum <code>PaintAttribute</code> { <code>BackingStore</code> = 1, <code>Opaque</code> = 2, <code>HackStyledBackground</code> = 4, <code>ImmediatePaint</code> = 8 }<br />
 <i>Paint attributes. </i><br />
 enum <code>FocusIndicator</code> { <code>NoFocusIndicator</code>, <code>CanvasFocusIndicator</code>, <code>ItemFocusIndicator</code> }<br />
 <i>Focus indicator The default setting is NoFocusIndicator. </i><br />
 typedef QFlags&lt; <code>PaintAttribute</code> &gt; <code>PaintAttributes</code><br />
 <i>Paint attributes. </i></p>
<h3>Public Slots</h3>
<p>void <code>replot</code> () </p>
<h3>Public Member Functions</h3>
<p><code>QwtPlotCanvas</code> (<code>QwtPlot</code> *=NULL)<br />
 <i>Constructor. </i><br />
 virtual <code>~QwtPlotCanvas</code> ()<br />
 <i>Destructor. </i><br />
 <code>QwtPlot</code> * <code>plot</code> ()<br />
 <i>Return parent plot widget. </i><br />
 const <code>QwtPlot</code> * <code>plot</code> () const<br />
 <i>Return parent plot widget. </i><br />
 void <code>setFocusIndicator</code> (<code>FocusIndicator</code>) </p>
<p> <code>FocusIndicator</code> <code>focusIndicator</code> () const </p>
<p> void <code>setBorderRadius</code> (double) </p>
<p> double <code>borderRadius</code> () const </p>
<p> void <code>setPaintAttribute</code> (<code>PaintAttribute</code>, bool on=true)<br />
 <i>Changing the paint attributes. </i><br />
 bool <code>testPaintAttribute</code> (<code>PaintAttribute</code>) const </p>
<p> const QPixmap * <code>backingStore</code> () const </p>
<p> void <code>invalidateBackingStore</code> ()<br />
 <i>Invalidate the internal backing store. </i><br />
 virtual bool <code>event</code> (QEvent *) </p>
<p> Q_INVOKABLE QPainterPath <code>borderPath</code> (const QRect &amp;) const </p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>paintEvent</code> (QPaintEvent *) </p>
<p> virtual void <code>resizeEvent</code> (QResizeEvent *) </p>
<p> virtual void <code>drawFocusIndicator</code> (QPainter *) </p>
<p> virtual void <code>drawBorder</code> (QPainter *) </p>
<p> void <code>updateStyleSheetInfo</code> ()<br />
 <i>Update the cached information about the current style sheet. </i></p>
<h2>Detailed Description</h2>
<p>Canvas of a <code>QwtPlot</code>. </p>
<p> Canvas is the widget where all plot items are displayed </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlot::setCanvas()</code>, <code>QwtPlotGLCanvas</code></dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtPlotCanvas::FocusIndicator</code></h3>
<p>Focus indicator The default setting is NoFocusIndicator. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setFocusIndicator()</code>, <code>focusIndicator()</code>, paintFocus()</dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>NoFocusIndicator </i></p>
<dd>Don&#8217;t paint a focus indicator.</p>
<dt><i>CanvasFocusIndicator </i></p>
<dd>The focus is related to the complete canvas. Paint the focus indicator using paintFocus()</p>
<dt><i>ItemFocusIndicator </i></p>
<dd>The focus is related to an item (curve, point, &#8230;) on the canvas. It is up to the application to display a focus indication using f.e. highlighting.</dl>
<h3>enum <code>QwtPlotCanvas::PaintAttribute</code></h3>
<p>Paint attributes. The default setting enables BackingStore and Opaque. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPaintAttribute()</code>, <code>testPaintAttribute()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>BackingStore </i></p>
<dd>Paint double buffered reusing the content of the pixmap buffer when possible. Using a backing store might improve the performance significantly, when working with widget overlays ( like rubber bands ). Disabling the cache might improve the performance for incremental paints (using <code>QwtPlotDirectPainter</code> ).</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>backingStore()</code>, <code>invalidateBackingStore()</code></dl>
<dl COMPACT>
<dt><i>Opaque </i></p>
<dd>Try to fill the complete contents rectangle of the plot canvas. When using styled backgrounds Qt assumes, that the canvas doesn&#8217;t fill its area completely ( f.e because of rounded borders ) and fills the area below the canvas. When this is done with gradients it might result in a serious performance bottleneck &#8211; depending on the size.</dl>
<p> When the Opaque attribute is enabled the canvas tries to identify the gaps with some heuristics and to fill those only. </p>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>Will not work for semitransparent backgrounds</dl>
<dl COMPACT>
<dt><i>HackStyledBackground </i></p>
<dd>Try to improve painting of styled backgrounds. <code>QwtPlotCanvas</code> supports the box model attributes for customizing the layout with style sheets. Unfortunately the design of Qt style sheets has no concept how to handle backgrounds with rounded corners &#8211; beside of padding.</dl>
<p> When HackStyledBackground is enabled the plot canvas tries to separate the background from the background border by reverse engineering to paint the background before and the border after the plot items. In this order the border gets perfectly antialiased and you can avoid some pixel artifacts in the corners.</p>
<dl COMPACT>
<dt><i>ImmediatePaint </i></p>
<dd>When ImmediatePaint is set <code>replot()</code> calls repaint() instead of update().</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>replot()</code>, QWidget::repaint(), QWidget::update()</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPlotCanvas::QwtPlotCanvas (<code>QwtPlot</code> *plot = NULL) [explicit]</h3>
<p>Constructor. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>plot</i> Parent plot widget</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlot::setCanvas()</code></dl>
<h2>Member Function Documentation</h2>
<h3>const QPixmap * QwtPlotCanvas::backingStore () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Backing store, might be null</dl>
<h3>QPainterPath QwtPlotCanvas::borderPath (const QRect &amp;rect) const</h3>
<p>Calculate the painter path for a styled or rounded border </p>
<p> When the canvas has no styled background or rounded borders the painter path is empty. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rect</i> Bounding rectangle of the canvas</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Painter path, that can be used for clipping</dl>
<h3>double QwtPlotCanvas::borderRadius () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Radius for the corners of the border frame</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBorderRadius()</code></dl>
<h3>void QwtPlotCanvas::drawBorder (QPainter *painter) [protected], [virtual]</h3>
<p>Draw the border of the plot canvas </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBorderRadius()</code></dl>
<h3>void QwtPlotCanvas::drawFocusIndicator (QPainter *painter) [protected], [virtual]</h3>
<p>Draw the focus indication </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter</dl>
<h3>bool QwtPlotCanvas::event (QEvent *event) [virtual]</h3>
<p>Qt event handler for QEvent::PolishRequest and QEvent::StyleChange </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Qt Event</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>See QFrame::event()</dl>
<h3><code>QwtPlotCanvas::FocusIndicator</code> QwtPlotCanvas::focusIndicator () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Focus indicator</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>FocusIndicator</code>, <code>setFocusIndicator()</code></dl>
<h3>void QwtPlotCanvas::paintEvent (QPaintEvent *event) [protected], [virtual]</h3>
<p>Paint event </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Paint event</dl>
<h3>void QwtPlotCanvas::replot () [slot]</h3>
<p>Invalidate the paint cache and repaint the canvas </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>invalidatePaintCache()</dl>
<h3>void QwtPlotCanvas::resizeEvent (QResizeEvent *event) [protected], [virtual]</h3>
<p>Resize event </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Resize event</dl>
<h3>void QwtPlotCanvas::setBorderRadius (doubleradius)</h3>
<p>Set the radius for the corners of the border frame </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>radius</i> Radius of a rounded corner</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>borderRadius()</code></dl>
<h3>void QwtPlotCanvas::setFocusIndicator (<code>FocusIndicator</code>focusIndicator)</h3>
<p>Set the focus indicator </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>FocusIndicator</code>, <code>focusIndicator()</code></dl>
<h3>void QwtPlotCanvas::setPaintAttribute (<code>PaintAttribute</code>attribute, boolon = true)</h3>
<p>Changing the paint attributes. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>attribute</i> Paint attribute<br />
 <i>on</i> On/Off</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>testPaintAttribute()</code>, <code>backingStore()</code></dl>
<h3>bool QwtPlotCanvas::testPaintAttribute (<code>PaintAttribute</code>attribute) const</h3>
<p>Test whether a paint attribute is enabled </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>attribute</i> Paint attribute</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true, when attribute is enabled</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPaintAttribute()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
