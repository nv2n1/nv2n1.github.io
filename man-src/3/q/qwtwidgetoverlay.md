---
title: "qwtwidgetoverlay(3)"
name: "qwtwidgetoverlay"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtwidgetoverlay/"
description: "QwtWidgetOverlay –"
---

<p>QwtWidgetOverlay &#8211; </p>
<p> An overlay for a widget.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_widget_overlay.h&gt; </p>
<p> Inherits QWidget. </p>
<p> Inherited by QwtPickerRubberband, and QwtPickerTracker.</p>
<h3>Public Types</h3>
<p>enum <code>MaskMode</code> { <code>NoMask</code>, <code>MaskHint</code>, <code>AlphaMask</code> }<br />
 <i>Mask mode. </i><br />
 enum <code>RenderMode</code> { <code>AutoRenderMode</code>, <code>CopyAlphaMask</code>, <code>DrawOverlay</code> }<br />
 <i>Render mode. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtWidgetOverlay</code> (QWidget *)<br />
 <i>Constructor. </i><br />
 virtual <code>~QwtWidgetOverlay</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setMaskMode</code> (<code>MaskMode</code>)<br />
 <i>Specify how to find the mask for the overlay. </i><br />
 <code>MaskMode</code> <code>maskMode</code> () const </p>
<p> void <code>setRenderMode</code> (<code>RenderMode</code>) </p>
<p> <code>RenderMode</code> <code>renderMode</code> () const </p>
<p> void <code>updateOverlay</code> () </p>
<p> virtual bool <code>eventFilter</code> (QObject *, QEvent *)<br />
 <i>Event filter. </i></p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>paintEvent</code> (QPaintEvent *event) </p>
<p> virtual void <code>resizeEvent</code> (QResizeEvent *event) </p>
<p> virtual QRegion <code>maskHint</code> () const<br />
 <i>Calculate an approximation for the mask. </i><br />
 virtual void <code>drawOverlay</code> (QPainter *painter) const =0 </p>
<h2>Detailed Description</h2>
<p>An overlay for a widget. </p>
<p> The main use case of an widget overlay is to avoid heavy repaint operation of the widget below. </p>
<p> F.e. in combination with the plot canvas an overlay avoid replots as the content of the canvas can be restored from its backing store. </p>
<p> <code>QwtWidgetOverlay</code> is an abstract base class. Deriving classes are supposed to reimplement the following methods: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd><code>drawOverlay()</code></p>
<dt>&bull;</p>
<dd><code>maskHint()</code></dl>
<p> Internally <code>QwtPlotPicker</code> uses overlays for displaying the rubber band and the tracker text. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtPlotCanvas::BackingStore</code></dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtWidgetOverlay::MaskMode</code></h3>
<p>Mask mode. When using masks the widget below gets paint events for the masked regions of the overlay only. Otherwise Qt triggers full repaints. On less powerful hardware ( f.e embedded systems ) &#8211; or when using the raster paint engine on a remote desktop &#8211; bit blitting is a noticeable operation, that needs to be avoided. </p>
<p> If and how to mask depends on how expensive the calculation of the mask is and how many pixels can be excluded by the mask. </p>
<p> The default setting is MaskHint. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setMaskMode()</code>, <code>maskMode()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>NoMask </i></p>
<dd>Don&#8217;t use a mask.</p>
<dt><i>MaskHint </i></p>
<dd>Use <code>maskHint()</code> as mask. For many situations a fast approximation is good enough and it is not necessary to build a more detailed mask ( f.e the bounding rectangle of a text ).</p>
<dt><i>AlphaMask </i></p>
<dd>Calculate a mask by checking the alpha values. Sometimes it is not possible to give a fast approximation and the mask needs to be calculated by drawing the overlay and testing the result.</dl>
<p> When a valid <code>maskHint()</code> is available only pixels inside this approximation are checked.</p>
<h3>enum <code>QwtWidgetOverlay::RenderMode</code></h3>
<p>Render mode. For calculating the alpha mask the overlay has already been painted to a temporary QImage. Instead of rendering the overlay twice this buffer can be copied for drawing the overlay. </p>
<p> On graphic systems using the raster paint engine ( QWS, Windows ) it means usually copying some memory only. On X11 it results in an expensive operation building a pixmap and for simple overlays it might not be recommended. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The render mode has no effect, when <code>maskMode()</code> != AlphaMask.</dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>AutoRenderMode </i></p>
<dd>Copy the buffer, when using the raster paint engine.</p>
<dt><i>CopyAlphaMask </i></p>
<dd>Always copy the buffer.</p>
<dt><i>DrawOverlay </i></p>
<dd>Never copy the buffer.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtWidgetOverlay::QwtWidgetOverlay (QWidget *widget)</h3>
<p>Constructor. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>widget</i> Parent widget, where the overlay is aligned to</dl>
<h2>Member Function Documentation</h2>
<h3>virtual void QwtWidgetOverlay::drawOverlay (QPainter *painter) const [protected], [pure virtual]</h3>
<p>Draw the widget overlay </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter</dl>
<h3>bool QwtWidgetOverlay::eventFilter (QObject *object, QEvent *event) [virtual]</h3>
<p>Event filter. Resize the overlay according to the size of the parent widget. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>object</i> Object to be filtered<br />
 <i>event</i> Event</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>See QObject::eventFilter()</dl>
<h3>QRegion QwtWidgetOverlay::maskHint () const [protected], [virtual]</h3>
<p>Calculate an approximation for the mask.</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>MaskHint The hint is used as mask.</p>
<dt>&bull;</p>
<dd>AlphaMask The hint is used to speed up the algorithm for calculating a mask from non transparent pixels</p>
<dt>&bull;</p>
<dd>NoMask The hint is unused.</dl>
<p> The default implementation returns an invalid region indicating no hint. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Hint for the mask</dl>
<h3><code>QwtWidgetOverlay::MaskMode</code> QwtWidgetOverlay::maskMode () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Mode how to find the mask for the overlay</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setMaskMode()</code></dl>
<h3>void QwtWidgetOverlay::paintEvent (QPaintEvent *event) [protected], [virtual]</h3>
<p>Paint event </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Paint event</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>drawOverlay()</code></dl>
<h3><code>QwtWidgetOverlay::RenderMode</code> QwtWidgetOverlay::renderMode () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Render mode</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>RenderMode</code>, <code>setRenderMode()</code></dl>
<h3>void QwtWidgetOverlay::resizeEvent (QResizeEvent *event) [protected], [virtual]</h3>
<p>Resize event </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Resize event</dl>
<h3>void QwtWidgetOverlay::setMaskMode (<code>MaskMode</code>mode)</h3>
<p>Specify how to find the mask for the overlay. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>mode</i> New mode</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>maskMode()</code></dl>
<h3>void QwtWidgetOverlay::setRenderMode (<code>RenderMode</code>mode)</h3>
<p>Set the render mode </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>mode</i> Render mode</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>RenderMode</code>, <code>renderMode()</code></dl>
<h3>void QwtWidgetOverlay::updateOverlay ()</h3>
<p>Recalculate the mask and repaint the overlay </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
