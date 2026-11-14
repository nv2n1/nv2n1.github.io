---
title: "xmselectionbox(3)"
name: "xmselectionbox"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmselectionbox/"
description: "XmSelectionBox — The SelectionBox widget class"
---

<p><code>XmSelectionBox</code> &#8212; The SelectionBox widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/SelectioB.h&gt;</pre>
<h2>Description</h2>
<p>SelectionBox is a general dialog widget that allows the user to select one item from a list. By default, a SelectionBox includes the following:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd>A scrolling list of alternatives</p>
<dt> &bull;</p>
<dd>An editable text field for the selected alternative</p>
<dt> &bull;</p>
<dd>Labels for the list and text field</p>
<dt> &bull;</p>
<dd>Three or four buttons</dl>
<p> The default button labels are <code>OK</code>, <code>Cancel</code>, and <code>Help</code>. By default an <code>Apply</code> button is also created; if the parent of the SelectionBox is a DialogShell, it is managed; otherwise it is unmanaged. Additional children may be added to the SelectionBox after creation. The first child is used as a work area. The value of <code>XmNchildPlacement</code> determines if the work area is placed above or below the Text area, or above or below the List area. Additional children are laid out in the following manner:</p>
<dl COMPACT>
<dt>Menubar</p>
<dd>The first menu bar child is placed at the top of the window. The <code>XmQTmenuSystem</code> trait is used to check that it is the first MenuBar child.</p>
<dt>Buttons</p>
<dd>All <code>XmPushButton</code> widgets or gadgets, and their subclasses are placed after the <code>OK</code> button in the order of their creation (this order is checked using the <code>XmQTactivatable</code> trait). The layout direction of the buttons depends on the <code>XmNlayoutDirection</code> resource.</dl>
<p> The layout of additional children that are not in the above categories is undefined. </p>
<p> The user can select an item in two ways: by scrolling through the list and selecting the desired item or by entering the item name directly into the text edit area. Selecting an item from the list causes that item name to appear in the selection text edit area. </p>
<p> The user may select a new item as many times as desired. The item is not actually selected until the user presses the <code>OK</code> PushButton. </p>
<p> The default value for the <code>XmBulletinBoard</code> resource <code>XmNcancelButton</code> is the Cancel button, unless <code>XmNdialogType</code> is <code>XmDIALOG_COMMAND</code>, when the default is NULL. The default value for the <code>XmBulletinBoard</code> <code>XmNdefaultButton</code> resource is the OK button, unless <code>XmNdialogType</code> is <code>XmDIALOG_COMMAND</code>, when the default is NULL. </p>
<p> For SelectionBox and its subclasses, the default value for <code>XmNinitialFocus</code> is the text edit area. </p>
<p> The user can specify resources in a resource file for the automatically created widgets and gadgets of SelectionBox. The following list identifies the names of these widgets (or gadgets) and the associated SelectionBox areas:</p>
<dl COMPACT>
<dt>List Items Label</p>
<dd><code>Items</code></p>
<dt>List Items</p>
<dd><code>ItemsList</code></p>
<dt>Selection Label</p>
<dd><code>Selection</code></p>
<dt>Selection Text</p>
<dd><code>Text</code> or <code>TextField</code></p>
<dt>Selection Separator</p>
<dd><code>Separator</code></dl>
<p> SelectionBox uses the <code>XmQTaccessTextual</code>, <code>XmQTactivatable</code>, and <code>XmQTmenuSystem</code> traits.</p>
<h3>Descendants</h3>
<p>SelectionBox automatically creates the descendants shown in the following table. An application can use <code>XtNameToWidget</code> to gain access to the named descendant. In addition, a user or an application can use the named descendant when specifying resource values. </p>
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
<td><code>Apply</code></td>
<td><code>XmPushButtonGadget</code></td>
<td>Apply button
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>Cancel</code></td>
<td><code>XmPushButtonGadget</code></td>
<td>Cancel button
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>Help</code></td>
<td><code>XmPushButtonGadget</code></td>
<td>Help button
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>Items</code></td>
<td><code>XmLabelGadget</code></td>
<td>title above the list of items
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>ItemsList</code></td>
<td><code>XmList</code></td>
<td> list of items from which the user will select
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>ItemsListSW</code></td>
<td><code>XmScrolledWindow</code></td>
<td>ScrolledWindow parent of <code>ItemsList</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>OK</code></td>
<td><code>XmPushButtonGadget</code></td>
<td>OK button
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>Selection</code></td>
<td><code>XmLabelGadget</code></td>
<td>title above the selection box
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>Separator</code></td>
<td><code>XmSeparatorGadget</code></td>
<td> dividing line between selection box and buttons
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>Text</code></td>
<td><code>XmTextField</code></td>
<td> selection box containing text of selected item
</td>
</tr>
<tr VALIGN=top>
<td>
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
<p>SelectionBox inherits behavior, resources, and traits from <code>Core</code>, <code>Composite</code>, <code>Constraint</code>, <code>XmManager</code>, and <code>XmBulletinBoard</code>. </p>
<p> The class pointer is <code>xmSelectionBoxWidgetClass</code>. </p>
<p> The class name is <code>XmSelectionBox</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmSelectionBox Resource Set</code>
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
<td>XmNapplyCallback</td>
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
<td>XmNapplyLabelString</td>
<td>XmCApplyLabelString</td>
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
<td>XmNcancelCallback</td>
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
<td>XmNcancelLabelString</td>
<td>XmCCancelLabelString</td>
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
<td>XmNchildPlacement</td>
<td>XmCChildPlacement</td>
<td>unsigned char</td>
<td>XmPLACE_ABOVE_SELECTION</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNdialogType</td>
<td>XmCDialogType</td>
<td>unsigned char</td>
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
<td>XmNhelpLabelString</td>
<td>XmCHelpLabelString</td>
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
<td>XmNlistItemCount</td>
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
<td>XmNlistItems</td>
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
<td>XmNlistLabelString</td>
<td>XmCListLabelString</td>
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
<td>XmNlistVisibleItemCount</td>
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
<tr VALIGN=top>
<td>XmNminimizeButtons</td>
<td>XmCMinimizeButtons</td>
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
<td>XmNmustMatch</td>
<td>XmCMustMatch</td>
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
<td>XmNnoMatchCallback</td>
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
<td>XmNokCallback</td>
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
<td>XmNokLabelString</td>
<td>XmCOkLabelString</td>
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
<td>XmNselectionLabelString</td>
<td>XmCSelectionLabelString</td>
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
<td>XmNtextAccelerators</td>
<td>XmCTextAccelerators</td>
<td>XtAccelerators</td>
<td>default</td>
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
<td>XmNtextColumns</td>
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
<td>XmNtextString</td>
<td>XmCTextString</td>
<td>XmString</td>
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
</table>
</table>
<dl COMPACT>
<dt><code>XmNapplyCallback</code></p>
<dd>Specifies the list of callbacks called when the user activates the <code>Apply</code> button. The callback reason is <code>XmCR_APPLY</code>.</p>
<dt><code>XmNapplyLabelString</code></p>
<dd>Specifies the string label for the <code>Apply</code> button. The default for this resource depends on the locale. In the C locale the default is <code>Apply</code>.</p>
<dd>Now that some default localized label strings are provided through message catalogs for the children of composite widgets, the <code>labelString</code> resources cannot be set on the child through default resource files. Instead, the resource provided at the parent level must be used.</p>
<dt><code>XmNcancelCallback</code></p>
<dd>Specifies the list of callbacks called when the user activates the <code>Cancel</code> button. The callback reason is <code>XmCR_CANCEL</code>.</p>
<dt><code>XmNcancelLabelString</code></p>
<dd>Specifies the string label for the <code>Cancel</code> button. The default for this resource depends on the locale. In the C locale the default is <code>Cancel</code>.</p>
<dd>Now that some default localized label strings are provided through message catalogs for the children of composite widgets, the <code>labelString</code> resources cannot be set on the child through default resource files. Instead, the resource provided at the parent level must be used.</p>
<dt><code>XmNchildPlacement</code></p>
<dd>Specifies the placement of the work area child. The possible values are</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmPLACE_ABOVE_SELECTION</code></p>
<dd>Places the work area child above the Text area</p>
<dt><code>XmPLACE_BELOW_SELECTION</code></p>
<dd>Places the work area child below the Text area</p>
<dt><code>XmPLACE_TOP</code></p>
<dd>Places the work area child above the List area, and below a MenuBar, if one is present</dl>
</dl>
<dt><code>XmNdialogType</code></p>
<dd>Determines the set of SelectionBox children widgets that are created and managed at initialization. The possible values are</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmDIALOG_PROMPT</code></p>
<dd>All standard children except the list and list label are created, and all except the <code>Apply</code> button are managed</p>
<dt><code>XmDIALOG_COMMAND</code></p>
<dd>Only the list, the selection label, and the text field are created and managed</p>
<dt><code>XmDIALOG_SELECTION</code></p>
<dd>All standard children are created and managed</p>
<dt><code>XmDIALOG_FILE_SELECTION</code></p>
<dd>All standard children are created and managed</p>
<dt><code>XmDIALOG_WORK_AREA</code></p>
<dd>All standard children are created, and all except the <code>Apply</code> button are managed</dl>
</dl>
<dd>If the parent of the SelectionBox is a DialogShell, the default is <code>XmDIALOG_SELECTION</code>; otherwise, the default is <code>XmDIALOG_WORK_AREA</code>. <code>XmCreatePromptDialog</code> and <code>XmCreateSelectionDialog</code> set and append this resource to the creation <i>arglist</i> supplied by the application. This resource cannot be modified after creation.</p>
<dt><code>XmNhelpLabelString</code></p>
<dd>Specifies the string label for the <code>Help</code> button. The default for this resource depends on the locale. In the C locale the default is <code>Help</code>.</p>
<dd>Now that some default localized label strings are provided through message catalogs for the children of composite widgets, the <code>labelString</code> resources cannot be set on the child through default resource files. Instead, the resource provided at the parent level must be used.</p>
<dt><code>XmNlistItems</code></p>
<dd>Specifies the items in the SelectionBox list. <code>XtGetValues</code> for this resource returns the list items themselves, not a copy of the list items. The application must not free the returned items.</p>
<dt><code>XmNlistItemCount</code></p>
<dd>Specifies the number of items in the SelectionBox list. The value must not be negative.</p>
<dt><code>XmNlistLabelString</code></p>
<dd>Specifies the string label to appear above the SelectionBox list containing the selection items. The default for this resource depends on the locale. In the C locale the default is <code>Items</code> unless <code>XmNdialogType</code> is <code>XmDIALOG_PROMPT</code>; in this case the default is NULL.</p>
<dd>Now that some default localized label strings are provided through message catalogs for the children of composite widgets, the <code>labelString</code> resources cannot be set on the child through default resource files. Instead, the resource provided at the parent level must be used.</p>
<dt><code>XmNlistVisibleItemCount</code></p>
<dd>Specifies the number of items displayed in the SelectionBox list. The value must be greater than 0 (zero) unless <code>XmNdialogType</code> is <code>XmDIALOG_PROMPT</code>; in this case, the value is always 0. The default is dynamic based on the height of the list.</p>
<dt><code>XmNminimizeButtons</code></p>
<dd>Sets the buttons to the width of the widest button and height of the tallest button if False. If True, button width and height are not modified.</p>
<dt><code>XmNmustMatch</code></p>
<dd>Specifies whether the selection widget should check if the user&#8217;s selection in the text edit field has an exact match in the SelectionBox list when the <code>OK</code> button is activated. If the selection does not have an exact match, and <code>XmNmustMatch</code> is True, the <code>XmNnoMatchCallback</code> callbacks are called. If the selection does have an exact match or if <code>XmNmustMatch</code> is False, <code>XmNokCallback</code> callbacks are called.</p>
<dt><code>XmNnoMatchCallback</code></p>
<dd>Specifies the list of callbacks called when the user makes a selection from the text edit field that does not have an exact match with any of the items in the list box. The callback reason is <code>XmCR_NO_MATCH</code>. Callbacks in this list are called only if <code>XmNmustMatch</code> is true.</p>
<dt><code>XmNokCallback</code></p>
<dd>Specifies the list of callbacks called when the user activates the <code>OK</code> button. The callback reason is <code>XmCR_OK</code>. If the selection text does not match a list item, and <code>XmNmustMatch</code> is True, the <code>XmNnoMatchCallback</code> callbacks are called instead.</p>
<dt><code>XmNokLabelString</code></p>
<dd>Specifies the string label for the <code>OK</code> button. The default for this resource depends on the locale. In the C locale the default is <code>OK</code>.</p>
<dd>Now that some default localized label strings are provided through message catalogs for the children of composite widgets, the <code>labelString</code> resources cannot be set on the child through default resource files. Instead, the resource provided at the parent level must be used.</p>
<dt><code>XmNselectionLabelString</code></p>
<dd>Specifies the string label for the selection text edit field. The default for this resource depends on the locale. In the C locale the default is <code>Selection</code>.</p>
<dd>Now that some default localized label strings are provided through message catalogs for the children of composite widgets, the <code>labelString</code> resources cannot be set on the child through default resource files. Instead, the resource provided at the parent level must be used.</p>
<dt><code>XmNtextAccelerators</code></p>
<dd>Specifies translations added to the Text widget child of the SelectionBox. The default includes bindings for the up and down keys for auto selection of list items. This resource is ignored if <code>XmNaccelerators</code> is initialized to a nondefault value.</p>
<dt><code>XmNtextColumns</code></p>
<dd>Specifies the number of columns in the Text widget. The value must be greater than 0 (zero).</p>
<dt><code>XmNtextString</code></p>
<dd>Specifies the text in the text edit selection field.</dl>
<h3>Inherited Resources</h3>
<p>SelectionBox inherits behavior and resources from the superclasses in the following tables. For a complete description of each resource, refer to the reference page for that superclass. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmBulletinBoard Resource Set</code>
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
<td>XmNallowOverlap</td>
<td>XmCAllowOverlap</td>
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
<td>XmNautoUnmanage</td>
<td>XmCAutoUnmanage</td>
<td>Boolean</td>
<td>True</td>
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
<td>XmNbuttonFontList</td>
<td>XmCButtonFontList</td>
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
<td>XmNbuttonRenderTable</td>
<td>XmCButtonRenderTable</td>
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
<td>XmNcancelButton</td>
<td>XmCWidget</td>
<td>Widget</td>
<td>dynamic</td>
<td>SG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNdefaultButton</td>
<td>XmCWidget</td>
<td>Widget</td>
<td>dynamic</td>
<td>SG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNdefaultPosition</td>
<td>XmCDefaultPosition</td>
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
<td>XmNdialogStyle</td>
<td>XmCDialogStyle</td>
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
<td>XmNdialogTitle</td>
<td>XmCDialogTitle</td>
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
<td>XmNlabelFontList</td>
<td>XmCLabelFontList</td>
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
<td>XmNlabelRenderTable</td>
<td>XmCLabelRenderTable</td>
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
<td>XmNmapCallback</td>
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
<tr VALIGN=top>
<td>XmNmarginWidth</td>
<td>XmCMarginWidth</td>
<td>Dimension</td>
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
<tr VALIGN=top>
<td>XmNnoResize</td>
<td>XmCNoResize</td>
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
<td>XmNresizePolicy</td>
<td>XmCResizePolicy</td>
<td>unsigned char</td>
<td>XmRESIZE_ANY</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNshadowType</td>
<td>XmCShadowType</td>
<td>unsigned char</td>
<td>XmSHADOW_OUT</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtextFontList</td>
<td>XmCTextFontList</td>
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
<td>XmNtextRenderTable</td>
<td>XmCTextRenderTable</td>
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
<td>XmNtextTranslations</td>
<td>XmCTranslations</td>
<td>XtTranslations</td>
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
<td>XmNunmapCallback</td>
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
 XmString <i>value</i>;
 int <i>length</i>;
} XmSelectionBoxCallbackStruct;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the callback</p>
<dt><i>value</i></p>
<dd>Indicates the <code>XmString</code> value selected by the user from the SelectionBox list or entered into the SelectionBox text field</p>
<dt><i>length</i></p>
<dd>Indicates the size in bytes of the <code>XmString</code> value This member is obsolete and exists for compatibility with earlier releases.</dl>
<h3>Translations</h3>
<p><code>XmSelectionBox</code> inherits translations from <code>XmBulletinBoard</code>.</p>
<h3>Accelerators</h3>
<p>The <code>XmNtextAccelerators</code> are added to the Text descendant of <code>XmSelectionBox</code>. The default accelerators are described in the following list. </p>
<p> The following key names are listed in the X standard key event translation table syntax. This format is the one used by Motif to specify the widget actions corresponding to a given key. A brief overview of the format is provided under <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3). For a complete description of the format, please refer to the X Toolkit Instrinsics Documentation.</p>
<dl COMPACT>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfUp&gt;</code>:</p>
<dd>SelectionBoxUpOrDown(<code>Previous</code>)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfDown&gt;</code>:</p>
<dd>SelectionBoxUpOrDown(<code>Next</code>)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfBeginLine&gt;</code>:</p>
<dd>SelectionBoxUpOrDown(<code>First</code>)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfEndLine&gt;</code>:</p>
<dd>SelectionBoxUpOrDown(<code>Last</code>)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfRestore&gt;</code>:</p>
<dd>SelectionBoxRestore()</p>
<dt><code>s c &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>space</code>:</p>
<dd>SelectionBoxRestore()</dl>
<h3>Action Routines</h3>
<p>The XmSelectionBox action routines are</p>
<dl COMPACT>
<dt>SelectionBoxUpOrDown(<code>Previous|Next|First|Last</code>):</p>
<dd>When called with an argument of <code>Previous</code>, or 0 (zero) for compatibility, selects the previous item in the list and replaces the text with that item.</p>
<dd>When called with an argument of <code>Next</code>, or 1 for compatibility, selects the next item in the list and replaces the text with that item.</p>
<dd>When called with an argument of <code>First</code>, or 2 for compatibility, selects the first item in the list and replaces the text with that item.</p>
<dd>When called with an argument of <code>Last</code>, or 3 for compatibility, selects the last item in the list and replaces the text with that item.</p>
<dt>SelectionBoxRestore():</p>
<dd>Replaces the text value with the list selection. If no item in the list is selected, clears the text.</dl>
<h3>Additional Behavior</h3>
<p>The SelectionBox widget has the following additional behavior:</p>
<dl COMPACT>
<dt><code>&lt;Key&gt;</code><code>&lt;osfCancel&gt;</code>:</p>
<dd>Calls the activate callbacks for the cancel button if it is sensitive. If no cancel button exists and the parent of the SelectionBox is a manager, passes the event to the parent.</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfActivate&gt;</code>:</p>
<dd>Calls the activate callbacks for the button with the keyboard focus. If no button has the keyboard focus, calls the activate callbacks for the default button if it is sensitive. In a List widget or single-line Text widget, the List or Text action associated with <code>&lt;Key&gt;</code><code>&lt;osfActivate&gt;</code> is called before the SelectionBox actions associated with <code>&lt;Key&gt;</code><code>&lt;osfActivate&gt;</code>. In a multiline Text widget, any <code>&lt;Key&gt;</code><code>&lt;osfActivate&gt;</code> event except <code>&lt;Key&gt;</code><code>&lt;osfEnter&gt;</code> calls the Text action associated with <code>&lt;Key&gt;</code><code>&lt;osfActivate&gt;</code>, then the SelectionBox actions associated with <code>&lt;Key&gt;</code><code>&lt;osfActivate&gt;</code>. If no button has the focus, no default button exists, and the parent of the SelectionBox is a manager, passes the event to the parent.</p>
<dt><code>&lt;OK Button Activated&gt;</code>:</p>
<dd>If <code>XmNmustMatch</code> is True and the text does not match an item in the file list, calls the <code>XmNnoMatchCallback</code> callbacks with reason <code>XmCR_NO_MATCH</code>. Otherwise, calls the <code>XmNokCallback</code> callbacks with reason <code>XmCR_OK</code>.</p>
<dt><code>&lt;Apply Button Activated&gt;</code>:</p>
<dd>Calls the <code>XmNapplyCallback</code> callbacks with reason <code>XmCR_APPLY</code>.</p>
<dt><code>&lt;Cancel Button Activated&gt;</code>:</p>
<dd>Calls the <code>XmNcancelCallback</code> callbacks with reason <code>XmCR_CANCEL</code>.</p>
<dt><code>&lt;Help Button Activated&gt;</code>:</p>
<dd>Calls the <code>XmNhelpCallback</code> callbacks with reason <code>XmCR_HELP</code>.</p>
<dt><code>&lt;MapWindow&gt;</code>:</p>
<dd>Calls the callbacks for <code>XmNmapCallback</code> if the SelectionBox is a child of a Dialog shell.</p>
<dt><code>&lt;UnmapWindow&gt;</code>:</p>
<dd>Calls the callbacks for <code>XmNunmapCallback</code> if the SelectionBox is the child of a DialogShell.</dl>
<h3>Virtual Bindings</h3>
<p>The bindings for virtual keys are vendor specific. For information about bindings for virtual buttons and keys, see <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-composite/">Composite</a></code>(3), <code><a href="/docs/linux/man/3-constraint/">Constraint</a></code>(3), <code><a href="/docs/linux/man/3-core/">Core</a></code>(3), <code><a href="/docs/linux/man/3-xmbulletinboard/">XmBulletinBoard</a></code>(3), <code><a href="/docs/linux/man/3-xmcreateselectionbox/">XmCreateSelectionBox</a></code>(3), <code><a href="/docs/linux/man/3-xmcreateselectiondialog/">XmCreateSelectionDialog</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatepromptdialog/">XmCreatePromptDialog</a></code>(3), <code><a href="/docs/linux/man/3-xmmanager/">XmManager</a></code>(3), and <code><a href="/docs/linux/man/3-xmselectionboxgetchild/">XmSelectionBoxGetChild</a></code>(3).</p>
