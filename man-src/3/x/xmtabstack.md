---
title: "xmtabstack(3)"
name: "xmtabstack"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtabstack/"
description: "XmTabStack – The TabStack widget class"
---

<p><code>XmTabStack</code> &#8211; The TabStack widget class</p>
<h2>Synopsis</h2>
<p>#include &lt;Xm/TabStack.h&gt;</p>
<h2>Description</h2>
<p>The XmTabStack widget manages a group of widgets such that only one widget in the group is visible at a time. Each child is associated with a &quot;tab&quot; that displays a text label and/or a pixmap. By selecting the &quot;tab&quot; the user interactively determines which child is displayed. This widget exhibits behavior similar to the Microsoft Windows(TM) Tab Control. </p>
<p> The tabs can be configured to appear above, below, to the right, and to the left of a work area with the text oriented in any of the four cardinal directions. </p>
<p> The TabStack allows the user to select, either by pointer or keyboard traversal, tabs. When a tab is selected it changes appearance so that it appears to be raised above the other tabs. When a tab is selected the child associated with the tab is made visible. One tab is selected at all times.</p>
<h3>Classes</h3>
<p>TabStack inherits behavior and resources form <code>Core</code>, <code>Composite</code>, <code>Constraint</code>, <code>XmManager</code> and <code>XmBulletinBoard Classes. </p>
<p> The class pointer is xmTabStackWidgetClass</code>. </p>
<p> The class name is <code>XmTabStack</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a .Xdefaults file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a .Xdefaults file, remove the <code>Xm</code> or prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time(C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
<p> <center></p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3><code>XmTabStack Resource Set</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>Name</code></td>
<td><code>Default</code></td>
<td><code>Access</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Class</code></td>
<td><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Type</code></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNfontList</td>
<td>Dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCFontList</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmFontList</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNhighlightThickness</td>
<td>2</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCHighlightThickness</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Dimension</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNstackedEffect</td>
<td>True</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCStackedEffect</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtabAutoSelect</td>
<td>True</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCTabAutoSelect</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtabCornerPercent</td>
<td>40</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCTabCornerPercent</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>int</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtabLabelSpacing</td>
<td>2</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCTabLabelSpacing</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Dimension</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtabMarginHeight</td>
<td>3</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCTabMarginHeight</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Dimension</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtabMarginWidth</td>
<td>3</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCTabMarginWidth</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Dimension</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtabMode</td>
<td>XmTABS_BASIC</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCTabMode</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>int</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtabOffset</td>
<td>10</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCTabOffset</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Dimension</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtabOrientation</td>
<td>Dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCTabOrientation</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>int</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtabSelectColor</td>
<td>Dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCTabSelectColor</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Pixel</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtabSelectedCallback</td>
<td>NULL</td>
<td>CS
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCCallback</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XtCallbackList</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtabSelectPixmap</td>
<td>XmUNSPECIFIED_PIXMAP</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCTabSelectPixmap</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Pixmap</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtabSide</td>
<td>XmTABS_ON_TOP</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCTabSide</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>int</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtabStyle</td>
<td>XmTABS_BEVELED</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCTabStyle</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>int</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNuniformTabSize</td>
<td>True</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCUniformTabSize</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNuseImageCache</td>
<td>True</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCUseImageCache</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
</table>
<p></center></p>
<dl COMPACT>
<dt><code>XmNfontList</code></p>
<dd>Specifies the XmFontList to use when drawing the label strings for the tabs.</p>
<dt><code>XmNhighlightThickness</code></p>
<dd>Specifies the thickness of the rectangle drawn around the label string and label pixmap of the tab with keyboard traversal.</p>
<dt><code>XmNstackedEffect</code></p>
<dd>Specifies if the visuals should depict a stack of folders, True, or if the XmTabStack should use all available space for its children, False.</p>
<dt><code>XmNtabAutoSelect</code></p>
<dd>Specifies if a tab is automatically selected when it receives keyboard traversal.</p>
<dt><code>XmNtabCornerPercent</code></p>
<dd>Specifies the percent of the font height that should be used for the corner visual.</p>
<dt><code>XmNtabLabelSpacing</code></p>
<dd>Specifies the amount of space to leave between a text label and a pixmap in the tab area.</p>
<dt><code>XmNtabMarginHeight</code></p>
<dd>Specifies the vertical border that is placed around the label area of a tab.</p>
<dt><code>XmNtabMarginWidth</code></p>
<dd>Specifies the horizontal border that is placed around the label area of a tab.</p>
<dt><code>XmNtabMode</code></p>
<dd>Specifies the mode in which the XmTabStack distributes the tabs. Valid values for this resource include:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmTABS_BASIC</code></p>
<dd>Distributes the tabs in either a vertical or horizontal row and clips the tabs if there is not enough room to display all the tabs.</p>
<dt><code>XmTABS_STACKED</code></p>
<dd>Distributes the tabs in either a vertical or horizontal row. If there is not enough room to display all the tabs additional rows are added. When a tab is selected, its row is moved next to the children in the stack.</p>
<dt><code>XmTABS_STACKED_STATIC</code></p>
<dd>Distributes the tabs in either a vertical or horizontal row. If there is not enough room to display all the tabs additional rows are added. The positions of rows are not changed when tabs are selected.</dl>
</dl>
<dt><code>XmNtabOffset</code></p>
<dd>Specifies the amount of indentation used to stagger the tab rows when displaying tabs in either the <code>XmTABS_STACKED</code> or <code>XmTABS_STACKED_STATIC</code> mode.</p>
<dt><code>XmNtabOrientation</code></p>
<dd>Specifies the orientation of the tab, and the rotation factor of the tab label. Valid values for this resource include:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmTAB_ORIENTATION_DYNAMIC</code></p>
<dd>Specifies that the orientation of the tabs should be calculated dynamically based on the <code>XmNtabSide</code> resource.</p>
<dt><code>XmTABS_LEFT_TO_RIGHT</code></p>
<dd>Specifies that the text appears at the default rotation.</p>
<dt><code>XmTABS_RIGHT_TO_LEFT</code></p>
<dd>Specifies that the text appears upside down.</p>
<dt><code>XmTABS_TOP_TO_BOTTOM</code></p>
<dd>Specifies that the text should be rotated to the vertical position with the first character drawn at the lowest y position and the bottom of the text faces the lowest x position.</p>
<dt><code>XmTABS_BOTTOM_TO_TOP</code></p>
<dd>Specifies that the text should be rotated to the vertical, position with the first character drawn at the highest y position and the bottom of the text faces the highest x position.</dl>
</dl>
<dt><code>XmNtabSelectColor</code></p>
<dd>Specifies the color of the selected tab.</p>
<dt><code>XmNtabSelectedCallback</code></p>
<dd>Specifies the list of callbacks to call when a child becomes the selected tab.</p>
<dt><code>XmNtabSelectPixmap</code></p>
<dd>Specifies the pixmap of the selected tab.</p>
<dt><code>XmNtabSide</code></p>
<dd>Specifies the location of the tab with respect to the children of the XmTabStack. Valid values for this resource include:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmTABS_ON_TOP</code></p>
<dd>Specifies that the tabs should be placed above the children.</p>
<dt><code>XmTABS_ON_BOTTOM</code></p>
<dd>Specifies that the tabs should be placed below the children.</p>
<dt><code>XmTABS_ON_RIGHT</code></p>
<dd>Specifies that the tabs should be placed to the right of the children.</p>
<dt><code>XmTABS_ON_LEFT</code></p>
<dd>Specifies that the tabs should be placed to the left of the children.</dl>
</dl>
<dt><code>XmNtabStyle</code></p>
<dd>Specifies the appearance of the tabs associated with the children of the XmTabStack. Valid values for this resource include:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmTABS_BEVELED</code></p>
<dd>Draws the corners of the tabs as an angled line.</p>
<dt><code>XmTABS_ROUNDED</code></p>
<dd>Draws the corners of the tabs as a quarter of a circle.</p>
<dt><code>XmTABS_SQUARED</code></p>
<dd>Draws the tabs as rectangles.</dl>
</dl>
<dt><code>XmNuniformTabSize</code></p>
<dd>Determines if all tabs should have a uniform major dimension, where the major dimension is width if the tab orientation is <code>XmTABS_LEFT_TO_RIGHT</code> or <code>XmTABS_RIGHT_TO_LEFT</code> or height if the tab orientation is <code>XmTABS_TOP_TO_BOTTOM</code> or <code>XmTABS_BOTTOM_TO_TOP</code>. When <code>XmNtabMode</code> is either <code>XmTABS_STACKED</code> or <code>XmTABS_STACKED_STATIC</code>, this resource is forced to True.</p>
<dt><code>XmNuseImageCache</code></p>
<dd>Destermines if the Xmmages used for rotating text and pixmaps should be cached. This increases performance but uses up more memory. </p>
<p> <center></p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3><code>XmTabStack Constraint Resource Set</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>Name</code></td>
<td><code>Default</code></td>
<td><code>Access</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Class</code></td>
<td><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Type</code></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNfreeTabPixmap</td>
<td>False</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCFreeTabPixmap</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtabAlignment</td>
<td>XmALIGNMENT_CENTER</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCAlignment</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>unsigned char</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtabBackground</td>
<td>Dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCBackground</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Pixel</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtabBackgroundPixmap</td>
<td>Dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCBackgroundPixmap</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Pixmap</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtabForeground</td>
<td>Dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCForeground</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Pixel</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtabLabelPixmap</td>
<td>XmUNSPECIFIED_PIXMAP</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCTabLabelPixmap</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Pixmap</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtabLabelString</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCTabLabelString</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmString</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtabPixmapPlacement</td>
<td>XmPIXMAP_RIGHT</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCTabPixmapPlacement</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmPixmapPlacement</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtabStringDirection</td>
<td>XmSTRING_DIRECTION_DEFAULT</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCTabStringDirection</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>unsigned char</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
</table>
<p></center></p>
<dt><code>XmNfreeTabPixmap</code></p>
<dd>Specifies that the pixmaps assigned to the <code>XmNlabelPixmap</code> resources should be freed when the widget is destroyed.</p>
<dt><code>XmNtabAlignment</code></p>
<dd>Specifies the alignment of the tab label. Valid values for this resource include:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmALIGNMENT_BEGINNING</code></p>
<dd>Aligns the label to the left side of the available space.</p>
<dt><code>XmALIGNMENT_CENTER</code></p>
<dd>Aligns the label centered in the available space.</p>
<dt><code>XmALIGNMENT_END</code></p>
<dd>Aligns the label to the right side of the available space.</dl>
</dl>
<dt><code>XmNtabBackground</code></p>
<dd>Specifies the background pixel for the tab.</p>
<dt><code>XmNtabBackgroundPixmap</code></p>
<dd>Specifies the background pixmap for the tab.</p>
<dt><code>XmNtabForeground</code></p>
<dd>Specifies the foreground pixel for the tab.</p>
<dt><code>XmNtabLabelPixmap</code></p>
<dd>Specifies the pixmap to display in the tab label.</p>
<dt><code>XmNtabLabelString</code></p>
<dd>Specifies the XmString to display as the textual portion of the tab label. This is copied when set on the widget. The value fetched via XtGetValues should not be freed as it returns a pointer to the widgets value. If you wish to use the value returned from XtGetValues use XmStringCopy the returned value.</p>
<dt><code>XmNtabPixmapPlacement</code></p>
<dd>Specifies the location of the pixmap with respect to the text in the tab label. Valid values for this resource include:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmPIXMAP_TOP</code></p>
<dd>Specifies that the pixmap should be above the XmString.</p>
<dt><code>XmPIXMAP_BOTTOM</code></p>
<dd>Specifies that the pixmap should be below the XmString.</p>
<dt><code>XmPIXMAP_RIGHT</code></p>
<dd>Specifies that the pixmap should be to the right of the XmString.</p>
<dt><code>XmPIXMAP_LEFT</code></p>
<dd>Specifies that the pixmap should be to the left of the XmString.</p>
<dt><code>XmPIXMAP_ONLY</code></p>
<dd>Specifies that only the pixmap portion of the tab label should be displayed.</p>
<dt><code>XmPIXMAP_NONE</code></p>
<dd>Specifies that only the XmString portion of the tab label should be displayed.</dl>
</dl>
<dt><code>XmNtabStringDirection</code></p>
<dd>Specifies the string direction for the XmString portion of the tab label. Valid values for this resouce include:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmSTRING_DIRECTION_L_TO_R</code></p>
<dd>Left to right</p>
<dt><code>XmSTRING_DIRECTION_R_TO_L</code></p>
<dd>Right to left</dl>
</dl>
</dl>
<h3>Inherited Resources</h3>
<p>TabStack inherits behavior and resources from the following superclasses. For a complete description of each resource, refer to the man page for that superclass. </p>
<p> <center></p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3><code>XmBulletinBoard Resource Set</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>Name</code></td>
<td><code>Default Access</code></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Class</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Type</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNallowOverlap</td>
<td>True</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCAllowOverlap</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNautoUnmanage</td>
<td>False</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCAutoUnmanage</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNbuttonFontList</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCButtonFontList</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmFontList</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNcancelButton</td>
<td>NULL</td>
<td>SG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCWidget</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Widget</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNdefaultButton</td>
<td>NULL</td>
<td>SG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCWidget</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Widget</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNdefaultPosition</td>
<td>True</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCDefaultPosition</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNdialogStyle</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCDialogStyle</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>unsigned char</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNdialogTitle</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCDialogTitle</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmString</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNfocusCallback</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCCallback</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XtCallbackList</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNlabelFontList</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCLabelFontList</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmFontList</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNmapCallback</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCCallback</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XtCallbackList</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNmarginHeight</td>
<td>10</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCMarginHeight</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Dimension</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNmarginWidth</td>
<td>10</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCMarginWidth</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Dimension</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNnoResize</td>
<td>False</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCNoResize</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> <center></p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3><code>XmManager Resource Set</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>Name</code></td>
<td><code>Default Access</code></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Class</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Type</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNbottomShadowColor</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCBottomShadowColor</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Pixel</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNbottomShadowPixmap</td>
<td>XmUNSPECIFIED_PIXMAP</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCBottomShadowPixmap</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Pixmap</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNforeground</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCForeground</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Pixel</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNhelpCallback</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCCallback</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XtCallbackList</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNhighlightColor</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCHighlightColor</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Pixel</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNhighlightPixmap</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCHighlightPixmap</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Pixmap</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNinitialFocus</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCInitialFocus</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Widget</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNnavigationType</td>
<td>XmTAB_GROUP</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCNavigationType</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmNavigationType</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNshadowThickness</td>
<td>2</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCShadowThickness</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Dimension</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNstringDirection</td>
<td>dynamic</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCStringDirection</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmStringDirection</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtopShadowColor</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCTopShadowColor</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Pixel</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtopShadowPixmap</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCTopShadowPixmap</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Pixmap</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtraversalOn</td>
<td>True</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCTraversalOn</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNunitType</td>
<td>dynamic CSG</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCUnitType</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>unsigned char</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNuserData</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCUserData</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XtPointer</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> <center></p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3><code>Composite Resource Set</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>Name</code></td>
<td><code>Default Access</code></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Class</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Type</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNchildren</td>
<td>NULL</td>
<td>G
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCReadOnly</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>WidgetList</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNinsertPosition</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCInsertPosition</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XtOrderProc</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNnumChildren</td>
<td>0</td>
<td>G
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCReadOnly</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Cardinal</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> <center></p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3><code>Core Resource Set</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>Name</code></td>
<td><code>Default Access</code></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Class</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Type</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNaccelerators</td>
<td>dynamic</td>
<td>N/A
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCAccelerators</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XtAccelerators</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNancestorSensitive</td>
<td>dynamic</td>
<td>G
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCSensitive</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNbackground</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCBackground</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Pixel</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNbackgroundPixmap</td>
<td>XmUNSPECIFIED_PIXMAP</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCPixmap</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Pixmap</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNborderColor</td>
<td>XtDefaultForeground</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCBorderColor</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Pixel</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNborderPixmap</td>
<td>XmUNSPECIFIED_PIXMAP</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCPixmap</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Pixmap</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNborderWidth</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCBorderWidth</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Dimension</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNcolormap</td>
<td>dynamic</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCColormap</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Colormap</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNdepth</td>
<td>dynamic</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCDepth</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>int</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNdestroyCallback</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCCallback</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XtCallbackList</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNheight</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCHeight</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Dimension</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNinitialResourcesPersistent</td>
<td>True</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCInitialResourcesPersistent</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNmappedWhenManaged</td>
<td>True</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCMappedWhenManaged</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNscreen</td>
<td>Screen*</td>
<td>dynamic
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCScreen</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Screen</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNsensitive</td>
<td>True</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCSensitive</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Boolean</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtranslations</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCTranslations</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XtTranslations</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNwidth</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCWidth</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Dimension</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNx</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCPosition</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Position</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNy</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>XmCPosition</td>
<td>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Position</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
</table>
<p></center></p>
<h3>Calback Information</h3>
<p>A pointer to the following structure is passed to each callback: </p>
<p> <font SIZE="-1"> </font></p>
<pre>typedef struct _XmTabStackCallbackStruct {
 int<i>reason</i><code>;
 XEvent</code><i>*event</i><code>;
 Widget</code><i>selected_child</i><code>;
} XmTabStackCallbackStruct;
</code><font SIZE="+1"></font></pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked. Valid callbacks reasons include:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmCR_TAB_SELECTED</code></p>
<dd>Indicates that a child has been made the selected widget.</dl>
</dl>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the callback.</p>
<dt><i>selected_child</i></p>
<dd>Contains the widget ID of the selected child.</dl>
<h3>Translations</h3>
<p>XmTabStack includes the translations from the XmManager. </p>
<h3>Additional Behavior</h3>
<p>The XmTabStack has no additional behavior.</p>
<h3>Virtual Bindings</h3>
<p>The bindings for virtual keys are vendor specific. For information about bindings for virtual buttons and keys, see <code><a href="//www.systutorials.com/docs/linux/man/3X-VirtualBindings/">VirtualBindings</a>(3X)</code>.</p>
<h2>Related Information</h2>
<p><code><a href="/docs/linux/man/3-xmbulletinboard/">XmBulletinBoard</a></code>(3), <code><a href="/docs/linux/man/3-composite/">Composite</a></code>(3), <code><a href="/docs/linux/man/3-constraint/">Constraint</a></code>(3), <code><a href="/docs/linux/man/3-core/">Core</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatetabstack/">XmCreateTabStack</a></code>(3), <code><a href="/docs/linux/man/3-xmmanager/">XmManager</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatetabstack/">XmVaCreateTabStack</a></code>(3), and <code><a href="/docs/linux/man/3-xmvacreatemanagedtabstack/">XmVaCreateManagedTabStack</a></code>(3).</p>
