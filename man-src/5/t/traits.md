---
title: "traits(5)"
name: "traits"
section: "5"
letter: "t"
url: "/docs/linux/man/5-traits/"
description: "Traits — Lists the traits used by the Motif Toolkit."
---

<p><code>Traits</code> &#8212; Lists the traits used by the Motif Toolkit.</p>
<h2>Description</h2>
<p>A trait is a characteristic of a widget. A widget holding a particular trait is announcing a particular ability to other widgets. The following table summarizes the standard Motif traits. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=2><code>Purpose of Each Trait</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>Trait Name</code></td>
<td> <code>A Widget Holding This Trait Can Do The Following:</code>
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
<td><code>XmQTaccessTextual</code></td>
<td>Display one primary text parcel.
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
<td><code>XmQTactivatable</code></td>
<td> Become a command button in a dialog box.
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
<td><code>XmQTcareParentVisual</code></td>
<td> Borrow its parent&#8217;s visual information.
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
<td><code>XmQTcontainer</code></td>
<td>Manage container item children.
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
<td><code>XmQTcontainerItem</code></td>
<td> Become a child of a container widget.
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
<td><code>XmQTdialogShellSavvy</code></td>
<td>Become a child of a DialogShell.
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
<td><code>XmQTjoinSide</code></td>
<td> Attach itself to one side of a suitable parent.
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
<td><code>XmQTmenuSavvy</code></td>
<td>Become a menu child.
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
<td><code>XmQTmenuSystem</code></td>
<td>Manage a menu system.
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
<td><code>XmQTnavigator</code></td>
<td> Act as a navigator to a scrollable widget.
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
<td><code>XmQTscrollFrame</code></td>
<td> Handle one or more navigator widgets.
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
<td><code>XmQTspecifyRenderTable</code></td>
<td> Supply the names of its default render tables.
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
<td><code>XmQTtakesDefault</code></td>
<td> Change its appearance to show that it is the default button.
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
<td><code>XmQTtransfer</code></td>
<td> Transfer data to other widgets and/or receive data from other widgets
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
<p> Traits are not often used in Motif application programs. However, traits are very important to widget writers. For complete details on traits, see the <i>Motif Widget Writer&#8217;s Guide</i>. </p>
<p> The following table lists the names of all widgets and gadgets in the standard Motif widget set that hold a particular trait. For example, the following table shows that the <code>XmQTcontainerItem</code> trait is held by the <code>XmIconGadget</code>. As the table suggests, some traits are held by many of the standard Motif widgets. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=2> <code>Trait Installation in Standard Widget Set</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>Trait Name</code></td>
<td> <code>Is Installed on The Following Widgets:</code>
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
<td><code>XmQTaccessTextual</code></td>
<td> <code>XmLabel</code> and all its subclasses; <code>XmLabelGadget</code> and all its subclasses; <code>XmText; XmTextField</code>
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
<td><code>XmQTactivatable</code></td>
<td> <code>XmArrowButton; XmArrowButtonGadget; XmDrawnButton; XmPushButton; XmPushButtonGadget</code>
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
<td><code>XmQTcareParentVisual</code></td>
<td> All the subclasses of <code>XmGadget</code> (but not <code>XmGadget</code> itself); <code>XmPrimitive</code> and all its subclasses
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
<td><code>XmQTcontainer</code></td>
<td><code>XmContainer</code>
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
<td><code>XmQTcontainerItem</code></td>
<td><code>XmIconGadget</code>
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
<td><code>XmQTdialogShellSavvy</code></td>
<td><code>XmBulletinBoard</code>
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
<td><code>XmQTjoinSide</code></td>
<td>No widgets install this trait
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
<td><code>XmQTmenuSavvy</code></td>
<td> <code>XmLabel; XmDrawnButton; XmCascadeButton; XmPushButton; XmToggleButton; XmLabelGadget; XmCascadeButtonGadget; XmPushButtonGadget; XmToggleButtonGadget</code>
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
<td><code>XmQTmenuSystem</code></td>
<td><code>XmRowColumn</code>
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
<td><code>XmQTnavigator</code></td>
<td><code>XmScrollBar; XmSpinBox</code>
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
<td><code>XmQTscrollFrame</code></td>
<td><code>XmNotebook; XmScrolledWindow</code>
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
<td><code>XmQTspecifyRenderTable</code></td>
<td> <code>XmBulletinBoard</code> and all its subclasses; <code>XmMenuShell; XmVendorShell</code>
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
<td><code>XmQTtakesDefault</code></td>
<td><code>XmPushButton; XmPushButtonGadget</code>
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
<td><code>XmQTtransfer</code></td>
<td> <code>XmContainer; XmLabel</code> and all its subclasses; <code>XmLabelGadget</code> and all its subclasses; <code>XmList; XmScale; XmText; XmTextField</code>
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
<p> The following table lists the traits installed on each widget. For example, the following table indicates that the <code>XmArrowButton</code> widget holds both the <code>XmQTactivatable</code> and <code>XmQTcareParentVisual</code> traits. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=2><code>Trait Use by</code>
</td>
</tr>
<tr VALIGN=top>
<td>Widget</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>Widget Name</code></td>
<td><code>Installs These Traits</code>
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
<td><code>=</code></td>
<td>
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
<td><code>XmArrowButton</code></td>
<td> <code>XmQTactivatable, XmQTcareParentVisual</code>
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
<td><code>XmArrowButtonGadget</code></td>
<td> <code>XmQTactivatable, XmQTcareParentVisual</code>
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
<td><code>XmBulletinBoard</code></td>
<td> <code>XmQTdialogShellSavvy, XmQTspecifyRenderTable</code>
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
<td><code>XmCascadeButton</code></td>
<td> <code>XmQTaccessTextual, XmQTcareParentVisual, XmQTmenuSavvy, XmQTtransfer</code>
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
<td><code>XmCascadeButtonGadget</code></td>
<td> <code>XmQTaccessTextual, XmQTcareParentVisual, XmQTmenuSavvy, XmQTtransfer XmComboBox</code>
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
<td><code>XmCommand</code></td>
<td><code>XmQTspecifyRenderTable</code>
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
<td><code>XmContainer</code></td>
<td><code>XmQTcontainer, XmQTtransfer</code>
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
<td><code>XmDialogShell</code></td>
<td>None
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
<td><code>XmDisplay</code></td>
<td>None
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
<td><code>XmDragContext</code></td>
<td>None
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
<td><code>XmDragIcon</code></td>
<td>None
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
<td><code>XmDrawingArea</code></td>
<td>None
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
<td><code>XmDrawnButton</code></td>
<td> <code>XmQTaccessTextual, XmQTactivatable, XmQTcareParentVisual, XmQTmenuSavvy, XmQTtransfer</code>
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
<td><code>XmDropTransfer</code></td>
<td>None
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
<td><code>XmFileSelectionBox</code></td>
<td><code>XmQTspecifyRenderTable</code>
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
<td><code>XmForm</code></td>
<td><code>XmQTspecifyRenderTable</code>
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
<td><code>XmFrame</code></td>
<td>None
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
<td><code>XmGadget</code></td>
<td>None
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
<td><code>XmIconGadget</code></td>
<td> <code>XmQTcareParentVisual, XmQTcontainerItem</code>
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
<td><code>XmLabel</code></td>
<td> <code>XmQTaccessTextual, XmQTcareParentVisual, XmQTmenuSavvy, XmQTtransfer</code>
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
<td><code>XmLabelGadget</code></td>
<td> <code>XmQTaccessTextual, XmQTcareParentVisual, XmQTmenuSavvy, XmQTtransfer</code>
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
<td><code>XmList</code></td>
<td><code>XmQTcareParentVisual, XmQTtransfer</code>
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
<td><code>XmMainWindow</code></td>
<td>
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
<td><code>XmManager</code></td>
<td>
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
<td><code>XmMenuShell</code></td>
<td><code>XmQTspecifyRenderTable</code>
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
<td><code>XmMessageBox</code></td>
<td><code>XmQTspecifyRenderTable</code>
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
<td><code>XmNotebook</code></td>
<td><code>XmQTscrollFrame</code>
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
<td><code>XmPanedWindow</code></td>
<td>
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
<td><code>XmPrimitive</code></td>
<td><code>XmQTcareParentVisual</code>
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
<td><code>XmPushButton</code></td>
<td> <code>XmQTaccessTextual, XmQTactivatable, XmQTcareParentVisual, XmQTmenuSavvy, XmQTtakesDefault, XmQTtransfer</code>
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
<td><code>XmPushButtonGadget</code></td>
<td> <code>XmQTaccessTextual, XmQTactivatable, XmQTcareParentVisual, XmQTmenuSavvy, XmQTtakesDefault, XmQTtransfer</code>
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
<td><code>XmRowColumn</code></td>
<td><code>XmQTmenuSystem</code>
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
<td><code>XmScale</code></td>
<td><code>XmQTtransfer</code>
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
<td><code>XmScreen</code></td>
<td>
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
<td><code>XmScrollbar</code></td>
<td><code>XmQTcareParentVisual, XmQTnavigator</code>
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
<td><code>XmScrolledWindow</code></td>
<td><code>XmQTscrollFrame</code>
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
<td><code>XmSelectionBox</code></td>
<td><code>XmQTspecifyRenderTable</code>
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
<td><code>XmSeparator</code></td>
<td><code>XmQTcareParentVisual</code>
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
<td><code>XmSeparatorGadget</code></td>
<td><code>XmQTcareParentVisual</code>
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
<td><code>XmSpinBox</code></td>
<td><code>XmQTnavigator</code>
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
<td><code>XmText</code></td>
<td> <code>XmQTaccessTextual, XmQTcareParentVisual, XmQTtransfer</code>
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
<td><code>XmTextField</code></td>
<td> <code>XmQTaccessTextual, XmQTcareParentVisual, XmQTtransfer</code>
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
<td><code>XmToggleButton</code></td>
<td> <code>XmQTaccessTextual, XmQTcareParentVisual, XmQTtransfer</code>
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
<td><code>XmToggleButtonGadget</code></td>
<td> <code>XmQTaccessTextual, XmQTcareParentVisual, XmQTtransfer</code>
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
<td><code>VendorShell</code></td>
<td><code>XmQTspecifyRenderTable</code>
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
<p> The following table summarizes how the standard Motif widgets access traits. There are two general ways for a widget to access the traits of another widget. </p>
<p> One way is for a widget to ask another widget if it holds a particular trait. For example, <code>XmBulletinBoard</code> asks each of its children widgets if they hold the <code>XmQTtakesDefault</code> trait. <code>XmBulletinBoard</code> calls none of the trait methods of <code>XmQTtakesDefault</code>. </p>
<p> Another kind of access is when one widget calls another widget&#8217;s trait method(s). For example, <code>XmBulletinBoard</code> calls the <code>getRenderTable</code> trait method of the <code>XmQTspecifyRenderTable</code> trait. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3><code>Trait Access By</code>
</td>
</tr>
<tr VALIGN=top>
<td>Widget</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>Widget</code></td>
<td><code>Accesses These Traits:</code></td>
<td><code>Calls These Trait Methods:</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmArrowButton</code></td>
<td>None</td>
<td>None
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmArrowButtonGadget</code></td>
<td>None</td>
<td>None
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmBulletinBoard</code></td>
<td><code>XmQTtakesDefault</code></td>
<td>None
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmBulletinBoard</code></td>
<td><code>XmQTspecifyRenderTable</code></td>
<td><code>getRenderTable</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmCascadeButton</code></td>
<td><code>XmQTmenuSystem</code></td>
<td>Many
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmCascadeButton</code></td>
<td><code>XmQTspecifyRenderTable</code></td>
<td><code>getRenderTable</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmCascadeButtonGadget</code></td>
<td><code>XmQTmenuSystem</code></td>
<td>Many
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmCascadeButtonGadget</code></td>
<td><code>XmQTspecifyRenderTable</code></td>
<td><code>getRenderTable</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmComboBox</code></td>
<td><code>XmQTaccessTextual</code></td>
<td><code>getValue, setValue</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmCommand</code></td>
<td>None</td>
<td>None
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmContainer</code></td>
<td><code>XmQTcontainerItem</code></td>
<td><code>getValues, setValues</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmContainer</code></td>
<td><code>XmQTscrollFrame</code></td>
<td><code>getInfo</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmDialogShell</code></td>
<td><code>XmQTdialogShellSavvy</code></td>
<td><code>callMapUnmapCB</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmDisplay</code></td>
<td>None</td>
<td>None
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmDragContext</code></td>
<td>None</td>
<td>None
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmDragIcon</code></td>
<td>None</td>
<td>None
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmDrawingArea</code></td>
<td>None</td>
<td>None
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmDrawnButton</code></td>
<td><code>XmQTmenuSystem</code></td>
<td>Many
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmDrawnButton</code></td>
<td><code>XmQTspecifyRenderTable</code></td>
<td><code>getRenderTable</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmDropTransfer</code></td>
<td>None</td>
<td>None
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmFileSelectionBox</code></td>
<td><code>XmQTactivatable</code></td>
<td>None
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmForm</code></td>
<td>None</td>
<td>None
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmFrame</code></td>
<td>None</td>
<td>None
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmGadget</code></td>
<td>None</td>
<td>None
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmIconGadget</code></td>
<td><code>XmQTcontainer</code></td>
<td><code>getValues</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmIconGadget</code></td>
<td><code>XmQTspecifyRenderTable</code></td>
<td><code>getRenderTable</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmLabel</code></td>
<td><code>XmQTmenuSystem</code></td>
<td><code>various methods</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmLabel</code></td>
<td><code>XmQTspecifyRenderTable</code></td>
<td><code>getRenderTable</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmLabelGadget</code></td>
<td><code>XmQTmenuSystem</code></td>
<td><code>various methods</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmLabelGadget</code></td>
<td><code>XmQTspecifyRenderTable</code></td>
<td><code>getRenderTable</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmList</code></td>
<td><code>XmQTnavigator</code></td>
<td><code>getValues</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmList</code></td>
<td><code>XmQTscrollFrame</code></td>
<td><code>getInfo, init</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmList</code></td>
<td><code>XmQTspecifyRenderTable</code></td>
<td><code>getRenderTable</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmMainWindow</code></td>
<td><code>XmQTmenuSystem</code></td>
<td><code>various methods</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmManager</code></td>
<td>None</td>
<td>None
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmMenuShell</code></td>
<td><code>XmQTmenuSystem</code></td>
<td><code>various methods</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmMenuShell</code></td>
<td><code>XmQTspecifyRenderTable</code></td>
<td><code>getRenderTable</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmMessageBox</code></td>
<td><code>XmQTactivatable</code></td>
<td>None
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNotebook</code></td>
<td><code>XmQTscrollFrame</code></td>
<td><code>init, addNavigator, removeNavigator</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNotebook</code></td>
<td><code>XmQTnavigator</code></td>
<td><code>getValue</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNotebook</code></td>
<td><code>XmQTactivatable</code></td>
<td><code>changeCB</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNotebook</code></td>
<td><code>XmQTaccessTextual</code></td>
<td>None
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmPanedWindow</code></td>
<td>None</td>
<td>None
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmPrimitive</code></td>
<td>None</td>
<td>None
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmPushButton</code></td>
<td><code>XmQTmenuSystem</code></td>
<td><code>various methods</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmPushButton</code></td>
<td><code>XmQTspecifyRenderTable</code></td>
<td><code>getRenderTable</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmPushButtonGadget</code></td>
<td><code>XmQTmenuSystem</code></td>
<td><code>various methods</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmPushButtonGadget</code></td>
<td><code>XmQTspecifyRenderTable</code></td>
<td><code>getRenderTable</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmRowColumn</code></td>
<td><code>XmQTmenuSavvy</code></td>
<td> <code>getAccelerator, getMnemonic, getActivateCBName</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmRowColumn</code></td>
<td><code>XmQTmenuSystem</code></td>
<td><code>various methods</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmScale</code></td>
<td><code>XmQTspecifyRenderTable</code></td>
<td><code>getRenderTable</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmScreen</code></td>
<td>None</td>
<td>None
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmScrollbar</code></td>
<td>None</td>
<td>None
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmScrolledWindow</code></td>
<td><code>XmQTnavigator</code></td>
<td><code>getValue</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmScrolledWindow</code></td>
<td><code>XmQTscrollFrame</code></td>
<td><code>init, addNavigator</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmSelectionBox</code></td>
<td><code>XmQTaccessTextual</code></td>
<td><code>setValue;</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmSelectionBox</code></td>
<td><code>XmQTactivatable</code></td>
<td>None
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmSeparator</code></td>
<td>None</td>
<td>None
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmSeparatorGadget</code></td>
<td>None</td>
<td>None
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmSpinBox</code></td>
<td><code>XmQTaccessTextual</code></td>
<td><code>setValue</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmText</code></td>
<td><code>XmQTaccessTextual</code></td>
<td><code>getValue, setValue</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmText</code></td>
<td><code>XmQTnavigator</code></td>
<td><code>getValue</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmText</code></td>
<td><code>XmQTscrollFrame</code></td>
<td><code>getInfo, init</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmText</code></td>
<td><code>XmQTspecifyRenderTable</code></td>
<td><code>getRenderTable</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmTextField</code></td>
<td><code>XmQTspecifyRenderTable</code></td>
<td><code>getRenderTable</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmToggleButton</code></td>
<td><code>XmQTmenuSystem</code></td>
<td><code>various methods</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmToggleButton</code></td>
<td><code>XmQTspecifyRenderTable</code></td>
<td><code>getRenderTable</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmToggleButtonGadget</code></td>
<td><code>XmQTmenuSystem</code></td>
<td><code>various methods</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmToggleButtonGadget</code></td>
<td><code>XmQTspecifyRenderTable</code></td>
<td><code>getRenderTable</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>VendorShell</code></td>
<td><code>XmQTspecifyRenderTable</code></td>
<td><code>getRenderTable</code>
</td>
</tr>
<tr VALIGN=top>
<td>
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
<h2>Related</h2>
<p>The following reference pages are documented in the <i>Motif Widget Writer&#8217;s Guide</i>: <code><a href="/docs/linux/man/3-xmetraitset/">XmeTraitSet</a></code>(3), <code><a href="/docs/linux/man/3-xmetraitget/">XmeTraitGet</a></code>(3), <code><a href="/docs/linux/man/3-xmqtaccesstextual/">XmQTaccessTextual</a></code>(3), <code><a href="/docs/linux/man/3-xmqtactivatable/">XmQTactivatable</a></code>(3), <code><a href="/docs/linux/man/3-xmqtcareparentvisual/">XmQTcareParentVisual</a></code>(3), <code><a href="/docs/linux/man/3-xmqtcontainer/">XmQTcontainer</a></code>(3), <code><a href="/docs/linux/man/3-xmqtcontaineritem/">XmQTcontainerItem</a></code>(3), <code><a href="/docs/linux/man/3-xmqtdialogshellsavvy/">XmQTdialogShellSavvy</a></code>(3), <code><a href="/docs/linux/man/3-xmqtjoinside/">XmQTjoinSide</a></code>(3), <code><a href="/docs/linux/man/3-xmqtmenusavvy/">XmQTmenuSavvy</a></code>(3), <code><a href="/docs/linux/man/3-xmqtmenusystem/">XmQTmenuSystem</a></code>(3), <code><a href="/docs/linux/man/3-xmqtnavigator/">XmQTnavigator</a></code>(3), <code><a href="/docs/linux/man/3-xmqtscrollframe/">XmQTscrollFrame</a></code>(3), <code><a href="/docs/linux/man/3-xmqtspecifyrendertable/">XmQTspecifyRenderTable</a></code>(3), and <code><a href="/docs/linux/man/3-xmqttakesdefault/">XmQTtakesDefault</a></code>(3).</p>
