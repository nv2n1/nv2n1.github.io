---
title: "xmmanager(3)"
name: "xmmanager"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmmanager/"
description: "XmManager — The Manager widget class"
---

<p><code>XmManager</code> &#8212; The Manager widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;</pre>
<h2>Description</h2>
<p>Manager is a widget class used as a supporting superclass for other widget classes. It supports the visual resources, graphics contexts, and traversal resources necessary for the graphics and traversal mechanisms.</p>
<h3>Classes</h3>
<p>Manager inherits behavior and resources from <code>Core</code>, <code>Composite</code>, and <code>Constraint</code>. </p>
<p> The class pointer is <code>xmManagerWidgetClass</code>. </p>
<p> The class name is <code>XmManager</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
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
<dl COMPACT>
<dt><code>XmNbottomShadowColor</code></dt>
<dd>Specifies the color to use to draw the bottom and right sides of the border shadow. This color is used if the <code>XmNbottomShadowPixmap</code> resource is NULL.</dd>
<dt><code>XmNbottomShadowPixmap</code></dt>
<dd>Specifies the pixmap to use to draw the bottom and right sides of the border shadow.</dd>
<dt><code>XmNforeground</code></dt>
<dd>Specifies the foreground drawing color used by manager widgets.</dd>
<dt><code>XmNhelpCallback</code></dt>
<dd>Specifies the list of callbacks that are called when the help key sequence is pressed. The reason sent by this callback is <code>XmCR_HELP</code>.</dd>
<dt><code>XmNhighlightColor</code></dt>
<dd>Specifies the color of the highlighting rectangle. This color is used if the highlight pixmap resource is <code>XmUNSPECIFIED_PIXMAP</code>.</dd>
<dt><code>XmNhighlightPixmap</code></dt>
<dd>Specifies the pixmap used to draw the highlighting rectangle.</dd>
<dt><code>XmNinitialFocus</code></dt>
<dd>Specifies the ID of a widget descendant of the manager. The widget must meet these conditions:</dd>
<dl COMPACT>
<dd>
</dd><dl COMPACT>
<dt> &bull;</dt>
<dd>The widget must be either a tab group or a non-tab-group widget that can receive keyboard focus. For the definition of a tab group, see the description of the Manager, Primitive, and Gadget <code>XmNnavigationType</code> resources. In general a widget can receive keyboard focus when it is a primitive, a gadget, or a manager (such as a DrawingArea with no traversable children) that acts as a primitive.</dd>
<dt> &bull;</dt>
<dd>The widget must not be a descendant of a tab group that is itself a descendant of the manager. That is, the widget cannot be contained within a tab group that is nested inside the manager.</dd>
<dt> &bull;</dt>
<dd>The widget and its ancestors must have a value of True for their <code>XmNtraversalOn</code> resources.</dd></dl>
</dl>
<dd>If the widget does not meet these conditions, <code>XmNinitialFocus</code> is treated as if the value were NULL.</dd>
<dd>This resource is meaningful only when the nearest shell ancestor&#8217;s <code>XmNkeyboardFocusPolicy</code> is <code>XmEXPLICIT</code>. It is used to determine which widget receives focus in these situations:</dd>
<dl COMPACT>
<dd>
</dd><dl COMPACT>
<dt> &bull;</dt>
<dd>When the manager is the child of a shell and the shell hierarchy receives focus for the first time</dd>
<dt> &bull;</dt>
<dd>When focus is inside the shell hierarchy, the manager is a composite tab group, and the user traverses to the manager via the keyboard</dd></dl>
</dl>
<dd>Focus is then determined as follows:</dd>
<dl COMPACT>
<dd>
</dd><dl COMPACT>
<dt> &bull;</dt>
<dd>If <code>XmNinitialFocus</code> is a traversable non-tab-group widget, that widget receives focus.</dd>
<dt> &bull;</dt>
<dd>If <code>XmNinitialFocus</code> is a traversable tab group, that tab group receives focus. If that tab group is a composite with descendant tab groups or traversable non-tab-group widgets, these procedures are used recursively to assign focus to a descendant of that tab group.</dd>
<dt> &bull;</dt>
<dd>If <code>XmNinitialFocus</code> is NULL, the first traversable non-tab-group widget that is not contained within a nested tab group receives focus.</dd>
<dt> &bull;</dt>
<dd>If <code>XmNinitialFocus</code> is NULL and no traversable non-tab-group widget exists, the first traversable tab group that is not contained within a nested tab group receives focus. If that tab group is a composite with descendant tab groups or traversable non-tab-group widgets, these procedures are used recursively to assign focus to a descendant of that tab group.</dd></dl>
</dl>
<dd>If a shell hierarchy regains focus after losing it, focus returns to the widget that had the focus at the time it left the hierarchy.</dd>
<dd>The use of <code>XmNinitialFocus</code> is undefined if the manager is a MenuBar, PulldownMenu, PopupMenu, or OptionMenu.</dd>
<dt><code>XmNlayoutDirection</code></dt>
<dd>Specifies the direction in which components of the manager (including strings) are laid out. The values are of type <code>XmDirection</code>. If the widget&#8217;s parent is a manager or shell, the value is inherited from the widget&#8217;s parent. Otherwise, it is inherited from the closest ancestor vendor or menu shell. Refer to the <code><a href="/docs/linux/man/3-xmdirection/">XmDirection</a></code>(3) reference page for the possible direction values.</dd>
<dt><code>XmNnavigationType</code></dt>
<dd>Determines whether the widget is a tab group.</dd>
<dl COMPACT>
<dd>
</dd><dl COMPACT>
<dt><code>XmNONE</code></dt>
<dd>Indicates that the widget is not a tab group.</dd>
<dt><code>XmTAB_GROUP</code></dt>
<dd>Indicates that the widget is a tab group, unless the <code>XmNnavigationType</code> of another widget in the hierarchy is <code>XmEXCLUSIVE_TAB_GROUP</code>.</dd>
<dt><code>XmSTICKY_TAB_GROUP</code></dt>
<dd>Indicates that the widget is a tab group, even if the <code>XmNnavigationType</code> of another widget in the hierarchy is <code>XmEXCLUSIVE_TAB_GROUP</code>.</dd>
<dt><code>XmEXCLUSIVE_TAB_GROUP</code></dt>
<dd>Indicates that the widget is a tab group and that widgets in the hierarchy whose <code>XmNnavigationType</code> is <code>XmTAB_GROUP</code> are not tab groups.</dd>
<dd>When a parent widget has an <code>XmNnavigationType</code> of <code>XmEXCLUSIVE_TAB_GROUP</code>, traversal of non-tab-group widgets within the group is based on the order of those widgets in their parent&#8217;s <code>XmNchildren</code> list.</dd>
<dd>When the <code>XmNnavigationType</code> of any widget in a hierarchy is <code>XmEXCLUSIVE_TAB_GROUP</code>, traversal of tab groups in the hierarchy proceeds to widgets in the order in which their <code>XmNnavigationType</code> resources were specified as <code>XmEXCLUSIVE_TAB_GROUP</code> or <code>XmSTICKY_TAB_GROUP</code>, whether by creating the widgets with that value, by calling <code>XtSetValues</code>, or by calling <code>XmAddTabGroup</code>.</dd></dl>
</dl>
<dt><code>XmNpopupHandlerCallback</code></dt>
<dd>Allows the application to control which popup menu will be automatically posted. The reason can either be <code>XmCR_POST</code> or <code>XmCR_REPOST:</code></dd>
<dl COMPACT>
<dd>
</dd><dl COMPACT>
<dt><code>XmCR_POST</code></dt>
<dd>Indicates that this is a regular posting request.</dd>
<dt><code>XmCR_REPOST</code></dt>
<dd>Indicates that the menu was just unposted and that this callback was invoked on a replay.</dd></dl>
</dl>
<dd>This callback uses the <code>XmPopupHandlerCallbackStruct</code> structure to pass information.</dd>
<dt><code>XmNshadowThickness</code></dt>
<dd>Specifies the thickness of the drawn border shadow. <code>XmBulletinBoard</code> and its descendants set this value dynamically. If the widget is a top-level window, this value is set to 1. If it is not a top-level window, this value is set to 0 (zero).</dd>
<dt><code>XmNstringDirection</code></dt>
<dd>Is a synthetic resource for setting <code>XmNlayoutDirection</code>. The values for this resource are <code>XmSTRING_DIRECTION_L_TO_R</code> and <code>XmSTRING_DIRECTION_R_TO_L</code>. Refer to the <code>XmNlayoutDirection</code> resource description. The <code>XmNstringDirection</code> resource is obsoleted by <code>XmNlayoutDirection</code>, but is kept here for backward compatibility.</dd>
<dt><code>XmNtopShadowColor</code></dt>
<dd>Specifies the color to use to draw the top and left sides of the border shadow. This color is used if the <code>XmNtopShadowPixmap</code> resource is NULL.</dd>
<dt><code>XmNtopShadowPixmap</code></dt>
<dd>Specifies the pixmap to use to draw the top and left sides of the border shadow.</dd>
<dt><code>XmNtraversalOn</code></dt>
<dd>Specifies whether traversal is activated for this widget.</dd>
<dt><code>XmNunitType</code></dt>
<dd>Provides the basic support for resolution independence. It defines the type of units a widget uses with sizing and positioning resources. If the widget&#8217;s parent is a subclass of <code>XmManager</code> and if the <code>XmNunitType</code> resource is not explicitly set, it defaults to the unit type of the parent widget. If the widget&#8217;s parent is not a subclass of <code>XmManager</code>, the resource has a default unit type of <code>XmPIXELS</code>.</dd>
<dd>The unit type can also be specified in resource files, with the following format:</dd></dl>
<pre><tt></tt><i>&lt;floating value&gt;&lt;unit&gt;</i></pre>
<dl COMPACT>
<dd>where:</dd>
<dl COMPACT>
<dd>
</dd><dl COMPACT>
<dt><i>unit</i></dt>
<dd>is &lt;&quot; &quot;, pixels, inches, centimeters, millimeters, points, font units&gt;</dd>
<dt><i>pixels</i></dt>
<dd>is &lt;<i>pix</i>, <i>pixel</i>, <i>pixels</i>&gt;</dd>
<dt><i>inches</i></dt>
<dd>is &lt;<i>in</i>, <i>inch</i>, <i>inches</i>&gt;</dd>
<dt><i>centimeter</i></dt>
<dd>is &lt;<i>cm</i>, <i>centimeter</i>, <i>centimeters</i>&gt;</dd>
<dt><i>millimeters</i></dt>
<dd>is &lt;<i>mm</i>, <i>millimeter</i>, <i>millimeters</i>&gt;</dd>
<dt><code>points</code></dt>
<dd>is &lt;<i>pt</i>, <i>point</i>, <i>points</i>&gt;</dd>
<dt><code>font units</code></dt>
<dd>is &lt;<i>fu</i>, <code>font_unit</code>, <code>font_units</code>&gt;</dd>
<dt><i>float</i></dt>
<dd>is {&quot;+&quot;|&quot;-&quot;}&#123;&#123;&lt;&quot;0&quot;-&quot;9&quot;&gt;*}.}&lt;&quot;0&quot;-&quot;9&quot;&gt;*</dd>
<dd>Note that the type Dimension must always be positive.</dd></dl>
</dl>
<dd>For example,</dd></dl>
<pre><tt>xmfonts*XmMainWindow.height: 10.4cm
*PostIn.width: 3inches</tt></pre>
<dl COMPACT>
<dd><code>XmNunitType</code> can have the following values:</dd>
<dl COMPACT>
<dd>
</dd><dl COMPACT>
<dt><code>XmPIXELS</code></dt>
<dd>All values provided to the widget are treated as normal pixel values.</dd>
<dt><code>XmMILLIMETERS</code></dt>
<dd>All values provided to the widget are treated as normal millimeter values.</dd>
<dt><code>Xm100TH_MILLIMETERS</code></dt>
<dd>All values provided to the widget are treated as 1/100 of a millimeter.</dd>
<dt><code>XmCENTIMETERS</code></dt>
<dd>All values provided to the widget are treated as normal centimeter values.</dd>
<dt><code>XmINCHES</code></dt>
<dd>All values provided to the widget are treated as normal inch values.</dd>
<dt><code>Xm1000TH_INCHES</code></dt>
<dd>All values provided to the widget are treated as 1/1000 of an inch.</dd>
<dt><code>XmPOINTS</code></dt>
<dd>All values provided to the widget are treated as normal point values. A point is a unit used in text processing applications and is defined as 1/72 of an inch.</dd>
<dt><code>Xm100TH_POINTS</code></dt>
<dd>All values provided to the widget are treated as 1/100 of a point. A point is a unit used in text processing applications and is defined as 1/72 of an inch.</dd>
<dt><code>XmFONT_UNITS</code></dt>
<dd>All values provided to the widget are treated as normal font units. A font unit has horizontal and vertical components. These are the values of the XmScreen resources <code>XmNhorizontalFontUnit</code> and <code>XmNverticalFontUnit</code>.</dd>
<dt><code>Xm100TH_FONT_UNITS</code></dt>
<dd>All values provided to the widget are treated as 1/100 of a font unit. A font unit has horizontal and vertical components. These are the values of the XmScreen resources <code>XmNhorizontalFontUnit</code> and <code>XmNverticalFontUnit</code>.</dd></dl>
</dl>
<dt><code>XmNuserData</code></dt>
<dd>Allows the application to attach any necessary specific data to the widget. This is an internally unused resource.</dd></dl>
<h3>Dynamic Color Defaults</h3>
<p>The foreground, background, top shadow, bottom shadow, and highlight color resources are dynamically defaulted. If no color data is specified, the colors are automatically generated. On a single-plane system, a black and white color scheme is generated. Otherwise, four colors are generated, which display the correct shading for the 3-D visuals. If the background is the only color specified for a widget, the top shadow and bottom shadow colors are generated to give the 3-D appearance. Foreground and highlight colors are generated to provide sufficient contrast with the background color. </p>
<p> Colors are generated only at creation. Resetting the background through <code>XtSetValues</code> does not regenerate the other colors. <code>XmChangeColor</code> can be used to recalculate all associated colors based on a new background color.</p>
<h3>Inherited Resources</h3>
<p>Manager inherits resources from the superclasses described in the following tables. For a complete description of each resource, refer to the reference page for that superclass. </p>
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
<p>A pointer to the following structure is passed to each callback for <code>XmNhelpCallback</code>: </p>
<pre>typedef struct
{
 int <i>reason</i>;
 XEvent <i>* event</i>;
} XmAnyCallbackStruct;</pre>
<dl COMPACT>
<dt><i>reason</i></dt>
<dd>Indicates why the callback was invoked. For this callback, <i>reason</i> is set to <code>XmCR_HELP</code>.</dd>
<dt><i>event</i></dt>
<dd>Points to the <code>XEvent</code> that triggered the callback.</dd></dl>
<p> A pointer to the following structure is passed to each callback for <code>XmNpopupHandlerCallback</code>: </p>
<pre>typedef struct
{
 int <i>reason</i>;
 XEvent <i>* event</i>;
 Widget <i>menuToPost</i>;
 Boolean <i>postIt</i>;
 Widget <i>target</i>;
} XmPopupHandlerCallbackStruct;</pre>
<dl COMPACT>
<dt><i>reason</i></dt>
<dd>Indicates why the callback was invoked.</dd>
<dt><i>event</i></dt>
<dd>Points to the <code>XEvent</code> that triggered the handler.</dd>
<dt><i>menuToPost</i></dt>
<dd>Specifies the popup menu that the menu system believes should be posted. The application may modify this field.</dd>
<dt><i>postIt</i></dt>
<dd>Indicates whether the posting process should continue. The application may modify this field.</dd>
<dt><i>target</i></dt>
<dd>Specifies the most specific widget or gadget that the menu sytem found from the event that matches the event.</dd></dl>
<h3>Translations</h3>
<p>The following set of translations are used by Manager widgets that have Gadget children. Because Gadgets cannot have translations associated with them, it is the responsibility of the Manager widget to intercept the events of interest and pass them to any Gadget child with focus. These events are ignored if no Gadget child has the focus. </p>
<p> The following key names are listed in the X standard key event translation table syntax. This format is the one used by Motif to specify the widget actions corresponding to a given key. A brief overview of the format is provided under <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3). For a complete description of the format, please refer to the X Toolkit Instrinsics Documentation.</p>
<dl COMPACT>
<dt><code>&lt;BtnMotion&gt;</code>:</dt>
<dd>ManagerGadgetButtonMotion()</dd>
<dt><code>c&lt;Btn1Down&gt;</code>:</dt>
<dd>ManagerGadgetTraverseCurrent()</dd>
<dt><code>&asymp;c</code><code>&lt;Btn1Down&gt;</code>:</dt>
<dd>ManagerGadgetArm()</dd>
<dt><code>&asymp;c</code><code>&lt;Btn1Down&gt;</code><code>,&asymp;c</code><code>&lt;Btn1Up&gt;</code>:</dt>
<dd>ManagerGadgetActivate()</dd>
<dt><code>&asymp;c</code><code>&lt;Btn1Up&gt;</code>:</dt>
<dd>ManagerGadgetActivate()</dd>
<dt><code>&asymp;c</code><code>&lt;Btn1Down&gt;</code><code>(2+)</code>:</dt>
<dd>ManagerGadgetMultiArm()</dd>
<dt><code>&asymp;c</code><code>&lt;Btn1Up&gt;</code><code>(2+)</code>:</dt>
<dd>ManagerGadgetMultiActivate()</dd>
<dt><code>&lt;Btn2Down&gt;</code>:</dt>
<dd>ManagerGadgetDrag()</dd>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfActivate&gt;</code>:</dt>
<dd>ManagerParentActivate()</dd>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfCancel&gt;</code>:</dt>
<dd>ManagerParentCancel()</dd>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfSelect&gt;</code>:</dt>
<dd>ManagerGadgetSelect()</dd>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfHelp&gt;</code>:</dt>
<dd>ManagerGadgetHelp()</dd>
<dt><code>&asymp;s &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>Return</code>:</dt>
<dd>ManagerParentActivate()</dd>
<dt><code>&asymp;s &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>space</code>:</dt>
<dd>ManagerGadgetSelect()</dd>
<dt><code>&lt;Key&gt;</code>:</dt>
<dd>ManagerGadgetKeyInput()</dd>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfBeginLine&gt;</code>:</dt>
<dd>ManagerGadgetTraverseHome()</dd>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfUp&gt;</code>:</dt>
<dd>ManagerGadgetTraverseUp()</dd>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfDown&gt;</code>:</dt>
<dd>ManagerGadgetTraverseDown()</dd>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfLeft&gt;</code>:</dt>
<dd>ManagerGadgetTraverseLeft()</dd>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfRight&gt;</code>:</dt>
<dd>ManagerGadgetTraverseRight()</dd>
<dt><code>s &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>Tab</code>:</dt>
<dd>ManagerGadgetPrevTabGroup()</dd>
<dt><code>&asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>Tab</code>:</dt>
<dd>ManagerGadgetNextTabGroup()</dd></dl>
<h3>Action Routines</h3>
<p>The <code>XmManager</code> action routines are</p>
<dl COMPACT>
<dt>GadgetTakeFocus():</dt>
<dd>Causes the current gadget to take keyboard focus when <code>Ctrl&lt;Btn1Down&gt;</code> is pressed.</dd>
<dt>ManagerGadgetActivate():</dt>
<dd>Causes the current gadget to be activated.</dd>
<dt>ManagerGadgetArm():</dt>
<dd>Causes the current gadget to be armed.</dd>
<dt>ManagerGadgetButtonMotion():</dt>
<dd>Causes the current gadget to process a mouse motion event.</dd>
<dt>ManagerGadgetDrag():</dt>
<dd>Causes the current gadget to begin a drag operation. This action is undefined for gadgets used in a menu system.</dd>
<dt>ManagerGadgetHelp():</dt>
<dd>Calls the callbacks for the current gadget&#8217;s <code>XmNhelpCallback</code> if any exist. If there are no help callbacks for this widget, this action calls the help callbacks for the nearest ancestor that has them.</dd>
<dt>ManagerGadgetKeyInput():</dt>
<dd>Causes the current gadget to process a keyboard event.</dd>
<dt>ManagerGadgetMultiActivate():</dt>
<dd>Causes the current gadget to process a multiple mouse click.</dd>
<dt>ManagerGadgetMultiArm():</dt>
<dd>Causes the current gadget to process a multiple mouse button press.</dd>
<dt>ManagerGadgetNextTabGroup():</dt>
<dd>This action depends on the value of the Display resource <code>XmNenableButtonTab</code>. When <code>XmNenableButtonTab</code> is False (default), this action traverses to the first item in the next tab group. If the current tab group is the last entry in the tab group list, it wraps to the beginning of the tab group list.</dd>
<dd>When <code>XmNenableButtonTab</code> is True, this action moves to the next item within the current tab group, unless it is the last item in the tab group. When the item is the last in the group, the action traverses to the first item in the next tab group. The <code>XmNenableButtonTab</code> behavior applies only to PushButton, ArrowButton, and DrawnArrow.</dd>
<dt>ManagerGadgetPrevTabGroup():</dt>
<dd>This action depends on the value of the Display resource <code>XmNenableButtonTab</code>. When <code>XmNenableButtonTab</code> is False (default), this action traverses to the first item in the previous tab group. If the beginning of the tab group list is reached, it wraps to the end of the tab group list.</dd>
<dd>When <code>XmNenableButtonTab</code> is True, this action moves to the previous item within the current tab group unless it is the first item in the tab group. When the item is the first in the group, the action traverses to the first item in the previous tab group. The <code>XmNenableButtonTab</code> behavior applies only PushButton, ArrowButton, and DrawnButton.</dd>
<dt>ManagerGadgetSelect():</dt>
<dd>Causes the current gadget to be armed and activated.</dd>
<dt><code>ManagerGadgetTraverseCurrent</code></dt>
<dd>Causes the current gadget to take keyboard focus when <code>Ctrl&lt;Btn1Down&gt;</code> is pressed. Gadget is not activated.</dd>
<dt>ManagerGadgetTraverseDown():</dt>
<dd>Traverses to the next item below the current gadget in the current tab group, wrapping if necessary. The wrapping direction depends on the layout direction of the widget tab group.</dd>
<dt>ManagerGadgetTraverseHome():</dt>
<dd>Traverses to the first widget or gadget in the current tab group.</dd>
<dt>ManagerGadgetTraverseLeft():</dt>
<dd>Traverses to the next item to the left of the current gadget in the current tab group, wrapping if necessary. The wrapping direction depends on the layout direction of the widget tab group.</dd>
<dt>ManagerGadgetTraverseNext():</dt>
<dd>Traverses to the next item in the current tab group, wrapping if necessary. The wrapping direction depends on the layout direction of the widget tab group.</dd>
<dt>ManagerGadgetTraversePrev():</dt>
<dd>Traverses to the previous item in the current tab group, wrapping if necessary. The wrapping direction depends on the layout direction of the widget tab group.</dd>
<dt>ManagerGadgetTraverseRight()</dt>
<dd>Traverses to the next item to the right of the current gadget in the current tab, wrapping if necessary. widget tab group. The wrapping direction depends on the layout direction of the widget tab group.</dd>
<dt>ManagerGadgetTraverseUp():</dt>
<dd>Traverses to the next item above the current gadget in the current tab group, wrapping if necessary. The wrapping direction depends on the layout direction of the widget tab group.</dd>
<dt>ManagerParentActivate():</dt>
<dd>If the parent is a manager, passes the <code>&lt;osfActivate&gt;</code> event received by the current widget/gadget to its parent.</dd>
<dt>ManagerParentCancel():</dt>
<dd>If the parent is a manager, passes the <code>&lt;osfCancel&gt;</code> event received by the current widget/gadget to its parent.</dd></dl>
<h3>Additional Behavior</h3>
<p>This widget has the additional behavior described below:</p>
<dl COMPACT>
<dt><code>&lt;FocusIn&gt;</code>:</dt>
<dd>If the shell&#8217;s keyboard focus policy is <code>XmEXPLICIT</code> and the event occurs in a gadget, causes the gadget to be highlighted and to take the focus.</dd>
<dt><code>&lt;FocusOut&gt;</code>:</dt>
<dd>If the shell&#8217;s keyboard focus policy is <code>XmEXPLICIT</code> and the event occurs in a gadget, causes the gadget to be unhighlighted and to lose the focus.</dd></dl>
<h3>Virtual Bindings</h3>
<p>The bindings for virtual keys are vendor specific. For information about bindings for virtual buttons and keys, see <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-composite/">Composite</a></code>(3), <code><a href="/docs/linux/man/3-constraint/">Constraint</a></code>(3), <code><a href="/docs/linux/man/3-core/">Core</a></code>(3), <code><a href="/docs/linux/man/3-xmdirection/">XmDirection</a></code>(3), <code><a href="/docs/linux/man/3-xmchangecolor/">XmChangeColor</a></code>(3), <code><a href="/docs/linux/man/3-xmgadget/">XmGadget</a></code>(3), and <code><a href="/docs/linux/man/3-xmscreen/">XmScreen</a></code>(3).</p>
