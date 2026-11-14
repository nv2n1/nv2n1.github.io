---
title: "xmiconbox(3)"
name: "xmiconbox"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmiconbox/"
description: "XmIconBox — The IconBox widget class"
---

<p><code>XmIconBox</code> &#8212; The IconBox widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/IconBox.h&gt;</pre>
<h2>Description</h2>
<p>The Icon Box widget lays out its children on a grid with each child forced to be the same size and with the location of each child specified as an X and Y location on the grid. </p>
<p> The size of the Icon Box, its children, and the number of cells displayed are calculated as described below. The general idea is that all children are always be shown and should be given their desired size whenever possible. The user may add or delete cells by resizing this window using the window manager widget. </p>
<p> The preferred size is calculated by using the maximum desired child height or width and making sure that these are no smaller than the minimum sizes. This size is multiplied by the number of cells along the axis and properly padded to come up with a preferred size. The number of cells is the maximum of the largest cellX or cellY value and the minimum number of horizontal or vertical cells. </p>
<p> If the Icon box is forced larger than its preferred size more cells are added at the bottom-right of the widget while the children all remain at their preferred sizes. </p>
<p> If the Icon box is forced smaller than its preferred size each cell is forced to be smaller in order to allow all children to fit within the Icon Box. All children will be forced to the same smaller size.</p>
<h3>Classes</h3>
<p>Icon Box inherits behavior, resources, and traits from <code>Core</code>, <code>Composite</code>, <code>Constraint</code>, and <code>XmManager</code>. </p>
<p> The class pointer is <code>xmIconBoxWidgetClass</code>. </p>
<p> The class name is <code>XmIconBox</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmIconBox Resource Set</code>
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
<td>XmNhorizontalMargin</td>
<td>XmCMargin</td>
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
<td>XmNminimumHorizontalCells</td>
<td>XmCDefaultCells</td>
<td>int</td>
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
<td>XmNminimumVerticalCells</td>
<td>XmCDefaultCells</td>
<td>int</td>
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
<td>XmNminimumCellHeight</td>
<td>XmCMinimumCellSize</td>
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
<td>XmNminimumCellWidth</td>
<td>XmCMinimumCellSize</td>
<td>Dimension</td>
<td>20</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNverticalMargin</td>
<td>XmCMargin</td>
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
</table>
</table>
<dl COMPACT>
<dt><code>XmNhorizontalMargin</code></p>
<dd>
<dt><code>XmNverticalMargin</code></p>
<dd>The amount of space between each cell and its neighbor or the edge of the Icon Box.</p>
<dt><code>XmNminimumHorizontalCells</code></p>
<dd>
<dt><code>XmNminimumVerticalCells</code></p>
<dd>The minimum number of cells to display in the horizontal and vertical directions. This number of cells will always be displayed.</p>
<dt><code>XmNminimumCellWidth</code></p>
<dd>
<dt><code>XmNminimumCellHeight</code></p>
<dd>The smallest size the cells are allowed to be in the direction specified.</dl>
<h3>Constraint Resources</h3>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmIconBox Constraint Resource Set</code>
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
<td>XmNcellX</td>
<td>XmCCellX</td>
<td>Short</td>
<td>XmIconBoxAnyCell</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNcellY</td>
<td>XmCCellY</td>
<td>Short</td>
<td>XmIconBoxAnyCell</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
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
<dt><code>XmNcellX</code></p>
<dd>
<dt><code>XmNcellY</code></p>
<dd>The location of this cell in cell space. These coordinates may be any positive integer. They determine where this widget will be placed relative to its neighbors. Having two children at the same cell X and cell Y location will result in undefined behavior. To place a cell at any empty cell, set cell X and cell Y to the value XmIconBoxAnyCell.</dl>
<h3>Inherited Resources</h3>
<p>Icon Box inherits behavior and resources from the superclasses described in the following tables. For a complete description of each resource, refer to the reference page for that superclass. </p>
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
<h3>Translations</h3>
<p>XmIconBox inherits translations from XmManager. </p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-composite/">Composite</a></code>(3), <code><a href="/docs/linux/man/3-constraint/">Constraint</a></code>(3), <code><a href="/docs/linux/man/3-core/">Core</a></code>(3), <code><a href="/docs/linux/man/3-xmcreateiconbox/">XmCreateIconBox</a></code>(3), <code><a href="/docs/linux/man/3-xmiconboxiscellempty/">XmIconBoxIsCellEmpty</a></code>(3), <code><a href="/docs/linux/man/3-xmmanager/">XmManager</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreateiconbox/">XmVaCreateIconBox</a></code>(3), and <code><a href="/docs/linux/man/3-xmvacreatemanagediconbox/">XmVaCreateManagedIconBox</a></code>(3). </p>
<h2>Copyright</h2>
<p>Copyright (c) 1992 by Integrated Computer Solutions, Inc.</p>
