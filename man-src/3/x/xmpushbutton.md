---
title: "xmpushbutton(3)"
name: "xmpushbutton"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmpushbutton/"
description: "XmPushButton — The PushButton widget class"
---

<p><code>XmPushButton</code> &#8212; The PushButton widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/PushB.h&gt;</pre>
<h2>Description</h2>
<p>PushButton issues commands within an application. It consists of a text label or pixmap surrounded by a border shadow. When a PushButton is selected, the shadow changes to give the appearance that it has been pressed in. When a PushButton is unselected, the shadow changes to give the appearance that it is out. </p>
<p> The default behavior associated with a PushButton in a menu depends on the type of menu system in which it resides. By default, <code>&lt;Btn1&gt;</code> controls the behavior of the PushButton. In addition, <code>&lt;Btn3&gt;</code> controls the behavior of the PushButton if it resides in a PopupMenu system. The actual mouse button used is determined by its RowColumn parent. </p>
<p> Thickness for a second shadow, used when the PushButton is the default button, may be specified with the <code>XmNshowAsDefault</code> resource. If it has a nonzero value, the Label&#8217;s resources <code>XmNmarginLeft</code>, <code>XmNmarginRight</code>, <code>XmNmarginTop</code>, and <code>XmNmarginBottom</code> may be modified to accommodate the second shadow. </p>
<p> If an initial value is specified for <code>XmNarmPixmap</code> but not for <code>XmNlabelPixmap</code>, the <code>XmNarmPixmap</code> value is used for <code>XmNlabelPixmap</code>. </p>
<p> PushButton uses the <code>XmQTmenuSystem</code> and <code>XmQTspecifyRenderTable</code> traits, and holds the <code>XmQactivatable</code>, <code>XmQTmenuSavvy</code>, and <code>XmQTtakesDefault</code> traits.</p>
<h3>Classes</h3>
<p>PushButton inherits behavior, resources, and traits from <code>Core</code>, <code>XmPrimitive</code>, and <code>XmLabel</code>. </p>
<p> The class pointer is <code>xmPushButtonWidgetClass</code>. </p>
<p> The class name is <code>XmPushButton</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmPushButton Resource Set</code>
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
<td>XmNarmColor</td>
<td>XmCArmColor</td>
<td>Pixel</td>
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
<td>XmNarmPixmap</td>
<td>XmCArmPixmap</td>
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
<td>XmNdefaultButtonShadowThickness</td>
<td>XmCDefaultButtonShadowThickness</td>
<td>Dimension</td>
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
<td>XmNfillOnArm</td>
<td>XmCFillOnArm</td>
<td>Boolean</td>
<td>True</td>
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
<td>XmNshowAsDefault</td>
<td>XmCShowAsDefault</td>
<td>Dimension</td>
<td>0</td>
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
<dd>Specifies the list of callbacks that is called when PushButton is activated. PushButton is activated when the user presses and releases the active mouse button while the pointer is inside that widget. Activating the PushButton also disarms it. For this callback, the reason is <code>XmCR_ACTIVATE</code>. This callback uses the <code>XmQTactivatable</code> trait.</p>
<dt><code>XmNarmCallback</code></p>
<dd>Specifies the list of callbacks that is called when PushButton is armed. PushButton is armed when the user presses the active mouse button while the pointer is inside that widget. For this callback, the reason is <code>XmCR_ARM</code>.</p>
<dt><code>XmNarmColor</code></p>
<dd>Specifies the color with which to fill the armed button. <code>XmNfillOnArm</code> must be set to True for this resource to have an effect. The default for a color display is a color between the background and the bottom shadow color. For a monochrome display, the default is set to the foreground color, and any text in the label appears in the background color when the button is armed.</p>
<dd>This resource is also used when the button is armed in a menu and the <code>XmNenableEtchedInMenu</code> resource is <code>True</code>.</p>
<dt><code>XmNarmPixmap</code></p>
<dd>Specifies the pixmap to be used as the button face if <code>XmNlabelType</code> is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code> and PushButton is armed. This resource is disabled when the PushButton is in a menu.</p>
<dt><code>XmNdefaultButtonShadowThickness</code></p>
<dd>This resource specifies the width of the default button indicator shadow. If this resource is 0 (zero), the width of the shadow comes from the value of the <code>XmNshowAsDefault</code> resource. If this resource is greater than 0, the <code>XmNshowAsDefault</code> resource is only used to specify whether this button is the default. The default value is the initial value of <code>XmNshowAsDefault</code>.</p>
<dt><code>XmNdisarmCallback</code></p>
<dd>Specifies the list of callbacks that is called when PushButton is disarmed. PushButton is disarmed when the user presses and releases the active mouse button while the pointer is inside that widget. For this callback, the reason is <code>XmCR_DISARM</code>.</p>
<dt><code>XmNfillOnArm</code></p>
<dd>Forces the PushButton to fill the background of the button with the color specified by <code>XmNarmColor</code> when the button is armed and when this resource is set to True. If False, only the top and bottom shadow colors are switched. When the PushButton is in a menu, this resource is ignored and assumed to be False.</p>
<dt><code>XmNmultiClick</code></p>
<dd>If a button click is followed by another button click within the time span specified by the display&#8217;s multiclick time, and this resource is set to <code>XmMULTICLICK_DISCARD</code>, do not process the second click. If this resource is set to <code>XmMULTICLICK_KEEP</code>, process the event and increment <i>click_count</i> in the callback structure. When the button is in a menu, the default is <code>XmMULTICLICK_DISCARD</code>; otherwise, for a button not in a menu, <code>XmMULTICLICK_KEEP</code> is the default value.</p>
<dt><code>XmNshowAsDefault</code></p>
<dd>If <code>XmNdefaultButtonShadowThickness</code> is greater than 0 (zero), a value greater than 0 in this resource specifies to mark this button as the default button. If <code>XmNdefaultButtonShadowThickness</code> is 0, a value greater than 0 in this resource specifies to mark this button as the default button with the shadow thickness specified by this resource. When the Display resource <code>XmNdefaultButtonEmphasis</code> has a value of <code>XmEXTERNAL_HIGHLIGHT</code> (the default), PushButton draws the location cursor outside of the outer shadow. When this resource has a value of <code>XmINTERNAL_HIGHLIGHT</code>, the highlight is drawn between the inner and outer shadows. The space between the shadow and the default shadow is equal to the sum of both shadows. The default value is 0. When this value is not 0, the Label resources <code>XmNmarginLeft</code>, <code>XmNmarginRight</code>, <code>XmNmarginTop</code>, and <code>XmNmarginBottom</code> may be modified to accommodate the second shadow. This resource is disabled when the PushButton is in a menu.</dl>
<h3>Inherited Resources</h3>
<p>PushButton inherits behavior and resources from the superclasses described the following tables. For a complete description of each resource, refer to the reference page for that superclass. </p>
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
<td>XmNacceleratorText</td>
<td>XmCAcceleratorText</td>
<td>XmString</td>
<td>NULL</td>
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
<td>XmNlabelString</td>
<td>XmCXmString</td>
<td>XmString</td>
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
<td>XmNlabelType</td>
<td>XmCLabelType</td>
<td>unsigned char</td>
<td>XmSTRING</td>
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
<td>XmNmarginBottom</td>
<td>XmCMarginBottom</td>
<td>Dimension</td>
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
<td>XmNmarginHeight</td>
<td>XmCMarginHeight</td>
<td>Dimension</td>
<td>2</td>
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
<td>XmNmarginLeft</td>
<td>XmCMarginLeft</td>
<td>Dimension</td>
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
<td>XmNmarginRight</td>
<td>XmCMarginRight</td>
<td>Dimension</td>
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
<td>XmNmarginTop</td>
<td>XmCMarginTop</td>
<td>Dimension</td>
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
<td>XmNmarginWidth</td>
<td>XmCMarginWidth</td>
<td>Dimension</td>
<td>2</td>
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
<td>XmNmnemonic</td>
<td>XmCMnemonic</td>
<td>KeySym</td>
<td>NULL</td>
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
<td>XmNmnemonicCharSet</td>
<td>XmCMnemonicCharSet</td>
<td>String</td>
<td>XmFONTLIST_DEFAULT_TAG</td>
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
<td>XmNpixmapPlacement</td>
<td>XmCPixmapPlacement</td>
<td>unsigned int</td>
<td>XmPIXMAP_LEFT</td>
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
<td>XmNpixmapTextPadding</td>
<td>XmCSpace</td>
<td>Dimension</td>
<td>2</td>
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
<td>XmNrecomputeSize</td>
<td>XmCRecomputeSize</td>
<td>Boolean</td>
<td>True</td>
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
<td>XmNrenderTable</td>
<td>XmCRenderTable</td>
<td>XmRenderTable</td>
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
<td>XmNstringDirection</td>
<td>XmCStringDirection</td>
<td>XmStringDirection</td>
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
</table>
</table>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmPrimitive Resource Set</code>
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
<td>XmNbottomShadowColor</td>
<td>XmCBottomShadowColor</td>
<td>Pixel</td>
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
<td>XmNbottomShadowPixmap</td>
<td>XmCBottomShadowPixmap</td>
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
<td>XmNconvertCallback</td>
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
<td>XmNforeground</td>
<td>XmCForeground</td>
<td>Pixel</td>
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
<td>XmNhelpCallback</td>
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
<td>XmNhighlightColor</td>
<td>XmCHighlightColor</td>
<td>Pixel</td>
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
<td>XmNhighlightOnEnter</td>
<td>XmCHighlightOnEnter</td>
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
<td>XmNhighlightPixmap</td>
<td>XmCHighlightPixmap</td>
<td>Pixmap</td>
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
<td>XmNhighlightThickness</td>
<td>XmCHighlightThickness</td>
<td>Dimension</td>
<td>2</td>
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
<td>XmNlayoutDirection</td>
<td>XmCLayoutDirection</td>
<td>XmDirection</td>
<td>dynamic</td>
<td>CG
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
<td>XmNnavigationType</td>
<td>XmCNavigationType</td>
<td>XmNavigationType</td>
<td>XmNONE</td>
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
<td>XmNpopupHandlerCallback</td>
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
<td>XmNshadowThickness</td>
<td>XmCShadowThickness</td>
<td>Dimension</td>
<td>2</td>
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
<td>XmNtopShadowColor</td>
<td>XmCTopShadowColor</td>
<td>Pixel</td>
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
<td>XmNtopShadowPixmap</td>
<td>XmCTopShadowPixmap</td>
<td>Pixmap</td>
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
<td>XmNtraversalOn</td>
<td>XmCTraversalOn</td>
<td>Boolean</td>
<td>True</td>
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
<td>XmNunitType</td>
<td>XmCUnitType</td>
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
<td>XmNuserData</td>
<td>XmCUserData</td>
<td>XtPointer</td>
<td>NULL</td>
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
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>Core Resource Set</code>
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
<td>XmNaccelerators</td>
<td>XmCAccelerators</td>
<td>XtAccelerators</td>
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
<td>XmNancestorSensitive</td>
<td>XmCSensitive</td>
<td>Boolean</td>
<td>dynamic</td>
<td>G
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
<td>XmNbackground</td>
<td>XmCBackground</td>
<td>Pixel</td>
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
<td>XmNbackgroundPixmap</td>
<td>XmCPixmap</td>
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
<td>XmNborderColor</td>
<td>XmCBorderColor</td>
<td>Pixel</td>
<td>XtDefaultForeground</td>
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
<td>XmNborderPixmap</td>
<td>XmCPixmap</td>
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
<td>XmNborderWidth</td>
<td>XmCBorderWidth</td>
<td>Dimension</td>
<td>0</td>
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
<td>XmNcolormap</td>
<td>XmCColormap</td>
<td>Colormap</td>
<td>dynamic</td>
<td>CG
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
<td>XmNdepth</td>
<td>XmCDepth</td>
<td>int</td>
<td>dynamic</td>
<td>CG
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
<td>XmNdestroyCallback</td>
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
<td>XmNheight</td>
<td>XmCHeight</td>
<td>Dimension</td>
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
<td>XmNinitialResourcesPersistent</td>
<td>XmCInitialResourcesPersistent</td>
<td>Boolean</td>
<td>True</td>
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
<td>XmNmappedWhenManaged</td>
<td>XmCMappedWhenManaged</td>
<td>Boolean</td>
<td>True</td>
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
<td>XmNscreen</td>
<td>XmCScreen</td>
<td>Screen *</td>
<td>dynamic</td>
<td>CG
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
<td>XmNsensitive</td>
<td>XmCSensitive</td>
<td>Boolean</td>
<td>True</td>
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
<td>XmNtranslations</td>
<td>XmCTranslations</td>
<td>XtTranslations</td>
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
<td>XmNwidth</td>
<td>XmCWidth</td>
<td>Dimension</td>
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
<td>XmNx</td>
<td>XmCPosition</td>
<td>Position</td>
<td>0</td>
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
<td>XmNy</td>
<td>XmCPosition</td>
<td>Position</td>
<td>0</td>
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
<h3>Callback Information</h3>
<p>A pointer to the following structure is passed to each callback: </p>
<pre>typedef struct
{
 int <i>reason</i>;
 XEvent <i>* event</i>;
 int <i>click_count</i>;
} XmPushButtonCallbackStruct;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked.</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the callback.</p>
<dt><i>click_count</i></p>
<dd>This value is valid only when the reason is <code>XmCR_ACTIVATE</code>. It contains the number of clicks in the last multiclick sequence if the <code>XmNmultiClick</code> resource is set to <code>XmMULTICLICK_KEEP</code>, otherwise it contains 1. The activate callback is invoked for each click if <code>XmNmultiClick</code> is set to <code>XmMULTICLICK_KEEP</code>.</dl>
<h3>Translations</h3>
<p><code>XmPushButton</code> includes translations from <i>Primitive</i>. </p>
<p> Note that altering translations in <code>#override</code> or <code>#augment</code> mode is undefined. </p>
<p> Additional <code>XmPushButton</code> translations for <code>XmPushButtons</code> not in a menu system are described in the following list. </p>
<p> The following key names are listed in the X standard key event translation table syntax. This format is the one used by Motif to specify the widget actions corresponding to a given key. A brief overview of the format is provided under <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3). For a complete description of the format, please refer to the X Toolkit Instrinsics Documentation.</p>
<dl COMPACT>
<dt><code>c&lt;Btn1Down&gt;</code>:</p>
<dd>ButtonTakeFocus()</p>
<dt><code>&asymp;c</code><code>&lt;Btn1Down&gt;</code>:</p>
<dd>Arm()</p>
<dt><code>&asymp;c</code><code>&lt;Btn1Down&gt;</code><code>,&asymp;c</code><code>&lt;Btn1Up&gt;</code>:</p>
<dd>Activate() Disarm()</p>
<dt><code>&asymp;c</code><code>&lt;Btn1Down&gt;</code><code>(2+)</code>:</p>
<dd>MultiArm()</p>
<dt><code>&asymp;c</code><code>&lt;Btn1Up&gt;</code><code>(2+)</code>:</p>
<dd>MultiActivate()</p>
<dt><code>&asymp;c</code><code>&lt;Btn1Up&gt;</code>:</p>
<dd>Activate() Disarm()</p>
<dt><code>&asymp;c</code><code>&lt;Btn2Down&gt;</code>:</p>
<dd>ProcessDrag()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfActivate&gt;</code>:</p>
<dd>PrimitiveParentActivate()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfCancel&gt;</code>:</p>
<dd>PrimitiveParentCancel()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfSelect&gt;</code>:</p>
<dd>ArmAndActivate()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfHelp&gt;</code>:</p>
<dd>Help()</p>
<dt><code>&asymp;s &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>Return</code>:</p>
<dd>PrimitiveParentActivate()</p>
<dt><code>&asymp;s &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>space</code>:</p>
<dd>ArmAndActivate()</dl>
<p> <code>XmPushButton</code> inherits menu traversal translations from <code>XmLabel</code>. Additional XmPushButton translations for PushButtons in a menu system are described in the following list. In a Popup menu system, <code>&lt;Btn3&gt;</code> also performs the <code>&lt;Btn1&gt;</code> actions. </p>
<p> The following key names are listed in the X standard key event translation table syntax. This format is the one used by Motif to specify the widget actions corresponding to a given key. A brief overview of the format is provided under <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3). For a complete description of the format, please refer to the X Toolkit Instrinsics Documentation.</p>
<dl COMPACT>
<dt><code>&lt;Btn2Down&gt;</code>:</p>
<dd>ProcessDrag()</p>
<dt><code>c&lt;Btn1Down&gt;</code>:</p>
<dd>MenuButtonTakeFocus()</p>
<dt><code>c&lt;Btn1Up&gt;</code>:</p>
<dd>MenuButtonTakeFocusUp()</p>
<dt><code>&asymp;c</code><code>&lt;BtnDown&gt;</code>:</p>
<dd>BtnDown()</p>
<dt><code>&asymp;c</code><code>&lt;BtnUp&gt;</code>:</p>
<dd>BtnUp()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfSelect&gt;</code>:</p>
<dd>ArmAndActivate()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfActivate&gt;</code>:</p>
<dd>ArmAndActivate()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfCancel&gt;</code>:</p>
<dd>MenuEscape()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfHelp&gt;</code>:</p>
<dd>Help()</p>
<dt><code>&asymp;s &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>Return</code>:</p>
<dd>ArmAndActivate()</p>
<dt><code>&asymp;s &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>space</code>:</p>
<dd>ArmAndActivate()</dl>
<h3>Action Routines</h3>
<p>The <code>XmPushButton</code> action routines are</p>
<dl COMPACT>
<dt>Activate():</p>
<dd>This action draws the shadow in the unarmed state. If the button is not in a menu and if <code>XmNfillOnArm</code> is set to True, the background color reverts to the unarmed color. If <code>XmNlabelType</code> is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code>, <code>XmNlabelPixmap</code> is used for the button face. If the pointer is still within the button, this action calls the callbacks for <code>XmNactivateCallback</code>.</p>
<dt>Arm():</p>
<dd>This action arms the PushButton. It draws the shadow in the armed state. If the button is not in a menu and if <code>XmNfillOnArm</code> is set to True, it fills the button with the color specified by <code>XmNarmColor</code>. If <code>XmNlabelType</code> is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code>, the <code>XmNarmPixmap</code> is used for the button face. It calls the <code>XmNarmCallback</code> callbacks.</p>
<dt>ArmAndActivate():</p>
<dd>In a menu, unposts all menus in the menu hierarchy and, unless the button is already armed, calls the <code>XmNarmCallback</code> callbacks. This action calls the <code>XmNactivateCallback</code> and <code>XmNdisarmCallback</code> callbacks.</p>
<dd>Outside a menu, draws the shadow in the armed state and, if <code>XmNfillOnArm</code> is set to True, fills the button with the color specified by <code>XmNarmColor</code>. If <code>XmNlabelType</code> is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code>, <code>XmNarmPixmap</code> is used for the button face. This action calls the <code>XmNarmCallback</code> callbacks.</p>
<dd>Outside a menu, this action also arranges for the following to happen, either immediately or at a later time: the shadow is drawn in the unarmed state and, if <code>XmNfillOnArm</code> is set to True, the background color reverts to the unarmed color. If <code>XmNlabelType</code> is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code>, <code>XmNlabelPixmap</code> is used for the button face. The <code>XmNactivateCallback</code> and <code>XmNdisarmCallback</code> callbacks are called.</p>
<dt>BtnDown():</p>
<dd>This action unposts any menus posted by the PushButton&#8217;s parent menu, disables keyboard traversal for the menu, and enables mouse traversal for the menu. It draws the shadow in the armed state and, unless the button is already armed, calls the <code>XmNarmCallback</code> callbacks.</p>
<dt>BtnUp():</p>
<dd>This action unposts all menus in the menu hierarchy and activates the PushButton. It calls the <code>XmNactivateCallback</code> callbacks and then the <code>XmNdisarmCallback</code> callbacks.</p>
<dt>ButtonTakeFocus():</p>
<dd>Causes the PushButton to take keyboard focus when <code>Ctrl&lt;Btn1Down&gt;</code> is pressed, without activating the widget.</p>
<dt>Disarm():</p>
<dd>Calls the callbacks for <code>XmNdisarmCallback</code>.</p>
<dt>Help():</p>
<dd>In a Pulldown or Popup MenuPane, unposts all menus in the menu hierarchy and, when the shell&#8217;s keyboard focus policy is <code>XmEXPLICIT</code>, restores keyboard focus to the widget that had the focus before the menu system was entered. This action calls the callbacks for <code>XmNhelpCallback</code> if any exist. If there are no help callbacks for this widget, this action calls the help callbacks for the nearest ancestor that has them.</p>
<dt>MenuShellPopdownOne():</p>
<dd>In a top-level Pulldown MenuPane from a MenuBar, unposts the menu, disarms the MenuBar CascadeButton and the MenuBar; and, when the shell&#8217;s keyboard focus policy is <code>XmEXPLICIT</code>, restores keyboard focus to the widget that had the focus before the MenuBar was entered. In other Pulldown MenuPanes, it unposts the menu.</p>
<dd>In a Popup MenuPane, this action unposts the menu and restores keyboard focus to the widget from which the menu was posted.</p>
<dt>MultiActivate():</p>
<dd>If <code>XmNmultiClick</code> is <code>XmMULTICLICK_DISCARD</code>, this action does nothing.</p>
<dd>If <code>XmNmultiClick</code> is <code>XmMULTICLICK_KEEP</code>, this action increments <i>click_count</i> in the callback structure and draws the shadow in the unarmed state. If the button is not in a menu and if <code>XmNfillOnArm</code> is set to True, the background color reverts to the unarmed color. If <code>XmNlabelType</code> is <code>XmPIXMAP</code>, the <code>XmNlabelPixmap</code> is used for the button face. If the pointer is within the PushButton, calls the callbacks for <code>XmNactivateCallback</code> and <code>XmNdisarmCallback</code>.</p>
<dt>MultiArm():</p>
<dd>If <code>XmNmultiClick</code> is <code>XmMULTICLICK_DISCARD</code>, this action does nothing.</p>
<dd>If <code>XmNmultiClick</code> is <code>XmMULTICLICK_KEEP</code>, this action draws the shadow in the armed state. If the button is not in a menu and if <code>XmNfillOnArm</code> is set to True, this action fills the button with the color specified by <code>XmNarmColor</code>. If <code>XmNlabelType</code> is <code>XmPIXMAP</code>, the <code>XmNarmPixmap</code> is used for the button face. This action calls the <code>XmNarmCallback</code> callbacks.</p>
<dt>ProcessDrag():</p>
<dd>Drags the contents of a PushButton label, identified when <code>BTransfer</code> is pressed. This action sets the <code>XmNconvertProc</code> of the DragContext to a function that calls the <code>XmNconvertCallback</code> procedures, possibly multiple times, for the <code>_MOTIF_DROP</code> selection. This action is undefined for PushButtons used in a menu system.</dl>
<h3>Additional Behavior</h3>
<p>This widget has the following additional behavior:</p>
<dl COMPACT>
<dt><code>&lt;EnterWindow&gt;</code>:</p>
<dd>In a menu, if keyboard traversal is enabled, this action does nothing. Otherwise, it draws the shadow in the armed state and calls the <code>XmNarmCallback</code> callbacks.</p>
<dd>If the PushButton is not in a menu and the cursor leaves and then reenters the PushButton&#8217;s window while the button is pressed, this action draws the shadow in the armed state. If <code>XmNfillOnArm</code> is set to True, it also fills the button with the color specified by <code>XmNarmColor</code>. If <code>XmNlabelType</code> is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code>, <code>XmNarmPixmap</code> is used for the button face.</p>
<dt><code>&lt;LeaveWindow&gt;</code>:</p>
<dd>In a menu, if keyboard traversal is enabled, this action does nothing. Otherwise, it draws the shadow in the unarmed state and calls the <code>XmNdisarmCallback</code> callbacks.</p>
<dd>If the PushButton is not in a menu and the cursor leaves the PushButton&#8217;s window while the button is pressed, this action draws the shadow in the unarmed state. If <code>XmNfillOnArm</code> is set to True, the background color reverts to the unarmed color. If <code>XmNlabelType</code> is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code>, the <code>XmNlabelPixmap</code> is used for the button face.</dl>
<h3>Virtual Bindings</h3>
<p>The bindings for virtual keys are vendor specific. For information about bindings for virtual buttons and keys, see <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-core/">Core</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatepushbutton/">XmCreatePushButton</a></code>(3), <code><a href="/docs/linux/man/3-xmlabel/">XmLabel</a></code>(3), <code><a href="/docs/linux/man/3-xmprimitive/">XmPrimitive</a></code>(3), <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatepushbutton/">XmVaCreatePushButton</a></code>(3), and <code><a href="/docs/linux/man/3-xmvacreatemanagedpushbutton/">XmVaCreateManagedPushButton</a></code>(3).</p>
