---
title: "xmprimitive(3)"
name: "xmprimitive"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmprimitive/"
description: "XmPrimitive — The Primitive widget class"
---

<p><code>XmPrimitive</code> &#8212; The Primitive widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;</pre>
<h2>Description</h2>
<p>Primitive is a widget class used as a supporting superclass for other widget classes. It handles border drawing and highlighting, traversal activation and deactivation, and various callback lists needed by Primitive widgets. Primitive and all its subclasses hold the <code>XmQTcareParentVisual</code> trait.</p>
<h3>Data Transfer Behavior</h3>
<p>Primitive has no widget class conversion or destination procedure. Subclasses and the <code>XmNconvertCallback</code> procedures are responsible for any conversion of selections. Subclasses and the subclass <code>XmNdestinationCallback</code> procedures are responsible for any data transfers to the widget.</p>
<h3>Classes</h3>
<p>Primitive inherits behavior, resources, and traits from <code>Core</code>. </p>
<p> The class pointer is <code>xmPrimitiveWidgetClass</code>. </p>
<p> The class name is <code>XmPrimitive</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmPrimitive Resource Set</code>
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
<td>XmNhighlightOnEnter</td>
<td>XmCHighlightOnEnter</td>
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
<td>XmNhighlightThickness</td>
<td>XmCHighlightThickness</td>
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
<td>XmNtoolTipString</td>
<td>XmCToolTipString</td>
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
<dt><code>XmNbottomShadowColor</code></p>
<dd>Specifies the color to use to draw the bottom and right sides of the border shadow. This color is used if the <code>XmNtopShadowPixmap</code> resource is unspecified.</p>
<dt><code>XmNbottomShadowPixmap</code></p>
<dd>Specifies the pixmap to use to draw the bottom and right sides of the border shadow.</p>
<dt><code>XmNconvertCallback</code></p>
<dd>Specifies a list of callbacks called when the widget is asked to convert a selection. The type of the structure whose address is passed to these callbacks is <code>XmConvertCallbackStruct</code>. The reason is <code>XmCR_OK</code>.</p>
<dt><code>XmNforeground</code></p>
<dd>Specifies the foreground drawing color used by Primitive widgets.</p>
<dt><code>XmNhelpCallback</code></p>
<dd>Specifies the list of callbacks that is called when the help key is pressed. The reason sent by the callback is <code>XmCR_HELP</code>.</p>
<dt><code>XmNhighlightColor</code></p>
<dd>Specifies the color of the highlighting rectangle. This color is used if the highlight pixmap resource is <code>XmUNSPECIFIED_PIXMAP</code>.</p>
<dt><code>XmNhighlightOnEnter</code></p>
<dd>Specifies if the highlighting rectangle is drawn when the cursor moves into the widget. If the shell&#8217;s focus policy is <code>XmEXPLICIT</code>, this resource is ignored, and the widget is highlighted when it has the focus. If the shell&#8217;s focus policy is <code>XmPOINTER</code> and if this resource is True, the highlighting rectangle is drawn when the cursor moves into the widget. If the shell&#8217;s focus policy is <code>XmPOINTER</code> and if this resource is False, the highlighting rectangle is not drawn when the the cursor moves into the widget. The default is False.</p>
<dt><code>XmNhighlightPixmap</code></p>
<dd>Specifies the pixmap used to draw the highlighting rectangle.</p>
<dt><code>XmNhighlightThickness</code></p>
<dd>Specifies the thickness of the highlighting rectangle.</p>
<dt><code>XmNlayoutDirection</code></p>
<dd>Specifies the direction in which components of the primitive (including strings) are laid out. The values are of type <code>XmDirection</code>. If the widget&#8217;s parent is a primitive or shell, the value is inherited from the widget&#8217;s parent. Otherwise, it is inherited from the closest ancestor vendor or menu shell. Refer to the <code><a href="/docs/linux/man/3-xmdirection/">XmDirection</a></code>(3) reference page for the possible direction values.</p>
<dt><code>XmNnavigationType</code></p>
<dd>Determines whether the widget is a tab group.</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmNONE</code></p>
<dd>Indicates that the widget is not a tab group.</p>
<dt><code>XmTAB_GROUP</code></p>
<dd>Indicates that the widget is a tab group, unless the <code>XmNnavigationType</code> of another widget in the hierarchy is <code>XmEXCLUSIVE_TAB_GROUP</code>.</p>
<dt><code>XmSTICKY_TAB_GROUP</code></p>
<dd>Indicates that the widget is a tab group, even if the <code>XmNnavigationType</code> of another widget in the hierarchy is <code>XmEXCLUSIVE_TAB_GROUP</code>.</p>
<dt><code>XmEXCLUSIVE_TAB_GROUP</code></p>
<dd>Indicates that the widget is a tab group and that widgets in the hierarchy whose <code>XmNnavigationType</code> is <code>XmTAB_GROUP</code> are not tab groups.</p>
<dd>When a parent widget has an <code>XmNnavigationType</code> of <code>XmEXCLUSIVE_TAB_GROUP</code>, traversal of non-tab-group widgets within the group is based on the order of those widgets in their parent&#8217;s <code>XmNchildren</code> list.</p>
<dd>When the <code>XmNnavigationType</code> of any widget in a hierarchy is <code>XmEXCLUSIVE_TAB_GROUP</code>, traversal of tab groups in the hierarchy proceeds to widgets in the order in which their <code>XmNnavigationType</code> resources were specified as <code>XmEXCLUSIVE_TAB_GROUP</code> or <code>XmSTICKY_TAB_GROUP</code>, whether by creating the widgets with that value, by calling <code>XtSetValues</code>, or by calling <code>XmAddTabGroup</code>.</dl>
</dl>
<dt><code>XmNpopupHandlerCallback</code></p>
<dd>Allows the application to control which popup menu will be automatically posted. The reason can either be <code>XmCR_POST</code> or <code>XmCR_REPOST:</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmCR_POST</code></p>
<dd>Indicates that this is a regular posting request.</p>
<dt><code>XmCR_REPOST</code></p>
<dd>Indicates that the menu was just unposted and that this callback was invoked on a replay.</dl>
</dl>
<dd>This callback uses the <code>XmPopupHandlerCallbackStruct</code> structure to pass information.</p>
<dt><code>XmNshadowThickness</code></p>
<dd>Specifies the size of the drawn border shadow.</p>
<dt><code>XmNtoolTipString</code></p>
<dd>The XmString to display as the toolTip. If this resource is NULL, no tip will be displayed. ToolTips are described in <a href="/docs/linux/man/3-vendorshell/">VendorShell</a>(3) </p>
<dt><code>XmNtopShadowColor</code></p>
<dd>Specifies the color to use to draw the top and left sides of the border shadow. This color is used if the <code>XmNtopShadowPixmap</code> resource is unspecified. If a default top shadow pixmap exists, it will need to be removed for the <code>XmNtopShadowColor</code> to take effect.</p>
<dt><code>XmNtopShadowPixmap</code></p>
<dd>Specifies the pixmap to use to draw the top and left sides of the border shadow. A Primitive top shadow pixmap is created in two situations. In either of these situations, a default 50-foreground top shadow pixmap is created.</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd>If the Primitive top shadow color is the same as the Core background pixel color.</p>
<dt> &bull;</p>
<dd>If the depth of the screen is only one.</dl>
</dl>
<dd>For example, if a widget with the same top shadow and background color is created, a default shadow pixmap is generated. Such a pixmap needs to be removed for the <code>XmNtopShadowColor</code> resource to take effect.</p>
<dt><code>XmNtraversalOn</code></p>
<dd>Specifies if traversal is activated for this widget. In CascadeButton and CascadeButtonGadget, this resource is forced to True unless the parent is an OptionMenu.</p>
<dt><code>XmNunitType</code></p>
<dd>Provides the basic support for resolution independence. It defines the type of units a widget uses with sizing and positioning resources. If the widget&#8217;s parent is a subclass of <code>XmManager</code> and if the <code>XmNunitType</code> resource is not explicitly set, it defaults to the unit type of the parent widget. If the widget&#8217;s parent is not a subclass of <code>XmManager</code>, the resource has a default unit type of <code>XmPIXELS</code>.</p>
<dd>The unit type can also be specified in resource files, with the following format:</dl>
<pre><tt></tt><i>&lt;floating value&gt;&lt;unit&gt;</i></pre>
<dl COMPACT>
<dd>where:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><i>unit</i></p>
<dd>is &lt;&quot; &quot;, pixels, inches, centimeters, millimeters, points, font units&gt;</p>
<dt><i>pixels</i></p>
<dd>is &lt;<i>pix</i>, <i>pixel</i>, <i>pixels</i>&gt;</p>
<dt><i>inches</i></p>
<dd>is &lt;<i>in</i>, <i>inch</i>, <i>inches</i>&gt;</p>
<dt><i>centimeter</i></p>
<dd>is &lt;<i>cm</i>, <i>centimeter</i>, <i>centimeters</i>&gt;</p>
<dt><i>millimeters</i></p>
<dd>is &lt;<i>mm</i>, <i>millimeter</i>, <i>millimeters</i>&gt;</p>
<dt><code>points</code></p>
<dd>is &lt;<i>pt</i>, <i>point</i>, <i>points</i>&gt;</p>
<dt><code>font units</code></p>
<dd>is &lt;<i>fu</i>, <code>font_unit</code>, <code>font_units</code>&gt;</p>
<dt><i>float</i></p>
<dd>is {&quot;+&quot;|&quot;-&quot;}&#123;&#123;&lt;&quot;0&quot;-&quot;9&quot;&gt;*}.}&lt;&quot;0&quot;-&quot;9&quot;&gt;*</p>
<dd>Note that the type Dimension must always be positive.</dl>
</dl>
<dd>For example,</dl>
<pre><tt>xmfonts*XmMainWindow.height: 10.4cm
*PostIn.width: 3inches</tt></pre>
<dl COMPACT>
<dd><code>XmNunitType</code> can have the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmPIXELS</code></p>
<dd>All values provided to the widget are treated as normal pixel values.</p>
<dt><code>XmMILLIMETERS</code></p>
<dd>All values provided to the widget are treated as normal millimeter values.</p>
<dt><code>Xm100TH_MILLIMETERS</code></p>
<dd>All values provided to the widget are treated as 1/100 of a millimeter.</p>
<dt><code>XmCENTIMETERS</code></p>
<dd>All values provided to the widget are treated as normal centimeter values.</p>
<dt><code>XmINCHES</code></p>
<dd>All values provided to the widget are treated as normal inch values.</p>
<dt><code>Xm1000TH_INCHES</code></p>
<dd>All values provided to the widget are treated as 1/1000 of an inch.</p>
<dt><code>XmPOINTS</code></p>
<dd>All values provided to the widget are treated as normal point values. A point is a unit used in text processing applications and is defined as 1/72 of an inch.</p>
<dt><code>Xm100TH_POINTS</code></p>
<dd>All values provided to the widget are treated as 1/100 of a point. A point is a unit used in text processing applications and is defined as 1/72 of an inch.</p>
<dt><code>XmFONT_UNITS</code></p>
<dd>All values provided to the widget are treated as normal font units. A font unit has horizontal and vertical components. These are the values of the XmScreen resources <code>XmNhorizontalFontUnit</code> and <code>XmNverticalFontUnit</code>.</p>
<dt><code>Xm100TH_FONT_UNITS</code></p>
<dd>All values provided to the widget are treated as 1/100 of a font unit. A font unit has horizontal and vertical components. These are the values of the <code>XmScreen</code> resources <code>XmNhorizontalFontUnit</code> and <code>XmNverticalFontUnit</code>.</dl>
</dl>
<dt><code>XmNuserData</code></p>
<dd>Allows the application to attach any necessary specific data to the widget. It is an internally unused resource. </p>
</dl>
<h3>Dynamic Color Defaults</h3>
<p>The foreground, background, top shadow, bottom shadow, and highlight color resources are dynamically defaulted. If no color data is specified, the colors are automatically generated. On a single-plane system, a black and white color scheme is generated. Otherwise, four colors are generated, which display the correct shading for the 3-D visuals. If the background is the only color specified for a widget, the top shadow and bottom shadow colors are generated to give the 3-D appearance. Foreground and highlight colors are generated to provide sufficient contrast with the background color. </p>
<p> Colors are generated only at creation. Resetting the background through <code>XtSetValues</code> does not regenerate the other colors. <code>XmChangeColor</code> can be used to recalculate all associated colors based on a new background color.</p>
<h3>Inherited Resources</h3>
<p>Primitive inherits behavior and resources from the superclass described in the following table. For a complete description of each resource, refer to the reference page for that superclass. </p>
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
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked. For this callback, <i>reason</i> is set to <code>XmCR_HELP</code>.</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the callback.</dl>
<p> A pointer to the following callback structure is passed to the <code>XmNconvertCallback</code> procedures: </p>
<pre>typedef struct
{
 int <i>reason</i>;
 XEvent *<i>event</i>;
 Atom <i>selection</i>;
 Atom <i>target</i>;
 XtPointer <i>source_data</i>;
 XtPointer location_data;
 int <i>flags</i>;
 XtPointer <i>parm</i>;
 int <i>parm_format</i>;
 unsigned long <i>parm_length</i>;
 Atom <i>parm_type</i>;
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
<dd>Contains information about the location of data to be converted. If the value is NULL, the data to be transferred consists of the widget&#8217;s current selection. Otherwise, the type and interpretation of the value are specific to the widget class.</p>
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
<dt><i>parm_type</i></p>
<dd>Specifies the parameter type of <i>parm</i>.</p>
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
<dd>An IN/OUT parameter that contains any data that the callback procedure produces as a result of the conversion. The initial value is NULL. If the callback procedure sets this member, it must ensure that the <i>type</i>, <i>format</i>, and <i>length</i> members correspond to the data in <i>value</i>. The callback procedure is responsible for allocating memory when it sets this member. The toolkit frees this memory when it is no longer needed.</p>
<dt><i>type</i></p>
<dd>An IN/OUT parameter that indicates the type of the data in the <i>value</i> member. The initial value is <code>INTEGER</code>.</p>
<dt><i>format</i></p>
<dd>An IN/OUT parameter that specifies whether the data in <i>value</i> should be viewed as a list of <i>char</i>, <i>short</i>, or <i>long</i> quantities. The initial value is 8. The callback procedure can set this member to 8 (for a list of <i>char</i>), 16 (for a list of <i>short</i>), or 32 (for a list of <i>long</i>).</p>
<dt><i>length</i></p>
<dd>An IN/OUT member that specifies the number of elements of data in <i>value</i>, where each element has the size symbolized by <i>format</i>. The initial value is 0.</dl>
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
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked.</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the handler.</p>
<dt><i>menuToPost</i></p>
<dd>Specifies the popup menu that the menu system believes should be posted. The application may modify this field.</p>
<dt><i>postIt</i></p>
<dd>Indicates whether the posting process should continue. The application may modify this field.</p>
<dt><i>target</i></p>
<dd>Specifies the most specific widget or gadget that the menu sytem found from the event that matches the event.</dl>
<h3>Translations</h3>
<p>The <code>XmPrimitive</code> translations are listed below. </p>
<p> Note that for buttons in menus, altering translations in <code>#override</code> or <code>#augment</code> mode is undefined. </p>
<p> The following key names are listed in the X standard key event translation table syntax. This format is the one used by Motif to specify the widget actions corresponding to a given key. A brief overview of the format is provided under <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3). For a complete description of the format, please refer to the X Toolkit Instrinsics Documentation.</p>
<dl COMPACT>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfActivate&gt;</code>:</p>
<dd>PrimitiveParentActivate()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfCancel&gt;</code>:</p>
<dd>PrimitiveParentCancel()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfBeginLine&gt;</code>:</p>
<dd>PrimitiveTraverseHome()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfUp&gt;</code>:</p>
<dd>PrimitiveTraverseUp()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfDown&gt;</code>:</p>
<dd>PrimitiveTraverseDown()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfLeft&gt;</code>:</p>
<dd>PrimitiveTraverseLeft()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfRight&gt;</code>:</p>
<dd>PrimitiveTraverseRight()</p>
<dt><code>&asymp;s &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>Return</code>:</p>
<dd>PrimitiveParentActivate()</p>
<dt><code>s &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>Tab</code>:</p>
<dd>PrimitivePrevTabGroup()</p>
<dt><code>&asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>Tab</code>:</p>
<dd>PrimitiveNextTabGroup()</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfHelp&gt;</code>:</p>
<dd>PrimitiveHelp()</dl>
<h3>Action Routines</h3>
<p>The <code>XmPrimitive</code> action routines are</p>
<dl COMPACT>
<dt>PrimitiveHelp():</p>
<dd>Calls the callbacks for <code>XmNhelpCallback</code> if any exist. If there are no help callbacks for this widget, this action calls the help callbacks for the nearest ancestor that has them.</p>
<dt>PrimitiveNextTabGroup():</p>
<dd>This action depends on the value of the Display resource <code>XmNenableButtonTab</code>. When <code>XmNenableButtonTab</code> is False (default), this action traverses to the first item in the next tab group. If the current tab group is the last entry in the tab group list, it wraps to the beginning of the tab group list.</p>
<dd>When <code>XmNenableButtonTab</code> is True, this action moves to the next item within the current tab group, unless it is the last item in the tab group. When the item is the last in the group, the action traverses to the first item in the next tab group. The <code>XmNenableButtonTab</code> behavior applies only to PushButton, ArrowButton, and DrawnArrow.</p>
<dt>PrimitiveParentActivate():</p>
<dd>If the parent is a manager, passes the <code>KActivate</code> event received by the widget to the parent.</p>
<dt>PrimitiveParentCancel():</p>
<dd>If the parent is a manager, passes the <code>KCancel</code> event received by the widget to the parent.</p>
<dt>PrimitivePrevTabGroup():</p>
<dd>This action depends on the value of the Display resource <code>XmNenableButtonTab</code>. When <code>XmNenableButtonTab</code> is False (default), this action traverses to the first item in the previous tab group. If the beginning of the tab group list is reached, it wraps to the end of the tab group list.</p>
<dd>When <code>XmNenableButtonTab</code> is True, this action moves to the previous item within the current tab group unless it is the first item in the tab group. When the item is the first in the group, the action traverses to the first item in the previous tab group. The <code>XmNenableButtonTab</code> behavior applies only PushButton, ArrowButton, and DrawnButton.</p>
<dt>PrimitiveTraverseDown():</p>
<dd>Traverses to the next item below the current widget in the current tab group, wrapping if necessary. The wrapping direction depends on the layout direction of the widget tab group.</p>
<dt>PrimitiveTraverseHome():</p>
<dd>Traverses to the first widget or gadget in the current tab group.</p>
<dt>PrimitiveTraverseLeft():</p>
<dd>Traverses to the next item to the left of the current widget in the current tab group, wrapping if necessary. The wrapping direction depends on the layout direction of the widget tab group.</p>
<dt>PrimitiveTraverseNext():</p>
<dd>Traverses to the next item in the current tab group, wrapping if necessary. The wrapping direction depends on the layout direction of the widget tab group.</p>
<dt>PrimitiveTraversePrev():</p>
<dd>Traverses to the previous item in the current tab group, wrapping if necessary. The wrapping direction depends on the layout direction of the widget tab group.</p>
<dt>PrimitiveTraverseRight():</p>
<dd>Traverses to the next item to the right of the current gadget in the current tab group, wrapping if necessary. The wrapping direction depends on the layout direction of the widget tab group.</p>
<dt>PrimitiveTraverseUp():</p>
<dd>Traverses to the next item above the current gadget in the current tab group, wrapping if necessary. The wrapping direction depends on the layout direction of the widget tab group.</dl>
<h3>Additional Behavior</h3>
<p>This widget has the following additional behavior:</p>
<dl COMPACT>
<dt><code>&lt;FocusIn&gt;</code>:</p>
<dd>If the shell&#8217;s keyboard focus policy is <code>XmEXPLICIT</code>, highlights the widget and gives it the focus</p>
<dt><code>&lt;FocusOut&gt;</code>:</p>
<dd>If the shell&#8217;s keyboard focus policy is <code>XmEXPLICIT</code>, unhighlights the widget and removes the focus</dl>
<h3>Virtual Bindings</h3>
<p>The bindings for virtual keys are vendor specific. For information about bindings for virtual buttons and keys, see <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-core/">Core</a></code>(3), <code><a href="/docs/linux/man/3-xmdirection/">XmDirection</a></code>(3), <code><a href="/docs/linux/man/3-xmchangecolor/">XmChangeColor</a></code>(3), and <code><a href="/docs/linux/man/3-xmscreen/">XmScreen</a></code>(3).</p>
