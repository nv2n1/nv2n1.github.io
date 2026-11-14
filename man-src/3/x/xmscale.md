---
title: "xmscale(3)"
name: "xmscale"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmscale/"
description: "XmScale — The Scale widget class"
---

<p><code>XmScale</code> &#8212; The Scale widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Scale.h&gt;</pre>
<h2>Description</h2>
<p>Scale is used by an application to indicate a value from within a range of values, and it allows the user to input or modify a value from the same range. </p>
<p> A Scale has an elongated rectangular region similar to a ScrollBar. A slider inside this region indicates the current value along the Scale. The user can also modify the Scale&#8217;s value by moving the slider within the rectangular region of the Scale. A Scale can also include a label set located outside the Scale region. These can indicate the relative value at various positions along the scale. The placement of this label depends on the <code>XmNlayoutDirection</code> resource of the widget. </p>
<p> A Scale can be either input/output or output only. An input/output Scale&#8217;s value can be set by the application and also modified by the user with the slider. An output-only Scale is used strictly as an indicator of the current value of something and cannot be modified interactively by the user. The <code>XmScale</code> resource <code>XmNeditable</code> specifies whether the user can interactively modify the Scale&#8217;s value. </p>
<p> The user can specify resources in a resource file for the automatically created gadget that contains the title of the Scale widget. The name of the gadget is <code>Title</code>. The placement of the title depends on the <code>XmNlayoutDirection</code> resource of the widget. The direction of the title is based on the widget&#8217;s layout direction. </p>
<p> Scale uses the <code>XmQTspecifyRenderTable</code> trait, and holds the <code>XmQTtransfer</code> trait.</p>
<h3>Data Transfer Behavior</h3>
<p>Scale supports dragging of the representation of the Scale value from the Scale when the value is displayed and when the value of the <code>XmNenableUnselectableDrag</code> resource of <code>XmDisplay</code> is set to True. </p>
<p> As a source of data, Scale supports the following targets and associated conversions of data to these targets:</p>
<dl COMPACT>
<dt><code>COMPOUND_TEXT</code></p>
<dd>The widget transfers a string representation of <code>XmNvalue</code> as type <code>COMPOUND_TEXT</code>.</p>
<dt><code>UTF8_STRING</code></p>
<dd>The widget transfers a string representation of <code>XmNvalue</code> as type <code>UTF8_STRING</code>.</p>
<dt><code>STRING</code></p>
<dd>The widget transfers a string representation of <code>XmNvalue</code> as type <code>STRING</code>.</p>
<dt><code>_MOTIF_CLIPBOARD_TARGETS</code></p>
<dd>The widget transfers, as type <code>ATOM</code>, a list of the targets it supports for the <code>CLIPBOARD</code> selection. These include <code>STRING</code>, <code>COMPOUND_TEXT</code> and <code>UTF8_STRING</code>.</p>
<dt><code>_MOTIF_EXPORT_TARGETS</code></p>
<dd>The widget transfers, as type <code>ATOM</code>, a list of the targets to be used as the value of the DragContext&#8217;s <code>XmNexportTargets</code> in a drag-and-drop transfer. These include <code>STRING</code>, <code>COMPOUND_TEXT</code> and <code>UTF8_STRING</code>.</dl>
<p> As a source of data, Scale also supports the following standard Motif targets:</p>
<dl COMPACT>
<dt><code>BACKGROUND</code></p>
<dd>The widget transfers <code>XmNbackground</code> as type <code>PIXEL</code>.</p>
<dt><code>CLASS</code></p>
<dd>The widget finds the first shell in the widget hierarchy that has a <code>WM_CLASS</code> property and transfers the contents as text in the current locale.</p>
<dt><code>CLIENT_WINDOW</code></p>
<dd>The widget finds the first shell in the widget hierarchy and transfers its window as type <code>WINDOW</code>.</p>
<dt><code>COLORMAP</code></p>
<dd>The widget transfers <code>XmNcolormap</code> as type <code>COLORMAP</code>.</p>
<dt><code>FOREGROUND</code></p>
<dd>The widget transfers <code>XmNforeground</code> as type <code>PIXEL</code>.</p>
<dt><code>NAME</code></p>
<dd>The widget finds the first shell in the widget hierarchy that has a <code>WM_NAME</code> property and transfers the contents as text in the current locale.</p>
<dt><code>TARGETS</code></p>
<dd>The widget transfers, as type <code>ATOM</code>, a list of the targets it supports. These include the standard targets in this list. These also include <code>STRING</code>, <code>COMPOUND_TEXT</code> and <code>UTF8_STRING</code>.</p>
<dt><code>TIMESTAMP</code></p>
<dd>The widget transfers the timestamp used to acquire the selection as type <code>INTEGER</code>.</p>
<dt><code>_MOTIF_RENDER_TABLE</code></p>
<dd>The widget transfers <code>XmNrenderTable</code> if it exists, or else the default text render table, as type <code>STRING</code>.</p>
<dt><code>_MOTIF_ENCODING_REGISTRY</code></p>
<dd>The widget transfers its encoding registry as type <code>STRING</code>. The value is a list of NULL separated items in the form of tag encoding pairs. This target symbolizes the transfer target for the Motif Segment Encoding Registry. Widgets and applications can use this Registry to register text encoding formats for specified render table tags. Applications access this Registry by calling <code>XmRegisterSegmentEncoding</code> and <code>XmMapSegmentEncoding</code>.</dl>
<h3>Descendants</h3>
<p>Scale automatically creates the descendants shown in the following table. An application can use <code>XtNameToWidget</code> to gain access to the named descendant. In addition, a user or an application can use the named descendant when specifying resource values. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td><code>Named Descendant</code></td>
<td><code>Class</code></td>
<td><code>Identity</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>Scrollbar</code></td>
<td><code>XmScrollBar</code></td>
<td>scroll bar
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>Title</code></td>
<td><code>XmLabelGadget</code></td>
<td>title of scale
</td>
</tr>
<tr VALIGN=top>
<td>
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
<h3>Classes</h3>
<p>Scale inherits behavior, resources, and traits from <code>Core</code>, <code>Composite</code>, <code>Constraint</code>, and <code>XmManager</code> classes. </p>
<p> The class pointer is <code>xmScaleWidgetClass</code>. </p>
<p> The class name is <code>XmScale</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmScale Resource Set</code>
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
<td>XmNdecimalPoints</td>
<td>XmCDecimalPoints</td>
<td>short</td>
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
<td>XmNdragCallback</td>
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
<td>XmNeditable</td>
<td>XmCEditable</td>
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
<td>XmNmaximum</td>
<td>XmCMaximum</td>
<td>int</td>
<td>100</td>
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
<td>XmNminimum</td>
<td>XmCMinimum</td>
<td>int</td>
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
<td>XmNorientation</td>
<td>XmCOrientation</td>
<td>unsigned char</td>
<td>XmVERTICAL</td>
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
<td>XmNprocessingDirection</td>
<td>XmCProcessingDirection</td>
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
<td>XmNscaleHeight</td>
<td>XmCScaleHeight</td>
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
<td>XmNscaleMultiple</td>
<td>XmCScaleMultiple</td>
<td>int</td>
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
<td>XmNscaleWidth</td>
<td>XmCScaleWidth</td>
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
<td>XmNshowArrows</td>
<td>XmCShowArrows</td>
<td>XtEnum</td>
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
<td>XmNshowValue</td>
<td>XmCShowValue</td>
<td>XtEnum</td>
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
<td>XmNsliderMark</td>
<td>XmCSliderMark</td>
<td>XtEnum</td>
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
<td>XmNsliderVisual</td>
<td>XmCSliderVisual</td>
<td>XtEnum</td>
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
<td>XmNslidingMode</td>
<td>XmCSlidingMode</td>
<td>XtEnum</td>
<td>XmSLIDER</td>
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
<td>XmNtitleString</td>
<td>XmCTitleString</td>
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
<td>XmNvalue</td>
<td>XmCValue</td>
<td>int</td>
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
<dl COMPACT>
<dt><code>XmNconvertCallback</code></p>
<dd>Specifies a list of callbacks called when the Scale is asked to convert a selection. The type of the structure whose address is passed to these callbacks is <code>XmConvertCallbackStruct</code>. The reason is <code>XmCR_OK</code>.</p>
<dt><code>XmNdecimalPoints</code></p>
<dd>Specifies the number of decimal points to shift the slider value when displaying it. For example, a slider value of 2,350 and an <code>XmdecimalPoints</code> value of 2 results in a display value of 23.50. The value must not be negative.</p>
<dt><code>XmNdragCallback</code></p>
<dd>Specifies the list of callbacks that is called when the slider position changes as the slider is being dragged. The reason sent by the callback is <code>XmCR_DRAG</code>.</p>
<dt><code>XmNeditable</code></p>
<dd>Specifies how the Scale scrollbar will react to user input. This resource can be True or False values, as follows:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>True</code></p>
<dd>Allows the scrollbar to be sensitive to user input. This is the default value.</p>
<dt><code>False</code></p>
<dd>Makes the Scale scrollbar insensitive to user input. The visual is not greyed out. This value would mostly be used in <code>XmTHERMOMETER</code> mode.</dl>
</dl>
<dd>When <code>XmNeditable</code> is used on a widget it sets the dropsite to <code>XmDROP_SITE_ACTIVE</code>.</p>
<dt><code>XmNfontList</code></p>
<dd>Specifies the font list to use for the title text string specified by <code>XmNtitleString</code>, and the label displayed when <code>XmNshowValue</code> is True. The font list is an obsolete structure, and is retained only for compatibility with earlier releases of Motif. See the <code>XmNrenderTable</code> resource.</p>
<dt><code>XmNhighlightOnEnter</code></p>
<dd>Specifies whether the highlighting rectangle is drawn when the cursor moves into the widget. If the shell&#8217;s focus policy is <code>XmEXPLICIT</code>, this resource is ignored, and the widget is highlighted when it has the focus. If the shell&#8217;s focus policy is <code>XmPOINTER</code> and if this resource is True, the highlighting rectangle is drawn when the the cursor moves into the widget. If the shell&#8217;s focus policy is <code>XmPOINTER</code> and if this resource is False, the highlighting rectangle is not drawn when the the cursor moves into the widget. The default is False.</p>
<dt><code>XmNhighlightThickness</code></p>
<dd>Specifies the size of the slider&#8217;s border drawing rectangle used for enter window and traversal highlight drawing.</p>
<dt><code>XmNmaximum</code></p>
<dd>Specifies the slider&#8217;s maximum value. <code>XmNmaximum</code> must be greater than <code>XmNminimum</code>.</p>
<dt><code>XmNminimum</code></p>
<dd>Specifies the slider&#8217;s minimum value. <code>XmNmaximum</code> must be greater than <code>XmNminimum</code>.</p>
<dt><code>XmNorientation</code></p>
<dd>Displays Scale vertically or horizontally. This resource can have values of <code>XmVERTICAL</code> and <code>XmHORIZONTAL</code>.</p>
<dt><code>XmNprocessingDirection</code></p>
<dd>Specifies whether the value for <code>XmNmaximum</code> is on the right or left side of <code>XmNminimum</code> for horizontal Scales or above or below <code>XmNminimum</code> for vertical Scales. This resource can have values of <code>XmMAX_ON_TOP, XmMAX_ON_BOTTOM, XmMAX_ON_LEFT</code>, and <code>XmMAX_ON_RIGHT</code>. If the Scale is oriented vertically, the default value is <code>XmMAX_ON_TOP</code>. If the XmScale is oriented horizontally, the default value depends on the <code>XmNlayoutDirection</code> resource of the widget.</p>
<dt><code>XmNrenderTable</code></p>
<dd>Specifies the render table to use for the title text string specified by <code>XmNtitleString</code>, and the label displayed when <code>XmNshowValue</code> is True. If this value is NULL at initialization, the parent hierarchy is searched for an ancestor that holds the <code>XmQTspecifyRenderTable</code> trait. If such an ancestor is found, the render table is initialized to the <code>XmLABEL_RENDER_TABLE</code> value of the ancestor widget. If no such ancestor is found, the default is implementation dependent. If a font list (<code>XmNfontList</code>) and a render table are both specified, the render table will take precedence. Refer to <code><a href="/docs/linux/man/3-xmrendertable/">XmRenderTable</a></code>(3) for more information on the creation and structure of a render table.</p>
<dt><code>XmNscaleHeight</code></p>
<dd>Specifies the height of the slider area. The value should be in the specified unit type (the default is pixels). If no value is specified a default height is computed.</p>
<dt><code>XmNscaleMultiple</code></p>
<dd>Specifies the amount to move the slider when the user takes an action that moves the slider by a multiple increment. The default is (<code>XmNmaximum</code> &#8211; <code>XmNminimum</code>) divided by 10, with a minimum of 1.</p>
<dt><code>XmNscaleWidth</code></p>
<dd>Specifies the width of the slider area. The value should be in the specified unit type (the default is pixels). If no value is specified a default width is computed.</p>
<dt><code>XmNshowArrows</code></p>
<dd>Specifies whether the arrows are displayed and how they are to be displayed. This resource can take the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmEACH_SIDE</code></p>
<dd>Indicates that one arrow is displayed on each end of the ScrollBar slider.</p>
<dt><code>XmMAX_SIDE</code></p>
<dd>Indicates that one arrow is displayed on the <code>XmNmaximum</code> side of the ScrollBar slider.</p>
<dt><code>XmMIN_SIDE</code></p>
<dd>Indicates that one arrow is displayed on the <code>XmNminimum</code> side of the ScrollBar slider.</p>
<dt><code>XmNONE</code></p>
<dd>Indicates that no arrows are displayed.</dl>
</dl>
<dd><code>XmNONE</code> is the default value.</p>
<dt><code>XmNshowValue</code></p>
<dd>Specifies whether a label for the current slider value should be displayed next to the slider. If the value is <code>XmNEAR_SLIDER</code>, the current slider value is displayed. If the value is <code>XmNONE</code>, no slider value is displayed. If the value is <code>XmNEAR_BORDER</code>, the current slider value is displayed near the border.</p>
<dt><code>XmNsliderMark</code></p>
<dd>Specifies the shape the slider is to be displayed in. This resource can take the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmETCHED_LINE</code></p>
<dd>Specifies the slider as an etched line. This is the default when <code>XmNslidingMode</code> is <code>XmSLIDER</code>.</p>
<dt><code>XmNONE</code></p>
<dd>Specifies the slider as a foregrounded rectangle. This is the default when <code>XmNslidingMode</code> is <code>XmTHERMOMETER</code> and the Scale scrollbar is insensitive to user input (<code>XmNeditable</code> is <code>False</code>.</p>
<dt><code>XmROUND_MARK</code></p>
<dd>Specifies the slider as a shadowed circle. This is the default when <code>XmNslidingMode</code> is <code>XmTHERMOMETER</code> and the Scale scrollbar is sensitive to user input (<code>XmNeditable</code> is <code>True</code>.</p>
<dt><code>XmTHUMB_MARK</code></p>
<dd>Specifies the slider as a series of three etched lines centered in the middle of the slider.</dl>
</dl>
<dt><code>XmNslidingMode</code></p>
<dd>Specifies the mode the slider works in. There are two possible modes:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmSLIDER</code></p>
<dd>Allows the slider to move freely between the minimum and maximum ends of the scale. This is the default value.</p>
<dt><code>XmTHERMOMETER</code></p>
<dd>Forces the slider to be anchored to one side of the trough area.</dl>
</dl>
<dt><code>XmNsliderVisual</code></p>
<dd>Specifies the color of the slider visual. This resource can take the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmBACKGROUND_COLOR</code></p>
<dd>Specifies that the slider visual is in the background color.</p>
<dt><code>XmFOREGROUND_COLOR</code></p>
<dd>Specifies that the slider visual is in the foreground color.</p>
<dt><code>XmSHADOWED_BACKGROUND</code></p>
<dd>Specifies that the slider visual is in the background color, with a shadow. This is the default when the <code>XmNslidingModel</code> resource is <code>XmSLIDER</code>.</p>
<dt><code>XmTROUGH_COLOR</code></p>
<dd>Specifies that the slider visual is in the trough color. This is the default when the <code>XmNslidingModel</code> resource is <code>XmTHERMOMETER</code>.</dl>
</dl>
<dt><code>XmNtitleString</code></p>
<dd>Specifies the title text string to appear in the Scale widget window.</p>
<dt><code>XmNvalue</code></p>
<dd>Specifies the slider&#8217;s current position along the scale, between <code>XmNminimum</code> and <code>XmNmaximum</code>. The value is constrained to be within these inclusive bounds. The initial value of this resource is the larger of 0 (zero) and <code>XmNminimum</code>.</p>
<dt><code>XmNvalueChangedCallback</code></p>
<dd>Specifies the list of callbacks that is called when the value of the slider has changed. The reason sent by the callback is <code>XmCR_VALUE_CHANGED</code>.</dl>
<h3>Inherited Resources</h3>
<p>Scale inherits behavior and resources from the superclasses described in the following tables. For a complete description of each resource, refer to the reference page for that superclass. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmManager Resource Set</code>
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
<td>XmNinitialFocus</td>
<td>XmCInitialFocus</td>
<td>Widget</td>
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
<td>XmTAB_GROUP</td>
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
<td>XmNstringDirection</td>
<td>XmCStringDirection</td>
<td>XmStringDirection</td>
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
<td ALIGN=center COLSPAN=5><code>Composite Resource Set</code>
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
<td>XmNchildren</td>
<td>XmCReadOnly</td>
<td>WidgetList</td>
<td>NULL</td>
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
<td>XmNinsertPosition</td>
<td>XmCInsertPosition</td>
<td>XtOrderProc</td>
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
<td>XmNnumChildren</td>
<td>XmCReadOnly</td>
<td>Cardinal</td>
<td>0</td>
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
<p>A pointer to the following structure is passed to the <code>XmNdragCallback</code> and <code>XmNvalueChangedCallback</code> procedures: </p>
<pre>typedef struct
{
 int <i>reason</i>;
 XEvent <i>* event</i>;
 int <i>value</i>;
} XmScaleCallbackStruct;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the callback</p>
<dt><i>value</i></p>
<dd>Is the new slider value</dl>
<p> A pointer to the following structure is passed to the <code>XmNconvertCallback</code> procedures: </p>
<pre>typedef struct
{
 int <i>reason</i>;
 XEvent *<i>event</i>;
 Atom <i>selection</i>;
 Atom <i>target</i>;
 XtPointer <i>source_data</i>;
 XtPointer <i>location_data</i>;
 int <i>flags</i>;
 XtPointer <i>parm</i>;
 int <i>parm_format</i>;
 unsigned long <i>parm_length</i>;
 int <i>status</i>;
 XtPointer <i>value</i>;
 Atom <i>type</i>;
 int <i>format</i>;
 unsigned long <i>length</i>;
} XmConvertCallbackStruct;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked.</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the callback. It can be NULL.</p>
<dt><i>selection</i></p>
<dd>Indicates the selection for which conversion is being requested. Possible values are <code>CLIPBOARD</code>, <code>PRIMARY</code>, <code>SECONDARY</code>, and <code>_MOTIF_DROP</code>.</p>
<dt><i>target</i></p>
<dd>Indicates the conversion target.</p>
<dt><i>source_data</i></p>
<dd>Contains information about the selection source. When the selection is <code>_MOTIF_DROP</code>, <i>source_data</i> is the DragContext. Otherwise, it is NULL.</p>
<dt><code>location_data</code></p>
<dd>Contains information about the location of data to be converted. If the value is NULL, the data to be transferred consists of the widget&#8217;s current selection.</p>
<dt><i>flags</i></p>
<dd>Indicates the status of the conversion. Following are the possible values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmCONVERTING_NONE</code></p>
<dd>This flag is currently unused.</p>
<dt><code>XmCONVERTING_PARTIAL</code></p>
<dd>The target widget was able to be converted, but some data was lost.</p>
<dt><code>XmCONVERTING_SAME</code></p>
<dd>The conversion target is the source of the data to be transferred.</p>
<dt><code>XmCONVERTING_TRANSACT</code></p>
<dd>This flag is currently unused.</dl>
</dl>
<dt><i>parm</i></p>
<dd>Contains parameter data for this target. If no parameter data exists, the value is NULL.</p>
<dd>When <i>selection</i> is <code>CLIPBOARD</code> and <i>target</i> is <code>_MOTIF_CLIPBOARD_TARGETS</code> or <code>_MOTIF_DEFERRED_CLIPBOARD_TARGETS</code>, the value is the requested operation (<code>XmCOPY</code>, <code>XmMOVE</code>, or <code>XmLINK</code>).</p>
<dt><i>parm_format</i></p>
<dd>Specifies whether the data in <i>parm</i> should be viewed as a list of <i>char</i>, <i>short</i>, or <i>long</i> quantities. Possible values are 0 (when <i>parm</i> is NULL), 8 (when the data in <i>parm</i> should be viewed as a list of <i>char</i>s), 16 (when the data in <i>parm</i> should be viewed as a list of <i>short</i>s), or 32 (when the data in <i>parm</i> should be viewed as a list of <i>long</i>s). Note that <i>parm_format</i> symbolizes a data type, not the number of bits in each list element. For example, on some machines, a <i>parm_format</i> of 32 means that the data in <i>parm</i> should be viewed as a list of 64-bit quantities, not 32-bit quantities.</p>
<dt><i>parm_length</i></p>
<dd>Specifies the number of elements of data in <i>parm</i>, where each element has the size specified by <i>parm_format</i>. When <i>parm</i> is NULL, the value is 0.</p>
<dt><i>status</i></p>
<dd>An IN/OUT member that specifies the status of the conversion. The initial value is <code>XmCONVERT_DEFAULT</code>. The callback procedure can set this member to one of the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmCONVERT_DEFAULT</code></p>
<dd>This value means that the widget class conversion procedure, if any, is called after the callback procedures return. If the widget class conversion procedure produces any data, it overwrites the data provided by the callback procedures in the <i>value</i> member.</p>
<dt><code>XmCONVERT_MERGE</code></p>
<dd>This value means that the widget class conversion procedure, if any, is called after the callback procedures return. If the widget class conversion procedure produces any data, it appends its data to the data provided by the callback procedures in the <i>value</i> member. This value is intended for use with targets that result in lists of data, such as <code>TARGETS</code>.</p>
<dt><code>XmCONVERT_DONE</code></p>
<dd>This value means that the callback procedure has successfully finished the conversion. The widget class conversion procedure, if any, is not called after the callback procedures return.</p>
<dt><code>XmCONVERT_REFUSE</code></p>
<dd>This value means that the callback procedure has terminated the conversion process without completing the requested conversion. The widget class conversion procedure, if any, is not called after the callback procedures return.</dl>
</dl>
<dt><i>value</i></p>
<dd>An IN/OUT parameter that contains any data that the callback procedure produces as a result of the conversion. The initial value is NULL. If the callback procedure sets this member, it must ensure that the <i>type</i>, <i>format</i>, and <i>length</i> members correspond to the data in <i>value</i>. The callback procedure is responsible for allocating, but not for freeing, memory when it sets this member.</p>
<dt><i>type</i></p>
<dd>An IN/OUT parameter that indicates the type of the data in the <i>value</i> member. The initial value is <code>INTEGER</code>.</p>
<dt><i>format</i></p>
<dd>An IN/OUT parameter that specifies whether the data in <i>value</i> should be viewed as a list of <i>char</i>, <i>short</i>, or <i>long</i> quantities. The initial value is 8. The callback procedure can set this member to 8 (for a list of <i>char</i>), 16 (for a list of <i>short</i>), or 32 (for a list of <i>long</i>).</p>
<dt><i>length</i></p>
<dd>An IN/OUT member that specifies the number of elements of data in <i>value</i>, where each element has the size symbolized by <i>format</i>. The initial value is 0.</dl>
<h3>Behavior</h3>
<p>XmScale has the following behavior:</p>
<dl COMPACT>
<dt><code>&lt;Btn1Down&gt;</code>&nbsp;<wbr>or&nbsp;<wbr><code>&lt;Btn2Down&gt;</code>:</p>
<dd><code>In the region between an end of the Scale and the slider</code>: Moves the slider by one multiple increment in the direction of the end of the Scale and calls the <code>XmNvalueChangedCallback</code> callbacks. If <code>XmNprocessingDirection</code> is <code>XmMAX_ON_RIGHT</code> or <code>XmMAX_ON_BOTTOM</code>, movement toward the right or bottom increments the Scale value, and movement toward the left or top decrements the Scale value. If <code>XmNprocessingDirection</code> is <code>XmMAX_ON_LEFT</code> or <code>XmMAX_ON_TOP</code>, movement toward the right or bottom decrements the Scale value, and movement toward the left or top increments the Scale value. If the button is held down longer than a delay period, the slider is moved again by the same increment and the same callbacks are called.</p>
<dd><code>In slider:</code> Activates the interactive dragging of the slider.</p>
<dt><code>&lt;Btn2Down&gt;</code>&nbsp;<wbr>in value label:</p>
<dd>Drags the contents of the label showing the current slider value. This action sets the <code>XmNconvertProc</code> of the DragContext to a function that calls the <code>XmNconvertCallback</code> procedures, possibly multiple times, for the <code>_MOTIF_DROP</code> selection.</p>
<dt><code>&lt;Btn1Motion&gt;</code>&nbsp;<wbr>or&nbsp;<wbr><code>&lt;Btn2Motion&gt;</code>:</p>
<dd>If the button press occurs within the slider, the subsequent motion events move the slider to the position of the pointer and call the callbacks for <code>XmNdragCallback</code>.</p>
<dt><code>&lt;Btn1Up&gt;</code>&nbsp;<wbr>or&nbsp;<wbr><code>&lt;Btn2Up&gt;</code>:</p>
<dd>If the button press occurs within the slider and the slider position is changed, the callbacks for <code>XmNvalueChangedCallback</code> are called.</p>
<dt><code>&lt;Ctrl&gt;</code><code>&lt;Btn1Down&gt;</code>:</p>
<dd><code>In the region between an end of the Scale and the slider</code>: Moves the slider to that end of the Scale and calls the <code>XmNvalueChangedCallback</code> callbacks. If <code>XmNprocessingDirection</code> is <code>XmMAX_ON_RIGHT</code> or <code>XmMAX_ON_BOTTOM</code>, movement toward the right or bottom increments the Scale value, and movement toward the left or top decrements the Scale value. If <code>XmNprocessingDirection</code> is <code>XmMAX_ON_LEFT</code> or <code>XmMAX_ON_TOP</code>, movement toward the right or bottom decrements the Scale value, and movement toward the left or top increments the Scale value.</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfUp&gt;</code>:</p>
<dd>For vertical Scales, moves the slider up one increment and calls the <code>XmNvalueChangedCallback</code> callbacks. If <code>XmNprocessingDirection</code> is <code>XmMAX_ON_TOP</code>, movement toward the top increments the Scale value. If <code>XmNprocessingDirection</code> is <code>XmMAX_ON_BOTTOM</code>, movement toward the top decrements the Scale value.</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfDown&gt;</code>:</p>
<dd>For vertical Scales, moves the slider down one increment and calls the <code>XmNvalueChangedCallback</code> callbacks. If <code>XmNprocessingDirection</code> is <code>XmMAX_ON_BOTTOM</code>, movement toward the bottom increments the Scale value. If <code>XmNprocessingDirection</code> is <code>XmMAX_ON_TOP</code>, movement toward the bottom decrements the Scale value.</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfLeft&gt;</code>:</p>
<dd>For horizontal Scales, moves the slider one increment to the left and calls the <code>XmNvalueChangedCallback</code> callbacks. If <code>XmNprocessingDirection</code> is <code>XmMAX_ON_LEFT</code>, movement toward the left increments the Scale value. If <code>XmNprocessingDirection</code> is <code>XmMAX_ON_RIGHT</code>, movement toward the left decrements the Scale value.</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfRight&gt;</code>:</p>
<dd>For horizontal Scales, moves the slider one increment to the right and calls the <code>XmNvalueChangedCallback</code> callbacks. If <code>XmNprocessingDirection</code> is <code>XmMAX_ON_RIGHT</code>, movement toward the right increments the Scale value. If <code>XmNprocessingDirection</code> is <code>XmMAX_ON_LEFT</code>, movement toward the right decrements the Scale value.</p>
<dt><code>&lt;Ctrl&gt;</code><code>&lt;Key&gt;</code><code>&lt;osfUp&gt;</code>&nbsp;<wbr>or&nbsp;<wbr><code>&lt;Key&gt;</code><code>&lt;osfPageUp&gt;</code>:</p>
<dd>For vertical Scales, moves the slider up one multiple increment and calls the <code>XmNvalueChangedCallback</code> callbacks. If <code>XmNprocessingDirection</code> is <code>XmMAX_ON_TOP</code>, movement toward the top increments the Scale value. If <code>XmNprocessingDirection</code> is <code>XmMAX_ON_BOTTOM</code>, movement toward the top decrements the Scale value.</p>
<dt><code>&lt;Ctrl&gt;</code><code>&lt;Key&gt;</code><code>&lt;osfDown&gt;</code>&nbsp;<wbr>or&nbsp;<wbr><code>&lt;Key&gt;</code><code>&lt;osfPageDown&gt;</code>:</p>
<dd>For vertical Scales, moves the slider down one multiple increment and calls the <code>XmNvalueChangedCallback</code> callbacks. If <code>XmNprocessingDirection</code> is <code>XmMAX_ON_BOTTOM</code>, movement toward the bottom increments the Scale value. If <code>XmNprocessingDirection</code> is <code>XmMAX_ON_TOP</code>, movement toward the bottom decrements the Scale value.</p>
<dt><code>&lt;Ctrl&gt;</code><code>&lt;Key&gt;</code><code>&lt;osfLeft&gt;</code>&nbsp;<wbr>or&nbsp;<wbr><code>&lt;Key&gt;</code><code>&lt;osfPageLeft&gt;</code>:</p>
<dd>For horizontal Scales, moves the slider one multiple increment to the left and calls the <code>XmNvalueChangedCallback</code> callbacks. If <code>XmNprocessingDirection</code> is <code>XmMAX_ON_LEFT</code>, movement toward the left increments the Scale value. If <code>XmNprocessingDirection</code> is <code>XmMAX_ON_RIGHT</code>, movement toward the left decrements the Scale value.</p>
<dt><code>&lt;Ctrl&gt;</code><code>&lt;Key&gt;</code><code>&lt;osfRight&gt;</code>&nbsp;<wbr>or&nbsp;<wbr><code>&lt;Key&gt;</code><code>&lt;osfPageRight&gt;</code>:</p>
<dd>For horizontal Scales, moves the slider one multiple increment to the right and calls the <code>XmNvalueChangedCallback</code> callbacks. If <code>XmNprocessingDirection</code> is <code>XmMAX_ON_RIGHT</code>, movement toward the right increments the Scale value. If <code>XmNprocessingDirection</code> is <code>XmMAX_ON_LEFT</code>, movement toward the right decrements the Scale value.</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfBeginLine&gt;</code>&nbsp;<wbr>or&nbsp;<wbr><code>&lt;Key&gt;</code><code>&lt;osfBeginData&gt;</code>:</p>
<dd>Moves the slider to the minimum value and calls the <code>XmNvalueChangedCallback</code> callbacks.</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfEndLine&gt;</code>&nbsp;<wbr>or&nbsp;<wbr><code>&lt;Key&gt;</code><code>&lt;osfEndData&gt;</code>:</p>
<dd>Moves the slider to the maximum value and calls the <code>XmNvalueChangedCallback</code> callbacks.</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfNextField&gt;</code>:</p>
<dd>Traverses to the first item in the next tab group. If the current tab group is the last entry in the tab group list, it wraps to the beginning of the tab group list.</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfPrevField&gt;</code>:</p>
<dd>Traverses to the first item in the previous tab group. If the beginning of the tab group list is reached, it wraps to the end of the tab group list.</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfHelp&gt;</code>:</p>
<dd>Calls the callbacks for <code>XmNhelpCallback</code> if any exist. If there are no help callbacks for this widget, this action calls the help callbacks for the nearest ancestor that has them.</dl>
<h3>Virtual Bindings</h3>
<p>The bindings for virtual keys are vendor specific. For information about bindings for virtual buttons and keys, see <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-composite/">Composite</a></code>(3), <code><a href="/docs/linux/man/3-constraint/">Constraint</a></code>(3), <code><a href="/docs/linux/man/3-core/">Core</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatescale/">XmCreateScale</a></code>(3), <code><a href="/docs/linux/man/3-xmmanager/">XmManager</a></code>(3), <code><a href="/docs/linux/man/3-xmscalegetvalue/">XmScaleGetValue</a></code>(3), <code><a href="/docs/linux/man/3-xmscalesetvalue/">XmScaleSetValue</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatescale/">XmVaCreateScale</a></code>(3), and <code><a href="/docs/linux/man/3-xmvacreatemanagedscale/">XmVaCreateManagedScale</a></code>(3).</p>
