---
title: "qwtknob(3)"
name: "qwtknob"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtknob/"
description: "QwtKnob –"
---

<p>QwtKnob &#8211; </p>
<p> The Knob Widget.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_knob.h&gt; </p>
<p> Inherits <code>QwtAbstractSlider</code>.</p>
<h3>Public Types</h3>
<p>enum <code>KnobStyle</code> { <code>Flat</code>, <code>Raised</code>, <code>Sunken</code>, <code>Styled</code> }<br />
 <i>Style of the knob surface. </i><br />
 enum <code>MarkerStyle</code> { <code>NoMarker</code> = -1, <code>Tick</code>, <code>Triangle</code>, <code>Dot</code>, <code>Nub</code>, <code>Notch</code> }<br />
 <i>Marker type. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtKnob</code> (QWidget *parent=NULL)<br />
 <i>Constructor. </i><br />
 virtual <code>~QwtKnob</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setAlignment</code> (Qt::Alignment)<br />
 <i>Set the alignment of the knob. </i><br />
 Qt::Alignment <code>alignment</code> () const </p>
<p> void <code>setKnobWidth</code> (int)<br />
 <i>Change the knob&#8217;s width. </i><br />
 int <code>knobWidth</code> () const<br />
 <i>Return the width of the knob. </i><br />
 void <code>setNumTurns</code> (int)<br />
 <i>Set the number of turns. </i><br />
 int <code>numTurns</code> () const </p>
<p> void <code>setTotalAngle</code> (double angle)<br />
 <i>Set the total angle by which the knob can be turned. </i><br />
 double <code>totalAngle</code> () const </p>
<p> void <code>setKnobStyle</code> (<code>KnobStyle</code>)<br />
 <i>Set the knob type. </i><br />
 <code>KnobStyle</code> <code>knobStyle</code> () const </p>
<p> void <code>setBorderWidth</code> (int bw)<br />
 <i>Set the knob&#8217;s border width. </i><br />
 int <code>borderWidth</code> () const<br />
 <i>Return the border width. </i><br />
 void <code>setMarkerStyle</code> (<code>MarkerStyle</code>)<br />
 <i>Set the marker type of the knob. </i><br />
 <code>MarkerStyle</code> <code>markerStyle</code> () const </p>
<p> void <code>setMarkerSize</code> (int)<br />
 <i>Set the size of the marker. </i><br />
 int <code>markerSize</code> () const </p>
<p> virtual QSize <code>sizeHint</code> () const </p>
<p> virtual QSize <code>minimumSizeHint</code> () const </p>
<p> void <code>setScaleDraw</code> (<code>QwtRoundScaleDraw</code> *) </p>
<p> const <code>QwtRoundScaleDraw</code> * <code>scaleDraw</code> () const </p>
<p> <code>QwtRoundScaleDraw</code> * <code>scaleDraw</code> () </p>
<p> QRect <code>knobRect</code> () const </p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>paintEvent</code> (QPaintEvent *) </p>
<p> virtual void <code>changeEvent</code> (QEvent *) </p>
<p> virtual void <code>drawKnob</code> (QPainter *, const QRectF &amp;) const<br />
 <i>Draw the knob. </i><br />
 virtual void <code>drawFocusIndicator</code> (QPainter *) const </p>
<p> virtual void <code>drawMarker</code> (QPainter *, const QRectF &amp;, double arc) const<br />
 <i>Draw the marker at the knob&#8217;s front. </i><br />
 virtual double <code>scrolledTo</code> (const QPoint &amp;) const<br />
 <i>Determine the value for a new position of the mouse. </i><br />
 virtual bool <code>isScrollPosition</code> (const QPoint &amp;) const<br />
 <i>Determine what to do when the user presses a mouse button. </i></p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p>The Knob Widget. </p>
<p> The <code>QwtKnob</code> widget imitates look and behavior of a volume knob on a radio. It looks similar to QDial &#8211; not to <code>QwtDial</code>. </p>
<p> The value range of a knob might be divided into several turns. </p>
<p> The layout of the knob depends on the <code>knobWidth()</code>. </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>width &gt; 0 The diameter of the knob is fixed and the knob is aligned according to the <code>alignment()</code> flags inside of the contentsRect().</p>
<dt>&bull;</p>
<dd>width &lt;= 0 The knob is extended to the minimum of width/height of the contentsRect() and aligned in the other direction according to <code>alignment()</code>.</dl>
<p> Setting a fixed <code>knobWidth()</code> is helpful to align several knobs with different scale labels. </p>
<p>&nbsp;<wbr></p>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtKnob::KnobStyle</code></h3>
<p>Style of the knob surface. Depending on the KnobStyle the surface of the knob is filled from the brushes of the widget palette(). </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setKnobStyle()</code>, <code>knobStyle()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>Flat </i></p>
<dd>Fill the knob with a brush from QPalette::Button.</p>
<dt><i>Raised </i></p>
<dd>Build a gradient from QPalette::Midlight and QPalette::Button.</p>
<dt><i>Sunken </i></p>
<dd>Build a gradient from QPalette::Midlight, QPalette::Button and QPalette::Midlight</p>
<dt><i>Styled </i></p>
<dd>Build a radial gradient from QPalette::Button like it is used for QDial in various Qt styles.</dl>
<h3>enum <code>QwtKnob::MarkerStyle</code></h3>
<p>Marker type. The marker indicates the current value on the knob The default setting is a Notch marker. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setMarkerStyle()</code>, <code>setMarkerSize()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>NoMarker </i></p>
<dd>Don&#8217;t paint any marker.</p>
<dt><i>Tick </i></p>
<dd>Paint a single tick in QPalette::ButtonText color.</p>
<dt><i>Triangle </i></p>
<dd>Paint a triangle in QPalette::ButtonText color.</p>
<dt><i>Dot </i></p>
<dd>Paint a circle in QPalette::ButtonText color.</p>
<dt><i>Nub </i></p>
<dd>Draw a raised ellipse with a gradient build from QPalette::Light and QPalette::Mid</p>
<dt><i>Notch </i></p>
<dd>Draw a sunken ellipse with a gradient build from QPalette::Light and QPalette::Mid</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtKnob::QwtKnob (QWidget *parent = NULL) [explicit]</h3>
<p>Constructor. Construct a knob with an angle of 270°. The style is <code>QwtKnob::Raised</code> and the marker style is <code>QwtKnob::Notch</code>. The width of the knob is set to 50 pixels. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>parent</i> Parent widget</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setTotalAngle()</code></dl>
<h2>Member Function Documentation</h2>
<h3>Qt::Alignment QwtKnob::alignment () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Alignment of the knob inside of contentsRect()</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setAlignment()</code>, <code>knobWidth()</code>, <code>knobRect()</code></dl>
<h3>void QwtKnob::changeEvent (QEvent *event) [protected], [virtual]</h3>
<p>Handle QEvent::StyleChange and QEvent::FontChange; </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Change event</dl>
<h3>void QwtKnob::drawFocusIndicator (QPainter *painter) const [protected], [virtual]</h3>
<p>Draw the focus indicator </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter</dl>
<h3>void QwtKnob::drawKnob (QPainter *painter, const QRectF &amp;knobRect) const [protected], [virtual]</h3>
<p>Draw the knob. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> painter<br />
 <i>knobRect</i> Bounding rectangle of the knob (without scale)</dl>
<h3>void QwtKnob::drawMarker (QPainter *painter, const QRectF &amp;rect, doubleangle) const [protected], [virtual]</h3>
<p>Draw the marker at the knob&#8217;s front. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>rect</i> Bounding rectangle of the knob without scale<br />
 <i>angle</i> Angle of the marker in degrees ( clockwise, 0 at the 12 o&#8217;clock position )</dl>
<h3>bool QwtKnob::isScrollPosition (const QPoint &amp;pos) const [protected], [virtual]</h3>
<p>Determine what to do when the user presses a mouse button. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pos</i> Mouse position</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>True,when</i> pos is inside the circle of the knob.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>scrolledTo()</code></dl>
<p> Implements <code>QwtAbstractSlider</code>.</p>
<h3>QRect QwtKnob::knobRect () const</h3>
<p>Calculate the bounding rectangle of the knob without the scale </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Bounding rectangle of the knob</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>knobWidth()</code>, <code>alignment()</code>, QWidget::contentsRect()</dl>
<h3><code>QwtKnob::KnobStyle</code> QwtKnob::knobStyle () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Marker type of the knob</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setKnobStyle()</code>, <code>setBorderWidth()</code></dl>
<h3>int QwtKnob::markerSize () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Marker size</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setMarkerSize()</code></dl>
<h3><code>QwtKnob::MarkerStyle</code> QwtKnob::markerStyle () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Marker type of the knob</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setMarkerStyle()</code>, <code>setMarkerSize()</code></dl>
<h3>QSize QwtKnob::minimumSizeHint () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Minimum size hint</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>sizeHint()</code></dl>
<h3>int QwtKnob::numTurns () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Number of turns.</dl>
<p> When the total angle is below 360° <code>numTurns()</code> is ceiled to 1. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setNumTurns()</code>, <code>setTotalAngle()</code>, <code>totalAngle()</code></dl>
<h3>void QwtKnob::paintEvent (QPaintEvent *event) [protected], [virtual]</h3>
<p>Repaint the knob </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Paint event</dl>
<h3>const <code>QwtRoundScaleDraw</code> * QwtKnob::scaleDraw () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the scale draw of the knob</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setScaleDraw()</code></dl>
<h3><code>QwtRoundScaleDraw</code> * QwtKnob::scaleDraw ()</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the scale draw of the knob</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setScaleDraw()</code></dl>
<h3>double QwtKnob::scrolledTo (const QPoint &amp;pos) const [protected], [virtual]</h3>
<p>Determine the value for a new position of the mouse. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pos</i> Mouse position</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Value for the mouse position</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isScrollPosition()</code></dl>
<p> Implements <code>QwtAbstractSlider</code>.</p>
<h3>void QwtKnob::setAlignment (Qt::Alignmentalignment)</h3>
<p>Set the alignment of the knob. Similar to a QLabel::alignment() the flags decide how to align the knob inside of contentsRect(). </p>
<p> The default setting is Qt::AlignCenter </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>alignment</i> Or&#8217;d alignment flags</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>alignment()</code>, <code>setKnobWidth()</code>, <code>knobRect()</code></dl>
<h3>void QwtKnob::setBorderWidth (intborderWidth)</h3>
<p>Set the knob&#8217;s border width. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>borderWidth</i> new border width</dl>
<h3>void QwtKnob::setKnobStyle (<code>KnobStyle</code>knobStyle)</h3>
<p>Set the knob type. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>knobStyle</i> Knob type</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>knobStyle()</code>, <code>setBorderWidth()</code></dl>
<h3>void QwtKnob::setKnobWidth (intwidth)</h3>
<p>Change the knob&#8217;s width. Setting a fixed value for the diameter of the knob is helpful for aligning several knobs in a row. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>width</i> New width</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>knobWidth()</code>, <code>setAlignment()</code></dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Modifies the sizePolicy()</dl>
<h3>void QwtKnob::setMarkerSize (intsize)</h3>
<p>Set the size of the marker. When setting a size &lt;= 0 the marker will automatically scaled to 40% of the radius of the knob. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>markerSize()</code>, <code>markerStyle()</code></dl>
<h3>void QwtKnob::setMarkerStyle (<code>MarkerStyle</code>markerStyle)</h3>
<p>Set the marker type of the knob. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>markerStyle</i> Marker type</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>markerStyle()</code>, <code>setMarkerSize()</code></dl>
<h3>void QwtKnob::setNumTurns (intnumTurns)</h3>
<p>Set the number of turns. When numTurns &gt; 1 the knob can be turned several times around its axis</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>otherwise the total angle is floored to 360°.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>numTurns()</code>, <code>totalAngle()</code>, <code>setTotalAngle()</code></dl>
<h3>void QwtKnob::setScaleDraw (<code>QwtRoundScaleDraw</code> *scaleDraw)</h3>
<p>Change the scale draw of the knob </p>
<p> For changing the labels of the scales, it is necessary to derive from <code>QwtRoundScaleDraw</code> and overload <code>QwtRoundScaleDraw::label()</code>. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>scaleDraw()</code></dl>
<h3>void QwtKnob::setTotalAngle (doubleangle)</h3>
<p>Set the total angle by which the knob can be turned. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>angle</i> Angle in degrees.</dl>
<p> The angle has to be between [10, 360] degrees. Angles above 360 ( so that the knob can be turned several times around its axis ) have to be set using <code>setNumTurns()</code>. </p>
<p> The default angle is 270 degrees. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>totalAngle()</code>, <code>setNumTurns()</code></dl>
<h3>QSize QwtKnob::sizeHint () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd><code>sizeHint()</code></dl>
<h3>double QwtKnob::totalAngle () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the total angle</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setTotalAngle()</code>, <code>setNumTurns()</code>, <code>numTurns()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
