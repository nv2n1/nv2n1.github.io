---
title: "xmlabelgadget(3)"
name: "xmlabelgadget"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmlabelgadget/"
description: "XmLabelGadget — The LabelGadget widget class"
---

<p><code>XmLabelGadget</code> &#8212; The LabelGadget widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/LabelG.h&gt;</pre>
<h2>Description</h2>
<p>LabelGadget is an instantiable widget and is also used as a superclass for other button gadgets, such as PushButtonGadget and ToggleButtonGadget. </p>
<p> LabelGadget can contain either text or a pixmap. LabelGadget text is a compound string. Refer to the <i>Motif Programmer&#8217;s</i> Guide for more information on compound strings. The text can be multilingual, multiline, and/or multifont. When a LabelGadget is insensitive, its text is stippled, or the user-supplied insensitive pixmap is displayed. </p>
<p> LabelGadget supports both accelerators and mnemonics primarily for use in LabelGadget subclass widgets that are contained in menus. Mnemonics are available in a menu system when the button is visible. Accelerators in a menu system are accessible even when the button is not visible. The LabelGadget displays the mnemonic by underlining the first matching character in the text string. The accelerator is displayed as a text string adjacent to the label text or pixmap, depending on the layout direction. </p>
<p> LabelGadget consists of many margin fields surrounding the text or pixmap. These margin fields are resources that may be set by the user, but LabelGadget subclasses and Manager parents also modify some of these fields. They tend to modify the <code>XmNmarginLeft</code>, <code>XmNmarginRight</code>, <code>XmNmarginTop</code>, and <code>XmNmarginBottom</code> resources and leave the <code>XmNmarginWidth</code> and <code>XmNmarginHeight</code> resources as set by the application. </p>
<p> LabelGadget takes into account <code>XmNshadowThickness</code> in determining its layout but does not draw the shadow. That is, if <code>XmNshadowThickness</code> is greater than 0 (zero), LabelGadget leaves space for the shadow, but the shadow does not appear. </p>
<p> In a LabelGadget, <code>XmNtraversalOn</code> and <code>XmNhighlightOnEnter</code> are forced to False inside Popup menu panes, Pulldown menu panes, and OptionMenus. Otherwise these resources default to False. </p>
<p> LabelGadget uses the <code>XmQTmenuSystem</code> and <code>XmQTspecifyRenderTable</code> traits, and holds the <code>XmQTaccessTextual</code>, <code>XmQTcareParentVisual</code>, <code>XmQTmenuSavvy</code>, and <code>XmQTtransfer</code> traits.</p>
<h3>Data Transfer Behavior</h3>
<p>LabelGadget and it subclasses, except when used in a menu system, support dragging of the label contents from the LabelGadget. However, the label contents are draggable only if the <code>XmNenableUnselectableDrag</code> resource of <code>XmDisplay</code> is set to True. </p>
<p> As a source of data, LabelGadget and its subclasses support the following targets and associated conversions of data to these targets:</p>
<dl COMPACT>
<dt><i>locale</i></p>
<dd>If the <i>locale</i> target matches the widget&#8217;s locale, the widget transfers <code>XmNlabelString</code> in the encoding of the locale. This target is supported only when <code>XmNlabelType</code> is <code>XmSTRING</code> or <code>XmPIXMAP_AND_STRING</code>.</p>
<dt><code>COMPOUND_TEXT</code></p>
<dd>The widget transfers <code>XmNlabelString</code> as type <code>COMPOUND_TEXT</code>. This target is supported only when <code>XmNlabelType</code> is <code>XmSTRING</code> or <code>XmPIXMAP_AND_STRING.</p>
<dt>UTF8_STRING</code></p>
<dd>The widget transfers <code>XmNlabelString</code> as type <code>UTF8_STRING</code>. This target is supported only when <code>XmNlabelType</code> is <code>XmSTRING</code> of <code>XmPIXMAP_AND_STRING</code>.</p>
<dt><code>PIXMAP</code></p>
<dd>The widget transfers <code>XmNlabelPixmap</code> as type <code>DRAWABLE</code>. This target is supported when <code>XmNlabelType</code> is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code>.</p>
<dt><code>STRING</code></p>
<dd>The widget transfers <code>XmNlabelString</code> as type <code>STRING</code>. This target is supported when <code>XmNlabelType</code> is <code>XmSTRING</code> or <code>XmPIXMAP_AND_STRING</code>.</p>
<dt><code>TEXT</code></p>
<dd>If <code>XmNlabelString</code> is fully convertible to the encoding of the locale, the widget transfers <code>XmNlabelString</code> in the encoding of the locale. Otherwise, the widget transfers <code>XmNlabelString</code> as type <code>COMPOUND_TEXT</code>. This target is supported when <code>XmNlabelType</code> is <code>XmSTRING</code> or <code>XmPIXMAP_AND_STRING</code>.</p>
<dt><code>_MOTIF_CLIPBOARD_TARGETS</code></p>
<dd>The widget transfers, as type <code>ATOM</code>, a list of the targets it supports for the <code>CLIPBOARD</code> selection. When <code>XmNlabelType</code> is <code>XmSTRING</code> or <code>XmPIXMAP_AND_STRING</code>, these include the following targets:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd><code>_MOTIF_COMPOUND_STRING</code></p>
<dt> &bull;</p>
<dd><code>COMPOUND_TEXT</code></p>
<dt> &bull;</p>
<dd><code>UTF8_STRING</code></p>
<dt> &bull;</p>
<dd>The encoding of the locale, if <code>XmNlabelString</code> is fully convertible to the encoding of the locale</p>
<dt> &bull;</p>
<dd><code>STRING</code>, if <code>XmNlabelString</code> is fully convertible to <code>STRING</code></dl>
</dl>
<dd>When <code>XmNlabelType</code> is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code>, the targets include <code>PIXMAP</code>.</p>
<dt><code>_MOTIF_COMPOUND_STRING</code></p>
<dd>The widget transfers <code>XmNlabelString</code> as a compound string in Byte Stream format. This target is supported when <code>XmNlabelType</code> is <code>XmSTRING</code> or <code>XmPIXMAP_AND_STRING</code>.</p>
<dt><code>_MOTIF_EXPORT_TARGETS</code></p>
<dd>The widget transfers, as type <code>ATOM</code>, a list of the targets to be used as the value of the DragContext&#8217;s <code>XmNexportTargets</code> in a drag-and-drop transfer. When <code>XmNlabelType</code> is <code>XmSTRING</code> or <code>XmPIXMAP_AND_STRING</code>, these include <code>_MOTIF_COMPOUND_STRING</code>, <code>COMPOUND_TEXT</code>, <code>UTF8_STRING</code>, the encoding of the locale, <code>STRING</code>, <code>TEXT</code>, <code>BACKGROUND</code>, and <code>FOREGROUND</code>. When <code>XmNlabelType</code> is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code>, these include <code>PIXMAP</code>, <code>BACKGROUND</code>, and <code>FOREGROUND</code>.</dl>
<p> As a source of data, LabelGadget also supports the following standard Motif targets:</p>
<dl COMPACT>
<dt><code>BACKGROUND</code></p>
<dd>The widget transfers the parent&#8217;s <code>XmNbackground</code> as type <code>PIXEL</code>.</p>
<dt><code>CLASS</code></p>
<dd>The widget finds the first shell in the widget hierarchy that has a <code>WM_CLASS</code> property and transfers the contents as text in the current locale.</p>
<dt><code>CLIENT_WINDOW</code></p>
<dd>The widget finds the first shell in the widget hierarchy and transfers its window as type <code>WINDOW</code>.</p>
<dt><code>COLORMAP</code></p>
<dd>The widget transfers the parent&#8217;s <code>XmNcolormap</code> as type <code>COLORMAP</code>.</p>
<dt><code>FOREGROUND</code></p>
<dd>The widget transfers the parent&#8217;s <code>XmNforeground</code> as type <code>PIXEL</code>.</p>
<dt><code>NAME</code></p>
<dd>The widget finds the first shell in the widget hierarchy that has a <code>WM_NAME</code> property and transfers the contents as text in the current locale.</p>
<dt><code>TARGETS</code></p>
<dd>The widget transfers, as type <code>ATOM</code>, a list of the targets it supports. These include the standard targets in this list. When <code>XmNlabelType</code> is <code>XmSTRING</code> or <code>XmPIXMAP_AND_STRING</code>, these also include <code>_MOTIF_COMPOUND_STRING</code>, <code>COMPOUND_TEXT</code>, <code>UTF8_STRING</code>, the encoding of the locale, <code>STRING</code>, and <code>TEXT</code>. When <code>XmNlabelType</code> is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code>, these also include <code>PIXMAP</code>.</p>
<dt><code>TIMESTAMP</code></p>
<dd>The widget transfers the timestamp used to acquire the selection as type <code>INTEGER</code>.</p>
<dt><code>_MOTIF_RENDER_TABLE</code></p>
<dd>The widget transfers <code>XmNrenderTable</code> if it exists, or else the default text render table, as type <code>STRING</code>.</p>
<dt><code>_MOTIF_ENCODING_REGISTRY</code></p>
<dd>The widget transfers its encoding registry as type <code>STRING</code>. The value is a list of NULL separated items in the form of tag encoding pairs. This target symbolizes the transfer target for the Motif Segment Encoding Registry. Widgets and applications can use this Registry to register text encoding formats for specified render table tags. Applications access this Registry by calling <code>XmRegisterSegmentEncoding</code> and <code>XmMapSegmentEncoding</code>.</dl>
<h3>Classes</h3>
<p>LabelGadget inherits behavior, resources, and traits from <code>Object</code>, <code>RectObj</code> and <code>XmGadget</code>. </p>
<p> The class pointer is <code>xmLabelGadgetClass</code>. </p>
<p> The class name is <code>XmLabelGadget</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
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
<dl COMPACT>
<dt><code>XmNaccelerator</code></p>
<dd>Sets the accelerator on a button widget in a menu, which activates a visible or invisible, but managed, button from the keyboard. This resource is a string that describes a set of modifiers and the key that may be used to select the button. The format of this string is identical to that used by the translations manager, with the exception that only a single event may be specified and only <code>KeyPress</code> events are allowed.</p>
<dd>Accelerators for buttons are supported only for PushButtonGadgets and ToggleButtonGadgets in Pulldown and Popup menus.</p>
<dt><code>XmNacceleratorText</code></p>
<dd>Specifies the text displayed for the accelerator. The text is displayed adjacent to the label string or pixmap. The direction of its layout depends on the <code>XmNlayoutDirection</code> resource of the widget. Accelerator text for buttons is displayed only for PushButtonGadgets and ToggleButtonGadgets in Pulldown and Popup Menus.</p>
<dt><code>XmNalignment</code></p>
<dd>Specifies the label alignment for text or pixmap.</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmALIGNMENT_BEGINNING</code> (left alignment)</p>
<dd>Causes the left sides of the lines of text to be vertically aligned with the left edge of the gadget. For a pixmap, its left side is vertically aligned with the left edge of the gadget.</p>
<dt><code>XmALIGNMENT_CENTER</code> (center alignment)</p>
<dd>Causes the centers of the lines of text to be vertically aligned in the center of the gadget. For a pixmap, its center is vertically aligned with the center of the gadget.</p>
<dt><code>XmALIGNMENT_END</code> (right alignment)</p>
<dd>Causes the right sides of the lines of text to be vertically aligned with the right edge of the gadget. For a pixmap, its right side is vertically aligned with the right edge of the gadget.</dl>
</dl>
<dd>The preceding descriptions for text are correct when <code>XmNlayoutDirection</code> is <code>XmLEFT_TO_RIGHT</code>. When that resource is <code>XmRIGHT_TO_LEFT</code>, the descriptions for <code>XmALIGNMENT_BEGINNING</code> and <code>XmALIGNMENT_END</code> are switched.</p>
<dd>If the parent is a RowColumn whose <code>XmNisAligned</code> resource is True, <code>XmNalignment</code> is forced to the same value as the RowColumn&#8217;s <code>XmNentryAlignment</code> if the RowColumn&#8217;s <code>XmNrowColumnType</code> is <code>XmWORK_AREA</code> or if the gadget is a subclass of <code>XmLabelGadget</code>. Otherwise, the default is <code>XmALIGNMENT_CENTER</code>.</p>
<dt><code>XmNfontList</code></p>
<dd>Specifies the font of the text used in the gadget. <code>XmNfontList</code> is obsolete and exists for compatibility with previous releases. You should now use <code>XmNrenderTable</code> instead of <code>XmNfontList</code>. If both are specified, the render table will take precedence. If <code>XmNfontList</code> is NULL at initialization, the parent hierarchy of the widget is searched for an ancestor that is a subclass of the <code>XmBulletinBoard</code>, <code>VendorShell</code>, or <code>XmMenuShell</code> widget class. If such an ancestor is found, the font list is initialized to the <code>XmNbuttonFontList</code> (for button gadget subclasses) or <code>XmNlabelFontList</code> of the ancestor widget. If no such ancestor is found, the default is implementation dependent. Refer to <code><a href="/docs/linux/man/3-xmfontlist/">XmFontList</a></code>(3) for more information on the creation and structure of a font list.</p>
<dt><code>XmNlabelInsensitivePixmap</code></p>
<dd>Specifies a pixmap used as the button face if <code>XmNlabelType</code> is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code> and the button is insensitive. The default value, <code>XmUNSPECIFIED_PIXMAP</code>, displays an empty label.</p>
<dt><code>XmNlabelPixmap</code></p>
<dd>Specifies the pixmap when <code>XmNlabelType</code> is <code>XmPIXMAP</code> or <code>XmPIXMAP_AND_STRING</code>. The default value, <code>XmUNSPECIFIED_PIXMAP</code>, displays an empty label.</p>
<dt><code>XmNlabelString</code></p>
<dd>Specifies the compound string when <code>XmNlabelType</code> is <code>XmSTRING</code> or <code>XmPIXMAP_AND_STRING</code>. If the value of this resource is NULL, it is initialized to name of the gadget converted to a compound string. Refer to <code><a href="/docs/linux/man/3-xmstring/">XmString</a></code>(3) for more information on the creation and the structure of compound strings.</p>
<dt><code>XmNlabelType</code></p>
<dd>Specifies the label type.</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmSTRING</code></p>
<dd>Text displays <code>XmNlabelString</code></p>
<dt><code>XmPIXMAP</code></p>
<dd>Icon data in pixmap displays <code>XmNlabelPixmap</code> or <code>XmNlabelInsensitivePixmap</code> <code>XmPIXMAP_AND_STRING</code> Icon data in pixmap displays <code>XmNlabelPixmap</code> or <code>XmNlabelInsensitivePixmap</code> and text displays <code>XmNlabelString</code></dl>
</dl>
<dt><code>XmNmarginBottom</code></p>
<dd>Specifies the amount of spacing between the bottom of the label text and the top of the bottom margin specified by <code>XmNmarginHeight</code>. This may be modified by LabelGadget&#8217;s subclasses. For example, CascadeButtonGadget may increase this field to make room for the cascade pixmap.</p>
<dt><code>XmNmarginHeight</code></p>
<dd>Specifies an equal amount of spacing above the margin defined by <code>XmNmarginTop</code> and below the margin defined by <code>XmNmarginBottom</code>. <code>XmNmarginHeight</code> specifies the amount of spacing between the top edge of the margin set by <code>XmNmarginTop</code> and the bottom edge of the top shadow, and the amount of spacing between the bottom edge of the margin specified by <code>XmNmarginBottom</code> and the top edge of the bottom shadow.</p>
<dt><code>XmNmarginLeft</code></p>
<dd>Specifies the amount of spacing between the left edge of the label text and the right side of the left margin (specified by <code>XmNmarginWidth</code>). This may be modified by LabelGadget&#8217;s subclasses. For example, ToggleButtonGadget may increase this field to make room for the toggle indicator and for spacing between the indicator and label. Whether this actually applies to the left or right side of the label depends on the value of <code>XmNlayoutDirection</code>.</p>
<dt><code>XmNmarginRight</code></p>
<dd>Specifies the amount of spacing between the right edge of the label text and the left side of the right margin (specified by <code>XmNmarginWidth</code>). This may be modified by LabelGadget&#8217;s subclasses. For example, CascadeButtonGadget may increase this field to make room for the cascade pixmap. Whether this actually applies to the left or right side of the label depends on the value of <code>XmNlayoutDirection</code>.</p>
<dt><code>XmNmarginTop</code></p>
<dd>Specifies the amount of spacing between the top of the label text and the bottom of the top margin specified by <code>XmNmarginHeight</code>. This may be modified by LabelGadget&#8217;s subclasses. For example, CascadeButtonGadget may increase this field to make room for the cascade pixmap.</p>
<dt><code>XmNmarginWidth</code></p>
<dd>Specifies an equal amount of spacing to the left of the margin defined by <code>XmNmarginLeft</code> and to the right of the margin defined by <code>XmNmarginRight</code>. <code>XmNmarginWidth</code> specifies the amount of spacing between the left edge of the margin set by <code>XmNmarginLeft</code> and the right edge of the left shadow, and the amount of spacing between the right edge of the margin specified by <code>XmNmarginRight</code> and the left edge of the right shadow.</p>
<dt><code>XmNmnemonic</code></p>
<dd>Provides the user with an alternate means of activating a button. A button in a MenuBar, a Popup menu pane, or a Pulldown menu pane can have a mnemonic.</p>
<dd>This resource contains a keysym as listed in the X11 keysym table. The first character in the label string that exactly matches the mnemonic in the character set specified in <code>XmNmnemonicCharSet</code> is underlined when the button is displayed.</p>
<dd>When a mnemonic has been specified, the user activates the button by pressing the mnemonic key while the button is visible. If the button is a CascadeButtonGadget in a MenuBar and the MenuBar does not have the focus, the user must use the <code>MAlt</code> modifier while pressing the mnemonic. The user can activate the button by pressing either the shifted or the unshifted mnemonic key.</p>
<dt><code>XmNmnemonicCharSet</code></p>
<dd>Specifies the character set of the mnemonic for the label. The default is <code>XmFONTLIST_DEFAULT_TAG</code>.</p>
<dt><code>XmNpixmapPlacement</code></p>
<dd>The location of the pixmap with respect to the text label. This resource can take one of the following values: <code>XmPIXMAP_TOP</code>, <code>XmPIXMAP_BOTTOM</code>, <code>XmPIXMAP_LEFT</code>, and <code>XmPIXMAP_RIGHT</code>. A type converter has been registered that converts the following strings: &quot;top&quot;, &quot;bottom&quot;, &quot;left&quot;, and &quot;right&quot;.</p>
<dt><code>XmNpixmapTextPadding</code></p>
<dd>The amount of space to be left between the pixmap and the label string.</p>
<dt><code>XmNrecomputeSize</code></p>
<dd>Specifies a Boolean value that indicates whether the gadget shrinks or expands to accommodate its contents (label string or pixmap) as a result of an <code>XtSetValues</code> resource value that would change the size of the gadget. If True, the gadget shrinks or expands to exactly fit the label string or pixmap. If False, the gadget never attempts to change size on its own.</p>
<dt><code>XmNrenderTable</code></p>
<dd>Specifies the render table associated with the <code>labelString</code>. If this value is NULL at initialization, Label searches its parent hierarchy for an ancestor that holds the <code>XmQTspecifyRenderTable</code> trait. If such an ancestor is found, Label initializes <code>XmNrenderTable</code> to the <code>XmLABEL_RENDER_TABLE</code> value of the ancestor widget. Similarly, button subclasses of Label initialize <code>XmNrenderTable</code> to the <code>XmBUTTON_RENDER_TABLE</code> value of the ancestor widget. (Note that all current subclasses of Label are button subclasses.) If no such ancestor is found, the default is implementation dependent. If a font list and a render table are both specified, the render table will take precedence. Refer to <code><a href="/docs/linux/man/3-xmrendertable/">XmRenderTable</a></code>(3) for more information on the creation and structure of a render table.</p>
<dt><code>XmNstringDirection</code></p>
<dd>Is a synthetic resource for setting <code>XmNlayoutDirection</code>. The values for this resource are <code>XmSTRING_DIRECTION_L_TO_R</code> and <code>XmSTRING_DIRECTION_R_TO_L</code>. Refer to the <code>XmNlayoutDirection</code> resource description. The <code>XmNstringDirection</code> resource is obsoleted by <code>XmNlayoutDirection</code>, but is kept here for backward compatibility.</dl>
<h3>Inherited Resources</h3>
<p>LabelGadget inherits behavior and resources from the superclasses described in the following tables. For a complete description of each resource, refer to the reference page for that superclass. </p>
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
<h3>Behavior</h3>
<p>XmLabelGadget includes behavior from XmGadget. Additional XmLabelGadget behavior is described in the following list:</p>
<dl COMPACT>
<dt><code>&lt;Btn2Down&gt;</code>:</p>
<dd>Drags the contents of a LabelGadget, identified when <code>BTransfer</code> is pressed. This action is undefined for LabelGadgets used in a menu system.</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfHelp&gt;</code>:</p>
<dd>In a Popup or Pulldown MenuPane, unposts all menus in the menu hierarchy and, when the shell&#8217;s keyboard focus policy is <code>XmEXPLICIT</code>, restores keyboard focus to the widget that had the focus before the menu system was entered. Calls the callbacks for <code>XmNhelpCallback</code> if any exist. If there are no help callbacks for this widget, this action calls the help callbacks for the nearest ancestor that has them.</p>
<dt><code>&lt;key&gt;</code><code>&lt;osfCancel&gt;</code>:</p>
<dd>In a MenuBar, disarms the CascadeButton and the menu and, when the shell&#8217;s keyboard focus policy is <code>XmEXPLICIT</code>, restores keyboard focus to the widget that had the focus before the menu was entered.</p>
<dd>In a toplevel Pulldown MenuPane from a MenuBar, unposts the menu, disarms the MenuBar CascadeButton and the MenuBar, and, when the shell&#8217;s keyboard focus policy is <code>XmEXPLICIT</code>, restores keyboard focus to the widget that had the focus before the MenuBar was entered. In other Pulldown MenuPanes, unposts the menu.</p>
<dd>In a Popup MenuPane, unposts the menu and, when the shell&#8217;s keyboard focus policy is <code>XmEXPLICIT</code>, restores keyboard focus to the widget from which the menu was posted.</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfDown&gt;</code>:</p>
<dd>If the current menu item has a submenu and is in a MenuBar, then this action posts the submenu, disarms the current menu item, and arms the submenu&#8217;s first traversable menu item.</p>
<dd>If the current menu item is in a MenuPane, then this action disarms the current menu item and arms the item below it. This action wraps within the MenuPane. The direction of the wrapping depends on the <code>XmNlayoutDirection</code> resource.</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfLeft&gt;</code>:</p>
<dd>When the current menu item is in a MenuBar, then this action disarms the current item and arms the MenuBar item to the left. This action wraps within the MenuBar.</p>
<dd>In MenuPanes, if the current menu item is not at the left edge of a MenuPane, this action disarms the current item and arms the item to its left. If the current menu item is at the left edge of a submenu attached to a MenuBar item, then this action unposts the submenu and traverses to the MenuBar item to the left, wrapping if necessary. If that MenuBar item has a submenu, it posts the submenu and arms the first traversable item in the submenu. If the current menu item is at the left edge of a submenu not directly attached to a MenuBar item, then this action unposts the current submenu only.</p>
<dd>In Popup or Torn-off MenuPanes, when the current menu item is at the left edge, this action wraps within the MenuPane. If the current menu item is at the left edge of the MenuPane and not in the top row, this action wraps to the rightmost menu item in the row above. If the current menu item is in the upper, leftmost corner, this action wraps to the tear-off control, if present, or else it wraps to the bottom, rightmost menu item in the MenuPane. The preceding description applies when the <code>XmNlayoutDirection</code> horizontal direction is <code>XmLEFT_TO_RIGHT</code>. If the <code>XmNlayoutDirection</code> horizontal direction is <code>XmRIGHT_TO_LEFT</code>, then the following applies.</p>
<dd>If the current menu item is in a MenuBar, then this action disarms the current item and arms the MenuBar item to the left. This action wraps within the MenuBar.</p>
<dd>In MenuPanes, if the current menu item is a CascadeButton, then this action posts its associated submenu. If the current menu item is not a CascadeButton and is not at the left edge of a MenuPane, this action disarms the current item and arms the item to its left, wrapping if necessary. If the current menu item is not a CascadeButton and is at the left edge of a submenu that is a descendent of a MenuBar, then this action unposts all submenus and traverses to the MenuBar item to the left. If that MenuBar item has a submenu, it posts the submenu and arms the submenu&#8217;s first traversable item.</p>
<dd>In Popup or Torn-off menus, if the current menu item is not a CascadeButton and is at the left edge of a row (except the bottom row), this action wraps to the rightmost menu item in the row below. If the current menu item is not a CascadeButton and is in the bottom, leftmost corner of a Popup or Pulldown MenuPane, this action wraps to the tear-off control, if present, or else it wraps to the top, rightmost menu item of the MenuPane.</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfRight&gt;</code>:</p>
<dd>If the current menu item is in a MenuBar, then this action disarms the current item and arms the MenuBar item to the right. This action wraps within the MenuBar.</p>
<dd>In MenuPanes, if the current menu item is a CascadeButton, then this action posts its associated submenu. If the current menu item is not a CascadeButton and is not at the right edge of a MenuPane, this action disarms the current item and arms the item to its right, wrapping if necessary. If the current menu item is not a CascadeButton and is at the right edge of a submenu that is a descendent of a MenuBar, then this action unposts all submenus and traverses to the MenuBar item to the right. If that MenuBar item has a submenu, it posts the submenu and arms the submenu&#8217;s first traversable item.</p>
<dd>In Popup or Torn-off menus, if the current menu item is not a CascadeButton and is at the right edge of a row (except the bottom row), this action wraps to the leftmost menu item in the row below. If the current menu item is not a CascadeButton and is in the bottom, rightmost corner of a Popup or Pulldown MenuPane, this action wraps to the tear-off control, if present, or else it wraps to the top, leftmost menu item of the MenuPane. The preceding description applies when the <code>XmNlayoutDirection</code> horizontal direction is <code>XmLEFT_TO_RIGHT</code>. If the <code>XmNlayoutDirection</code> horizontal direction is <code>XmRIGHT_TO_LEFT</code>, then the following applies.</p>
<dd>When the current menu item is in a MenuBar, then this action disarms the current item and arms the MenuBar item to the right. This action wraps within the MenuBar.</p>
<dd>In MenuPanes, if the current menu item is not at the right edge of a MenuPane, this action disarms the current item and arms the item to its right. If the current menu item is at the right edge of a submenu attached to a MenuBar item, then this action unposts the submenu and traverses to the MenuBar item to the right, wrapping if necessary. If that MenuBar item has a submenu, it posts the submenu and arms the first traversable item in the submenu. If the current menu item is at the right edge of a submenu not directly attached to a MenuBar item, then this action unposts the current submenu only.</p>
<dd>In Popup or Torn-off MenuPanes, when the current menu item is at the right edge, this action wraps within the MenuPane. If the current menu item is at the right edge of the MenuPane and not in the top row, this action wraps to the leftmost menu item in the row above. If the current menu item is in the upper, rightmost corner, this action wraps to the tear-off control, if present, or else it wraps to the bottom, leftmost menu item in the MenuPane.</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfUp&gt;</code>:</p>
<dd>When the current menu item is in a MenuPane, then this action disarms the current menu item and arms the item above it. This action wraps within the MenuPane. The direction of the wrapping depends on the <code>XmNlayoutDirection</code> resource.</dl>
<h3>Virtual Bindings</h3>
<p>The bindings for virtual keys are vendor specific. For information about bindings for virtual buttons and keys, see <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-object/">Object</a></code>(3), <code><a href="/docs/linux/man/3-rectobj/">RectObj</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatelabelgadget/">XmCreateLabelGadget</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatelabelgadget/">XmVaCreateLabelGadget</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatemanagedlabelgadget/">XmVaCreateManagedLabelGadget</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistcreate/">XmFontListCreate</a></code>(3), <code><a href="/docs/linux/man/3-xmstringcreate/">XmStringCreate</a></code>(3), <code><a href="/docs/linux/man/3-xmstringcreateltor/">XmStringCreateLtoR</a></code>(3), and <code><a href="/docs/linux/man/3-xmgadget/">XmGadget</a></code>(3).</p>
