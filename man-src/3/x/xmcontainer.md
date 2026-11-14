---
title: "xmcontainer(3)"
name: "xmcontainer"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcontainer/"
description: "XmContainer — The Container widget class"
---

<p><code>XmContainer</code> &#8212; The Container widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Container.h&gt;</pre>
<h2>Description</h2>
<p>Container manages child widgets that have the <code>ContainerItem</code> trait. These child widgets can be viewed in several different layout formats, selected using different selection types and techniques, and directly manipulated by the user. </p>
<p> Three different formats or views are supported by the Container. They are specified via the <code>XmNentryViewType</code> resource:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd><code>XmLARGE_ICON</code></p>
<dt> &bull;</p>
<dd><code>XmSMALL_ICON</code></p>
<dt> &bull;</p>
<dd><code>XmANY_ICON</code></dl>
<p> Three different layout types are supported by the Container. They are specified by the <code>XmNlayoutType</code> resource:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd><code>XmSPATIAL</code></p>
<dt> &bull;</p>
<dd><code>XmOUTLINE</code></p>
<dt> &bull;</p>
<dd><code>XmDETAIL</code></dl>
<p> In the <code>XmSPATIAL</code> layout type, several other resources (<code>XmNspatialStyle</code>, <code>XmNspatialIncludeModel</code>, <code>XmNspatialSnapModel</code>) control the positioning of the items within the Container; an application programmer can specify these resources so that the Container strictly enforces the position of each item or so that the Container positions items according to constraint resources specified for each item. The user, however, can alter the position of an item in the <code>XmSPATIAL</code> layout type within the Container by direct manipulation; for example, by pressing <code>BTransfer</code> over the item and then dragging and releasing <code>BTransfer</code> over some location within the Container. </p>
<p> In the <code>XmOUTLINE</code> layout type, the Container controls the positioning of the items. Items within the Container can have parent-child relationships between them. Each item&#8217;s <code>XmNentryParent</code> resource can specify another item in the same Container as its parent; items with a non-NULL value for <code>XmNentryParent</code> can only be displayed in the <code>XmOUTLINE</code> layout type. In the <code>XmOUTLINE</code> layout type, items are positioned in a tree configuration with connecting lines drawn to illustrate the relationships. Items are positioned top to bottom in the order specified by <code>XmNpositionIndex</code> within their parent. Container positions a PushButton next to each item that has a parent relationship to other items. The PushButton contains a pixmap to illustrate whether the child items are shown or not; the user can activate the PushButton to toggle between showing or hiding the child items. Direct manipulation to alter the position of the item is not supported in the <code>XmOUTLINE</code> layout type. Note that the <code>XmNtraversalOn</code> resource of the PushButtons created by Container are set to False. </p>
<p> The <code>XmDETAIL</code> layout type is the same as <code>XmOUTLINE</code>, except that each item can also display additional information as rows in columns with column headers specified in the <code>XmNdetailColumnHeading</code> resources. In each item row, the item&#8217;s detail information (see the reference page on <code>XmIconGadget</code> for a description of the <code>XmNentryDetail</code> resource) is displayed. Items are positioned top to bottom in the order specified by <code>XmNpositionIndex</code> within the parent.</p>
<h3>Selection</h3>
<p>When a child widget of the container is selected, the container specifies that the item should display the appropriate visual information to the user via the <code>ContainerItem</code> trait. The application program is notified of selection changes through <code>XmNselectionCallback</code>. </p>
<p> The container uses four selection policies:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd>Single</p>
<dt> &bull;</p>
<dd>Browse</p>
<dt> &bull;</p>
<dd>Multiple</p>
<dt> &bull;</p>
<dd>Extended</dl>
<p> In Single Select and Browse Select modes, only one item can be selected at a time. Pressing <code>BSelect</code> on an item selects it and deselects any other selected item. Pressing <code>BSelect</code> over an empty space in the Container deselects all items. In Browse Select, dragging <code>BSelect</code> moves the selection as the pointer is moved. </p>
<p> In Multiple Select and Extended Select modes, any number of items can be selected at the same time. In Multiple Select, pressing and dragging <code>BSelect</code> or <code>BExtend</code> to specify an item, range of items, or group of discontiguous items causes the selection states of those items to be toggled. In Extended Select, pressing and dragging <code>BSelect</code> to indicate an item, range of items, or group of discontiguous items selects those items and deselects all others. Pressing and dragging <code>BExtend</code> in Extended Select to indicate an item, range of items, or discontiguous group of items causes the selection states of those items to be toggled. </p>
<p> Several techniques are available to indicate an item, range of items, or group of discontiguous items in the Multiple Select and Extended Select modes. </p>
<p> In the <code>XmSPATIAL</code> and <code>XmOUTLINE</code> layout types, the <code>XmNselectionTechnique</code> resource specifies the techniques to be used to indicate items. The default specification of <code>XmTOUCH_OVER</code> allows both the Random-Swipe and Marquee techniques to be used when <code>XmNlayoutStyle</code> is <code>XmSPATIAL</code>. The default specification of <code>XmTOUCH_OVER</code> allows the Range-Swipe, Range-Click, and Marquee techniques to be used when <code>XmNlayoutStyle</code> is <code>XmOUTLINE</code>. </p>
<p> Discontiguous groups of items can be selected using the Random-Swipe technique. In the Random-Swipe technique, pressing <code>BSelect</code> (or <code>BExtend</code>) over an item and dragging <code>BSelect</code> over other items selects all of those items. Only those items that pointer passed over are selected. </p>
<p> In the Range-Swipe technique, the user presses <code>BSelect</code> (or <code>BExtend</code>) over the first item and releases <code>BSelect</code> over the last item; all items within the range between the first and last item are selected whether the pointer actually passed over them or not. In the Range-Click technique, the user presses and releases <code>BSelect</code> (or <code>BExtend</code>) over the first item and then presses and releases <code>BExtend</code> over the last item. </p>
<p> In the Marquee technique, pressing <code>BSelect</code> (or <code>BExtend</code>) over a blank space within the Container indicates the starting point of a Marquee rectangle. Dragging <code>BSelect</code> draws a Marquee rectangle (rubberband line) between the starting point and current pointer. All items completely within the Marquee rectangle are selected. </p>
<p> Specifying <code>XmTOUCH_ONLY</code> for <code>XmNselectionTechnique</code> enforces the Random-Swipe technique even when <code>BSelect</code> (or <code>BExtend</code>) is pressed over a blank space. Similarly, specifying <code>XmMARQUEE</code> enforces the Marquee technique even when <code>BSelect</code> (or <code>BExtend</code>) is pressed over an item; since the item over which the press occurs is only partially included in the Marquee rectangle, it is not selected. <code>XmMARQUEE_EXTEND_START</code> and <code>XmMARQUEE_EXTEND_BOTH</code> enforce the Marquee technique and also cause the rectangle to extend automatically around the first item indicated and, for <code>XmMARQUEE_EXTEND_BOTH</code>, the last item. </p>
<p> In the <code>XmDETAIL</code> layout type, the Range-Swipe and Range-Click techniques are available to indicate a range of items for selection. </p>
<p> Container uses the <code>XmQTcontainerItem</code>, <code>XmQTscrollFrame</code>, and <code>XmQTspecifyRenderTable</code> traits and holds the <code>XmQTcontainer</code> and <code>XmQTtransfer</code> traits.</p>
<h3>Data Transfer Behavior</h3>
<p>Container supports dragging of selected items from the widget. Depending on the value of <code>XmNprimaryOwnership</code>, Container can also support primary selection. </p>
<p> As a source of data, Container supports the following targets and associated conversions of data to these targets:</p>
<dl COMPACT>
<dt><i>locale</i></p>
<dd>If the <i>locale</i> target matches the widget&#8217;s locale, the widget transfers the selected items in the encoding of the locale. The value for each item transferred, except the last, includes a trailing separator. Each item value is the <code>XmNlabelString</code> of the item.</p>
<dt><code>COMPOUND_TEXT</code></p>
<dd>The widget transfers the selected items as type <code>COMPOUND_TEXT</code>. The value for each item transferred, except the last, includes a trailing separator. Each item value is the <code>XmNlabelString</code> of the item.</p>
<dt><code>DELETE</code></p>
<dd>The widget deletes the selected items.</p>
<dt><code>PIXMAP</code></p>
<dd>The widget transfers a list of the pixmap IDs of the selected items as type <code>DRAWABLE</code>.</p>
<dt><code>STRING</code></p>
<dd>The widget transfers the selected items as type <code>STRING</code>. The value for each item transferred, except the last, includes a trailing separator. Each item value is the <code>XmNlabelString</code> of the item.</p>
<dt><code>TEXT</code></p>
<dd>If the selected items are fully convertible to the encoding of the locale, the widget transfers the selected items in the encoding of the locale. Otherwise, the widget transfers the selected items as type <code>COMPOUND_TEXT</code>. The value for each item transferred, except the last, includes a trailing separator. Each item value is the <code>XmNlabelString</code> of the item.</p>
<dt><code>_MOTIF_CLIPBOARD_TARGETS</code></p>
<dd>The widget transfers, as type <code>ATOM</code>, a list of the targets it supports for immediate transfer for the <code>CLIPBOARD</code> selection. These include <code>_MOTIF_COMPOUND_STRING</code> and <code>PIXMAP</code>. If the selected items are fully convertible to <code>STRING</code>, these also include <code>STRING</code>; otherwise, they also include <code>COMPOUND_TEXT</code> and <code>UTF8_STRING</code>.</p>
<dt><code>_MOTIF_COMPOUND_STRING</code></p>
<dd>The widget transfers the selected items as a compound string in Byte Stream format. The value for each item transferred, except the last, includes a trailing separator. Each item value is the <code>XmNlabelString</code> of the item.</p>
<dt><code>UTF8_STRING</code></p>
<dd>The widget transfers the selected items as type <code>UTF8_STRING</code>. The value for each item transferred, except the last, includes a trailing separator. Each item value is the <code>XmNlabelString</code> of the item.</p>
<dt><code>_MOTIF_DEFERRED_CLIPBOARD_TARGETS</code></p>
<dd>The widget transfers, as type <code>ATOM</code>, a list of the targets it supports for delayed transfer for the <code>CLIPBOARD</code> selection. This widget currently supplies no targets for <code>_MOTIF_DEFERRED_CLIPBOARD_TARGETS</code>.</p>
<dt><code>_MOTIF_DRAG_OFFSET</code></p>
<dd>The widget transfers a list of two 16-bit numbers, of type <code>INTEGER</code>, representing an x and y offset for an item being dragged. This offset is calculated so that, if the offset were added to the x and y coordinates at the drop site, and the dragged pixmap placed at that position, it would correspond to the position the user would expect the pixmap to placed at, based on the drag icon used at the drop site.</p>
<dt><code>_MOTIF_EXPORT_TARGETS</code></p>
<dd>The widget transfers, as type <code>ATOM</code>, a list of the targets to be used as the value of the DragContext&#8217;s <code>XmNexportTargets</code> in a drag-and-drop transfer. These include <code>_MOTIF_COMPOUND_STRING</code>, <code>PIXMAP</code>, <code>COMPOUND_TEXT</code>, the encoding of the locale, <code>STRING</code>, <code>TEXT</code>, <code>BACKGROUND</code>, <code>FOREGROUND</code>, and <code>UTF8_STRING</code>.</dl>
<p> As a source of data, Container also supports the following standard Motif targets:</p>
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
<dd>The widget transfers, as type <code>ATOM</code>, a list of the targets it supports. These include the standard targets in this list. These also include <code>_MOTIF_COMPOUND_STRING</code>, <code>PIXMAP</code>, <code>COMPOUND_TEXT</code>, the encoding of the locale, <code>STRING</code>, <code>TEXT</code>, and <code>UTF8_STRING</code>.</p>
<dt><code>TIMESTAMP</code></p>
<dd>The widget transfers the timestamp used to acquire the selection as type <code>INTEGER</code>.</p>
<dt><code>_MOTIF_RENDER_TABLE</code></p>
<dd>The widget transfers <code>XmNrenderTable</code> if it exists, or else the default text render table, as type <code>STRING</code>.</p>
<dt><code>_MOTIF_ENCODING_REGISTRY</code></p>
<dd>The widget transfers its encoding registry as type <code>STRING</code>. The value is a list of NULL separated items in the form of tag encoding pairs. This target symbolizes the transfer target for the Motif Segment Encoding Registry. Widgets and applications can use this Registry to register text encoding formats for specified render table tags. Applications access this Registry by calling <code>XmRegisterSegmentEncoding</code> and <code>XmMapSegmentEncoding</code>.</dl>
<p> As a destination for data, Container supports only the dropping of items being dragged from the same widget. Subclasses and the <code>XmNdestinationCallback</code> procedures are responsible for any other data transfers to the widget.</p>
<h3>Classes</h3>
<p>Container inherits behavior, resources, and traits from the <code>Core</code>, <code>Composite</code>, <code>Constraint</code>, and <code>XmManager</code> classes. </p>
<p> The class pointer is <code>xmContainerWidgetClass</code>. </p>
<p> The class name is <code>XmContainer</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate whether the given resource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmContainer Resource Set</code>
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
<td>unsigned char</td>
<td>XmAUTO_SELECT</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNcollapsedStatePixmap</td>
<td>XmCCollapsedStatePixmap</td>
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
<td>XmNdetailColumnHeading</td>
<td>XmCDetailColumnHeading</td>
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
<td>XmNdetailColumnHeadingCount</td>
<td>XmCDetailColumnHeadingCount</td>
<td>Cardinal</td>
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
<td>XmNdetailOrder</td>
<td>XmCDetailOrder</td>
<td>Cardinal *</td>
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
<td>XmNdetailOrderCount</td>
<td>XmCDetailOrderCount</td>
<td>Cardinal</td>
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
<td>XmNdetailTabList</td>
<td>XmCDetailTabList</td>
<td>XmTabList</td>
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
<td>XmNentryViewType</td>
<td>XmCEntryViewType</td>
<td>unsigned char</td>
<td>XmANY_ICON</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNexpandedStatePixmap</td>
<td>XmCExpandedStatePixmap</td>
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
<td>XmNlargeCellHeight</td>
<td>XmCCellHeight</td>
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
<td>XmNlargeCellWidth</td>
<td>XmCCellWidth</td>
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
<td>XmNlayoutType</td>
<td>XmCLayoutType</td>
<td>unsigned char</td>
<td>XmSPATIAL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
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
<td>XmNoutlineButtonPolicy</td>
<td>XmCOutlineButtonPolicy</td>
<td>unsigned char</td>
<td>XmOUTLINE_BUTTON_PRESENT</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNoutlineChangedCallback</td>
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
<td>XmNoutlineColumnWidth</td>
<td>XmCOutlineColumnWidth</td>
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
<td>XmNoutlineIndentation</td>
<td>XmCOutlineIndentation</td>
<td>Dimension</td>
<td>40</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNoutlineLineStyle</td>
<td>XmCLineStyle</td>
<td>unsigned char</td>
<td>XmSINGLE</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
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
<td>XmCprimaryOwnership</td>
<td>unsigned char</td>
<td>XmOWN_POSSIBLE_MULTIPLE</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
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
<td>XmNselectedObjects</td>
<td>XmCSelectedObjects</td>
<td>WidgetList</td>
<td>NULL</td>
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
<td>XmNselectedObjectCount</td>
<td>XmCSelectedObjectCount</td>
<td>unsigned int</td>
<td>0</td>
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
<td>XmNselectionCallback</td>
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
<td>XmNselectionPolicy</td>
<td>XmCSelectionPolicy</td>
<td>unsigned char</td>
<td>XmEXTENDED_SELECT</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNselectionTechnique</td>
<td>XmCSelectionTechnique</td>
<td>unsigned char</td>
<td>XmTOUCH_OVER</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNsmallCellHeight</td>
<td>XmCCellHeight</td>
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
<td>XmNsmallCellWidth</td>
<td>XmCCellWidth</td>
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
<td>XmNspatialIncludeModel</td>
<td>XmCSpatialIncludeModel</td>
<td>unsigned char</td>
<td>XmAPPEND</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNspatialResizeModel</td>
<td>XmCSpatialResizeModel</td>
<td>unsigned char</td>
<td>XmGROW_MINOR</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNspatialSnapModel</td>
<td>XmCSpatialSnapModel</td>
<td>unsigned char</td>
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
<td>XmNspatialStyle</td>
<td>XmCSpatialStyle</td>
<td>unsigned char</td>
<td>XmGRID</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
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
<dd>Indicates whether the Container invokes selection callbacks when each item is selected (or toggled) or whether selection callbacks are not invoked until the user has completed selection actions (for example, the user has released the mouse button). It can have one of the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmAUTO_SELECT</code></p>
<dd>Makes selection callbacks automatically when each item is selected or toggled. This may also be the value <code>TRUE</code>.</p>
<dt><code>XmNO_AUTO_SELECT</code></p>
<dd>Delays selection callbacks until the user has finished selection actions. This may also be the value <code>FALSE</code>.</dl>
</dl>
<dt><code>XmNcollapsedStatePixmap</code></p>
<dd>Specifies the pixmap to display on a PushButton next to a Container item with child items, when <code>XmNoutlineButtonPolicy</code> is <code>XmOUTLINE_BUTTON_PRESENT</code>. <code>XmNcollapsedStatePixmap</code> indicates that the child items are not displayed. If set to <code>XmUNSPECIFIED_PIXMAP</code>, a default pixmap showing an arrow pointing up is used.</p>
<dt><code>XmNconvertCallback</code></p>
<dd>Specifies a list of callbacks called when the Container is asked to convert a selection. The type of the structure whose address is passed to these callbacks is <code>XmConvertCallbackStruct</code>. The reason is <code>XmCR_OK</code>.</p>
<dt><code>XmNdefaultActionCallback</code></p>
<dd>Specifies a list of callbacks to call when the user double-clicks an item or presses <code>&lt;Enter&gt;</code> or <code>&lt;Return&gt;</code> over an item. The callback structure is <code>XmContainerSelectCallbackStruct</code>. The reason is <code>XmCR_DEFAULT_ACTION</code>.</p>
<dt><code>XmNdestinationCallback</code></p>
<dd>Specifies a list of callbacks called when the Container is the destination of a transfer operation. The type of the structure whose address is passed to these callbacks is <code>XmDestinationCallbackStruct</code>. The reason is <code>XmCR_OK</code>.</p>
<dt><code>XmNdetailColumnHeading</code></p>
<dd>Specifies a table of <code>XmString</code>s to display as the headings to columns. If NULL, or if <code>XmNlayoutType</code> is not <code>XmDETAIL</code>, no heading is displayed.</p>
<dt><code>XmNdetailColumnHeadingCount</code></p>
<dd>Specifies a count of <code>XmString</code>s in the table specified for <code>XmNdetailColumnHeading</code>.</p>
<dt><code>XmNdetailOrder</code></p>
<dd>Specifies an array of <code>Cardinal</code>s that indicate which column detail information, and in which order, each Container child will display its detail information. This resource is ignored if <code>XmNlayoutType</code> is not <code>XmDETAIL</code>. If NULL, the the default behavior is determined by <code>XmNdetailOrderCount</code>.</p>
<dt><code>XmNdetailOrderCount</code></p>
<dd>Specifies a count of <code>Cardinal</code>s in the array specified for <code>XmNdetailOrder</code>. If <code>XmNdetailOrder</code> is NULL and <code>XmNdetailOrderCount</code> is not 0, then each Container child displays its detail information in order from column 1 to the <code>XmNdetailOrderCount</code> column number. If <code>XmNdetailOrderCount</code> is 0, then a default is calculated from the detail order count information of each item accessed via the <code>ContainerItem</code> trait.</p>
<dt><code>XmNdetailTabList</code></p>
<dd>Indicates an <code>XmTabList</code> specifying the start of each column in the <code>XmDETAIL</code> layout. If this resource is set to NULL, then Container calculates an <code>XmTabList</code>. This resource is ignored if <code>XmNlayoutType</code> is not <code>XmDETAIL</code>.</p>
<dt><code>XmNentryViewType</code></p>
<dd>Specifies the view type for all Container children. The view type is specified for each item via the <code>ContainerItem</code> trait. It can have one of the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmANY_ICON</code></p>
<dd>No specification is made for Container children. Children use their own default specifications.</p>
<dt><code>XmLARGE_ICON</code></p>
<dd>The view type for all children is <code>XmLARGE_ICON</code>.</p>
<dt><code>XmSMALL_ICON</code></p>
<dd>The view type for all children is <code>XmSMALL_ICON</code>.</dl>
</dl>
<dt><code>XmNexpandedStatePixmap</code></p>
<dd>Specifies the pixmap to display on a PushButton next to a Container item with child items, when <code>XmNoutlineButtonPolicy</code> is <code>XmOUTLINE_BUTTON_PRESENT</code>. <code>XmNexpandedStatePixmap</code> indicates that the child items are displayed. If set to <code>XmUNSPECIFIED_PIXMAP</code>, a default pixmap showing an arrow pointing down is used.</p>
<dt><code>XmNfontList</code></p>
<dd>Specifies the fontlist associated with <code>XmContainer</code>. The fontlist is an obsolete construct and has been superseded by the render table. It is included for compatibility with earlier versions of Motif, and for applications that do not easily support render tables. The default fontlist is derived from the default render table; and if both a fontlist and a render table are specified, the render table takes precedence.</p>
<dt><code>XmNlargeCellHeight</code></p>
<dd>Specifies the height of a cell for <code>XmGRID</code> or <code>XmCELLS</code> spatial style when <code>XmNentryViewType</code> is <code>XmLARGE_ICON</code> or <code>XmANY_ICON</code>.</p>
<dt><code>XmNlargeCellWidth</code></p>
<dd>Specifies the width of a cell for <code>XmGRID</code> or <code>XmCELLS</code> spatial style when <code>XmNentryViewType</code> is <code>XmLARGE_ICON</code> or <code>XmANY_ICON</code>.</p>
<dt><code>XmNlayoutType</code></p>
<dd>Specifies the policy for laying out child widgets within the Container. It can have one of the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmDETAIL</code></p>
<dd>Displays items in the same manner as when the resource is <code>XmOUTLINE</code>, except that each item displays detail information next to it.</p>
<dt><code>XmOUTLINE</code></p>
<dd>Displays items in a tree configuration, in <code>XmNpositionIndex</code> within <code>XmNentryParent</code> order, with connecting lines drawn to show their parent-child relationships.</p>
<dt><code>XmSPATIAL</code></p>
<dd>Displays items according to <code>XmNspatialStyle</code>. Items with <code>XmNentryParent</code> values are not displayed.</dl>
</dl>
<dt><code>XmNmarginHeight</code></p>
<dd>Specifies the margin spacing at the top and bottom of the Container.</p>
<dt><code>XmNmarginWidth</code></p>
<dd>Specifies the margin spacing at the left and right sides of the Container.</p>
<dt><code>XmNoutlineButtonPolicy</code></p>
<dd>Specifies whether or not to display buttons for users to expand and collapse the display of items. It can have one of the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmOUTLINE_BUTTON_ABSENT</code></p>
<dd>Do not display the outline buttons.</p>
<dt><code>XmOUTLINE_BUTTON_PRESENT</code></p>
<dd>Display the outline buttons.</dl>
</dl>
<dt><code>XmNoutlineChangedCallback</code></p>
<dd>Specifies a list of callbacks to call when an item&#8217;s <code>XmNoutlineState</code> is changed. The callback structure is <code>XmContainerOutlineCallbackStruct</code>. The reason is <code>XmCR_COLLAPSED</code> or <code>XmCR_EXPANDED</code>, depending on the new value of <code>XmNoutlineState</code>.</p>
<dt><code>XmNoutlineColumnWidth</code></p>
<dd>Specifies the width of the first column displayed when <code>XmNlayoutType</code> is <code>XmDETAIL</code>. Specifies the preferred width of the Container (without the margins) when <code>XmNlayoutType</code> is <code>XmOUTLINE</code>. If not specified, Container will determine a default value equal to the widest space necessary to display an item&#8217;s pixmap and <code>XmNoutlineIndentation</code>.</p>
<dt><code>XmNoutlineIndentation</code></p>
<dd>Specifies the distance to indent for the display of child items when <code>XmNlayoutType</code> is <code>XmOUTLINE</code> or <code>XmDETAIL</code>.</p>
<dt><code>XmNoutlineLineStyle</code></p>
<dd>Specifies whether to draw lines between items with parent-child relationships when <code>XmNlayoutType</code> is <code>XmOUTLINE</code> or <code>XmDETAIL</code>. It can have one of the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmNO_LINE</code></p>
<dd>Draws no line.</p>
<dt><code>XmSINGLE</code></p>
<dd>Draws a line one pixel wide.</dl>
</dl>
<dt><code>XmNprimaryOwnership</code></p>
<dd>Specifies whether Container takes ownership of the primary selection when a selection is made inside it. This resource can take the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmOWN_NEVER</code></p>
<dd>Never takes ownership.</p>
<dt><code>XmOWN_ALWAYS</code></p>
<dd>Always takes ownership.</p>
<dt><code>XmOWN_MULTIPLE</code></p>
<dd>Only takes ownership if more than one element has been selected.</p>
<dt><code>XmOWN_POSSIBLE_MULTIPLE</code></p>
<dd>Only takes ownership if more than one element can be selected at a time.</dl>
</dl>
<dt><code>XmNrenderTable</code></p>
<dd>Specifies the <code>XmRenderTable</code> that is inherited by all children of the Container. The default is implementation dependent. If both a render table and a fontlist are specified, the render table will take precedence.</p>
<dt><code>XmNselectColor</code></p>
<dd>Specifies a Pixel that can be accessed by children of the Container and used to indicate that the child is in a selected state. In addition to a Pixel value, the following symbolic values can be specified:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmDEFAULT_SELECT_COLOR</code></p>
<dd>Specifies a color between the background and the bottom shadow color.</p>
<dt><code>XmREVERSED_GROUND_COLORS</code></p>
<dd>Forces the select color to the foreground color and causes the default color of any text rendered over the select color to be the background color.</p>
<dt><code>HIGHLIGHT_COLOR</code></p>
<dd>Forces the fill color to use the highlight color.</dl>
</dl>
<dt><code>XmNselectedObjectCount</code></p>
<dd>Specifies the number of widgets in the selected items list. The value must be the number of items in <code>XmNselectedObjects</code>.</p>
<dt><code>XmNselectedObjects</code></p>
<dd>An array of widgets that represents the Container items that are currently selected, either by the user or by the application.</p>
<dd>If the application sets <code>XmNselectedObjects</code> to an array of widgets, those array elements that are valid Container items are selected.</p>
<dt><code>XmNselectionCallback</code></p>
<dd>Specifies a list of callbacks to call when an item is selected. The callback structure is <code>XmContainerSelectCallbackStruct</code>. The reason is <code>XmCR_SINGLE_SELECT</code>, <code>XmCR_BROWSE_SELECT</code>, <code>XmCR_MULTIPLE_SELECT</code>, or <code>XmCR_EXTENDED_MULTIPLE</code>, depending on <code>XmNselectionPolicy</code>.</p>
<dt><code>XmNselectionPolicy</code></p>
<dd>Defines the interpretation of the selection action. This can be one of the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmSINGLE_SELECT</code></p>
<dd>Allows only single selections.</p>
<dt><code>XmBROWSE_SELECT</code></p>
<dd>Allows &quot;drag and browse&quot; selections.</p>
<dt><code>XmMULTIPLE_SELECT</code></p>
<dd>Allows multiple selections.</p>
<dt><code>XmEXTENDED_SELECT</code></p>
<dd>Allows extended selections.</dl>
</dl>
<dt><code>XmNselectionTechnique</code></p>
<dd>Specifies the selection technique to use when the Container displays items in a 2-dimensional layout (<code>XmNentryViewType</code> is <code>XmLARGE_ICON</code> or <code>XmSMALL_ICON</code>). In the <code>XmDETAIL</code> layout, the <code>XmNselectionTechnique</code> resource is treated as <code>XmTOUCH_ONLY</code>. In either case, it can have one of the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmMARQUEE</code></p>
<dd>Uses the Marquee technique only.</p>
<dt><code>XmMARQUEE_EXTEND_START</code></p>
<dd>Uses the Marquee technique only and extends the Marquee rectangle around any item under the Marquee start point.</p>
<dt><code>XmMARQUEE_EXTEND_BOTH</code></p>
<dd>Uses the Marquee technique only and extends the Marquee rectangle around any items under the Marquee start and end points.</p>
<dt><code>XmTOUCH_ONLY</code></p>
<dd>Uses the Random-Swipe technique only if <code>XmNlayoutType</code> is <code>XmSPATIAL</code>. Otherwise, uses the Range-Swipe and Range-Click techniques.</p>
<dt><code>XmTOUCH_OVER</code></p>
<dd>If the selection action begins over an item and <code>XmNlayoutType</code> is <code>XmSPATIAL</code>, uses the Random-Swipe technique. If the selection action begins over an item and <code>XmNlayoutType</code> is <code>XmOUTLINE</code> or <code>XmDETAIL</code>, uses the Range-Swipe and Range-Click techniques. Uses the Marquee technique if the select action begins over an unoccupied area in the Container.</dl>
</dl>
<dt><code>XmNsmallCellHeight</code></p>
<dd>Specifies the height of a cell for <code>XmGRID</code> or <code>XmCELLS</code> spatial style when <code>XmNentryViewType</code> is <code>XmSMALL_ICON</code>.</p>
<dt><code>XmNsmallCellWidth</code></p>
<dd>Specifies the width of a cell for <code>XmGRID</code> or <code>XmCELLS</code> spatial style when <code>XmNentryViewType</code> is <code>XmSMALL_ICON</code>.</p>
<dt><code>XmNspatialIncludeModel</code></p>
<dd>Specifies the layout of an item when the item is managed in the Container when <code>XmNlayoutType</code> is <code>XmSPATIAL</code> and <code>XmNspatialStyle</code> is <code>XmGRID</code> or <code>XmCELLS</code>. It can have one of the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmAPPEND</code></p>
<dd>Places the item after the last occupied cell according to <code>XmNlayoutDirection</code>.</p>
<dt><code>XmCLOSEST</code></p>
<dd>Places the item in the free cell closest to the position specified by <code>XmNx</code> and <code>XmNy</code>.</p>
<dt><code>XmFIRST_FIT</code></p>
<dd>Places the item in the first free cell according to <code>XmNlayoutDirection</code>.</dl>
</dl>
<dt><code>XmNspatialResizeModel</code></p>
<dd>Specifies how Container will attempt to grow its dimensions when <code>XmNlayoutType</code> is <code>XmSPATIAL</code> and <code>XmNspatialStyle</code> is <code>XmGRID</code> or <code>XmCELLS</code> and there are not enough cells to contain a new Container item. It can have one of the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmGROW_BALANCED</code></p>
<dd>Container will request both width and height growth from its parent.</p>
<dt><code>XmGROW_MAJOR</code></p>
<dd>Container will request growth in its major dimension from its parent. Container&#8217;s major dimension is width when the precedence of <code>XmNlayoutDirection</code> is horizontal, and height when vertical.</p>
<dt><code>XmGROW_MINOR</code></p>
<dd>Container will request growth in its minor dimension from its parent. Container&#8217;s minor dimension is height when the precedence of <code>XmNlayoutDirection</code> is horizontal, and width when vertical.</dl>
</dl>
<dt><code>XmNspatialSnapModel</code></p>
<dd>Specifies how Container will position an item within the cell layout when <code>XmNlayoutType</code> is <code>XmSPATIAL</code> and <code>XmNspatialStyle</code> is <code>XmGRID</code> or <code>XmCELLS</code>. It can have one of the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmCENTER</code></p>
<dd>Center the items as follows, depending on the value of <code>XmNentryViewType</code>:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmLARGE_ICON</code></p>
<dd>The child is centered in the cell horizontally and baseline-aligned vertically.</p>
<dt><code>XmSMALL_ICON</code></p>
<dd>The child is centered in the cell vertically on its baseline and aligned with the left or right of the cell horizontally, depending on the value of <code>XmNlayoutDirection</code>.</dl>
</dl>
<dt><code>XmSNAP_TO_GRID</code></p>
<dd>Position the item at the upper-left or upper-right corner of the cell(s), depending on the value of <code>XmNlayoutDirection</code>.</p>
<dt><code>XmNONE</code></p>
<dd>Position the item according to the position specified by <code>XmNx</code> and <code>XmNy</code>. If the position is not within the coordinates of the cell(s), then position the item at the upper-left or upper-right corner of the cell(s), depending on the value of <code>XmNlayoutDirection</code>.</dl>
</dl>
<dt><code>XmNspatialStyle</code></p>
<dd>Specifies the layout of Container items when <code>XmNlayoutType</code> is <code>XmSPATIAL</code>. It can have one of the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmCELLS</code></p>
<dd>Lays out items within a grid of same-size cells. Each item occupies as many cells as required to contain the item dimensions.</p>
<dt><code>XmGRID</code></p>
<dd>Lays out items within a grid of same-size cells. Each item occupies only one cell. Items that are larger than the cell size may overlap other items.</p>
<dt><code>XmNONE</code></p>
<dd>Lays out items according to <code>XmNx</code> and <code>XmNy</code>.</dl>
</dl>
</dl>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmContainer Constraint Resource Set</code>
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
<td>XmNentryParent</td>
<td>XmCWidget</td>
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
<td>XmNoutlineState</td>
<td>XmCOutlineState</td>
<td>unsigned char</td>
<td>XmCOLLAPSED</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNpositionIndex</td>
<td>XmCPositionIndex</td>
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
<dt><code>XmNentryParent</code></p>
<dd>Specifies the widget that is this item&#8217;s logical parent. A value of NULL indicates that this is a root-level item. Parent-child information is displayed only when the <code>XmNlayoutPolicy</code> is <code>XmOUTLINE</code> or <code>XmDETAIL</code>.</p>
<dt><code>XmNoutlineState</code></p>
<dd>Specifies whether to display child items when <code>XmNlayoutPolicy</code> is <code>XmOUTLINE</code> or <code>XmDETAIL</code>. It can have one of the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmCOLLAPSED</code></p>
<dd>Does not display child items.</p>
<dt><code>XmEXPANDED</code></p>
<dd>Displays child items.</dl>
</dl>
<dt><code>XmNpositionIndex</code></p>
<dd>Specifies the order of items in the Container for display. When <code>XmNlayoutType</code> is <code>XmOUTLINE</code> or <code>XmDETAIL</code>, items are displayed in <code>XmNpositionIndex</code> order within <code>XmNentryParent</code>. Items that have an <code>XmNentryParent</code> resource are ignored when <code>XmNlayoutType</code> is <code>XmSPATIAL</code>. If <code>XmNpositionIndex</code> is not specified, it defaults to the <code>XmNpositionIndex</code> value plus 1 of the item with the highest <code>XmNpositionIndex</code> that has the same <code>XmNentryParent</code> if such an item exists; otherwise, it defaults to 0.</dl>
<h3>Inherited Resources</h3>
<p>Container inherits behavior and resources from the superclasses described in the following tables. For a complete description of each resource, refer to the reference page for that superclass. </p>
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
<p>A pointer to the following structure is passed to callbacks for <code>XmNoutlineChangedCallback</code>. </p>
<pre>typedef struct
{
 int <i>reason</i>;
 XEvent <i>* event</i>;
 Widget <i>item</i>;
 unsigned char <i>new_outline_state</i>;
} XmContainerOutlineCallbackStruct;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Specifies the reason for the callback.</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the callback. It can be NULL.</p>
<dt><i>item</i></p>
<dd>Specifies the container item affected by the event.</p>
<dt><i>new_outline_state</i></p>
<dd>Specifies the next <code>XmNoutlineState</code> for <i>item</i>. The user can change this value in the callback.</dl>
<p> A pointer to the following structure is passed to callbacks for <code>XmNdefaultActionCallback</code> and <code>XmNselectionCallback</code>. </p>
<pre>typedef struct
{
 int <i>reason</i>;
 XEvent <i>* event</i>;
 WidgetList <i>selected_items</i>;
 int <i>selected_item_count</i>;
 unsigned char <i>auto_selection_type</i>;
} XmContainerSelectCallbackStruct;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Specifies the reason for the callback. It corresponds to the <code>XmNselectionPolicy</code> at the time the selection was made, or indicates that the default action should be taken.</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the callback. It can be NULL.</p>
<dt><i>selected_items</i></p>
<dd>Specifies a list of items selected at the time of the <i>event</i> that caused the callback. The <i>selected_items</i> field points to a temporary storage space that is reused after the callback is finished. Therefore, if an application needs to save the selected list, it should copy the list into its own data space.</p>
<dt><i>selected_item_count</i></p>
<dd>Specifies the number of items in the <i>selected_items</i> list. This number must be positive or 0 (zero).</p>
<dt><code>auto_selection_type</code></p>
<dd>Indicates the cause of the selection when <code>XmNautomaticSelection</code> is <code>XmAUTO_SELECT</code>. Valid values are the following:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmAUTO_UNSET</code></p>
<dd>Returned when <code>XmNautomaticSelection</code> is <code>XmNO_AUTO_SELECT</code>.</p>
<dt><code>XmAUTO_BEGIN</code></p>
<dd>Indicates the beginning of automatic selection.</p>
<dt><code>XmAUTO_MOTION</code></p>
<dd>Indicates that there is a button drag selection.</p>
<dt><code>XmAUTO_CANCEL</code></p>
<dd>Indicates that the new selection is canceled.</p>
<dt><code>XmAUTO_NO_CHANGE</code></p>
<dd>Indicates that the currently selected item matches the initial item.</p>
<dt><code>XmAUTO_CHANGE</code></p>
<dd>Indicates that the currently selected item does not match the initial item.</dl>
</dl>
</dl>
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
<dd>Contains information about the location of data to be converted. If the value is NULL, the data to be transferred consists of the widget&#8217;s current selection. Otherwise, it is the widget ID of the item being transferred, or the widget ID of the Container if all items are being transferred.</p>
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
<dd>The widget class conversion procedure, if any, is called after the callback procedures return. If the widget class conversion procedure produces any data, it overwrites the data provided by the callback procedures in the <i>value</i> member.</p>
<dt><code>XmCONVERT_MERGE</code></p>
<dd>The widget class conversion procedure, if any, is called after the callback procedures return. If the widget class conversion procedure produces any data, it appends its data to the data provided by the callback procedures in the <i>value</i> member. This value is intended for use with targets that result in lists of data, such as <code>TARGETS</code>.</p>
<dt><code>XmCONVERT_DONE</code></p>
<dd>The callback procedure has successfully finished the conversion. The widget class conversion procedure, if any, is not called after the callback procedures return.</p>
<dt><code>XmCONVERT_REFUSE</code></p>
<dd>The callback procedure has terminated the conversion process without completing the requested conversion. The widget class conversion procedure, if any, is not called after the callback procedures return.</dl>
</dl>
<dt><i>value</i></p>
<dd>An IN/OUT parameter that contains any data that the callback procedure produces as a result of the conversion. The initial value is NULL. If the callback procedure sets this member, it must ensure that the <i>type</i>, <i>format</i>, and <i>length</i> members correspond to the data in <i>value</i>. The callback procedure is responsible for allocating, but not for freeing, memory when it sets this member.</p>
<dt><i>type</i></p>
<dd>An IN/OUT parameter that indicates the type of the data in the <i>value</i> member. The initial value is <code>INTEGER</code>.</p>
<dt><i>format</i></p>
<dd>An IN/OUT parameter that specifies whether the data in <i>value</i> should be viewed as a list of <i>char</i>, <i>short</i>, or <i>long</i> quantities. The initial value is 8. The callback procedure can set this member to 8 (for a list of <i>char</i>), 16 (for a list of <i>short</i>), or 32 (for a list of <i>long</i>).</p>
<dt><i>length</i></p>
<dd>An IN/OUT member that specifies the number of elements of data in <i>value</i>, where each element has the size symbolized by <i>format</i>. The initial value is 0 (zero).</dl>
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
<dd>Contains information about the location where data is to be transferred. The value is always NULL when the selection is <code>SECONDARY</code> or <code>CLIPBOARD</code>. If the value is NULL, the data is to be inserted at the widget&#8217;s cursor position. Otherwise, the value is a pointer to an <code>XPoint</code> structure containing the x and y coordinates at the location where the data is to be transferred. Once <code>XmTransferDone</code> procedures start to be called, <code>location_data</code> will no longer be stable.</p>
<dt><i>time</i></p>
<dd>Indicates the time when the transfer operation began.</dl>
<h3>Translations</h3>
<p>The <code>XmContainer</code> translations are listed below. </p>
<p> The following key names are listed in the X standard key event translation table syntax. This format is the one used by Motif to specify the widget actions corresponding to a given key. A brief overview of the format is provided under <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3). For a complete description of the format, please refer to the X Toolkit Instrinsics Documentation.</p>
<dl COMPACT>
<dt><code>&asymp;c &asymp;s &asymp;m &asymp;a</code> <code>&lt;Btn1Down&gt;</code>:</p>
<dd>ContainerBeginSelect()</p>
<dt><code>&lt;Btn1Motion&gt;</code>:</p>
<dd>ContainerButtonMotion()</p>
<dt><code>&asymp;c &asymp;s &asymp;m &asymp;a</code> <code>&lt;Btn1Up&gt;</code>:</p>
<dd>ContainerEndSelect()</p>
<dt><code>c &asymp;s &asymp;m &asymp;a</code> <code>&lt;Btn1Down&gt;</code>:</p>
<dd>ContainerBeginToggle()</p>
<dt><code>c &asymp;s &asymp;m &asymp;a</code> <code>&lt;Btn1Up&gt;</code>:</p>
<dd>ContainerEndToggle()</p>
<dt><code>&asymp;c s &asymp;m &asymp;a</code> <code>&lt;Btn1Down&gt;</code>:</p>
<dd>ContainerBeginExtend()</p>
<dt><code>&asymp;c s &asymp;m &asymp;a</code> <code>&lt;Btn1Up&gt;</code>:</p>
<dd>ContainerEndExtend()</p>
<dt><code>c s &asymp;m &asymp;a</code> <code>&lt;Btn1Down&gt;</code>:</p>
<dd>ContainerBeginExtend()</p>
<dt><code>c s &asymp;m &asymp;a</code> <code>&lt;Btn1Up&gt;</code>:</p>
<dd>ContainerEndExtend()</p>
<dt><code>&asymp;c &asymp;s &asymp;m &asymp;a</code> <code>&lt;Btn2Down&gt;</code>:</p>
<dd>ContainerStartTransfer(<code>Copy</code>)</p>
<dt><code>c s &asymp;m &asymp;a</code> <code>&lt;Btn2Down&gt;</code>:</p>
<dd>ContainerStartTransfer(<code>Link</code>)</p>
<dt><code>&asymp;c s &asymp;m &asymp;a</code> <code>&lt;Btn2Down&gt;</code>:</p>
<dd>ContainerStartTransfer(<code>Move</code>)</p>
<dt><code>&asymp;m &asymp;a</code> <code>&lt;Btn2Up&gt;</code>:</p>
<dd>ContainerEndTransfer()</p>
<dt><code>:c s a</code> <code>&lt;Key&gt;</code><code>&lt;osfInsert&gt;</code>:</p>
<dd>ContainerPrimaryLink()</p>
<dt><code>:c s m</code> <code>&lt;Key&gt;</code><code>&lt;osfInsert&gt;</code>:</p>
<dd>ContainerPrimaryLink()</p>
<dt><code>:a</code> <code>&lt;Key&gt;</code><code>&lt;osfInsert&gt;</code>:</p>
<dd>ContainerPrimaryCopy()</p>
<dt><code>:m</code> <code>&lt;Key&gt;</code><code>&lt;osfInsert&gt;</code>:</p>
<dd>ContainerPrimaryCopy()</p>
<dt><code>:s a</code> <code>&lt;Key&gt;</code><code>&lt;osfDelete&gt;</code>:</p>
<dd>ContainerPrimaryMove()</p>
<dt><code>:s m</code> <code>&lt;Key&gt;</code><code>&lt;osfDelete&gt;</code>:</p>
<dd>ContainerPrimaryMove()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfCancel&gt;</code>:</p>
<dd>ContainerCancel()</p>
<dt><code>:s</code> <code>&lt;Key&gt;</code><code>&lt;osfSelect&gt;</code>:</p>
<dd>ContainerExtend()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfSelect&gt;</code>:</p>
<dd>ContainerSelect()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfSelectAll&gt;</code>:</p>
<dd>ContainerSelectAll()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfDeselectAll&gt;</code>:</p>
<dd>ContainerDeselectAll()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfAddMode&gt;</code>:</p>
<dd>ContainerToggleMode()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfActivate&gt;</code>:</p>
<dd>ContainerActivate()</p>
<dt><code>s &asymp;c &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>space</code>:</p>
<dd>ContainerExtend()</p>
<dt><code>&asymp;s &asymp;c &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>space</code>:</p>
<dd>ContainerSelect()</p>
<dt><code>&asymp;s &asymp;c &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>Return</code>:</p>
<dd>ContainerActivate()</p>
<dt><code>&asymp;s c &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>slash</code>:</p>
<dd>ContainerSelectAll()</p>
<dt><code>&asymp;s c &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>backslash</code>:</p>
<dd>ContainerDeselectAll()</p>
<dt><code>:c s</code> <code>&lt;Key&gt;</code><code>&lt;osfBeginLine&gt;</code>:</p>
<dd>ContainerExtendCursor(<code>First</code>)</p>
<dt><code>:c s</code> <code>&lt;Key&gt;</code><code>&lt;osfEndLine&gt;</code>:</p>
<dd>ContainerExtendCursor(<code>Last</code>)</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfBeginLine&gt;</code>:</p>
<dd>ContainerMoveCursor(<code>First</code>)</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfEndLine&gt;</code>:</p>
<dd>ContainerMoveCursor(<code>Last</code>)</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfLeft&gt;</code>:</p>
<dd>ContainerExpandOrCollapse(<code>Left</code>)</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfRight&gt;</code>:</p>
<dd>ContainerExpandOrCollapse(<code>Right</code>)</p>
<dt><code>:s</code> <code>&lt;Key&gt;</code><code>&lt;osfUp&gt;</code>:</p>
<dd>ContainerExtendCursor(<code>Up</code>)</p>
<dt><code>:s</code> <code>&lt;Key&gt;</code><code>&lt;osfDown&gt;</code>:</p>
<dd>ContainerExtendCursor(<code>Down</code>)</p>
<dt><code>:s</code> <code>&lt;Key&gt;</code><code>&lt;osfLeft&gt;</code>:</p>
<dd>ContainerExtendCursor(<code>Left</code>)</p>
<dt><code>:s</code> <code>&lt;Key&gt;</code><code>&lt;osfRight&gt;</code>:</p>
<dd>ContainerExtendCursor(<code>Right</code>)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfUp&gt;</code>:</p>
<dd>ContainerMoveCursor(<code>Up</code>)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfDown&gt;</code>:</p>
<dd>ContainerMoveCursor(<code>Down</code>)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfLeft&gt;</code>:</p>
<dd>ContainerMoveCursor(<code>Left</code>)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfRight&gt;</code>:</p>
<dd>ContainerMoveCursor(<code>Right</code>)</p>
<dt><code>s &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>Tab</code>:</p>
<dd>ManagerGadgetPrevTabGroup()</p>
<dt><code>&asymp;s &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>Tab</code>:</p>
<dd>ManagerGadgetNextTabGroup()</dl>
<p> The Container button event translations are modified when Display&#8217;s <code>XmNenableBtn1Transfer</code> resource does not have a value of <code>XmOFF</code> (in other words, it is either <code>XmBUTTON2_TRANSFER</code> or <code>XmBUTTON2_ADJUST</code>). This option allows the actions for selection and transfer to be integrated on <code>&lt;Btn1&gt;</code>, and the actions for extending the selection can be bound to <code>&lt;Btn2&gt;</code>. The actions for <code>&lt;Btn1&gt;</code> that are defined in the preceding list still apply when the <code>&lt;Btn1&gt;</code> event occurs over text that is not selected. The following actions apply when the <code>&lt;Btn1&gt;</code> event occurs over text that is selected:</p>
<dl COMPACT>
<dt><code>~c ~s ~m ~a</code> <code>&lt;Btn1Down&gt;</code><code>:</code></p>
<dd>ContainerHandleBtn1Down(<code>ContainerBeginSelect,Copy</code>)</p>
<dt><code>c ~s ~m ~a &lt;Btn1Down&gt;:</code></p>
<dd>ContainerHandleBtn1Down(<code>ContainerBeginToggle,Copy</code>)</p>
<dt><code>c s ~m ~a &lt;Btn1Down&gt;:</code></p>
<dd>ContainerHandleBtn1Down(<code>ContainerNoop,Link</code>)</p>
<dt><code>~c s ~m ~a &lt;Btn1Down&gt;:</code></p>
<dd>ContainerHandleBtn1Down(<code>ContainerBeginExtend,Move</code>)</p>
<dt><code>&lt;Btn1Motion&gt;</code><code>:</code></p>
<dd>ContainerHandleBtn1Motion(<code>ContainerButtonMotion</code>)</p>
<dt><code>~c ~s ~m ~a &lt;Btn1Up&gt;:</code></p>
<dd>ContainerHandleBtn1Up(<code>ContainerEndSelect</code>)</p>
<dt><code>c ~s ~m ~a &lt;Btn1Up&gt;:</code></p>
<dd>ContainerHandleBtn1Up(<code>ContainerEndToggle</code>)</p>
<dt><code>~c s ~m ~a &lt;Btn1Up&gt;:</code></p>
<dd>ContainerHandleBtn1Up(<code>ContainerEndExtend</code>)</p>
<dt><code>c s ~m ~a &lt;Btn1Down&gt;:</code></p>
<dd>ContainerHandleBtn1Down(<code>ContainerBeginExtend</code>)</p>
<dt><code>c s ~m ~a &lt;Btn1Up&gt;:</code></p>
<dd>ContainerHandleBtn1Up(<code>ContainerEndExtend</code>)</dl>
<p> When Display&#8217;s <code>XmNenableBtn1Transfer</code> resource has a value of <code>XmBUTTON2_ADJUST</code>, the following actions apply:</p>
<dl COMPACT>
<dt><code>~c ~s ~m ~a &lt;Btn2Down&gt;:</code></p>
<dd>ContainerHandleBtn2Down(<code>ContainerStartTransfer,Copy</code>)</p>
<dt><code>c s ~m ~a &lt;Btn2Down&gt;:</code></p>
<dd>ContainerHandleBtn2Down(<code>ContainerStartTransfer,Link</code>)</p>
<dt><code>~c s ~m ~a &lt;Btn2Down&gt;:</code></p>
<dd>ContainerHandleBtn2Down(<code>ContainerStartTransfer,Move</code>)</p>
<dt><code>&lt;Btn2Motion&gt;</code><code>:</code></p>
<dd>ContainerHandleBtn2Motion(<code>ContainerButtonMotion</code>)</p>
<dt><code>~m ~a &lt;Btn2Up&gt;:</code></p>
<dd>ContainerHandleBtn2Up(<code>ContainerEndTransfer</code>)</dl>
<h3>Action Routines</h3>
<p>The Container action routines are described below. The current selections are always shown with the background color specified by the <code>XmNselectColor</code> resource.</p>
<dl COMPACT>
<dt>ContainerActivate():</p>
<dd>This action calls <code>XmNdefaultActionCallback</code> with reason <code>XmCR_DEFAULT_ACTION</code>.</p>
<dt>ContainerBeginExtend():</p>
<dd>Simply returns if <code>XmNselectionPolicy</code> is <code>XmSINGLE_SELECT</code> or <code>XmBROWSE_SELECT</code>. Simply returns if <code>XmNlayoutType</code> is <code>XmSPATIAL</code>.</p>
<dd>Otherwise, this action sets the selection state of all items between the anchor item and the item under the pointer to the selection state of the anchor item. The location cursor is moved to the item under the pointer. If <code>XmNautomaticSelection</code> is <code>XmAUTO_SELECT</code>, the <code>XmNselectionCallback</code>(s) is called with either <code>XmCR_MULTIPLE_SELECT</code> or <code>XmCR_EXTENDED_SELECT</code> as the reason depending on <code>XmNselectionPolicy</code>, and with <code>auto_selection_type</code> <code>XmAUTO_CHANGE</code>.</p>
<dt>ContainerBeginSelect():</p>
<dd>If this is a second ContainerBeginSelect() action that has occurred within the time specified by the display&#8217;s multiclick time, this action calls <code>XmNdefaultActionCallback</code> with reason <code>XmCR_DEFAULT_ACTION</code> and returns.</p>
<dd>Otherwise, processing depends on the value of <code>XmNselectionPolicy</code> as follows:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmSINGLE_SELECT</code></p>
<dd>This action deselects all items and toggles the item (if any) under the pointer.</p>
<dt><code>XmBROWSE_SELECT</code></p>
<dd>This action deselects all items and toggles the item (if any) under the pointer. This item is now the anchor item for further selection. If <code>XmNautomaticSelection</code> is <code>XmAUTO_SELECT</code> and a change in any item&#8217;s selection state is made, the <code>XmNselectionCallback</code>(s) is called with reason <code>XmCR_BROWSE_SELECT</code> and <code>auto_selection_type</code> <code>XmAUTO_BEGIN</code>.</p>
<dt><code>XmMULTIPLE_SELECT</code></p>
<dd>If the pointer is over an item and <code>XmNselectionTechnique</code> is not <code>XmMARQUEE</code>, this action toggles the selection state of that item. The item becomes the anchor item for further selection. If <code>XmNselectionTechnique</code> is <code>XmMARQUEE</code>, <code>XmMARQUEE_EXTEND_START</code>, or <code>XmMARQUEE_EXTEND_BOTH</code>, this action sets the start point for the Marquee rectangle. If <code>XmNselectionTechnique</code> is <code>XmMARQUEE_EXTEND_START</code> or <code>XmMARQUEE_EXTEND_BOTH</code> and the pointer is over an item, this action draws the Marquee rectangle around the item. If <code>XmNautomaticSelection</code> is <code>XmAUTO_SELECT</code>, the <code>XmNselectionCallback</code>(s) is called with reason <code>XmCR_MULTIPLE_SELECT</code> and <code>auto_selection_type</code> <code>XmAUTO_BEGIN</code>.</p>
<dt><code>XmEXTENDED_SELECT</code></p>
<dd>All items are first deselected. Processing is then identical to the case where <code>XmNselectionPolicy</code> is <code>XmMULTIPLE_SELECT</code>, except that <code>XmCR_EXTENDED_SELECT</code> is the callback reason given if <code>XmNselectionCallback</code> is called.</dl>
</dl>
<dt>ContainerBeginToggle():</p>
<dd>Simply returns if <code>XmNselectionPolicy</code> is <code>XmSINGLE_SELECT</code> or <code>XmBROWSE_SELECT</code>.</p>
<dd>Otherwise, if the pointer is over an item and <code>XmNselectionTechnique</code> is not <code>XmMARQUEE</code>, this action toggles the selection state of that item. The item becomes the anchor item for further selection. If <code>XmNselectionTechnique</code> is <code>XmMARQUEE</code>, <code>XmMARQUEE_EXTEND_START</code>, or <code>XmMARQUEE_EXTEND_BOTH</code> this action sets the start point for the Marquee rectangle. If <code>XmNselectionTechnique</code> is <code>XmMARQUEE_EXTEND_START</code> or <code>XmMARQUEE_EXTEND_BOTH</code> and the pointer is over an item, this action draws the Marquee rectangle around the item. If <code>XmNautomaticSelection</code> is <code>XmAUTO_SELECT</code>, the <code>XmNselectionCallback</code>(s) is called with either <code>XmCR_MULTIPLE_SELECT</code> or <code>XmCR_EXTENDED_SELECT</code> as the reason, depending on <code>XmNselectionPolicy</code>, and with <code>auto_selection_type</code> <code>XmAUTO_BEGIN</code>.</p>
<dt>ContainerButtonMotion():</p>
<dd>Processing depends on the value of <code>XmNselectionPolicy</code>, as follows:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmSINGLE_SELECT</code></p>
<dd>This action simply returns to the caller.</p>
<dt><code>XmBROWSE_SELECT</code></p>
<dd>Simply returns if this action follows a ContainerBeginExtend() action or ContainerBeginToggle() action.</p>
<dd>If the pointer is no longer over the current anchor item, this action toggles the current anchor item and then toggles the item under the pointer (if any) and makes it the new anchor item for further processing. If <code>XmNautomaticSelection</code> is <code>XmAUTO_SELECT</code> and a change in any item&#8217;s selection state is made, the <code>XmNselectionCallback</code>(s) is called with reason <code>XmCR_BROWSE_SELECT</code> and <code>auto_selection_type</code> <code>XmAUTO_MOTION</code>.</p>
<dt><code>XmMULTIPLE_SELECT</code></p>
<dd>If a previous action has set a Marquee rectangle start point, this action draws the Marquee rectangle between the current pointer position and the Marquee start point. If the <code>XmNselectionTechnique</code> is <code>XmMARQUEE_EXTEND_BOTH</code> and the pointer is over an item, the end point of the Marquee rectangle is extended to include the item. The selection states of all items within the Marquee rectangle are toggled to match the state of the anchor item.</p>
<dd>If no Marquee rectangle start point is set and the pointer is over an item, processing depends on the <code>XmNlayoutType</code> resource. The anchor item from the previous action is used. If <code>XmNlayoutType</code> is <code>XmSPATIAL</code>, the selection state of the item under the pointer is toggled to match the selection state of the anchor item. If <code>XmNlayoutType</code> is <code>XmOUTLINE</code> or <code>XmDETAIL</code>, the selection state of all items between the anchor item and the item under the pointer are toggled to match the selection state of the anchor item.</p>
<dd>If <code>XmNautomaticSelection</code> is <code>XmAUTO_SELECT</code> and a change in any item&#8217;s selection state is made, the <code>XmNselectionCallback</code>(s) is called with reason <code>XmCR_MULTIPLE_SELECT</code> and <code>auto_selection_type</code> <code>XmAUTO_MOTION</code>.</p>
<dt><code>XmEXTENDED_SELECT</code></p>
<dd>Processing is identical to the case where <code>XmNselectionPolicy</code> is <code>XmMULTIPLE_SELECT</code>, except that <code>XmCR_EXTENDED_SELECT</code> is the callback reason given if <code>XmNselectionCallback</code> is called.</dl>
</dl>
<dt>ContainerCancel():</p>
<dd>If a selection is in progress, this action restores selection states of all items to their state before the selection began. If <code>XmNautomaticSelection</code> is True and a change in any item&#8217;s selection state is made, the <code>XmNselectionCallback</code> is called with reason <code>XmCR_BROWSE_SELECT</code>, <code>XmMULTIPLE_SELECT</code>, or <code>XmCR_EXTENDED_SELECT</code> depending on the <code>XmNselectionPolicy</code> resource and <code>auto_selection_type</code> <code>XmAUTO_CANCEL</code>.</p>
<dt>ContainerDeselectAll():</p>
<dd>This action deselects all items and calls <code>XmNselectionCallback</code> with reason depending on <code>XmNselectionPolicy</code>.</p>
<dt>ContainerEndExtend():</p>
<dd>Simply returns if <code>XmNselectionPolicy</code> is <code>XmSINGLE_SELECT</code> or <code>XmBROWSE_SELECT</code>. Simply returns if <code>XmNlayoutType</code> is <code>XmSPATIAL</code>.</p>
<dd>Otherwise, if <code>XmNautomaticSelection</code> is <code>XmNO_AUTO_SELECT</code>, <code>XmNselectionCallback</code>(s) is called with either <code>XmCR_MULTIPLE_SELECT</code> or <code>XmCR_EXTENDED_SELECT</code> as the reason depending on <code>XmNselectionPolicy</code>. If <code>XmNautomaticSelection</code> is <code>XmAUTO_SELECT</code> and no change is made in any item&#8217;s selection state by this action, <code>XmNselectionCallback</code>(s) is called with either <code>XmCR_MULTIPLE_SELECT</code> or <code>XmCR_EXTENDED_SELECT</code> as the reason depending on <code>XmNselectionPolicy</code> and <code>auto_selection_type</code> <code>XmAUTO_CHANGE</code>. If <code>XmNautomaticSelection</code> is <code>XmAUTO_SELECT</code> and this action makes no change in any item&#8217;s selection state, <code>XmNselectionCallback</code>(s) is called with either <code>XmCR_MULTIPLE_SELECT</code> or <code>XmCR_EXTENDED_SELECT</code> as the reason depending on <code>XmNselectionPolicy</code> and <code>auto_selection_type</code> <code>XmAUTO_NO_CHANGE</code>.</p>
<dt>ContainerEndSelect():</p>
<dd>Processing depends on the value of <code>XmNselectionPolicy</code>, as follows:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmSINGLE_SELECT</code></p>
<dd>This action calls <code>XmNselectionCallback</code> with reason <code>XmCR_SINGLE_SELECT</code>.</p>
<dt><code>XmBROWSE_SELECT</code></p>
<dd>If the pointer is no longer over the current anchor item, this action toggles the current anchor item and then toggles the item under the pointer (if any). If <code>XmNautomaticSelection</code> is <code>XmNO_AUTO_SELECT</code>, the <code>XmNselectionCallback</code>(s) is called with reason <code>XmCR_BROWSE_SELECT</code>. If <code>XmNautomaticSelection</code> is <code>XmAUTO_SELECT</code> and a change in any item&#8217;s selection state is made, <code>XmNselectionCallback</code>(s) is called with reason <code>XmCR_BROWSE_SELECT</code> and <code>auto_selection_type</code> <code>XmAUTO_CHANGE</code>. If <code>XmNautomaticSelection</code> is <code>XmAUTO_SELECT</code> and no change is made in any item&#8217;s selection state by this action, <code>XmNselectionCallback</code>(s) is called with reason <code>XmCR_BROWSE_SELECT</code> and <code>auto_selection_type</code> <code>XmAUTO_NO_CHANGE</code>.</p>
<dt><code>XmMULTIPLE_SELECT</code></p>
<dd>This action first performs the same processing as the ContainerButtonMotion() action, except that <code>XmNselectionCallback</code> is not called. If <code>XmNautomaticSelection</code> is <code>XmNO_AUTO_SELECT</code>, the <code>XmNselectionCallback</code>(s) is called with reason <code>XmCR_MULTIPLE_SELECT</code>. If <code>XmNautomaticSelection</code> is <code>XmAUTO_SELECT</code> and a change in any item&#8217;s selection state is made, the <code>XmNselectionCallback</code>(s) is called with reason <code>XmCR_MULTIPLE_SELECT</code> and <code>auto_selection_type</code> <code>XmAUTO_CHANGE</code>. If <code>XmNautomaticSelection</code> is <code>XmAUTO_SELECT</code> and this action makes no change in any item&#8217;s selection state, <code>XmNselectionCallback</code>(s) is called with reason <code>XmCR_MULTIPLE_SELECT</code> and <code>auto_selection_type</code> <code>XmAUTO_NO_CHANGE</code>.</p>
<dt><code>XmEXTENDED_SELECT</code></p>
<dd>This action first performs the same processing as the ContainerButtonMotion() action, except that <code>XmNselectionCallback</code> is not called. If <code>XmNautomaticSelection</code> is <code>XmNO_AUTO_SELECT</code>, the <code>XmNselectionCallback</code>(s) is called with reason <code>XmCR_EXTENDED_SELECT</code>. If <code>XmNautomaticSelection</code> is <code>XmAUTO_SELECT</code> and a change in any item&#8217;s selection state is made, <code>XmNselectionCallback</code>(s) is called with reason <code>XmCR_EXTENDED_SELECT</code> and <code>auto_selection_type</code> <code>XmAUTO_CHANGE</code>. If <code>XmNautomaticSelection</code> is <code>XmAUTO_SELECT</code> and this action makes no change in any item&#8217;s selection state, <code>XmNselectionCallback</code>(s) is called with reason <code>XmCR_EXTENDED_SELECT</code> and <code>auto_selection_type</code> <code>XmAUTO_NO_CHANGE</code>.</dl>
</dl>
<dt>ContainerEndToggle():</p>
<dd>Simply returns if <code>XmNselectionPolicy</code> is <code>XmSINGLE_SELECT</code> or <code>XmBROWSE_SELECT</code>. If <code>XmNselectionPolicy</code> is <code>XmMULTIPLE_SELECT</code> or <code>XmEXTENDED_SELECT</code>, this action performs the same processing as the ContainerEndSelect() action.</p>
<dt>ContainerEndTransfer()::</p>
<dd>If the elapsed time since a ContainerStartTransfer() action has occurred exceeds the time span specified by the display&#8217;s multiclick time, this action returns.</p>
<dd>Otherwise, the ContainerPrimaryCopy(), ContainerPrimaryLink(), or ContainerPrimaryMove() action is invoked, depending on the value of the operation parameter saved by ContainerStartTransfer().</p>
<dt>ContainerExpandOrCollapse(<code>Left|Right|Collapse|Expand</code>):</p>
<dd>This action changes the value of the <code>XmNoutlineState</code> of the current focus widget. If the argument value is <code>Collapse</code> or <code>Left</code>, the <code>XmNoutlineState</code> resource value is set to <code>XmCOLLAPSED</code>. If the argument value is <code>Expand</code> or <code>Right</code>, the <code>XmNoutlineState</code> resource value is set to <code>XmEXPANDED</code>.</p>
<dd>If the argument is <code>Left</code> or <code>Right</code> and the layout is right to left, then the setting of the <code>XmNoutlineState</code> value is reversed from that described in the preceding paragraph.</p>
<dd>Simply returns if <code>XmNlayoutType</code> is <code>XmSPATIAL</code>.</p>
<dt>ContainerExtend():</p>
<dd>Processing depends on the value of <code>XmNselectionPolicy</code>, as follows:</p>
<dd>If the selection policy is <code>XmSINGLE_SELECT</code> or <code>XmBROWSE_SELECT</code>, this action returns. If <code>XmNlayoutType</code> is <code>XmSPATIAL</code>, this action returns.</p>
<dd>If the selection policy is <code>XmMULTIPLE_SELECT</code>, this action sets the selection state of all items between the anchor item and the location cursor to the selection state of the anchor item.</p>
<dd>If the selection policy is <code>XmEXTENDED_SELECT</code> and the Container is in Normal Mode, this action deselects all items and selects all items between the anchor item and the location cursor. If the selection policy is <code>XmEXTENDED_SELECT</code> and the Container is in Add Mode, this action sets the selection state of all items between the anchor item and the location cursor to the selection state of the anchor item.</p>
<dd><code>XmNselectionCallback</code> is called with reason <code>XmCR_MULTIPLE_SELECT</code> or <code>XmCR_EXTENDED_SELECT</code> depending on <code>XmNselectionPolicy</code>.</p>
<dt>ContainerExtendCursor(<code>Left|Right|Up|Down</code>):</p>
<dd>Processing depends on the value of <code>XmNselectionPolicy</code>, as follows:</p>
<dd>If the selection policy is <code>XmSINGLE_SELECT</code> or <code>XmBROWSE_SELECT</code>, this action returns. If <code>XmNlayoutType</code> is <code>XmSPATIAL</code>, this action returns.</p>
<dd>This action moves the location cursor one item in the indicated direction, if possible. If the value of the argument string is <code>First</code> or <code>Last</code>, this action moves the location cursor to the indicated item. For other values of the argument string, the location cursor is not affected.</p>
<dd>If the selection policy is <code>XmMULTIPLE_SELECT</code>, this action sets the selection state of all items between the anchor item and the location cursor to the selection state of the anchor item.</p>
<dd>If the selection policy is <code>XmEXTENDED_SELECT</code> and the Container is in Normal Mode, this action deselects all items and selects all items between the anchor item and the location cursor. If the selection policy is <code>XmEXTENDED_SELECT</code> and the Container is in Add Mode, this action sets the selection state of all items between the anchor item and the location cursor to the selection state of the anchor item.</p>
<dd><code>XmNselectionCallback</code> is called with reason <code>XmCR_MULTIPLE_SELECT</code> or <code>XmCR_EXTENDED_SELECT</code> depending on <code>XmNselectionPolicy</code>.</p>
<dt>ContainerHandleBtn1Down(<i>string</i><code>)</code></p>
<dd>When Display&#8217;s <code>XmNenableBtn1Transfer</code> resource is not <code>XmOFF</code>, the actions for selection and transfer are integrated on <code>&lt;Btn1&gt;</code>. If the pointer is over an unselected item or background, the item is first selected before the transfer is started. Otherwise, if the item is already selected, the transfer is started. The value of <i>string</i> can be one of the following actions:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd><code>ContainerBeginSelect,Copy</code></p>
<dt> &bull;</p>
<dd><code>ContainerBeginToggle,Copy</code></p>
<dt> &bull;</p>
<dd><code>ContainerNoop,Link</code></p>
<dt> &bull;</p>
<dd><code>ContainerBeginExtend,Move</code></dl>
</dl>
<dt>ContainerHandleBtn1Motion(<i>string</i><code>)</code></p>
<dd>When Display&#8217;s <code>XmNenableBtn1Transfer</code> resource is not <code>XmOFF</code>, the actions for selection and transfer are integrated on <code>&lt;Btn1&gt;</code>. When this action is invoked, and a selection is in progress, a drag is performed. Otherwise, the default action as specified in <i>string</i> is performed. The value of <i>string</i> can be <code>ContainerButtonMotion</code>.</p>
<dt>ContainerHandleBtn1Up(<i>string</i><code>)</code></p>
<dd>If a Button 1 transfer was in progress, then when this action is invoked, that transfer is cancelled. Otherwise, the default action as specified in <i>string</i> is performed. The value of <i>string</i> can be one of the following actions:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd><code>ContainerEndSelect</code></p>
<dt> &bull;</p>
<dd><code>ContainerEndToggle</code></p>
<dt> &bull;</p>
<dd><code>ContainerEndExtend</code></dl>
</dl>
<dt>ContainerHandleBtn2Down(<i>string</i><code>)</code></p>
<dd>When Display&#8217;s <code>XmNenableBtn1Transfer</code> resource has a value of <code>XmBUTTON2_ADJUST</code>, the actions for extending selection are bound on <code>&lt;Btn2&gt;</code>. Otherwise, the action that is performed depends on the value of <i>string</i>, which can be one of the following actions:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd><code>ContainerStartTransfer,Copy</code></p>
<dt> &bull;</p>
<dd><code>ContainerStartTransfer,Link</code></p>
<dt> &bull;</p>
<dd><code>ContainerStartTransfer,Move</code></dl>
</dl>
<dt>ContainerHandleBtn2Motion(<i>string</i><code>)</code></p>
<dd>When Display&#8217;s <code>XmNenableBtn1Transfer</code> resource is not <code>XmBUTTON2_ADJUST</code>, and a selection is in progress, a drag is performed. Otherwise, the default action that is performed depends on the value of <i>string</i>, which can be <code>ContainerButtonMotion</code>.</p>
<dt>ContainerHandleBtn2Up(<i>string</i><code>)</code></p>
<dd>When Display&#8217;s <code>XmNenableBtn1Transfer</code> resource has a value of <code>XmBUTTON2_ADJUST</code>, this action ends an extend. Otherwise, the action that is performed depends on the value of <i>string</i>, which can be <code>ContainerEndTransfer</code>.</p>
<dt>ContainerMoveCursor(<code>Left|Right|Up|Down|First|Last</code>):</p>
<dd>If the argument is <code>Left</code>, <code>Right</code>, <code>Up</code>, or <code>Down</code>, this action moves the location cursor one item in the indicated direction, if possible. If the value of the argument string is <code>First</code> or <code>Last</code>, this action moves the location cursor to the indicated item. Any other arguments are ignored.</p>
<dd>If <code>XmNselectionPolicy</code> is <code>XmBROWSE_SELECT</code>, or if <code>XmNselectionPolicy</code> is <code>XmEXTENDED_SELECT</code> and the Container is in Normal Mode, this action deselects all items, selects the item at the location cursor, and calls <code>XmNselectionCallback</code> with the reason depending on <code>XmNselectionPolicy</code>.</p>
<dt>ContainerPrimaryCopy():</p>
<dd>This action requests that primary selection data be copied to the Container. This action calls the <code>XmNdestinationCallback</code> procedures for the <code>PRIMARY</code> selection and the <code>XmCOPY</code> operation. By default, the Container does not do any transfer, and copying the selection is the responsibility of the <code>XmNdestinationCallback</code> procedures.</p>
<dt>ContainerPrimaryLink():</p>
<dd>This action requests that primary selection data be linked to the Container. This action calls the <code>XmNdestinationCallback</code> procedures for the <code>PRIMARY</code> selection and the <code>XmLINK</code> operation. By default, the Container does not do any transfer, and linking the selection is the responsibility of the <code>XmNdestinationCallback</code> procedures.</p>
<dt>ContainerPrimaryMove():</p>
<dd>This action requests that primary selection data be copied to the Container and deleted from the primary source. This action calls the <code>XmNdestinationCallback</code> procedures for the <code>PRIMARY</code> selection and the <code>XmMOVE</code> operation. By default, the Container does not do any transfer, and moving the selection is the responsibility of the <code>XmNdestinationCallback</code> procedures. If the transfer is successful, this action then calls the selection owner&#8217;s <code>XmNconvertCallback</code> procedures for the <code>PRIMARY</code> selection and the <code>DELETE</code> target.</p>
<dt>ContainerSelect():</p>
<dd>Processing depends on the value of <code>XmNselectionPolicy</code>, as follows:</p>
<dd>If the selection policy is <code>XmSINGLE_SELECT</code> or <code>XmBROWSE_SELECT</code>, this action deselects all items and selects the item at the location cursor.</p>
<dd>If the selection policy is <code>XmMULTIPLE_SELECT</code>, this action toggles the selection state of the item at the location cursor. This item becomes the anchor item for further selections.</p>
<dd>If the selection policy is <code>XmEXTENDED_SELECT</code> and the Container is in Normal Mode, this action deselects all items and selects the item at the location cursor. If the selection policy is <code>XmEXTENDED_SELECT</code> and the Container is in Add Mode, this action toggles the selection state of the item at the location cursor. The selected/toggled item becomes the anchor item for further selections.</p>
<dd><code>XmNselectionCallback</code> is called with the reason depending on <code>XmNselectionPolicy</code>.</p>
<dt>ContainerSelectAll():</p>
<dd>If <code>XmNselectionPolicy</code> is <code>XmSINGLE_SELECT</code> or <code>XmBROWSE_SELECT</code>, this action deselects all items and selects the item at the location cursor position.</p>
<dd>If <code>XmNselectionPolicy</code> is <code>XmMULTIPLE_SELECT</code> or <code>XmEXTENDED_SELECT</code>, this action selects all items.</p>
<dd><code>XmNselectionCallback</code> is called with the reason depending on the value of <code>XmNselectionCallback</code>.</p>
<dt>ContainerStartTransfer(<code>Copy|Move|Link</code>):</p>
<dd>This action saves the event and the operation specified in the argument string for use by subsequent actions. If no ContainerEndTransfer() actions occur within the time span specified by the display&#8217;s multiclick time and if <code>XmNlayoutType</code> is <code>XmSPATIAL</code>, this action creates a DragContext and starts a drag transfer by using <i>string</i> to specify the transfer operation. If no argument string is specified, <code>Copy</code> is the default value.</p>
<dd>Unless default drag and drop behavior has been overridden by a <code>XmNconvertCallback</code> procedure, if the drop operation occurs within the Container, then the item(s) being dragged are relocated at the position of the drop operation. If the item targeted by the Drag operation is not in the selected state, then only that item is moved. If the item is in the selected state, however, all items in the selected state are moved.</p>
<dt>ContainerToggleMode():</p>
<dd>If <code>XmNselectionPolicy</code> is <code>XmEXTENDED_SELECT</code>, this action toggles the Container between Normal Mode and Add Mode.</dl>
<h3>Additional Behavior</h3>
<p>The Container widget has the following additional behavior:</p>
<dl COMPACT>
<dt><code>&lt;Btn1Down&gt;</code><code>(2+)</code></p>
<dd>If a button click is followed by another button click within the time span specified by the display&#8217;s multiclick time, the Container interprets that as a double-click and calls the <code>XmNdefaultActionCallback</code> callbacks.</p>
<dt><code>&lt;FocusIn&gt;</code>:</p>
<dd>If the focus policy is explicit, sets the focus and draws the location cursor.</p>
<dt><code>&lt;FocusOut&gt;</code>:</p>
<dd>If the focus policy is explicit, removes the focus and erases the location cursor.</dl>
<h3>Virtual Bindings</h3>
<p>The bindings for virtual keys are vendor specific. For information about bindings for virtual buttons and keys, see <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-composite/">Composite</a></code>(3), <code><a href="/docs/linux/man/3-constraint/">Constraint</a></code>(3), <code><a href="/docs/linux/man/3-core/">Core</a></code>(3), <code>XmContainerCopy</code>, <code>XmContainerCopyLink</code>, <code>XmContainerCut</code>, <code>XmContainerGetItemChildren</code>, <code>XmContainerPaste</code>, <code>XmContainerPasteLink</code>, <code><a href="/docs/linux/man/3-xmcontainerrelayout/">XmContainerRelayout</a></code>(3), <code><a href="/docs/linux/man/3-xmcontainerreorder/">XmContainerReorder</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatecontainer/">XmCreateContainer</a></code>(3), <code><a href="/docs/linux/man/3-xmcreateicongadget/">XmCreateIconGadget</a></code>(3), <code><a href="/docs/linux/man/3-xmicongadget/">XmIconGadget</a></code>(3), <code><a href="/docs/linux/man/3-xmmanager/">XmManager</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatecontainer/">XmVaCreateContainer</a></code>(3), and <code><a href="/docs/linux/man/3-xmvacreatemanagedcontainer/">XmVaCreateManagedContainer</a></code>(3).</p>
