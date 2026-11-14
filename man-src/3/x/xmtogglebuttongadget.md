---
title: "xmtogglebuttongadget(3)"
name: "xmtogglebuttongadget"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtogglebuttongadget/"
description: "XmToggleButtonGadget — The ToggleButtonGadget widget class"
---

<p><code>XmToggleButtonGadget</code> &#8212; The ToggleButtonGadget widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/ToggleBG.h&gt;</pre>
<h2>Description</h2>
<p>ToggleButtonGadget sets nontransitory state data within an application. Usually this gadget consists of an indicator (square, diamond, or round) with either text or a pixmap on one side of it. However, it can also consist of just text or a pixmap without the indicator. </p>
<p> The toggle graphics display a <code>1-of-many</code>, <code>N-of-many</code>, or <code>N-of-many-round</code> selection state. When a toggle indicator is displayed, a square indicator shows an <code>N-of-many</code> selection state, a diamond-shaped indicator shows a <code>1-of-many</code> selection state, and a circle-shaped indicator shows a <code>1-of-many-round</code> selection state. </p>
<p> ToggleButtonGadget implies a set or unset state. In the case of a label and an indicator, an empty indicator (square, diamond, or round) indicates that ToggleButtonGadget is unset, and a filled indicator shows that it is set. The indicator may be filled with a check mark or the select color. In the case of a pixmap toggle, different pixmaps are used to display the set/unset states. ToggleButtonGadget can also indicate an indeterminate state. In the case of a label and an indicator, an indeterminate state is indicated by a stippled flat box. In the case of a pixmap toggle, a different pixmap is used to display the indeterminate state. </p>
<p> The default behavior associated with a ToggleButtonGadget in a menu depends on the type of menu system in which it resides. By default, <code>&lt;Btn1&gt;</code> controls the behavior of the ToggleButtonGadget. In addition, <code>&lt;Btn3&gt;</code> controls the behavior of the ToggleButtonGadget if it resides in a PopupMenu system. The actual mouse button used is determined by its RowColumn parent. </p>
<p> Label&#8217;s resource <code>XmNmarginLeft</code> may be increased to accommodate the toggle indicator when it is created. </p>
<p> ToggleButtonGadget uses the <code>XmQTmenuSystem</code> and <code>XmQTspecifyRenderTable</code> traits.</p>
<h3>Classes</h3>
<p>ToggleButtonGadget inherits behavior, resources, and traits from <code>Object</code>, <code>RectObj</code>, <code>XmGadget</code> and <code>XmLabelGadget</code>. </p>
<p> The class pointer is <code>xmToggleButtonGadgetClass</code>. </p>
<p> The class name is <code>XmToggleButtonGadget</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmToggleButtonGadget Resource Set</code>
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
<td>XmNarmCallback</td>
<td>XmCArmCallback</td>
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
<td>XmNdetailShadowThickness</td>
<td>XmCDetailShadowThickness</td>
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
<td>XmNdisarmCallback</td>
<td>XmCDisarmCallback</td>
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
<td>XmNfillOnSelect</td>
<td>XmCFillOnSelect</td>
<td>Boolean</td>
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
<td>XmNindeterminatePixmap</td>
<td>XmCIndeterminatePixmap</td>
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
<td>XmNindicatorOn</td>
<td>XmCIndicatorOn</td>
<td>unsigned char</td>
<td>XmINDICATOR_FILL</td>
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
<td>XmNindicatorSize</td>
<td>XmCIndicatorSize</td>
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
<td>XmNindicatorType</td>
<td>XmCIndicatorType</td>
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
<td>XmNselectColor</td>
<td>XmCSelectColor</td>
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
<td>XmNselectInsensitivePixmap</td>
<td>XmCSelectInsensitivePixmap</td>
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
<td>XmNselectPixmap</td>
<td>XmCSelectPixmap</td>
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
<td>XmNset</td>
<td>XmCSet</td>
<td>unsigned char</td>
<td>XmUNSET</td>
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
<td>XmNspacing</td>
<td>XmCSpacing</td>
<td>Dimension</td>
<td>4</td>
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
<td>XmNtoggleMode</td>
<td>XmCToggleMode</td>
<td>unsigned char</td>
<td>XmTOGGLE_BOOLEAN</td>
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
<td>XmNunselectColor</td>
<td>XmCUnselectColor</td>
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
<td>XmNvalueChangedCallback</td>
<td>XmCValueChangedCallback</td>
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
<td>XmNvisibleWhenOff</td>
<td>XmCVisibleWhenOff</td>
<td>Boolean</td>
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
<dl COMPACT>
<dt><code>XmNarmCallback</code></p>
<dd>Specifies a list of callbacks that is called when the ToggleButtonGadget is armed. To arm this gadget, press the active mouse button while the pointer is inside the ToggleButtonGadget. For this callback, the reason is <code>XmCR_ARM</code>.</p>
<dt><code>XmNdetailShadowThickness</code></p>
<dd>Specifies the thickness of the indicator shadow. The default thickness is 2 pixels.</p>
<dt><code>XmNdisarmCallback</code></p>
<dd>Specifies a list of callbacks called when ToggleButtonGadget is disarmed. To disarm this gadget, press and release the active mouse button while the pointer is inside the ToggleButtonGadget. The gadget is also disarmed when the user moves out of the gadget and releases the mouse button when the pointer is outside the gadget. For this callback, the reason is <code>XmCR_DISARM</code>.</p>
<dt><code>XmNfillOnSelect</code></p>
<dd>Fills the indicator with the color specified in <code>XmNselectColor</code> and switches the top and bottom shadow colors when set to True. If unset, fills the indicator with the unselect color. If indeterminate, fills the indicator with half select color and half unselect color. Otherwise, it switches only the top and bottom shadow colors. The default is set True only if a box type of indicator (such as a check box) is specified, or if the <code>XmNindicatorType</code> is a <code>1-of</code> type and a toggle indicator is drawn. If <code>XmNfillOnSelect</code> is True, <code>XmNset</code> is <code>XmSET</code>, and <code>XmNindicatorOn</code> is <code>XmINDICATOR_NONE</code> the ToggleButtonGadget&#8217;s background is set to <code>XmNselectColor</code>. For the other <code>XmNindicatorOn</code> values, only the indicator is filled with <code>XmNselectColor</code>.</p>
<dt><code>XmNindeterminateInsensitivePixmap</code></p>
<dd>Specifies the pixmap to be displayed as the button face when the Label <code>XmNlableType</code> resource is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code>, the ToggleButtonGadget <code>XmNset</code> resource is <code>XmINDETERMINATE</code>, and the <code>Core</code> <code>XmNsensitive</code> resource is False.</p>
<dt><code>XmNindeterminatePixmap</code></p>
<dd>Specifies the pixmap to be displayed as the button face when the Label <code>XmNlableType</code> resource is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code>, the ToggleButtonGadget <code>XmNset</code> resource is <code>XmINDETERMINATE</code>, and the <code>Core</code> <code>XmNsensitive</code> resource is True.</p>
<dt><code>XmNindicatorOn</code></p>
<dd>Specifies that if a toggle indicator is to be drawn, it will be drawn to one side of the toggle text or pixmap, depending on the <code>XmNlayoutDirection</code> resource of the widget. The default value is <code>XmINDICATOR_FILL</code>. Toggles accept the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmINDICATOR_NONE</code></p>
<dd>No space is allocated for the indicator, and it is not displayed. Any shadows around the entire widget are switched when the toggle is selected or unselected.</p>
<dt><code>XmINDICATOR_BOX</code></p>
<dd>The toggle indicator is in the shape of a shadowed box.</p>
<dt><code>XmINDICATOR_FILL</code></p>
<dd>If the value of the <code>XmDisplay XmNenableToggleVisual</code> resource is <code>True</code> , the visuals are those of <code>XmINDICATOR_CHECK_BOX</code> ; if <code>False</code> , the indicator visuals are those of <code>XmINDICATOR_BOX</code>.</p>
<dt><code>XmINDICATOR_CHECK</code></p>
<dd>The toggle indicator is in the shape of a checkmark in the foreground color.</p>
<dt><code>XmINDICATOR_CHECK_BOX</code></p>
<dd>The toggle indicator is in the shape of a checkmark enclosed in a box. This is the default if the <code>XmDisplay XmNenableToggleVisual</code> resource is set.</p>
<dt><code>XmINDICATOR_CROSS_BOX</code></p>
<dd>The toggle indicator is in the shape of a cross enclosed in a box.</p>
<dt><code>XmINDICATOR_CROSS</code></p>
<dd>The toggle indicator is in the shape of a cross.</dl>
</dl>
<dd>All ToggleButton checks and crosses should be drawn in the foreground color.</p>
<dd>If this resource is not <code>XmINDICATOR_NONE</code>, it will control the appearance of the toggle visual. If <code>XmNset</code> is <code>XmINDETERMINATE</code> and <code>XmNindicatorOn</code> is not <code>XmINDICATOR_NONE</code>, this resource shows a stippled flat box. If <code>XmNset</code> is <code>XmINDETERMINATE</code>, <code>XmNindicatorOn</code> is <code>XmINDICATOR_NONE</code>, and <code>XmNtoggleMode</code> is <code>XmTOGGLE_INDETERMINATE</code>, the label and the ToggleButton are stippled with a combination of the <code>XmNselectColor</code> and the <code>XmNunselectColor</code> color, and the border is flat.</p>
<dt><code>XmNindicatorSize</code></p>
<dd>Sets the size of the indicator. If no value is specified, the size of the indicator is based on the size of the label string or pixmap. If the label string or pixmap changes, the size of the indicator is recomputed based on the size of the label string or pixmap. Once a value has been specified for <code>XmNindicatorSize</code>, the indicator has that size, regardless of the size of the label string or pixmap, until a new value is specified. The size of indicators inside menus may differ from those outside of menus. Note that a change in this resource may also cause a change in the values of the inherited resources <code>XmNmarginTop</code>, <code>XmNmarginBottom</code>, and <code>XmNmarginLeft</code>.</p>
<dt><code>XmNindicatorType</code></p>
<dd>Specifies if the indicator is a <code>1-of</code> or <code>N-of</code> indicator. For the <code>1-of</code> indicator, the value can be <code>XmONE_OF_MANY</code>, <code>XmONE_OF_MANY_ROUND</code>, or <code>XmONE_OF_MANY_DIAMOND</code>. For the <code>N-of</code> indicator, the value is <code>XmN_OF_MANY</code>. This value specifies only the visuals and does not enforce the behavior. When the ToggleButton is in a radio box, the default is <code>XmONE_OF_MANY</code>; otherwise, the default is <code>XmN_OF_MANY</code>. Legal values are:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmONE_OF_MANY</code></p>
<dd>When the Display <code>XmNenableToggleVisual</code> resource is set, indicators are drawn with the same appearance as <code>XmONE_OF_MANY_ROUND</code>; otherwise, they appear the same as <code>XmONE_OF_MANY_DIAMOND</code>.</p>
<dt><code>XmN_OF_MANY</code></p>
<dd>The indicators are drawn as specified by the <code>XmNindicatorOn</code> resource.</p>
<dt><code>XmONE_OF_MANY_ROUND</code></p>
<dd>A shadowed circle.</p>
<dt><code>XmONE_OF_MANY_DIAMOND</code></p>
<dd>A shadowed diamond.</dl>
</dl>
<dt><code>XmNselectColor</code></p>
<dd>Allows the application to specify what color fills the center of the square, diamond-shaped, or round indicator when it is set. If this color is the same as either the top or the bottom shadow color of the indicator, a one-pixel-wide margin is left between the shadows and the fill; otherwise, it is filled completely. The results of this resource depend on the value of the Display resource <code>XmNenableToggleColor</code>. A value of True causes the fill color to use the <code>XmHIGHLIGHT_COLOR</code> color by default. A value of False causes the fill color to use the background color. This resource&#8217;s default for a color display is a color between the background and the bottom shadow color. For a monochrome display, the default is set to the foreground color. To set the background of the button to <code>XmNselectColor</code> when <code>XmNindicatorOn</code> is <code>XmINDICATOR_NONE</code>, the value of <code>XmNfillOnSelect</code> must be explicitly set to True.</p>
<dd>This resource can take the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmDEFAULT_SELECT_COLOR</code></p>
<dd>Is the same as the current dynamic default, which is a color between the background and the bottom shadow color.</p>
<dt><code>XmREVERSED_GROUND_COLORS</code></p>
<dd>Forces the select color to the foreground color and causes the default color of any text rendered over the select color to be in the background color.</p>
<dt><code>XmHIGHLIGHT_COLOR</code></p>
<dd>Forces the fill color to use the highlight color.</dl>
</dl>
<dt><code>XmNselectInsensitivePixmap</code></p>
<dd>Specifies a pixmap used as the button face when the ToggleButtonGadget is selected, the button is insensitive, and the LabelGadget resource <code>XmNlabelType</code> is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code>. If the ToggleButtonGadget is unselected and the button is insensitive, the pixmap in <code>XmNlabelInsensitivePixmap</code> is used as the button face. If no value is specified for <code>XmNlabelInsensitivePixmap</code>, that resource is set to the value specified for <code>XmNselectInsensitivePixmap</code>.</p>
<dt><code>XmNselectPixmap</code></p>
<dd>Specifies the pixmap to be used as the button face if <code>XmNlabelType</code> is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code>, and the ToggleButtonGadget is selected. When the ToggleButtonGadget is unselected, the pixmap specified in LabelGadget&#8217;s <code>XmNlabelPixmap</code> is used. If no value is specified for <code>XmNlabelPixmap</code>, that resource is set to the value specified for <code>XmNselectPixmap</code>.</p>
<dt><code>XmNset</code></p>
<dd>Represents the state of the ToggleButton. A value of <code>XmUNSET</code> indicates that the ToggleButton is not set. A value of <code>XmSET</code> indicates that the ToggleButton is set. A value of <code>XmINDETERMINATE</code> indicates that the ToggleButton is in an indeterminate state (neither set nor unset). The ToggleButton states cycle through in the order of <code>XmSET</code>, <code>XmINDETERMINATE</code> (if <code>XmNtoggleMode</code> is set to <code>XmTOGGLE_INDETERMINATE</code>), and <code>XmUNSET</code>, and then back around to <code>XmSET</code>. If <code>XmNtoggleMode</code> is set to <code>XmTOGGLE_BOOLEAN</code>, then the ToggleButton states cycle through in the order of <code>XmSET</code>, then <code>XmUNSET</code>, and then back around to <code>XmSET</code>. Setting this resource sets the state of the ToggleButton.</p>
<dt><code>XmNspacing</code></p>
<dd>Specifies the amount of spacing between the toggle indicator and the toggle label (text or pixmap).</p>
<dt><code>XmNtoggleMode</code></p>
<dd>Specifies the mode of the ToggleButtonGadget as either <code>XmTOGGLE_BOOLEAN</code> or <code>XmTOGGLE_INDETERMINATE</code>. The <code>XmTOGGLE_INDETERMINATE</code> value allows the <code>XmNset</code> resource to be able to accept the values <code>XmINDETERMINATE</code>, <code>XmSET</code>, and <code>XmUNSET</code>. The <code>XmNtoggleMode</code> resource is forced to <code>XmTOGGLE_BOOLEAN</code> if the toggle is in an <code>XmRowColumn</code> widget whose radio behavior is <code>XmONE_OF_MANY</code>. In <code>XmTOGGLE_BOOLEAN</code> mode, the <code>XmNset</code> resource can only accept <code>XmSET</code> and <code>XmUNSET</code>.</p>
<dt><code>XmNunselectColor</code></p>
<dd>Allows the application to specify what color fills the center of the square, diamond-shaped, or round indicator when it is not set. If this color is the same as either the top or the bottom shadow color of the indicator, a one-pixel-wide margin is left between the shadows and the fill; otherwise, it is filled completely. This resource&#8217;s default for a color display is <code>XmNbackground</code>. For a monochrome display, the default is set to the background color. To set the background of the button to <code>XmNunselectColor</code> when <code>XmNindicatorOn</code> is <code>XmINDICATOR_NONE</code>, the value of <code>XmNfillOnSelect</code> must be explicitly set to True. This resource acts like the <code>XmNselectColor</code> resource, but for the case when <code>XmNset</code> is <code>XmUNSET</code>.</p>
<dt><code>XmNvalueChangedCallback</code></p>
<dd>Specifies a list of callbacks called when the ToggleButtonGadget value is changed. To change the value, press and release the active mouse button while the pointer is inside the ToggleButtonGadget. This action also causes the gadget to be disarmed. For this callback, the reason is <code>XmCR_VALUE_CHANGED</code>.</p>
<dt><code>XmNvisibleWhenOff</code></p>
<dd>Indicates that the toggle indicator is visible in the unselected state when the Boolean value is True. When the ToggleButtonGadget is in a menu, the default value is False. When the ToggleButtonGadget is in a RadioBox, the default value is True.</dl>
<h3>Inherited Resources</h3>
<p>ToggleButtonGadget inherits behavior and resources from the superclasses described in the following tables. For a complete description of each resource, refer to the reference page for that superclass. </p>
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
 int <i>set</i>;
} XmToggleButtonCallbackStruct;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the callback</p>
<dt><i>set</i></p>
<dd>Reflects the ToggleButtonGadget&#8217;s state, either <code>XmSET</code> (selected), <code>XmUNSET</code> (unselected), or <code>XmINDETERMINATE</code> (neither). Note that the reported state is the state that the ToggleButtonGadget is in after the <i>event</i> has been processed. For example, suppose that a user clicks on a ToggleButtonGadget to change it from the unselected state to the selected state. In this case, ToggleButtonGadget changes the value of <i>set</i> from <code>XmUNSET</code> to <code>XmSET</code> prior to calling the callback.</dl>
<h3>Behavior</h3>
<p><code>XmToggleButtonGadget</code> includes behavior from <code>XmGadget</code>. <code>XmToggleButtonGadget</code> includes menu traversal behavior from <code>XmLabelGadget</code>. Additional <code>XmToggleButtonGadget</code> behavior is described in the following list:</p>
<dl COMPACT>
<dt><code>&lt;Btn2Down&gt;</code>:</p>
<dd>Drags the contents of a ToggleButtonGadget label, identified when <code>&lt;Btn2&gt;</code> is pressed. This action is undefined for ToggleButtonGadgets used in a menu system.</p>
<dt><code>&lt;Btn1Down&gt;</code>:</p>
<dd>In a menu, this action unposts any menus posted by the ToggleButtonGadget&#8217;s parent menu, disables keyboard traversal for the menu, and enables mouse traversal for the menu. It draws the shadow in the armed state and, unless the button is already armed, calls the <code>XmNarmCallback</code> callbacks.</p>
<dd>Outside a menu, if the button was previously unset, this action does the following: if <code>XmNindicatorOn</code> is True, it draws the indicator shadow so that the indicator looks pressed; if <code>XmNfillOnSelect</code> is True, it fills the indicator with the color specified by <code>XmNselectColor</code>. If <code>XmNindicatorOn</code> is False, it draws the button shadow so that the button looks pressed. If <code>XmNlabelType</code> is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code>, the <code>XmNselectPixmap</code> is used as the button face. This resource calls the <code>XmNarmCallback</code> callbacks.</p>
<dd>Outside a menu, if the button was previously set, this action does the following: if both <code>XmNindicatorOn</code> and <code>XmNvisibleWhenOff</code> are True, it draws the indicator shadow so that the indicator looks raised; if <code>XmNfillOnSelect</code> is True, it fills the indicator with the background color. If <code>XmNindicatorOn</code> is False, it draws the button shadow so that the button looks raised. If <code>XmNlabelType</code> is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code>, the <code>XmNlabelPixmap</code> is used as the button face. This resource calls the <code>XmNarmCallback</code> callbacks.</p>
<dt><code>&lt;Btn1Up&gt;</code>:</p>
<dd>In a menu, this action unposts all menus in the menu hierarchy. If the ToggleButtonGadget was previously set, this action unsets it; if the ToggleButtonGadget was previously unset, this action sets it. It calls the <code>XmNvalueChangedCallback</code> callbacks and then the <code>XmNdisarmCallback</code> callbacks.</p>
<dd>If the button is outside a menu and the pointer is within the button, this action does the following: if the button was previously unset, sets it; if the button was previously set, unsets it. This action calls the <code>XmNvalueChangedCallback</code> callbacks.</p>
<dd>If the button is outside a menu, this action calls the <code>XmNdisarmCallback</code> callbacks.</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfHelp&gt;</code>:</p>
<dd>In a Pulldown or Popup MenuPane, unposts all menus in the menu hierarchy and, when the shell&#8217;s keyboard focus policy is <code>XmEXPLICIT</code>, restores keyboard focus to the widget that had the focus before the menu system was entered. Calls the callbacks for <code>XmNhelpCallback</code> if any exist. If there are no help callbacks for this widget, this action calls the help callbacks for the nearest ancestor that has them.</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfActivate&gt;</code>:</p>
<dd>In a menu, this action unposts all menus in the menu hierarchy. Unless the button is already armed, this action calls the <code>XmNarmCallback</code> callbacks; and calls the <code>XmNvalueChangedCallback</code> and <code>XmNdisarmCallback</code> callbacks. Outside a menu, if the parent is a manager, this action passes the event to the parent.</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfSelect&gt;</code>:</p>
<dd>If the ToggleButtonGadget was previously set, this action unsets it; if the ToggleButtonGadget was previously unset, this action sets it.</p>
<dd>In a menu, this action unposts all menus in the menu hierarchy. Unless the button is already armed, this action calls the <code>XmNarmCallback</code>, the <code>XmNvalueChangedCallback</code>, and <code>XmNdisarmCallback</code> callbacks.</p>
<dd>Outside a menu, if the button was previously unset, this action does the following: If <code>XmNindicatorOn</code> is True, it draws the indicator shadow so that the indicator looks pressed; if <code>XmNfillOnSelect</code> is True, it fills the indicator with the color specified by <code>XmNselectColor</code>. If <code>XmNindicatorOn</code> is False, it draws the button shadow so that the button looks pressed. If <code>XmNlabelType</code> is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code>, the <code>XmNselectPixmap</code> is used as the button face. This action calls the <code>XmNarmCallback</code>, <code>XmNvalueChangedCallback</code>, <code>XmNdisarmCallback</code> callbacks.</p>
<dd>Outside a menu, if the button was previously set, this action does the following: If both <code>XmNindicatorOn</code> and <code>XmNvisibleWhenOff</code> are True, it draws the indicator shadow so that the indicator looks raised; if <code>XmNfillOnSelect</code> is True, it fills the indicator with the background color. If <code>XmNindicatorOn</code> is False, it draws the button shadow so that the button looks raised. If <code>XmNlabelType</code> is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code>, the <code>XmNlabelPixmap</code> is used as the button face. Calls the <code>XmNarmCallback</code>, <code>XmNvalueChangedCallback</code>, and <code>XmNdisarmCallback</code> callbacks.</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfCancel&gt;</code>:</p>
<dd>In a toplevel Pulldown MenuPane from a MenuBar, unposts the menu, disarms the MenuBar CascadeButton and the MenuBar, and, when the shell&#8217;s keyboard focus policy is <code>XmEXPLICIT</code>, restores keyboard focus to the widget that had the focus before the MenuBar was entered. In other Pulldown MenuPanes, this action unposts the menu. Outside a menu, if the parent is a manager, this action passes the event to the parent.</p>
<dd>In a Popup MenuPane, this action unposts the menu and restores keyboard focus to the widget from which the menu was posted.</p>
<dt><code>&lt;Enter&gt;</code>:</p>
<dd>In a menu, if keyboard traversal is enabled, this action does nothing. Otherwise, it draws the shadow in the armed state and calls the <code>XmNarmCallback</code> callbacks.</p>
<dd>If the ToggleButtonGadget is not in a menu and the cursor leaves and then reenters the ToggleButtonGadget while the button is pressed, this action restores the button&#8217;s armed appearance.</p>
<dt><code>&lt;Leave&gt;</code>:</p>
<dd>In a menu, if keyboard traversal is enabled, this action does nothing. Otherwise, it draws the shadow in the unarmed state and calls the <code>XmNdisarmCallback</code> callbacks.</p>
<dd>If the ToggleButtonGadget is not in a menu and the cursor leaves the ToggleButtonGadget while the button is pressed, this action restores the button&#8217;s unarmed appearance.</dl>
<h3>Virtual Bindings</h3>
<p>The bindings for virtual keys are vendor specific. For information about bindings for virtual buttons and keys, see <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-object/">Object</a></code>(3), <code><a href="/docs/linux/man/3-rectobj/">RectObj</a></code>(3), <code><a href="/docs/linux/man/3-xmcreateradiobox/">XmCreateRadioBox</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatetogglebuttongadget/">XmCreateToggleButtonGadget</a></code>(3), <code><a href="/docs/linux/man/3-xmgadget/">XmGadget</a></code>(3), <code><a href="/docs/linux/man/3-xmlabelgadget/">XmLabelGadget</a></code>(3), <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3), <code><a href="/docs/linux/man/3-xmtogglebuttongadgetgetstate/">XmToggleButtonGadgetGetState</a></code>(3), <code><a href="/docs/linux/man/3-xmtogglebuttongadgetsetstate/">XmToggleButtonGadgetSetState</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatetogglebuttongadget/">XmVaCreateToggleButtonGadget</a></code>(3), and <code><a href="/docs/linux/man/3-xmvacreatemanagedtogglebuttongadget/">XmVaCreateManagedToggleButtonGadget</a></code>(3).</p>
