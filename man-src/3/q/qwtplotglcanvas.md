---
title: "qwtplotglcanvas(3)"
name: "qwtplotglcanvas"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtplotglcanvas/"
description: "QwtPlotGLCanvas –"
---

<p>QwtPlotGLCanvas &#8211; </p>
<p> An alternative canvas for a <code>QwtPlot</code> derived from QGLWidget.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_plot_glcanvas.h&gt; </p>
<p> Inherits QGLWidget.</p>
<h3>Public Types</h3>
<p>enum <code>Shadow</code> { <code>Plain</code> = QFrame::Plain, <code>Raised</code> = QFrame::Raised, <code>Sunken</code> = QFrame::Sunken }<br />
 <i>Frame shadow. </i><br />
 enum <code>Shape</code> { <code>NoFrame</code> = QFrame::NoFrame, <code>Box</code> = QFrame::Box, <code>Panel</code> = QFrame::Panel }<br />
 <i>Frame shape. </i></p>
<h3>Public Slots</h3>
<p>void <code>replot</code> ()<br />
 <i>Calls repaint() </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtPlotGLCanvas</code> (<code>QwtPlot</code> *=NULL)<br />
 <i>Constructor. </i><br />
 virtual <code>~QwtPlotGLCanvas</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setFrameStyle</code> (int style) </p>
<p> int <code>frameStyle</code> () const </p>
<p> void <code>setFrameShadow</code> (<code>Shadow</code>) </p>
<p> <code>Shadow</code> <code>frameShadow</code> () const </p>
<p> void <code>setFrameShape</code> (<code>Shape</code>) </p>
<p> <code>Shape</code> <code>frameShape</code> () const </p>
<p> void <code>setLineWidth</code> (int) </p>
<p> int <code>lineWidth</code> () const </p>
<p> void <code>setMidLineWidth</code> (int) </p>
<p> int <code>midLineWidth</code> () const </p>
<p> int <code>frameWidth</code> () const </p>
<p> QRect <code>frameRect</code> () const </p>
<p> Q_INVOKABLE QPainterPath <code>borderPath</code> (const QRect &amp;) const </p>
<p> virtual bool <code>event</code> (QEvent *) </p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>paintEvent</code> (QPaintEvent *) </p>
<p> virtual void <code>drawBackground</code> (QPainter *) </p>
<p> virtual void <code>drawBorder</code> (QPainter *) </p>
<p> virtual void <code>drawItems</code> (QPainter *) </p>
<h2>Detailed Description</h2>
<p>An alternative canvas for a <code>QwtPlot</code> derived from QGLWidget. </p>
<p> <code>QwtPlotGLCanvas</code> implements the very basics to act as canvas inside of a <code>QwtPlot</code> widget. It might be extended to a full featured alternative to <code>QwtPlotCanvas</code> in a future version of Qwt. </p>
<p> Even if <code>QwtPlotGLCanvas</code> is not derived from QFrame it imitates its API. When using style sheets it supports the box model &#8211; beside backgrounds with rounded borders. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlot::setCanvas()</code>, <code>QwtPlotCanvas</code></dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>You might want to use the QPaintEngine::OpenGL paint engine ( see QGL::setPreferredPaintEngine() ). On a Linux test system QPaintEngine::OpenGL2 shows very basic problems ( wrong geometries of rectangles ) but also more advanced stuff like antialiasing doesn&#8217;t work. </p>
<p> Another way to introduce OpenGL rendering to Qwt is to use QGLPixelBuffer or QGLFramebufferObject. Both type of buffers can be converted into a QImage and used in combination with a regular <code>QwtPlotCanvas</code>.</dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtPlotGLCanvas::Shadow</code></h3>
<p>Frame shadow. Unfortunately it is not possible to use QFrame::Shadow as a property of a widget that is not derived from QFrame. The following enum is made for the designer only. It is safe to use QFrame::Shadow instead. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>Plain </i></p>
<dd>QFrame::Plain.</p>
<dt><i>Raised </i></p>
<dd>QFrame::Raised.</p>
<dt><i>Sunken </i></p>
<dd>QFrame::Sunken.</dl>
<h3>enum <code>QwtPlotGLCanvas::Shape</code></h3>
<p>Frame shape. Unfortunately it is not possible to use QFrame::Shape as a property of a widget that is not derived from QFrame. The following enum is made for the designer only. It is safe to use QFrame::Shadow instead. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>QFrame::StyledPanel and QFrame::WinPanel are unsuported and will be displayed as QFrame::Panel.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPlotGLCanvas::QwtPlotGLCanvas (<code>QwtPlot</code> *plot = NULL) [explicit]</h3>
<p>Constructor. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>plot</i> Parent plot widget</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlot::setCanvas()</code></dl>
<h2>Member Function Documentation</h2>
<h3>QPainterPath QwtPlotGLCanvas::borderPath (const QRect &amp;rect) const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Empty path</dl>
<h3>void QwtPlotGLCanvas::drawBackground (QPainter *painter) [protected], [virtual]</h3>
<p>Draw the background of the canvas </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter</dl>
<h3>void QwtPlotGLCanvas::drawBorder (QPainter *painter) [protected], [virtual]</h3>
<p>Draw the border of the canvas </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter</dl>
<h3>void QwtPlotGLCanvas::drawItems (QPainter *painter) [protected], [virtual]</h3>
<p>Draw the plot items </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlot::drawCanvas()</code></dl>
<h3>bool QwtPlotGLCanvas::event (QEvent *event) [virtual]</h3>
<p>Qt event handler for QEvent::PolishRequest and QEvent::StyleChange </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Qt Event</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>See QGLWidget::event()</dl>
<h3>QRect QwtPlotGLCanvas::frameRect () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>The rectangle where the frame is drawn in.</dl>
<h3><code>QwtPlotGLCanvas::Shadow</code> QwtPlotGLCanvas::frameShadow () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Frame shadow</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setFrameShadow()</code>, QFrame::setFrameShadow()</dl>
<h3><code>QwtPlotGLCanvas::Shape</code> QwtPlotGLCanvas::frameShape () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Frame shape</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setFrameShape()</code>, QFrame::frameShape()</dl>
<h3>int QwtPlotGLCanvas::frameStyle () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>The bitwise OR between a <code>frameShape()</code> and a <code>frameShadow()</code></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setFrameStyle()</code>, QFrame::frameStyle()</dl>
<h3>int QwtPlotGLCanvas::frameWidth () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Frame width depending on the style, line width and midline width.</dl>
<h3>int QwtPlotGLCanvas::lineWidth () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Line width of the frame</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLineWidth()</code>, <code>midLineWidth()</code></dl>
<h3>int QwtPlotGLCanvas::midLineWidth () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Midline width of the frame</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setMidLineWidth()</code>, <code>lineWidth()</code></dl>
<h3>void QwtPlotGLCanvas::paintEvent (QPaintEvent *event) [protected], [virtual]</h3>
<p>Paint event </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Paint event</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlot::drawCanvas()</code></dl>
<h3>void QwtPlotGLCanvas::setFrameShadow (<code>Shadow</code>shadow)</h3>
<p>Set the frame shadow </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>shadow</i> Frame shadow</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>frameShadow()</code>, <code>setFrameShape()</code>, QFrame::setFrameShadow()</dl>
<h3>void QwtPlotGLCanvas::setFrameShape (<code>Shape</code>shape)</h3>
<p>Set the frame shape </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>shape</i> Frame shape</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>frameShape()</code>, <code>setFrameShadow()</code>, QFrame::frameShape()</dl>
<h3>void QwtPlotGLCanvas::setFrameStyle (intstyle)</h3>
<p>Set the frame style </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>style</i> The bitwise OR between a shape and a shadow.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>frameStyle()</code>, QFrame::setFrameStyle(), <code>setFrameShadow()</code>, <code>setFrameShape()</code></dl>
<h3>void QwtPlotGLCanvas::setLineWidth (intwidth)</h3>
<p>Set the frame line width </p>
<p> The default line width is 2 pixels. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>width</i> Line width of the frame</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>lineWidth()</code>, <code>setMidLineWidth()</code></dl>
<h3>void QwtPlotGLCanvas::setMidLineWidth (intwidth)</h3>
<p>Set the frame mid line width </p>
<p> The default midline width is 0 pixels. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>width</i> Midline width of the frame</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>midLineWidth()</code>, <code>setLineWidth()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
