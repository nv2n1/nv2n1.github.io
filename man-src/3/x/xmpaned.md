---
title: "xmpaned(3)"
name: "xmpaned"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmpaned/"
description: "XmPaned — The Paned widget class"
---

<p><code>XmPaned</code> &#8212; The Paned widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Paned.h&gt;</pre>
<h2>Description</h2>
<p>The Paned widget manages children in a vertically or horizontally tiled fashion with each child in a separate pane. The panes may be dynamically resized by the user using &quot;control sashes&quot; that appear between the panes. </p>
<p> Application programmers have control over whether or not sashes and separators are displayed, the preferred size of each pane, and which pane will be forced to absorb size restrictions imposed by the Paned widget&#8217;s parent.</p>
<h3>Geometry Management</h3>
<p>The Paned widget usually resizes its children to their preferred sizes when a new child is managed. It will first attempt to resize itself to contain its panes exactly. If this is not possible then it will hunt through the children, from bottom to top (or right to left), for a pane to resize. </p>
<p> The Paned widget will attempt to honor the geometry request of its children. It will first attempt to resize itself to satisfy the request then go through the layout rules below to satisfy the request. Only if all panes are at their min/max values will a geometry request be refused. If the XmNallowResize resource is False for the child then all geometry requests will be denied,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>of course.</p>
<h3>Special Considerations</h3>
<p>When a user resizes a pane with the sashes, the Paned widget assumes that this new size is the preferred size of both the pane above and the pane below, unless the XmNresizeToPreferred constraint resource is True for that pane.</p>
<h3>Layout Semantics</h3>
<p>In order to make effective use of the Paned widget it is helpful to know the rules it uses to determine which child will be resized in any given situation. There are three rules used to determine which child is resized. While these rules are always the same, the panes that are searched can change depending upon what caused the change of layout.</p>
<h3>Layout Rules</h3>
<dl COMPACT>
<dd>1. Do not let a pane grow larger than its max or smaller than its min size. In addition do not let a pane without a sash shrink below its preferred size due to a grip movement of another pane.</p>
<dd>2. Do not adjust panes with XmNskipAdjust set.</p>
<dd>3. Do not adjust panes away from their preferred size, although moving one closer to its preferred size is fine.</dl>
<p> When searching the children the Paned widget looks for panes that satisfy all the rules, and if unsuccessful then it eliminates rule 3 and then 2. Rule 1 is always enforced. </p>
<p> If the relayout is due to a resize or change in management then the panes are searched from bottom to top. If space is needed above the current sash the panes are searched from bottom to top beginning with the second pane above the grip that was moved. If space is needed below the current sash the panes are searched from top to bottom beginning with the second pane below the grip that was moved. The Paned widget never wraps its pane resizing. Therefore if space is needed below the sash then no widget above the sash will ever be resized. </p>
<p> Note: If the orientation is horizontal then substitute &quot;right&quot; for &quot;bottom&quot; and &quot;left&quot; for &quot;top&quot; in the above paragraph.</p>
<h3>Resizing Panes</h3>
<p>When the Paned widget is resized it must determine a new size for each pane. There are two methods of doing this. The Paned widget can either give each pane its preferred size and then resize the panes to fit, or it can use the current sizes and then resize the panes to fit. The XmNresizeToPreferred constraint resource allows the application to tell the Paned widget whether to query the child about its preferred size (subject to the XmNpreferredPaneSize) or to use the current size when refiguring the pane locations after the Paned widget has been resized. </p>
<p> All panes assume they should resize to their preferred size until the Paned widget becomes visible to the user. </p>
<h3>Classes</h3>
<p>Paned inherits behavior and resources from the <code>Core</code>, <code>Composite</code>, <code>Constraint</code>, abd <code>Xmmanager</code> classes. </p>
<p> The class pointer of <code>xmPanedWidgetClass</code>. </p>
<p> The class name is <code>XmPaned</code>.</p>
<h3>New resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmPaned Resource Set</code>
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
<td>XmNcursor</td>
<td>XmCursor</td>
<td>tCursor</td>
<td>None</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
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
<td>XmNsashTranslations%Translations%XtTranslations%see below</td>
<td></td>
<td></td>
<td></td>
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
<td>
<hr>
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
<dt><code>XmNcursor</code></p>
<dd>Image that will be displayed as the pointer cursor whenever the pointer is over this widget. If the children do not explicitly set their cursor attribute then this resource will be inherited by each child.</p>
<dt><code>XmNmarginHeight</code></p>
<dd>Specifies the distance between the top and bottom edges of the Paned widget and its children.</p>
<dt><code>XmNmarginWidth</code></p>
<dd>Specifies the distance between the left and right edges of the Paned widget and its children.</p>
<dt><code>XmNorientation</code></p>
<dd>Specifies the layout as either vertical (with the <code>XmVERTICAL</code> value) or horizontal (with the <code>XmHORIZONTAL</code> value). In the vertical layout, the children are laid out in a vertically tiled format. In the horizontal layout, the children are laid out in a horizontal layout, with the sash moveable along the horizontal axis.</p>
<dt><code>XmNrefigureMode</code></p>
<dd>Determines whether the panes&#8217; positions are recomputed and repositioned when programmatic changes are being made to the Paned widget. Setting this resource to True resets the children to their appropriate positions.</p>
<dt><code>XmNsashHeight</code></p>
<dd>Specifies the height of the sash.</p>
<dt><code>XmNsashIndent</code></p>
<dd>Specifies the horizontal placement of the sash along each pane. A positive value causes the sash to be offset from the near (left) side of the Paned widget, and a negative value causes the sash to be offset from the far (right) side of the Paned widget. If the offset is greater than the width of the Paned widget minus the width of the sash, the sash is placed flush against the near side of the Paned widget.</p>
<dd>Whether the placement actually corresponds to the left or right side of the Paned widget depends on the <code>XmNlayoutDirection</code> resource of the widget.</p>
<dt><code>XmNsashTranslations</code></p>
<dd>Translation bindings for the sash. See below.</p>
<dt><code>XmNsashShadowThickness</code></p>
<dd>Specifies the thickness of the shadows of the sashes.</p>
<dt><code>XmNsashWidth</code></p>
<dd>Specifies the width of the sash.</p>
<dt><code>XmNseparatorOn</code></p>
<dd>Determines whether a separator is created between each of the panes. Setting this resource to True creates a Separator at the midpoint between each of the panes.</p>
<dt><code>XmNspacing</code></p>
<dd>Specifies the distance between each child pane. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5> <code>XmPaned Constraint Resource Set</code>
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
<tr VALIGN=top>
<td>XmNpreferredPaneSize</td>
<td>XmCPreferredPaneSize</td>
<td>Dimension</td>
<td>XmPanedAskChild</td>
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
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNresizeToPreferred</td>
<td>XmCBoolean</td>
<td>Boolean</td>
<td>False</td>
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
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNshowSash</td>
<td>XmCBoolean</td>
<td>Boolean</td>
<td>True</td>
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
<td>
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
<dd>Allows an application to specify whether the Paned widget should allow a pane to request to be resized. This flag has an effect only after the Paned widget and its children have been realized. If this flag is set to True, the Paned widget tries to honor requests to alter the height of the pane. If False, it always denies pane requests to resize.</p>
<dt><code>XmNpaneMaximum</code></p>
<dd>Allows an application to specify the maximum size to which a pane may be resized. This value must be greater than the specified minimum.</p>
<dt><code>XmNpaneMinimum</code></p>
<dd>Allows an application to specify the minimum size to which a pane may be resized. This value must be greater than 0 (zero).</p>
<dt><code>XmNskipAdjust</code></p>
<dd>When set to True, this Boolean resource allows an application to specify that the Paned widget should not automatically resize this pane.</p>
<dt><code>XmNpreferredPaneSize</code></p>
<dd>Preferred size of the pane. If this value is not set the paned widget will query the child for a preferred size. This resource allows the user or application to provide a new preferred size.</p>
<dt><code>XmNresizeToPreferred</code></p>
<dd>Specifies whether to resize each pane to its preferred size when the Paned window is resized. If this is False then only those panes the user has not resized with the sashes will be resized to their preferred size.</p>
<dt><code>XmNshowSash</code></p>
<dd>If True show the Sash below or to the right of this pane.</dl>
<h3>Inherited Resources</h3>
<p>Paned widget inherits behavior and resources from the superclasses described in the following tables. For a complete description of each resource, refer to the reference page for that superclass. </p>
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
<tr VALIGN=top>
<td></td>
<td></td>
<td></td>
<td></td>
<td>
</td>
</tr>
</table>
</table>
<h3>Translations</h3>
<p><code>XmPaned widget</code> inherits translations from <code>XmManager</code>. </p>
<p> The translations for sashes within the Paned widget are described in the following table. </p>
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
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfHelp&gt;</code>:</p>
<dd>Help()</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfUp&gt;</code>:</p>
<dd>SashAction(<code>Key,10,Up</code>)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfUp&gt;</code>:</p>
<dd>SashAction(<code>Key,1,Up</code>)</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfRight&gt;</code>:</p>
<dd>SashAction(<code>Key,10,Right</code>)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfRight&gt;</code>:</p>
<dd>SashAction(<code>Key,1,Right</code>)</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfDown&gt;</code>:</p>
<dd>SashAction(<code>Key,10,Down</code>)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfDown&gt;</code>:</p>
<dd>SashAction(<code>Key,1,Down</code>)</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfLeft&gt;</code>:</p>
<dd>SashAction(<code>Key,10,Left</code>)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfLeft&gt;</code>:</p>
<dd>SashAction(<code>Key,1,Left</code>)</p>
<dt><code>s &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>Tab</code>:</p>
<dd>PrevTabGroup()</p>
<dt><code>&asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>Tab</code>:</p>
<dd>NextTabGroup()</dl>
<h3>Action Routines</h3>
<p>The <code>XmPaned</code> action routines are</p>
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
<dd>Note that the SashAction action routine is not a direct action routine of the <code>XmPaned,</code> but rather an action of the Sash control created by the <code>XmPaned</code>.</dl>
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
<p><code><a href="/docs/linux/man/3-composite/">Composite</a></code>(3), <code><a href="/docs/linux/man/3-constraint/">Constraint</a></code>(3), <code><a href="/docs/linux/man/3-core/">Core</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatepaned/">XmCreatePaned</a></code>(3), <code><a href="/docs/linux/man/3-xmmanager/">XmManager</a></code>(3), <code><a href="/docs/linux/man/3-xmpanegetpanes/">XmPaneGetpanes</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatepaned/">XmVaCreatePaned</a></code>(3), and <code><a href="/docs/linux/man/3-xmvacreatemanagedpaned/">XmVaCreateManagedPaned</a></code>(3).</p>
