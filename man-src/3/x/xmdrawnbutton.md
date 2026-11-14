---
title: "xmdrawnbutton(3)"
name: "xmdrawnbutton"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmdrawnbutton/"
description: "XmDrawnButton — The DrawnButton widget class"
---

<p><code>XmDrawnButton</code> &#8212; The DrawnButton widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/DrawnB.h&gt;</pre>
<h2>Description</h2>
<p>The DrawnButton widget consists of an empty widget window surrounded by a shadow border. It provides the application developer with a graphics area that can have PushButton input semantics. </p>
<p> Callback types are defined for widget exposure and widget resize to allow the application to redraw or reposition its graphics. If the DrawnButton widget has a highlight and shadow thickness, the application should not draw in that area. To avoid drawing in the highlight and shadow area, create the graphics context with a clipping rectangle for drawing in the widget. The clipping rectangle should take into account the size of the widget&#8217;s highlight thickness and shadow. DrawnButton uses the <code>XmQTmenuSystem</code> and <code>XmQTspecifyRenderTable</code> traits, and holds the <code>XmQTactivatable</code> trait.</p>
<h3>Classes</h3>
<p>DrawnButton inherits behavior, resources, and traits from the <code>Core</code>, <code>Primitive</code>, and <code>XmLabel</code> classes. </p>
<p> The class pointer is <code>xmDrawnButtonWidgetClass</code>. </p>
<p> The class name is <code>XmDrawnButton</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmDrawnButton Resource Set</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>Name</code></td>
<td><code>Class</code></td>
<td><code>Type</code></td>
<td><code>Default</code></td>
<td><code>Access</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNactivateCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNarmCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNdisarmCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNexposeCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNmultiClick</td>
<td>XmCMultiClick</td>
<td>unsigned char</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNpushButtonEnabled</td>
<td>XmCPushButtonEnabled</td>
<td>Boolean</td>
<td>False</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNresizeCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNshadowType</td>
<td>XmCShadowType</td>
<td>unsigned char</td>
<td>XmSHADOW_ETCHED_IN</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
</table>
</table>
<dl COMPACT>
<dt><code>XmNactivateCallback</code></p>
<dd>Specifies the list of callbacks that is called when the widget becomes selected. The reason sent by the callback is <code>XmCR_ACTIVATE</code>. This callback uses the <code>XmQTactivatable</code> trait.</p>
<dt><code>XmNarmCallback</code></p>
<dd>Specifies the list of callbacks that is called when the widget becomes armed. The reason sent by the callback is <code>XmCR_ARM</code>.</p>
<dt><code>XmNdisarmCallback</code></p>
<dd>Specifies the list of callbacks that is called when the widget becomes disarmed. The reason sent by the callback is <code>XmCR_DISARM</code>.</p>
<dt><code>XmNexposeCallback</code></p>
<dd>Specifies the list of callbacks that is called when the widget receives an exposure event. The reason sent by the callback is <code>XmCR_EXPOSE</code>.</p>
<dt><code>XmNmultiClick</code></p>
<dd>If a button click is followed by another button click within the time span specified by the display&#8217;s multiclick time, and this resource is set to <code>XmMULTICLICK_DISCARD</code>, the second click is not processed. If this resource is set to <code>XmMULTICLICK_KEEP</code>, the event is processed and <i>click_count</i> is incremented in the callback structure. When the button is not in a menu, the default value is <code>XmMULTICLICK_KEEP</code>.</p>
<dt><code>XmNpushButtonEnabled</code></p>
<dd>Enables or disables the 3-dimensional shadow drawing as in PushButton.</p>
<dt><code>XmNresizeCallback</code></p>
<dd>Specifies the list of callbacks that is called when the widget receives a resize event. The reason sent by the callback is <code>XmCR_RESIZE</code>. The event returned for this callback is NULL.</p>
<dt><code>XmNshadowType</code></p>
<dd>Describes the drawing style for the DrawnButton. This resource can have the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmSHADOW_IN</code></p>
<dd>Draws the DrawnButton so that the shadow appears inset. This means that the bottom shadow visuals and top shadow visuals are reversed.</p>
<dt><code>XmSHADOW_OUT</code></p>
<dd>Draws the DrawnButton so that the shadow appears outset.</p>
<dt><code>XmSHADOW_ETCHED_IN</code></p>
<dd>Draws the DrawnButton using a double line. This gives the effect of a line etched into the window. The thickness of the double line is equal to the value of <code>XmNshadowThickness</code>.</p>
<dt><code>XmSHADOW_ETCHED_OUT</code></p>
<dd>Draws the DrawnButton using a double line. This gives the effect of a line coming out of the window. The thickness of the double line is equal to the value of <code>XmNshadowThickness</code>.</dl>
</dl>
</dl>
<h3>Inherited Resources</h3>
<p>DrawnButton inherits behavior and resources from the superclasses described in the following tables. For a complete description of each resource, refer to the reference page for that superclass. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmLabel Resource Set</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>Name</code></td>
<td><code>Class</code></td>
<td><code>Type</code></td>
<td><code>Default</code></td>
<td><code>Access</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNaccelerator</td>
<td>XmCAccelerator</td>
<td>String</td>
<td>NULL</td>
<td>N/A
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNacceleratorText</td>
<td>XmCAcceleratorText</td>
<td>XmString</td>
<td>NULL</td>
<td>N/A
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNalignment</td>
<td>XmCAlignment</td>
<td>unsigned char</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNfontList</td>
<td>XmCFontList</td>
<td>XmFontList</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNlabelInsensitivePixmap</td>
<td>XmCLabelInsensitivePixmap</td>
<td>Pixmap</td>
<td>XmUNSPECIFIED_PIXMAP</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNlabelPixmap</td>
<td>XmCLabelPixmap</td>
<td>Pixmap</td>
<td>XmUNSPECIFIED_PIXMAP</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNlabelString</td>
<td>XmCXmString</td>
<td>XmString</td>
<td>&quot;
