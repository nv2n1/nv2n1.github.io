---
title: "xmpushbuttongadget(3)"
name: "xmpushbuttongadget"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmpushbuttongadget/"
description: "XmPushButtonGadget — The PushButtonGadget widget class"
---

<p><code>XmPushButtonGadget</code> &#8212; The PushButtonGadget widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/PushBG.h&gt;</pre>
<h2>Description</h2>
<p>PushButtonGadget issues commands within an application. It consists of a text label or pixmap surrounded by a border shadow. When PushButtonGadget is selected, the shadow changes to give the appearance that the PushButtonGadget has been pressed in. When PushButtonGadget is unselected, the shadow changes to give the appearance that the PushButtonGadget is out. </p>
<p> The default behavior associated with a PushButtonGadget in a menu depends on the type of menu system in which it resides. By default, <code>&lt;Btn1&gt;</code> controls the behavior of the PushButtonGadget. In addition, <code>&lt;Btn3&gt;</code> controls the behavior of the PushButtonGadget if it resides in a PopupMenu system. The actual mouse button used is determined by its RowColumn parent. </p>
<p> Thickness for a second shadow may be specified with the <code>XmNshowAsDefault</code> resource. If it has a nonzero value, the Label&#8217;s <code>XmNmarginLeft</code>, <code>XmNmarginRight</code>, <code>XmNmarginTop</code>, and <code>XmNmarginBottom</code> resources may be modified to accommodate the second shadow. </p>
<p> If an initial value is specified for <code>XmNarmPixmap</code> but not for <code>XmNlabelPixmap</code>, the <code>XmNarmPixmap</code> value is used for <code>XmNlabelPixmap</code>. </p>
<p> PushButtonGadget uses the <code>XmQTmenuSystem</code> and <code>XmQTspecifyRenderTable</code> traits, and holds the <code>XmQactivatable</code>, <code>XmQTmenuSavvy</code>, and <code>XmQTtakesDefault</code> traits.</p>
<h3>Classes</h3>
<p>PushButtonGadget inherits behavior, resources, and traits from <code>Object</code>, <code>RectObj</code>, <code>XmGadget</code> and <code>XmLabelGadget</code>. </p>
<p> The class pointer is <code>xmPushButtonGadgetClass</code>. </p>
<p> The class name is <code>XmPushButtonGadget</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmPushButtonGadget Resource Set</code>
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
<td>XmCdefaultButtonShadowThickness</td>
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
<dd>Specifies the list of callbacks that is called when the PushButtonGadget is activated. It is activated when the user presses and releases the active mouse button while the pointer is inside the PushButtonGadget. Activating PushButtonGadget also disarms it. For this callback, the reason is <code>XmCR_ACTIVATE</code>. This callback uses the <code>XmQTactivatable</code> trait.</p>
<dt><code>XmNarmCallback</code></p>
<dd>Specifies the list of callbacks that is called when PushButtonGadget is armed. It is armed when the user presses the active mouse button while the pointer is inside the PushButtonGadget. For this callback, the reason is <code>XmCR_ARM</code>.</p>
<dt><code>XmNarmColor</code></p>
<dd>Specifies the color with which to fill the armed button. <code>XmNfillOnArm</code> must be set to True for this resource to have an effect. The default for a color display is a color between the background and the bottom shadow color. For a monochrome display, the default is set to the foreground color, and any text in the label appears in the background color when the button is armed.</p>
<dt><code>XmNarmPixmap</code></p>
<dd>Specifies the pixmap to be used as the button face if <code>XmNlabeltype</code> is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code> and PushButtonGadget is armed. This resource is disabled when the PushButtonGadget is in a menu.</p>
<dt><code>XmNdefaultButtonShadowThickness</code></p>
<dd>This resource specifies the width of the default button indicator shadow. If this resource is 0 (zero), the width of the shadow comes from the value of the <code>XmNshowAsDefault</code> resource. If this resource is greater than zero, the <code>XmNshowAsDefault</code> resource is only used to specify whether this button is the default. The default value is the initial value of <code>XmNshowAsDefault</code>.</p>
<dt><code>XmNdisarmCallback</code></p>
<dd>Specifies the list of callbacks that is called when the PushButtonGadget is disarmed. PushButtonGadget is disarmed when the user presses and releases the active mouse button while the pointer is inside that gadget. For this callback, the reason is <code>XmCR_DISARM</code>.</p>
<dt><code>XmNfillOnArm</code></p>
<dd>Forces the PushButtonGadget to fill the background of the button with the color specified by <code>XmNarmColor</code> when the button is armed and when this resource is set to True. If it is False, only the top and bottom shadow colors are switched. When the PushButtonGadget is in a menu, this resource is ignored and assumed to be False.</p>
<dt><code>XmNmultiClick</code></p>
<dd>If a button click is followed by another button click within the time span specified by the display&#8217;s multiclick time, and this resource is set to <code>XmMULTICLICK_DISCARD</code>, the second click is not processed. If this resource is set to <code>XmMULTICLICK_KEEP</code>, the event is processed and <i>click_count</i> is incremented in the callback structure. When the button is in a menu, the default is <code>XmMULTICLICK_DISCARD</code>; otherwise, for a button not in a menu, the default value is <code>XmMULTICLICK_KEEP</code>.</p>
<dt><code>XmNshowAsDefault</code></p>
<dd>If <code>XmNdefaultButtonShadowThickness</code> is greater than 0 (zero), a value greater than zero in this resource specifies to mark this button as the default button. If <code>XmNdefaultButtonShadowThickness</code> is 0, a value greater than 0 in this resource specifies to mark this button as the default button with the shadow thickness specified by this resource. The space between the shadow and the default shadow is equal to the sum of both shadows. The default value is 0. When the Display resource <code>XmNdefaultButtonEmphasis</code> has a value of <code>XmEXTERNAL_HIGHLIGHT</code> (the default), PushButton draws the location cursor outside of the outer shadow. When this resource has a value of <code>XmINTERNAL_HIGHLIGHT</code>, the highlight is drawn between the inner and outer shadows. When this value is not 0, the Label <code>XmNmarginLeft</code>, <code>XmNmarginRight</code>, <code>XmNmarginTop</code>, and <code>XmNmarginBottom</code> resources may be modified to accommodate the second shadow. This resource is disabled when the PushButton is in a menu.</dl>
<h3>Inherited Resources</h3>
<p>PushButtonGadget inherits behavior and resources from the superclasses described in the following tables. For a complete description of each resource, refer to the reference page for that superclass. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmLabelGadget Resource Set</code>
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
<td>XmNmnemonicCharSet</td>
<td>XmCMnemonicCharSet</td>
<td>String</td>
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
<td ALIGN=center COLSPAN=5><code>XmGadget Resource Set</code>
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
<td>XmNCLayoutDirection</td>
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
<td ALIGN=center COLSPAN=5><code>RectObj Resource Set</code>
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
<td>XmNborderWidth</td>
<td>XmCBorderWidth</td>
<td>Dimension</td>
<td>0</td>
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
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>Object Resource Set</code>
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
<dd>Valid only when the reason is <code>XmCR_ACTIVATE</code>. It contains the number of clicks in the last multiclick sequence if the <code>XmNmultiClick</code> resource is set to <code>XmMULTICLICK_KEEP</code>; otherwise it contains 1. The activate callback is invoked for each click if <code>XmNmultiClick</code> is set to <code>XmMULTICLICK_KEEP</code>.</dl>
<h3>Behavior</h3>
<p><code>XmPushButtonGadget</code> includes behavior from <code>XmGadget</code>. <code>XmPushButtonGadget</code> includes menu traversal behavior from <code>XmLabelGadget</code>. Additional behavior for XmPushButtonGadget is described in the following list.</p>
<dl COMPACT>
<dt><code>&lt;Btn2Down&gt;</code>:</p>
<dd>Drags the contents of a PushButtonGadget label, identified when <code>&lt;Btn2&gt;</code> is pressed. This action is undefined for PushButtonGadgets used in a menu system.</p>
<dt><code>&lt;Btn1Down&gt;</code>:</p>
<dd>This action arms the PushButtonGadget.</p>
<dd>In a menu, this action unposts any menus posted by the PushButtonGadget&#8217;s parent menu, disables keyboard traversal for the menu, and enables mouse traversal for the menu. It draws the shadow in the armed state. Unless the button is already armed, it calls the <code>XmNarmCallback</code> callbacks.</p>
<dd>If the button is not in a menu, this action draws the shadow in the armed state. If <code>XmNfillOnArm</code> is set to True, it fills the button with the color specified by <code>XmNarmColor</code>. If <code>XmNlabelType</code> is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code>, the <code>XmNarmPixmap</code> is used for the button face. It calls the <code>XmNarmCallback</code> callbacks.</p>
<dt><code>&lt;Btn1&gt;</code><code>(2+)</code>:</p>
<dd>If <code>XmNmultiClick</code> is <code>XmMULTICLICK_DISCARD</code>, this action does nothing.</p>
<dd>If <code>XmNmultiClick</code> is <code>XmMULTICLICK_KEEP</code>, this action draws the shadow in the armed state. If the button is not in a menu and if <code>XmNfillOnArm</code> is set to True, it fills the button with the color specified by <code>XmNarmColor</code>. If <code>XmNlabelType</code> is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code>, the <code>XmNarmPixmap</code> is used for the button face. This action calls the <code>XmNarmCallback</code> callbacks.</p>
<dt><code>&lt;Btn1Up&gt;</code>:</p>
<dd>In a menu, this action unposts all menus in the menu hierarchy and activates the PushButtonGadget. It calls the <code>XmNactivateCallback</code> callbacks and then the <code>XmNdisarmCallback</code> callbacks.</p>
<dd>If the PushButtonGadget is not in a menu, this action draws the shadow in the unarmed state. If <code>XmNfillOnArm</code> is set to True, the background color reverts to the unarmed color. If <code>XmNlabelType</code> is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code>, the <code>XmNlabelPixmap</code> is used for the button face. If the pointer is still within the button, this action calls the callbacks for <code>XmNactivateCallback</code> and <code>XmNdisarmCallback</code>.</p>
<dt><code>&lt;Btn1Up&gt;</code><code>(2+)</code>:</p>
<dd>If <code>XmNmultiClick</code> is <code>XmMULTICLICK_DISCARD</code>, this action does nothing.</p>
<dd>If <code>XmNmultiClick</code> is <code>XmMULTICLICK_KEEP</code>, this action increments <i>click_count</i> in the callback structure and draws the shadow in the unarmed state. If the button is not in a menu and if <code>XmNfillOnArm</code> is set to True, the background color reverts to the unarmed color. If <code>XmNlabelType</code> is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code>, <code>XmNlabelPixmap</code> is used for the button face. If the pointer is within the PushButtonGadget, this action calls the callbacks for <code>XmNactivateCallback</code> and <code>XmNdisarmCallback</code>.</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfActivate&gt;</code>:</p>
<dd>In a menu, this action unposts all menus in the menu hierarchy, unless the button is already armed, and calls the <code>XmNarmCallback</code> callbacks, the <code>XmNactivateCallback</code> and the <code>XmNdisarmCallback</code> callbacks. Outside a menu, <code>KActivate</code> has no effect. For PushButtonGadgets outside of a menu, if the parent is a manager, this action passes the event to the parent.</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfSelect&gt;</code>:</p>
<dd>In a menu, this action unposts all menus in the menu hierarchy, unless the button is already armed, and calls the <code>XmNarmCallback</code> callbacks. This acton calls the <code>XmNactivateCallback</code> and <code>XmNdisarmCallback</code> callbacks.</p>
<dd>Outside a menu, this action draws the shadow in the armed state and, if <code>XmNfillOnArm</code> is set to True, fills the button with the color specified by <code>XmNarmColor</code>. If <code>XmNlabelType</code> is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code>, <code>XmNarmPixmap</code> is used for the button face. This action calls the <code>XmNarmCallback</code> callbacks.</p>
<dd>Outside a menu, this action also arranges for the following to happen, either immediately or at a later time: the shadow is drawn in the unarmed state and, if <code>XmNfillOnArm</code> is set to True, the background color reverts to the unarmed color. If <code>XmNlabelType</code> is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code>, the <code>XmNlabelPixmap</code> is used for the button face. The <code>XmNactivateCallback</code> and <code>XmNdisarmCallback</code> callbacks are called.</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfHelp&gt;</code>:</p>
<dd>In a Pulldown or Popup MenuPane, unposts all menus in the menu hierarchy and restores keyboard focus to the widget that had the focus before the menu system was entered. This action calls the callbacks for <code>XmNhelpCallback</code> if any exist. If there are no help callbacks for this widget, this action calls the help callbacks for the nearest ancestor that has them.</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfCancel&gt;</code>:</p>
<dd>In a toplevel Pulldown MenuPane from a MenuBar, unposts the menu, disarms the MenuBar CascadeButton and the MenuBar, and restores keyboard focus to the widget that had the focus before the MenuBar was entered. In other Pulldown MenuPanes, unposts the menu.</p>
<dd>In a Popup MenuPane, unposts the menu and restores keyboard focus to the widget from which the menu was posted. For a PushButtonGadget outside of a menu, if the parent is a manger, this action passes the event to the parent.</p>
<dt><code>&lt;Enter&gt;</code>:</p>
<dd>In a menu, if keyboard traversal is enabled, this action does nothing. Otherwise, it draws the shadow in the armed state and calls the <code>XmNarmCallback</code> callbacks.</p>
<dd>If the PushButtonGadget is not in a menu and the cursor leaves and then reenters the PushButtonGadget while the button is pressed, this action draws the shadow in the armed state. If <code>XmNfillOnArm</code> is set to True, it also fills the button with the color specified by <code>XmNarmColor</code>. If <code>XmNlabelType</code> is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code>, the <code>XmNarmPixmap</code> is used for the button face.</p>
<dt><code>&lt;Leave&gt;</code>:</p>
<dd>In a menu, if keyboard traversal is enabled, this action does nothing. Otherwise, it draws the shadow in the unarmed state and calls the <code>XmNdisarmCallback</code> callbacks.</p>
<dd>If the PushButtonGadget is not in a menu and the cursor leaves the PushButtonGadget while the button is pressed, this action draws the shadow in the unarmed state. If <code>XmNfillOnArm</code> is set to True, the background color reverts to the unarmed color. If <code>XmNlabelType</code> is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code>, the <code>XmNlabelPixmap</code> is used for the button face.</dl>
<h3>Virtual Bindings</h3>
<p>The bindings for virtual keys are vendor specific. For information about bindings for virtual buttons and keys, see <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-object/">Object</a></code>(3), <code><a href="/docs/linux/man/3-rectobj/">RectObj</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatepushbuttongadget/">XmCreatePushButtonGadget</a></code>(3), <code><a href="/docs/linux/man/3-xmgadget/">XmGadget</a></code>(3), <code><a href="/docs/linux/man/3-xmlabelgadget/">XmLabelGadget</a></code>(3), <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatepushbuttongadget/">XmVaCreatePushButtonGadget</a></code>(3), and <code><a href="/docs/linux/man/3-xmvacreatemanagedpushbuttongadget/">XmVaCreateManagedPushButtonGadget</a></code>(3).</p>
