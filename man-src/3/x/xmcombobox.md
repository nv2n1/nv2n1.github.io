---
title: "xmcombobox(3)"
name: "xmcombobox"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcombobox/"
description: "XmComboBox — The ComboBox widget class"
---

<p><code>XmComboBox</code> &#8212; The ComboBox widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/ComboBox.h&gt;</pre>
<h2>Description</h2>
<p><code>XmComboBox</code> combines the capabilities of a single-line TextField widget and a List widget. It allows users to perform opoerations like typing and pasting information, and it also provides a list of possible choices that the user can select from to complete the TextField entry field. The list can either be displayed at all times or can be dropped down by the user. When the list portion of the ComboBox is hidden, users are given a visual cue (a downward-pointing arrow) next to the TextField field. The position of the arrow relative to the TextField field depends on the <code>XmNlayoutDirection</code> resource of the widget. This version of the ComboBox is called the &quot;drop-down&quot; ComboBox. Drop-down ComboBoxes are useful when screen space is limited, or when users will complete the text entry field more often by typing text than by selecting the entry field text from the list. The user can access the drop-down ComboBox in either one of two ways:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd>By clicking and releasing <code>&lt;Btn1&gt;</code> on the downward-pointing arrow, which pops the list up, and the list stays up. A later selection of an item in the list will cause the item to appear in the text entry field, and the list will unpost itself.</p>
<dt> &bull;</p>
<dd>By pressing <code>&lt;Btn1&gt;</code> on the downward-pointing arrow, dragging it to a list item, and then releasing it there, which selects that item. The list disappears, and the selected item appears in the text entry field.</dl>
<p> The application provides an array of strings that fill the list. At creation time, string items can be passed to the ComboBox via an arglist. Each string becomes an item in the list, with the first string becoming the item in position 1, the second string becoming the item in position 2, and so on. The size of the list is set by specifying the number of items that are visible in the list (<code>XmNvisibleItemCount</code>). If the number of items in the list exceeds the number of items that are visible, a vertical scroll bar will automatically appear that allows the user to scroll through a large number of items. </p>
<p> ComboBox creates two child widgets: a TextField widget for entering text and a ScrolledWindow containing a List for the list of items. The name of the items list itself is <code>List</code>, and the name of the TextField is <code>Text</code>. The application or user can specify resource values for these widgets in a resource file, and the application can use <code>XtNameToWidget</code> (specifying <code>&quot;*List&quot;</code> for the items list or <code>&quot;*Text&quot;</code> for the TextField widget) to obtain the widget IDs of the descendant widgets. At creation time, ComboBox passes appropriate resource values in the creation arglist, including <code>XmNitems</code>, to the items list. Note that the result of providing the <code>XmNdestroyCallback</code> resource in the creation <i>arglist</i> is unspecified. The application should use the <code>XtAddCallback</code> function to add callbacks to the appropriate widget (TextField or List) after creating it. </p>
<p> ComboBox forces the following resource values on its List child:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd>If <code>XmNcomboBoxType</code> is <code>XmCOMBO_BOX</code>, <code>XmNtraversalOn</code> is forced to False.</p>
<dt> &bull;</p>
<dd><code>XmNhighlightThickness</code> is forced to 2 in a drop-down ComboBox and to 0 in other types of ComboBoxes.</p>
<dt> &bull;</p>
<dd><code>XmNborderWidth</code> is forced to 0.</p>
<dt> &bull;</p>
<dd><code>XmNnavigationType</code> is forced to <code>XmNONE</code>.</p>
<dt> &bull;</p>
<dd><code>XmNselectionPolicy</code> is forced to <code>XmBROWSE_SELECT</code>.</p>
<dt> &bull;</p>
<dd><code>XmNlistSizePolicy</code> is forced to <code>XmVARIABLE</code>.</p>
<dt> &bull;</p>
<dd><code>XmNspacing</code> is forced to 0.</p>
<dt> &bull;</p>
<dd><code>XmNvisualPolicy</code> is forced to <code>XmVARIABLE</code>.</p>
<dt> &bull;</p>
<dd><code>XmNselectedPositions</code> is forced to NULL.</p>
<dt> &bull;</p>
<dd><code>XmNselectedPositionsCount</code> is forced to 0.</dl>
<p> When <code>XmNcomboBoxType</code> is <code>XmDROP_DOWN_LIST</code>, ComboBox forces the following resource values on its TextField child:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd><code>XmNeditable</code> is forced to False.</p>
<dt> &bull;</p>
<dd><code>XmNcursorPositionVisible</code> is forced to False.</p>
<dt> &bull;</p>
<dd><code>XmNshadowThickness</code> is forced to 0.</dl>
<p> By contrast, when <code>XmNcomboBoxType</code> is <code>XmCOMBO_BOX</code> or <code>XmDROP_DOWN_COMBO_BOX</code>, ComboBox forces the following resource values on its TextField child:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd><code>XmNeditable</code> is forced to True.</p>
<dt> &bull;</p>
<dd><code>XmNcursorPositionVisible</code> is forced to True.</p>
<dt> &bull;</p>
<dd><code>XmNeditMode</code> is forced to <code>XmSINGLE_LINE_EDIT</code>.</dl>
<p> ComboBox always forces the values of the following resources on the TextField:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd><code>XmNnavigationType</code> is forced to <code>XmNONE</code>.</p>
<dt> &bull;</p>
<dd><code>XmNhighlightThickness</code> is forced to 0.</p>
<dt> &bull;</p>
<dd><code>XmNborderWidth</code> is forced to 0.</dl>
<p> ComboBox allows a single item to be selected in two ways: by selecting the desired item from the List or by entering text into the TextField. ComboBox does not automatically select a list item if the user types that string into the TextField. It selects the item when the user presses <code>KActivate</code> or moves the focus. ComboBox supports the Browse Select selection model of List (see the <code>XmList</code> reference page for a description of this model), so selections are mutually exclusive. Selecting an item from the list causes that item to be displayed in the TextField portion of the ComboBox. If an application sets the <code>XmNvalue</code> resource of TextField, that string is shown in the TextField. If the application has not provided any list items, or if there is no current selection, the TextField is empty. </p>
<p> The TextField in the ComboBox widget can be either editable or noneditable, depending on the value of the <code>XmNcomboBoxType</code> resource. </p>
<p> If the TextField is editable, the user can type into it. When the user presses the Return key, the ComboBox will compare the typed entry to the items in the List. If there is an exact match, then the matched List item is selected. If the application wishes to validate the entered text (for example, to ensure that the typed selection is a valid one), it can do so by setting <code>XmNmodifyVerifyCallback</code> on the TextField widget. </p>
<p> If the TextField is noneditable, typing text may invoke a matching algorithm that will attempt to match the entered text with items in the list. The specific matching algorithm applied, which may be none, is determined by the value of the <code>XmNmatchBehavior</code> resource in ComboBox, which can be either <code>XmNONE</code> or <code>XmQUICK_NAVIGATE</code>. A value of <code>XmNONE</code> indicates that no matching algorithm will occur. A value of <code>XmQUICK_NAVIGATE</code> indicates that when the List widget has focus, one-character navigation is supported. In this algorithm, if the typed character is the initial character of some item in the List, this algorithm causes that item to be navigated to and selected, and the item is displayed in the TextField. Subsequently typing the same character will cycle among the items with the same first character. </p>
<p> Regardless of the selection mechanism used (either selected directly from the List or typed into the TextField), when an item in the List is selected, that item is highlighted in the List. In addition, the selected item is displayed in the TextField of the ComboBox. If the user performs an action that would move focus away from ComboBox, or selects a List item, the <code>XmNselectionCallback</code> callbacks are invoked to notify the application of the current contents of the TextField (or choice). The application then takes whatever action is required based on those contents (or choice). </p>
<p> ComboBox uses the <code>XmQTspecifyRenderTable</code> trait and holds the <code>XmQTaccessTextual</code> trait.</p>
<h3>Classes</h3>
<p><code>XmComboBox</code> inherits behavior, resources, and traits from <code>Core</code>, <code>Composite</code>, and <code>XmManager</code> classes. </p>
<p> The class pointer is <code>xmComboBoxWidgetClass</code>. </p>
<p> The class name is <code>XmComboBox</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmComboBox Resource Set</code>
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
<td>XmNarrowSize</td>
<td>XmCArrowSize</td>
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
<td>XmNarrowSpacing</td>
<td>XmCArrowSpacing</td>
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
<td>XmNcolumns</td>
<td>XmCColumn</td>
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
<td>XmNcomboBoxType</td>
<td>XmCComboBoxType</td>
<td>unsigned char</td>
<td>XmCOMBO_BOX</td>
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
<td>XmNfontList</td>
<td>XmCFontList</td>
<td>XmFontList</td>
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
<td>XmNitemCount</td>
<td>XmCItemCount</td>
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
<td>XmNitems</td>
<td>XmCItems</td>
<td>XmStringTable</td>
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
<td>XmNlist</td>
<td>XmCList</td>
<td>Widget</td>
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
<td>XmNmatchBehavior</td>
<td>XmCMatchBehavior</td>
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
<td>XmNpositionMode</td>
<td>XmCPositionMode</td>
<td>XtEnum</td>
<td>XmZERO_BASED</td>
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
<td>XmNselectedItem</td>
<td>XmCSelectedItem</td>
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
<td>XmNselectedPosition</td>
<td>XmCSelectedPosition</td>
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
<td>XmNselectionCallback</td>
<td>XmCCallback</td>
<td>XmCallbackList</td>
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
<td>XmtextField</td>
<td>XmCTextField</td>
<td>Widget</td>
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
<td>XmNvisibleItemCount</td>
<td>XmCVisibleItemCount</td>
<td>int</td>
<td>10</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
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
<dt><code>XmNarrowSize</code></p>
<dd>Specifies the width of the arrow. The default size depends on the size of the text, as well as the size of the ComboBox.</p>
<dt><code>XmNarrowSpacing</code></p>
<dd>Specifies the space between the text and arrow visual in pixels. The default value is obtained from the <code>XmNmarginWidth</code> resource.</p>
<dt><code>XmNcolumns</code></p>
<dd>Specifies the number of columns in the text field. If unset, the text field&#8217;s value is used. Refer to the <code>XmTextField</code> man page for more detailed information.</p>
<dt><code>XmNcomboBoxType</code></p>
<dd>Specifies the type of ComboBox to be created. This can be one of the following:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmCOMBO_BOX</code></p>
<dd>Generates a ComboBox where the list is always displayed, and the text entry field is editable.</p>
<dt><code>XmDROP_DOWN_COMBO_BOX</code></p>
<dd>Generates a ComboBox where the list is hidden unless specifically requested, and the text entry field is editable.</p>
<dt><code>XmDROP_DOWN_LIST</code></p>
<dd>Generates a ComboBox where the list is hidden unless specifically requested, and the text entry field is noneditable.</dl>
</dl>
<dt><code>XmNfontList</code></p>
<dd>Specifies the fontlist associated with <code>XmComboBox</code>. The fontlist is an obsolete construct, and has been superseded by the render table. It is included for compatibility with earlier versions of Motif, and for applications that do not easily support render tables. The default fontlist is derived from the default render table, and if both a fontlist and a render table are specified, the render table takes precedence.</p>
<dt><code>XmNhighlightThickness</code></p>
<dd>Specifies the thickness of the highlighting rectangle.</p>
<dt><code>XmNitemCount</code></p>
<dd>Specifies the number of items in the list. If unset, the lists&#8217;s value is used. Refer to the <code>XmList</code> man page for more detailed information.</p>
<dt><code>XmNitems</code></p>
<dd>Specifies the items in the list. If unset, the lists&#8217;s value is used. Refer to the <code>XmList</code> man page for more detailed information.</p>
<dt><code>XmNlist</code></p>
<dd>The list widget.</p>
<dt><code>XmNmarginWidth</code></p>
<dd>Specifies the horizontal spacing between the child widgets and the boundary of the ComboBox.</p>
<dt><code>XmNmarginHeight</code></p>
<dd>Specifies the vertical spacing between the child widgets and the boundary of the ComboBox.</p>
<dt><code>XmNmatchBehavior</code></p>
<dd>Defines the matching algorithm applied to match the text typed by the user in the TextField field with items in the list. The current values are <code>XmNONE</code> and <code>XmQUICK_NAVIGATE</code>, as follows:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmNONE</code></p>
<dd>Indicates that there is no assigned matching algorithm.</p>
<dt><code>XmQUICK_NAVIGATE</code></p>
<dd>Is only valid for noneditable ComboBoxes (<code>XmNcomboBoxType</code> resource value <code>XmDROP_DOWN_LIST</code>). This algorithm supports 1-character navigation when the List widget has focus. If the typed character is the initial character of some item in the List, this algorithm causes that item to be navigated to and selected. Subsequently typing the same character will cycle among the items with the same first character.</dl>
</dl>
<dt><code>XmNpositionMode</code></p>
<dd>Specifies how the value of the <code>XmNselectedPosition</code> resource and the <code>item_position</code> field of the callback structure are to be interpreted. Note that the convenience functions <code>XmComboBoxDeletePos</code> and <code>XmComboBoxAddItem</code> are not affected by this resource, and (like <code>XmList</code>) always use 1-based positions. Valid values for this resource are:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmZERO_BASED</code></p>
<dd>(DtComboBox compatibility mode: default) <code>XmNselectedPosition</code> is in <code>[0,itemcount-1]</code>. The <code>item_position</code> in the <code>XmComboBoxCallbackStruct</code> is 0 if the first element in the list was selected. Note that 0 is also returned if no element in the list was selected (that is, a new item was entered in the text field).</p>
<dt><code>XmONE_BASED</code></p>
<dd>(Motif mode) Both the resource value and the callback fields are 1-based. This is consistent with other Motif widgets.</dl>
</dl>
<dt><code>XmNrenderTable</code></p>
<dd>Specifies the render table associated with ComboBox. This render table is used in both the TextField field and the List in the ComboBox. This is used in conjunction with the <code>XmNvisibleItemCount</code> resource of the List to determine the height of the ComboBox widget.</p>
<dd>If this value is NULL at initialization, and if the widget parent is <code>XmBulletinBoard</code> or its subclasses, <code>VendorShell</code> or its subclasses, or <code>XmMenuShell</code>, then the widget parent provides the default render table associated with the widget. If both a render table and a fontlist are specified, the render table will take precedence.</p>
<dt><code>XmNselectedItem</code></p>
<dd>Specifies a compound string that represents the current selection of the ComboBox. The selected item is the content of the ComboBox text entry field.</p>
<dt><code>XmNselectedPosition</code></p>
<dd>If the selection in the ComboBox is an item in the list, this is the index of the selected item in the list. If no item in the list is selected, this is 0.</p>
<dt><code>XmNselectionCallback</code></p>
<dd>Specifies the list of callbacks called when an item is selected. The reason field in the <code>XmComboBoxCallbackStruct</code> is <code>XmCR_SELECT</code>.</p>
<dt><code>XmNtextField</code></p>
<dd>The text field widget.</p>
<dt><code>XmNvisibleItemCount</code></p>
<dd>Specifies the number of visible items in the list. This will override any value specified for the list. Refer to the <code>XmList</code> man page for more detailed information.</dl>
<h3>Inherited Resources</h3>
<p>ComboBox inherits behavior and resources from superclasses described in the following tables. For a complete description of each resource, refer to the reference page for that superclass. </p>
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
<td>XmSTICKY_TAG_GROUP</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
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
<p>A pointer to the following structure is passed to each callback. The callback structure is defined as follows: </p>
<pre>typedef struct
{
 int <i>reason</i>;
 XEvent *<i>event</i>;
 XmString <i>item_or_text</i>;
 int <i>item_position</i>;
} XmComboBoxCallbackStruct;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked.</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the callback. It can be NULL.</p>
<dt><i>item_or_text</i></p>
<dd>The contents of the text field at the time the event caused the callback. The <i>item_or_text</i> parameter points to a temporary storage space that is reused after the callback is finished. If an application needs to save the item, it should copy <i>item_or_text</i> into its own data space.</p>
<dt><i>item_position</i></p>
<dd>The position of item in the list&#8217;s <code>XmNitems</code> 1-based array. If this is 0, it means that the <i>item_or_text</i> was not selected from the List.</dl>
<h3>Translations</h3>
<p>The ComboBox translations are listed below. </p>
<p> The following key names are listed in the X standard key event translation table syntax. This format is the one used by Motif to specify the widget actions corresponding to a given key. A brief overview of the format is provided under <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3). For a complete description of the format, please refer to the X Toolkit Instrinsics Documentation. </p>
<dl COMPACT>
<dd><code>Note: </p>
<p> The KPageUp and KPageDown translations do not take effect unless the List</code> child widget is posted.</dl>
<dl COMPACT>
<dt><code>&lt;Btn1Down&gt;</code>:</p>
<dd>CBArmAndDropDownList()</p>
<dt><code>&lt;Btn1Up&gt;</code>:</p>
<dd>CBDisarm()</dl>
<p> The following lists the List translations in the drop-down list. When ComboBox <code>XmNcomboBoxType</code> is <code>XmDROP_DOWN_LIST</code>, <code>&lt;osfActivate&gt;</code>, <code>&lt;osfCancel&gt;</code>, and <code>Return</code> are overriden by ComboBox actions.</p>
<dl COMPACT>
<dt><code>:c</code> &lt;Key&gt;<code>&lt;osfDown&gt;</code>:</p>
<dd>CBDropDownList()</p>
<dt><code>:c</code> &lt;Key&gt;<code>&lt;osfUp&gt;</code>:</p>
<dd>CBDropDownList()</p>
<dt><code>:</code>&lt;Key&gt;<code>&lt;osfCancel&gt;</code>:</p>
<dd>CBCancel()</p>
<dt><code>:</code>&lt;Key&gt;<code>&lt;osfActivate&gt;</code>:</p>
<dd>CBActivate()</p>
<dt><code>&asymp;s &asymp;m &asymp;a</code>&lt;Key&gt;<code>Return</code>:</p>
<dd>CBActivate()</dl>
<h3>Accelerators</h3>
<p>The following accelerators are added to ComboBox and its children. The accelerators may not directly correspond to a translation table. If the translation is not listed below, it may depend on the context of the event.</p>
<dl COMPACT>
<dt><code>:c</code> &lt;Key&gt;<code>&lt;osfUp&gt;</code>:</p>
<dd>CBDropDownList()</p>
<dt><code>:</code>&lt;Key&gt;<code>&lt;osfUp&gt;</code>:</p>
<dd>CBListAction(<code>Up</code>)</p>
<dt><code>:c</code> &lt;Key&gt;<code>&lt;osfDown&gt;</code>:</p>
<dd>CBDropDownList()</p>
<dt><code>:</code>&lt;Key&gt;<code>&lt;osfDown&gt;</code>:</p>
<dd>CBListAction(<code>Down</code>)</p>
<dt><code>:c</code> &lt;Key&gt;<code>&lt;osfBeginLine&gt;</code>:</p>
<dd>CBListAction(<code>ListBeginData</code>)</p>
<dt><code>:c</code> &lt;Key&gt;<code>&lt;osfEndLine&gt;</code>:</p>
<dd>CBListAction(<code>ListEndData</code>)</p>
<dt><code>:</code>&lt;Key&gt;<code>&lt;osfPageUp&gt;</code>:</p>
<dd>CBListAction(<code>ListPrevPage</code>)</p>
<dt><code>:</code>&lt;Key&gt;<code>&lt;osfPageDown&gt;</code>:</p>
<dd>CBListAction(<code>ListNextPage</code>)</dl>
<p> A drop-down ComboBox also adds accelerators to its List child. Aside from the accelerators that are already listed in this section, those accelerators are the default TextField key translations.</p>
<h3>Action Routines</h3>
<p>The <code>XmComboBox</code> action routines are as follows:</p>
<dl COMPACT>
<dt>CBActivate():</p>
<dd>Calls the <code>XmNselectionCallback</code> callbacks. If the <code>XmNcomboBoxType</code> is <code>XmDROP_DOWN_COMBO_BOX</code> or <code>XmDROP_DOWN_LIST</code>, it unposts the list. If the parent is a manager, passes the event to the parent.</p>
<dt>CBArmAndDropDownList():</p>
<dd>If the pointer is within the down arrow, draws the shadow of the arrow in the selected state, and then posts the list.</p>
<dt>CBCancel():</p>
<dd>If the <code>XmNcomboBoxType</code> is <code>XmDROP_DOWN_COMBO_BOX</code> or <code>XmDROP_DOWN_LIST</code>, pops down the list. If the parent is a manager, passes the event to the parent.</p>
<dt>CBDisarm():</p>
<dd>Redraws the arrow in an unselected state.</p>
<dt>CBDropDownList():</p>
<dd>If <code>XmNcomboBoxType</code> is <code>XmDROP_DOWN</code> or <code>XmDROP_DOWN_LIST</code>, and list is not displayed, posts the list. If list is displayed, it unposts the list.</p>
<dt>CBListAction(<code>ListBeginData</code>):</p>
<dd>Moves the location cursor to the first item in the list. In Normal Mode, this also deselects any current selection, selects the first item in the list, and calls the <code>XmNbrowseSelectionCallback</code> selection callback.</p>
<dt>CBListAction(<code>ListEndData</code>):</p>
<dd>Moves the location cursor to the last item in the list. In Normal Mode, this also deselects any current selection, selects the last item in the list, and calls the <code>XmNbrowseSelectionCallback</code> selection callback.</p>
<dt>CBListAction(<code>ListPrevPage</code>):</p>
<dd>Scrolls the list to the previous page, moving the location cursor to a new item. This action also selects the new item, deselects any current selection, and calls the <code>XmNbrowseSelectionCallback</code> callbacks. If the ComboBox is not a drop-down type, then this action does nothing.</p>
<dt>CBListAction(<code>ListNextPage</code>):</p>
<dd>Scrolls the list to the next page, moving the location cursor to a new item. This action also selects the new item, deselects any current selection, and calls the <code>XmNbrowseSelectionCallback</code> callbacks. If the ComboBox is not a drop-down type, then this action does nothing.</p>
<dt>CBListAction(<code>Up</code>):</p>
<dd>Moves the location cursor to the previous item in the list. This action also selects the previous item, deselects any current selection, and calls the <code>XmNbrowseSelectionCallback</code> callbacks. Note that, unlike the List <code>ListPrevItem</code> action, this action wraps around.</p>
<dt>CBListAction(<code>Down</code>):</p>
<dd>Moves the location cursor to the next item in the list. This action also selects the next item, deselects any current selection, and calls the <code>XmNbrowseSelectionCallback</code> callbacks. Note that, unlike the List <code>ListNextItem</code> action, this action wraps around.</dl>
<h3>Virtual Bindings</h3>
<p>The bindings for virtual keys are vendor specific. For information about bindings for virtual buttons and keys, see <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3).</p>
<h2>Errors/Warnings</h2>
<p>The toolkit will display a warning if the application tries to set the value of <code>XmNlist</code> or the <code>XmNtextField</code> resource, which are read-only (marked G in the resource table).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-composite/">Composite</a></code>(3), <code><a href="/docs/linux/man/3-core/">Core</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatecombobox/">XmCreateComboBox</a></code>(3), <code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3), <code><a href="/docs/linux/man/3-xmmanager/">XmManager</a></code>(3), <code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatecombobox/">XmVaCreateComboBox</a></code>(3), and <code><a href="/docs/linux/man/3-xmvacreatemanagedcombobox/">XmVaCreateManagedComboBox</a></code>(3).</p>
