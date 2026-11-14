---
title: "xmpanedwindow(3)"
name: "xmpanedwindow"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmpanedwindow/"
description: "XmPanedWindow — The PanedWindow widget class"
---

<p><code>XmPanedWindow</code> &#8212; The PanedWindow widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/PanedW.h&gt;</pre>
<h2>Description</h2>
<p>PanedWindow is a composite widget that lays out children in a vertically tiled format. Children appear in top-to-bottom fashion, with the first child inserted appearing at the top of the PanedWindow and the last child inserted appearing at the bottom. The PanedWindow grows to match the width of its widest child and all other children are forced to this width. The height of the PanedWindow is equal to the sum of the heights of all its children, the spacing between them, and the size of the top and bottom margins. </p>
<p> The user can also adjust the size of the panes. To facilitate this adjustment, a pane control sash is created for most children. The sash appears as a square box positioned on the bottom of the pane that it controls. The user can adjust the size of a pane by using the mouse or keyboard. </p>
<p> The PanedWindow is also a constraint widget, which means that it creates and manages a set of constraints for each child. You can specify a minimum and maximum size for each pane. The PanedWindow does not allow a pane to be resized below its minimum size or beyond its maximum size. Also, when the minimum size of a pane is equal to its maximum size, no control sash is presented for that pane or for the lowest pane. </p>
<p> The default <code>XmNinsertPosition</code> procedure for PanedWindow causes all panes to appear first in the <code>XmNchildren</code> list and all sashes to appear after the panes. For a pane child, it returns the value of <code>XmNpositionIndex</code> if one has been specified for the child. Otherwise, it returns the number of <i>panes</i> in the PanedWindow&#8217;s <code>XmNchildren</code> list. Other than the fact that all sashes appear after all panes, the insertion order of sashes is unspecified. This procedure also causes nonsash widgets to be inserted after other nonsash children but before any sashes. The behavior of PanedWindow is undefined if <code>XmNinsertPosition</code> is set to a procedure other than the default. </p>
<p> All panes and sashes in a PanedWindow must be tab groups. When a pane is inserted as a child of the PanedWindow, if the pane&#8217;s <code>XmNnavigationType</code> is not <code>XmEXCLUSIVE_TAB_GROUP</code>, PanedWindow sets it to <code>XmSTICKY_TAB_GROUP</code>.</p>
<h3>Descendants</h3>
<p>PanedWindow automatically creates for each paned window the descendants shown in the following table. An application can use <code>XtName</code> and the child list information to gain access to the named descendant. In addition, a user or an application can use the named descendant when specifying resource values. </p>
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
<td><code>Sash</code></td>
<td><code>subclass of</code> <code>XmPrimitive</code></td>
<td>sash
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
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
<td>dividing line between window panes
</td>
</tr>
<tr VALIGN=top>
<td>
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
<p>PanedWindow inherits behavior and resources from the <code>Core</code>, <code>Composite</code>, <code>Constraint</code>, and <code>XmManager</code> classes. </p>
<p> The class pointer is <code>xmPanedWindowWidgetClass</code>. </p>
<p> The class name is <code>XmPanedWindow</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmPanedWindow Resource Set</code>
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
<td>XmNmarginHeight</td>
<td>XmCMarginHeight</td>
<td>Dimension</td>
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
<td>XmNmarginWidth</td>
<td>XmCMarginWidth</td>
<td>Dimension</td>
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
<td>XmNorientation</td>
<td>XmCOrientation</td>
<td>unsigned char</td>
<td>XmVERTICAL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNrefigureMode</td>
<td>XmCBoolean</td>
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
<td>XmNsashHeight</td>
<td>XmCSashHeight</td>
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
<td>XmNsashIndent</td>
<td>XmCSashIndent</td>
<td>Position</td>
<td>-10</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNsashShadowThickness</td>
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
<td>XmNsashWidth</td>
<td>XmCSashWidth</td>
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
<td>XmNseparatorOn</td>
<td>XmCSeparatorOn</td>
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
<td>XmNspacing</td>
<td>XmCSpacing</td>
<td>Dimension</td>
<td>8</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
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
<dt><code>XmNmarginHeight</code></p>
<dd>Specifies the distance between the top and bottom edges of the PanedWindow and its children.</p>
<dt><code>XmNmarginWidth</code></p>
<dd>Specifies the distance between the left and right edges of the PanedWindow and its children.</p>
<dt><code>XmNorientation</code></p>
<dd>Specifies the layout as either vertical (with the <code>XmVERTICAL</code> value) or horizontal (with the <code>XmHORIZONTAL</code> value). In the vertical layout, the children are laid out in a vertically tiled format. In the horizontal layout, the children are laid out in a horizontal layout, with the sash moveable along the horizontal axis.</p>
<dt><code>XmNrefigureMode</code></p>
<dd>Determines whether the panes&#8217; positions are recomputed and repositioned when programmatic changes are being made to the PanedWindow. Setting this resource to True resets the children to their appropriate positions.</p>
<dt><code>XmNsashHeight</code></p>
<dd>Specifies the height of the sash.</p>
<dt><code>XmNsashIndent</code></p>
<dd>Specifies the horizontal placement of the sash along each pane. A positive value causes the sash to be offset from the near (left) side of the PanedWindow, and a negative value causes the sash to be offset from the far (right) side of the PanedWindow. If the offset is greater than the width of the PanedWindow minus the width of the sash, the sash is placed flush against the near side of the PanedWindow.</p>
<dd>Whether the placement actually corresponds to the left or right side of the PanedWindow depends on the <code>XmNlayoutDirection</code> resource of the widget.</p>
<dt><code>XmNsashShadowThickness</code></p>
<dd>Specifies the thickness of the shadows of the sashes.</p>
<dt><code>XmNsashWidth</code></p>
<dd>Specifies the width of the sash.</p>
<dt><code>XmNseparatorOn</code></p>
<dd>Determines whether a separator is created between each of the panes. Setting this resource to True creates a Separator at the midpoint between each of the panes.</p>
<dt><code>XmNspacing</code></p>
<dd>Specifies the distance between each child pane.</p>
<dd>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5> <code>XmPanedWindow Constraint Resource Set</code>
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
<td>XmNallowResize</td>
<td>XmCBoolean</td>
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
<td>XmNpaneMaximum</td>
<td>XmCPaneMaximum</td>
<td>Dimension</td>
<td>1000</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNpaneMinimum</td>
<td>XmCPaneMinimum</td>
<td>Dimension</td>
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
<td>XmNpositionIndex</td>
<td>XmCPositionIndex</td>
<td>short</td>
<td>XmLAST_POSITION</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNskipAdjust</td>
<td>XmCBoolean</td>
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
</table>
</table>
<dt><code>XmNallowResize</code></p>
<dd>Allows an application to specify whether the PanedWindow should allow a pane to request to be resized. This flag has an effect only after the PanedWindow and its children have been realized. If this flag is set to True, the PanedWindow tries to honor requests to alter the height of the pane. If False, it always denies pane requests to resize.</p>
<dt><code>XmNpaneMaximum</code></p>
<dd>Allows an application to specify the maximum size to which a pane may be resized. This value must be greater than the specified minimum.</p>
<dt><code>XmNpaneMinimum</code></p>
<dd>Allows an application to specify the minimum size to which a pane may be resized. This value must be greater than 0 (zero).</p>
<dt><code>XmNpositionIndex</code></p>
<dd>Specifies the position of the widget in its parent&#8217;s list of children (the list of pane children, not including sashes). The value is an integer that is no less than 0 (zero) and no greater than the number of children in the list at the time the value is specified. A value of 0 means that the child is placed at the beginning of the list. The value can also be specified as <code>XmLAST_POSITION</code> (the default), which means that the child is placed at the end of the list. Any other value is ignored. <code>XtGetValues</code> returns the position of the widget in its parent&#8217;s child list at the time of the call to <code>XtGetValues</code>.</p>
<dd>When a widget is inserted into its parent&#8217;s child list, the positions of any existing children that are greater than or equal to the specified widget&#8217;s <code>XmNpositionIndex</code> are increased by 1. The effect of a call to <code>XtSetValues</code> for <code>XmNpositionIndex</code> is to remove the specified widget from its parent&#8217;s child list, decrease by one the positions of any existing children that are greater than the specified widget&#8217;s former position in the list, and then insert the specified widget into its parent&#8217;s child list as described in the preceding sentence.</p>
<dt><code>XmNskipAdjust</code></p>
<dd>When set to True, this Boolean resource allows an application to specify that the PanedWindow should not automatically resize this pane.</dl>
<h3>Inherited Resources</h3>
<p>PanedWindow inherits behavior and resources from the superclasses described in the following tables. For a complete description of each resource, refer to the reference page for that superclass. </p>
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
<td>default procedure</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
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
<h3>Translations</h3>
<p><code>XmPanedWindow</code> inherits translations from <code>XmManager</code>. </p>
<p> The translations for sashes within the PanedWindow are described in the following table. </p>
<p> The following key names are listed in the X standard key event translation table syntax. This format is the one used by Motif to specify the widget actions corresponding to a given key. A brief overview of the format is provided under <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3). For a complete description of the format, please refer to the X Toolkit Instrinsics Documentation.</p>
<dl COMPACT>
<dt><code>&asymp;c &asymp;s &asymp;m &asymp;a</code> <code>&lt;Btn1Down&gt;</code>:</p>
<dd>SashAction(<code>Start</code>)</p>
<dt><code>&asymp;c &asymp;s &asymp;m &asymp;a</code> <code>&lt;Btn1Motion&gt;</code>:</p>
<dd>SashAction(<code>Move</code>)</p>
<dt><code>&asymp;c &asymp;s &asymp;m &asymp;a</code> <code>&lt;Btn1Up&gt;</code>:</p>
<dd>SashAction(<code>Commit</code>)</p>
<dt><code>&asymp;c &asymp;s &asymp;m &asymp;a</code> <code>&lt;Btn2Down&gt;</code>:</p>
<dd>SashAction(<code>Start</code>)</p>
<dt><code>&asymp;c &asymp;s &asymp;m &asymp;a</code> <code>&lt;Btn2Motion&gt;</code>:</p>
<dd>SashAction(<code>Move</code>)</p>
<dt><code>&asymp;c &asymp;s &asymp;m &asymp;a</code> <code>&lt;Btn2Up&gt;</code>:</p>
<dd>SashAction(<code>Commit</code>)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfActivate&gt;</code>:</p>
<dd>PrimitiveParentActivate()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfCancel&gt;</code>:</p>
<dd>PrimitiveParentCancel()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfHelp&gt;</code>:</p>
<dd>Help()</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfUp&gt;</code>:</p>
<dd>SashAction(<code>Key,LargeIncr,Up</code>)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfUp&gt;</code>:</p>
<dd>SashAction(<code>Key,DefaultIncr,Up</code>)</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfRight&gt;</code>:</p>
<dd>SashAction(<code>Key,LargeIncr,Right</code>)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfRight&gt;</code>:</p>
<dd>SashAction(<code>Key,DefaultIncr,Right</code>)</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfDown&gt;</code>:</p>
<dd>SashAction(<code>Key,LargeIncr,Down</code>)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfDown&gt;</code>:</p>
<dd>SashAction(<code>Key,DefaultIncr,Down</code>)</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfLeft&gt;</code>:</p>
<dd>SashAction(<code>Key,LargeIncr,Left</code>)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfLeft&gt;</code>:</p>
<dd>SashAction(<code>Key,DefaultIncr,Left</code>)</p>
<dt><code>&asymp;s &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>Return</code>:</p>
<dd>PrimitiveParentActivate()</p>
<dt><code>s &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>Tab</code>:</p>
<dd>PrevTabGroup()</p>
<dt><code>&asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>Tab</code>:</p>
<dd>NextTabGroup()</dl>
<h3>Action Routines</h3>
<p>The <code>XmPanedWindow</code> action routines are</p>
<dl COMPACT>
<dt>Help():</p>
<dd>Calls the callbacks for <code>XmNhelpCallback</code> if any exist. If there are no help callbacks for this widget, this action calls the help callbacks for the nearest ancestor that has them.</p>
<dt>NextTabGroup():</p>
<dd>Moves the keyboard focus to the next tab group. By default, each pane and sash is a tab group.</p>
<dt>PrevTabGroup():</p>
<dd>Moves the keyboard focus to the previous tab group. By default, each pane and sash is a tab group.</p>
<dt>SashAction(<i>action</i><code>)</code>&nbsp;<wbr>or SashAction(<code>Key,</code><i>increment</i><code>,</code><i>direction</i><code>)</code>:</p>
<dd>The <code>Start</code> action activates the interactive placement of the pane&#8217;s borders. The <code>Move</code> action causes the sash to track the position of the pointer. If one of the panes reaches its minimum or maximum size, adjustment continues with the next adjustable pane. The <code>Commit</code> action ends sash motion.</p>
<dd>When sash action is caused by a keyboard event, the sash with the keyboard focus is moved according to the <i>increment</i> and <i>direction</i> specified. <code>DefaultIncr</code> adjusts the sash by one line. <code>LargeIncr</code> adjusts the sash by one view region. The <i>direction</i> is specified as either <code>Up</code>, <code>Down</code>, <code>Left</code>, or <code>Right</code>.</p>
<dd>Note that the SashAction action routine is not a direct action routine of the <code>XmPanedWindow,</code> but rather an action of the Sash control created by the <code>XmPanedWindow</code>.</dl>
<h3>Additional Behavior</h3>
<p>This widget has the following additional behavior:</p>
<dl COMPACT>
<dt><code>&lt;FocusIn&gt;</code>:</p>
<dd>Moves the keyboard focus to the sash and highlights it</p>
<dt><code>&lt;FocusOut&gt;</code>:</p>
<dd>Unsets the keyboard focus in the sash and unhighlights it</dl>
<h3>Virtual Bindings</h3>
<p>The bindings for virtual keys are vendor specific. For information about bindings for virtual buttons and keys, see <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-composite/">Composite</a></code>(3), <code><a href="/docs/linux/man/3-constraint/">Constraint</a></code>(3), <code><a href="/docs/linux/man/3-core/">Core</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatepanedwindow/">XmCreatePanedWindow</a></code>(3), <code><a href="/docs/linux/man/3-xmmanager/">XmManager</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatepanedwindow/">XmVaCreatePanedWindow</a></code>(3), and <code><a href="/docs/linux/man/3-xmvacreatemanagedpanedwindow/">XmVaCreateManagedPanedWindow</a></code>(3).</p>
