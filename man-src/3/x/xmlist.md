---
title: "xmlist(3)"
name: "xmlist"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmlist/"
description: "XmList — The List widget class"
---

<p><code>XmList</code> &#8212; The List widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/List.h&gt;</pre>
<h2>Description</h2>
<p>List allows a user to select one or more items from a group of choices. Items are selected from the list in a variety of ways, using both the pointer and the keyboard. List operates on an array of compound strings that are defined by the application. Each compound string becomes an item in the List, with the first compound string becoming the item in position 1, the second becoming the item in position 2, and so on. </p>
<p> Specifying the number of items that are visible sets the size of the List. If the number of visible items is not specified, the height of the list controls the number of visible items. Each item assumes the height of the tallest element in the list. To create a list that allows the user to scroll easily through a large number of items, use the <code>XmCreateScrolledList</code> convenience function. </p>
<p> To select items, move the pointer or cursor to the desired item and press the <code>&lt;Btn1&gt;</code> mouse button or the key defined as <code>&lt;osfSelect&gt;</code>. There are several styles of selection behavior, and they all highlight the selected item or items by displaying them in inverse colors. An appropriate callback is invoked to notify the application of the user&#8217;s choice. The application then takes whatever action is required for the specified selection. When a List is insensitive, all of the list items are displayed in a stippled fill pattern. </p>
<p> List uses the <code>XmQTspecifyRenderTable</code>, <code>XmQTscrollFrame</code>, and <code>XmQTnavigator</code> traits, and holds the <code>XmQTtransfer</code> trait.</p>
<h3>Selection</h3>
<p>Each list has one of four selection models:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd>Single Select</p>
<dt> &bull;</p>
<dd>Browse Select</p>
<dt> &bull;</p>
<dd>Multiple Select</p>
<dt> &bull;</p>
<dd>Extended Select</dl>
<p> In Single Select and Browse Select, at most one item is selected at a time. In Single Select, pressing <code>&lt;Btn1&gt;</code> on an item toggles its selection state and deselects any other selected item. In Browse Select, pressing <code>&lt;Btn1&gt;</code> on an item selects it and deselects any other selected item; dragging <code>&lt;Btn1&gt;</code> moves the selection as the pointer is moved. Releasing <code>&lt;Btn1&gt;</code> on an item moves the location cursor to that item. </p>
<p> In Multiple Select, any number of items can be selected at a time. Pressing <code>&lt;Btn1&gt;</code> on an item toggles its selection state but does not deselect any other selected items. </p>
<p> In Extended Select, any number of items can be selected at a time, and the user can easily select ranges of items. Pressing <code>&lt;Btn1&gt;</code> on an item selects it and deselects any other selected item. Dragging <code>&lt;Btn1&gt;</code> or pressing or dragging <code>&lt;Shift&gt;</code><code>&lt;Btn1&gt;</code> following a <code>&lt;Btn1&gt;</code> action selects all items between the item under the pointer and the item on which <code>&lt;Btn1&gt;</code> was pressed. This action also deselects any other selected items outside that range. </p>
<p> Extended Select also allows the user to select and deselect discontiguous ranges of items. Pressing <code>&lt;Ctrl&gt;</code><code>&lt;Btn1&gt;</code> on an item toggles its selection state but does not deselect any other selected items. Dragging <code>&lt;Ctrl&gt;</code><code>&lt;Btn1&gt;</code> or pressing or dragging <code>&lt;Shift&gt;</code><code>&lt;Btn1&gt;</code> following a <code>&lt;Ctrl&gt;</code><code>&lt;Btn1&gt;</code> action sets the selection state of all items between the item under the pointer and the item on which <code>&lt;Ctrl&gt;</code><code>&lt;Btn1&gt;</code> was pressed to the state of the item on which <code>&lt;Ctrl&gt;</code><code>&lt;Btn1&gt;</code> was pressed. This action does not deselect any other selected items outside that range. </p>
<p> All selection operations available from the mouse are also available from the keyboard. List has two keyboard selection modes, Normal Mode and Add Mode. In Normal Mode, navigation operations and <code>&lt;osfSelect&gt;</code> select the item at the location cursor and deselect any other selected items. In Add Mode, navigation operations have no effect on selection, and <code>&lt;osfSelect&gt;</code> toggles the selection state of the item at the location cursor without deselecting any other selected items, except in Single Select. </p>
<p> Single and Multiple Select use Add Mode, and Browse Select uses Normal Mode. </p>
<p> Extended Select can use either mode; the user changes modes by pressing <code>&lt;osfAddMode&gt;</code>. In Extended Select Normal Mode, pressing <code>&lt;osfSelect&gt;</code> has the same effect as pressing <code>&lt;Btn1&gt;</code>; <code>&lt;osfExtend&gt;</code> and shifted navigation have the same effect as pressing <code>&lt;Shift&gt;</code><code>&lt;Btn1&gt;</code> following a <code>&lt;Btn1&gt;</code> action. In Extended Select Add Mode, pressing <code>&lt;osfSelect&gt;</code> has the same effect as pressing <code>&lt;Ctrl&gt;</code><code>&lt;Btn1&gt;</code>; <code>&lt;osfExtend&gt;</code> and shifted navigation have the same effect as pressing <code>&lt;Shift&gt;</code><code>&lt;Btn1&gt;</code> following a <code>&lt;Ctrl&gt;</code><code>&lt;Btn1&gt;</code> action. </p>
<p> Normal Mode is indicated by a solid location cursor, and Add Mode is indicated by a dashed location cursor.</p>
<h3>Data Transfer Behavior</h3>
<p>List supports dragging of items from the List and transfer of items to the clipboard. When the user presses <code>BTransfer</code> on a selected item, the widget transfers all selected items. When the user presses <code>BTransfer</code> on an unselected item, the widget transfers only that item. Depending on the value of <code>XmNprimaryOwnership</code>, List can also support primary selection. </p>
<p> When the <code>XmNconvertCallback</code> procedures are called, the <code>location_data</code> member of the <code>XmConvertCallbackStruct</code> member is NULL if the selected items are being transferred. If the selected items are not being transferred, this member has the following value: If a single item is being transferred, the value is an integer representing the position of the item in the List. A value of 1 transfers the first item in the List; a value of 2 transfers the second item; and so on. If the entire contents of the List are being transferred, the value is -1. </p>
<p> As a source of data, List supports the following targets and associated conversions of data to these targets:</p>
<dl COMPACT>
<dt><i>locale</i></p>
<dd>If the <i>locale</i> target matches the widget&#8217;s locale, the widget transfers the selected list items in the encoding of the locale. Each item transferred except the last includes a trailing separator.</p>
<dt><code>COMPOUND_TEXT</code></p>
<dd>The widget transfers the selected list items as type <code>COMPOUND_TEXT</code>. Each item transferred except the last includes a trailing separator.</p>
<dt><code>UTF8_STRING</code></p>
<dd>The widget transfers the selected list items as type <code>UTF8_STRING</code>. Each item transferred except the last includes a trailing separator.</p>
<dt><code>STRING</code></p>
<dd>The widget transfers the selected list items as type <code>STRING</code>. Each item transferred except the last includes a trailing separator.</p>
<dt><code>TEXT</code></p>
<dd>If the selected list items are fully convertible to the encoding of the locale, the widget transfers the selected list items in the encoding of the locale. Otherwise, the widget transfers the selected list items as type <code>COMPOUND_TEXT</code>. Each item transferred except the last includes a trailing separator.</p>
<dt><code>_MOTIF_CLIPBOARD_TARGETS</code></p>
<dd>The widget transfers, as type <code>ATOM</code>, a list of the targets it supports for immediate transfer for the <code>CLIPBOARD</code> selection. These include <code>_MOTIF_COMPOUND_STRING</code>. If the selected list items are fully convertible to <code>STRING</code>, these also include <code>STRING</code>; otherwise, they also include <code>COMPOUND_TEXT</code> and <code>UTF8_STRING</code>.</p>
<dt><code>_MOTIF_COMPOUND_STRING</code></p>
<dd>The widget transfers the selected list items as a compound string in Byte Stream format. Each item transferred except the last includes a trailing separator.</p>
<dt><code>_MOTIF_DEFERRED_CLIPBOARD_TARGETS</code></p>
<dd>The widget transfers, as type <code>ATOM</code>, a list of the targets it supports for delayed transfer for the <code>CLIPBOARD</code> selection. This widget currently supplies no targets for <code>_MOTIF_DEFERRED_CLIPBOARD_TARGETS</code>.</p>
<dt><code>_MOTIF_EXPORT_TARGETS</code></p>
<dd>The widget transfers, as type <code>ATOM</code>, a list of the targets to be used as the value of the DragContext&#8217;s <code>XmNexportTargets</code> in a drag-and-drop transfer. These include <code>_MOTIF_COMPOUND_STRING</code>, <code>COMPOUND_TEXT</code>, <code>UTF8_STRING</code>, the encoding of the locale, <code>STRING</code>, <code>TEXT</code>, <code>BACKGROUND</code>, and <code>FOREGROUND</code>.</p>
<dt><code>_MOTIF_LOSE_SELECTION</code></p>
<dd>When the widget loses the selection, it deselects all list items.</dl>
<p> As a source of data, List also supports the following standard Motif targets:</p>
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
<dd>The widget transfers, as type <code>ATOM</code>, a list of the targets it supports. These include the standard targets in this list. These also include <code>_MOTIF_COMPOUND_STRING</code>, <code>COMPOUND_TEXT</code>, <code>UTF8_STRING</code> the encoding of the locale, <code>STRING</code>, and <code>TEXT</code>.</p>
<dt><code>TIMESTAMP</code></p>
<dd>The widget transfers the timestamp used to acquire the selection as type <code>INTEGER</code>.</p>
<dt><code>_MOTIF_RENDER_TABLE</code></p>
<dd>The widget transfers <code>XmNrenderTable</code> if it exists, or else the default text render table, as type <code>STRING</code>.</p>
<dt><code>_MOTIF_ENCODING_REGISTRY</code></p>
<dd>The widget transfers its encoding registry as type <code>STRING</code>. The value is a list of NULL separated items in the form of tag encoding pairs. This target symbolizes the transfer target for the Motif Segment Encoding Registry. Widgets and applications can use this Registry to register text encoding formats for specified render table tags. Applications access this Registry by calling <code>XmRegisterSegmentEncoding</code> and <code>XmMapSegmentEncoding</code>.</dl>
<p> List has no widget class destination procedure. Subclasses and the <code>XmNdestinationCallback</code> procedures are responsible for any data transfers to the widget.</p>
<h3>Classes</h3>
<p>List inherits behavior, resources, and traits from <code>Core</code> and <code>XmPrimitive</code>. </p>
<p> The class pointer is <code>xmListWidgetClass</code>. </p>
<p> The class name is <code>XmList</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmList Resource Set</code>
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
<td>XmNautomaticSelection</td>
<td>XmCAutomaticSelection</td>
<td>XtEnum</td>
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
<td>XmNbrowseSelectionCallback</td>
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
<td>XmNdefaultActionCallback</td>
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
<td>XmNdoubleClickInterval</td>
<td>XmCDoubleClickInterval</td>
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
<td>XmNextendedSelectionCallback</td>
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
<td>XmNitemCount</td>
<td>XmCItemCount</td>
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
<td>XmNitems</td>
<td>XmCItems</td>
<td>XmStringTable</td>
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
<td>XmNlistMarginHeight</td>
<td>XmCListMarginHeight</td>
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
<td>XmNlistMarginWidth</td>
<td>XmCListMarginWidth</td>
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
<td>XmNlistSizePolicy</td>
<td>XmCListSizePolicy</td>
<td>unsigned char</td>
<td>XmVARIABLE</td>
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
<td>XmNlistSpacing</td>
<td>XmCListSpacing</td>
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
<td>XmNmatchBehavior</td>
<td>XmCMatchBehavior</td>
<td>unsigned char</td>
<td>XmQUICK_NAVIGATE</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNmultipleSelectionCallback</td>
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
<td>XmNprimaryOwnership</td>
<td>XmCPrimaryOwnership</td>
<td>unsigned char</td>
<td>XmOWN_NEVER</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
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
<td>XmNscrollBarDisplayPolicy</td>
<td>XmCScrollBarDisplayPolicy</td>
<td>unsigned char</td>
<td>XmAS_NEEDED</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
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
<td>XmRSelectColor</td>
<td>XmREVERSED_GROUND_COLORS</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNselectedItemCount</td>
<td>XmCSelectedItemCount</td>
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
<td>XmNselectedItems</td>
<td>XmCSelectedItems</td>
<td>XmStringTable</td>
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
<td>XmNselectedPositionCount</td>
<td>XmCSelectedPositionCount</td>
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
<td>XmNselectedPositions</td>
<td>XmCSelectedPositions</td>
<td>unsigned int *</td>
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
<td>XmNselectionMode</td>
<td>XmCSelectionMode</td>
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
<td>XmNselectionPolicy</td>
<td>XmCSelectionPolicy</td>
<td>unsigned char</td>
<td>XmBROWSE_SELECT</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNsingleSelectionCallback</td>
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
<tr VALIGN=top>
<td>XmNtopItemPosition</td>
<td>XmCTopItemPosition</td>
<td>int</td>
<td>1</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
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
<dt><code>XmNautomaticSelection</code></p>
<dd>Invokes either <code>XmNbrowseSelectionCallback</code> or <code>XmNextendedSelectionCallback</code> when <code>&lt;Btn1&gt;</code> is pressed and the items that are shown as selected change if the value is True (or <code>XmAUTO</code>) and the selection mode is either <code>XmBROWSE_SELECT</code> or <code>XmEXTENDED_SELECT</code> respectively. If False (<code>XmNO_AUTO_SELECT</code>), no selection callbacks are invoked until the user releases the mouse button. See <code>Behavior</code> for further details on the interaction of this resource with the selection modes.</p>
<dt><code>XmNbrowseSelectionCallback</code></p>
<dd>Specifies a list of callbacks that is called when an item is selected in the browse selection mode. The reason is <code>XmCR_BROWSE_SELECT</code>.</p>
<dt><code>XmNdefaultActionCallback</code></p>
<dd>Specifies a list of callbacks that is called when an item is double clicked or <code>&lt;osfActivate&gt;</code> is pressed. The reason is <code>XmCR_DEFAULT_ACTION</code>.</p>
<dt><code>XmNdestinationCallback</code></p>
<dd>Specifies a list of callbacks called when the List is the destination of a transfer operation. The type of the structure whose address is passed to these callbacks is <code>XmDestinationCallbackStruct</code>. The reason is <code>XmCR_OK</code>.</p>
<dt><code>XmNdoubleClickInterval</code></p>
<dd>If a button click is followed by another button click within the time span specified by this resource (in milliseconds), the button clicks are considered a double-click action, rather than two single-click actions. The value must not be negative. The default value is the display&#8217;s multiclick time.</p>
<dt><code>XmNextendedSelectionCallback</code></p>
<dd>Specifies a list of callbacks that is called when items are selected using the extended selection mode. The reason is <code>XmCR_EXTENDED_SELECT</code>.</p>
<dt><code>XmNfontList</code></p>
<dd>Specifies the font list associated with the list items. <code>XmNfontList</code> is obsolete and exists only for compatibility with previous releases. You should now use <code>XmNrenderTable</code> instead of <code>XmNfontList</code>. If both are specified, the render table will take precedence. The font list is used in conjunction with the <code>XmNvisibleItemCount</code> resource to determine the height of the List widget. If this value is NULL at initialization, the parent hierarchy of the widget is searched for a widget that holds the <code>XmQTspecifyRenderTable</code> trait. If such an ancestor is found, the font list is initialized to the <code>XmTEXT_RENDER_TABLE</code> value of the ancestor widget. If no such widget is found, the default is implementation dependent. Refer to <code><a href="/docs/linux/man/3-xmfontlist/">XmFontList</a></code>(3) for more information on a font list structure.</p>
<dt><code>XmNitemCount</code></p>
<dd>Specifies the total number of items. The value must be the number of items in <code>XmNitems</code> and must not be negative. It is automatically updated by the list whenever an item is added to or deleted from the list.</p>
<dt><code>XmNitems</code></p>
<dd>Points to an array of compound strings that are to be displayed as the list items. Refer to <code><a href="/docs/linux/man/3-xmstring/">XmString</a></code>(3) for more information on the creation and structure of compound strings. <code>XtGetValues</code> for this resource returns the list items themselves, not a copy of the list items. The application must not free the returned items.</p>
<dt><code>XmNlistMarginHeight</code></p>
<dd>Specifies the height of the margin between the list border and the items.</p>
<dt><code>XmNlistMarginWidth</code></p>
<dd>Specifies the width of the margin between the list border and the items.</p>
<dt><code>XmNlistSizePolicy</code></p>
<dd>Controls the reaction of the List when an item grows horizontally beyond the current size of the list work area. If the value is <code>XmCONSTANT</code>, the list viewing area does not grow, and a horizontal ScrollBar is added for a List whose parent is a ScrolledWindow. If this resource is set to <code>XmVARIABLE</code>, the List grows to match the size of the longest item, and no horizontal ScrollBar appears.</p>
<dd>When the value of this resource is <code>XmRESIZE_IF_POSSIBLE</code>, the List attempts to grow or shrink to match the width of the widest item. If it cannot grow to match the widest size, a horizontal ScrollBar is added for a List whose parent is a ScrolledWindow if the longest item is wider than the list viewing area.</p>
<dd>The size policy must be set at the time the List widget is created. It cannot be changed at a later time through <code>XtSetValues</code>.</p>
<dt><code>XmNlistSpacing</code></p>
<dd>Specifies the spacing between list items. This spacing increases by the value of the <code>XmNhighlightThickness</code> resource in Primitive.</p>
<dt><code>XmNmatchBehavior</code></p>
<dd>Specifies the matching behavior followed by XmList. The current values are <code>XmNONE</code> and <code>XmQUICK_NAVIGATE</code>, as follows:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmNONE</code></p>
<dd>Specifies that the typed in characters are ignored.</p>
<dt><code>XmQUICK_NAVIGATE</code></p>
<dd>Specifies that 1-character navigation shall be supported when List has focus. If the typed character is the initial character of some set of items in List, the first of those items following the current item will be navigated to (become the current item). If all such items precede the current item, the first such item becomes the current item. Subsequently, typing the same character will cyclically navigate among the items with the same first character.</dl>
</dl>
<dt><code>XmNmultipleSelectionCallback</code></p>
<dd>Specifies a list of callbacks that is called when an item is selected in multiple selection mode. The reason is <code>XmCR_MULTIPLE_SELECT</code>.</p>
<dt><code>XmNprimaryOwnership</code></p>
<dd>Specifies whether XmContainer takes ownership of the Primary selection when a selection is made inside it. This resource can take the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmOWN_NEVER</code></p>
<dd>Never takes ownership.</p>
<dt><code>XmOWN_ALWAYS</code></p>
<dd>Always takes ownership.</p>
<dt><code>XmOWN_MULTIPLE</code></p>
<dd>Only takes ownership is more than one element has been selected.</p>
<dt><code>XmOWN_POSSIBLE_MULTIPLE</code></p>
<dd>Only takes ownership if more than one element can be selected at a time.</dl>
</dl>
<dt><code>XmNrenderTable</code></p>
<dd>Specifies the render table associated with the list items. The render table is used in conjunction with the <code>XmNvisibleItemCount</code> resource to determine the height of the List widget. If this value is NULL at initialization, List searches its parent hierarchy for a widget that holds the <code>XmQTspecifyRenderTable</code> trait. If such an ancestor is found, the render table is initialized to the <code>XmTEXT_RENDER_TABLE</code> value of the ancestor widget. If no such widget is found, the default is implementation dependent. If a font list and a render table are both specified, the render table will take precedence. Refer to <code><a href="/docs/linux/man/3-xmrendertable/">XmRenderTable</a></code>(3) for more information on the creation and structure of a render table.</p>
<dt><code>XmNscrollBarDisplayPolicy</code></p>
<dd>Controls the display of vertical ScrollBars in a List whose parent is a ScrolledWindow. When the value of this resource is <code>XmAS_NEEDED</code>, a vertical ScrollBar is displayed only when the number of items in the List exceeds the number of visible items. When the value is <code>XmSTATIC</code>, a vertical ScrollBar is always displayed.</p>
<dt><code>XmNselectColor</code></p>
<dd>Allows the application to specify the color of the background rectangle that indicates selected text. It takes two values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmDEFAULT_SELECT_COLOR</code></p>
<dd>Causes the select color to be set to a color between the background and the bottom shadow color.</p>
<dt><code>XmREVERSED_GROUND_COLORS</code></p>
<dd>Forces the select color to the foreground color and the color of any text rendered over the select color to be in the background color.</p>
<dt><code>HIGHLIGHT_COLOR</code></p>
<dd>Forces the fill color to use the highlight color.</dl>
</dl>
<dt><code>XmNselectedItemCount</code></p>
<dd>Specifies the number of strings in the selected items list. The value must be the number of items in <code>XmNselectedItems</code> and must not be negative.</p>
<dt><code>XmNselectedItems</code></p>
<dd>Points to an array of compound strings that represents the list items that are currently selected, either by the user or by the application. <code>XtGetValues</code> for this resource returns the list items themselves, not a copy of the list items. The application must not free the returned items or the array.</p>
<dd>Setting <code>XmNselectedItems</code> selects those list items that exactly match items in the given <code>XmNselectedItems</code> list. There may be additional items in <code>XmNselectedItems</code> that do not match items in the list. These items remain until <code>XmNselectedItems</code> is updated. If <code>XmNitems</code> is changed such that the list now contains items matching previously unmatched items in <code>XmNselectedItems</code>, those new items will also appear selected.</p>
<dd>Any user interaction with the list that causes at least one item to be selected or deselected and any call to <code>XmListDeleteAllItems</code>, <code>XmListDeleteItem</code>, <code>XmListDeleteItems</code>, <code>XmListDeleteItemsPos</code>, <code>XmListDeletePos</code>, <code>XmListDeletePositions</code>, <code>XmListDeselectAllItems</code>, <code>XmListDeselectItem</code>, <code>XmListDeselectPos</code>, <code>XmListSelectItem</code>, <code>XmListSelectPos</code>, or <code>XmListUpdateSelectedList</code> cause <code>XmNselectedItems</code> to be updated immediately to exactly reflect the visual state of the list. Calls to any other <code>XmList</code> functions do not affect <code>XmNselectedItems</code>.</p>
<dt><code>XmNselectedPositionCount</code></p>
<dd>Specifies the number of positions in the selected positions list. The value must be the number of items in <code>XmNselectedPositions</code></p>
<dt><code>XmNselectedPositions</code></p>
<dd>Points to an array of the positions of the selected items in the List. <code>XtGetValues</code> for this resource returns the list items themselves, not a copy of the list items. The application must not free the returned items or the array.</p>
<dt><code>XmNselectionMode</code></p>
<dd>Defines what effect keyboard navigations have on selection. The valid modes are:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmADD_MODE</code></p>
<dd>Allows no navigation operations to have effect on selection, and <code>&lt;osfSelect&gt;</code> toggles the selection state of the item at the location cursor without deselecting any other selected items, except in Single Select. However, the widget cannot be put into add mode if the <code>XmNselectionPolicy</code> resource is an incompatible mode (<code>XmNselectionPolicy</code> cannot be <code>XmBROWSE_SELECT</code>).</p>
<dt><code>XmNORMAL_MODE</code></p>
<dd>Allows navigation operations and <code>&lt;osfSelect&gt;</code> to select the item at the location cursor and deselect any other selected items. However, the widget cannot be put into normal mode if the <code>XmNselectionPolicy</code> resource is an incompatible mode (<code>XmNselectionPolicy</code> cannot be <code>XmSINGLE_SELECT</code> or <code>XmMULTIPLE_SELECT</code>).</dl>
</dl>
<dt><code>XmNselectionPolicy</code></p>
<dd>Defines the interpretation of the selection action. This can be one of the following:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmSINGLE_SELECT</code></p>
<dd>Allows only single selections</p>
<dt><code>XmMULTIPLE_SELECT</code></p>
<dd>Allows multiple selections</p>
<dt><code>XmEXTENDED_SELECT</code></p>
<dd>Allows extended selections</p>
<dt><code>XmBROWSE_SELECT</code></p>
<dd>Allows drag-and-browse functionality</dl>
</dl>
<dt><code>XmNsingleSelectionCallback</code></p>
<dd>Specifies a list of callbacks that is called when an item is selected in single selection mode. The reason is <code>XmCR_SINGLE_SELECT</code>.</p>
<dt><code>XmNstringDirection</code></p>
<dd>Is a synthetic resource for setting <code>XmNlayoutDirection</code>. The values for this resource are <code>XmSTRING_DIRECTION_L_TO_R</code> and <code>XmSTRING_DIRECTION_R_TO_L</code>. Refer to the <code>XmNlayoutDirection</code> resource description. The <code>XmNstringDirection</code> resource is obsoleted by <code>XmNlayoutDirection</code>, but is kept here for backward compatibility.</p>
<dt><code>XmNtopItemPosition</code></p>
<dd>Specifies the position of the item that is the first visible item in the list. Setting this resource is equivalent to calling the <code>XmListSetPos</code> function. The position of the first item in the list is 1; the position of the second item is 2; and so on. A position of 0 (zero) specifies the last item in the list. The value must not be negative.</p>
<dt><code>XmNvisibleItemCount</code></p>
<dd>Specifies the number of items that can fit in the visible space of the list work area. The List uses this value to determine its height. The value must be greater than 0 (zero).</dl>
<h3>Inherited Resources</h3>
<p>List inherits behavior and resources from the superclasses described in the following tables. For a complete description of each resource, refer to the reference page for that superclass. </p>
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
<p>List defines a new callback structure. The application must first look at the reason field and use only the structure members that are valid for that particular reason, because not all fields are relevant for every possible reason. The callback structure is defined as follows: </p>
<pre>typedef struct
{
 int <i>reason</i>;
 XEvent *<i>event</i>;
 XmString <i>item</i>;
 int <i>item_length</i>;
 int <i>item_position</i>;
 XmString *<i>selected_items</i>;
 int <i>selected_item_count</i>;
 int *<i>selected_item_positions</i>;
 char <i>selection_type</i>;
 unsigned char <i>auto_selection_type</i>;
} XmListCallbackStruct;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked.</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the callback. It can be NULL.</p>
<dt><i>item</i></p>
<dd>The last item selected at the time of the <i>event</i> that caused the callback. <i>item</i> points to a temporary storage space that is reused after the callback is finished. Therefore, if an application needs to save the item, it should copy the item into its own data space.</p>
<dt><i>item_length</i></p>
<dd>The length in bytes of <i>item</i>. This member is obsolete and exists for compatibility with earlier releases.</p>
<dt><i>item_position</i></p>
<dd>The position (plus one) of <i>item</i> in the List&#8217;s <code>XmNitems</code> array. An <i>item_position</i> value of one symbolizes the first element in the list.</p>
<dt><i>selected_items</i></p>
<dd>A list of items selected at the time of the <i>event</i> that caused the callback. <i>selected_items</i> points to a temporary storage space that is reused after the callback is finished. Therefore, if an application needs to save the selected list, it should copy the list into its own data space.</p>
<dt><i>selected_item_count</i></p>
<dd>The number of items in the <i>selected_items</i> list. This number must be non-negative.</p>
<dt><i>selected_item_positions</i></p>
<dd>An array of integers, one for each selected item, representing the position of each selected item in the List&#8217;s <code>XmNitems</code> array. <i>selected_item_positions</i> points to a temporary storage space that is reused after the callback is finished. Therefore, if an application needs to save this array, it should copy the array into its own data space.</p>
<dt><i>selection_type</i></p>
<dd>Indicates that the most recent extended selection was the initial selection (<code>XmINITIAL</code>), a modification of an existing selection (<code>XmMODIFICATION</code>), or an additional noncontiguous selection (<code>XmADDITION</code>).</p>
<dt><code>auto_selection_type</code></p>
<dd>Indicates the type of automatic selection callback. The types of callbacks include the following:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmAUTO_BEGIN</code></p>
<dd>Indicates the beginning of automatic selection.</p>
<dt><code>XmAUTO_MOTION</code></p>
<dd>Indicates that there is a button drag selection.</p>
<dt><code>XmAUTO_CANCEL</code></p>
<dd>Indicates that the new selection is cancelled.</p>
<dt><code>XmAUTO_NO_CHANGE</code></p>
<dd>Indicates that the currently selected item matches the initial item.</p>
<dt><code>XmAUTO_CHANGE</code></p>
<dd>Indicates that the currently selected item does not match the initial item.</dl>
</dl>
</dl>
<p> The following table describes the reasons for which the individual callback structure fields are valid. </p>
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
<td>XmCR_SINGLE_SELECT</td>
<td> <i>reason, event, item, item_length, item_position</i>
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
<td>XmCR_DEFAULT_ACTION</td>
<td> <i>reason, event, item, item_length, item_position, selected_items, selected_item_count, selected_item_positions</i>
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
<td>XmCR_BROWSE_SELECT</td>
<td> <i>reason, event, item, item_length, item_position</i>
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
<td>XmCR_MULTIPLE_SELECT</td>
<td> <i>reason, event, item, item_length, item_position, selected_items, selected_item_count, selected_item_positions</i>
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
<td>XmCR_EXTENDED_SELECT</td>
<td> <i>reason, event, item, item_length, item_position, selected_items, selected_item_count, selected_item_positions, selection_type</i>
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
<dd>When the selection is <code>PRIMARY</code>, possible values are <code>XmMOVE</code>, <code>XmCOPY</code>, and <code>XmLINK</code>.</p>
<dt> &bull;</p>
<dd>When the selection is <code>SECONDARY</code> or <code>CLIPBOARD</code>, possible values are <code>XmCOPY</code> and <code>XmLINK</code>.</p>
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
<dd>Contains information about the location where data is to be transferred. The value is always NULL when the selection is <code>SECONDARY</code> or <code>CLIPBOARD</code>. If the value is NULL, the data is to be inserted at the widget&#8217;s cursor position. Otherwise, the value is an integer representing the position in the List where the items are to be transferred. A value of 1 makes the first new item the first item in the list; a value of 2 makes it the second item; and so on. Once <code>XmTransferDone</code> procedures start to be called, <code>location_data</code> will no longer be stable.</p>
<dt><i>time</i></p>
<dd>Indicates the time when the transfer operation began.</dl>
<h3>Translations</h3>
<p><code>XmList</code> includes translations from Primitive. The <code>XmList</code> translations are described in the following list. </p>
<p> The following key names are listed in the X standard key event translation table syntax. This format is the one used by Motif to specify the widget actions corresponding to a given key. A brief overview of the format is provided under <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3). For a complete description of the format, please refer to the X Toolkit Instrinsics Documentation.</p>
<dl COMPACT>
<dt><code>&lt;Btn1&gt;</code><code>&lt;Motion&gt;</code>:</p>
<dd>ListButtonMotion()</p>
<dt><code>s &asymp;m &asymp;a</code> <code>&lt;Btn1Down&gt;</code>:</p>
<dd>ListBeginExtend()</p>
<dt><code>s &asymp;m &asymp;a</code> <code>&lt;Btn1Up&gt;</code>:</p>
<dd>ListEndExtend()</p>
<dt><code>c &asymp;s &asymp;m &asymp;a</code> <code>&lt;Btn1Down&gt;</code>:</p>
<dd>ListBeginToggle()</p>
<dt><code>c &asymp;s &asymp;m &asymp;a</code> <code>&lt;Btn1Up&gt;</code>:</p>
<dd>ListEndToggle()</p>
<dt><code>&asymp;s &asymp;c &asymp;m &asymp;a</code> <code>&lt;Btn1Down&gt;</code>:</p>
<dd>ListBeginSelect()</p>
<dt><code>&asymp;s &asymp;c &asymp;m &asymp;a</code> <code>&lt;Btn1Up&gt;</code>:</p>
<dd>ListEndSelect()</p>
<dt><code>&lt;Btn2Down&gt;</code>:</p>
<dd>ListProcessDrag()</p>
<dt><code>:s c</code> <code>&lt;Key&gt;</code><code>&lt;osfBeginLine&gt;</code>:</p>
<dd>ListBeginDataExtend()</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfBeginLine&gt;</code>:</p>
<dd>ListBeginData()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfBeginLine&gt;</code>:</p>
<dd>ListBeginLine()</p>
<dt><code>:s c</code> <code>&lt;Key&gt;</code><code>&lt;osfEndLine&gt;</code>:</p>
<dd>ListEndDataExtend()</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfEndLine&gt;</code>:</p>
<dd>ListEndData()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfEndLine&gt;</code>:</p>
<dd>ListEndLine()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfPageLeft&gt;</code>:</p>
<dd>ListLeftPage()</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfPageUp&gt;</code>:</p>
<dd>ListLeftPage()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfPageUp&gt;</code>:</p>
<dd>ListPrevPage()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfPageRight&gt;</code>:</p>
<dd>ListRightPage()</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfPageDown&gt;</code>:</p>
<dd>ListRightPage()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfPageDown&gt;</code>:</p>
<dd>ListNextPage()</p>
<dt><code>s</code> <code>&lt;KeyDown&gt;</code><code>&lt;osfSelect&gt;</code><code>:</code></p>
<dd>ListKbdBeginExtend()</p>
<dt><code>:</code><code>&lt;KeyDown&gt;</code><code>&lt;osfSelect&gt;</code>:</p>
<dd>ListKbdBeginSelect()</p>
<dt><code>:s</code> <code>&lt;KeyUp&gt;</code><code>&lt;osfSelect&gt;</code>:</p>
<dd>ListKbdEndExtend()</p>
<dt><code>:</code><code>&lt;KeyUp&gt;</code><code>&lt;osfSelect&gt;</code>:</p>
<dd>ListKbdEndSelect()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfSelectAll&gt;</code>:</p>
<dd>ListKbdSelectAll()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfDeselectAll&gt;</code>:</p>
<dd>ListKbdDeSelectAll()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfActivate&gt;</code>:</p>
<dd>ListKbdActivate()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfAddMode&gt;</code>:</p>
<dd>ListAddMode()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfHelp&gt;</code>:</p>
<dd>PrimitiveHelp()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfCancel&gt;</code>:</p>
<dd>ListKbdCancel()</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfLeft&gt;</code>:</p>
<dd>ListLeftPage()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfLeft&gt;</code>:</p>
<dd>ListLeftChar()</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfRight&gt;</code>:</p>
<dd>ListRightPage()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfRight&gt;</code>:</p>
<dd>ListRightChar()</p>
<dt><code>:s</code> <code>&lt;Key&gt;</code><code>&lt;osfUp&gt;</code>:</p>
<dd>ListExtendPrevItem()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfUp&gt;</code>:</p>
<dd>ListPrevItem()</p>
<dt><code>:s</code> <code>&lt;Key&gt;</code><code>&lt;osfDown&gt;</code>:</p>
<dd>ListExtendNextItem()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfDown&gt;</code>:</p>
<dd>ListNextItem()</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfInsert&gt;</code>:</p>
<dd>ListCopyToClipboard()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfCopy&gt;</code>:</p>
<dd>ListCopyToClipboard()</p>
<dt><code>&asymp;s c &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>slash</code>:</p>
<dd>ListKbdSelectAll()</p>
<dt><code>&asymp;s c &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>backslash</code>:</p>
<dd>ListKbdDeSelectAll()</p>
<dt><code>s &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>Tab</code>:</p>
<dd>PrimitivePrevTabGroup()</p>
<dt><code>&asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>Tab</code>:</p>
<dd>PrimitiveNextTabGroup()</p>
<dt><code>&asymp;s &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>Return</code>:</p>
<dd>ListKbdActivate()</p>
<dt><code>&asymp;s &asymp;m &asymp;a</code> <code>&lt;KeyDown&gt;</code><code>space</code>:</p>
<dd>ListKbdBeginSelect()</p>
<dt><code>&asymp;s &asymp;m &asymp;a</code> <code>&lt;KeyUp&gt;</code><code>space</code>:</p>
<dd>ListKbdEndSelect()</p>
<dt><code>s &asymp;m &asymp;a</code> <code>&lt;KeyDown&gt;</code><code>space</code>:</p>
<dd>ListKbdBeginExtend()</p>
<dt><code>s &asymp;m &asymp;a</code> <code>&lt;KeyUp&gt;</code><code>space</code>:</p>
<dd>ListKbdEndExtend()</p>
<dt><code>&lt;Key&gt;</code>:</p>
<dd>ListQuickNavigate()</dl>
<p> The List button event translations are modified when Display&#8217;s <code>XmNenableBtn1Transfer</code> resource does not have a value of <code>XmOFF</code> (in other words, it is either <code>XmBUTTON2_TRANSFER</code> or <code>XmBUTTON2_ADJUST</code>). This option allows the actions for selection and transfer to be integrated on <code>&lt;Btn1&gt;</code>, and the actions for extending the selection can be bound to <code>&lt;Btn2&gt;</code>. The actions for <code>&lt;Btn1&gt;</code> that are defined above still apply when the <code>&lt;Btn1&gt;</code> event occurs over text that is not selected. The following actions apply when the <code>&lt;Btn1&gt;</code> event occurs over text that is selected:</p>
<dl COMPACT>
<dt><code>&lt;Btn1Motion&gt;</code><code>:</code></p>
<dd>ListProcessBtn1(<code>ListButtonMotion</code>)</p>
<dt><code>s &asymp;m &asymp;a</code> <code>&lt;Btn1Down&gt;</code></p>
<dd>ListProcessBtn1(<code>ListBeginExtend</code>)</p>
<dt><code>s &asymp;m &asymp;a</code> <code>&lt;Btn1Up&gt;</code></p>
<dd>ListProcessBtn1(<code>ListEndExtend</code>)</p>
<dt><code>c &asymp;s &asymp;m &asymp;a</code> <code>&lt;Btn1Down&gt;</code></p>
<dd>ListProcessBtn1(<code>ListBeginToggle</code>)</p>
<dt><code>c &asymp;s &asymp;m &asymp;a</code> <code>&lt;Btn1Up&gt;</code></p>
<dd>ListProcessBtn1(<code>ListEndToggle</code>)</p>
<dt><code>&asymp;s &asymp;c &asymp;m &asymp;a</code> <code>&lt;Btn1Down&gt;</code></p>
<dd>ListProcessBtn1(<code>ListBeginSelect</code>)</p>
<dt><code>&asymp;s &asymp;c &asymp;m &asymp;a</code> <code>&lt;Btn1Up&gt;</code></p>
<dd>ListProcessBtn1(<code>ListEndSelect</code>)</dl>
<p> When Display&#8217;s <code>XmNenableBtn1Transfer</code> resource has a value of <code>XmBUTTON2_ADJUST</code>, the following actions apply:</p>
<dl COMPACT>
<dt><code>&lt;Btn2Down&gt;</code><code>:</code></p>
<dd>ListProcessBtn2(<code>ListBeginExtend</code>)</p>
<dt><code>&lt;Btn2Motion&gt;</code><code>:</code></p>
<dd>ListProcessBtn2(<code>ListButtonMotion</code>)</p>
<dt><code>&lt;Btn2Up&gt;</code><code>:</code></p>
<dd>ListProcessBtn2(<code>ListEndExtend</code>)</dl>
<h3>Action Routines</h3>
<p>The <code>XmList</code> action routines are described in the following list. The current selection is always shown with inverted colors.</p>
<dl COMPACT>
<dt>ListAddMode():</p>
<dd>Toggles the state of Add Mode for keyboard selection.</p>
<dt>ListBeginData():</p>
<dd>Moves the location cursor to the first item in the list. In Normal Mode, this also deselects any current selection, selects the first item in the list, and calls the appropriate selection callbacks (<code>XmNbrowseSelectionCallback</code> when <code>XmNselectionPolicy</code> is set to <code>XmBROWSE_SELECT</code>, <code>XmNextendedSelectionCallback</code> when <code>XmNselectionPolicy</code> is set to <code>XmEXTENDED_SELECT</code>).</p>
<dt>ListBeginDataExtend():</p>
<dd>If <code>XmNselectionPolicy</code> is set to <code>XmMULTIPLE_SELECT</code> or <code>XmEXTENDED_SELECT</code>, this action moves the location cursor to the first item in the list.</p>
<dd>If <code>XmNselectionPolicy</code> is set to <code>XmEXTENDED_SELECT</code>, this action does the following: If an extended selection has been made from the current anchor point, restores the selection state of the items in that range to their state before the extended selection was done; changes the selection state of the first item and all items between it and the current anchor point to the state of the item at the current anchor point; calls the <code>XmNextendedSelectionCallback</code> callbacks.</p>
<dt>ListBeginExtend():</p>
<dd>If <code>XmNselectionPolicy</code> is set to <code>XmEXTENDED_SELECT</code>, this action does the following: If an extended selection has been made from the current anchor point, restores the selection state of the items in that range to their state before the extended selection was done, and changes the selection state of the item under the pointer and all items between it and the current anchor point to the state of the item at the current anchor point. If <code>XmNautomaticSelection</code> is set to True, this action calls the <code>XmNextendedSelectionCallback</code> callbacks. The <code>auto_selection_type</code> component of the callback structure will be set to <code>XmAUTO_BEGIN</code>.</p>
<dt>ListBeginLine():</p>
<dd>Moves the horizontal scroll region to the beginning of the line.</p>
<dt>ListBeginSelect():</p>
<dd>If <code>XmNselectionPolicy</code> is set to <code>XmSINGLE_SELECT</code>, deselects any current selection and toggles the selection state of the item under the pointer.</p>
<dd>If <code>XmNselectionPolicy</code> is set to <code>XmBROWSE_SELECT</code>, deselects any current selection and selects the item under the pointer. If <code>XmNautomaticSelection</code> is set to True, calls the <code>XmNbrowseSelectionCallback</code> callbacks. The <code>auto_selection_type</code> component of the callback structure will be set to <code>XmAUTO_BEGIN</code>.</p>
<dd>If <code>XmNselectionPolicy</code> is set to <code>XmMULTIPLE_SELECT</code>, toggles the selection state of the item under the pointer. Any previous selections remain.</p>
<dd>If <code>XmNselectionPolicy</code> is set to <code>XmEXTENDED_SELECT</code>, this action deselects any current selection, selects the item under the pointer, and sets the current anchor at that item. If <code>XmNautomaticSelection</code> is set to True, this action calls the <code>XmNextendedSelectionCallback</code> callbacks. The <code>auto_selection_type</code> component of the callback structure will be set to <code>XmAUTO_BEGIN</code>.</p>
<dt>ListBeginToggle():</p>
<dd>If <code>XmNselectionPolicy</code> is set to <code>XmEXTENDED_SELECT</code>, this action moves the current anchor to the item under the pointer without changing the current selection. If the item is unselected, this action selects it; if the item is selected, this action unselects it. If <code>XmNautomaticSelection</code> is set to True, this action calls the <code>XmNextendedSelectionCallback</code> callbacks.</p>
<dd>Otherwise, the list takes keyboard focus. No other action occurs. The <code>auto_selection_type</code> component of the callback structure will be set to <code>XmAUTO_BEGIN</code>.</p>
<dt>ListButtonMotion():</p>
<dd>If <code>XmNselectionPolicy</code> is set to <code>XmBROWSE_SELECT</code>, this action deselects any current selection and selects the item under the pointer. If <code>XmNautomaticSelection</code> is set to True and the pointer has entered a new list item, this action calls the <code>XmNbrowseSelectionCallback</code> callbacks.</p>
<dd>If <code>XmNselectionPolicy</code> is set to <code>XmEXTENDED_SELECT</code>, this action does the following: If an extended selection is being made and an extended selection has previously been made from the current anchor point, restores the selection state of the items in that range to their state before the previous extended selection was done and changes the selection state of the item under the pointer and all items between it and the current anchor point to the state of the item at the current anchor point. If <code>XmNautomaticSelection</code> is set to True and the pointer has entered a new list item, calls the <code>XmNextendedSelectionCallback</code> callbacks.</p>
<dd>If the pointer leaves a scrolled list, this action scrolls the list in the direction of the pointer motion. The <code>auto_selection_type</code> component of the callback structure will be set to <code>XmAUTO_MOTION</code>.</p>
<dt>ListCopyToClipboard()</p>
<dd>Copies the content of the selected items to the clipboard as a single compound string with each item separated by a newline. This action calls the <code>XmNconvertCallback</code> procedures, possibly multiple times, for the <code>CLIPBOARD</code> selection.</p>
<dt>ListEndData():</p>
<dd>Moves the location cursor to the last item in the list. In Normal Mode, this also deselects any current selection, selects the last item in the list, and calls the appropriate selection callbacks (<code>XmNbrowseSelectionCallback</code> when <code>XmNselectionPolicy</code> is set to <code>XmBROWSE_SELECT</code>, <code>XmNextendedSelectionCallback</code> when <code>XmNselectionPolicy</code> is set to <code>XmEXTENDED_SELECT</code>).</p>
<dt>ListEndDataExtend():</p>
<dd>If <code>XmNselectionPolicy</code> is set to <code>XmMULTIPLE_SELECT</code> or <code>XmEXTENDED_SELECT</code>, this action moves the location cursor to the last item in the list.</p>
<dd>If <code>XmNselectionPolicy</code> is set to <code>XmEXTENDED_SELECT</code>, this action does the following: If an extended selection has been made from the current anchor point, restores the selection state of the items in that range to their state before the extended selection was done; changes the selection state of the last item and all items between it and the current anchor point to the state of the item at the current anchor point; calls the <code>XmNextendedSelectionCallback</code> callbacks.</p>
<dt>ListEndExtend():</p>
<dd>If <code>XmNselectionPolicy</code> is set to <code>XmEXTENDED_SELECT</code>, this action moves the location cursor to the last item selected or deselected and calls the <code>XmNextendedSelectionCallback</code> callbacks.</p>
<dd>If <code>XmNautomaticSelection</code> is set to True, then the <code>auto_selection_type</code> field of the callback will be valid. If <code>XmNselectionPolicy</code> is set to <code>XmBROWSE_SELECT</code> and the currently selected item position matches the position of the item that was selected before the browse selection began, or if <code>XmNselectionPolicy</code> is set to <code>XmEXTENDED_SELECT</code> and the set of currently selected item positions matches the set of item positions selected before the extended selection began, the callback will be called with <code>auto_selection_type</code> set to <code>XmAUTO_NO_CHANGE</code>. Otherwise, it will be set to <code>XmAUTO_CHANGE</code>.</p>
<dt>ListEndLine():</p>
<dd>Moves the horizontal scroll region to the end of the line.</p>
<dt>ListEndSelect():</p>
<dd>This action moves the location cursor to the last item selected or deselected and calls the appropriate selection callbacks (<code>XmNsingleSelectionCallback</code> when <code>XmNselectionPolicy</code> is set to <code>XmSINGLE_SELECT</code>, <code>XmNbrowseSelectionCallback</code> when <code>XmNselectionPolicy</code> is set to <code>XmBROWSE_SELECT</code>, <code>XmNmultipleSelectionCallback</code> when <code>XmNselectionPolicy</code> is set to <code>XmMULTIPLE_SELECT</code>, <code>XmNextendedSelectionCallback</code> when <code>XmNselectionPolicy</code> is set to <code>XmEXTENDED_SELECT</code>).</p>
<dd>If <code>XmNautomaticSelection</code> is set to True, then the <code>auto_selection_type</code> field of the callback will be valid. If <code>XmNselectionPolicy</code> is set to <code>XmBROWSE_SELECT</code> and the currently selected item position matches the position of the item that was selected before the brose selection began, or if <code>XmNselectionPolicy</code> is set to <code>XmEXTENDED_SELECT</code> and the set of currently selected item positions matches the set of item positions selected before the extended selection began, the callback will be called with <code>auto_selection_type</code> set to <code>XmAUTO_NO_CHANGE</code>. Otherwise, it will be set to <code>XmAUTO_CHANGE</code>.</p>
<dt>ListEndToggle():</p>
<dd>If <code>XmNselectionPolicy</code> is set to <code>XmEXTENDED_SELECT</code>, moves the location cursor to the last item selected or deselected and calls the <code>XmNextendedSelectionCallback</code> callbacks.</p>
<dd>If <code>XmNautomaticSelection</code> is set to True, then the <code>auto_selection_type</code> field of the callback will be valid. If <code>XmNselectionPolicy</code> is set to <code>XmBROWSE_SELECT</code> and the currently selected item position matches the position of the item that was selected before the browse selection began, or if <code>XmNselectionPolicy</code> is set to <code>XmEXTENDED_SELECT</code> and the set of currently selected item positions matches the set of item positions selected before the extended selection began, the callback will be called with <code>auto_selection_type</code> set to <code>XmAUTO_NO_CHANGE</code>. Otherwise, it will be set to <code>XmAUTO_CHANGE</code>.</p>
<dt>ListExtendNextItem():</p>
<dd>If <code>XmNselectionPolicy</code> is set to <code>XmEXTENDED_SELECT</code>, this action does the following: If an extended selection has been made from the current anchor point, restores the selection state of the items in that range to their state before the extended selection was done; moves the location cursor to the next item and changes the selection state of the item and all items between it and the current anchor point to the state of the item at the current anchor point; calls the <code>XmNextendedSelectionCallback</code> callbacks.</p>
<dt>ListExtendPrevItem():</p>
<dd>If <code>XmNselectionPolicy</code> is set to <code>XmEXTENDED_SELECT</code>, this action does the following: If an extended selection has been made from the current anchor point, restores the selection state of the items in that range to their state before the extended selection was done; moves the location cursor to the previous item and changes the selection state of the item and all items between it and the current anchor point to the state of the item at the current anchor point; calls the <code>XmNextendedSelectionCallback</code> callbacks.</p>
<dt>ListScrollCursorVertically(<i>percentage</i><code>)</code>:</p>
<dd>Scrolls the line containing the insertion cursor vertically to an intermediate position in the visible window based on an input percentage. A value of 0 (zero) indicates the top of the window; a value of 100, the bottom of the window. If this action is called with no argument, the line containing the insertion cursor is scrolled vertically to a new position designated by the <i>y</i> event passed to the routine.</p>
<dt>ListKbdActivate():</p>
<dd>Calls the callbacks for <code>XmNdefaultActionCallback</code>. If the List&#8217;s parent is a manager, this action passes the event to the parent.</p>
<dt>ListKbdBeginExtend():</p>
<dd>If <code>XmNselectionPolicy</code> is set to <code>XmEXTENDED_SELECT</code>, does the following: If an extended selection has been made from the current anchor point, restores the selection state of the items in that range to their state before the extended selection was done; changes the selection state of the item at the location cursor and all items between it and the current anchor point to the state of the item at the current anchor point. If <code>XmNautomaticSelection</code> is set to True, this action calls the <code>XmNextendedSelectionCallback</code> callbacks. The <code>auto_selection_type</code> component of the callback structure will be set to <code>XmAUTO_BEGIN</code>&quot;.</p>
<dt>ListKbdBeginSelect():</p>
<dd>If the <code>XmNselectionPolicy</code> is set to <code>XmSINGLE_SELECT</code>, deselects any current selection and toggles the state of the item at the location cursor. The <code>auto_selection_type</code> component of the callback structure will be set to <code>XmAUTO_BEGIN</code>&quot;.</p>
<dd>If the <code>XmNselectionPolicy</code> is set to <code>XmBROWSE_SELECT</code>, deselects any current selection and selects the item at the location cursor. If <code>XmNautomaticSelection</code> is set to True, calls the <code>XmNbrowseSelectionCallback</code> callbacks.</p>
<dd>If the <code>XmNselectionPolicy</code> is set to <code>XmMULTIPLE_SELECT</code>, toggles the selection state of the item at the location cursor. Any previous selections remain.</p>
<dd>If the <code>XmNselectionPolicy</code> is set to <code>XmEXTENDED_SELECT</code>, moves the current anchor to the item at the location cursor. In Normal Mode, this action deselects any current selection and selects the item at the location cursor. In Add Mode, this action toggles the selection state of the item at the location cursor and leaves the current selection unchanged. If <code>XmNautomaticSelection</code> is set to True, this action calls the <code>XmNextendedSelectionCallback</code> callbacks. The <code>auto_selection_type</code> component of the callback structure will be set to <code>XmAUTO_BEGIN</code>&quot;.</p>
<dt>ListKbdCancel():</p>
<dd>If <code>XmNselectionPolicy</code> is set to <code>XmEXTENDED_SELECT</code> and an extended selection is being made from the current anchor point, this action cancels the new selection and restores the selection state of the items in that range to their state before the extended selection was done. If <code>XmNautomaticSelection</code> is set to True, this action calls the <code>XmNextendedSelectionCallback</code> callbacks; otherwise, if the parent is a manager, it passes the event to the parent. The <code>auto_selection_type</code> component of the callback structure will be set to <code>XmAUTO_CANCEL</code>&quot;.</p>
<dt>ListKbdDeSelectAll():</p>
<dd>If the <code>XmNselectionPolicy</code> is set to <code>XmSINGLE_SELECT</code>, <code>XmMULTIPLE_SELECT</code>, or <code>XmEXTENDED_SELECT</code> in Add Mode, this action deselects all items in the list. If the <code>XmNselectionPolicy</code> is set to <code>XmEXTENDED_SELECT</code> in Normal Mode, this action deselects all items in the list (except the item at the location cursor if the shell&#8217;s <code>XmNkeyboardFocusPolicy</code> is <code>XmEXPLICIT</code>). This action also calls the appropriate selection callbacks (<code>XmNsingleSelectionCallback</code> when <code>XmNselectionPolicy</code> is set to <code>XmSINGLE_SELECT</code>, <code>XmNmultipleSelectionCallback</code> when <code>XmNselectionPolicy</code> is set to <code>XmMULTIPLE_SELECT</code>, <code>XmNextendedSelectionCallback</code> when <code>XmNselectionPolicy</code> is set to <code>XmEXTENDED_SELECT</code>).</p>
<dt>ListKbdEndExtend():</p>
<dd>If <code>XmNselectionPolicy</code> is set to <code>XmEXTENDED_SELECT</code>, this action calls the <code>XmNextendedSelectionCallback</code> callbacks.</p>
<dd>If <code>XmNautomaticSelection</code> is set to True, then the <code>auto_selection_type</code> field of the callback will be valid. If <code>XmNselectionPolicy</code> is set to <code>XmBROWSE_SELECT</code> and the currently selected item position matches the position of the item that was selected before the browse selection began, or if <code>XmNselectionPolicy</code> is set to <code>XmEXTENDED_SELECT</code> and the set of currently selected item positions matches the set of item positions selected before the extended selection began, the callback will be called with <code>auto_selection_type</code> set to <code>XmAUTO_NO_CHANGE</code>. Otherwise, it will be set to <code>XmAUTO_CHANGE</code>.</p>
<dt>ListKbdEndSelect():</p>
<dd>Calls the appropriate selection callbacks (<code>XmNsingleSelectionCallback</code> when <code>XmNselectionPolicy</code> is set to <code>XmSINGLE_SELECT</code>, <code>XmNbrowseSelectionCallback</code> when <code>XmNselectionPolicy</code> is set to <code>XmBROWSE_SELECT</code>, <code>XmNmultipleSelectionCallback</code> when <code>XmNselectionPolicy</code> is set to <code>XmMULTIPLE_SELECT</code>, <code>XmNextendedSelectionCallback</code> when <code>XmNselectionPolicy</code> is set to <code>XmEXTENDED_SELECT</code>).</p>
<dd>If <code>XmNautomaticSelection</code> is set to True, then the <code>auto_selection_type</code> field of the callback will be valid. If <code>XmNselectionPolicy</code> is set to <code>XmBROWSE_SELECT</code> and the currently selected item position matches the position of the item that was selected before the browse selection began, or if <code>XmNselectionPolicy</code> is set to <code>XmEXTENDED_SELECT</code> and the set of currently selected item positions matches the set of item positions selected before the extended selection began, the callback will be called with <code>auto_selection_type</code> set to <code>XmAUTO_NO_CHANGE</code>. Otherwise, it will be set to <code>XmAUTO_CHANGE</code>.</p>
<dt>ListKbdSelectAll():</p>
<dd>If <code>XmNselectionPolicy</code> is set to <code>XmSINGLE_SELECT</code> or <code>XmBROWSE_SELECT</code>, this action selects the item at the location cursor. If <code>XmNselectionPolicy</code> is set to <code>XmEXTENDED_SELECT</code> or <code>XmMULTIPLE_SELECT</code>, it selects all items in the list. This action also calls the appropriate selection callbacks (<code>XmNsingleSelectionCallback</code> when <code>XmNselectionPolicy</code> is set to <code>XmSINGLE_SELECT</code>, <code>XmNbrowseSelectionCallback</code> when <code>XmNselectionPolicy</code> is set to <code>XmBROWSE_SELECT</code>, <code>XmNmultipleSelectionCallback</code> when <code>XmNselectionPolicy</code> is set to <code>XmMULTIPLE_SELECT</code>, <code>XmNextendedSelectionCallback</code> when <code>XmNselectionPolicy</code> is set to <code>XmEXTENDED_SELECT</code>).</p>
<dt>ListLeftChar():</p>
<dd>Scrolls the list one character to the left.</p>
<dt>ListLeftPage():</p>
<dd>Scrolls the list one page to the left.</p>
<dt>ListNextItem():</p>
<dd>Moves the location cursor to the next item in the list.</p>
<dd>If the <code>XmNselectionPolicy</code> is set to <code>XmBROWSE_SELECT</code>, this action also selects the next item, deselects any current selection, and calls the <code>XmNbrowseSelectionCallback</code> callbacks.</p>
<dd>If the <code>XmNselectionPolicy</code> is set to <code>XmEXTENDED_SELECT</code>, this action in Normal Mode also selects the next item, deselects any current selection, moves the current anchor to the next item, and calls the <code>XmNextendedSelectionCallback</code> callbacks. In Add Mode, this action does not affect the selection or the anchor.</p>
<dt>ListNextPage():</p>
<dd>Scrolls the list to the next page, moving the location cursor to a new item.</p>
<dd>If the <code>XmNselectionPolicy</code> is set to <code>XmBROWSE_SELECT</code>, this action also selects the new item, deselects any current selection, and calls the <code>XmNbrowseSelectionCallback</code> callbacks.</p>
<dd>If the <code>XmNselectionPolicy</code> is set to <code>XmEXTENDED_SELECT</code>, this action in Normal Mode also selects the new item, deselects any current selection, moves the current anchor to the new item, and calls the <code>XmNextendedSelectionCallback</code> callbacks. In Add Mode, this action does not affect the selection or the anchor.</p>
<dt>ListPrevItem():</p>
<dd>Moves the location cursor to the previous item in the list.</p>
<dd>If the <code>XmNselectionPolicy</code> is set to <code>XmBROWSE_SELECT</code>, this action also selects the previous item, deselects any current selection, and calls the <code>XmNbrowseSelectionCallback</code> callbacks.</p>
<dd>If the <code>XmNselectionPolicy</code> is set to <code>XmEXTENDED_SELECT</code>, this action in Normal Mode also selects the previous item, deselects any current selection, moves the current anchor to the previous item, and calls the <code>XmNextendedSelectionCallback</code> callbacks. In Add Mode, this action does not affect the selection or the anchor.</p>
<dt>ListPrevPage():</p>
<dd>Scrolls the list to the previous page, moving the location cursor to a new item.</p>
<dd>If the <code>XmNselectionPolicy</code> is set to <code>XmBROWSE_SELECT</code>, this action also selects the new item, deselects any current selection, and calls the <code>XmNbrowseSelectionCallback</code> callbacks.</p>
<dd>If the <code>XmNselectionPolicy</code> is set to <code>XmEXTENDED_SELECT</code>, this action in Normal Mode also selects the new item, deselects any current selection, moves the current anchor to the new item, and calls the <code>XmNextendedSelectionCallback</code> callbacks. In Add Mode this action does not affect the selection or the anchor.</p>
<dt>ListProcessBtn1(<i>string</i>)</p>
<dd>When Display&#8217;s <code>XmNenableBtn1Transfer</code> resource is not <code>XmOFF</code>, the actions for selection and transfer are integrated on <code>&lt;Btn1&gt;</code>. When the button is not performing a transfer or drag, the action that is performed depends on the value of <i>string</i>, which can be one of the following actions:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd><code>ListButtonMotion</code></p>
<dt> &bull;</p>
<dd><code>ListBeginExtend</code></p>
<dt> &bull;</p>
<dd><code>ListEndExtend</code></p>
<dt> &bull;</p>
<dd><code>ListBeginToggle</code></p>
<dt> &bull;</p>
<dd><code>ListEndToggle</code></p>
<dt> &bull;</p>
<dd><code>ListBeginSelect</code></p>
<dt> &bull;</p>
<dd><code>ListEndSelect</code></dl>
</dl>
<dt><code>ListProcessBtn2</code></p>
<dd>When Display&#8217;s <code>XmNenableBtn1Transfer</code> resource has a value of <code>XmBUTTON2_TRANSFER</code>, the actions for extending selection are bound on <code>&lt;Btn2&gt;</code>, and a drag starts immediately. When Display&#8217;s <code>XmNenableBtn1Transfer</code> resource has a value of <code>XmBUTTON2_ADJUST</code>, the action that is performed depends on the value of <i>string</i>, which can be one of the following actions:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd><code>ListBeginExtend</code></p>
<dt> &bull;</p>
<dd><code>ListButtonMotion</code></p>
<dt> &bull;</p>
<dd><code>ListEndExtend</code></dl>
</dl>
<dt>ListProcessDrag():</p>
<dd>Drags the content of one or more selected list items. Each item is separated by a newline. If <code>BTransfer</code> is pressed on an unselected item, it drags only that item, excluding any other selected items. This action sets the <code>XmNconvertProc</code> of the DragContext to a function that calls the <code>XmNconvertCallback</code> procedures, possibly multiple times, for the <code>_MOTIF_DROP</code> selection.</p>
<dt><code>ListQuickNavigate</code></p>
<dd>Navigates to an item. When List&#8217;s <code>XmNmatchBehavior</code> resource is <code>XmQUICK_NAVIGATE</code>, this action uses 1-character navigation to navigate. Refer to the <code>XmNmatchBehavior</code> resource for a description of how this navigation works.</p>
<dt>ListRightChar():</p>
<dd>Scrolls the list one character to the right.</p>
<dt>ListRightPage():</p>
<dd>Scrolls the list one page to the right.</p>
<dt>PrimitiveHelp():</p>
<dd>Calls the callbacks for <code>XmNhelpCallback</code> if any exist. If there are no help callbacks for this widget, this action calls the help callbacks for the nearest ancestor that has them.</p>
<dt>PrimitiveNextTabGroup():</p>
<dd>Moves the focus to the first item contained within the next tab group. If the current tab group is the last entry in the tab group list, it wraps to the beginning of the tab group list.</p>
<dt>PrimitivePrevTabGroup():</p>
<dd>Moves the focus to the first item contained within the previous tab group. If the beginning of the tab group list is reached, it wraps to the end of the tab group list.</dl>
<h3>Additional Behavior</h3>
<p>The List widget has the following additional behavior:</p>
<dl COMPACT>
<dt><code>&lt;Double Click&gt;</code></p>
<dd>If a button click is followed by another button click within the time span specified by the display&#8217;s multiclick time, the List interprets that as a double click and calls the callbacks for <code>XmNdefaultActionCallback</code>. The item&#8217;s colors invert to indicate that it is selected. The <code>XmNdoubleClickInterval</code> resource can be used to specify a time span that overrides the display&#8217;s multi-click time.</p>
<dt><code>&lt;FocusIn&gt;</code>:</p>
<dd>If the focus policy is Explicit, this action sets the focus and draw the location cursor.</p>
<dt><code>&lt;FocusOut&gt;</code>:</p>
<dd>If the focus policy is Explicit, this action removes the focus and erase the location cursor.</dl>
<h3>Virtual Bindings</h3>
<p>The bindings for virtual keys are vendor specific. For information about bindings for virtual buttons and keys, see <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-core/">Core</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatelist/">XmCreateList</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatescrolledlist/">XmCreateScrolledList</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistcreate/">XmFontListCreate</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistappendentry/">XmFontListAppendEntry</a></code>(3), <code><a href="/docs/linux/man/3-xmlistadditem/">XmListAddItem</a></code>(3), <code><a href="/docs/linux/man/3-xmlistadditems/">XmListAddItems</a></code>(3), <code><a href="/docs/linux/man/3-xmlistadditemunselected/">XmListAddItemUnselected</a></code>(3), <code><a href="/docs/linux/man/3-xmlistadditemsunselected/">XmListAddItemsUnselected</a></code>(3), <code><a href="/docs/linux/man/3-xmlistdeleteallitems/">XmListDeleteAllItems</a></code>(3), <code><a href="/docs/linux/man/3-xmlistdeleteitem/">XmListDeleteItem</a></code>(3), <code><a href="/docs/linux/man/3-xmlistdeleteitems/">XmListDeleteItems</a></code>(3), <code><a href="/docs/linux/man/3-xmlistdeleteitemspos/">XmListDeleteItemsPos</a></code>(3), <code><a href="/docs/linux/man/3-xmlistdeletepos/">XmListDeletePos</a></code>(3), <code><a href="/docs/linux/man/3-xmlistdeletepositions/">XmListDeletePositions</a></code>(3), <code><a href="/docs/linux/man/3-xmlistdeselectallitems/">XmListDeselectAllItems</a></code>(3), <code><a href="/docs/linux/man/3-xmlistdeselectitem/">XmListDeselectItem</a></code>(3), <code><a href="/docs/linux/man/3-xmlistdeselectpos/">XmListDeselectPos</a></code>(3), <code>XmListGetKbdItemPos</code> <code><a href="/docs/linux/man/3-xmlistgetmatchpos/">XmListGetMatchPos</a></code>(3), <code><a href="/docs/linux/man/3-xmlistgetselectedpos/">XmListGetSelectedPos</a></code>(3), <code><a href="/docs/linux/man/3-xmlistitemexists/">XmListItemExists</a></code>(3), <code><a href="/docs/linux/man/3-xmlistitempos/">XmListItemPos</a></code>(3), <code><a href="/docs/linux/man/3-xmlistpostobounds/">XmListPosToBounds</a></code>(3), <code><a href="/docs/linux/man/3-xmlistreplaceitems/">XmListReplaceItems</a></code>(3), <code><a href="/docs/linux/man/3-xmlistreplaceitemspos/">XmListReplaceItemsPos</a></code>(3), <code><a href="/docs/linux/man/3-xmlistreplaceitemspos/">XmListReplaceItemsPos</a></code>(3), <code><a href="/docs/linux/man/3-xmlistreplaceitemsposunselected/">XmListReplaceItemsPosUnselected</a></code>(3), <code><a href="/docs/linux/man/3-xmlistreplaceitemsunselected/">XmListReplaceItemsUnselected</a></code>(3), <code><a href="/docs/linux/man/3-xmlistselectitem/">XmListSelectItem</a></code>(3), <code><a href="/docs/linux/man/3-xmlistselectpos/">XmListSelectPos</a></code>(3), <code><a href="/docs/linux/man/3-xmlistsetaddmode/">XmListSetAddMode</a></code>(3), <code><a href="/docs/linux/man/3-xmlistsetbottomitem/">XmListSetBottomItem</a></code>(3), <code><a href="/docs/linux/man/3-xmlistsetbottompos/">XmListSetBottomPos</a></code>(3), <code><a href="/docs/linux/man/3-xmlistsethorizpos/">XmListSetHorizPos</a></code>(3), <code><a href="/docs/linux/man/3-xmlistsetitem/">XmListSetItem</a></code>(3), <code><a href="/docs/linux/man/3-xmlistsetkbditempos/">XmListSetKbdItemPos</a></code>(3), <code><a href="/docs/linux/man/3-xmlistsetpos/">XmListSetPos</a></code>(3), <code><a href="/docs/linux/man/3-xmlistupdateselectedlist/">XmListUpdateSelectedList</a></code>(3), <code><a href="/docs/linux/man/3-xmlistytopos/">XmListYToPos</a></code>(3), <code><a href="/docs/linux/man/3-xmprimitive/">XmPrimitive</a></code>(3) <code><a href="/docs/linux/man/3-xmstringcreate/">XmStringCreate</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatelist/">XmVaCreateList</a></code>(3), and <code><a href="/docs/linux/man/3-xmvacreatemanagedlist/">XmVaCreateManagedList</a></code>(3).</p>
