---
title: "xmdrawingarea(3)"
name: "xmdrawingarea"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmdrawingarea/"
description: "XmDrawingArea — The DrawingArea widget class"
---

<p><code>XmDrawingArea</code> &#8212; The DrawingArea widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/DrawingA.h&gt;</pre>
<h2>Description</h2>
<p>DrawingArea is an empty widget that is easily adaptable to a variety of purposes. It does no drawing and defines no behavior except for invoking callbacks. Callbacks notify the application when graphics need to be drawn (exposure events or widget resize) and when the widget receives input from the keyboard or mouse. </p>
<p> Applications are responsible for defining appearance and behavior as needed in response to DrawingArea callbacks. </p>
<p> DrawingArea is also a composite widget and subclass of <code>XmManager</code> that supports minimal geometry management for multiple widget or gadget children. </p>
<p> DrawingArea uses the <code>XmNinitialFocus</code> resource of <code>XmManager</code> to define whether or not DrawingArea will receive focus when it is traversed to, even if it has traversable children. If <code>XmNinitialFocus</code> is NULL, DrawingArea receives focus only if it does not have any traversable children. If <code>XmNinitialFocus</code> is not NULL, then DrawingArea receives focus when traversed to. In the latter case, the application first needs to be able to realize that the DrawingArea will receive focus, then, as appropriate, needs to either call the <code>XmProcessTraversal</code> function for the desired child, or to navigate across the private DrawingArea graphics objects. </p>
<p> The following resources are not currently used by the DrawingArea widget: <code>XmNshadowThickness</code>, <code>XmNtopShadowPixmap</code>, <code>XmNbottomShadowPixmap</code>, <code>XmNtopShadowColor</code>, and <code>XmNbottomShadowColor</code></p>
<h3>Data Transfer Behavior</h3>
<p>DrawingArea has no widget class conversion or destination procedure. Subclasses and the <code>XmNconvertCallback</code> procedures are responsible for any conversion of selections. Subclasses and the <code>XmNdestinationCallback</code> procedures are responsible for any data transfers to the widget.</p>
<h3>Classes</h3>
<p>DrawingArea inherits behavior and resources from the <code>Core</code>, <code>Composite</code>, <code>Constraint</code>, and <code>XmManager</code> classes. </p>
<p> The class pointer is <code>xmDrawingAreaWidgetClass</code>. </p>
<p> The class name is <code>XmDrawingArea</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmDrawingArea Resource Set</code>
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
<td>XmNexposeCallback</td>
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
<td>XmNinputCallback</td>
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
<td>XmNresizeCallback</td>
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
</table>
</table>
<dl COMPACT>
<dt><code>XmNconvertCallback</code></p>
<dd>Specifies a list of callbacks called when the DrawingArea is asked to convert a selection. The type of the structure whose address is passed to these callbacks is <code>XmConvertCallbackStruct</code>. The reason is <code>XmCR_OK</code>.</p>
<dt><code>XmNdestinationCallback</code></p>
<dd>Specifies a list of callbacks called when the DrawingArea is the destination of a transfer operation. The type of the structure whose address is passed to these callbacks is <code>XmDestinationCallbackStruct</code>. The reason is <code>XmCR_OK</code>.</p>
<dt><code>XmNexposeCallback</code></p>
<dd>Specifies the list of callbacks that is called when DrawingArea receives an exposure event. The callback reason is <code>XmCR_EXPOSE</code>. The callback structure also includes the exposure event.</p>
<dd>The default bit gravity for Manager windows is <code>NorthWestGravity</code>. This may cause the <code>XmNexposeCallback</code> procedures not to be invoked when the DrawingArea window is made smaller.</p>
<dt><code>XmNinputCallback</code></p>
<dd>Specifies the list of callbacks that is called when the DrawingArea receives a keyboard or mouse event (key or button, up or down). The callback reason is <code>XmCR_INPUT</code>. The callback structure also includes the input event.</p>
<dt><code>XmNmarginHeight</code></p>
<dd>Specifies the minimum spacing in pixels between the top or bottom edge of DrawingArea and any child widget.</p>
<dt><code>XmNmarginWidth</code></p>
<dd>Specifies the minimum spacing in pixels between the left or right edge of DrawingArea and any child widget.</p>
<dt><code>XmNresizeCallback</code></p>
<dd>Specifies the list of callbacks that is called when the DrawingArea is resized. The callback reason is <code>XmCR_RESIZE</code>.</p>
<dt><code>XmNresizePolicy</code></p>
<dd>Controls the policy for resizing DrawingArea widgets. Possible values include <code>XmRESIZE_NONE</code> (fixed size), <code>XmRESIZE_ANY</code> (shrink or grow as needed), and <code>XmRESIZE_GROW</code> (grow only).</dl>
<h3>Inherited Resources</h3>
<p>DrawingArea inherits behavior and resources from the following superclasses. For a complete description of each resource, refer to the reference page for that superclass. </p>
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
<p>A pointer to the following structure is passed to the <code>XmNexposeCallback</code>, <code>XmNinputCallback</code>, and <code>XmNresizeCallback</code> procedures: </p>
<pre>typedef struct
{
 int <i>reason</i>;
 XEvent <i>* event</i>;
 Window <i>window</i>;
} XmDrawingAreaCallbackStruct;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked.</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the callback. This is NULL for the <code>XmNresizeCallback</code>.</p>
<dt><i>window</i></p>
<dd>Is set to the widget window.</dl>
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
<dd>Contains information about the location where data is to be transferred. The value is always NULL when the selection is <code>SECONDARY</code> or <code>CLIPBOARD</code>. If the value is NULL, the data is to be inserted at the widget&#8217;s cursor position. <code>location_data</code> is only valid for the duration of a transfer. Once <code>XmTransferDone</code> procedures start to be called, <code>location_data</code> will no longer be stable.</p>
<dt><i>time</i></p>
<dd>Indicates the time when the transfer operation began.</dl>
<h3>Translations</h3>
<p>XmDrawingArea inherits translations from XmManager. Before calling the XmManager actions, all events in the inherited translations except <code>&lt;BtnMotion&gt;</code>, <code>&lt;EnterWindow&gt;</code>, <code>&lt;LeaveWindow&gt;</code>, <code>&lt;FocusIn&gt;</code>, and <code>&lt;FocusOut&gt;</code> also call the DrawingAreaInput() action. </p>
<p> XmDrawingArea has the following additional translations. The following key names are listed in the X standard key event translation table syntax. This format is the one used by Motif to specify the widget actions corresponding to a given key. A brief overview of the format is provided under <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3). For a complete description of the format, please refer to the X Toolkit Instrinsics Documentation.</p>
<dl COMPACT>
<dt><code>&lt;BtnDown&gt;</code>:</p>
<dd>DrawingAreaInput()</p>
<dt><code>&lt;BtnUp&gt;</code>:</p>
<dd>DrawingAreaInput()</p>
<dt><code>&lt;KeyDown&gt;</code>:</p>
<dd>DrawingAreaInput() ManagerGadgetKeyInput()</p>
<dt><code>&lt;KeyUp&gt;</code>:</p>
<dd>DrawingAreaInput()</dl>
<h3>Action Routines</h3>
<p>The <code>XmDrawingArea</code> action routines are</p>
<dl COMPACT>
<dt>DrawingAreaInput():</p>
<dd>Unless the event takes place in a gadget, calls the callbacks for <code>XmNinputCallback</code></p>
<dt>ManagerGadgetKeyInput():</p>
<dd>Causes the current gadget to process a keyboard event</dl>
<h3>Additional Behavior</h3>
<p>The XmDrawingArea widget has the following additional behavior:</p>
<dl COMPACT>
<dt><code>&lt;Expose&gt;</code>:</p>
<dd>Calls the callbacks for <code>XmNexposeCallback</code></p>
<dt><code>&lt;Widget Resize&gt;</code>:</p>
<dd>Calls the callbacks for <code>XmNresizeCallback</code></dl>
<h3>Virtual Bindings</h3>
<p>The bindings for virtual keys are vendor specific. For information about bindings for virtual buttons and keys, see <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-composite/">Composite</a></code>(3), <code><a href="/docs/linux/man/3-constraint/">Constraint</a></code>(3), <code><a href="/docs/linux/man/3-core/">Core</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatedrawingarea/">XmCreateDrawingArea</a></code>(3), <code><a href="/docs/linux/man/3-xmmanager/">XmManager</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatedrawingarea/">XmVaCreateDrawingArea</a></code>(3), and <code><a href="/docs/linux/man/3-xmvacreatemanageddrawingarea/">XmVaCreateManagedDrawingArea</a></code>(3).</p>
