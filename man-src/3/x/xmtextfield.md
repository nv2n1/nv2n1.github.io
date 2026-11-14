---
title: "xmtextfield(3)"
name: "xmtextfield"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextfield/"
description: "XmTextField — The TextField class"
---

<p><code>XmTextField</code> &#8212; The TextField class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;</pre>
<h2>Description</h2>
<p>The TextField widget provides a single line text editor for customizing both user and programmatic interfaces. It is used for single-line string entry, and forms entry with verification procedures. It provides an application with a consistent editing system for textual data. </p>
<p> TextField provides separate callback lists to verify movement of the insert cursor, modification of the text, and changes in input focus. Each of these callbacks provides the verification function with the widget instance, the event that caused the callback, and a data structure specific to the verification type. From this information, the function can verify if the application considers this to be a legitimate state change and can signal the widget whether to continue with the action. </p>
<p> The user interface tailors a new set of actions. The key bindings have been added for insert cursor movement, deletion, insertion, and selection of text. </p>
<p> TextField allows the user to select regions of text. Selection is based on the model specified in the <i>Inter-Client Communication Conventions Manual</i> (ICCCM). TextField supports primary and secondary selection. </p>
<p> TextField uses the <code>XmQTnavigator</code>, <code>XmQTspecifyRenderTable</code>, and <code>XmQTscrollFrame</code> traits, and holds the <code>XmQTaccessTextual</code> <code>XmQTtransfer</code> traits. </p>
<p> If an application or widget calls the <code>setValue</code> trait method of <code>XmQTaccessTextual</code>, then <code>XmTextField</code> will call <code>XmTextFieldSetString</code> to set the string value.</p>
<h3>Data Transfer Behavior</h3>
<p>TextField supports transfer of the primary, secondary, and clipboard selections and dragging of selected text from the widget. TextField can also be the destination for the primary, secondary, and clipboard selections, and it supports dropping of data being dragged onto the widget. </p>
<p> When the <code>XmNconvertCallback</code> procedures are called, the <code>location_data</code> member of the <code>XmConvertCallbackStruct</code> member is NULL if the selected text is being transferred. If the entire text, not the selected text, is being transferred, the value of this member is the widget ID of the TextField widget. </p>
<p> As a source of data, TextField supports the following targets and associated conversions of data to these targets:</p>
<dl COMPACT>
<dt><code>UTF8_STRING</code></p>
<dd>The widget transfers the selected text as type <code>UTF8_STRING</code>.</p>
<dt><i>locale</i></p>
<dd>If the <i>locale</i> target matches the widget&#8217;s locale, the widget transfers the selected text in the encoding of the locale.</p>
<dt><code>COMPOUND_TEXT</code></p>
<dd>The widget transfers the selected text as type <code>COMPOUND_TEXT</code>.</p>
<dt><code>STRING</code></p>
<dd>The widget transfers the selected text as type <code>STRING</code>.</p>
<dt><code>TEXT</code></p>
<dd>If the selected text is fully convertible to the encoding of the locale, the widget transfers the selected text in the encoding of the locale. Otherwise, the widget transfers the selected text as type <code>COMPOUND_TEXT</code>.</p>
<dt><code>DELETE</code></p>
<dd>The widget deletes the selected text.</p>
<dt><code>_MOTIF_CLIPBOARD_TARGETS</code></p>
<dd>The widget transfers, as type <code>ATOM</code>, a list of the targets to which the widget can convert data to be placed on the clipboard immediately. These include the following targets:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd><code>UTF8_STRING</code></p>
<dt> &bull;</p>
<dd><code>COMPOUND_TEXT</code></p>
<dt> &bull;</p>
<dd>The encoding of the locale, if the selected text is fully convertible to the encoding of the locale</p>
<dt> &bull;</p>
<dd><code>STRING</code>, if the selected text is fully convertible to <code>STRING</code></dl>
</dl>
<dt><code>_MOTIF_EXPORT_TARGETS</code></p>
<dd>The widget transfers, as type <code>ATOM</code>, a list of the targets to be used as the value of the DragContext&#8217;s <code>XmNexportTargets</code> in a drag-and-drop transfer. These include <code>COMPOUND_TEXT</code>, the encoding of the locale, <code>STRING</code>, <code>TEXT</code>, <code>UTF8_STRING</code>, <code>BACKGROUND</code>, and <code>FOREGROUND</code>.</p>
<dt><code>_MOTIF_LOSE_SELECTION</code></p>
<dd>The widget takes the following actions:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd>When losing the <code>PRIMARY</code> selection, it unhighlights the selected text and calls the <code>XmNlosePrimaryCallback</code> procedures.</p>
<dt> &bull;</p>
<dd>When losing the <code>SECONDARY</code> selection, it removes the secondary selection highlight.</p>
<dt> &bull;</p>
<dd>When losing the <code>_MOTIF_DESTINATION</code> selection, if the widget does not have focus it changes the cursor to indicate that the widget is no longer the destination.</dl>
</dl>
</dl>
<p> As a source of data, TextField also supports the following standard Motif targets:</p>
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
<dd>The widget transfers, as type <code>ATOM</code>, a list of the targets it supports. These include the standard targets in this list. These also include <code>COMPOUND_TEXT</code>, the encoding of the locale, <code>STRING</code>, <code>TEXT</code> and <code>UTF8_STRING</code>.</p>
<dt><code>TIMESTAMP</code></p>
<dd>The widget transfers the timestamp used to acquire the selection as type <code>INTEGER</code>.</p>
<dt><code>_MOTIF_RENDER_TABLE</code></p>
<dd>The widget transfers <code>XmNrenderTable</code> if it exists, or else the default text render table, as type <code>STRING</code>.</p>
<dt><code>_MOTIF_ENCODING_REGISTRY</code></p>
<dd>The widget transfers its encoding registry as type <code>STRING</code>. The value is a list of NULL separated items in the form of tag encoding pairs. This target symbolizes the transfer target for the Motif Segment Encoding Registry. Widgets and applications can use this Registry to register text encoding formats for specified render table tags. Applications access this Registry by calling <code>XmRegisterSegmentEncoding</code> and <code>XmMapSegmentEncoding</code>.</dl>
<p> As a destination for data, TextField chooses a target and requests conversion of the selection to that target. If the encoding of the locale is present in the list of available targets, TextField chooses a requested target from the available targets in the following order of preference:</p>
<dl COMPACT>
<dt> 1.</p>
<dd><code>TEXT</code></p>
<dt> 1.</p>
<dd><code>UTF8_STRING</code></p>
<dt> 2.</p>
<dd><code>COMPOUND_TEXT</code></p>
<dt> 3.</p>
<dd>The encoding of the locale</p>
<dt> 4.</p>
<dd><code>STRING</code></dl>
<p> If the encoding of the locale is not present in the list of available targets, TextField chooses a requested target from the available targets in the following order of preference:</p>
<dl COMPACT>
<dt> 1.</p>
<dd><code>UTF8_STRING</code></p>
<dt> 1.</p>
<dd><code>COMPOUND_TEXT</code></p>
<dt> 2.</p>
<dd><code>STRING</code></dl>
<h3>Classes</h3>
<p>TextField widget inherits behavior, resources, and traits from <code>Core</code> and <i>Primitive</i>. </p>
<p> The class pointer is <code>xmTextFieldWidgetClass</code>. </p>
<p> The class name is <code>XmTextField</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lower case or upper case, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmTextFieldResource Set</code>
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
<td>XmNblinkRate</td>
<td>XmCBlinkRate</td>
<td>int</td>
<td>500</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNcolumns</td>
<td>XmCColumns</td>
<td>short</td>
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
<td>XmNcursorPosition</td>
<td>XmCCursorPosition</td>
<td>XmTextPosition</td>
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
<td>XmNcursorPositionVisible</td>
<td>XmCCursorPositionVisible</td>
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
<td>XmNdestinationCallback</td>
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
<td>XmNfocusCallback</td>
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
<td>XmNgainPrimaryCallback</td>
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
<td>XmNlosePrimaryCallback</td>
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
<td>XmNlosingFocusCallback</td>
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
<td>XmNmarginHeight</td>
<td>XmCMarginHeight</td>
<td>Dimension</td>
<td>5</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
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
<td>5</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNmaxLength</td>
<td>XmCMaxLength</td>
<td>int</td>
<td>largest integer</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNmodifyVerifyCallback</td>
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
<td>XmNmodifyVerifyCallbackWcs</td>
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
<td>XmNmotionVerifyCallback</td>
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
<td>XmNpendingDelete</td>
<td>XmCPendingDelete</td>
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
<td>XmNresizeWidth</td>
<td>XmCResizeWidth</td>
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
<td>XmNselectionArray</td>
<td>XmCSelectionArray</td>
<td>XtPointer</td>
<td>default array</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNselectionArrayCount</td>
<td>XmCSelectionArrayCount</td>
<td>int</td>
<td>3</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNselectThreshold</td>
<td>XmCSelectThreshold</td>
<td>int</td>
<td>5</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
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
<td>String</td>
<td>&quot;&quot;</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
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
<tr VALIGN=top>
<td>XmNvalueWcs</td>
<td>XmCValueWcs</td>
<td>wchar_t *</td>
<td>(wchar_t *)&quot;&quot;</td>
<td>CSG1
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNverifyBell</td>
<td>XmCVerifyBell</td>
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
<p> 1 This resource cannot be specified in a resource file.</p>
<dl COMPACT>
<dt><code>XmNactivateCallback</code></p>
<dd>Specifies the list of callbacks that is called when the user invokes an event that calls the activate() action. The type of the structure whose address is passed to this callback is <code>XmAnyCallbackStruct</code>. The reason sent by the callback is <code>XmCR_ACTIVATE</code>.</p>
<dt><code>XmNblinkRate</code></p>
<dd>Specifies the blink rate of the text cursor in milliseconds. The time indicated in the blink rate relates to the length of time the cursor is visible and the time the cursor is invisible (that is, the time it will take to blink the insertion cursor on and off will be two times the blink rate). The cursor will not blink when the blink rate is set to 0 (zero). The value must not be negative.</p>
<dt><code>XmNcolumns</code></p>
<dd>Specifies the initial width of the text window as an integer number of characters. The width equals the number of characters specified by this resource multiplied by the width as derived from the specified font. If the em-space value is available, it is used. If not, the width of the numeral &quot;0&quot; is used. If this is not available, the maximum width is used. For proportionate fonts, the actual number of characters that fit on a given line may be greater than the value specified.</p>
<dt><code>XmNcursorPosition</code></p>
<dd>Indicates the position in the text where the current insert cursor is to be located. Position is determined by the number of characters from the beginning of the text.</p>
<dt><code>XmNcursorPositionVisible</code></p>
<dd>If the text widget has an <code>XmPrintShell</code> as one of its ancestors (that is, the widget was created on a print server connection) then the default value is <code>False</code>; otherwise, it is <code>True</code>.</p>
<dt><code>XmNdestinationCallback</code></p>
<dd>Specifies a list of callbacks called when the widget is the destination of a transfer operation. The type of the structure whose address is passed to these callbacks is <code>XmDestinationCallbackStruct</code>. The reason is <code>XmCR_OK</code>.</p>
<dt><code>XmNeditable</code></p>
<dd>When set to True, indicates that the user can edit the text string. A false value will prohibit the user from editing the text.</p>
<dd>When <code>XmNeditable</code> is used on a widget it sets the dropsite to <code>XmDROP_SITE_ACTIVE</code>.</p>
<dt><code>XmNfocusCallback</code></p>
<dd>Specifies the list of callbacks called when TextField accepts input focus. The type of the structure whose address is passed to this callback is <code>XmAnyCallbackStruct</code>. The reason sent by the callback is <code>XmCR_FOCUS</code>.</p>
<dt><code>XmNfontList</code></p>
<dd>Specifies the font list to be used for TextField. The font list is an obsolete structure, and is retained only for compatibility with earlier releases of Motif. Use the render table (<code>XmNrenderTable</code>) instead of font lists wherever possible. If both are specified, the render table will take precedence. If this value is NULL at initialization, the parent hierarchy of the widget is searched for an ancestor that holds the <code>XmQTspecifyRenderTable</code> trait. If such an ancestor is found, the font list is initialized to the <code>XmTEXT_RENDER_TABLE</code> value of the ancestor widget. If no such ancestor is found, the default is implementation dependent.</p>
<dd>TextField searches the font list for the first occurrence of a font set that has an <code>XmFONTLIST_DEFAULT_TAG</code>. If a default element is not found, the first font set in the font list is used. If the list contains no font sets, the first font in the font list will be used. Refer to <code><a href="/docs/linux/man/3-xmfontlist/">XmFontList</a></code>(3) for more information on a font list structure.</p>
<dt><code>XmNgainPrimaryCallback</code></p>
<dd>Specifies the list of callbacks that are called when the user invokes an event that causes the text widget to gain ownership of the primary selection. The callback reason for this callback is <code>XmCR_GAIN_PRIMARY</code>.</p>
<dt><code>XmNlosePrimaryCallback</code></p>
<dd>Specifies the list of callbacks that are called when the user invokes an event that cause the text widget to lose ownership of the primary selection. The callback reason for this callback is <code>XmCR_LOSE_PRIMARY</code>.</p>
<dt><code>XmNlosingFocusCallback</code></p>
<dd>Specifies the list of callbacks that are called before TextField widget loses input focus. The type of the structure whose address is passed to this callback is <code>XmTextVerifyCallbackStruct</code>. The reason sent by the callback is <code>XmCR_LOSING_FOCUS</code>.</p>
<dt><code>XmNmarginHeight</code></p>
<dd>Specifies the distance between the top edge of the widget window and the text, and the bottom edge of the widget window and the text.</p>
<dt><code>XmNmarginWidth</code></p>
<dd>Specifies the distance between the left edge of the widget window and the text, and the right edge of the widget window and the text.</p>
<dt><code>XmNmaxLength</code></p>
<dd>Specifies the maximum length of the text string that can be entered into text from the keyboard. This value must be nonnegative. Strings that are entered using the <code>XmNvalue</code> resource or the <code>XmTextFieldSetString</code> function ignore this resource.</p>
<dt><code>XmNmodifyVerifyCallback</code></p>
<dd>Specifies the list of callbacks that is called before text is deleted from or inserted into TextField. The type of the structure whose address is passed to this callback is <code>XmTextVerifyCallbackStruct</code>. The reason sent by the callback is <code>XmCR_MODIFYING_TEXT_VALUE</code>. When multiple TextField widgets share the same source, only the widget that initiates the source change will generate the <code>XmNmodifyVerifyCallback</code>.</p>
<dd>If both <code>XmNmodifyVerifyCallback</code> and <code>XmNmodifyVerifyCallbackWcs</code> are registered callback lists, the procedure(s) in the <code>XmNmodifyVerifyCallback</code> list is always executed first; and the resulting data, which may have been modified, is passed to the <code>XmNmodifyVerifyCallbackWcs</code> callback routines.</p>
<dt><code>XmNmodifyVerifyCallbackWcs</code></p>
<dd>Specifies the list of callbacks called before text is deleted from or inserted into Text. The type of the structure whose address is passed to this callback is <code>XmTextVerifyCallbackStructWcs</code>. The reason sent by the callback is <code>XmCR_MODIFYING_TEXT_VALUE</code>. When multiple TextField widgets share the same source, only the widget that initiates the source change will generate the <code>XmNmodifyVerifyCallbackWcs</code>.</p>
<dd>If both <code>XmNmodifyVerifyCallback</code> and <code>XmNmodifyVerifyCallbackWcs</code> are registered callback lists, the procedure(s) in the <code>XmNmodifyVerifyCallback</code> list is always executed first; and the resulting data, which may have been modified, is passed to the <code>XmNmodifyVerifyCallbackWcs</code> callback routines.</p>
<dt><code>XmNmotionVerifyCallback</code></p>
<dd>Specifies the list of callbacks that is called before the insert cursor is moved to a new position. The type of the structure whose address is passed to this callback is <code>XmTextVerifyCallbackStruct</code>. The reason sent by the callback is <code>XmCR_MOVING_INSERT_CURSOR</code>. It is possible for more than one <code>XmNmotionVerifyCallback</code>s to be generated from a single action.</p>
<dt><code>XmNpendingDelete</code></p>
<dd>Indicates that pending delete mode is on when the Boolean is True. Pending deletion is defined as deletion of the selected text when an insertion is made.</p>
<dt><code>XmNrenderTable</code></p>
<dd>Specifies the render table to be used in deriving a font set or font for displaying text. If both a render table and a font list are specified, the render table will take precedence. If the value of <code>XmNrenderTable</code> is NULL at initialization, the parent hierarchy of the widget is searched for an ancestor that holds the <code>XmQTspecifyRenderTable</code> trait. If such an ancestor is found, the font list is initialized to the <code>XmTEXT_RENDER_TABLE</code> value of the ancestor widget. If no such ancestor is found, the default is implementation dependent.</p>
<dd>TextField searches the render table for the first occurrence of a rendition that has the tag <code>_MOTIF_DEFAULT_LOCALE</code>. If a default element is not found, the first rendition in the table is used. Refer to <code><a href="/docs/linux/man/3-xmrendertable/">XmRenderTable</a></code>(3) for more information on the render table structure.</p>
<dt><code>XmNresizeWidth</code></p>
<dd>Indicates that the TextField widget will attempt to resize its width to accommodate all the text contained in the widget when Boolean is True.</p>
<dt><code>XmNselectionArray</code></p>
<dd>Defines the actions for multiple mouse clicks. Each mouse click performed within some time of the previous mouse click will increment the index into this array and perform the defined action for that index. (This &quot;multi-click&quot; time is specified by the operating environment, and varies among different systems. In general, it is usually set to some fraction of a second.) The possible actions are</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmSELECT_POSITION</code></p>
<dd>Resets the insert cursor position</p>
<dt><code>XmSELECT_WORD</code></p>
<dd>Selects a word</p>
<dt><code>XmSELECT_LINE</code></p>
<dd>Selects a line of text</dl>
</dl>
<dt><code>XmNselectionArrayCount</code></p>
<dd>Specifies the number of actions that are defined in the <code>XmNselectionArray</code> resource. The value must not be negative.</p>
<dt><code>XmNselectThreshold</code></p>
<dd>Specifies the number of pixels of motion that is required to select the next character when selection is performed using the click-drag mode of selection. The value must not be negative. This resource also specifies whether a drag should be started and the number of pixels to start a drag when <code>Btn2Down</code> and <code>Btn1Down</code> are integrated.</p>
<dt><code>XmNvalue</code></p>
<dd>Specifies the string value of the TextField widget as a <code>char*</code> data value. Moves the cursor to position 0 unless a value of <code>XmNcursorPosition</code> was explicitly supplied in the argument list. If <code>XmNvalue</code> and <code>XmNvalueWcs</code> are both defined, the value of <code>XmNvalueWcs</code> supersedes that of <code>XmNvalue</code>. <code>XtGetValues</code> returns a copy of the value of the internal buffer and <code>XtSetValues</code> copies the string values into the internal buffer.</p>
<dt><code>XmNvalueChangedCallback</code></p>
<dd>Specifies the list of callbacks that is called after text is deleted from or inserted into TextField. The type of the structure whose address is passed to this callback is <code>XmAnyCallbackStruct</code>. The reason sent by the callback is <code>XmCR_VALUE_CHANGED</code>. The <code>XmNvalueChangedCallback</code> should occur only in pairs with a <code>XmNmodifyVerifyCallback</code>, assuming that the <i>doit</i> flag in the callback structure of the <code>XmNmodifyVerifyCallback</code> is not set to False.</p>
<dt><code>XmNvalueWcs</code></p>
<dd>Specifies the string value of the TextField widget as a <code>wchar_t*</code> data value. Moves the cursor to position 0 unless a value of <code>XmNcursorPosition</code> was explicitly supplied in the argument list.</p>
<dd>This resource cannot be specified in a resource file.</p>
<dd>If <code>XmNvalue</code> and <code>XmNvalueWcs</code> are both defined, the value of <code>XmNvalueWcs</code> supersedes that of <code>XmNvalue</code>. <code>XtGetValues</code> returns a copy of the value of the internal buffer encoded as a wide character string. <code>XtSetValues</code> copies the value of the wide character string into the internal buffer.</p>
<dt><code>XmNverifyBell</code></p>
<dd>Specifies whether a bell will sound when an action is reversed during a verification callback. The default depends on the value of the ancestor VendorShell&#8217;s <code>XmNaudibleWarning</code> resource.</dl>
<h3>Inherited Resources</h3>
<p>TextField widget inherits behavior and resources from the superclasses in the following tables. For a complete description of these resources, refer to the reference page for that superclass. </p>
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
} XmAnyCallbackStruct;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the callback</dl>
<p> The TextField widget defines a new callback structure for use with verification callbacks. Note that not all of the fields are relevant for every callback reason. The application must first look at the <i>reason</i> field and use only the structure members that are valid for the particular reason. The values <i>startPos</i>, <i>endPos</i>, and <i>text</i> in the callback structure <code>XmTextVerifyCallbackStruct</code> may be modified upon receiving the callback, and these changes will be reflected as the change made to the source of the TextField widget. (For example, all keystrokes can be converted to spaces or NULL characters when a password is entered into a TextField widget.) The application programmer should not overwrite the <i>text</i> field, but should attach data to that pointer. </p>
<p> A pointer to the following structure is passed to the callbacks for <code>XmNlosingFocusCallback</code>, <code>XmNmodifyVerifyCallback</code>, and <code>XmNmotionVerifyCallback</code>. </p>
<pre>typedef struct
{
 int <i>reason</i>;
 XEvent *<i>event</i>;
 Boolean <i>doit</i>;
 XmTextPosition <i>currInsert, newInsert</i>;
 XmTextPosition <i>startPos, endPos</i>;
 XmTextBlock <i>text</i>;
} XmTextVerifyCallbackStruct, *XmTextVerifyPtr;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked.</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> the triggered the callback. It can be NULL. For example, changes made to the Text widget programmatically do not have an event that can be passed to the associated callback.</p>
<dt><i>doit</i></p>
<dd>Indicates whether the action that invoked the callback will be performed. Setting <i>doit</i> to False negates the action. Note that not all actions may be negated. For example, <code>XmCR_LOSING_FOCUS</code> callbacks may be beyond the control of the widget if they are produced by mouse clicks.</p>
<dt><i>currInsert</i></p>
<dd>Indicates the current position of the insert cursor.</p>
<dt><i>newInsert</i></p>
<dd>Indicates the position at which the user attempts to position the insert cursor.</p>
<dt><i>startPos</i></p>
<dd>Indicates the starting position of the text to modify. If the callback is not a modify verification callback, this value is the same as <i>currInsert</i>.</p>
<dt><i>endPos</i></p>
<dd>Indicates the ending position of the text to modify. If no text is replaced or deleted, then the value is the same as <i>startPos</i>. If the callback is not a modify verification callback, this value is the same as <i>currInsert</i>.</p>
<dt><i>text</i></p>
<dd>Points to the following structure of type <code>XmTextBlockRec</code>. This structure holds the textual information to be inserted.</dl>
<pre>typedef struct
{
 char *<i>ptr</i>;
 int <i>length</i>;
 XmTextFormat <i>format</i>
} XmTextBlockRec, *XmTextBlock;</pre>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><i>ptr</i></p>
<dd>The text to be inserted. <i>ptr</i> points to a temporary storage space that is reused after the callback is finished. Therefore, if an application needs to save the text to be inserted, it should copy the text into its own data space.</p>
<dt><i>length</i></p>
<dd>Specifies the length of the text to be inserted.</p>
<dt><i>format</i></p>
<dd>Specifies the format of the text, either <code>XmFMT_8_BIT</code> or <code>XmFMT_16_BIT</code>.</dl>
</dl>
<p> A pointer to the following structure is passed to callbacks for <code>XmNmodifyVerifyCallbackWcs</code>. </p>
<pre>typedef struct
{
 int <i>reason</i>;
 XEvent *<i>event</i>;
 Boolean <i>doit</i>;
 XmTextPosition <i>currInsert, newInsert</i>;
 XmTextPosition <i>startPos, endPos</i>;
 XmWcsTextBlock <i>text</i>;
} XmTextVerifyCallbackStructWcs, *XmTextVerifyPtrWcs;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked.</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the callback. It can be NULL. For example, changes made to the Text widget programmatically do not have an event that can be passed to the associated callback.</p>
<dt><i>doit</i></p>
<dd>Indicates whether the action that invoked the callback is performed. Setting <i>doit</i> to False negates the action. Note that not all actions may be negated. For example, <code>XmCR_LOSING_FOCUS</code> callbacks may be beyond the control of the widget if they are produced by mouse clicks.</p>
<dt><i>currInsert</i></p>
<dd>Indicates the current position of the insert cursor.</p>
<dt><i>newInsert</i></p>
<dd>Indicates the position at which the user attempts to position the insert cursor.</p>
<dt><i>startPos</i></p>
<dd>Indicates the starting position of the text to modify. If the callback is not a modify verification callback, this value is the same as <i>currInsert</i>.</p>
<dt><i>endPos</i></p>
<dd>Indicates the ending position of the text to modify. If no text is replaced or deleted, the value is the same as <i>startPos</i>. If the callback is not a modify verification callback, this value is the same as <i>currInsert</i>.</p>
<dt><i>text</i></p>
<dd>Points to the following structure of type <code>XmTextBlockRecWcs</code>. This structure holds the textual information to be inserted.</dl>
<pre>typedef struct
{
 wchar_t *<i>wcsptr</i>;
 int <i>length</i>;
} XmTextBlockRecWcs, *XmTextBlockWcs;</pre>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><i>wcsptr</i></p>
<dd>Points to the wide character text to be inserted</p>
<dt><i>length</i></p>
<dd>Specifies the number of characters to be inserted</dl>
</dl>
<p> The following table describes the reasons for which the individual verification callback structure fields are valid. Note that the <i>event</i> field will never be valid for <code>XmCR_MOVING_INSERT_CURSOR</code>. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td><code>Reason</code></td>
<td><code>Valid Fields</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmCR_LOSING_FOCUS</td>
<td><i>reason, event, doit</i>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmCR_MODIFYING_TEXT_VALUE</td>
<td> <i>reason, event, doit, currInsert, newInsert, startPos, endPos, text</i>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmCR_MOVING_INSERT_CURSOR</td>
<td><i>reason, doit, currInsert, newInsert</i>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
</table>
</table>
<p> A pointer to the following callback structure is passed to the <code>XmNdestinationCallback</code> procedures: </p>
<pre>typedef struct
{
 int <i>reason</i>;
 XEvent *<i>event</i>;
 Atom <i>selection</i>;
 XtEnum <i>operation</i>;
 int <i>flags</i>;
 XtPointer <i>transfer_id</i>;
 XtPointer <i>destination_data</i>;
 XtPointer <i>location_data</i>;
 Time <i>time</i>;
} XmDestinationCallbackStruct;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked.</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the callback. It can be NULL.</p>
<dt><i>selection</i></p>
<dd>Indicates the selection for which data transfer is being requested. Possible values are <code>CLIPBOARD</code>, <code>PRIMARY</code>, <code>SECONDARY</code>, and <code>_MOTIF_DROP</code>.</p>
<dt><i>operation</i></p>
<dd>Indicates the type of transfer operation requested.</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd>When the selection is <code>PRIMARY</code> or <code>SECONDARY</code>, possible values are <code>XmMOVE</code>, <code>XmCOPY</code>, and <code>XmLINK</code>.</p>
<dt> &bull;</p>
<dd>When the selection is <code>CLIPBOARD</code>, possible values are <code>XmCOPY</code> and <code>XmLINK</code>.</p>
<dt> &bull;</p>
<dd>When the selection is <code>_MOTIF_DROP</code>, possible values are <code>XmMOVE</code>, <code>XmCOPY</code>, <code>XmLINK</code>, and <code>XmOTHER</code>. A value of <code>XmOTHER</code> means that the callback procedure must get further information from the <code>XmDropProcCallbackStruct</code> in the <i>destination_data</i> member.</dl>
</dl>
<dt><i>flags</i></p>
<dd>Indicates whether or not the destination widget is also the source of the data to be transferred. Following are the possible values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmCONVERTING_NONE</code></p>
<dd>The destination widget is not the source of the data to be transferred.</p>
<dt><code>XmCONVERTING_SAME</code></p>
<dd>The destination widget is the source of the data to be transferred.</dl>
</dl>
<dt><code>transfer_id</code></p>
<dd>Serves as a unique ID to identify the transfer transaction.</p>
<dt><i>destination_data</i></p>
<dd>Contains information about the destination. When the selection is <code>_MOTIF_DROP</code>, the callback procedures are called by the drop site&#8217;s <code>XmNdropProc</code>, and <i>destination_data</i> is a pointer to the <code>XmDropProcCallbackStruct</code> passed to the <code>XmNdropProc</code> procedure. When the selection is <code>SECONDARY</code>, <i>destination_data</i> is an Atom representing a target recommmended by the selection owner for use in converting the selection. Otherwise, <i>destination_data</i> is NULL.</p>
<dt><code>location_data</code></p>
<dd>Contains information about the location where data is to be transferred. The value is always NULL when the selection is <code>CLIPBOARD</code>. If the value is NULL, the data is to be inserted at the widget&#8217;s cursor position. Otherwise, the value is a pointer to an <code>XPoint</code> structure containing the x and y coordinates at the location where the data is to be transferred. Once <code>XmTransferDone</code> procedures start to be called, <code>location_data</code> will no longer be stable.</p>
<dt><i>time</i></p>
<dd>Indicates the time when the transfer operation began.</dl>
<h3>Translations</h3>
<p>The <code>XmTextField</code> translations are described in the following list. The actions represent the effective behavior of the associated events, and they may differ in a right-to-left language environment. </p>
<p> The following key names are listed in the X standard key event translation table syntax. This format is the one used by Motif to specify the widget actions corresponding to a given key. A brief overview of the format is provided under <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3). For a complete description of the format, please refer to the X Toolkit Instrinsics Documentation.</p>
<dl COMPACT>
<dt><code>&asymp;c s &asymp;m &asymp;a</code> <code>&lt;Btn1Down&gt;</code>:</p>
<dd>extend-start()</p>
<dt><code>c &asymp;s &asymp;m &asymp;a</code> <code>&lt;Btn1Down&gt;</code>:</p>
<dd>move-destination()</p>
<dt><code>&asymp;c &asymp;s &asymp;m &asymp;a</code> <code>&lt;Btn1Down&gt;</code>:</p>
<dd>grab-focus()</p>
<dt><code>&asymp;c &asymp;m &asymp;a</code> <code>&lt;Btn1Motion&gt;</code>:</p>
<dd>extend-adjust()</p>
<dt><code>&asymp;c &asymp;m &asymp;a</code> <code>&lt;Btn1Up&gt;</code>:</p>
<dd>extend-end()</p>
<dt><code>&lt;Btn2Down&gt;</code>:</p>
<dd>process-bdrag()</p>
<dt><code>m &asymp;a</code> <code>&lt;Btn2Motion&gt;</code>:</p>
<dd>secondary-adjust()</p>
<dt><code>&asymp;m a</code> <code>&lt;Btn2Motion&gt;</code>:</p>
<dd>secondary-adjust()</p>
<dt><code>s c &lt;Btn2Up&gt;</code>:</p>
<dd>link-to()</p>
<dt><code>&asymp;s</code> <code>&lt;Btn2Up&gt;</code>:</p>
<dd>copy-to()</p>
<dt><code>&asymp;c</code> <code>&lt;Btn2Up&gt;</code>:</p>
<dd>move-to()</p>
<dt><code>:m</code> <code>&lt;Key&gt;</code><code>&lt;osfPrimaryPaste&gt;</code>:</p>
<dd>cut-primary()</p>
<dt><code>:a</code> <code>&lt;Key&gt;</code><code>&lt;osfPrimaryPaste&gt;</code>:</p>
<dd>cut-primary()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfPrimaryPaste&gt;</code>:</p>
<dd>copy-primary()</p>
<dt><code>:m</code> <code>&lt;Key&gt;</code><code>&lt;osfCut&gt;</code>:</p>
<dd>cut-primary()</p>
<dt><code>:a</code> <code>&lt;Key&gt;</code><code>&lt;osfCut&gt;</code>:</p>
<dd>cut-primary()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfCut&gt;</code>:</p>
<dd>cut-clipboard()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfPaste&gt;</code>:</p>
<dd>paste-clipboard()</p>
<dt><code>:m</code> <code>&lt;Key&gt;</code><code>&lt;osfCopy&gt;</code>:</p>
<dd>copy-primary()</p>
<dt><code>:a</code> <code>&lt;Key&gt;</code><code>&lt;osfCopy&gt;</code>:</p>
<dd>copy-primary()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfCopy&gt;</code>:</p>
<dd>copy-clipboard()</p>
<dt><code>:s</code> <code>&lt;Key&gt;</code><code>&lt;osfBeginLine&gt;</code>:</p>
<dd>beginning-of-line(<code>extend</code>)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfBeginLine&gt;</code>:</p>
<dd>beginning-of-line()</p>
<dt><code>:s</code> <code>&lt;Key&gt;</code><code>&lt;osfEndLine&gt;</code>:</p>
<dd>end-of-line(<code>extend</code>)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfEndLine&gt;</code>:</p>
<dd>end-of-line()</p>
<dt><code>:s</code> <code>&lt;Key&gt;</code><code>&lt;osfPageLeft&gt;</code>:</p>
<dd>page-left(<code>extend</code>)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfPageLeft&gt;</code>:</p>
<dd>page-left()</p>
<dt><code>:s c</code><code>&lt;Key&gt;</code><code>&lt;osfPageUp&gt;</code>:</p>
<dd>page-left(<code>extend</code>)</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfPageUp&gt;</code>:</p>
<dd>page-left()</p>
<dt><code>:s</code> <code>&lt;Key&gt;</code><code>&lt;osfPageRight&gt;</code>:</p>
<dd>page-right(<code>extend</code>)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfPageRight&gt;</code>:</p>
<dd>page-right()</p>
<dt><code>s c</code> <code>&lt;Key&gt;</code><code>&lt;osfPageDown&gt;</code>:</p>
<dd>page-right(<code>extend</code>)</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfPageDown&gt;</code>:</p>
<dd>page-right()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfClear&gt;</code>:</p>
<dd>clear-selection()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfBackSpace&gt;</code>:</p>
<dd>delete-previous-character()</p>
<dt><code>:s m</code> <code>&lt;Key&gt;</code><code>&lt;osfDelete&gt;</code>:</p>
<dd>cut-primary()</p>
<dt><code>:s a</code> <code>&lt;Key&gt;</code><code>&lt;osfDelete&gt;</code>:</p>
<dd>cut-primary()</p>
<dt><code>:s</code> <code>&lt;Key&gt;</code><code>&lt;osfDelete&gt;</code>:</p>
<dd>cut-clipboard()</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfDelete&gt;</code>:</p>
<dd>delete-to-end-of-line()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfDelete&gt;</code>:</p>
<dd>delete-next-character()</p>
<dt><code>:c m</code> <code>&lt;Key&gt;</code><code>&lt;osfInsert&gt;</code>:</p>
<dd>copy-primary()</p>
<dt><code>:c a</code> <code>&lt;Key&gt;</code><code>&lt;osfInsert&gt;</code>:</p>
<dd>copy-primary()</p>
<dt><code>:s</code> <code>&lt;Key&gt;</code><code>&lt;osfInsert&gt;</code>:</p>
<dd>paste-clipboard()</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfInsert&gt;</code>:</p>
<dd>copy-clipboard()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfInsert&gt;</code>:</p>
<dd>toggle-overstrike()</p>
<dt><code>:s</code> <code>&lt;Key&gt;</code><code>&lt;osfSelect&gt;</code>:</p>
<dd>key-select()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfSelect&gt;</code>:</p>
<dd>set-anchor()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfSelectAll&gt;</code>:</p>
<dd>select-all()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfDeselectAll&gt;</code>:</p>
<dd>deselect-all()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfActivate&gt;</code>:</p>
<dd>activate()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfAddMode&gt;</code>:</p>
<dd>toggle-add-mode()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfHelp&gt;</code>:</p>
<dd>Help()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfCancel&gt;</code>:</p>
<dd>process-cancel()</p>
<dt><code>:s c</code> <code>&lt;Key&gt;</code><code>&lt;osfLeft&gt;</code>:</p>
<dd>backward-word(<code>extend</code>)</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfLeft&gt;</code>:</p>
<dd>backward-word()</p>
<dt><code>:s</code> <code>&lt;Key&gt;</code><code>&lt;osfLeft&gt;</code>:</p>
<dd>key-select(<code>left</code>)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfLeft&gt;</code>:</p>
<dd>backward-character()</p>
<dt><code>:s c</code> <code>&lt;Key&gt;</code><code>&lt;osfRight&gt;</code>:</p>
<dd>forward-word(<code>extend</code>)</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfRight&gt;</code>:</p>
<dd>forward-word()</p>
<dt><code>:s</code> <code>&lt;Key&gt;</code><code>&lt;osfRight&gt;</code>:</p>
<dd>key-select(<code>right</code>)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfRight&gt;</code>:</p>
<dd>forward-character()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfUp&gt;</code>:</p>
<dd>traverse-prev()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfDown&gt;</code>:</p>
<dd>traverse-next()</p>
<dt><code>c &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>slash</code>:</p>
<dd>select-all()</p>
<dt><code>c &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>backslash</code>:</p>
<dd>deselect-all()</p>
<dt><code>s &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>Tab</code>:</p>
<dd>prev-tab-group()</p>
<dt><code>&asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>Tab</code>:</p>
<dd>next-tab-group()</p>
<dt><code>&asymp;s &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>Return</code>:</p>
<dd>activate()</p>
<dt><code>c &asymp;s &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>space</code>:</p>
<dd>set-anchor()</p>
<dt><code>c s &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>space</code>:</p>
<dd>key-select()</p>
<dt><code>s &asymp;c &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>space</code>:</p>
<dd>self-insert()</p>
<dt><code>&lt;Key&gt;</code>:</p>
<dd>self-insert()</dl>
<p> The TextField button event translations are modified when Display&#8217;s <code>XmNenableBtn1Transfer</code> resource does not have a value of <code>XmOFF</code> (in other words, it is either <code>XmBUTTON2_TRANSFER</code> or <code>XmBUTTON2_ADJUST</code>). This option allows the actions for selection and transfer to be integrated on <code>&lt;Btn1&gt;</code>. The actions for <code>&lt;Btn1&gt;</code> that are defined above still apply when the <code>&lt;Btn1&gt;</code> event occurs over text that is not selected. The following actions apply when the <code>&lt;Btn1&gt;</code> event occurs over text that is selected:</p>
<dl COMPACT>
<dt><code>&lt;Btn1Down&gt;</code>:</p>
<dd>process-bdrag().</p>
<dt><code>&lt;Shift&gt;</code><code>&lt;Btn1Down&gt;</code>:</p>
<dd>process-bdrag().</p>
<dt><code>&lt;Btn1Down&gt;</code><code>&lt;Shift&gt;</code><code>&lt;Btn1Up&gt;</code>:</p>
<dd>grab-focus(), <code>extend-end</code>.</p>
<dt><code>&lt;Shift&gt;</code><code>&lt;Btn1Down&gt;</code><code>&lt;Shift&gt;</code><code>&lt;Btn1Up&gt;</code>:</p>
<dd>extend-start(), extend-end().</p>
<dt><code>&lt;Ctrl&gt;</code><code>&lt;Btn1Down&gt;</code><code>&lt;Shift&gt;</code><code>&lt;Btn1Up&gt;</code>:</p>
<dd>move-destination().</p>
<dt><code>&lt;Ctrl&gt;</code><code>&lt;Btn1Down&gt;</code>:</p>
<dd>process-bdrag().</dl>
<p> When Display&#8217;s <code>XmNenableBtn1Transfer</code> resource has a value of <code>XmBUTTON2_ADJUST</code>, the following actions apply:</p>
<dl COMPACT>
<dt><code>&lt;Btn2Down&gt;</code>:</p>
<dd>extend-start().</p>
<dt><code>&lt;Btn2Motion&gt;</code>:</p>
<dd>extend-adjust().</p>
<dt><code>&lt;Btn2Up&gt;</code>:</p>
<dd>extend-end().</dl>
<h3>Action Routines</h3>
<p>The <code>XmTextField</code> action routines are</p>
<dl COMPACT>
<dt>activate():</p>
<dd>Calls the callbacks for <code>XmNactivateCallback</code>. If the parent is a manager, passes the event to the parent.</p>
<dt>backward-character(<code>extend</code>):</p>
<dd>Moves the insertion cursor one character to the left. This action may have different behavior in a right-to-left language environment.</p>
<dd>If called with an argument of <i>extend</i>, moves the insertion cursor as in the case of no argument and extends the current selection.</p>
<dd>The backward-character() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>. If called with the <i>extend</i> argument, the backward-character() action may produce calls to the <code>XmNgainPrimaryCallback</code> procedures. See callback description for more information.</p>
<dt>backward-word(<code>extend</code>):</p>
<dd>If this action is called with no argument, moves the insertion cursor to the first non-whitespace character after the first whitespace character to the left or after the beginning of the line. If the insertion cursor is already at the beginning of a word, moves the insertion cursor to the beginning of the previous word. This action may have different behavior in a locale other than the C locale.</p>
<dd>If called with an argument of <i>extend</i>, moves the insertion cursor as in the case of no argument and extends the current selection.</p>
<dd>The backward-word() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>. If called with the <i>extend</i> argument, the backward-word() action may produce calls to the <code>XmNgainPrimaryCallback</code> procedures. See callback description for more information.</p>
<dt>beginning-of-line(<code>extend</code>):</p>
<dd>If this action is called with no argument, moves the insertion cursor to the beginning of the line.</p>
<dd>If called with an argument of <i>extend</i>, moves the insertion cursor as in the case of no argument and extends the current selection.</p>
<dd>The beginning-of-line() action produces calls to the <code>XmNmotionVerifyCallback</code> with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>. If called with the <i>extend</i> argument, the beginning-of-line() action may produce calls to the <code>XmNgainPrimaryCallback</code> procedures. See callback description for more information.</p>
<dt>clear-selection():</p>
<dd>Clears the current selection by replacing each character except <code>&lt;Return&gt;</code> with a <code>&lt;space&gt;</code> character.</p>
<dd>The clear-selection() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code> and the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>.</p>
<dt>copy-clipboard():</p>
<dd>If this widget owns the primary selection, this action copies the selection to the clipboard. This action calls the <code>XmNconvertCallback</code> procedures, possibly multiple times, for the <code>CLIPBOARD</code> selection.</p>
<dt>copy-primary():</p>
<dd>Copies the primary selection to just before the insertion cursor. This action calls the <code>XmNdestinationCallback</code> procedures for the <code>PRIMARY</code> selection and the <code>XmCOPY</code> operation. It calls the selection owner&#8217;s <code>XmNconvertCallback</code> procedures, possibly multiple times, for the <code>PRIMARY</code> selection.</p>
<dd>In addition, the copy-primary() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, the <code>XmNvalueChangedCallback</code> with reason value <code>XmCR_VALUE_CHANGED</code>, and the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>. The copy-primary() action may produce calls to the <code>XmNgainPrimaryCallback</code> procedures. See callback description for more information.</p>
<dt>copy-to():</p>
<dd>If a secondary selection exists, this action copies the secondary selection to the insertion position of the destination component. If the primary selection is in the destination widget, it will be deselected. Otherwise, there is no effect on the primary selection.</p>
<dd>This action calls the destination&#8217;s <code>XmNdestinationCallback</code> procedures for the <code>SECONDARY</code> selection and the <code>XmCOPY</code> operation. The destination&#8217;s <code>XmNdestinationCallback</code> procedures or the destination component itself invokes the selection owner&#8217;s <code>XmNconvertCallback</code> procedures, possibly multiple times, for the <code>SECONDARY</code> selection.</p>
<dd>If no secondary selection exists, this action copies the primary selection to the pointer position. This action calls the <code>XmNdestinationCallback</code> procedures for the <code>PRIMARY</code> selection and the <code>XmCOPY</code> operation. It calls the selection owner&#8217;s <code>XmNconvertCallback</code> procedures, possibly multiple times, for the <code>PRIMARY</code> selection.</p>
<dd>In addition, the copy-to() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>, and the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>. If there is no secondary selection, the copy-to() action may produce calls to the <code>XmNgainPrimaryCallback</code> procedures. See callback description for more information.</p>
<dt>cut-clipboard():</p>
<dd>If this widget owns the primary selection, this action cuts the selection to the clipboard. This action calls the <code>XmNconvertCallback</code> procedures, possibly multiple times, for the <code>CLIPBOARD</code> selection. If the transfer is successful, this action then calls the <code>XmNconvertCallback</code> procedures for the <code>CLIPBOARD</code> selection and the <code>DELETE</code> target.</p>
<dd>In addition, the cut-clipboard() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, and the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>.</p>
<dt>cut-primary():</p>
<dd>Cuts the primary selection and pastes it just before the insertion cursor. This action calls the <code>XmNdestinationCallback</code> procedures for the <code>PRIMARY</code> selection and the <code>XmMOVE</code> operation. It calls the selection owner&#8217;s <code>XmNconvertCallback</code> procedures, possibly multiple times, for the <code>PRIMARY</code> selection. If the transfer is successful, this action then calls the selection owner&#8217;s <code>XmNconvertCallback</code> procedures for the <code>PRIMARY</code> selection and the <code>DELETE</code> target.</p>
<dd>In addition, the cut-primary() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>, the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, and the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>.</p>
<dt>delete-next-character():</p>
<dd>In normal mode, if there is a nonnull selection, deletes the selection; otherwise, deletes the character following the insertion cursor. In add mode, if there is a nonnull selection, the cursor is not disjoint from the selection and <code>XmNpendingDelete</code> is set to True, deletes the selection; otherwise, deletes the character following the insertion cursor. This may impact the selection.</p>
<dd>The delete-next-character() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, and the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>.</p>
<dt>delete-next-word():</p>
<dd>In normal mode, if there is a nonnull selection, deletes the selection; otherwise, deletes the characters following the insertion cursor to the next space, tab or end-of-line character. In add mode, if there is a nonnull selection, the cursor is not disjoint from the selection and <code>XmNpendingDelete</code> is set to True, deletes the selection; otherwise, deletes the characters following the insertion cursor to the next space, tab or end-of-line character. This may impact the selection. This action may have different behavior in a locale other than the C locale.</p>
<dd>The delete-next-word() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, and the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>.</p>
<dt>delete-previous-character():</p>
<dd>In normal mode, if there is a nonnull selection, deletes the selection; otherwise, deletes the character of text immediately preceding the insertion cursor. In add mode, if there is a nonnull selection, the cursor is not disjoint from the selection and <code>XmNpendingDelete</code> is set to True, deletes the selection; otherwise, deletes the character of text immediately preceding the insertion cursor. This may impact the selection.</p>
<dd>The delete-previous-character() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>, and the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>.</p>
<dt>delete-previous-word():</p>
<dd>In normal mode, if there is a nonnull selection, deletes the selection; otherwise, deletes the characters preceding the insertion cursor to the next space, tab or beginning-of-line character. In add mode, if there is a nonnull selection, the cursor is not disjoint from the selection and <code>XmNpendingDelete</code> is set to True, deletes the selection; otherwise, deletes the characters preceding the insertion cursor to the next space, tab or beginning-of-line character. This may impact the selection. This action may have different behavior in a locale other than the C locale.</p>
<dd>The delete-previous-word() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>, and the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>.</p>
<dt>delete-selection():</p>
<dd>Deletes the current selection.</p>
<dd>The delete-selection() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>, and the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>.</p>
<dt>delete-to-end-of-line():</p>
<dd>In normal mode, if there is a nonnull selection, deletes the selection; otherwise, deletes the characters following the insertion cursor to the next end of line character. In add mode, if there is a nonnull selection, the cursor is not disjoint from the selection and <code>XmNpendingDelete</code> is set to True, deletes the selection; otherwise, deletes the characters following the insertion cursor to the next end of line character. This may impact the selection.</p>
<dd>The delete-to-end-of-line() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, and the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>.</p>
<dt>delete-to-start-of-line():</p>
<dd>In normal mode, if there is a nonnull selection, deletes the selection; otherwise, deletes the characters preceding the insertion cursor to the previous beginning-of-line character. In add mode, if there is a nonnull selection, the cursor is not disjoint from the selection and <code>XmNpendingDelete</code> is set to True, deletes the selection; otherwise, deletes the characters preceding the insertion cursor to the previous beginning-of-line character. This may impact the selection.</p>
<dd>The delete-to-start-of-line() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>, and the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>.</p>
<dt>deselect-all():</p>
<dd>Deselects the current selection.</p>
<dd>The deselect-all() action produces no callbacks.</p>
<dt>end-of-line(<code>extend</code>):</p>
<dd>If this action is called with no argument, moves the insertion cursor to the end of the line. If called with an argument of <i>extend</i>, moves the insertion cursor as in the case of no argument and extends the current selection.</p>
<dd>The end-of-line() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>. If called with the <i>extend</i> argument, the end-of-line() action may produce calls to the <code>XmNgainPrimaryCallback</code> procedures. See callback description for more information.</p>
<dt>extend-adjust():</p>
<dd>Selects text from the anchor to the pointer position and deselects text outside that range.</p>
<dd>The extend-adjust() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>. The extend-adjust() action may produce calls to the <code>XmNgainPrimaryCallback</code> procedures. See callback description for more information.</p>
<dt>extend-end():</p>
<dd>Moves the insertion cursor to the position of the pointer. The extend-end() action is used to commit the selection. After this action has been done, process-cancel() will no longer cancel the selection.</p>
<dd>The extend-end() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>. The extend-end() action may produce calls to the <code>XmNgainPrimaryCallback</code> procedures. See callback description for more information.</p>
<dt>extend-start():</p>
<dd>Adjusts the anchor using the balance-beam method. Selects text from the anchor to the pointer position and deselects text outside that range.</p>
<dd>The extend-start() action can produce no callbacks, however, it may produce calls to the <code>XmNgainPrimaryCallback</code> and <code>XmNmotionVerifyCallback</code> procedures. See callback description for more information.</p>
<dt>forward-character(<code>extend</code>):</p>
<dd>Moves the insertion cursor one character to the right. This action may have different behavior in a right-to-left language environment.</p>
<dd>If called with an argument of <i>extend</i>, moves the insertion cursor as in the case of no argument and extends the current selection.</p>
<dd>The forward-character() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>. If called with the <i>extend</i> argument, the forward-character() action may produce calls to the <code>XmNgainPrimaryCallback</code> procedures. See callback description for more information.</p>
<dt>forward-word(<code>extend</code>):</p>
<dd>If this action is called with no argument, moves the insertion cursor to the first whitespace character or end-of-line following the next non-whitespace character. If the insertion cursor is already at the end of a word, moves the insertion cursor to the end of the next word. This action may have different behavior in a locale other than the C locale.</p>
<dd>If called with an argument of <i>extend</i>, moves the insertion cursor as in the case of no argument and extends the current selection.</p>
<dd>The forward-word() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>. If called with the <i>extend</i> argument, the forward-word() action may produce calls to the <code>XmNgainPrimaryCallback</code> procedures. See callback description for more information.</p>
<dt>grab-focus():</p>
<dd>This key binding performs the action defined in the <code>XmNselectionArray</code>, depending on the number of multiple mouse clicks. The default selection array ordering is one click to move the insertion cursor to the pointer position, two clicks to select a word, and three clicks to select a line of text. A single click also deselects any selected text and sets the anchor at the pointer position. This action may have different behavior in a locale other than the C locale.</p>
<dd>The grab-focus() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>.</p>
<dt>Help():</p>
<dd>Calls the callbacks for <code>XmNhelpCallback</code> if any exist. If there are no help callbacks for this widget, this action calls the help callbacks for the nearest ancestor that has them.</p>
<dt>key-select(<code>right|left</code>):</p>
<dd>If called with an argument of <i>right</i>, moves the insertion cursor one character to the right and extends the current selection. If called with an argument of <i>left</i>, moves the insertion cursor one character to the left and extends the current selection. If called with no argument, extends the current selection.</p>
<dd>Note that after a <code>key-select</code> action, the selection will still begin at the original anchor, and will extend to the position indicated in the action call. If this new position is on the opposite side of the selection anchor from the previous selection boundary, the original selection will be deselected.</p>
<dd>The key-select() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>. The key-select() action may also produce calls to the <code>XmNgainPrimaryCallback</code> procedures. See callback description for more information.</p>
<dt>link-primary():</p>
<dd>Places a link to the primary selection just before the insertion cursor. This action calls the <code>XmNdestinationCallback</code> procedures for the <code>PRIMARY</code> selection and the <code>XmLINK</code> operation. The TextField widget itself performs no transfers; the <code>XmNdestinationCallback</code> procedures are responsible for inserting the link to the primary selection and for taking any related actions.</p>
<dt>link-to():</p>
<dd>If a secondary selection exists, this action places a link to the secondary selection at the insertion position of the destination component. This action calls the destination&#8217;s <code>XmNdestinationCallback</code> procedures for the <code>SECONDARY</code> selection and the <code>XmLINK</code> operation.</p>
<dd>If no secondary selection exists, this action places a link to the primary selection at the pointer position. This action calls the <code>XmNdestinationCallback</code> procedures for the <code>PRIMARY</code> selection and the <code>XmLINK</code> operation.</p>
<dd>The TextField widget itself performs no transfers; the <code>XmNdestinationCallback</code> procedures are responsible for inserting the link to the primary or secondary selection and for taking any related actions.</p>
<dt>move-destination():</p>
<dd>Moves the insertion cursor to the pointer position without changing any existing current selection. If there is a current selection, sets the widget as the destination widget. This also moves the widget focus to match the insertion cursor.</p>
<dd>The move-destination() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>.</p>
<dt>move-to():</p>
<dd>If a secondary selection exists, this action moves the secondary selection to the insertion position of the destination component. If the secondary selection is in the destination widget, and the secondary selection and the primary selection overlap, the result is undefined. This action calls the destination&#8217;s <code>XmNdestinationCallback</code> procedures for the <code>SECONDARY</code> selection and the <code>XmCOPY</code> operation. The destination&#8217;s <code>XmNdestinationCallback</code> procedures or the destination component itself invokes the selection owner&#8217;s <code>XmNconvertCallback</code> procedures, possibly multiple times, for the <code>SECONDARY</code> selection. If the transfer is successful, this action then calls the selection owner&#8217;s <code>XmNconvertCallback</code> procedures for the <code>SECONDARY</code> selection and the <code>DELETE</code> target.</p>
<dd>If no secondary selection exists, this action moves the primary selection to the pointer position. This action calls the <code>XmNdestinationCallback</code> procedures for the <code>PRIMARY</code> selection and the <code>XmMOVE</code> operation. It calls the selection owner&#8217;s <code>XmNconvertCallback</code> procedures, possibly multiple times, for the <code>PRIMARY</code> selection. If the transfer is successful, this action then calls the selection owner&#8217;s <code>XmNconvertCallback</code> procedures for the <code>PRIMARY</code> selection and the <code>DELETE</code> target.</p>
<dd>In addition, the move-to() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>, and the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>. This action may also produce calls to the <code>XmNgainPrimaryCallback</code> procedures.</p>
<dt>next-tab-group():</p>
<dd>Traverses to the next tab group.</p>
<dd>The next-tab-group() action produces no callbacks, unless it results in the widget losing focus, in which case, the <code>XmNlosingFocusCallback</code> procedures are called with reason value <code>XmCR_LOSING_FOCUS</code>.</p>
<dt>page-left():</p>
<dd>Scrolls the viewing window left one page of text.</p>
<dd>The page-left() action produces no callbacks.</p>
<dt>page-right():</p>
<dd>Scrolls the viewing window right one page of text.</p>
<dd>The page-right() action produces no callbacks.</p>
<dt>paste-clipboard():</p>
<dd>Pastes the contents of the clipboard before the insertion cursor. This action calls the <code>XmNdestinationCallback</code> procedures for the <code>CLIPBOARD</code> selection and the <code>XmCOPY</code> operation.</p>
<dd>The paste-clipboard() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>, and the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>.</p>
<dt>prev-tab-group():</p>
<dd>Traverses to the previous tab group.</p>
<dd>The prev-tab-group() action produces no callbacks, unless it results in the widget losing focus, in which case, the <code>XmNlosingFocusCallback</code> procedures are called with reason value <code>XmCR_LOSING_FOCUS</code>.</p>
<dt>process-bdrag()</p>
<dd>If the pointer is within the selection, this action starts a drag operation for the selection. This action sets the <code>XmNconvertProc</code> of the DragContext to a function that calls the <code>XmNconvertCallback</code> procedures, possibly multiple times, for the <code>_MOTIF_DROP</code> selection.</p>
<dd>If no selection exists or the pointer is outside the selection, this action prepares to start a secondary selection at the pointer position.</p>
<dt>process-cancel():</p>
<dd>Cancels the current extend-adjust(), secondary-adjust() or process-bdrag() operation and leaves the selection state as it was before the operation; otherwise, and if the parent is a manager, it passes the event to the parent.</p>
<dt>secondary-adjust():</p>
<dd>Extends the secondary selection to the pointer position.</p>
<dd>The secondary-adjust() action produces no callbacks.</p>
<dt>secondary-start():</p>
<dd>Marks the beginning of a secondary selection.</p>
<dd>The secondary-start() action produces no callbacks.</p>
<dt>select-all():</p>
<dd>Selects all text.</p>
<dd>The select-all() action can produce no callbacks, however, it may produce calls to the <code>XmNgainPrimaryCallback</code> and <code>XmNmotionVerifyCallback</code> procedures. See callback description for more information.</p>
<dt>self-insert():</p>
<dd>If <code>XmNpendingDelete</code> is True and the cursor is not disjoint from the current selection, deletes the entire selection. Inserts the character associated with the key pressed before the insertion cursor.</p>
<dd>The self-insert() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>, and the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>.</p>
<dt>set-anchor():</p>
<dd>Resets the anchor point for extended selections. Resets the destination of secondary selection actions.</p>
<dd>The set-anchor() action produces no callbacks.</p>
<dt>toggle-add-mode():</p>
<dd>Toggles the state of Add Mode.</p>
<dd>The toggle-add-mode() action produces no callbacks.</p>
<dt>toggle-overstrike():</p>
<dd>Toggles the state of the text insertion mode. By default, characters typed into the TextField widget are inserted before the position of the insertion cursor. In overstrike mode, characters entered into the TextField widget replace the characters that directly follow the insertion cursor. In overstrike mode, when the end of a line is reached, characters are appended to the end of the line.</p>
<dd>The following traversal actions generate no callbacks unless they result in the loss of focus by the widget in question, as when <code>XmNnavigationType</code> is <code>XmNONE</code>. In this case, they produce calls to the <code>XmNlosingFocusCallback</code> procedures, with reason value <code>XmCR_FOCUS_MOVED</code>.</p>
<dt>traverse-home():</p>
<dd>Traverses to the first widget in the tab group.</p>
<dt>traverse-next():</p>
<dd>Traverses to the next widget in the tab group.</p>
<dt>traverse-prev():</p>
<dd>Traverses to the previous widget in the tab group.</dl>
<h3>Additional Behavior</h3>
<p>This widget has the following additional behavior:</p>
<dl COMPACT>
<dt><code>&lt;FocusIn&gt;</code>:</p>
<dd>Draws the insertion cursor as solid and starts blinking the cursor.</p>
<dt><code>&lt;FocusOut&gt;</code>:</p>
<dd>Displays the insertion cursor as a stippled I-beam unless it is the destination widget.</dl>
<h3>Virtual Bindings</h3>
<p>The bindings for virtual keys are vendor specific. For information about bindings for virtual buttons and keys, see <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-core/">Core</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatetextfield/">XmCreateTextField</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlist/">XmFontList</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistappendentry/">XmFontListAppendEntry</a></code>(3), <code><a href="/docs/linux/man/3-xmprimitive/">XmPrimitive</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfieldclearselection/">XmTextFieldClearSelection</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfieldcopy/">XmTextFieldCopy</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfieldcopylink/">XmTextFieldCopyLink</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfieldcut/">XmTextFieldCut</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfieldgetbaseline/">XmTextFieldGetBaseline</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfieldgeteditable/">XmTextFieldGetEditable</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfieldgetinsertionposition/">XmTextFieldGetInsertionPosition</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfieldgetlastposition/">XmTextFieldGetLastPosition</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfieldgetmaxlength/">XmTextFieldGetMaxLength</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfieldgetselection/">XmTextFieldGetSelection</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfieldgetselectionposition/">XmTextFieldGetSelectionPosition</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfieldgetselectionwcs/">XmTextFieldGetSelectionWcs</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfieldgetstring/">XmTextFieldGetString</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfieldgetstringwcs/">XmTextFieldGetStringWcs</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfieldgetsubstring/">XmTextFieldGetSubstring</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfieldgetsubstringwcs/">XmTextFieldGetSubstringWcs</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfieldinsert/">XmTextFieldInsert</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfieldinsertwcs/">XmTextFieldInsertWcs</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfieldpaste/">XmTextFieldPaste</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfieldpastelink/">XmTextFieldPasteLink</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfieldpostoxy/">XmTextFieldPosToXY</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfieldremove/">XmTextFieldRemove</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfieldreplace/">XmTextFieldReplace</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfieldreplacewcs/">XmTextFieldReplaceWcs</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfieldsetaddmode/">XmTextFieldSetAddMode</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfieldseteditable/">XmTextFieldSetEditable</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfieldsethighlight/">XmTextFieldSetHighlight</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfieldsetinsertionposition/">XmTextFieldSetInsertionPosition</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfieldsetmaxlength/">XmTextFieldSetMaxLength</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfieldsetselection/">XmTextFieldSetSelection</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfieldsetstring/">XmTextFieldSetString</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfieldsetstringwcs/">XmTextFieldSetStringWcs</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfieldshowposition/">XmTextFieldShowPosition</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfieldxytopos/">XmTextFieldXYToPos</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatetextfield/">XmVaCreateTextField</a></code>(3), and <code><a href="/docs/linux/man/3-xmvacreatemanagedtextfield/">XmVaCreateManagedTextField</a></code>(3).</p>
