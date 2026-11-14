---
title: "qwtthermo(3)"
name: "qwtthermo"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtthermo/"
description: "QwtThermo –"
---

<p>QwtThermo &#8211; </p>
<p> The Thermometer Widget.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_thermo.h&gt; </p>
<p> Inherits <code>QwtAbstractScale</code>.</p>
<h3>Public Types</h3>
<p>enum <code>ScalePosition</code> { <code>NoScale</code>, <code>LeadingScale</code>, <code>TrailingScale</code> } </p>
<p> enum <code>OriginMode</code> { <code>OriginMinimum</code>, <code>OriginMaximum</code>, <code>OriginCustom</code> } </p>
<h3>Public Slots</h3>
<p>virtual void <code>setValue</code> (double val) </p>
<h3>Public Member Functions</h3>
<p><code>QwtThermo</code> (QWidget *parent=NULL) </p>
<p> virtual <code>~QwtThermo</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setOrientation</code> (Qt::Orientation)<br />
 <i>Set the orientation. </i><br />
 Qt::Orientation <code>orientation</code> () const </p>
<p> void <code>setScalePosition</code> (<code>ScalePosition</code>)<br />
 <i>Change the position of the scale. </i><br />
 <code>ScalePosition</code> <code>scalePosition</code> () const </p>
<p> void <code>setSpacing</code> (int)<br />
 <i>Change the spacing between pipe and scale. </i><br />
 int <code>spacing</code> () const </p>
<p> void <code>setBorderWidth</code> (int w) </p>
<p> int <code>borderWidth</code> () const </p>
<p> void <code>setOriginMode</code> (<code>OriginMode</code>)<br />
 <i>Change how the origin is determined. </i><br />
 <code>OriginMode</code> <code>originMode</code> () const </p>
<p> void <code>setOrigin</code> (double)<br />
 <i>Specifies the custom origin. </i><br />
 double <code>origin</code> () const </p>
<p> void <code>setFillBrush</code> (const QBrush &amp;b)<br />
 <i>Change the brush of the liquid. </i><br />
 QBrush <code>fillBrush</code> () const </p>
<p> void <code>setAlarmBrush</code> (const QBrush &amp;b)<br />
 <i>Specify the liquid brush above the alarm threshold. </i><br />
 QBrush <code>alarmBrush</code> () const </p>
<p> void <code>setAlarmLevel</code> (double v) </p>
<p> double <code>alarmLevel</code> () const </p>
<p> void <code>setAlarmEnabled</code> (bool tf)<br />
 <i>Enable or disable the alarm threshold. </i><br />
 bool <code>alarmEnabled</code> () const </p>
<p> void <code>setColorMap</code> (<code>QwtColorMap</code> *)<br />
 <i>Assign a color map for the fill color. </i><br />
 <code>QwtColorMap</code> * <code>colorMap</code> () </p>
<p> const <code>QwtColorMap</code> * <code>colorMap</code> () const </p>
<p> void <code>setPipeWidth</code> (int w) </p>
<p> int <code>pipeWidth</code> () const </p>
<p> void <code>setRangeFlags</code> (<code>QwtInterval::BorderFlags</code>)<br />
 <i>Exclude/Include min/max values. </i><br />
 <code>QwtInterval::BorderFlags</code> <code>rangeFlags</code> () const </p>
<p> double <code>value</code> () const<br />
 <i>Return the value. </i><br />
 virtual QSize <code>sizeHint</code> () const </p>
<p> virtual QSize <code>minimumSizeHint</code> () const </p>
<p> void <code>setScaleDraw</code> (<code>QwtScaleDraw</code> *)<br />
 <i>Set a scale draw. </i><br />
 const <code>QwtScaleDraw</code> * <code>scaleDraw</code> () const </p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>drawLiquid</code> (QPainter *, const QRect &amp;) const </p>
<p> virtual void <code>scaleChange</code> ()<br />
 <i>Notify a scale change. </i><br />
 virtual void <code>paintEvent</code> (QPaintEvent *) </p>
<p> virtual void <code>resizeEvent</code> (QResizeEvent *) </p>
<p> virtual void <code>changeEvent</code> (QEvent *) </p>
<p> <code>QwtScaleDraw</code> * <code>scaleDraw</code> () </p>
<p> QRect <code>pipeRect</code> () const </p>
<p> QRect <code>fillRect</code> (const QRect &amp;) const<br />
 <i>Calculate the filled rectangle of the pipe. </i><br />
 QRect <code>alarmRect</code> (const QRect &amp;) const<br />
 <i>Calculate the alarm rectangle of the pipe. </i></p>
<h2>Detailed Description</h2>
<p>The Thermometer Widget. </p>
<p> <code>QwtThermo</code> is a widget which displays a value in an interval. It supports:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>a horizontal or vertical layout;</p>
<dt>&bull;</p>
<dd>a range;</p>
<dt>&bull;</p>
<dd>a scale;</p>
<dt>&bull;</p>
<dd>an alarm level.</dl>
<p> The fill colors might be calculated from an optional color map If no color map has been assigned <code>QwtThermo</code> uses the following colors/brushes from the widget palette: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>QPalette::Base Background of the pipe</p>
<dt>&bull;</p>
<dd>QPalette::ButtonText Fill brush below the alarm level</p>
<dt>&bull;</p>
<dd>QPalette::Highlight Fill brush for the values above the alarm level</p>
<dt>&bull;</p>
<dd>QPalette::WindowText For the axis of the scale</p>
<dt>&bull;</p>
<dd>QPalette::Text For the labels of the scale</dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtThermo::OriginMode</code></h3>
<p>Origin mode. This property specifies where the beginning of the liquid is placed. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setOriginMode()</code>, <code>setOrigin()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>OriginMinimum </i></p>
<dd>The origin is the minimum of the scale.</p>
<dt><i>OriginMaximum </i></p>
<dd>The origin is the maximum of the scale.</p>
<dt><i>OriginCustom </i></p>
<dd>The origin is specified using the <code>origin()</code> property.</dl>
<h3>enum <code>QwtThermo::ScalePosition</code></h3>
<p>Position of the scale </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setScalePosition()</code>, <code>setOrientation()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>NoScale </i></p>
<dd>The slider has no scale.</p>
<dt><i>LeadingScale </i></p>
<dd>The scale is right of a vertical or below of a horizontal slider.</p>
<dt><i>TrailingScale </i></p>
<dd>The scale is left of a vertical or above of a horizontal slider.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtThermo::QwtThermo (QWidget *parent = NULL) [explicit]</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>parent</i> Parent widget</dl>
<h2>Member Function Documentation</h2>
<h3>QBrush QwtThermo::alarmBrush () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Liquid brush ( QPalette::Highlight ) above the alarm threshold.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setAlarmBrush()</code>, QWidget::palette()</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The alarm threshold has no effect, when a color map has been assigned</dl>
<h3>bool QwtThermo::alarmEnabled () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, when the alarm threshold is enabled.</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The alarm threshold has no effect, when a color map has been assigned</dl>
<h3>double QwtThermo::alarmLevel () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Alarm threshold.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setAlarmLevel()</code></dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The alarm threshold has no effect, when a color map has been assigned</dl>
<h3>QRect QwtThermo::alarmRect (const QRect &amp;fillRect) const [protected]</h3>
<p>Calculate the alarm rectangle of the pipe. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>fillRect</i> Filled rectangle in the pipe</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Rectangle to be filled with the alarm brush</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>pipeRect()</code>, <code>fillRect()</code>, <code>alarmLevel()</code>, <code>alarmBrush()</code></dl>
<h3>int QwtThermo::borderWidth () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Border width of the thermometer pipe.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBorderWidth()</code></dl>
<h3>void QwtThermo::changeEvent (QEvent *event) [protected], [virtual]</h3>
<p>Qt change event handler </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Event</dl>
<h3><code>QwtColorMap</code> * QwtThermo::colorMap ()</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Color map for the fill color</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The alarm threshold has no effect, when a color map has been assigned</dl>
<h3>const <code>QwtColorMap</code> * QwtThermo::colorMap () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Color map for the fill color</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The alarm threshold has no effect, when a color map has been assigned</dl>
<h3>void QwtThermo::drawLiquid (QPainter *painter, const QRect &amp;pipeRect) const [protected], [virtual]</h3>
<p>Redraw the liquid in thermometer pipe. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>pipeRect</i> Bounding rectangle of the pipe without borders</dl>
<h3>QBrush QwtThermo::fillBrush () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Liquid ( QPalette::ButtonText ) brush.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setFillBrush()</code>, QWidget::palette()</dl>
<h3>QRect QwtThermo::fillRect (const QRect &amp;pipeRect) const [protected]</h3>
<p>Calculate the filled rectangle of the pipe. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>pipeRect</i> Rectangle of the pipe</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Rectangle to be filled ( fill and alarm brush )</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>pipeRect()</code>, <code>alarmRect()</code></dl>
<h3>QSize QwtThermo::minimumSizeHint () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Minimum size hint</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The return value depends on the font and the scale.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>sizeHint()</code></dl>
<h3>Qt::Orientation QwtThermo::orientation () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Orientation</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setOrientation()</code></dl>
<h3>double QwtThermo::origin () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Origin of the thermo, when OriginCustom is enabled</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setOrigin()</code>, <code>setOriginMode()</code>, <code>originMode()</code></dl>
<h3><code>QwtThermo::OriginMode</code> QwtThermo::originMode () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Mode, how the origin is determined.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setOriginMode()</code>, serOrigin(), <code>origin()</code></dl>
<h3>void QwtThermo::paintEvent (QPaintEvent *event) [protected], [virtual]</h3>
<p>Paint event handler </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Paint event</dl>
<h3>QRect QwtThermo::pipeRect () const [protected]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Bounding rectangle of the pipe ( without borders ) in widget coordinates</dl>
<h3>int QwtThermo::pipeWidth () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Width of the pipe.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setPipeWidth()</code></dl>
<h3><code>QwtInterval::BorderFlags</code> QwtThermo::rangeFlags () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Range flags</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setRangeFlags()</code></dl>
<h3>void QwtThermo::resizeEvent (QResizeEvent *event) [protected], [virtual]</h3>
<p>Resize event handler </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Resize event</dl>
<h3>const <code>QwtScaleDraw</code> * QwtThermo::scaleDraw () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the scale draw of the thermo</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setScaleDraw()</code></dl>
<h3><code>QwtScaleDraw</code> * QwtThermo::scaleDraw () [protected]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the scale draw of the thermo</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setScaleDraw()</code></dl>
<h3><code>QwtThermo::ScalePosition</code> QwtThermo::scalePosition () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Scale position.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setScalePosition()</code></dl>
<h3>void QwtThermo::setAlarmBrush (const QBrush &amp;brush)</h3>
<p>Specify the liquid brush above the alarm threshold. Changes the QPalette::Highlight brush of the palette. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>brush</i> New brush.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>alarmBrush()</code>, QWidget::setPalette()</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The alarm threshold has no effect, when a color map has been assigned</dl>
<h3>void QwtThermo::setAlarmEnabled (boolon)</h3>
<p>Enable or disable the alarm threshold. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>on</i> true (disabled) or false (enabled)</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The alarm threshold has no effect, when a color map has been assigned</dl>
<h3>void QwtThermo::setAlarmLevel (doublelevel)</h3>
<p>Specify the alarm threshold. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>level</i> Alarm threshold</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>alarmLevel()</code></dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The alarm threshold has no effect, when a color map has been assigned</dl>
<h3>void QwtThermo::setBorderWidth (intwidth)</h3>
<p>Set the border width of the pipe. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>width</i> Border width</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>borderWidth()</code></dl>
<h3>void QwtThermo::setColorMap (<code>QwtColorMap</code> *colorMap)</h3>
<p>Assign a color map for the fill color. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>colorMap</i> Color map</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The alarm threshold has no effect, when a color map has been assigned</dl>
<h3>void QwtThermo::setFillBrush (const QBrush &amp;brush)</h3>
<p>Change the brush of the liquid. Changes the QPalette::ButtonText brush of the palette. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>brush</i> New brush.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>fillBrush()</code>, QWidget::setPalette()</dl>
<h3>void QwtThermo::setOrientation (Qt::Orientationorientation)</h3>
<p>Set the orientation. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>orientation</i> Allowed values are Qt::Horizontal and Qt::Vertical.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>orientation()</code>, <code>scalePosition()</code></dl>
<h3>void QwtThermo::setOrigin (doubleorigin)</h3>
<p>Specifies the custom origin. If originMode is set to OriginCustom this property controls where the liquid starts. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>origin</i> New origin level</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setOriginMode()</code>, <code>originMode()</code>, <code>origin()</code></dl>
<h3>void QwtThermo::setOriginMode (<code>OriginMode</code>m)</h3>
<p>Change how the origin is determined. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>originMode()</code>, serOrigin(), <code>origin()</code></dl>
<h3>void QwtThermo::setPipeWidth (intwidth)</h3>
<p>Change the width of the pipe. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>width</i> Width of the pipe</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>pipeWidth()</code></dl>
<h3>void QwtThermo::setRangeFlags (<code>QwtInterval::BorderFlags</code>flags)</h3>
<p>Exclude/Include min/max values. According to the flags minValue() and maxValue() are included/excluded from the pipe. In case of an excluded value the corresponding tick is painted 1 pixel off of the <code>pipeRect()</code>. </p>
<p> F.e. when a minimum of 0.0 has to be displayed as an empty pipe the minValue() needs to be excluded. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>flags</i> Range flags</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>rangeFlags()</code></dl>
<h3>void QwtThermo::setScaleDraw (<code>QwtScaleDraw</code> *scaleDraw)</h3>
<p>Set a scale draw. For changing the labels of the scales, it is necessary to derive from <code>QwtScaleDraw</code> and overload <code>QwtScaleDraw::label()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>scaleDraw</i> ScaleDraw object, that has to be created with new and will be deleted in <code>~QwtThermo()</code> or the next call of <code>setScaleDraw()</code>.</dl>
<h3>void QwtThermo::setScalePosition (<code>ScalePosition</code>scalePosition)</h3>
<p>Change the position of the scale. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>scalePosition</i> Position of the scale.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>ScalePosition</code>, <code>scalePosition()</code></dl>
<h3>void QwtThermo::setSpacing (intspacing)</h3>
<p>Change the spacing between pipe and scale. A spacing of 0 means, that the backbone of the scale is below the pipe. </p>
<p> The default setting is 3 pixels. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>spacing</i> Number of pixels</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>spacing()</code>;</dl>
<h3>void QwtThermo::setValue (doublevalue) [virtual], [slot]</h3>
<p>Set the current value. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> New Value</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>value()</code></dl>
<h3>QSize QwtThermo::sizeHint () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the minimum size hint</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>minimumSizeHint()</code></dl>
<h3>int QwtThermo::spacing () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Number of pixels between pipe and scale</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setSpacing()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
