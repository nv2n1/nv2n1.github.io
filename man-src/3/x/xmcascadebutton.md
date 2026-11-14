---
title: "xmcascadebutton(3)"
name: "xmcascadebutton"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcascadebutton/"
description: "XmCascadeButton — The CascadeButton widget class"
---

<p><code>XmCascadeButton</code> &#8212; The CascadeButton widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/CascadeB.h&gt;</pre>
<h2>Description</h2>
<p>CascadeButton links two menu panes or a MenuBar to a menu pane. </p>
<p> It is used in menu systems and must have a RowColumn parent with its <code>XmNrowColumnType</code> resource set to <code>XmMENU_BAR</code>, <code>XmMENU_POPUP</code> or <code>XmMENU_PULLDOWN</code>. </p>
<p> It is the only widget that can have a Pulldown menu pane attached to it as a submenu. The submenu is displayed when this widget is activated within a MenuBar, a PopupMenu, or a PulldownMenu. Its visuals can include a label or pixmap and a cascading indicator when it is in a Popup or Pulldown menu pane; or it can include only a label or a pixmap when it is in a MenuBar. The positioning of the PulldownMenu with respect to the CascadeButton depends on the <code>XmNlayoutDirection</code> resource of the MenuShell. </p>
<p> The default behavior associated with a CascadeButton depends on the type of menu system in which it resides. By default, <code>BSelect</code> controls the behavior of the CascadeButton. In addition, <code>BMenu</code> controls the behavior of the CascadeButton if it resides in a PopupMenu system. The actual mouse button used is determined by its RowColumn parent. <code>BMenu</code> also performs the <code>BSelect</code> actions in all types of menu systems. </p>
<p> A CascadeButton&#8217;s visuals differ from most other button gadgets. When the button becomes armed, its visuals change from a 2-D to a 3-D look, and it displays the submenu that has been attached to it. If no submenu is attached, it simply changes its visuals. </p>
<p> When a CascadeButton within a Pulldown or Popup menu pane is armed as the result of the user moving the mouse pointer into the widget, it does not immediately display its submenu. Instead, it waits a short amount of time to see if the arming was temporary (that is, the user was simply passing through the widget), or whether the user really wanted the submenu posted. This time delay is configurable using <code>XmNmappingDelay</code>. </p>
<p> CascadeButton provides a single mechanism for activating the widget from the keyboard. This mechanism is referred to as a keyboard mnemonic. If a mnemonic has been specified for the widget, the user may activate the CascadeButton by simply typing the mnemonic while the CascadeButton is visible. If the CascadeButton is in a MenuBar and the MenuBar does not have the focus, the <code>MAlt</code> modifier must be pressed with the mnemonic. Mnemonics are typically used to interact with a menu using the keyboard interface. </p>
<p> If the Cascadebutton is in a Pulldown or Popup menu pane and there is a submenu attached, the <code>XmNmarginBottom</code>, <code>XmNmarginLeft</code>, <code>XmNmarginRight</code>, and <code>XmNmarginTop</code> resources may enlarge to accommodate <code>XmNcascadePixmap</code>. <code>XmNmarginWidth</code> defaults to 6 if this resource is in a MenuBar; otherwise, it takes Label&#8217;s default, which is 2. </p>
<p> CascadeButton uses the <code>XmQTmenuSystem</code> and <code>XmQTspecifyRenderTable</code> traits.</p>
<h3>Classes</h3>
<p>CascadeButton inherits behavior, resources, and traits from <code>Core</code>, <code>XmPrimitive</code>, and <code>XmLabel</code> classes. </p>
<p> The class pointer is <code>xmCascadeButtonWidgetClass</code>. </p>
<p> The class name is <code>XmCascadeButton</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmCascadeButton Resource Set</code>
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
<td>XmNactivateCallback</td>
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
<td>XmNcascadePixmap</td>
<td>XmCPixmap</td>
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
<td>XmNcascadingCallback</td>
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
<td>XmNmappingDelay</td>
<td>XmCMappingDelay</td>
<td>int</td>
<td>180 ms</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNsubMenuId</td>
<td>XmCMenuWidget</td>
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
<dt><code>XmNactivateCallback</code></p>
<dd>Specifies the list of callbacks that is called when the user activates the CascadeButton widget and there is no submenu attached to pop up. The activation occurs when a mouse button is released or when the mnemonic associated with the widget is typed. The specific mouse button depends on information in the RowColumn parent. The reason sent by the callback is <code>XmCR_ACTIVATE</code>.</p>
<dt><code>XmNcascadePixmap</code></p>
<dd>Specifies the cascade pixmap displayed on one end of the widget when a CascadeButton is used within a Popup or Pulldown menu pane and a submenu is attached. The Label class resources <code>XmNmarginBottom</code>, <code>XmNmarginLeft</code>, <code>XmNmarginRight</code>, and <code>XmNmarginTop</code> may be modified to ensure that room is left for the cascade pixmap. The default cascade pixmap is an arrow pointing to the side of the menu where the submenu will appear. The positioning of the cascade pixmap to either the left of right of the widget, and the direction of the arrow, depend on the <code>XmNlayoutDirection</code> resource of the MenuShell.</p>
<dt><code>XmNcascadingCallback</code></p>
<dd>Specifies the list of callbacks that is called just prior to the mapping of the submenu associated with CascadeButton. The reason sent by the callback is <code>XmCR_CASCADING</code>.</p>
<dt><code>XmNmappingDelay</code></p>
<dd>Specifies the amount of time, in milliseconds, between when a CascadeButton becomes armed and when it maps its submenu. This delay is used only when the widget is within a Popup or Pulldown menu pane. The value must not be negative.</p>
<dt><code>XmNsubMenuId</code></p>
<dd>Specifies the widget ID for the Pulldown menu pane to be associated with this CascadeButton. The specified menu pane is displayed when the CascadeButton becomes armed. The menu pane must have been created with the appropriate parentage depending on the type of menu used. See <code><a href="/docs/linux/man/3-xmcreatemenubar/">XmCreateMenuBar</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatepulldownmenu/">XmCreatePulldownMenu</a></code>(3), and <code><a href="/docs/linux/man/3-xmcreatepopupmenu/">XmCreatePopupMenu</a></code>(3) for more information on the menu systems.</dl>
<h3>Inherited Resources</h3>
<p>CascadeButton inherits behavior and resources from the superclasses described in the following tables. For a complete description of each resource, refer to the reference page for that superclass. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmLabel Resource Set</code>
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
<td>XmNaccelerator</td>
<td>XmCAccelerator</td>
<td>String</td>
<td>NULL</td>
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
<td>XmNacceleratorText</td>
<td>XmCAcceleratorText</td>
<td>XmString</td>
<td>NULL</td>
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
<td>XmNalignment</td>
<td>XmCAlignment</td>
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
<td>XmNfontList</td>
<td>XmCFontList</td>
<td>XmFontList</td>
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
<td>XmNlabelInsensitivePixmap</td>
<td>XmCLabelInsensitivePixmap</td>
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
<td>XmNlabelPixmap</td>
<td>XmCLabelPixmap</td>
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
<td>XmNlabelString</td>
<td>XmCXmString</td>
<td>XmString</td>
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
<td>XmNlabelType</td>
<td>XmCLabelType</td>
<td>unsigned char</td>
<td>XmSTRING</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNmarginBottom</td>
<td>XmCMarginBottom</td>
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
<td>XmNmarginHeight</td>
<td>XmCMarginHeight</td>
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
<td>XmNmarginLeft</td>
<td>XmCMarginLeft</td>
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
<td>XmNmarginRight</td>
<td>XmCMarginRight</td>
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
<td>XmNmarginTop</td>
<td>XmCMarginTop</td>
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
<td>XmNmarginWidth</td>
<td>XmCMarginWidth</td>
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
<td>XmNmnemonic</td>
<td>XmCMnemonic</td>
<td>KeySym</td>
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
<td>XmNmnemonicCharSet</td>
<td>XmCMnemonicCharSet</td>
<td>String</td>
<td>XmFONTLIST_DEFAULT_TAG</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNrecomputeSize</td>
<td>XmCRecomputeSize</td>
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
<td>XmNstringDirection</td>
<td>XmCStringDirection</td>
<td>XmStringDirection</td>
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
<h3>Callback Information</h3>
<p>A pointer to the following structure is passed to each callback: </p>
<pre>typedef struct
{
 int <i>reason</i>;
 XEvent <i>* event</i>;
} XmAnyCallbackStruct;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the callback or is NULL if this callback was not triggered due to an <code>XEvent</code></dl>
<h3>Translations</h3>
<p><code>XmCascadeButton</code> includes translations from <code>XmPrimitive</code>. <code>XmCascadeButton</code> includes the menu traversal translations from <code>XmLabel</code>. </p>
<p> Note that altering translations in <code>#override</code> or <code>#augment</code> mode is undefined. </p>
<p> The following list describes the translations for a CascadeButton in a MenuBar. The following key names are listed in the X standard key event translation table syntax. This format is the one used by Motif to specify the widget actions corresponding to a given key. A brief overview of the format is provided under <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3). For a complete description of the format, please refer to the X Toolkit Instrinsics Documentation.</p>
<dl COMPACT>
<dt><code>&lt;EnterWindow&gt;</code><code>Normal</code>:</p>
<dd>MenuBarEnter()</p>
<dt><code>&lt;LeaveWindow&gt;</code><code>Normal</code>:</p>
<dd>MenuBarLeave()</p>
<dt><code>&lt;Btn2Down&gt;</code>:</p>
<dd>ProcessDrag()</p>
<dt><code>c&lt;BtnDown&gt;</code>:</p>
<dd>MenuButtonTakeFocusUp()</p>
<dt><code>c&lt;BtnUp&gt;</code>:</p>
<dd>MenuButtonTakeFocusUp()</p>
<dt><code>&asymp;c</code><code>&lt;BtnDown&gt;</code>:</p>
<dd>MenuBarSelect()</p>
<dt><code>&asymp;c</code><code>&lt;BtnUp&gt;</code>:</p>
<dd>DoSelect()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfSelect&gt;</code>:</p>
<dd>KeySelect()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfActivate&gt;</code>:</p>
<dd>KeySelect()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfHelp&gt;</code>:</p>
<dd>Help()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfCancel&gt;</code>:</p>
<dd>CleanupMenuBar()</p>
<dt><code>&asymp;s</code><code>&lt;Key&gt;</code><code>Return</code>:</p>
<dd>KeySelect()</p>
<dt><code>&asymp;s</code><code>&lt;Key&gt;</code><code>space</code>:</p>
<dd>KeySelect()</dl>
<p> The following list describes the translations for a CascadeButton in a PullDown or Popup MenuPane. In a Popup menu system, <code>&lt;Btn3&gt;</code> also performs the <code>&lt;Btn1&gt;</code> actions.</p>
<dl COMPACT>
<dt><code>&lt;EnterWindow&gt;</code>:</p>
<dd>DelayedArm()</p>
<dt><code>&lt;LeaveWindow&gt;</code>:</p>
<dd>CheckDisarm()</p>
<dt><code>&lt;Btn2Down&gt;</code>:</p>
<dd>ProcessDrag()</p>
<dt><code>c&lt;BtnDown&gt;</code>:</p>
<dd>MenuButtonTakeFocus()</p>
<dt><code>c&lt;BtnUp&gt;</code>:</p>
<dd>MenuButtonTakeFocusUp()</p>
<dt><code>&asymp;c</code><code>&lt;BtnDown&gt;</code>:</p>
<dd>StartDrag()</p>
<dt><code>&asymp;c</code><code>&lt;BtnUp&gt;</code>:</p>
<dd>DoSelect()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfSelect&gt;</code>:</p>
<dd>KeySelect()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfActivate&gt;</code>:</p>
<dd>KeySelect()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfHelp&gt;</code>:</p>
<dd>Help()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfCancel&gt;</code>:</p>
<dd>CleanupMenuBar()</p>
<dt><code>&asymp;s</code><code>&lt;Key&gt;</code><code>Return</code>:</p>
<dd>KeySelect()</p>
<dt><code>&asymp;s</code><code>&lt;Key&gt;</code><code>space</code>:</p>
<dd>KeySelect()</dl>
<h3>Action Routines</h3>
<p>The XmCascadeButton action routines are</p>
<dl COMPACT>
<dt>CleanupMenuBar():</p>
<dd>In a MenuBar, disarms the CascadeButton and the menu and, when the shell&#8217;s keyboard focus policy is <code>XmEXPLICIT</code>, restores keyboard focus to the widget that had the focus before the menu was entered.</p>
<dd>In a toplevel Pulldown MenuPane from a MenuBar, unposts the menu, disarms the MenuBar CascadeButton and the MenuBar, and, when the shell&#8217;s keyboard focus policy is <code>XmEXPLICIT</code>, restores keyboard focus to the widget that had the focus before the MenuBar was entered. In other Pulldown MenuPanes, unposts the menu.</p>
<dd>In a Popup MenuPane, unposts the menu and, when the shell&#8217;s keyboard focus policy is <code>XmEXPLICIT</code>, restores keyboard focus to the widget from which the menu was posted.</p>
<dt>DoSelect():</p>
<dd>Calls the callbacks in <code>XmNcascadingCallback</code>, posts the submenu attached to the CascadeButton and enables keyboard traversal within the menu. If the CascadeButton does not have a submenu attached, this action calls the callbacks in <code>XmNactivateCallback</code>, activates the CascadeButton, and unposts all posted menus in the cascade.</p>
<dt>Help():</p>
<dd>Unposts all menus in the menu hierarchy and, when the shell&#8217;s keyboard focus policy is <code>XmEXPLICIT</code>, restores keyboard focus to the widget that had the focus before the menu system was entered. Calls the callbacks for <code>XmNhelpCallback</code> if any exist. If there are no help callbacks for this widget, this action calls the help callbacks for the nearest ancestor that has them.</p>
<dt>KeySelect():</p>
<dd>Calls the callbacks in <code>XmNcascadingCallback</code>, and posts the submenu attached to the CascadeButton if keyboard traversal is enabled in the menu. If the CascadeButton does not have a submenu attached, this action calls the callbacks in <code>XmNactivateCallback</code>, activates the CascadeButton, and unposts all posted menus in the cascade.</p>
<dt>MenuBarSelect():</p>
<dd>Unposts any menus posted by the parent menu. Arms both the CascadeButton and the MenuBar, posts the associated submenu, and enables mouse traversal. If the menu is already active, this event disables keyboard traversal for the menu and returns the menu to mouse traversal mode.</p>
<dt>StartDrag():</p>
<dd>Arms the CascadeButton, posts the associated submenu, and enables mouse traversal. If the menu is already active, this event disables keyboard traversal for the menu and returns the menu to mouse traversal mode.</dl>
<h3>Additional Behavior</h3>
<p>Posting a submenu calls the <code>XmNcascadingCallback</code> callbacks. This widget has the following additional behavior:</p>
<dl COMPACT>
<dt><code>&lt;EnterWindow&gt;</code>:</p>
<dd>If keyboard traversal is enabled, does nothing. Otherwise, in a MenuBar that is armed, unposts any MenuPanes associated with another MenuBar entry, arms the CascadeButton, and posts the associated submenu. In other menus, arms the CascadeButton and posts the associated submenu after the delay specified by <code>XmNmappingDelay</code>.</p>
<dt><code>&lt;LeaveWindow&gt;</code>:</p>
<dd>If keyboard traversal is enabled does nothing. Otherwise, in a MenuBar that is armed, disarms the CascadeButton if the submenu associated with the CascadeButton is not currently posted or if there is no submenu associated with the CascadeButton.</p>
<dd>In other menus, if the pointer moves anywhere except into a submenu associated with the CascadeButton, the CascadeButton is disarmed and its submenu is unposted.</dl>
<h3>Virtual Bindings</h3>
<p>The bindings for virtual keys are vendor specific. For information about bindings for virtual buttons and keys, see <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-core/">Core</a></code>(3), <code><a href="/docs/linux/man/3-xmcascadebuttonhighlight/">XmCascadeButtonHighlight</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatecascadebutton/">XmCreateCascadeButton</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatemenubar/">XmCreateMenuBar</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatepulldownmenu/">XmCreatePulldownMenu</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatepopupmenu/">XmCreatePopupMenu</a></code>(3), <code><a href="/docs/linux/man/3-xmlabel/">XmLabel</a></code>(3), <code><a href="/docs/linux/man/3-xmprimitive/">XmPrimitive</a></code>(3), <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatecascadebutton/">XmVaCreateCascadeButton</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatemanagedcascadebutton/">XmVaCreateManagedCascadeButton</a></code>(3).</p>
