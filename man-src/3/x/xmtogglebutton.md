---
title: "xmtogglebutton(3)"
name: "xmtogglebutton"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtogglebutton/"
description: "XmToggleButton — The ToggleButton widget class"
---

<p><code>XmToggleButton</code> &#8212; The ToggleButton widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/ToggleB.h&gt;</pre>
<h2>Description</h2>
<p>ToggleButton sets nontransitory state data within an application. Usually this widget consists of an indicator (square, diamond, or round) with either text or a pixmap on one side of it. However, it can also consist of just text or a pixmap without the indicator. </p>
<p> The toggle graphics display a <code>1-of-many</code>, <code>N-of-many</code>, or <code>1-of-many-round</code> selection state. When a toggle indicator is displayed, a square indicator shows an <code>N-of-many</code> selection state, a diamond-shaped indicator shows a <code>1-of-many</code> selection state, and a circle-shaped indicator shows a <code>1-of-many-round</code> selection state. </p>
<p> ToggleButton implies a set or unset state. In the case of a label and an indicator, an empty indicator (square, diamond, or round) indicates that ToggleButton is unset, and a filled indicator shows that it is set. The indicator may be filled with a check mark, a cross, or the select color. In the case of a pixmap toggle, different pixmaps are used to display the set/unset states. ToggleButton can also indicate an indeterminate state. In the case of a label and an indicator, an indeterminate state is indicated by a stippled flat box. In the case of a pixmap toggle, a different pixmap is used to display the indeterminate state. </p>
<p> The default behavior associated with a ToggleButton in a menu depends on the type of menu system in which it resides. By default, <code>&lt;Btn1&gt;</code> controls the behavior of the ToggleButton. In addition, <code>&lt;Btn3&gt;</code> controls the behavior of the ToggleButton if it resides in a PopupMenu system. The actual mouse button used is determined by its RowColumn parent. </p>
<p> Label&#8217;s resource <code>XmNmarginLeft</code> may be increased to accommodate the toggle indicator when it is created. </p>
<p> ToggleButton uses the <code>XmQTmenuSystem</code> and <code>XmQTspecifyRenderTable</code> traits.</p>
<h3>Classes</h3>
<p>ToggleButton inherits behavior, resources, and traits from <code>Core</code>, <code>XmPrimitive</code>, and <code>XmLabel</code>. </p>
<p> The class pointer is <code>xmToggleButtonWidgetClass</code>. </p>
<p> The class name is <code>XmToggleButton</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmToggleButton Resource Set</code>
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
<dd>Specifies the list of callbacks called when the ToggleButton is armed. To arm this widget, press the active mouse button while the pointer is inside the ToggleButton. For this callback, the reason is <code>XmCR_ARM</code>.</p>
<dt><code>XmNdetailShadowThickness</code></p>
<dd>Specifies the thickness of the indicator shadow. The default thickness is 2 pixels.</p>
<dt><code>XmNdisarmCallback</code></p>
<dd>Specifies the list of callbacks called when ToggleButton is disarmed. To disarm this widget, press and release the active mouse button while the pointer is inside the ToggleButton. This widget is also disarmed when the user moves out of the widget and releases the mouse button when the pointer is outside the widget. For this callback, the reason is <code>XmCR_DISARM</code>.</p>
<dt><code>XmNfillOnSelect</code></p>
<dd>Fills the indicator with the color specified in <code>XmNselectColor</code> and switches the top and bottom shadow colors when set to True. If unset, fills the indicator with the unselect color. If indeterminate, fills the indicator with half select color and half unselect color. Otherwise, it switches only the top and bottom shadow colors. The default is True only if a box type of indicator (such as a check box) is specified, or if the <code>XmNindicatorType</code> is a <code>1-of</code> type and a toggle indicator is drawn.</p>
<dd>If <code>XmNfillOnSelect</code> is True, <code>XmNset</code> is <code>XmSET</code>, and <code>XmNindicatorOn</code> is <code>XmINDICATOR_NONE</code> the ToggleButton&#8217;s background is set to <code>XmNselectColor</code>. For the other <code>XmNindicatorOn</code> values, only the indicator is filled with <code>XmNselectColor</code>.</p>
<dt><code>XmNindeterminateInsensitivePixmap</code></p>
<dd>Specifies the pixmap to be displayed as the button face when the Label <code>XmNlableType</code> resource is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code>, the ToggleButton <code>XmNset</code> resource is <code>XmINDETERMINATE</code>, and the <code>Core</code> <code>XmNsensitive</code> resource is False.</p>
<dt><code>XmNindeterminatePixmap</code></p>
<dd>Specifies the pixmap to be displayed as the button face when the Label <code>XmNlableType</code> resource is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code>, the ToggleButton <code>XmNset</code> resource is <code>XmINDETERMINATE</code>, and the <code>Core</code> <code>XmNsensitive</code> resource is True.</p>
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
<dd>This resource is also used as the background color when all of the following conditions are met: the button is armed in a menu, the <code>XmNenableEtchedInMenu</code> resource is <code>True</code>, the <code>XmNindicatorOn</code> resource is <code>False</code>, and the <code>XmNfillOnSelect</code> resource is <code>True</code>.</p>
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
<dd>Specifies a pixmap used as the button face when the ToggleButton is selected, the button is insensitive, and the Label resource <code>XmNlabelType</code> is set to <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code>. If the ToggleButton is unselected and the button is insensitive, the pixmap in <code>XmNlabelInsensitivePixmap</code> is used as the button face. If no value is specified for <code>XmNlabelInsensitivePixmap</code>, that resource is set to the value specified for <code>XmNselectInsensitivePixmap</code>.</p>
<dt><code>XmNselectPixmap</code></p>
<dd>Specifies the pixmap to be used as the button face when <code>XmNlabelType</code> is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code>, and the ToggleButton is selected. When the ToggleButton is unselected, the pixmap specified in the Label&#8217;s <code>XmNlabelPixmap</code> is used. If no value is specified for <code>XmNlabelPixmap</code>, that resource is set to the value specified for <code>XmNselectPixmap</code>.</p>
<dt><code>XmNset</code></p>
<dd>Represents the state of the ToggleButton. A value of <code>XmUNSET</code> indicates that the ToggleButton is not set. A value of <code>XmSET</code> indicates that the ToggleButton is set. A value of <code>XmINDETERMINATE</code> indicates that the ToggleButton is in an indeterminate state (neither set nor unset). The ToggleButton states cycle through in the order of <code>XmSET</code>, <code>XmINDETERMINATE</code> (if <code>XmNtoggleMode</code> is set to <code>XmTOGGLE_INDETERMINATE</code>), and <code>XmUNSET</code>, and then back around to <code>XmSET</code>. If <code>XmNtoggleMode</code> is set to <code>XmTOGGLE_BOOLEAN</code>, then the ToggleButton states cycle through in the order of <code>XmSET</code>, then <code>XmUNSET</code>, and then back around to <code>XmSET</code>. Setting this resource sets the state of the ToggleButton.</p>
<dt><code>XmNspacing</code></p>
<dd>Specifies the amount of spacing between the toggle indicator and the toggle label (text or pixmap).</p>
<dt><code>XmNtoggleMode</code></p>
<dd>Specifies the mode of the ToggleButton as either <code>XmTOGGLE_BOOLEAN</code> or <code>XmTOGGLE_INDETERMINATE</code>. The <code>XmTOGGLE_INDETERMINATE</code> value allows the <code>XmNset</code> resource to be able to accept the values <code>XmINDETERMINATE</code>, <code>XmSET</code>, and <code>XmUNSET</code>. The <code>XmNtoggleMode</code> resource is forced to <code>XmTOGGLE_BOOLEAN</code> if the toggle is in an <code>XmRowColumn</code> widget whose radio behavior is <code>XmONE_OF_MANY</code>. In <code>XmTOGGLE_BOOLEAN</code> mode, the <code>XmNset</code> resource can only accept <code>XmSET</code> and <code>XmUNSET</code>.</p>
<dt><code>XmNunselectColor</code></p>
<dd>Allows the application to specify what color fills the center of the square, diamond-shaped, or round indicator when it is not set. If this color is the same as either the top or the bottom shadow color of the indicator, a one-pixel-wide margin is left between the shadows and the fill; otherwise, it is filled completely. This resource&#8217;s default for a color display is <code>XmNbackground</code>. For a monochrome display, the default is set to the background color. To set the background of the button to <code>XmNunselectColor</code> when <code>XmNindicatorOn</code> is <code>XmINDICATOR_NONE</code>, the value of <code>XmNfillOnSelect</code> must be explicitly set to True. This resource acts like the <code>XmNselectColor</code> resource, but for the case when <code>XmNset</code> is <code>XmUNSET</code>.</p>
<dt><code>XmNvalueChangedCallback</code></p>
<dd>Specifies the list of callbacks called when the ToggleButton value is changed. To change the value, press and release the active mouse button while the pointer is inside the ToggleButton. This action also causes this widget to be disarmed. For this callback, the reason is <code>XmCR_VALUE_CHANGED</code>.</p>
<dt><code>XmNvisibleWhenOff</code></p>
<dd>Indicates that the toggle indicator is visible in the unselected state when the Boolean value is True. When the ToggleButton is in a menu, the default value is False. When the ToggleButton is in a RadioBox, the default value is True.</dl>
<h3>Inherited Resources</h3>
<p>ToggleButton inherits behavior and resources from the superclasses described in the following tables. For a complete description of each resource, refer to the reference page for that superclass. </p>
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
 int <i>set</i>;
} XmToggleButtonCallbackStruct;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the callback</p>
<dt><i>set</i></p>
<dd>Reflects the ToggleButton&#8217;s state, either <code>XmSET</code> (selected), <code>XmUNSET</code> (unselected), or <code>XmINDETERMINATE</code> (neither). Note that the reported state is the state that the ToggleButton is in after the <i>event</i> has been processed. For example, suppose that a user clicks on a ToggleButton to change it from the unselected state to the selected state. In this case, ToggleButton changes the value of <i>set</i> from <code>XmUNSET</code> to <code>XmSET</code> prior to calling the callback.</dl>
<h3>Translations</h3>
<p><code>XmToggleButton</code> includes translations from <i>Primitive</i>. Additional <code>XmToggleButton</code> translations for buttons not in a menu system are described in the following list. </p>
<p> Note that altering translations in <code>#override</code> or <code>#augment</code> mode is undefined. </p>
<p> The following key names are listed in the X standard key event translation table syntax. This format is the one used by Motif to specify the widget actions corresponding to a given key. A brief overview of the format is provided under <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3). For a complete description of the format, please refer to the X Toolkit Instrinsics Documentation.</p>
<dl COMPACT>
<dt><code>c&lt;Btn1Down&gt;</code>:</p>
<dd>ButtonTakeFocus()</p>
<dt><code>&asymp;c</code><code>&lt;Btn1Down&gt;</code>:</p>
<dd>Arm()</p>
<dt><code>&asymp;c</code><code>&lt;Btn1Up&gt;</code>:</p>
<dd>Select() Disarm()</p>
<dt><code>&lt;Btn2Down&gt;</code>:</p>
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
<p> <code>XmToggleButton</code> inherits menu traversal translations from <code>XmLabel</code>. Additional <code>XmToggleButton</code> translations for <code>ToggleButtons</code> in a menu system are described in the following list. In a Popup menu system, <code>&lt;Btn3&gt;</code> also performs the <code>&lt;Btn1&gt;</code> actions.</p>
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
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfHelp&gt;</code>:</p>
<dd>Help()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfCancel&gt;</code>:</p>
<dd>MenuEscape()</p>
<dt><code>&asymp;s &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>Return</code>:</p>
<dd>ArmAndActivate()</p>
<dt><code>&asymp;s &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>space</code>:</p>
<dd>ArmAndActivate()</dl>
<h3>Action Routines</h3>
<p>The <code>XmToggleButton</code> action routines are</p>
<dl COMPACT>
<dt>Arm():</p>
<dd>If the button was previously unset, this action does the following: if <code>XmNindicatorOn</code> is True, it draws the indicator shadow so that the indicator looks pressed; if <code>XmNfillOnSelect</code> is True, it fills the indicator with the color specified by <code>XmNselectColor</code>. If <code>XmNindicatorOn</code> is False, it draws the button shadow so that the button looks pressed. If <code>XmNlabelType</code> is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code>, the <code>XmNselectPixmap</code> is used as the button face. This action calls the <code>XmNarmCallback</code> callbacks.</p>
<dd>If the button was previously set, this action does the following: if both <code>XmNindicatorOn</code> and <code>XmNvisibleWhenOff</code> are True, it draws the indicator shadow so that the indicator looks raised; if <code>XmNfillOnSelect</code> is True, it fills the indicator with the background color. If <code>XmNindicatorOn</code> is False, it draws the button shadow so that the button looks raised. If <code>XmNlabelType</code> is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code>, the <code>XmNlabelPixmap</code> is used as the button face. This action calls the <code>XmNarmCallback</code> callbacks.</p>
<dt>ArmAndActivate():</p>
<dd>If the ToggleButton was previously set, unsets it; if the ToggleButton was previously unset, sets it.</p>
<dd>In a menu, this action unposts all menus in the menu hierarchy. Unless the button is already armed, it calls the <code>XmNarmCallback</code> callbacks. This action calls the <code>XmNvalueChangedCallback</code> and <code>XmNdisarmCallback</code> callbacks.</p>
<dd>Outside a menu, if the button was previously unset, this action does the following: if <code>XmNindicatorOn</code> is True, it draws the indicator shadow so that the indicator looks pressed; if <code>XmNfillOnSelect</code> is True, it fills the indicator with the color specified by <code>XmNselectColor</code>. If <code>XmNindicatorOn</code> is False, it draws the button shadow so that the button looks pressed. If <code>XmNlabelType</code> is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code>, the <code>XmNselectPixmap</code> is used as the button face. This action calls the <code>XmNarmCallback</code>, <code>XmNvalueChangedCallback</code>, and <code>XmNdisarmCallback</code> callbacks.</p>
<dd>Outside a menu, if the button was previously set, this action does the following: if both <code>XmNindicatorOn</code> and <code>XmNvisibleWhenOff</code> are True, it draws the indicator shadow so that the indicator looks raised; if <code>XmNfillOnSelect</code> is True, it fills the indicator with the background color. If <code>XmNindicatorOn</code> is False, it draws the button shadow so that the button looks raised. If <code>XmNlabelType</code> is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code>, the <code>XmNlabelPixmap</code> is used as the button face. This action calls the <code>XmNarmCallback</code>, <code>XmNvalueChangedCallback</code>, and <code>XmNdisarmCallback</code> callbacks.</p>
<dt>BtnDown():</p>
<dd>This action unposts any menus posted by the ToggleButton&#8217;s parent menu, disables keyboard traversal for the menu, and enables mouse traversal for the menu. It draws the shadow in the armed state and, unless the button is already armed, calls the <code>XmNarmCallback</code> callbacks.</p>
<dt>BtnUp():</p>
<dd>This action unposts all menus in the menu hierarchy. If the ToggleButton was previously set, unsets it; if the ToggleButton was previously unset, sets it. It calls the <code>XmNvalueChangedCallback</code> callbacks and then the <code>XmNdisarmCallback</code> callbacks.</p>
<dt>ButtonTakeFocus():</p>
<dd>Causes the ToggleButton to take keyboard focus when <code>Ctrl&lt;Btn1Down&gt;</code> is pressed, without activating the widget.</p>
<dt>Disarm():</p>
<dd>Calls the callbacks for <code>XmNdisarmCallback</code>.</p>
<dt>Help():</p>
<dd>In a Pulldown or Popup MenuPane, unposts all menus in the menu hierarchy and restores keyboard focus to the widget that had the focus before the menu system was entered. Calls the callbacks for <code>XmNhelpCallback</code> if any exist. If there are no help callbacks for this widget, this action calls the help callbacks for the nearest ancestor that has them.</p>
<dt>MenuShellPopdownOne():</p>
<dd>In a toplevel Pulldown MenuPane from a MenuBar, unposts the menu, disarms the MenuBar CascadeButton and the MenuBar, and restores keyboard focus to the widget that had the focus before the MenuBar was entered. In other Pulldown MenuPanes, unposts the menu.</p>
<dd>In a Popup MenuPane, unposts the menu and restores keyboard focus to the widget from which the menu was posted.</p>
<dt>ProcessDrag():</p>
<dd>Drags the contents of a ToggleButton label, identified when <code>BTransfer</code> is pressed. This action sets the <code>XmNconvertProc</code> of the DragContext to a function that calls the <code>XmNconvertCallback</code> procedures, possibly multiple times, for the <code>_MOTIF_DROP</code> selection. This action is undefined for ToggleButtons used in a menu system.</p>
<dt>Select():</p>
<dd>If the pointer is within the button, takes the following actions: If the button was previously unset, sets it; if the button was previously set, unsets it. This action calls the <code>XmNvalueChangedCallback</code> callbacks.</dl>
<h3>Additional Behavior</h3>
<p>This widget has the following additional behavior:</p>
<dl COMPACT>
<dt><code>&lt;EnterWindow&gt;</code>:</p>
<dd>In a menu, if keyboard traversal is enabled, this action does nothing. Otherwise, it draws the shadow in the armed state and calls the <code>XmNarmCallback</code> callbacks.</p>
<dd>If the ToggleButton is not in a menu and the cursor leaves and then reenters the ToggleButton&#8217;s window while the button is pressed, this action restores the button&#8217;s armed appearance.</p>
<dt><code>&lt;LeaveWindow&gt;</code>:</p>
<dd>In a menu, if keyboard traversal is enabled, this action does nothing. Otherwise, it draws the shadow in the unarmed state and calls the <code>XmNdisarmCallback</code> callbacks.</p>
<dd>If the ToggleButton is not in a menu and the cursor leaves the ToggleButton&#8217;s window while the button is pressed, this action restores the button&#8217;s unarmed appearance.</dl>
<h3>Virtual Bindings</h3>
<p>The bindings for virtual keys are vendor specific. For information about bindings for virtual buttons and keys, see <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-core/">Core</a></code>(3), <code><a href="/docs/linux/man/3-xmcreateradiobox/">XmCreateRadioBox</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatetogglebutton/">XmCreateToggleButton</a></code>(3), <code><a href="/docs/linux/man/3-xmlabel/">XmLabel</a></code>(3), <code><a href="/docs/linux/man/3-xmprimitive/">XmPrimitive</a></code>(3), <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3), <code><a href="/docs/linux/man/3-xmtogglebuttongetstate/">XmToggleButtonGetState</a></code>(3), <code><a href="/docs/linux/man/3-xmtogglebuttonsetstate/">XmToggleButtonSetState</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatetogglebutton/">XmVaCreateToggleButton</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatemanagedtogglebutton/">XmVaCreateManagedToggleButton</a></code>(3).</p>
