---
title: "xmscrolledwindow(3)"
name: "xmscrolledwindow"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmscrolledwindow/"
description: "XmScrolledWindow — The ScrolledWindow widget class"
---

<p><code>XmScrolledWindow</code> &#8212; The ScrolledWindow widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/ScrolledW.h&gt;</pre>
<h2>Description</h2>
<p>The ScrolledWindow widget combines one or two ScrollBar widgets and a viewing area to implement a visible window onto some other (usually larger) data display. The visible part of the window can be scrolled through the larger display by the use of ScrollBars. </p>
<p> To use ScrolledWindow, an application first creates a ScrolledWindow widget, any needed ScrollBar widgets, and a widget capable of displaying any desired data as the work area of ScrolledWindow. ScrolledWindow positions the work area widget and displays the ScrollBars if so requested. When the user performs some action on the ScrollBar, the application is notified through the normal ScrollBar callback interface. </p>
<p> ScrolledWindow can be configured to operate automatically so that it performs all scrolling and display actions with no need for application program involvement. It can also be configured to provide a minimal support framework in which the application is responsible for processing all user input and making all visual changes to the displayed data in response to that input. </p>
<p> When ScrolledWindow is performing automatic scrolling it creates a clipping window and automatically creates the scroll bars. Conceptually, this window becomes the viewport through which the user examines the larger underlying data area. The application simply creates the desired data, then makes that data the work area of the ScrolledWindow. When the user moves the slider to change the displayed data, the workspace is moved under the viewing area so that a new portion of the data becomes visible. </p>
<p> Sometimes it is impractical for an application to create a large data space and simply display it through a small clipping window. For example, in a text editor, creating a single data area that consisted of a large file would involve an undesirable amount of overhead. The application needs to use a ScrolledWindow (a small viewport onto some larger data), but needs to be notified when the user scrolls the viewport so it can bring in more data from storage and update the display area. For these cases, the ScrolledWindow can be configured so that it provides only visual layout support. No clipping window is created, and the application must maintain the data displayed in the work area, as well as respond to user input on the ScrollBars. </p>
<p> The user can specify resources in a resource file for the automatically created widgets that contain the horizontal and vertical scrollbars and the clipping area of the ScrolledWindow widget. The names of these widgets are <code>HorScrollBar</code>, <code>VertScrollBar</code>, and <code>ClipWindow</code> respectively, and remain consistent whether created by <code>XmCreateScrolledList</code>, <code>XmCreateScrolledText</code> or <code>XmCreateScrolledWindow</code>. </p>
<p> ScrolledWindow uses the <code>XmQTnavigator</code> trait, and holds the <code>XmQTscrollFrame</code> trait.</p>
<h3>Descendants</h3>
<p>ScrolledWindow automatically creates the descendants shown in the following table. An application can use <code>XtNameToWidget</code> to gain access to the named descendant. In addition, a user or an application can use the named descendant when specifying resource values. </p>
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
<td><code>VertScrollBar</code></td>
<td><code>XmScrollBar</code></td>
<td>vertical scroll bar
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>HorScrollBar</code></td>
<td><code>XmScrollBar</code></td>
<td>horizontal scroll bar
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>ClipWindow</code></td>
<td><code>XmClipWindow</code></td>
<td>clip window
</td>
</tr>
<tr VALIGN=top>
<td>
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
<p>ScrolledWindow inherits behavior, resources, and traits from <code>Core</code>, <code>Composite</code>, <code>Constraint</code>, and <code>XmManager</code>. </p>
<p> The class pointer is <code>xmScrolledWindowWidgetClass</code>. </p>
<p> The class name is <code>XmScrolledWindow</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmScrolledWindow Resource Set</code>
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
<td>XmNautoDragModel</td>
<td>XmCAutoDragModel</td>
<td>XtEnum</td>
<td>XmAUTO_DRAG_ENABLED</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNclipWindow</td>
<td>XmCClipWindow</td>
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
<td>XmNhorizontalScrollBar</td>
<td>XmCHorizontalScrollBar</td>
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
<td>XmNscrollBarDisplayPolicy</td>
<td>XmCScrollBarDisplayPolicy</td>
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
<td>XmNscrollBarPlacement</td>
<td>XmCScrollBarPlacement</td>
<td>unsigned char</td>
<td>XmBOTTOM_RIGHT</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNscrolledWindowMarginHeight</td>
<td>XmCScrolledWindowMarginHeight</td>
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
<td>XmNscrolledWindowMarginWidth</td>
<td>XmCScrolledWindowMarginWidth</td>
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
<td>XmNscrollingPolicy</td>
<td>XmCScrollingPolicy</td>
<td>unsigned char</td>
<td>XmAPPLICATION_DEFINED</td>
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
<td>XmNtraverseObscuredCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
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
<td>XmNverticalScrollBar</td>
<td>XmCVerticalScrollBar</td>
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
<td>XmNvisualPolicy</td>
<td>XmCVisualPolicy</td>
<td>unsigned char</td>
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
<td>XmNworkWindow</td>
<td>XmCWorkWindow</td>
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
</table>
</table>
<dl COMPACT>
<dt><code>XmNautoDragModel</code></p>
<dd>Indicates whether automatic drag is enabled (<code>XmAUTO_DRAG_ENABLED</code> or disabled (<code>XmAUTO_DRAG_DISABLED</code>). By default it is enabled.</p>
<dt><code>XmNclipWindow</code></p>
<dd>Specifies the widget ID of the clipping area. This is automatically created by ScrolledWindow when the <code>XmNvisualPolicy</code> resource is set to <code>XmCONSTANT</code> and can only be read by the application. Any attempt to set this resource to a new value causes a warning message to be printed by the scrolled window. If the <code>XmNvisualPolicy</code> resource is set to <code>XmVARIABLE</code>, this resource is set to NULL, and no clipping window is created.</p>
<dt><code>XmNhorizontalScrollBar</code></p>
<dd>Specifies the widget ID of the horizontal ScrollBar. This is automatically created by ScrolledWindow when the <code>XmNscrollingPolicy</code> is initialized to <code>XmAUTOMATIC</code>; otherwise, the default is NULL.</p>
<dt><code>XmNscrollBarDisplayPolicy</code></p>
<dd>Controls the automatic placement of the ScrollBars. If it is set to <code>XmAS_NEEDED</code> and if <code>XmNscrollingPolicy</code> is set to <code>XmAUTOMATIC</code>, ScrollBars are displayed only if the workspace exceeds the clip area in one or both dimensions. A resource value of <code>XmSTATIC</code> causes the ScrolledWindow to display the ScrollBars whenever they are managed, regardless of the relationship between the clip window and the work area. This resource must be <code>XmSTATIC</code> when <code>XmNscrollingPolicy</code> is <code>XmAPPLICATION_DEFINED</code>. The default is <code>XmAS_NEEDED</code> when <code>XmNscrollingPolicy</code> is <code>XmAUTOMATIC</code>, and <code>XmSTATIC</code> otherwise.</p>
<dt><code>XmNscrollBarPlacement</code></p>
<dd>Specifies the positioning of the ScrollBars in relation to the work window. The values are</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmTOP_LEFT</code></p>
<dd>The horizontal ScrollBar is placed above the work window; the vertical ScrollBar to is placed the left.</p>
<dt><code>XmBOTTOM_LEFT</code></p>
<dd>The horizontal ScrollBar is placed below the work window; the vertical ScrollBar to is placed the left.</p>
<dt><code>XmTOP_RIGHT</code></p>
<dd>The horizontal ScrollBar is placed above the work window; the vertical ScrollBar to is placed the right.</p>
<dt><code>XmBOTTOM_RIGHT</code></p>
<dd>The horizontal ScrollBar is placed below the work window; the vertical ScrollBar to is placed the right.</dl>
</dl>
<dd>The default value depends on the value of the <code>XmNlayoutDirection</code> resource of the widget.</p>
<dt><code>XmNscrolledWindowMarginHeight</code></p>
<dd>Specifies the margin height on the top and bottom of the ScrolledWindow. In order to use the autoscroll drag feature of the Motif drag and drop facility, a user must be able to hold a drag icon over the margin of a scrolled window. Though drag and drop will work with the default margin size of zero, a user may find it difficult to position the icon precisely enough to use the feature easily. The application programmer should ensure that the window margins are set to an adequate size, if the use of the autoscroll drag feature is desired.</p>
<dt><code>XmNscrolledWindowMarginWidth</code></p>
<dd>Specifies the margin width on the right and left sides of the ScrolledWindow. Please refer to the warning concerning the default margin size for the <code>XmNscrolledWindowMarginHeight</code> resource, above.</p>
<dt><code>XmNscrollingPolicy</code></p>
<dd>Performs automatic scrolling of the work area with no application interaction. If the value of this resource is <code>XmAUTOMATIC</code>, ScrolledWindow automatically creates the ScrollBars; attaches callbacks to the ScrollBars; sets the visual policy to <code>XmCONSTANT</code>; and automatically moves the work area through the clip window in response to any user interaction with the ScrollBars. An application can also add its own callbacks to the ScrollBars. This allows the application to be notified of a scroll event without having to perform any layout procedures.</p>
<dd><code>NOTE</code>: Since the ScrolledWindow adds callbacks to the ScrollBars, an application should not perform an <code>XtRemoveAllCallbacks</code> on any of the ScrollBar widgets.</p>
<dd>When <code>XmNscrollingPolicy</code> is set to <code>XmAPPLICATION_DEFINED</code>, the application is responsible for all aspects of scrolling. The ScrollBars must be created by the application, and it is responsible for performing any visual changes in the work area in response to user input.</p>
<dd>This resource must be set to the desired policy at the time the ScrolledWindow is created. It cannot be changed through <code>SetValues</code>.</p>
<dt><code>XmNspacing</code></p>
<dd>Specifies the distance that separates the ScrollBars from the work window.</p>
<dt><code>XmNtraverseObscuredCallback</code></p>
<dd>Specifies a list of callbacks that is called when traversing to a widget or gadget that is obscured due to its position in the work area relative to the location of the ScrolledWindow viewport. This resource is valid only when <code>XmNscrollingPolicy</code> is <code>XmAUTOMATIC</code>. If this resource is NULL, an obscured widget cannot be traversed to. The callback reason is <code>XmCR_OBSCURED_TRAVERSAL</code>.</p>
<dt><code>XmNverticalScrollBar</code></p>
<dd>Specifies the widget ID of the vertical ScrollBar. This is automatically created by ScrolledWindow when the <code>XmNscrollingPolicy</code> is initialized to <code>XmAUTOMATIC</code>; otherwise, the default is NULL.</p>
<dt><code>XmNvisualPolicy</code></p>
<dd>Enlarges the ScrolledWindow to match the size of the work area. It can also be used as a static viewport onto a larger data space. If the visual policy is <code>XmVARIABLE</code>, the ScrolledWindow forces the ScrollBar display policy to <code>XmSTATIC</code> and allows the work area to grow or shrink at any time and adjusts its layout to accommodate the new size. When the policy is <code>XmCONSTANT</code>, the work area grows or shrinks as requested, but a clipping window forces the size of the visible portion to remain constant. The only time the viewing area can grow is in response to a resize from the ScrolledWindow&#8217;s parent. The default is <code>XmCONSTANT</code> when <code>XmNscrollingPolicy</code> is <code>XmAUTOMATIC</code>, and <code>XmVARIABLE</code> otherwise.</p>
<dd><code>NOTE</code>: This resource must be set to the desired policy at the time the ScrolledWindow is created. It cannot be changed through <code>SetValues</code>.</p>
<dt><code>XmNworkWindow</code></p>
<dd>Specifies the widget ID of the viewing area. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5> <code>XmScrolledWindow Constraint Resource Set</code>
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
<td>XmNscrolledWindowChildType</td>
<td>XmCScrolledWindowChildType</td>
<td>unsigned char</td>
<td>RESOURCE_DEFAULT</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
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
<dt><code>XmNscrolledWindowChildType</code></p>
<dd>Specifies what the child is. ScrolledWindow supports a number of child types. The possible values are:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmWORK_AREA</code></p>
<dd>Indicates a work area child. This specifies that both ScrollBars are limited to moving the child inside the clipping window. If the scrolling policy is <code>XmAUTOMATIC</code>, the work area child can move in both directions.</p>
<dt><code>XmHOR_SCROLLBAR</code></p>
<dd>Indicates a horizontal child widget; the child must have the <code>XmQTnavigator</code> trait installed. For example, the <code>XmScrollBar</code> widget has the <code>XmQTnavigator</code> trait installed.</p>
<dt><code>XmVERT_SCROLLBAR</code></p>
<dd>Indicates a vertical child widget; the child must have the <code>XmQTnavigator</code> trait installed.</p>
<dt><code>XmSCROLL_HOR</code></p>
<dd>Indicates that only the horizontal ScrollBar moves the child. This value is only meaningful if the scrolling policy is <code>XmAUTOMATIC</code>.</p>
<dt><code>XmSCROLL_VERT</code></p>
<dd>Indicates that only the vertical ScrollBar moves the child. This value is only meaningful if the scrolling policy is <code>XmAUTOMATIC</code>.</p>
<dt><code>XmNO_SCROLL</code></p>
<dd>Indicates that the child does not move with the ScrollBars. This value is only meaningful if the scrolling policy is <code>XmAUTOMATIC</code>.</dl>
</dl>
</dl>
<h3>Inherited Resources</h3>
<p>ScrolledWindow inherits behavior and resources from the superclasses described in the following tables. For a complete description of each resource, refer to the reference page for that superclass. </p>
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
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
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
<p>The application must use the ScrollBar callbacks to be notified of user input. </p>
<p> ScrolledWindow defines a callback structure for use with <code>XmNtraverseObscuredCallback</code> callbacks. The <code>XmNtraverseObscuredCallback</code> resource provides a mechanism for traversal to obscured widgets (or gadgets) due to their position in the work area of a ScrolledWindow. The <code>XmNtraverseObscuredCallback</code> routine has responsibility for adjusting the position of the work area such that the specified traversal destination widget is positioned within the viewport of the ScrolledWindow. A NULL <code>XmNtraverseObscuredCallback</code> resource causes obscured widgets within the ScrolledWindow to be nontraversable. </p>
<p> Traversal to an obscured widget or gadget requires these conditions to be met: the widget or gadget can be obscured only due to its position in the work area of a ScrolledWindow relative to the viewport; the viewport of the associated ScrolledWindow is fully visible, or can be made so by virtue of ancestral <code>XmNtraverseObscuredCallback</code> routines; and the <code>XmNtraverseObscuredCallback</code> resource must be non-NULL. </p>
<p> When ScrolledWindow widgets are nested, the <code>XmNtraverseObscuredCallback</code> routine for each ScrolledWindow that obscures the traversal destination is called in ascending order within the given hierarchy. </p>
<p> A pointer to the following structure is passed to callbacks for <code>XmNtraverseObscuredCallback</code>. </p>
<pre>typedef struct
{
 int <i>reason</i>;
 XEvent *<i>event</i>:
 Widget <i>traversal_destination</i>;
 XmTraversalDirection <i>direction</i>;
} XmTraverseObscuredCallbackStruct;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked.</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the callback.</p>
<dt><i>traversal_destination</i></p>
<dd>Specifies the widget or gadget to traverse to, which will be a descendant of the work window.</p>
<dt><i>direction</i></p>
<dd>Specifies the direction of traversal. See the description of the <i>direction</i> parameter in the <code>XmProcessTraversal</code> reference page for an explanation of the valid values.</dl>
<h3>Translations</h3>
<p><code>XmScrolledWindow</code> includes the translations from <code>XmManager</code>.</p>
<h3>Additional Behavior</h3>
<p>This widget has the following additional behavior:</p>
<dl COMPACT>
<dt><code>&lt;Key&gt;</code><code>&lt;osfPageUp&gt;</code>:</p>
<dd>If <code>XmNscrollingPolicy</code> is <code>XmAUTOMATIC</code>, scrolls the window up the height of the viewport. The distance scrolled may be reduced to provide some overlap. The actual distance scrolled depends on the <code>XmNpageIncrement</code> resource of the vertical ScrollBar.</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfPageDown&gt;</code>:</p>
<dd>If <code>XmNscrollingPolicy</code> is <code>XmAUTOMATIC</code>, scrolls the window down the height of the viewport. The distance scrolled may be reduced to provide some overlap. The actual distance scrolled depends on the <code>XmNpageIncrement</code> resource of the vertical ScrollBar.</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfPageLeft&gt;</code>:</p>
<dd>If <code>XmNscrollingPolicy</code> is <code>XmAUTOMATIC</code>, scrolls the window left the width of the viewport. The distance scrolled may be reduced to provide some overlap. The actual distance scrolled depends on the <code>XmNpageIncrement</code> resource of the horizontal ScrollBar.</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfPageRight&gt;</code>:</p>
<dd>If <code>XmNscrollingPolicy</code> is <code>XmAUTOMATIC</code>, scrolls the window right the width of the viewport. The distance scrolled may be reduced to provide some overlap. The actual distance scrolled depends on the <code>XmNpageIncrement</code> resource of the horizontal ScrollBar.</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfBeginLine&gt;</code>:</p>
<dd>If <code>XmNscrollingPolicy</code> is <code>XmAUTOMATIC</code>, scrolls the window horizontally to the edge corresponding to the horizontal ScrollBar&#8217;s minimum value.</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfEndLine&gt;</code>:</p>
<dd>If <code>XmNscrollingPolicy</code> is <code>XmAUTOMATIC</code>, scrolls the window horizontally to the edge corresponding to the horizontal ScrollBar&#8217;s maximum value.</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfBeginData&gt;</code>:</p>
<dd>If <code>XmNscrollingPolicy</code> is <code>XmAUTOMATIC</code>, scrolls the window vertically to the edge corresponding to the vertical ScrollBar&#8217;s minimum value.</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfEndData&gt;</code>:</p>
<dd>If <code>XmNscrollingPolicy</code> is <code>XmAUTOMATIC</code>, scrolls the window vertically to the edge corresponding to the vertical ScrollBar&#8217;s maximum value.</dl>
<p> Certain applications will want to replace the page bindings with ones that are specific to the content of the scrolled area.</p>
<h3>Virtual Bindings</h3>
<p>The bindings for virtual keys are vendor specific. For information about bindings for virtual buttons and keys, see <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-composite/">Composite</a></code>(3), <code><a href="/docs/linux/man/3-constraint/">Constraint</a></code>(3), <code><a href="/docs/linux/man/3-core/">Core</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatescrolledwindow/">XmCreateScrolledWindow</a></code>(3), <code><a href="/docs/linux/man/3-xmmanager/">XmManager</a></code>(3), <code><a href="/docs/linux/man/3-xmprocesstraversal/">XmProcessTraversal</a></code>(3), <code><a href="/docs/linux/man/3-xmscrollbar/">XmScrollBar</a></code>(3), <code><a href="/docs/linux/man/3-xmscrollvisible/">XmScrollVisible</a></code>(3), <code><a href="/docs/linux/man/3-xmscrolledwindowsetareas/">XmScrolledWindowSetAreas</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatescrolledwindow/">XmVaCreateScrolledWindow</a></code>(3), and <code><a href="/docs/linux/man/3-xmvacreatemanagedscrolledwindow/">XmVaCreateManagedScrolledWindow</a></code>(3).</p>
