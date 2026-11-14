---
title: "xmgadget(3)"
name: "xmgadget"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmgadget/"
description: "XmGadget — The Gadget widget class"
---

<p><code>XmGadget</code> &#8212; The Gadget widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;</pre>
<h2>Description</h2>
<p>Gadget is a widget class used as a supporting superclass for other gadget classes. It handles shadow-border drawing and highlighting, traversal activation and deactivation, and various callback lists needed by gadgets. </p>
<p> The color and pixmap resources defined by <code>XmManager</code> are directly used by gadgets. If <code>XtSetValues</code> is used to change one of the resources for a manager widget, all of the gadget children within the manager also change.</p>
<h3>Classes</h3>
<p>Gadget inherits behavior and resources from <code>Object</code> and <code>RectObj</code>. </p>
<p> The class pointer is <code>xmGadgetClass</code>. </p>
<p> The class name is <code>XmGadget</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a .Xdefaults file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a .Xdefaults file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmGadget Resource Set</code>
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
<td>XmNCLayoutDirection</td>
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
</table>
</table>
<dl COMPACT>
<dt><code>XmNbackground</code></p>
<dd>Specifies the background color for the gadget.</p>
<dt><code>XmNbackgroundPixmap</code></p>
<dd>Specifies a pixmap for tiling the background. The first tile is placed at the upper left corner of the widget&#8217;s window.</p>
<dt><code>XmNbottomShadowColor</code></p>
<dd>Contains the color to use to draw the bottom and right sides of the border shadow.</p>
<dt><code>XmNbottomShadowPixmap</code></p>
<dd>Specifies the pixmap to use to draw the bottom and right sides of the border shadow.</p>
<dt><code>XmNforeground</code></p>
<dd>Specifies the foreground drawing color used by Primitive widgets.</p>
<dt><code>XmNhelpCallback</code></p>
<dd>Specifies the list of callbacks that is called when the help key sequence is pressed. The reason sent by the callback is <code>XmCR_HELP</code>.</p>
<dt><code>XmNhighlightColor</code></p>
<dd>Contains the color of the highlighting rectangle.</p>
<dt><code>XmNhighlightOnEnter</code></p>
<dd>Specifies if the highlighting rectangle is drawn when the cursor moves into the widget. If the shell&#8217;s focus policy is <code>XmEXPLICIT</code>, this resource is ignored, and the widget is highlighted when it has the focus. If the shell&#8217;s focus policy is <code>XmPOINTER</code> and if this resource is True, the highlighting rectangle is drawn when the the cursor moves into the widget. If the shell&#8217;s focus policy is <code>XmPOINTER</code> and if this resource is False, the highlighting rectangle is not drawn when the the cursor moves into the widget. The default is False.</p>
<dt><code>XmNhighlightPixmap</code></p>
<dd>Specifies the pixmap used to draw the highlighting rectangle.</p>
<dt><code>XmNhighlightThickness</code></p>
<dd>Specifies the thickness of the highlighting rectangle.</p>
<dt><code>XmNlayoutDirection</code></p>
<dd>Specifies the direction in which components of the manager (including strings) are laid out. The values are of type <code>XmDirection</code>. If the widget&#8217;s parent is a manager or shell, the value is inherited from the widget&#8217;s parent. Otherwise, it is inherited from the closest ancestor vendor or menu shell.</p>
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
<dt><code>XmNshadowThickness</code></p>
<dd>Specifies the size of the drawn border shadow.</p>
<dt><code>XmNtopShadowColor</code></p>
<dd>Contains the color to use to draw the top and left sides of the border shadow.</p>
<dt><code>XmNtopShadowPixmap</code></p>
<dd>Specifies the pixmap to use to draw the top and left sides of the border shadow.</p>
<dt><code>XmNtraversalOn</code></p>
<dd>Specifies traversal activation for this gadget.</p>
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
<dd>All values provided to the widget are treated as 1/100 of a point. A point is a unit used in text processing applications and is defined as 1/72 inch.</p>
<dt><code>XmFONT_UNITS</code></p>
<dd>All values provided to the widget are treated as normal font units. A font unit has horizontal and vertical components. These are the values of the XmScreen resources <code>XmNhorizontalFontUnit</code> and <code>XmNverticalFontUnit</code>.</p>
<dt><code>Xm100TH_FONT_UNITS</code></p>
<dd>All values provided to the widget are treated as 1/100 of a font unit. A font unit has horizontal and vertical components. These are the values of the XmScreen resources <code>XmNhorizontalFontUnit</code> and <code>XmNverticalFontUnit</code>.</dl>
</dl>
<dt><code>XmNuserData</code></p>
<dd>Allows the application to attach any necessary specific data to the gadget. This is an internally unused resource. </p>
<dt><code>XmNtoolTipString</code></p>
<dd>The XmString to display as the toolTip. If this resource is NULL, no tip will be displayed. ToolTips are described in <a href="/docs/linux/man/3-vendorshell/">VendorShell</a>(3) </p>
</dl>
<h3>Inherited Resources</h3>
<p>Gadget inherits resources from the superclass described in the following table. For a complete description of each resource, refer to the reference page for that superclass. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>RectObj Resource Set</code>
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
<td>XmNborderWidth</td>
<td>XmCBorderWidth</td>
<td>Dimension</td>
<td>0</td>
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
<td ALIGN=center COLSPAN=5><code>Object Resource Set</code>
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
</table>
</table>
<h3>Callback Information</h3>
<p>A pointer to the following structure is passed to each callback: </p>
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
<h3>Behavior</h3>
<p>Gadgets cannot have translations associated with them. Because of this, a Gadget&#8217;s behavior is determined by the Manager widget into which the Gadget is placed. If focus is on a Gadget, events are passed to the Gadget by its Manager.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-object/">Object</a></code>(3), <code><a href="/docs/linux/man/3-rectobj/">RectObj</a></code>(3), <code><a href="/docs/linux/man/3-xmmanager/">XmManager</a></code>(3), and <code><a href="/docs/linux/man/3-xmscreen/">XmScreen</a></code>(3).</p>
