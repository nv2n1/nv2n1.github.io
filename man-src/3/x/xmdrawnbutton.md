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
<dt><code>XmNactivateCallback</code></dt>
<dd>Specifies the list of callbacks that is called when the widget becomes selected. The reason sent by the callback is <code>XmCR_ACTIVATE</code>. This callback uses the <code>XmQTactivatable</code> trait.</dd>
<dt><code>XmNarmCallback</code></dt>
<dd>Specifies the list of callbacks that is called when the widget becomes armed. The reason sent by the callback is <code>XmCR_ARM</code>.</dd>
<dt><code>XmNdisarmCallback</code></dt>
<dd>Specifies the list of callbacks that is called when the widget becomes disarmed. The reason sent by the callback is <code>XmCR_DISARM</code>.</dd>
<dt><code>XmNexposeCallback</code></dt>
<dd>Specifies the list of callbacks that is called when the widget receives an exposure event. The reason sent by the callback is <code>XmCR_EXPOSE</code>.</dd>
<dt><code>XmNmultiClick</code></dt>
<dd>If a button click is followed by another button click within the time span specified by the display&#8217;s multiclick time, and this resource is set to <code>XmMULTICLICK_DISCARD</code>, the second click is not processed. If this resource is set to <code>XmMULTICLICK_KEEP</code>, the event is processed and <i>click_count</i> is incremented in the callback structure. When the button is not in a menu, the default value is <code>XmMULTICLICK_KEEP</code>.</dd>
<dt><code>XmNpushButtonEnabled</code></dt>
<dd>Enables or disables the 3-dimensional shadow drawing as in PushButton.</dd>
<dt><code>XmNresizeCallback</code></dt>
<dd>Specifies the list of callbacks that is called when the widget receives a resize event. The reason sent by the callback is <code>XmCR_RESIZE</code>. The event returned for this callback is NULL.</dd>
<dt><code>XmNshadowType</code></dt>
<dd>Describes the drawing style for the DrawnButton. This resource can have the following values:</dd>
<dl COMPACT>
<dd>
</dd><dl COMPACT>
<dt><code>XmSHADOW_IN</code></dt>
<dd>Draws the DrawnButton so that the shadow appears inset. This means that the bottom shadow visuals and top shadow visuals are reversed.</dd>
<dt><code>XmSHADOW_OUT</code></dt>
<dd>Draws the DrawnButton so that the shadow appears outset.</dd>
<dt><code>XmSHADOW_ETCHED_IN</code></dt>
<dd>Draws the DrawnButton using a double line. This gives the effect of a line etched into the window. The thickness of the double line is equal to the value of <code>XmNshadowThickness</code>.</dd>
<dt><code>XmSHADOW_ETCHED_OUT</code></dt>
<dd>Draws the DrawnButton using a double line. This gives the effect of a line coming out of the window. The thickness of the double line is equal to the value of <code>XmNshadowThickness</code>.</dd></dl>
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
<td>&quot;\0&quot;</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNlabelType</td>
<td>XmCLabelType</td>
<td>unsigned char</td>
<td>XmSTRING</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNmarginBottom</td>
<td>XmCMarginBottom</td>
<td>Dimension</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNmarginHeight</td>
<td>XmCMarginHeight</td>
<td>Dimension</td>
<td>2</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNmarginLeft</td>
<td>XmCMarginLeft</td>
<td>Dimension</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNmarginRight</td>
<td>XmCMarginRight</td>
<td>Dimension</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNmarginTop</td>
<td>XmCMarginTop</td>
<td>Dimension</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNmarginWidth</td>
<td>XmCMarginWidth</td>
<td>Dimension</td>
<td>2</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNmnemonic</td>
<td>XmCMnemonic</td>
<td>KeySym</td>
<td>NULL</td>
<td>N/A
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNmnemonicCharSet</td>
<td>XmCMnemonicCharSet</td>
<td>String</td>
<td>XmFONTLIST_DEFAULT_TAG</td>
<td>N/A
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNrecomputeSize</td>
<td>XmCRecomputeSize</td>
<td>Boolean</td>
<td>True</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNrenderTable</td>
<td>XmCRenderTable</td>
<td>XmRenderTable</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNstringDirection</td>
<td>XmCStringDirection</td>
<td>XmStringDirection</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
</table>
</table>
<table BORDER>
<tr>
<td><table>
 <tr VALIGN=top>
<td><code>XmPrimitive Resource Set</code>
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
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNbottomShadowColor</td>
<td>XmCBottomShadowColor</td>
<td>Pixel</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNbottomShadowPixmap</td>
<td>XmCBottomShadowPixmap</td>
<td>Pixmap</td>
<td>XmUNSPECIFIED_PIXMAP</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNconvertCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNforeground</td>
<td>XmCForeground</td>
<td>Pixel</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNhelpCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNhighlightColor</td>
<td>XmCHighlightColor</td>
<td>Pixel</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNhighlightOnEnter</td>
<td>XmCHighlightOnEnter</td>
<td>Boolean</td>
<td>False</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNhighlightPixmap</td>
<td>XmCHighlightPixmap</td>
<td>Pixmap</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNhighlightThickness</td>
<td>XmCHighlightThickness</td>
<td>Dimension</td>
<td>2</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNlayoutDirection</td>
<td>XmCLayoutDirection</td>
<td>XmDirection</td>
<td>dynamic</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNnavigationType</td>
<td>XmCNavigationType</td>
<td>XmNavigationType</td>
<td>XmNONE</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNpopupHandlerCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNshadowThickness</td>
<td>XmCShadowThickness</td>
<td>Dimension</td>
<td>2</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNtopShadowColor</td>
<td>XmCTopShadowColor</td>
<td>Pixel</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNtopShadowPixmap</td>
<td>XmCTopShadowPixmap</td>
<td>Pixmap</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNtraversalOn</td>
<td>XmCTraversalOn</td>
<td>Boolean</td>
<td>True</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNunitType</td>
<td>XmCUnitType</td>
<td>unsigned char</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNuserData</td>
<td>XmCUserData</td>
<td>XtPointer</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
</table>
</table>
<table BORDER>
<tr>
<td><table>
 <tr VALIGN=top>
<td><code>Core Resource Set</code>
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
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNaccelerators</td>
<td>XmCAccelerators</td>
<td>XtAccelerators</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNancestorSensitive</td>
<td>XmCSensitive</td>
<td>Boolean</td>
<td>dynamic</td>
<td>G
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNbackground</td>
<td>XmCBackground</td>
<td>Pixel</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNbackgroundPixmap</td>
<td>XmCPixmap</td>
<td>Pixmap</td>
<td>XmUNSPECIFIED_PIXMAP</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNborderColor</td>
<td>XmCBorderColor</td>
<td>Pixel</td>
<td>XtDefaultForeground</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNborderPixmap</td>
<td>XmCPixmap</td>
<td>Pixmap</td>
<td>XmUNSPECIFIED_PIXMAP</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNborderWidth</td>
<td>XmCBorderWidth</td>
<td>Dimension</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNcolormap</td>
<td>XmCColormap</td>
<td>Colormap</td>
<td>dynamic</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNdepth</td>
<td>XmCDepth</td>
<td>int</td>
<td>dynamic</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNdestroyCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNheight</td>
<td>XmCHeight</td>
<td>Dimension</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNinitialResourcesPersistent</td>
<td>XmCInitialResourcesPersistent</td>
<td>Boolean</td>
<td>True</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNmappedWhenManaged</td>
<td>XmCMappedWhenManaged</td>
<td>Boolean</td>
<td>True</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNscreen</td>
<td>XmCScreen</td>
<td>Screen *</td>
<td>dynamic</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNsensitive</td>
<td>XmCSensitive</td>
<td>Boolean</td>
<td>True</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNtranslations</td>
<td>XmCTranslations</td>
<td>XtTranslations</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNwidth</td>
<td>XmCWidth</td>
<td>Dimension</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNx</td>
<td>XmCPosition</td>
<td>Position</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>XmNy</td>
<td>XmCPosition</td>
<td>Position</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
</table>
</table>
<h3>Callback Information</h3>
<p> A pointer to the following structure is passed to each callback: </p>
<pre><code>typedef struct
{
        int reason ;
        XEvent * event ;
        Window window ;
        int click_count ;
} XmDrawnButtonCallbackStruct;
</code></pre>
<dl>
<dt><i>reason</i></dt>
<dd> <p> Indicates why the callback was invoked. </p>
 </dd>
<dt><i>event</i></dt>
<dd> <p> Points to the <code>XEvent</code> that triggered the callback. This is NULL for <code>XmNresizeCallback</code>. </p>
 </dd>
<dt><i>window</i></dt>
<dd> <p> Is set to the window ID in which the event occurred. </p>
 </dd>
<dt><i>click_count</i></dt>
<dd> <p> Contains the number of clicks in the last multiclick sequence if the <code>XmNmultiClick</code> resource is set to <code>XmMULTICLICK_KEEP</code>, otherwise it contains 1. The activate callback is invoked for each click if <code>XmNmultiClick</code> is set to <code>XmMULTICLICK_KEEP</code>. </p>
 </dd></dl>
<h3>Translations</h3>
<p> XmDrawnButton includes translations from Primitive. Additional XmDrawnButton translations are described in the following list. The following key names are listed in the X standard key event translation table syntax. This format is the one used by Motif to specify the widget actions corresponding to a given key. A brief overview of the format is provided under <code><a href="/docs/linux/man/3-VirtualBindings/">VirtualBindings</a></code>(3). For a complete description of the format, please refer to the X Toolkit Instrinsics Documentation. </p>
<dl>
<dt><code>c&lt;Btn1Down&gt;</code>:</dt>
<dd> <p> ButtonTakeFocus() </p>
 </dd>
<dt><code>&asymp;c</code><code>&lt;Btn1Down&gt;</code>:</dt>
<dd> <p> Arm() </p>
 </dd>
<dt><code>&asymp;c</code><code>&lt;Btn1Down&gt;</code><code>,&asymp;c</code><code>&lt;Btn1Up&gt;</code>:</dt>
<dd> <p> Activate() Disarm() </p>
 </dd>
<dt><code>&asymp;c</code><code>&lt;Btn1Down&gt;</code><code>(2+)</code>:</dt>
<dd> <p> MultiArm() </p>
 </dd>
<dt><code>&asymp;c</code><code>&lt;Btn1Up&gt;</code><code>(2+)</code>:</dt>
<dd> <p> MultiActivate() </p>
 </dd>
<dt><code>&asymp;c</code><code>&lt;Btn1Up&gt;</code>:</dt>
<dd> <p> Activate() Disarm() </p>
 </dd>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfActivate&gt;</code>:</dt>
<dd> <p> PrimitiveParentActivate() </p>
 </dd>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfCancel&gt;</code>:</dt>
<dd> <p> PrimitiveParentCancel() </p>
 </dd>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfSelect&gt;</code>:</dt>
<dd> <p> ArmAndActivate() </p>
 </dd>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfHelp&gt;</code>:</dt>
<dd> <p> Help() </p>
 </dd>
<dt><code>&asymp;s &asymp;m &asymp;a</code><code>&lt;Key&gt;</code><code>Return</code>:</dt>
<dd> <p> PrimitiveParentActivate() </p>
 </dd>
<dt><code>&asymp;s &asymp;m &asymp;a</code><code>&lt;Key&gt;</code><code>space</code>:</dt>
<dd> <p> ArmAndActivate() </p>
 </dd></dl>
<h3>Action Routines</h3>
<p> The <code>XmDrawnButton</code> action routines are </p>
<dl>
<dt>Activate():</dt>
<dd> <p> If <code>XmNpushButtonEnabled</code> is True, redraws the shadow in the unselected state; otherwise, redraws the shadow according to <code>XmNshadowType</code>. If the pointer is within the DrawnButton, calls the <code>XmNactivateCallback</code> callbacks. </p>
 </dd>
<dt>Arm():</dt>
<dd> <p> If <code>XmNpushButtonEnabled</code> is True, redraws the shadow in the selected state; otherwise, redraws the shadow according to <code>XmNshadowType</code>. Calls the callbacks for <code>XmNarmCallback</code>. </p>
 </dd>
<dt>ArmAndActivate():</dt>
<dd> <p> If <code>XmNpushButtonEnabled</code> is True, redraws the shadow in the selected state; otherwise, redraws the shadow according to <code>XmNshadowType</code>. Calls the callbacks for <code>XmNarmCallback</code>. </p>
 </dd>
<dd> <p> If <code>XmNpushButtonEnabled</code> is True, the shadow is redrawn in the unselected state; otherwise, the shadow is redrawn according to <code>XmNshadowType</code>. The callbacks for <code>XmNactivateCallback</code> and <code>XmNdisarmCallback</code> are called. These actions happen either immediately or at a later time. </p>
 </dd>
<dt>ButtonTakeFocus():</dt>
<dd> <p> Causes the PushButton to take keyboard focus when <code>Ctrl&lt;Btn1Down&gt;</code> is pressed, without activating the widget. </p>
 </dd>
<dt>Disarm():</dt>
<dd> <p> Marks the DrawnButton as unselected and calls the callbacks for <code>XmNdisarmCallback</code>. </p>
 </dd>
<dt>Help():</dt>
<dd> <p> Calls the callbacks for <code>XmNhelpCallback</code> if any exist. If there are no help callbacks for this widget, this action calls the help callbacks for the nearest ancestor that has them. </p>
 </dd>
<dt>MultiActivate():</dt>
<dd> <p> If <code>XmNmultiClick</code> is <code>XmMULTICLICK_DISCARD</code>, this action does nothing. </p>
 </dd>
<dd> <p> If <code>XmNmultiClick</code> is <code>XmMULTICLICK_KEEP</code>, this action increments <i>click_count</i> in the callback structure. If <code>XmNpushButtonEnabled</code> is True, this action redraws the shadow in the unselected state; otherwise, it redraws the shadow according to <code>XmNshadowType</code>. If the pointer is within the DrawnButton, this action calls the <code>XmNactivateCallback</code> callbacks and calls the callbacks for <code>XmNdisarmCallback</code>. </p>
 </dd>
<dt>MultiArm():</dt>
<dd> <p> If <code>XmNmultiClick</code> is <code>XmMULTICLICK_DISCARD</code>, this action does nothing. </p>
 </dd>
<dd> <p> If <code>XmNmultiClick</code> is <code>XmMULTICLICK_KEEP</code> and if <code>XmNpushButtonEnabled</code> is True, this action redraws the shadow in the selected state; otherwise, it redraws the shadow according to <code>XmNshadowType</code> and calls the callbacks for <code>XmNarmCallback</code>. </p>
 </dd></dl>
<h3>Additional Behavior</h3>
<p> This widget has the following additional behavior: </p>
<dl>
<dt><code>&lt;EnterWindow&gt;</code>:</dt>
<dd> <p> Draws the shadow in its selected state if <code>XmNpushButtonEnabled</code> is True and if the cursor leaves and re-enters the window while <code>BSelect</code> is pressed. </p>
 </dd>
<dt><code>&lt;LeaveWindow&gt;</code>:</dt>
<dd> <p> Draws the shadow in its unselected state if <code>XmNpushButtonEnabled</code> is True and if the cursor leaves the window while <code>BSelect</code> is pressed. </p>
 </dd></dl>
<h3>Virtual Bindings</h3>
<p> The bindings for virtual keys are vendor specific. For information about bindings for virtual buttons and keys, see <code><a href="/docs/linux/man/3-VirtualBindings/">VirtualBindings</a></code>(3).  </p>
<h2>RELATED</h2>
<p> <code><a href="/docs/linux/man/3-Core/">Core</a></code>(3), <code>XmCreateDrawnButton</code>, <code><a href="/docs/linux/man/3-XmLabel/">XmLabel</a></code>(3), <code><a href="/docs/linux/man/3-XmPrimitive/">XmPrimitive</a></code>(3), <code>XmPushButton</code>, <code><a href="/docs/linux/man/3-XmSeparator/">XmSeparator</a></code>(3), <code>XmVaCreateDrawnButton</code>, <code>XmVaCreateManagedDrawnButton</code>. </p>
