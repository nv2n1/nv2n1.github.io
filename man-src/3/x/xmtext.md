---
title: "xmtext(3)"
name: "xmtext"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtext/"
description: "XmText — The Text widget class"
---

<p><code>XmText</code> &#8212; The Text widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Text.h&gt;</pre>
<h2>Description</h2>
<p>Text provides a single-line and multiline text editor for customizing both user and programmatic interfaces. It can be used for single-line string entry, forms entry with verification procedures, and full-window editing. It provides an application with a consistent editing system for textual data. The screen&#8217;s textual data adjusts to the application writer&#8217;s needs. </p>
<p> Text provides separate callback lists to verify movement of the insert cursor, modification of the text, and changes in input focus. Each of these callbacks provides the verification function with the widget instance, the event that caused the callback, and a data structure specific to the verification type. From this information, the function can verify if the application considers this to be a legitimate state change and can signal the widget whether to continue with the action. </p>
<p> The user interface tailors a new set of translations. The default translations provide key bindings for insert cursor movement, deletion, insertion, and selection of text. </p>
<p> Text allows the user to select regions of text. Selection is based on the model specified in the <i>Inter-Client Communication Conventions Manual</i> (ICCCM). Text supports primary and secondary selection. </p>
<p> In some Asian languages, texts are drawn vertically. Also, some characters are displayed with 90-degree clockwise rotation, and other characters are mapped to vertical glyphs that differ from the normal horizaontal glyphs. Information about which characters require rotation or mapping to vertical glyphs is specified in the X Locale Database (NLS databases) and handled by X library, depending on <code>XNOrientation</code> <code>XOC</code> values. <code>XmText</code> widget should also handle the vertically aligned lines as for editing, entering, or selecting texts. </p>
<p> The vertical writing feature of the <code>XmText</code> widget is enabled when the <code>XmTOP_TO_BOTTOM</code> value is specified for the <code>XmNlayoutDirection</code> resource of the <code>XmText</code> widget. In that case, the horizontal scroll bar is displayed on the bottom of the <code>XmText</code> widget and the vertical scroll bar is displayed on the left side.</p>
<h3>Mouse Selection</h3>
<p>The Text widget allows text to be edited, inserted, and selected. The user can cut, copy, and paste text by using the clipboard, primary transfer, or secondary transfer. Text also provides a Drag and Drop facility that enables the user to copy or move data within Text or to a different widget. When keyboard focus policy is set to EXPLICIT, the widget that receives focus is the destination widget. In POINTER mode, any keyboard or mouse operation (except secondary selection) in an editable widget establishes that widget as the destination. </p>
<p> If a destination widget becomes insensitive or uneditable, it forfeits its destination status. In EXPLICIT mode, when a widget becomes insensitive, the focus moves to another widget. If that widget is editable, it becomes the destination widget; otherwise, there is no destination widget. The text of any insensitive Text widget is stippled, indicating its state to the user. </p>
<p> The insertion cursor, displayed as an I-beam, shows where input is inserted. Input is inserted just before the insertion cursor. </p>
<p> Text uses the <code>XmQTnavigator</code>, <code>XmQTspecifyRenderTable</code>, and <code>XmQTscrollFrame</code> traits, and holds the <code>XmQTaccessTextual</code> and <code>XmQTtransfer</code> traits. The widget checks its parent for the <code>XmQTscrollFrame</code> trait. If this trait does not exist, then the widget has no scrolling. If the trait does exist, and the ScrollFrame widget has not been initialized, the widget creates two navigators and sets up the scrollbars. </p>
<p> If an application or widget calls the <code>setValue</code> trait method of <code>XmQTaccessTextual</code>, then <code>XmText</code> will call <code>XmTextSetString</code> to set the string value.</p>
<h3>Classes</h3>
<p>Text inherits behavior, resources, and traits from <code>Core</code> and <code>XmPrimitive</code>. </p>
<p> The class pointer is <code>xmTextWidgetClass</code>. </p>
<p> The class name is <code>XmText</code>.</p>
<h3>Data Transfer Behavior</h3>
<p>Text supports transfer of the primary, secondary, and clipboard selections and dragging of selected text from the widget. Text can also be the destination for the primary, secondary, and clipboard selections, and it supports dropping of data being dragged onto the widget. </p>
<p> When the <code>XmNconvertCallback</code> procedures are called, the <code>location_data</code> member of the <code>XmConvertCallbackStruct</code> member is NULL if the selected text is being transferred. If the entire text, not the selected text, is being transferred, the value of this member is the widget ID of the Text widget. </p>
<p> As a source of data, Text supports the following targets and associated conversions of data to these targets:</p>
<dl COMPACT>
<dt><i>locale</i></p>
<dd>If the <i>locale</i> target matches the widget&#8217;s locale, the widget transfers the selected text in the encoding of the locale.</p>
<dt><code>COMPOUND_TEXT</code></p>
<dd>The widget transfers the selected text as type <code>COMPOUND_TEXT</code>.</p>
<dt><code>STRING</code></p>
<dd>The widget transfers the selected text as type <code>STRING</code>.</p>
<dt><code>TEXT</code></p>
<dd>If the selected text is fully convertible to the encoding of the locale, the widget transfers the selected text in the encoding of the locale. Otherwise, the widget transfers the selected text as type <code>COMPOUND_TEXT</code>.</p>
<dt><code>UTF8_STRING</code></p>
<dd>The widget transfers the selected text as type <code>UTF8_STRING</code>.</p>
<dt><code>DELETE</code></p>
<dd>The widget deletes the selected text.</p>
<dt><code>_MOTIF_CLIPBOARD_TARGETS</code></p>
<dd>The widget transfers, as type <code>ATOM</code>, a list of the targets to which the widget can convert data to be placed on the clipboard immediately. If the selected text is fully convertible to <code>STRING</code>, these include <code>STRING</code>; otherwise, they include <code>COMPOUND_TEXT</code>.</p>
<dt><code>_MOTIF_DEFERRED_CLIPBOARD_TARGETS</code></p>
<dd>The widget transfers, as type <code>ATOM</code>, a list of the targets it supports for delayed transfer for the <code>CLIPBOARD</code> selection. This widget currently supplies no targets for <code>_MOTIF_DEFERRED_CLIPBOARD_TARGETS</code>.</p>
<dt><code>_MOTIF_EXPORT_TARGETS</code></p>
<dd>The widget transfers, as type <code>ATOM</code>, a list of the targets to be used as the value of the DragContext&#8217;s <code>XmNexportTargets</code> in a drag-and-drop transfer. These include <code>COMPOUND_TEXT</code>, <code>UTF8_STRING</code>, the encoding of the locale, <code>STRING</code>, <code>TEXT</code>, <code>BACKGROUND</code>, and <code>FOREGROUND</code>.</p>
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
<dd>When losing the <code>_MOTIF_DESTINATION</code> selection, if the widget does not have focus, it changes the cursor to indicate that the widget is no longer the destination.</dl>
</dl>
</dl>
<p> As a source of data, Text also supports the following standard Motif targets:</p>
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
<dd>The widget transfers, as type <code>ATOM</code>, a list of the targets it supports. These include the standard targets in this list. These also include <code>COMPOUND_TEXT</code>, <code>UTF8_STRING</code>, the encoding of the locale, <code>STRING</code>, and <code>TEXT</code>.</p>
<dt><code>TIMESTAMP</code></p>
<dd>The widget transfers the timestamp used to acquire the selection as type <code>INTEGER</code>.</p>
<dt><code>_MOTIF_RENDER_TABLE</code></p>
<dd>The widget transfers <code>XmNrenderTable</code> if it exists, or else the default text render table, as type <code>STRING</code>.</p>
<dt><code>_MOTIF_ENCODING_REGISTRY</code></p>
<dd>The widget transfers its encoding registry as type <code>STRING</code>. The value is a list of NULL separated items in the form of tag encoding pairs. This target symbolizes the transfer target for the Motif Segment Encoding Registry. Widgets and applications can use this Registry to register text encoding formats for specified render table tags. Applications access this Registry by calling <code>XmRegisterSegmentEncoding</code> and <code>XmMapSegmentEncoding</code>.</dl>
<p> As a destination for data, Text chooses a target and requests conversion of the selection to that target. If the encoding of the locale is present in the list of available targets, Text chooses a requested target from the available targets in the following order of preference:</p>
<dl COMPACT>
<dt> 1.</p>
<dd>The encoding of the locale</p>
<dt> 2.</p>
<dd><code>TEXT</code></p>
<dt> 4.</p>
<dd><code>UTF8_STRING</code></p>
<dt> 3.</p>
<dd><code>COMPOUND_TEXT</code></p>
<dt> 4.</p>
<dd><code>STRING</code></dl>
<p> If the encoding of the locale is not present in the list of available targets, Text chooses a requested target from the available targets in the following order of preference:</p>
<dl COMPACT>
<dt> 4.</p>
<dd><code>UTF8_STRING</code></p>
<dt> 1.</p>
<dd><code>COMPOUND_TEXT</code></p>
<dt> 2.</p>
<dd><code>STRING</code></dl>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmText Resource Set</code>
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
<td>XmNautoShowCursorPosition</td>
<td>XmCAutoShowCursorPosition</td>
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
<td>XmNeditMode</td>
<td>XmCEditMode</td>
<td>int</td>
<td>XmSINGLE_LINE_EDIT</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
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
<td>XmtotalLines</td>
<td>XmCTotalLines</td>
<td>int</td>
<td>dynamic</td>
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
<td>XmNsource</td>
<td>XmCSource</td>
<td>XmTextSource</td>
<td>Default source</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtopCharacter</td>
<td>XmCTopCharacter</td>
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
<td>XmCvalueWcs</td>
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
</table>
</table>
<p> 1 This resource cannot be set in a resource file.</p>
<dl COMPACT>
<dt><code>XmNactivateCallback</code></p>
<dd>Specifies the list of callbacks that is called when the user invokes an event that calls the activate() action. The type of the structure whose address is passed to this callback is <code>XmAnyCallbackStruct</code>. The reason sent by the callback is <code>XmCR_ACTIVATE</code>.</p>
<dt><code>XmNautoShowCursorPosition</code></p>
<dd>Ensures that the visible text contains the insert cursor when set to True. If the insert cursor changes, the contents of Text may scroll in order to bring the insertion point into the window. Setting this resource to False, however, does not ensure that Text will not scroll.</p>
<dt><code>XmNcursorPosition</code></p>
<dd>Indicates the position in the text where the current insert cursor is to be located. Position is determined by the number of characters from the beginning of the text. The first character position is 0 (zero).</p>
<dt><code>XmNcursorPositionVisible</code></p>
<dd>If the widget has an <code>XmPrintShell</code> as one of its ancestors, then the default value is <code>False</code>; otherwise, it is <code>True</code>.</p>
<dt><code>XmNdestinationCallback</code></p>
<dd>Specifies a list of callbacks called when the widget is the destination of a transfer operation. The type of the structure whose address is passed to these callbacks is <code>XmDestinationCallbackStruct</code>. The reason is <code>XmCR_OK</code>.</p>
<dt><code>XmNeditable</code></p>
<dd>When set to True, indicates that the user can edit the text string. Prohibits the user from editing the text when set to False.</p>
<dd>When <code>XmNeditable</code> is used on a widget it sets the dropsite to <code>XmDROP_SITE_ACTIVE</code>.</p>
<dt><code>XmNeditMode</code></p>
<dd>Specifies the set of keyboard bindings used in Text. The default, <code>XmSINGLE_LINE_EDIT</code>, provides the set of key bindings to be used in editing single-line text. <code>XmMULTI_LINE_EDIT</code> provides the set of key bindings to be used in editing multiline text.</p>
<dd>The results of placing a Text widget inside a ScrolledWindow when the Text&#8217;s <code>XmNeditMode</code> is <code>XmSINGLE_LINE_EDIT</code> are undefined.</p>
<dt><code>XmNfocusCallback</code></p>
<dd>Specifies the list of callbacks called when Text accepts input focus. The type of the structure whose address is passed to this callback is <code>XmAnyCallbackStruct</code>. The reason sent by the callback is <code>XmCR_FOCUS</code>.</p>
<dt><code>XmNgainPrimaryCallback</code></p>
<dd>Specifies the list of callbacks called when an event causes the Text widget to gain ownership of the primary selection. The reason sent by the callback is <code>XmCR_GAIN_PRIMARY</code>.</p>
<dt><code>XmNlosePrimaryCallback</code></p>
<dd>Specifies the list of callbacks called when an event causes the Text widget to lose ownership of the primary selection. The reason sent by the callback is <code>XmCR_LOSE_PRIMARY</code>.</p>
<dt><code>XmNlosingFocusCallback</code></p>
<dd>Specifies the list of callbacks called before Text loses input focus. The type of the structure whose address is passed to this callback is <code>XmTextVerifyCallbackStruct</code>. The reason sent by the callback is <code>XmCR_LOSING_FOCUS</code>.</p>
<dt><code>XmNmarginHeight</code></p>
<dd>Specifies the distance between the top edge of the widget window and the text, and between the bottom edge of the widget window and the text.</p>
<dt><code>XmNmarginWidth</code></p>
<dd>Specifies the distance between the left edge of the widget window and the text, and between the right edge of the widget window and the text.</p>
<dt><code>XmNmaxLength</code></p>
<dd>Specifies the maximum length of the text string that can be entered into text from the keyboard. This value must be nonnegative. Strings that are entered by using the <code>XmNvalue</code> resource or the <code>XmTextSetString</code> function ignore this resource.</p>
<dt><code>XmNmodifyVerifyCallback</code></p>
<dd>Specifies the list of callbacks called before text is deleted from or inserted into Text. The type of the structure whose address is passed to this callback is <code>XmTextVerifyCallbackStruct</code>. The reason sent by the callback is <code>XmCR_MODIFYING_TEXT_VALUE</code>. When multiple Text widgets share the same source, only the widget that initiates the source change will generate <code>XmNmodifyVerifyCallback</code>.</p>
<dd>If both <code>XmNmodifyVerifyCallback</code> and <code>XmNmodifyVerifyCallbackWcs</code> are registered callback lists, the procedure(s) in the <code>XmNmodifyVerifyCallback</code> list is always executed first; and the resulting data, which may have been modified, is passed to the <code>XmNmodifyVerifyCallbackWcs</code> callback routines.</p>
<dt><code>XmNmodifyVerifyCallbackWcs</code></p>
<dd>Specifies the list of callbacks called before text is deleted from or inserted into Text. The type of the structure whose address is passed to this callback is <code>XmTextVerifyCallbackStructWcs</code>. The reason sent by the callback is <code>XmCR_MODIFYING_TEXT_VALUE</code>. When multiple Text widgets share the same source, only the widget that initiates the source change will generate the <code>XmNmodifyVerifyCallbackWcs</code>.</p>
<dd>If both <code>XmNmodifyVerifyCallback</code> and <code>XmNmodifyVerifyCallbackWcs</code> are registered callback lists, the procedure(s) in the <code>XmNmodifyVerifyCallback</code> list is always executed first; and the resulting data, which may have been modified, is passed to the <code>XmNmodifyVerifyCallbackWcs</code> callback routines.</p>
<dt><code>XmNmotionVerifyCallback</code></p>
<dd>Specifies the list of callbacks called before the insert cursor is moved to a new position. The type of the structure whose address is passed to this callback is <code>XmTextVerifyCallbackStruct</code>. The reason sent by the callback is <code>XmCR_MOVING_INSERT_CURSOR</code>. It is possible for more than one <code>XmNmotionVerifyCallback</code> to be generated from a single action.</p>
<dt><code>XmNsource</code></p>
<dd>Specifies the source with which the widget displays text. If no source is specified, the widget creates a default string source. This resource can be used to share text sources between Text widgets.</p>
<dt><code>XmNtopCharacter</code></p>
<dd>Displays the position of text at the top of the window. Position is determined by the number of characters from the beginning of the text. The first character position is 0 (zero).</p>
<dd>If the <code>XmNeditMode</code> is <code>XmMULTI_LINE_EDIT</code>, the line of text that contains the top character is displayed at the top of the widget without shifting the text left or right. <code>XtGetValues</code> for <code>XmNtopCharacter</code> returns the position of the first character in the line that is displayed at the top of the widget.</p>
<dt><code>XmNtotalLines</code></p>
<dd>Indicates the number of lines in the text widget buffer (not necessarily visible). The initial value 1 means the text buffer is empty. The number of lines reported takes into account the <code>wordWrap</code> policy (that is, it&#8217;s not simply the number of newline characters.</p>
<dt><code>XmNvalue</code></p>
<dd>Specifies the string value of the Text widget as a <code>char*</code> data value. Moves the cursor to position 0 unless a value of <code>XmNcursorPosition</code> was explicitly supplied in the argument list. If <code>XmNvalue</code> and <code>XmNvalueWcs</code> are both defined, the value of <code>XmNvalueWcs</code> supersedes that of <code>XmNvalue</code>. <code>XtGetValues</code> returns a copy of the value of the internal buffer and <code>XtSetValues</code> copies the string values into the internal buffer.</p>
<dt><code>XmNvalueChangedCallback</code></p>
<dd>Specifies the list of callbacks called after text is deleted from or inserted into Text. The type of the structure whose address is passed to this callback is <code>XmAnyCallbackStruct</code>. The reason sent by the callback is <code>XmCR_VALUE_CHANGED</code>. When multiple Text widgets share the same source, only the widget that initiates the source change will generate the <code>XmNvalueChangedCallback</code>. This callback represents a change in the source in the Text, not in the Text widget. The <code>XmNvalueChangedCallback</code> should occur only in pairs with an <code>XmNmodifyVerifyCallback</code>, assuming that the <i>doit</i> flag in the callback structure of the <code>XmNmodifyVerifyCallback</code> is not set to False.</p>
<dt><code>XmNvalueWcs</code></p>
<dd>Specifies the string value of the Text widget as a <code>wchar_t*</code> data value. Moves the cursor to position 0 unless a value of <code>XmNcursorPosition</code> was explicitly supplied in the argument list.</p>
<dd>This resource cannot be specified in a resource file.</p>
<dd>If <code>XmNvalue</code> and <code>XmNvalueWcs</code> are both defined, the value of <code>XmNvalueWcs</code> supersedes that of <code>XmNvalue</code>. <code>XtGetValues</code> returns a copy of the value of the internal buffer encoded as a wide character string. <code>XtSetValues</code> copies the value of the wide character string into the internal buffer.</p>
<dt><code>XmNverifyBell</code></p>
<dd>Specifies whether the bell should sound when the verification returns without continuing the action. The default depends on the value of the ancestor VendorShell&#8217;s <code>XmNaudibleWarning</code> resource. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmText Input Resource Set</code>
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
<td>XmNpendingDelete</td>
<td>XmCPendingDelete</td>
<td>Boolean</td>
<td>True</td>
<td>CSG
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
<td>XmNselectionArrayCount</td>
<td>XmCSelectionArrayCount</td>
<td>int</td>
<td>4</td>
<td>CSG
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
</table>
</table>
<dt><code>XmNpendingDelete</code></p>
<dd>Indicates that pending delete mode is on when the Boolean value is True. Pending deletion is defined as deletion of the selected text when an insertion is made.</p>
<dt><code>XmNselectionArray</code></p>
<dd>Defines the actions for multiple mouse clicks. The value of the resource is an array of <code>XmTextScanType</code> elements. <code>XmTextScanType</code> is an enumeration indicating possible actions. Each mouse click performed within some time of the previous mouse click increments the index into this array and performs the defined action for that index. (This &quot;multiclick&quot; time is specified by the operating environment, and varies among different systems. In general, it is usually set to some fraction of a second.) The possible actions in the order they occur in the default array are as follows:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> 3.</p>
<dd><code>XmSELECT_POSITION</code>, which resets the insert cursor position.</p>
<dt> 4.</p>
<dd><code>XmSELECT_WORD</code>, which selects a word.</p>
<dt> 5.</p>
<dd><code>XmSELECT_LINE</code>, which selects a line of text. This action sees a line as delimited by <i>hard</i> newline characters. In other words, if the word wrap feature is on (<code>XmNwordWrap</code> is True), this will ignore the newlines automatically inserted by the widget. This is the default.</p>
<dt> 6.</p>
<dd><code>XmSELECT_OUT_LINE</code>, which selects a line of text. This action sees a line as delimited by <i>hard</i> or <i>soft</i> newline characters. In other words, if the word wrap feature is on (<code>XmNwordWrap</code> is True), the newlines automatically inserted by the widget will be treated as delimiting lines.</p>
<dt> 7.</p>
<dd><code>XmSELECT_ALL</code>, which selects all of the text.</dl>
</dl>
<dt><code>XmNselectionArrayCount</code></p>
<dd>Indicates the number of elements in the <code>XmNselectionArray</code> resource. The value must not be negative.</p>
<dt><code>XmNselectThreshold</code></p>
<dd>Specifies the number of pixels of motion that is required to select the next character when selection is performed using the click-drag mode of selection. The value must not be negative. This resource also specifies whether a drag should be started and the number of pixels to start a drag when <code>Btn2Down</code> and <code>Btn1Down</code> are integrated. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmText Output Resource Set</code>
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
<td>XmNblinkRate</td>
<td>XmCBlinkRate</td>
<td>int</td>
<td>500</td>
<td>CSG
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
<td>XmNcursorPositionVisible</td>
<td>XmCCursorPositionVisible</td>
<td>Boolean</td>
<td>True</td>
<td>CSG
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
<td>XmNrenderTable</td>
<td>XmCRenderTable</td>
<td>XmRenderTable</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNresizeHeight</td>
<td>XmCResizeHeight</td>
<td>Boolean</td>
<td>False</td>
<td>CSG
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
<td>XmNrows</td>
<td>XmCRows</td>
<td>short</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNwordWrap</td>
<td>XmCWordWrap</td>
<td>Boolean</td>
<td>False</td>
<td>CSG
</td>
</tr>
</table>
</table>
<dt><code>XmNblinkRate</code></p>
<dd>Specifies the blink rate of the text cursor in milliseconds. The time indicated in the blink rate relates to the time the cursor is visible and the time the cursor is invisible (that is, the time it takes to blink the insertion cursor on and off is twice the blink rate). The cursor does not blink when the blink rate is set to 0 (zero). The value must not be negative.</p>
<dt><code>XmNcolumns</code></p>
<dd>Specifies the initial width of the text window as an integer number of characters. The width equals the number of characters specified by this resource multiplied by the width as derived from the specified font. If the em-space value is available, it is used. If not, the width of the numeral &quot;0&quot; is used. If this is not available, the maximum width is used. For proportionate fonts, the actual number of characters that fit on a given line may be greater than the value specified. The value must be greater than 0 (zero). The default value depends on the value of the <code>XmNwidth</code> resource. If no width is specified the default is 20.</p>
<dd>When the <code>XmNlayoutDirection</code> resource is <code>XmTOP_TO_BOTTOM</code>, and if the <code>XmText</code> widget resource <code>XmNeditMode</code> is <code>XmSINGLE_LINE_EDIT</code>, this attribute is ignored. If no width is specified, the default is 1.</p>
<dt><code>XmNcursorPositionVisible</code></p>
<dd>Indicates that the insert cursor position is marked by a text cursor when the Boolean value is True.</p>
<dt><code>XmNfontList</code></p>
<dd>Specifies the font list to be used for Text. The font list is an obsolete structure and is retained only for compatibility with earlier releases of Motif. Use the render table (<code>XmNrenderTable</code>) instead of font lists wherever possible. If both are specified, the render table will take precedence. If this value is NULL at initialization, the parent hierarchy of the widget is searched for an ancestor that holds the <code>XmQTspecifyRenderTable</code> trait. If such an ancestor is found, the font list is initialized to the <code>XmTEXT_RENDER_TABLE</code> value of the ancestor widget. If no such ancestor is found, the default is implementation dependent.</p>
<dd>Text searches the font list for the first occurrence of a font set that has <code>XmFONTLIST_DEFAULT_TAG</code>. If a default element is not found, the first font set in the font list is used. If the list contains no font sets, the first font in the font list will be used. Refer to <code><a href="/docs/linux/man/3-xmfontlist/">XmFontList</a></code>(3) for more information on a font list structure.</p>
<dt><code>XmNrenderTable</code></p>
<dd>Specifies the render table to be used in deriving a font set or font for rendering text. If both a render table and a font list are specified, the render table will take precedence. If the value of <code>XmNrenderTable</code> is NULL at initialization, the parent hierarchy of the widget is searched for an ancestor that holds the <code>XmQTspecifyRenderTable</code> trait. If such an ancestor is found, the font list is initialized to the <code>XmTEXT_RENDER_TABLE</code> value of the ancestor widget. If no such ancestor is found, the default is implementation dependent.</p>
<dd>Text searches the render table for the first occurrence of a rendition that has the tag <code>_MOTIF_DEFAULT_LOCALE</code>. If a default element is not found, the first rendition in the table is used. Refer to <code><a href="/docs/linux/man/3-xmrendertable/">XmRenderTable</a></code>(3) for more information on the render table structure.</p>
<dt><code>XmNresizeHeight</code></p>
<dd>Indicates that Text will attempt to resize its height to accommodate all the text contained in the widget when the Boolean value is True. If the Boolean value is set to True, the text is always displayed, starting from the first position in the source, even if instructed otherwise. This attribute is ignored when the application uses a Text widget whose parent is a ScrolledWindow and when <code>XmNscrollVertical</code> is True.</p>
<dd>When the <code>XmNlayoutDirection</code> resource is <code>XmTOP_TO_BOTTOM</code>, this resource indicates that the text attempts to resize its height to accommodate all the text contained in the widget when the Boolean value is <code>True</code>. This attribute is ignored if <code>XmNwordWrap</code> is <code>True</code>.</p>
<dt><code>XmNresizeWidth</code></p>
<dd>Indicates that Text attempts to resize its width to accommodate all the text contained in the widget when the Boolean value is True. This attribute is ignored if <code>XmNwordWrap</code> is True.</p>
<dd>When the <code>XmNlayoutDirection</code> resource is <code>XmTOP_TO_BOTTOM</code>, this attribute is still effective even if <code>XmNwordWrap</code> is <code>True</code>. Also, this attribute is ignored when the application uses a text widget whose parent is a <code>ScrolledWindow</code> and <code>XmNscrollHorizaontal</code> is <code>True</code>.</p>
<dt><code>XmNrows</code></p>
<dd>Specifies the initial height of the text window measured in character heights. This attribute is ignored if the text widget resource <code>XmNeditMode</code> is <code>XmSINGLE_LINE_EDIT</code>. The value must be greater than 0 (zero). The default value depends on the value of the <code>XmNheight</code> resource. If no height is specified, the default is 1.</p>
<dd>When the <code>XmNlayoutDirection</code> resource is <code>XmTOP_TO_BOTTOM</code>, this attribute is still effective, even if the <code>XmText</code> widget resource <code>XmNeditMode</code> is <code>XmSINGLE_LINE_EDIT</code>. If no height is specified, the default is 20.</p>
<dt><code>XmNwordWrap</code></p>
<dd>Indicates that lines are to be broken at word breaks (that is, the text does not go off the right edge of the window) when the Boolean value is True. Words are defined as a sequence of characters separated by whitespace. Whitespace is defined as a space, tab, or newline. This attribute is ignored if the text widget resource <code>XmNeditMode</code> is <code>XmSINGLE_LINE_EDIT</code>. Note that this resource is only valid when the widget is not a scroll one, or, if the widget is a scroll widget, that the <code>XmNscrollHorizontal</code> resource is False.</p>
<dd>Indicates that lines are to be broken at word breaks (that is, when the <code>XmNlayoutDirection</code> resource is <code>XmTOP_TO_BOTTOM</code>, the text does not go off the bottom edge of the window) when the Boolean value is <code>True</code>.</dl>
<p> The following resources are used only when text is created in a ScrolledWindow. See the reference page for <code>XmCreateScrolledText</code>. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmText Scrolling Resource Set</code>
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
<td>XmNscrollHorizontal</td>
<td>XmCScroll</td>
<td>Boolean</td>
<td>True</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td>XmNscrollLeftSide</td>
<td>XmCScrollSide</td>
<td>Boolean</td>
<td>False</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td>XmNscrollTopSide</td>
<td>XmCScrollSide</td>
<td>Boolean</td>
<td>False</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td>XmNscrollVertical</td>
<td>XmCScroll</td>
<td>Boolean</td>
<td>True</td>
<td>CG
</td>
</tr>
</table>
</table>
<p> Note in connection with this table that if the <code>XmNlayoutDirection</code> resource is <code>XmTOP_TO_BOTTOM</code>, the default is <code>True</code>.</p>
<dl COMPACT>
<dt><code>XmNscrollHorizontal</code></p>
<dd>Adds a ScrollBar that allows the user to scroll horizontally through text when the Boolean value is True. This resource is forced to False when the Text widget is placed in a ScrolledWindow with <code>XmNscrollingPolicy</code> set to <code>XmAUTOMATIC</code>.</p>
<dd>When the <code>XmNlayoutDirection</code> resource is <code>XmTOP_TO_BOTTOM</code>, this attribute is ignored if the <code>XmText</code> widget resource <code>XmNeditMode</code> is <code>XmSINGLE_LINE_EDIT</code>.</p>
<dt><code>XmNscrollLeftSide</code></p>
<dd>Indicates that the vertical ScrollBar should be placed on the left side of the scrolled text window when the Boolean value is True. This attribute is ignored if <code>XmNscrollVertical</code> is False or the Text resource <code>XmNeditMode</code> is <code>XmSINGLE_LINE_EDIT</code>.</p>
<dd>When the <code>XmNlayoutDirection</code> resource is <code>XmTOP_TO_BOTTOM</code>, this resource is still effective, even if the XmText widget resource <code>XmNeditMode</code> is <code>XmSINGLE_LINE_EDIT</code>.</p>
<dt><code>XmNscrollTopSide</code></p>
<dd>Indicates that the horizontal ScrollBar should be placed on the top side of the scrolled text window when the Boolean value is True.</p>
<dd>When the <code>XmNlayoutDirection</code> resource is <code>XmTOP_TO_BOTTOM</code>, this attribute is ignored if <code>XmNscrollHorizontal</code> is <code>False</code> or the <code>Xmtext</code> resource <code>XmNeditMode</code> is <code>XmSINGLE_LINE_EDIT</code>.</p>
<dt><code>XmNscrollVertical</code></p>
<dd>Adds a ScrollBar that allows the user to scroll vertically through text when the Boolean value is True. This attribute is ignored if the Text resource <code>XmNeditMode</code> is <code>XmSINGLE_LINE_EDIT</code>. This resource is forced to False when the Text widget is placed in a ScrolledWindow with <code>XmNscrollingPolicy</code> set to <code>XmAUTOMATIC</code>.</p>
<dd>When the <code>XmNlayoutDirection</code> resource is <code>XmTOP_TO_BOTTOM</code>, this resource is still effective, even if the <code>XmText</code> widget resource <code>XmNeditMode</code> is <code>XmSINGLE_LINE_EDIT</code>.</dl>
<h3>Inherited Resources</h3>
<p>Text inherits behavior and resources from the superclasses described in the following tables. For a complete description of each resource, refer to the reference page for that superclass. </p>
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
<td>XmNbottomShadowColor</td>
<td>XmCBottomShadowColor</td>
<td>Pixel</td>
<td>dynamic</td>
<td>CSG
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
<td>XmNconvertCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
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
<td>XmNhelpCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
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
<td>XmNhighlightOnEnter</td>
<td>XmCHighlightOnEnter</td>
<td>Boolean</td>
<td>False</td>
<td>CSG
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
<td>XmNhighlightThickness</td>
<td>XmCHighlightThickness</td>
<td>Dimension</td>
<td>2</td>
<td>CSG
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
<td>XmNnavigationType</td>
<td>XmCNavigationType</td>
<td>XmNavigationType</td>
<td>XmTAB_GROUP</td>
<td>CSG
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
<td>XmNshadowThickness</td>
<td>XmCShadowThickness</td>
<td>Dimension</td>
<td>2</td>
<td>CSG
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
<td>XmNtopShadowPixmap</td>
<td>XmCTopShadowPixmap</td>
<td>Pixmap</td>
<td>dynamic</td>
<td>CSG
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
<td>XmNunitType</td>
<td>XmCUnitType</td>
<td>unsigned char</td>
<td>dynamic</td>
<td>CSG
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
<td>XmNaccelerators</td>
<td>XmCAccelerators</td>
<td>XtAccelerators</td>
<td>dynamic</td>
<td>CSG
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
<td>XmNbackground</td>
<td>XmCBackground</td>
<td>Pixel</td>
<td>dynamic</td>
<td>CSG
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
<td>XmNborderColor</td>
<td>XmCBorderColor</td>
<td>Pixel</td>
<td>XtDefaultForeground</td>
<td>CSG
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
<td>XmNborderWidth</td>
<td>XmCBorderWidth</td>
<td>Dimension</td>
<td>0</td>
<td>CSG
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
<td>XmNdepth</td>
<td>XmCDepth</td>
<td>int</td>
<td>dynamic</td>
<td>CG
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
<td>XmNheight</td>
<td>XmCHeight</td>
<td>Dimension</td>
<td>dynamic</td>
<td>CSG
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
<td>XmNmappedWhenManaged</td>
<td>XmCMappedWhenManaged</td>
<td>Boolean</td>
<td>True</td>
<td>CSG
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
<td>XmNsensitive</td>
<td>XmCSensitive</td>
<td>Boolean</td>
<td>True</td>
<td>CSG
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
<td>XmNwidth</td>
<td>XmCWidth</td>
<td>Dimension</td>
<td>dynamic</td>
<td>CSG
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
<td>XmNy</td>
<td>XmCPosition</td>
<td>Position</td>
<td>0</td>
<td>CSG
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
<p> The Text widget defines a new callback structure for use with verification callbacks. Note that not all fields are relevant for every callback reason. The application must first look at the <i>reason</i> field and use only the structure members that are valid for the particular reason. The values <i>startPos</i>, <i>endPos</i>, and <i>text</i> in the callback structure <code>XmTextVerifyCallbackStruct</code> may be modified when the callback is received, and these changes will be reflected as changes made to the source of the Text widget. (For example, all keystrokes can be converted to spaces or NULL characters when a password is entered into a Text widget.) The application programmer should not overwrite the <i>text</i> field, but should attach data to that pointer. </p>
<p> A pointer to the following structure is passed to callbacks for <code>XmNlosingFocusCallback</code>, <code>XmNmodifyVerifyCallback</code>, and <code>XmNmotionVerifyCallback</code>: </p>
<pre>typedef struct
{
 int <i>reason</i>;
 XEvent <i>* event</i>;
 Boolean <i>doit</i>;
 XmTextPosition <i>currInsert, newInsert</i>;
 XmTextPosition <i>startPos, endPos</i>;
 XmTextBlock <i>text</i>;
} XmTextVerifyCallbackStruct, *XmTextVerifyPtr;</pre>
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
<dd>Points to a structure of type <code>XmTextBlockRec</code>. This structure holds the textual information to be inserted.</dl>
<pre>typedef struct
{
 char *<i>ptr</i>;
 int <i>length</i>;
 XmTextFormat <i>format</i>;
} XmTextBlockRec, *XmTextBlock;</pre>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><i>ptr</i></p>
<dd>Points to the text to be inserted.</p>
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
 XmTextBlockWcs <i>text</i>;
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
<dd>Points to the wide character text to be inserted.</p>
<dt><i>length</i></p>
<dd>Specifies the number of characters to be inserted.</dl>
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
<td>XmCR_LOSING_FOCUS</td>
<td> <i>reason, event, doit, currInsert, newInsert, startPos, endPos</i>
</td>
</tr>
<tr VALIGN=top>
<td>XmCR_MODIFYING_TEXT_VALUE</td>
<td> <i>reason, event, doit, currInsert, newInsert, startPos, endPos, text</i>
</td>
</tr>
<tr VALIGN=top>
<td>XmCR_MOVING_INSERT_CURSOR</td>
<td><i>reason, doit, currInsert, newInsert</i>
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
<dd>When the selection is <code>_MOTIF_DROP</code>, possible values are <code>XmMOVE</code>, <code>XmCOPY</code>, <code>XmLINK</code>, and <code>XmOTHER</code>. A value of <code>XmOTHER</code> means that the callback procedure must get further information from the <code>XmDropProcCallbackStruct</code> structure in the <i>destination_data</i> member.</dl>
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
<dd>Contains information about the destination. When the selection is <code>_MOTIF_DROP</code>, the callback procedures are called by the drop site&#8217;s <code>XmNdropProc</code>, and <i>destination_data</i> is a pointer to the <code>XmDropProcCallbackStruct</code> structure passed to the <code>XmNdropProc</code> procedure. When the selection is <code>SECONDARY</code>, <i>destination_data</i> is an Atom representing a target recommmended by the selection owner for use in converting the selection. Otherwise, <i>destination_data</i> is NULL.</p>
<dt><code>location_data</code></p>
<dd>Contains information about the location where data is to be transferred. The value is always NULL when the selection is <code>CLIPBOARD</code>. If the value is NULL, the data is to be inserted at the widget&#8217;s cursor position. Otherwise, the value is a pointer to an <code>XPoint</code> structure containing the x- and y- coordinates at the location where the data is to be transferred. Once <code>XmTransferDone</code> procedures start to be called, <code>location_data</code> will no longer be stable.</p>
<dt><i>time</i></p>
<dd>Indicates the time when the transfer operation began.</dl>
<h3>Translations</h3>
<p>The <code>XmText</code> translations are described in the following list. The actions represent the effective behavior of the associated events, and they may differ in a right-to-left language environment. </p>
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
<dt><code>:s c</code> <code>&lt;Key&gt;</code><code>&lt;osfBeginLine&gt;</code>:</p>
<dd>beginning-of-file(<code>extend</code>)</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfBeginLine&gt;</code>:</p>
<dd>beginning-of-file()</p>
<dt><code>:s</code> <code>&lt;Key&gt;</code><code>&lt;osfBeginLine&gt;</code>:</p>
<dd>beginning-of-line(<code>extend</code>)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfBeginLine&gt;</code>:</p>
<dd>beginning-of-line()</p>
<dt><code>:s c</code> <code>&lt;Key&gt;</code><code>&lt;osfEndLine&gt;</code>:</p>
<dd>end-of-file(<code>extend</code>)</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfEndLine&gt;</code>:</p>
<dd>end-of-file()</p>
<dt><code>:s</code> <code>&lt;Key&gt;</code><code>&lt;osfEndLine&gt;</code>:</p>
<dd>end-of-line(<code>extend</code>)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfEndLine&gt;</code>:</p>
<dd>end-of-line()</p>
<dt><code>:s</code> <code>&lt;Key&gt;</code><code>&lt;osfPageLeft&gt;</code>:</p>
<dd>page-left(<code>extend</code>) (ignored in vertical writing)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfPageLeft&gt;</code>:</p>
<dd>page-left() (next-page() in vertical writing)</p>
<dt><code>:s c</code> <code>&lt;Key&gt;</code><code>&lt;osfPageUp&gt;</code>:</p>
<dd>page-left(<code>extend</code>)</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfPageUp&gt;</code>:</p>
<dd>page-left()</p>
<dt><code>:s</code> <code>&lt;Key&gt;</code><code>&lt;osfPageUp&gt;</code>:</p>
<dd>previous-page(<code>extend</code>) (ignored in vertical writing)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfPageUp&gt;</code>:</p>
<dd>previous-page() (page-up() in vertical writing)</p>
<dt><code>:s</code> <code>&lt;Key&gt;</code><code>&lt;osfPageRight&gt;</code>:</p>
<dd>page-right(<code>extend</code>) (ignored in vertical writing)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfPageRight&gt;</code>:</p>
<dd>page-right() (previous-page() in vertical writing)</p>
<dt><code>s c</code> <code>&lt;Key&gt;</code><code>&lt;osfPageDown&gt;</code>:</p>
<dd>page-right(<code>extend</code>) (ignored in vertical writing)</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfPageDown&gt;</code>:</p>
<dd>page-right()</p>
<dt><code>:s</code> <code>&lt;Key&gt;</code><code>&lt;osfPageDown&gt;</code>:</p>
<dd>next-page(<code>extend</code>) (ignored in vertical writing)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfPageDown&gt;</code>:</p>
<dd>next-page() (page-down() in vertical writing)</p>
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
<dd>backward-word(<code>extend</code>) ( forward-paragraph(<code>extend</code>) in vertical writing)</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfLeft&gt;</code>:</p>
<dd>backward-word() (forward-paragraph() in vertical writing)</p>
<dt><code>:s</code> <code>&lt;Key&gt;</code><code>&lt;osfLeft&gt;</code>:</p>
<dd>key-select(<code>left</code>) (process-shift-left() in vertical writing)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfLeft&gt;</code>:</p>
<dd>backward-character() (process-left() in vertical writing)</p>
<dt><code>:s c</code> <code>&lt;Key&gt;</code><code>&lt;osfRight&gt;</code>:</p>
<dd>forward-word(<code>extend</code>) (backward-paragraph(<code>extend</code>) in vertical writing)</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfRight&gt;</code>:</p>
<dd>forward-word() (backward-paragraph() in vertical writing)</p>
<dt><code>:s</code> <code>&lt;Key&gt;</code><code>&lt;osfRight&gt;</code>:</p>
<dd>key-select(<code>right</code>) (process-shift-right in vertical writing)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfRight&gt;</code>:</p>
<dd>forward-character() (process-right() in vertical writing)</p>
<dt><code>:s c</code> <code>&lt;Key&gt;</code><code>&lt;osfUp&gt;</code>:</p>
<dd>backward-paragraph(<code>extend</code>) (backward-word(<code>extend</code>) in vertical writing)</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfUp&gt;</code>:</p>
<dd>backward-paragraph() (backward-word() in vertical writing)</p>
<dt><code>:s</code> <code>&lt;Key&gt;</code><code>&lt;osfUp&gt;</code>:</p>
<dd>process-shift-up() (key-select(<code>up</code>) in vertical writing)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfUp&gt;</code>:</p>
<dd>process-up() (backward-character() in vertical writing)</p>
<dt><code>:s c</code> <code>&lt;Key&gt;</code><code>&lt;osfDown&gt;</code>:</p>
<dd>forward-paragraph(<code>extend</code>) (forward-word(<code>extend</code>) in vertical writing)</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfDown&gt;</code>:</p>
<dd>forward-paragraph() (forward-word() in vertical writing)</p>
<dt><code>:s</code> <code>&lt;Key&gt;</code><code>&lt;osfDown&gt;</code>:</p>
<dd>process-shift-down() (key-select(<code>down</code>) in vertical writing)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfDown&gt;</code>:</p>
<dd>process-down() (forward-character() in vertical writing)</p>
<dt><code>c &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>slash</code>:</p>
<dd>select-all()</p>
<dt><code>c &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>backslash</code>:</p>
<dd>deselect-all()</p>
<dt><code>s c &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>Tab</code>:</p>
<dd>prev-tab-group()</p>
<dt><code>&asymp;s c &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>Tab</code>:</p>
<dd>next-tab-group()</p>
<dt><code>s &asymp;c &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>Tab</code>:</p>
<dd>process-tab(<code>Prev</code>)</p>
<dt><code>&asymp;s &asymp;c &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>Tab</code>:</p>
<dd>process-tab(<code>Next</code>)</p>
<dt><code>&asymp;s c &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>Return</code>:</p>
<dd>activate()</p>
<dt><code>&asymp;s &asymp;c &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>Return</code>:</p>
<dd>process-return()</p>
<dt><code>&asymp;s c &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>space</code>:</p>
<dd>set-anchor()</p>
<dt><code>s c &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>space</code>:</p>
<dd>key-select()</p>
<dt><code>s &asymp;c &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>space</code>:</p>
<dd>self-insert()</p>
<dt><code>&lt;Key&gt;</code>:</p>
<dd>self-insert()</dl>
<p> The Text button event translations are modified when Display&#8217;s <code>XmNenableBtn1Transfer</code> resource does not have a value of <code>XmOFF</code> (in other words, it is either <code>XmBUTTON2_TRANSFER</code> or <code>XmBUTTON2_ADJUST</code>). This option allows the actions for selection and transfer to be integrated on <code>&lt;Btn1&gt;</code>, and the actions for extending the selection can be bound to <code>&lt;Btn2&gt;</code>. The actions for <code>&lt;Btn1&gt;</code> that are defined above still apply when the <code>&lt;Btn1&gt;</code> event occurs over text that is not selected. The following actions apply when the <code>&lt;Btn1&gt;</code> event occurs over text that is selected:</p>
<dl COMPACT>
<dt><code>&lt;Btn1Down&gt;</code>:</p>
<dd>process-bdrag().</p>
<dt><code>&lt;Shift&gt;</code><code>&lt;Btn1Down&gt;</code>:</p>
<dd>process-bdrag().</p>
<dt><code>&lt;Ctrl&gt;</code><code>&lt;Btn1Down&gt;</code>:</p>
<dd>process-bdrag().</p>
<dt><code>&lt;Btn1Down&gt;</code><code>&lt;Shift&gt;</code><code>&lt;Btn1Up&gt;</code>:</p>
<dd>grab-focus(), <code>extend-end</code>.</p>
<dt><code>&lt;Shift&gt;</code><code>&lt;Btn1Down&gt;</code><code>&lt;Shift&gt;</code><code>&lt;Btn1Up&gt;</code>:</p>
<dd>extend-start(), extend-end().</p>
<dt><code>&lt;Ctrl&gt;</code><code>&lt;Btn1Down&gt;</code><code>&lt;Shift&gt;</code><code>&lt;Btn1Up&gt;</code>:</p>
<dd>move-destination().</dl>
<p> When Display&#8217;s <code>XmNenableBtn1Transfer</code> resource has a value of <code>XmBUTTON2_ADJUST</code>, the following actions apply:</p>
<dl COMPACT>
<dt><code>&lt;Btn2Down&gt;</code>:</p>
<dd>extend-start().</p>
<dt><code>&lt;Btn2Motion&gt;</code>:</p>
<dd>extend-adjust().</p>
<dt><code>&lt;Btn2Up&gt;</code>:</p>
<dd>extend-end().</dl>
<h3>Action Routines</h3>
<p>The <code>XmText</code> action routines are</p>
<dl COMPACT>
<dt>activate():</p>
<dd>Calls the callbacks for <code>XmNactivateCallback</code>. Passes the event to the parent.</p>
<dt>backward-character(<code>extend</code>):</p>
<dd>Moves the insertion cursor one character to the left. This action may have different behavior in a right-to-left language environment.</p>
<dd>If called with an argument of <i>extend</i>, moves the insertion cursor as in the case of no argument and extends the current selection.</p>
<dd>The backward-character() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>. If called with the <i>extend</i> argument, the backward-character() action may produce calls to the <code>XmNgainPrimaryCallback</code> procedures. See callback description for more information.</p>
<dd>In vertical writing, if <code>XmNeditMode</code> is <code>XmSINGLE_LINE_EDIT</code> and <code>XmNnavigationType</code> is <code>XmNONE</code>, traverses to the widget to the left in the tab group. If <code>XmNeditMode</code> is <code>XmMULTI_LINE_EDIT</code>, moves the insertion cursor to the next line in the same column.</p>
<dt>backward-paragraph(<code>extend</code>):</p>
<dd>If <code>XmNeditMode</code> is <code>XmMULTI_LINE_EDIT</code> and this action is called with no argument, moves the insertion cursor to the first non-whitespace character following the first previous blank line or beginning of the text. If the insertion cursor is already at the beginning of a paragraph, moves the insertion cursor to the beginning of the previous paragraph.</p>
<dd>If <code>XmNeditMode</code> is <code>XmMULTI_LINE_EDIT</code> and this action is called with an argument of <i>extend</i>, moves the insertion cursor as in the case of no argument and extends the current selection.</p>
<dd>The backward-paragraph() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>. If called with the <i>extend</i> argument, the backward-paragraph() action may produce calls to the <code>XmNgainPrimaryCallback</code> procedures. See callback description for more information.</p>
<dt>backward-word(<code>extend</code>):</p>
<dd>If this action is called with no argument, moves the insertion cursor to the first non-whitespace character after the first whitespace character to the left or after the beginning of the line. If the insertion cursor is already at the beginning of a word, moves the insertion cursor to the beginning of the previous word. This action may have different behavior in a locale other than the C locale.</p>
<dd>If called with an argument of <i>extend</i>, moves the insertion cursor as in the case of no argument and extends the current selection.</p>
<dd>The backward-word() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>. If called with the <i>extend</i> argument, the backward-word() action may produce calls to the <code>XmNgainPrimaryCallback</code> procedures. See callback description for more information.</p>
<dt>beep():</p>
<dd>Causes the terminal to beep. The beep() action produces no callbacks.</p>
<dt>beginning-of-file(<code>extend</code>):</p>
<dd>If this action is called with no argument, moves the insertion cursor to the beginning of the text.</p>
<dd>If called with an argument of <i>extend</i>, moves the insertion cursor as in the case of no argument and extends the current selection.</p>
<dd>The beginning-of-file() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>. If called with the <i>extend</i> argument, the beginning-of-file() action may produce calls to the <code>XmNgainPrimaryCallback</code> procedures. See callback description for more information.</p>
<dt>beginning-of-line(<code>extend</code>):</p>
<dd>If this action is called with no argument, moves the insertion cursor to the beginning of the line.</p>
<dd>If called with an argument of <i>extend</i>, moves the insertion cursor as in the case of no argument and extends the current selection.</p>
<dd>The beginning-of-line() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>. If called with the <i>extend</i> argument, the beginning-of-line() action may produce calls to the <code>XmNgainPrimaryCallback</code> procedures. See callback description for more information.</p>
<dt>clear-selection():</p>
<dd>Clears the current selection by replacing each character except <code>&lt;Return&gt;</code> with a <code>&lt;space&gt;</code> character.</p>
<dd>The clear-selection() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code> and the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>.</p>
<dt>copy-clipboard():</p>
<dd>If this widget owns the primary selection, this action copies the selection to the clipboard. This action calls the <code>XmNconvertCallback</code> procedures, possibly multiple times, for the <code>CLIPBOARD</code> selection.</p>
<dt>copy-primary():</p>
<dd>Copies the primary selection to just before the insertion cursor. This action calls the <code>XmNdestinationCallback</code> procedures for the <code>PRIMARY</code> selection and the <code>XmCOPY</code> operation. It calls the selection owner&#8217;s <code>XmNconvertCallback</code> procedures, possibly multiple times, for the <code>PRIMARY</code> selection.</p>
<dd>In addition, the copy-primary() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, to the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>, and to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>.</p>
<dt>copy-to():</p>
<dd>If a secondary selection exists, this action copies the secondary selection to the insertion position of the destination component. If the primary selection is in the destination widget, it will be deselected. Otherwise, there is no effect on the primary selection.</p>
<dd>This action calls the destination&#8217;s <code>XmNdestinationCallback</code> procedures for the <code>SECONDARY</code> selection and the <code>XmCOPY</code> operation. The destination&#8217;s <code>XmNdestinationCallback</code> procedures or the destination component itself invokes the selection owner&#8217;s <code>XmNconvertCallback</code> procedures, possibly multiple times, for the <code>SECONDARY</code> selection.</p>
<dd>If no secondary selection exists, this action copies the primary selection to the pointer position. This action calls the <code>XmNdestinationCallback</code> procedures for the <code>PRIMARY</code> selection and the <code>XmCOPY</code> operation. It calls the selection owner&#8217;s <code>XmNconvertCallback</code> procedures, possibly multiple times, for the <code>PRIMARY</code> selection.</p>
<dd>In addition, the copy-to() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, to the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>, and to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>. If there is no secondary selection, the copy-to() action may produce calls to the <code>XmNgainPrimaryCallback</code> procedures. See callback description for more information.</p>
<dt>cut-clipboard():</p>
<dd>If this widget owns the primary selection, this action cuts the selection to the clipboard. This action calls the <code>XmNconvertCallback</code> procedures, possibly multiple times, for the <code>CLIPBOARD</code> selection. If the transfer is successful, this action then calls the <code>XmNconvertCallback</code> procedures for the <code>CLIPBOARD</code> selection and the <code>DELETE</code> target.</p>
<dd>In addition, the cut-clipboard() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, and the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>.</p>
<dt>cut-primary():</p>
<dd>Cuts the primary selection and pastes it just before the insertion cursor. This action calls the <code>XmNdestinationCallback</code> procedures for the <code>PRIMARY</code> selection and the <code>XmMOVE</code> operation. It calls the selection owner&#8217;s <code>XmNconvertCallback</code> procedures, possibly multiple times, for the <code>PRIMARY</code> selection. If the transfer is successful, this action then calls the selection owner&#8217;s <code>XmNconvertCallback</code> procedures for the <code>PRIMARY</code> selection and the <code>DELETE</code> target. The cut-primary() action may produce calls to the <code>XmNgainPrimaryCallback</code> procedures. See callback description for more information.</p>
<dd>In addition, the cut-primary() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>, the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, and the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>.</p>
<dt>delete-next-character():</p>
<dd>In normal mode, if there is a nonnull selection, deletes the selection; otherwise, deletes the character following the insertion cursor. In add mode, if there is a nonnull selection, the cursor is not disjoint from the selection, and <code>XmNpendingDelete</code> is set to True, deletes the selection; otherwise, deletes the character following the insertion cursor. This may impact the selection.</p>
<dd>The delete-next-character() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, and the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>.</p>
<dt>delete-next-word():</p>
<dd>In normal mode, if there is a nonnull selection, deletes the selection; otherwise, deletes the characters following the insertion cursor to the next space, tab or end-of-line character. In add mode, if there is a nonnull selection, the cursor is not disjoint from the selection, and <code>XmNpendingDelete</code> is set to True, deletes the selection; otherwise, deletes the characters following the insertion cursor to the next space, tab or end-of-line character. This may impact the selection. This action may have different behavior in a locale other than the C locale.</p>
<dd>The delete-next-word() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, and the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>.</p>
<dt>delete-previous-character():</p>
<dd>In normal mode, if there is a nonnull selection, deletes the selection; otherwise, deletes the character of text immediately preceding the insertion cursor. In add mode, if there is a nonnull selection, the cursor is not disjoint from the selection, and <code>XmNpendingDelete</code> is set to True, deletes the selection; otherwise, deletes the character of text immediately preceding the insertion cursor. This may impact the selection.</p>
<dd>The delete-previous-character() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>, and the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>.</p>
<dt>delete-previous-word():</p>
<dd>In normal mode, if there is a nonnull selection, deletes the selection; otherwise, deletes the characters preceding the insertion cursor to the next space, tab or beginning-of-line character. In add mode, if there is a nonnull selection, the cursor is not disjoint from the selection, and <code>XmNpendingDelete</code> is set to True, deletes the selection; otherwise, deletes the characters preceding the insertion cursor to the next space, tab or beginning-of-line character. This may impact the selection. This action may have different behavior in a locale other than the C locale.</p>
<dd>The delete-previous-word() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>, and the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>.</p>
<dt>delete-selection():</p>
<dd>Deletes the current selection.</p>
<dd>The delete-selection() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>, and the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>.</p>
<dt>delete-to-end-of-line():</p>
<dd>In normal mode, if there is a nonnull selection, deletes the selection; otherwise, deletes the characters following the insertion cursor to the next end of line character. In add mode, if there is a nonnull selection, the cursor is not disjoint from the selection, and <code>XmNpendingDelete</code> is set to True, deletes the selection; otherwise, deletes the characters following the insertion cursor to the next end of line character. This may impact the selection.</p>
<dd>The <code>delete-to-end-of-line()</code> action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, and the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>.</p>
<dt>delete-to-start-of-line():</p>
<dd>In normal mode, if there is a nonnull selection, deletes the selection; otherwise, deletes the characters preceding the insertion cursor to the previous beginning-of-line character. In add mode, if there is a nonnull selection, the cursor is not disjoint from the selection, and <code>XmNpendingDelete</code> is set to True, deletes the selection; otherwise, deletes the characters preceding the insertion cursor to the previous beginning-of-line character. This may impact the selection.</p>
<dd>The delete-to-start-of-line() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>, and the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>.</p>
<dt>deselect-all():</p>
<dd>Deselects the current selection. The deselect-all() action produces no callbacks.</p>
<dt>end-of-file(<code>extend</code>):</p>
<dd>If this action is called with no argument, moves the insertion cursor to the end of the text.</p>
<dd>If called with an argument of <i>extend</i>, moves the insertion cursor as in the case of no argument and extends the current selection.</p>
<dd>The end-of-file() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>. If called with the <i>extend</i> argument, the end-of-file() action may produce calls to the <code>XmNgainPrimaryCallback</code> procedures. See callback description for more information.</p>
<dt>end-of-line(<code>extend</code>):</p>
<dd>If this action is called with no argument, moves the insertion cursor to the end of the line. If called with an argument of <i>extend</i>, moves the insertion cursor as in the case of no argument and extends the current selection.</p>
<dd>The end-of-line() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>. If called with the <i>extend</i> argument, the end-of-line() action may produce calls to the <code>XmNgainPrimaryCallback</code> procedures. See callback description for more information.</p>
<dt>extend-adjust():</p>
<dd>Selects text from the anchor to the pointer position and deselects text outside that range. Moving the pointer over several lines selects text from the anchor to the end of each line the pointer moves over and up to the pointer position on the current line.</p>
<dd>The extend-adjust() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>. The extend-adjust() action may produce calls to the <code>XmNgainPrimaryCallback</code> procedures. See callback description for more information.</p>
<dt>extend-end():</p>
<dd>Moves the insertion cursor to the position of the pointer. The extend-end() action is used to commit the selection. After this action has been done, process-cancel() will no longer cancel the selection.</p>
<dd>The extend-end() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>. The extend-end() action may produce calls to the <code>XmNgainPrimaryCallback</code> procedures. See callback description for more information.</p>
<dt>extend-start():</p>
<dd>Adjusts the anchor using the balance-beam method. Selects text from the anchor to the pointer position and deselects text outside that range. The extend-start() action may produce no callbacks, however, the extend-start() action may produce calls to the <code>XmNgainPrimaryCallback</code> procedures. See callback description for more information.</p>
<dt>forward-character(<code>extend</code>):</p>
<dd>Moves the insertion cursor one character to the right. This action may have different behavior in a right-to-left language environment.</p>
<dd>If called with an argument of <i>extend</i>, moves the insertion cursor as in the case of no argument and extends the current selection.</p>
<dd>The forward-character() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>. If called with the <i>extend</i> argument, the forward-character() action may produce calls to the <code>XmNgainPrimaryCallback</code> procedures. See callback description for more information.</p>
<dd>In vertical writing, if <code>XmNeditMode</code> is <code>XmSINGLE_LINE_EDIT</code> and <code>XmNnavigationType</code> is <code>XmNONE</code>, traverses to the widget to the right in the tab group. If <code>XmNeditMode</code> is <code>XmMULTI_LINE_EDIT</code>, moves the insertion cursor to the previous line in the same column.</p>
<dt>forward-paragraph(<code>extend</code>):</p>
<dd>If <code>XmNeditMode</code> is <code>XmMULTI_LINE_EDIT</code>, and this action is called with no argument, moves the insertion cursor to the first non-whitespace character following the next blank line. If the insertion cursor is already at the beginning of a paragraph, moves the insertion cursor to the beginning of the next paragraph.</p>
<dd>If <code>XmNeditMode</code> is <code>XmMULTI_LINE_EDIT</code> and this action is called with an argument of <i>extend</i>, moves the insertion cursor as in the case of no argument and extends the current selection.</p>
<dd>The forward-paragraph() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>. If called with the <i>extend</i> argument, the forward-paragraph() action may produce calls to the <code>XmNgainPrimaryCallback</code> procedures. See callback description for more information.</p>
<dt>forward-word(<code>extend</code>):</p>
<dd>If this action is called with no argument, moves the insertion cursor to the first whitespace character or end-of-line following the next non-whitespace character. If the insertion cursor is already at the end of a word, moves the insertion cursor to the end of the next word. This action may have different behavior in a locale other than the C locale.</p>
<dd>If called with an argument of <i>extend</i>, moves the insertion cursor as in the case of no argument and extends the current selection.</p>
<dd>The forward-word() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>. If called with the <i>extend</i> argument, the forward-word() action may produce calls to the <code>XmNgainPrimaryCallback</code> procedures. See callback description for more information.</p>
<dt>grab-focus():</p>
<dd>This key binding performs the action defined in the <code>XmNselectionArray</code>, depending on the number of multiple mouse clicks. The default selection array ordering is one click to move the insertion cursor to the pointer position, two clicks to select a word, three clicks to select a line of text, and four clicks to select all text. A single click also deselects any selected text and sets the anchor at the pointer position. This action may have different behavior in a locale other than the C locale.</p>
<dd>The grab-focus() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>.</p>
<dt>Help():</p>
<dd>Calls the callbacks for <code>XmNhelpCallback</code> if any exist. If there are no help callbacks for this widget, this action calls the help callbacks for the nearest ancestor that has them.</p>
<dt>insert-string(<i>string</i><code>)</code>:</p>
<dd>If <code>XmNpendingDelete</code> is True and the cursor is not disjoint from the current selection, deletes the entire selection. Inserts <i>string</i> before the insertion cursor.</p>
<dd>The insert-string() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>, and the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>. Note that, in the case of an empty string, no callbacks will be called, since no modification will have been done. However, if the insertion position is inside the current selection, <code>insert-string</code> with an empty string will cause the selection to be deselected, and the <code>XmNmotionVerifyCallback</code> procedures to be called with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>, <code>XmCR_MODIFYING_TEXT_VALUE</code>, and <code>XmCR_VALUE_CHANGED</code>.</p>
<dt>key-select(<code>right|left</code>):</p>
<dd>If called with an argument of <i>right</i>, moves the insertion cursor one character to the right and extends the current selection. If called with an argument of <i>left</i>, moves the insertion cursor one character to the left and extends the current selection. If called with no argument, extends the current selection.</p>
<dd>Note that after a <code>key-select</code> action, the selection will still begin at the original anchor, and will extend to the position indicated in the action call. If this new position is on the opposite side of the selection anchor from the previous selection boundary, the original selection will be deselected.</p>
<dd>The key-select() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>. The key-select() action may produce calls to the <code>XmNgainPrimaryCallback</code> procedures. See callback description for more information.</p>
<dd>In vertical writing, if called with the argument <code>left</code>, and if <code>XmNeditMode</code> is <code>XmMULTI_LINE_EDIT</code>, moves the insertion cursor to the next line in the same column. In vertical writing, if called with the argument <code>right</code>, and if <code>XmNeditMode</code> is <code>XmMULTI_LINE_EDIT</code>, moves the insertion cursor to the previous line in the same column.)</p>
<dt>kill-next-character():</p>
<dd>In normal mode, if there is a nonnull selection, kills the selection; otherwise, kills the character following the insertion cursor and stores the character in the cut buffer. In add mode, if there is a nonnull selection, the cursor is not disjoint from the selection, and <code>XmNpendingDelete</code> is set to True, deletes the selection; otherwise, kills the character following the insertion cursor and stores the character in the cut buffer. This may impact the selection.</p>
<dd>The killed text is stored in <code>CUT_BUFFER0</code>.</p>
<dd>The kill-next-character() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>, and the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>.</p>
<dt>kill-next-word():</p>
<dd>In normal mode, if there is a nonnull selection, deletes the selection; otherwise, kills the characters following the insertion cursor to the next space, tab or end-of-line character, and stores the characters in the cut buffer. In add mode, if there is a nonnull selection, the cursor is not disjoint from the selection, and <code>XmNpendingDelete</code> is set to True, deletes the selection; otherwise, kills the characters following the insertion cursor to the next space, tab or end-of-line character, and stores the characters in the cut buffer. This may impact the selection. This action may have different behavior in a locale other than the C locale.</p>
<dd>The killed text is stored in <code>CUT_BUFFER0</code>.</p>
<dd>The kill-next-word() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>, and the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>.</p>
<dt>kill-previous-character():</p>
<dd>In normal mode, if there is a nonnull selection, deletes the selection; otherwise, kills the character immediately preceding the insertion cursor and stores the character in the cut buffer. In add mode, if there is a nonnull selection, the cursor is not disjoint from the selection, and <code>XmNpendingDelete</code> is set to True, deletes the selection; otherwise, kills the character immediately preceding the insertion cursor and stores the character in the cut buffer. This may impact the selection.</p>
<dd>The killed text is stored in <code>CUT_BUFFER0</code>.</p>
<dd>The kill-previous-character() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>, and the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>.</p>
<dt>kill-previous-word():</p>
<dd>In normal mode, if there is a nonnull selection, deletes the selection; otherwise, kills the characters preceding the insertion cursor up to the next space, tab or beginning-of-line character, and stores the characters in the cut buffer. In add mode, if there is a nonnull selection, the cursor is not disjoint from the selection, and <code>XmNpendingDelete</code> is set to True, deletes the selection; otherwise, kills the characters preceding the insertion cursor up to the next space, tab or beginning-of-line character, and stores the characters in the cut buffer. This may impact the selection. This action may have different behavior in a locale other than the C locale.</p>
<dd>The killed text is stored in <code>CUT_BUFFER0</code>.</p>
<dd>The kill-previous-word() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>, and the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>.</p>
<dt>kill-selection():</p>
<dd>Kills the currently selected text and stores the text in the cut buffer.</p>
<dd>The killed text is stored in <code>CUT_BUFFER0</code>.</p>
<dd>The kill-selection() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>, and the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>.</p>
<dt>kill-to-end-of-line():</p>
<dd>In normal mode, if there is a nonnull selection, deletes the selection; otherwise, kills the characters following the insertion cursor to the next end-of-line character and stores the characters in the cut buffer. In add mode, if there is a nonnull selection, the cursor is not disjoint from the selection, and <code>XmNpendingDelete</code> is set to True, deletes the selection; otherwise, kills the characters following the insertion cursor to the next end of line character and stores the characters in the cut buffer. This may impact the selection.</p>
<dd>The killed text is stored in <code>CUT_BUFFER0</code>.</p>
<dd>The kill-to-end-of-line() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, and the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>. In the case where there is a non-null selection to be deleted, this action may also produce calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>.</p>
<dt>kill-to-start-of-line():</p>
<dd>In normal mode, if there is a nonnull selection, deletes the selection; otherwise, kills the characters preceding the insertion cursor to the next beginning-of-line character and stores the characters in the cut buffer. In add mode, if there is a nonnull selection, the cursor is not disjoint from the selection, and <code>XmNpendingDelete</code> is set to True, deletes the selection; otherwise, kills the characters preceding the insertion cursor to the next beginning-of-line character and stores the characters in the cut buffer. This may impact the selection.</p>
<dd>The killed text is stored in <code>CUT_BUFFER0</code>.</p>
<dd>The kill-to-start-of-line() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>, and the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>.</p>
<dt>link-primary():</p>
<dd>Places a link to the primary selection just before the insertion cursor. This action calls the <code>XmNdestinationCallback</code> procedures for the <code>PRIMARY</code> selection and the <code>XmLINK</code> operation. The Text widget itself performs no transfers; the <code>XmNdestinationCallback</code> procedures are responsible for inserting the link to the primary selection and for taking any related actions.</p>
<dt>link-to():</p>
<dd>If a secondary selection exists, this action places a link to the secondary selection at the insertion position of the destination component. This action calls the destination&#8217;s <code>XmNdestinationCallback</code> procedures for the <code>SECONDARY</code> selection and the <code>XmLINK</code> operation.</p>
<dd>If no secondary selection exists, this action places a link to the primary selection at the pointer position. This action calls the <code>XmNdestinationCallback</code> procedures for the <code>PRIMARY</code> selection and the <code>XmLINK</code> operation.</p>
<dd>The Text widget itself performs no transfers; the <code>XmNdestinationCallback</code> procedures are responsible for inserting the link to the primary or secondary selection and for taking any related actions.</p>
<dt>move-destination():</p>
<dd>Moves the insertion cursor to the pointer position without changing any existing current selection. If there is a current selection, sets the widget as the destination widget. This also moves the widget focus to match the insertion cursor.</p>
<dd>The move-destination() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>.</p>
<dt>move-to():</p>
<dd>If a secondary selection exists, this action moves the secondary selection to the insertion position of the destination component. If the secondary selection is in the destination widget, and the secondary selection and the primary selection overlap, the result is undefined. This action calls the destination&#8217;s <code>XmNdestinationCallback</code> procedures for the <code>SECONDARY</code> selection and the <code>XmMOVE</code> operation. The destination&#8217;s <code>XmNdestinationCallback</code> procedures or the destination component itself invokes the selection owner&#8217;s <code>XmNconvertCallback</code> procedures, possibly multiple times, for the <code>SECONDARY</code> selection. If the transfer is successful, this action then calls the selection owner&#8217;s <code>XmNconvertCallback</code> procedures for the <code>SECONDARY</code> selection and the <code>DELETE</code> target.</p>
<dd>If no secondary selection exists, this action moves the primary selection to the pointer position. This action calls the <code>XmNdestinationCallback</code> procedures for the <code>PRIMARY</code> selection and the <code>XmMOVE</code> operation. It calls the selection owner&#8217;s <code>XmNconvertCallback</code> procedures, possibly multiple times, for the <code>PRIMARY</code> selection. If the transfer is successful, this action then calls the selection owner&#8217;s <code>XmNconvertCallback</code> procedures for the <code>PRIMARY</code> selection and the <code>DELETE</code> target.</p>
<dd>The move-to() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>, and the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>. If there is no secondary selection, the move-to() action may produce calls to the <code>XmNgainPrimaryCallback</code> procedures. See callback description for more information.</p>
<dt>newline():</p>
<dd>If <code>XmNpendingDelete</code> is True and the cursor is not disjoint from the current selection, deletes the entire selection. Inserts a newline before the insertion cursor.</p>
<dd>The newline() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>, and the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>.</p>
<dt>newline-and-backup():</p>
<dd>If <code>XmNpendingDelete</code> is True and the cursor is not disjoint from the current selection, deletes the entire selection. Inserts a newline just before the insertion cursor and repositions the insertion cursor to the end of the line before the newline.</p>
<dd>The newline-and-backup() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, and the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>.</p>
<dt>newline-and-indent():</p>
<dd>If <code>XmNpendingDelete</code> is True and the cursor is not disjoint from the current selection, deletes the entire selection. Inserts a newline and then the same number of whitespace characters as at the beginning of the previous line.</p>
<dd>The newline-and-indent() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>, and the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>.</p>
<dt>next-line():</p>
<dd>Moves the insertion cursor to the next line.</p>
<dd>The next-line() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>.</p>
<dt>next-page(<code>extend</code>):</p>
<dd>If <code>XmNeditMode</code> is <code>XmMULTI_LINE_EDIT</code> and this action is called with no argument, moves the insertion cursor forward one page.</p>
<dd>If <code>XmNeditMode</code> is <code>XmMULTI_LINE_EDIT</code> and this action is called with an argument of <i>extend</i>, it moves the insertion cursor as in the case of no argument and extends the current selection.</p>
<dd>The next-page() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>. If called with the <i>extend</i> argument, the next-page() action may produce calls to the <code>XmNgainPrimaryCallback</code> procedures. See callback description for more information.</p>
<dd>In vertical writing, scrolls the viewing window down one page of text.</p>
<dt>next-tab-group():</p>
<dd>Traverses to the next tab group.</p>
<dd>The next-tab-group() action produces no callbacks, unless it results in the widget losing focus, in which case, the <code>XmNlosingFocusCallback</code> procedures are called with reason value <code>XmCR_LOSING_FOCUS</code>.</p>
<dt>page-left(<code>extend</code>):</p>
<dd>If <code>XmNeditMode</code> is <code>XmMULTI_LINE_EDIT</code> and this action is called with no argument, moves the insertion cursor back one page.</p>
<dd>If <code>XmNeditMode</code> is <code>XmMULTI_LINE_EDIT</code> and this action is called with an argument of <i>extend</i>, it moves the insertion cursor as in the case of no argument and extends the current selection.</p>
<dd>The page-left() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>. If called with the <i>extend</i> argument, the page-left() action may produce calls to the <code>XmNgainPrimaryCallback</code> procedures. See callback description for more information.</p>
<dt>page-right(<code>extend</code>):</p>
<dd>If <code>XmNeditMode</code> is <code>XmMULTI_LINE_EDIT</code> and this action is called with no argument, moves the insertion cursor forward one page.</p>
<dd>If <code>XmNeditMode</code> is <code>XmMULTI_LINE_EDIT</code> and this action is called with an argument of <i>extend</i>, it moves the insertion cursor as in the case of no argument and extends the current selection.</p>
<dd>The page-right() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>. If called with the <i>extend</i> argument, the page-right() action may produce calls to the <code>XmNgainPrimaryCallback</code> procedures. See callback description for more information.</p>
<dt>paste-clipboard():</p>
<dd>Pastes the contents of the clipboard before the insertion cursor. This action calls the <code>XmNdestinationCallback</code> procedures for the <code>CLIPBOARD</code> selection and the <code>XmCOPY</code> operation.</p>
<dd>The paste-clipboard() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>, and the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>.</p>
<dt>prev-tab-group():</p>
<dd>Traverses to the previous tab group.</p>
<dd>The prev-tab-group() action produces no callbacks, unless it results in the widget losing focus, in which case, the <code>XmNlosingFocusCallback</code> procedures are called with reason value <code>XmCR_LOSING_FOCUS</code>.</p>
<dt>previous-line():</p>
<dd>Moves the insertion cursor to the previous line.</p>
<dd>The previous-line() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>.</p>
<dt>previous-page(<code>extend</code>):</p>
<dd>If <code>XmNeditMode</code> is <code>XmMULTI_LINE_EDIT</code> and this action is called with no argument, moves the insertion cursor back one page.</p>
<dd>If <code>XmNeditMode</code> is <code>XmMULTI_LINE_EDIT</code> and this action is called with an argument of <i>extend</i>, it moves the insertion cursor as in the case of no argument and extends the current selection.</p>
<dd>The previous-page() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>. If called with the <i>extend</i> argument, the previous-page() action may produce calls to the <code>XmNgainPrimaryCallback</code> procedures. See callback description for more information.</p>
<dd>In vertical writing, if called without an argument, scrolls the viewing window up one page of text.</p>
<dt>process-bdrag()</p>
<dd>If the pointer is within the selection, this action starts a drag operation for the selection. This action sets the <code>XmNconvertProc</code> of the DragContext to a function that calls the <code>XmNconvertCallback</code> procedures, possibly multiple times, for the <code>_MOTIF_DROP</code> selection.</p>
<dd>If no selection exists or the pointer is outside the selection, this action prepares to start a secondary selection at the pointer position.</dl>
<dl COMPACT>
<dd><code>Note:</p>
<dl COMPACT>
<dd>Note that when dragging a secondary selection to a different widget, focus will shift momentarily to the second widget, and then back to the original widget. This will generate callbacks to the XmNlosingFocusCallback</code> procedures as focus is lost (by each widget) as well as callbacks to the <code>XmNfocusCallback</code> procedures as focus is regained.</dl>
</dl>
<dl COMPACT>
<dt>process-cancel():</p>
<dd>Cancels the current extend-adjust(), secondary-adjust() or process-bdrag() operation and leaves the selection state as it was before the operation; otherwise, and if the parent is a manager, passes the event to the parent.</p>
<dt>process-down(<code>extend</code>):</p>
<dd>If <code>XmNeditMode</code> is <code>XmSINGLE_LINE_EDIT</code>, and <code>XmNnavigationType</code> is <code>XmNONE</code>, traverses to the widget below the current one in the tab group.</p>
<dd>If <code>XmNeditMode</code> is <code>XmMULTI_LINE_EDIT</code> and this action is called with an argument of <i>extend</i>, moves the insertion cursor as in the case of no argument and extends the current selection.</p>
<dd>In this case, the action will produce the <code>XmNlosingFocusCallback</code> callbacks with reason value <code>XmCR_LOSING_FOCUS</code>.</p>
<dd>If <code>XmNeditMode</code> is <code>XmMULTI_LINE_EDIT</code>, moves the insertion cursor down one line.</p>
<dd>The process-down() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>.</p>
<dd>In vertical writing, moves the insertion cursor one character down.</p>
<dt>process-home():</p>
<dd>Moves the insertion cursor to the beginning of the line.</p>
<dd>The process-home() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>.</p>
<dt>process-return():</p>
<dd>If <code>XmNeditMode</code> is <code>XmSINGLE_LINE_EDIT</code>, calls the callbacks for <code>XmNactivateCallback</code>, and if the parent is a manager, passes the event to the parent. If <code>XmNeditMode</code> is <code>XmMULTI_LINE_EDIT</code>, inserts a newline.</p>
<dd>The process-return() action during single-line edit produces calls to the <code>XmNactivateCallback</code> procedures with reason value <code>XmCR_ACTIVATE</code>. During multi-line editing, the process-return() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>, and the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>.</p>
<dt>process-shift-down():</p>
<dd>If <code>XmNeditMode</code> is <code>XmMULTI_LINE_EDIT</code>, moves the insertion cursor down one line and selects. If <code>XmNeditMode</code> is <code>XmSINGLE_LINE_EDIT</code>, this action behaves like process-up() in <code>XmSINGLE_LINE_EDIT</code>. Refer to the process-up() action.</p>
<dd>The process-shift-down() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>.</p>
<dd>In vertical writing, if called with the argument <code>up</code>, moves the insertion cursor one character up and extends the current selection. If called with the argument <code>down</code>, moves the insertion cursor one character down and extends the current selection.</p>
<dt>process-shift-up():</p>
<dd>If <code>XmNeditMode</code> is <code>XmMULTI_LINE_EDIT</code>, moves the insertion cursor up one line and selects. If <code>XmNeditMode</code> is <code>XmSINGLE_LINE_EDIT</code>, this action behaves like process-up() in <code>XmSINGLE_LINE_EDIT</code>. Refer to the process-up() action.</p>
<dd>The process-shift-up() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>.</p>
<dd>In vertical writing, if called with the argument <code>up</code>, moves the insertion cursor one character up and extends the current selection. If called with the argument <code>down</code>, moves the insertion cursor one character down and extends the current selection.</p>
<dt>process-tab(<code>Prev|Next</code>):</p>
<dd>If <code>XmNeditMode</code> is <code>XmSINGLE_LINE_EDIT</code>, traverses to the next tab group if the direction argument is <code>Next</code>, or to the previous tab group if the direction is <code>Prev</code>. If <code>XmNeditMode</code> is <code>XmMULTI_LINE_EDIT</code>, and the direction is <code>Next</code>, the action inserts a tab. The <code>Prev</code> direction has no effect with <code>XmMULTI_LINE_EDIT</code>. In the Text widget, there is a preset tab stop at every eighth columns.</p>
<dd>The process-tab() action under multi-line editing produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>. Under single-line editing, the action produces no callbacks, unless it results in the widget losing focus, in which case, the <code>XmNlosingFocusCallback</code> procedures are called with reason value <code>XmCR_LOSING_FOCUS</code>.</p>
<dt>process-up(<code>extend</code>):</p>
<dd>If <code>XmNeditMode</code> is <code>XmSINGLE_LINE_EDIT</code> and <code>XmNnavigationType</code> is <code>XmNONE</code>, traverses to the widget above the current one in the tab group.</p>
<dd>If <code>XmNeditMode</code> is <code>XmMULTI_LINE_EDIT</code>, moves the insertion cursor up one line.</p>
<dd>If <code>XmNeditMode</code> is <code>XmMULTI_LINE_EDIT</code> and this action is called with an argument of <i>extend</i>, moves the insertion cursor as in the case of no argument and extends the current selection.</p>
<dd>The process-up() action under multi-line editing produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>. Under single-line editing, the action produces no callbacks unless it results in the widget losing focus, in which case, the <code>XmNlosingFocusCallback</code> procedures are called with reason value <code>XmCR_LOSING_FOCUS</code>.</p>
<dd>In vertical writing, moves the insertion cursor one character up.</p>
<dt>redraw-display():</p>
<dd>Redraws the contents of the text window.</p>
<dd>The redraw-display() action produces no callbacks.</p>
<dt>scroll-cursor-vertically(<i>percentage</i><code>)</code>:</p>
<dd>Scrolls the line containing the insertion cursor vertically to an intermediate position in the visible window based on an input percentage. A value of 0 indicates the top of the window; a value of 100, the bottom of the window. If this action is called with no argument, the line containing the insertion cursor is scrolled vertically to a new position designated by the <i>y</i> position of the event passed to the routine.</p>
<dd>The <code>scroll-cursor-vertically</code> action produces no callbacks.</p>
<dt>scroll-one-line-down():</p>
<dd>Scrolls the text area down one line.</p>
<dd>The scroll-one-line-down() action produces no callbacks.</p>
<dt>scroll-one-line-up():</p>
<dd>Scrolls the text area up one line.</p>
<dd>The scroll-one-line-up() action produces no callbacks.</p>
<dt>secondary-adjust():</p>
<dd>Extends the secondary selection to the pointer position.</p>
<dd>The secondary-adjust() action produces no callbacks.</p>
<dt>secondary-notify():</p>
<dd>Copies the secondary selection to the insertion cursor of the destination widget.</p>
<dd>The secondary-notify() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, and the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>.</p>
<dt>secondary-start():</p>
<dd>Marks the beginning of a secondary selection.</p>
<dd>The secondary-start() action produces no callbacks.</p>
<dt>select-adjust():</p>
<dd>Moves the current selection. The amount of text selected depends on the number of mouse clicks, as specified by the <code>XmNselectionArray</code> resource.</p>
<dd>The select-adjust() action may produce no callbacks, however, it may produce calls to the <code>XmNgainPrimaryCallback</code> procedures. See callback description for more information.</p>
<dt>select-all():</p>
<dd>Selects all text.</p>
<dd>The select-all() action may produce calls to the <code>XmNgainPrimaryCallback</code> procedures.</p>
<dt>select-end():</p>
<dd>Moves the current selection. The amount of text selected depends on the number of mouse clicks, as specified by the <code>XmNselectionArray</code> resource.</p>
<dd>The select-end() action produces no callbacks.</p>
<dt>select-start():</p>
<dd>Marks the beginning of a new selection region.</p>
<dd>The select-start() action may produce calls to the <code>XmNgainPrimaryCallback</code> procedures.</p>
<dt>self-insert():</p>
<dd>If <code>XmNpendingDelete</code> is True and the cursor is not disjoint from the current selection, deletes the entire selection. Inserts the character associated with the key pressed at the insertion cursor.</p>
<dd>The self-insert() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>, and the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>.</p>
<dt>set-anchor():</p>
<dd>Resets the anchor point for extended selections. Resets the destination of secondary selection actions.</p>
<dd>The set-anchor() action produces no callbacks.</p>
<dt>set-insertion-point():</p>
<dd>Sets the insertion position to the position of the mouse pointer.</p>
<dd>The set-insertion-point() action produces calls to the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>. Note that if the mouse pointer is already over the position of the insertion cursor, the cursor will not be moved, and no callbacks will be produced.</p>
<dt>set-selection-hint():</p>
<dd>Sets the text source and location of the current selection.</p>
<dd>The set-selection-hint() action produces no callbacks.</p>
<dt>toggle-add-mode():</p>
<dd>Toggles the state of Add Mode.</p>
<dd>The toggle-add-mode() action produces no callbacks.</p>
<dt>toggle-overstrike():</p>
<dd>Toggles the state of the text insertion mode. By default, characters typed into the Text widget are inserted at the position of the insertion cursor. In overstrike mode, characters entered into the Text widget replace the characters that directly follow the insertion cursor. In overstrike mode, when the end of a line is reached, characters are appended to the end of the line.</p>
<dd>The following traversal actions generate no callbacks unless they result in the loss of focus by the widget in question, as when <code>XmNnavigationType</code> is <code>XmNONE</code>. In this case, they produce calls to the <code>XmNlosingFocusCallback</code> procedures, with reason value <code>XmCR_FOCUS_MOVED</code>.</p>
<dt>traverse-home():</p>
<dd>Traverses to the first widget in the tab group.</p>
<dt>traverse-next():</p>
<dd>Traverses to the next widget in the tab group.</p>
<dt>traverse-prev():</p>
<dd>Traverses to the previous widget in the tab group.</p>
<dt>unkill():</p>
<dd>Restores last killed text to the position of the insertion cursor (or whatever is currently in the <code>CUT_BUFFER0</code>). The inserted text appears before the insertion cursor.</p>
<dd>The unkill() action produces calls to the <code>XmNmodifyVerifyCallback</code> procedures with reason value <code>XmCR_MODIFYING_TEXT_VALUE</code>, the <code>XmNvalueChangedCallback</code> procedures with reason value <code>XmCR_VALUE_CHANGED</code>, and the <code>XmNmotionVerifyCallback</code> procedures with reason value <code>XmCR_MOVING_INSERT_CURSOR</code>.</dl>
<h3>Additional Behavior</h3>
<p>This widget has the following additional behavior:</p>
<dl COMPACT>
<dt><code>&lt;FocusIn&gt;</code>:</p>
<dd>Draws the insertion cursor as solid and starts blinking the cursor.</p>
<dt><code>&lt;FocusOut&gt;</code>:</p>
<dd>Displays the insertion cursor as a stippled I-beam unless it is the destination widget and stops the cursor from blinking.</dl>
<h3>Virtual Bindings</h3>
<p>The bindings for virtual keys are vendor specific. For information about bindings for virtual buttons and keys, see <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-core/">Core</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatescrolledtext/">XmCreateScrolledText</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatetext/">XmCreateText</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlist/">XmFontList</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistappendentry/">XmFontListAppendEntry</a></code>(3), <code><a href="/docs/linux/man/3-xmprimitive/">XmPrimitive</a></code>(3), <code><a href="/docs/linux/man/3-xmtextclearselection/">XmTextClearSelection</a></code>(3), <code><a href="/docs/linux/man/3-xmtextcopy/">XmTextCopy</a></code>(3), <code><a href="/docs/linux/man/3-xmtextcopylink/">XmTextCopyLink</a></code>(3), <code><a href="/docs/linux/man/3-xmtextcut/">XmTextCut</a></code>(3), <code><a href="/docs/linux/man/3-xmtextenableredisplay/">XmTextEnableRedisplay</a></code>(3), <code><a href="/docs/linux/man/3-xmtextdisableredisplay/">XmTextDisableRedisplay</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfindstring/">XmTextFindString</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfindstringwcs/">XmTextFindStringWcs</a></code>(3), <code><a href="/docs/linux/man/3-xmtextgetbaseline/">XmTextGetBaseline</a></code>(3), <code><a href="/docs/linux/man/3-xmtextgeteditable/">XmTextGetEditable</a></code>(3), <code><a href="/docs/linux/man/3-xmtextgetinsertionposition/">XmTextGetInsertionPosition</a></code>(3), <code><a href="/docs/linux/man/3-xmtextgetlastposition/">XmTextGetLastPosition</a></code>(3), <code><a href="/docs/linux/man/3-xmtextgetmaxlength/">XmTextGetMaxLength</a></code>(3), <code><a href="/docs/linux/man/3-xmtextgetselection/">XmTextGetSelection</a></code>(3), <code><a href="/docs/linux/man/3-xmtextgetselectionwcs/">XmTextGetSelectionWcs</a></code>(3), <code><a href="/docs/linux/man/3-xmtextgetselectionposition/">XmTextGetSelectionPosition</a></code>(3), <code><a href="/docs/linux/man/3-xmtextgetsource/">XmTextGetSource</a></code>(3), <code><a href="/docs/linux/man/3-xmtextgetstring/">XmTextGetString</a></code>(3), <code><a href="/docs/linux/man/3-xmtextgetstringwcs/">XmTextGetStringWcs</a></code>(3), <code><a href="/docs/linux/man/3-xmtextgetsubstring/">XmTextGetSubstring</a></code>(3), <code><a href="/docs/linux/man/3-xmtextgetsubstringwcs/">XmTextGetSubstringWcs</a></code>(3), <code><a href="/docs/linux/man/3-xmtextgettopcharacter/">XmTextGetTopCharacter</a></code>(3), <code><a href="/docs/linux/man/3-xmtextinsert/">XmTextInsert</a></code>(3), <code><a href="/docs/linux/man/3-xmtextinsertwcs/">XmTextInsertWcs</a></code>(3), <code><a href="/docs/linux/man/3-xmtextpaste/">XmTextPaste</a></code>(3), <code><a href="/docs/linux/man/3-xmtextpastelink/">XmTextPasteLink</a></code>(3), <code><a href="/docs/linux/man/3-xmtextpostoxy/">XmTextPosToXY</a></code>(3), <code><a href="/docs/linux/man/3-xmtextposition/">XmTextPosition</a></code>(3), <code><a href="/docs/linux/man/3-xmtextremove/">XmTextRemove</a></code>(3), <code><a href="/docs/linux/man/3-xmtextreplace/">XmTextReplace</a></code>(3), <code><a href="/docs/linux/man/3-xmtextreplacewcs/">XmTextReplaceWcs</a></code>(3), <code><a href="/docs/linux/man/3-xmtextscroll/">XmTextScroll</a></code>(3), <code><a href="/docs/linux/man/3-xmtextsetaddmode/">XmTextSetAddMode</a></code>(3), <code><a href="/docs/linux/man/3-xmtextseteditable/">XmTextSetEditable</a></code>(3), <code><a href="/docs/linux/man/3-xmtextsethighlight/">XmTextSetHighlight</a></code>(3), <code><a href="/docs/linux/man/3-xmtextsetinsertionposition/">XmTextSetInsertionPosition</a></code>(3), <code><a href="/docs/linux/man/3-xmtextsetmaxlength/">XmTextSetMaxLength</a></code>(3), <code><a href="/docs/linux/man/3-xmtextsetselection/">XmTextSetSelection</a></code>(3), <code><a href="/docs/linux/man/3-xmtextsetsource/">XmTextSetSource</a></code>(3), <code><a href="/docs/linux/man/3-xmtextsetstring/">XmTextSetString</a></code>(3), <code><a href="/docs/linux/man/3-xmtextsetstringwcs/">XmTextSetStringWcs</a></code>(3), <code><a href="/docs/linux/man/3-xmtextsettopcharacter/">XmTextSetTopCharacter</a></code>(3), <code><a href="/docs/linux/man/3-xmtextshowposition/">XmTextShowPosition</a></code>(3), <code><a href="/docs/linux/man/3-xmtextxytopos/">XmTextXYToPos</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatetext/">XmVaCreateText</a></code>(3), and <code><a href="/docs/linux/man/3-xmvacreatemanagedtext/">XmVaCreateManagedText</a></code>(3).</p>
