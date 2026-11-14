---
title: "xmrowcolumn(3)"
name: "xmrowcolumn"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmrowcolumn/"
description: "XmRowColumn — The RowColumn widget class"
---

<p><code>XmRowColumn</code> &#8212; The RowColumn widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/RowColumn.h&gt;</pre>
<h2>Description</h2>
<p>The RowColumn widget is a general purpose RowColumn manager capable of containing any widget type as a child. In general, it requires no special knowledge about how its children function and provides nothing beyond support for several different layout styles. However, it can be configured as a menu, in which case, it expects only certain children, and it configures to a particular layout. The menus supported are MenuBar, Pulldown or Popup menu panes, and OptionMenu. RowColumn uses the <code>XmQTmenuSavvy</code> trait and holds the <code>XmQTmenuSystem</code> trait. </p>
<p> The type of layout performed is controlled by how the application has set the various layout resources. It can be configured to lay out its children in either rows or columns. In addition, the application can specify how the children are laid out, as follows:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd>The children are packed tightly together into either rows or columns</p>
<dt> &bull;</p>
<dd>Each child is placed in an identically sized box (producing a symmetrical look)</p>
<dt> &bull;</p>
<dd>A specific layout (the current <i>x</i> and <i>y</i> positions of the children control their location)</dl>
<p> In addition, the application has control over both the spacing that occurs between each row and column and the margin spacing present between the edges of the RowColumn widget and any children that are placed against it. </p>
<p> The default <code>XmNinsertPosition</code> procedure for the RowColumn returns the value of <code>XmNpositionIndex</code> if one has been specified for the child. Otherwise, this procedure returns the number of children in the RowColumn&#8217;s <code>XmNnumChildren</code> list. In a MenuBar, Pulldown menu pane, or Popup menu pane the default for the <code>XmNshadowThickness</code> resource is 2. In an OptionMenu or a WorkArea, (such as a RadioBox or CheckBox) this resource is not applicable and its use is undefined. If an application wishes to place a 3-D shadow around an OptionMenu or WorkArea, it can create the RowColumn as a child of a Frame widget. </p>
<p> In a MenuBar, Pulldown menu pane, or Popup menu pane the <code>XmNnavigationType</code> resource is not applicable and its use is undefined. In a WorkArea, the default for <code>XmNnavigationType</code> is <code>XmTAB_GROUP</code>. In an OptionMenu the default for <code>XmNnavigationType</code> is <code>XmNONE</code>. </p>
<p> In a MenuBar, Pulldown menu pane, or Popup menu pane the <code>XmNtraversalOn</code> resource is not applicable and its use is undefined. In an OptionMenu or WorkArea, the default for <code>XmNtraversalOn</code> is True. </p>
<p> If the parent of the RowColumn is a MenuShell, the <code>XmNmappedWhenManaged</code> resource is forced to False when the widget is realized. </p>
<p> The user can specify resources in a resource file for the automatically created widgets and gadgets of an OptionMenu. The following list identifies the names of these widgets (or gadgets) and the associated OptionMenu areas.</p>
<dl COMPACT>
<dt>Option Menu Label Gadget</p>
<dd><code>OptionLabel</code></p>
<dt>Option Menu Cascade Button</p>
<dd><code>OptionButton</code></dl>
<p> For the Popup and Pulldown Menupanes, popup and pulldown menus have particular behaviors when the <code>&lt;Btn1&gt;</code> button is pressed outside the menus. These behaviors are summarized here. </p>
<p> When there is already a popped up menu, a user can either press <code>&lt;Btn1&gt;</code> in the same area as the popped up menu, or can press <code>&lt;Btn1&gt;</code> in another area that should have a menu popped up. When <code>&lt;Btn1&gt;</code> is pressed in the same area as the already popped up menu, that menu is unposted. If <code>&lt;Btn1&gt;</code> is pressed in a different area, the associated popup menu is posted for the new area. Note, however, that if the <code>XmNpopupHandlerCallback</code> of either <code>XmManager</code> or <code>XmPrimitive</code> is available, then the callback may override these default behaviors. </p>
<p> For pulldown menus, a user can press <code>&lt;Btn1&gt;</code> on the Cascade button to post the pulldown menu, then click on it again. Upon the second click, the pulldown menu is unposted. </p>
<p> Popup menus are not allowed to have NULL parents.</p>
<h3>Tear-off Menus</h3>
<p>Pulldown and Popup menu panes support tear-off menus, which enable the user to retain a menu pane on the display to facilitate subsequent menu selections. A menu pane that can be torn-off is identified by a tear-off button that spans the width of the menu pane and displays a dashed line. A torn-off menu pane contains a window manager system menu icon and a title bar. The window title displays the label of the cascade button that initiated the action when the label type is <code>XmSTRING</code>. If the label contains a pixmap the window title is empty. A tear-off menu from a Popup menu pane also displays an empty title. Tear-off menus should not be shared. </p>
<p> The user can tear off a menu pane using the mouse or keyboard. Clicking <code>&lt;Btn1&gt;</code> or pressing <code>&lt;osfActivate&gt;</code> (or <code>&lt;osfSelect&gt;</code>) on the tear-off button, tears off the menu pane at the current position. Pressing <code>&lt;Btn2&gt;</code> on the tear-off button tears off the menu pane and allows the user to drag the torn-off menu to a new position designated by releasing the mouse button. Tearing off a menu pane unposts the current active menu. Only one tear-off copy for each menu pane is allowed. Subsequent tear-off actions of a torn menu pane unpost the existing copy first. </p>
<p> The name of the tear-off button of a torn-off menu pane is <code>TearOffControl</code>. The name can be used to set resources in a resource file. An application can also obtain the tear-off button itself using <code>XmGetTearOffControl</code> and then set resource values by calling <code>XtSetValues</code>. </p>
<p> The tear-off button has Separator-like behavior. Its appearance can be specified with the following tear-off button resources: <code>XmNbackground</code>, <code>XmNbackgroundPixmap</code>, <code>XmNbottomShadowColor</code>, <code>XmNforeground</code>, <code>XmNheight</code>, <code>XmNmargin</code>, <code>XmNseparatorType</code>, <code>XmNshadowThickness</code>, and <code>XmNtopShadowColor</code>. Refer to the <code>XmSeparator</code> reference page for a complete description of each of these resources. </p>
<p> The <code>XmNtearOffModel</code>, <code>XmNtearOffMenuActivateCallback</code>, and <code>XmNtearOffMenuDeactivateCallback</code> are RowColumn resources that affect tear-off menu behavior. The <code>XmNtearOffTitle</code> resource enables the application to specify the tear-off menu&#8217;s title if the menu is torn off. </p>
<p> By default, menus do not tear off. Setting the <code>XmNtearOffModel</code> resource to <code>XmTEAR_OFF_ENABLED</code> enables tear-off functionality. There is no resource converter preregistered for <code>XmNtearOffModel</code>. To allow tear-off functionality to be enabled through the resource database, call the function <code>XmRepTypeInstallTearOffModelConverter</code>. </p>
<p> Tear-off menu focus policy follows standard window manager policy. It is recommended that the <code>startupKeyFocus</code> and <code>autoKeyFocus</code> <code>mwm</code> resources be set to True.</p>
<h3>Descendants</h3>
<p>RowColumn automatically creates the descendants shown in the following table. An application can use <code>XtNameToWidget</code> to gain access to the named descendant. In addition, a user or an application can use the named descendant when specifying resource values. </p>
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
<td><code>OptionButton</code></td>
<td><code>XmCascadeButtonGadget</code></td>
<td>option menu button
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>OptionLabel</code></td>
<td><code>XmLabelGadget</code></td>
<td>option menu label
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>TearOffControl</code></td>
<td>subclass of <code>XmPrimitive</code></td>
<td> tear-off button of torn-off menu pane
</td>
</tr>
<tr VALIGN=top>
<td>
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
<p>RowColumn inherits behavior, resources, and traits from <code>Core</code>, <code>Composite</code>, <code>Constraint</code>, and <code>XmManager</code> classes. </p>
<p> The class pointer is <code>xmRowColumnWidgetClass</code>. </p>
<p> The class name is <code>XmRowColumn</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmRowColumn Resource Set</code>
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
<td>XmNadjustLast</td>
<td>XmCAdjustLast</td>
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
<td>XmNadjustMargin</td>
<td>XmCAdjustMargin</td>
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
<td>XmNentryAlignment</td>
<td>XmCAlignment</td>
<td>unsigned char</td>
<td>XmALIGNMENT_BEGINNING</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNentryBorder</td>
<td>XmCEntryBorder</td>
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
<td>XmNentryCallback</td>
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
<td>XmNentryClass</td>
<td>XmCEntryClass</td>
<td>WidgetClass</td>
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
<td>XmNentryVerticalAlignment</td>
<td>XmCVerticalAlignment</td>
<td>unsigned char</td>
<td>XmALIGNMENT_CENTER</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNisAligned</td>
<td>XmCIsAligned</td>
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
<td>XmNisHomogeneous</td>
<td>XmCIsHomogeneous</td>
<td>Boolean</td>
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
<td>XmNlabelString</td>
<td>XmCXmString</td>
<td>XmString</td>
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
<td>XmNmapCallback</td>
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
<td>XmNmenuAccelerator</td>
<td>XmCAccelerators</td>
<td>String</td>
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
<td>XmNmenuHelpWidget</td>
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
<tr VALIGN=top>
<td>XmNmenuHistory</td>
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
<tr VALIGN=top>
<td>XmNmenuPost</td>
<td>XmCMenuPost</td>
<td>String</td>
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
<td>XmNnumColumns</td>
<td>XmCNumColumns</td>
<td>short</td>
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
<td>XmNorientation</td>
<td>XmCOrientation</td>
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
<td>XmNpacking</td>
<td>XmCPacking</td>
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
<td>XmNpopupEnabled</td>
<td>XmCPopupEnabled</td>
<td>int</td>
<td>XmPOPUP_KEYBOARD</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNradioAlwaysOne</td>
<td>XmCRadioAlwaysOne</td>
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
<td>XmNradioBehavior</td>
<td>XmCRadioBehavior</td>
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
<td>XmNresizeHeight</td>
<td>XmCResizeHeight</td>
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
<td>XmNresizeWidth</td>
<td>XmCResizeWidth</td>
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
<td>XmNrowColumnType</td>
<td>XmCRowColumnType</td>
<td>unsigned char</td>
<td>XmWORK_AREA</td>
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
<tr VALIGN=top>
<td>XmNtearOffMenuActivateCallback</td>
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
<td>XmNtearOffMenuDeactivateCallback</td>
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
<td>XmNtearOffModel</td>
<td>XmCTearOffModel</td>
<td>unsigned char</td>
<td>XmTEAR_OFF_DISABLED</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtearOffTitle</td>
<td>XmCTearOffTitle</td>
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
<td>XmNunmapCallback</td>
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
<td>XmNwhichButton</td>
<td>XmCWhichButton</td>
<td>unsigned int</td>
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
<dl COMPACT>
<dt><code>XmNadjustLast</code></p>
<dd>Extends the last row of children to the bottom edge of RowColumn (when <code>XmNorientation</code> is <code>XmHORIZONTAL</code>) or extends the last column to the right edge of RowColumn (when <code>XmNorientation</code> is <code>XmVERTICAL</code>). Setting <code>XmNadjustLast</code> to False disables this feature.</p>
<dt><code>XmNadjustMargin</code></p>
<dd>Specifies whether the inner minor margins of all items contained within the RowColumn widget are forced to the same value. The inner minor margin corresponds to the <code>XmNmarginLeft</code>, <code>XmNmarginRight</code>, <code>XmNmarginTop</code>, and <code>XmNmarginBottom</code> resources supported by <code>XmLabel</code> and <code>XmLabelGadget</code>.</p>
<dd>A horizontal orientation causes <code>XmNmarginTop</code> and <code>XmNmarginBottom</code> for all items in a particular row to be forced to the same value; the value is the largest margin specified for one of the Label items.</p>
<dd>A vertical orientation causes <code>XmNmarginLeft</code> and <code>XmNmarginRight</code> for all items in a particular column to be forced to the same value; the value is the largest margin specified for one of the Label items.</p>
<dd>This keeps all text within each row or column lined up with all other text in its row or column. If <code>XmNrowColumnType</code> is either <code>XmMENU_POPUP</code> or <code>XmMENU_PULLDOWN</code> and this resource is True, only button children have their margins adjusted.</p>
<dt><code>XmNentryAlignment</code></p>
<dd>Specifies the alignment type for children that are subclasses of <code>XmLabel</code> or <code>XmLabelGadget</code> when <code>XmNisAligned</code> is enabled. The following are textual alignment types:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd><code>XmALIGNMENT_BEGINNING</code> (default)</p>
<dt> &bull;</p>
<dd><code>XmALIGNMENT_CENTER</code></p>
<dt> &bull;</p>
<dd><code>XmALIGNMENT_END</code></dl>
</dl>
<dd>See the description of <code>XmNalignment</code> in the <code><a href="/docs/linux/man/3-xmlabel/">XmLabel</a></code>(3) reference page for an explanation of these actions.</p>
<dt><code>XmNentryBorder</code></p>
<dd>Imposes a uniform border width upon all RowColumn&#8217;s children. The default value is 0 (zero), which disables the feature.</p>
<dt><code>XmNentryCallback</code></p>
<dd>Disables the <code>XmNactivateCallback</code> and <code>XmNvalueChangedCallback</code> callbacks for all CascadeButton, DrawnButton, PushButton, and ToggleButton widgets and gadgets contained within the RowColumn widget. If the application supplies this resource, the <code>XmNactivateCallback</code> and <code>XmNvalueChangedCallback</code> callbacks are then revectored to the <code>XmNentryCallback</code> callbacks. This allows an application to supply a single callback routine for handling all items contained in a RowColumn widget. The callback reason is <code>XmCR_ACTIVATE</code>. If the application does not supply this resource, the <code>XmNactivateCallback</code> and <code>XmNvalueChangedCallback</code> callbacks for each item in the RowColumn widget work as normal.</p>
<dd>The application must supply this resource when this widget is created. Changing this resource using the <code>XtSetValues</code> is not supported.</p>
<dt><code>XmNentryClass</code></p>
<dd>Specifies the only widget class that can be added to the RowColumn widget; this resource is meaningful only when the <code>XmNisHomogeneous</code> resource is set to True. Both widget and gadget variants of the specified class may be added to the widget.</p>
<dd>When <code>XmCreateRadioBox</code> is called or when <code>XmNrowColumnType</code> is set to <code>XmWORK_AREA</code> and <code>XmNradioBehavior</code> is True, the default value of <code>XmNentryClass</code> is <code>xmToggleButtonGadgetClass</code>. When <code>XmNrowColumnType</code> is set to <code>XmMENU_BAR</code>, the value of <code>XmNentryClass</code> is forced to <code>xmCascadeButtonWidgetClass</code>.</p>
<dt><code>XmNentryVerticalAlignment</code></p>
<dd>Specifies the type of vertical alignment for children that are subclasses of <code>XmLabel</code>, <code>XmLabelGadget, and</code> <code>XmText</code>. This resource is invalid if <code>XmNorientation</code> is <code>XmVERTICAL</code> and <code>XmNpacking</code> is <code>XmPACK_TIGHT</code>, because this layout preserves variable heights among the children. The vertical alignment types include:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmALIGNMENT_BASELINE_BOTTOM</code></p>
<dd>Causes the bottom baseline of all children in a row to be aligned. This resource is applicable only when all children in a row contain textual data.</p>
<dt><code>XmALIGNMENT_BASELINE_TOP</code></p>
<dd>Causes the top baseline of all children in a row to be aligned. This resource is applicable only when all children in a row contain textual data.</p>
<dt><code>XmALIGNMENT_CONTENTS_BOTTOM</code></p>
<dd>Causes the bottom of the contents (text or pixmap) of all children in a row to be aligned.</p>
<dt><code>XmALIGNMENT_CENTER</code></p>
<dd>Causes the center of all children in a row to be aligned.</p>
<dt><code>XmALIGNMENT_CONTENTS_TOP</code></p>
<dd>Causes the top of the contents (text or pixmap) of all children in a row to be aligned.</dl>
</dl>
<dt><code>XmNisAligned</code></p>
<dd>Specifies text alignment for each item within the RowColumn widget; this applies only to items that are subclasses of <code>XmLabel</code> or <code>XmLabelGadget</code>. However, if the item is a Label widget or gadget and its parent is either a Popup menu pane or a Pulldown menu pane, alignment is not performed; the Label is treated as the title within the menu pane, and the alignment set by the application is not overridden. <code>XmNentryAlignment</code> controls the type of textual alignment.</p>
<dt><code>XmNisHomogeneous</code></p>
<dd>Indicates whether the RowColumn widget should enforce exact homogeneity among the items it contains; if this resource is set to True, only the widgets that are of the class indicated by <code>XmNentryClass</code> are allowed as children of the RowColumn widget. This is most often used when creating a MenuBar. Attempting to insert a child that is not a member of the specified class generates a warning message.</p>
<dd>In a MenuBar, the value of <code>XmNisHomogeneous</code> is forced to True. In an OptionMenu, the value is forced to False. When <code>XmCreateRadioBox</code> is called the default value is True. Otherwise, the default value is False.</p>
<dt><code>XmNlabelString</code></p>
<dd>When <code>XmNrowColumnType</code> is set to <code>XmMENU_OPTION</code>, this resource points to a text string that displays the label with respect to the selection area. The positioning of the label relative to the selection area depends on the layout direction in the horizontal orientation. This resource is not meaningful for all other RowColumn types. If the application wishes to change the label after creation, it must get the LabelGadget ID (<code>XmOptionLabelGadget</code>) and call <code>XtSetValues</code> on the LabelGadget directly. The default value is no label.</p>
<dt><code>XmNmapCallback</code></p>
<dd>Specifies a widget-specific callback function that is invoked when the window associated with the RowColumn widget is about to be mapped. The callback reason is <code>XmCR_MAP</code>.</p>
<dt><code>XmNmarginHeight</code></p>
<dd>Specifies the amount of blank space between the top edge of the RowColumn widget and the first item in each column, and the bottom edge of the RowColumn widget and the last item in each column. The default value is 0 (zero) for Pulldown and Popup menu panes, and 3 pixels for other RowColumn types.</p>
<dt><code>XmNmarginWidth</code></p>
<dd>Specifies the amount of blank space between the left edge of the RowColumn widget and the first item in each row, and the right edge of the RowColumn widget and the last item in each row. The default value is 0 (zero) for Pulldown and Popup menu panes, and 3 pixels for other RowColumn types.</p>
<dt><code>XmNmenuAccelerator</code></p>
<dd>This resource is useful only when the RowColumn widget has been configured to operate as a Popup menu pane or a MenuBar. The format of this resource is similar to the left side specification of a translation string, with the limitation that it must specify a key event. For a Popup menu pane, when the accelerator is typed by the user, the Popup menu pane is posted. For a MenuBar, when the accelerator is typed by the user, the first item in the MenuBar is highlighted, and traversal is enabled in the MenuBar. The default for a Popup menu pane is <code>&lt;osfMenu&gt;</code>. The default for a MenuBar is <code>&lt;osfMenuBar&gt;</code>. Setting the <code>XmNpopupEnabled</code> resource to False disables the accelerator.</p>
<dt><code>XmNmenuHelpWidget</code></p>
<dd>Specifies the widget ID for the CascadeButton, which is treated as the Help widget if <code>XmNrowColumnType</code> is set to <code>XmMENU_BAR</code>. Which corner of the MenuBar the Help widget is placed at depends on the <code>XmNlayoutDirection</code> resource of the widget. If the RowColumn widget is any type other than <code>XmMENU_BAR</code>, this resource is not meaningful.</p>
<dt><code>XmNmenuHistory</code></p>
<dd>Specifies the widget ID of the last menu entry to be activated. It is also useful for specifying the current selection for an OptionMenu. If <code>XmNrowColumnType</code> is set to <code>XmMENU_OPTION</code>, the specified menu item is positioned under the cursor when the menu is displayed.</p>
<dd>If the RowColumn widget has the <code>XmNradioBehavior</code> resource set to True, the widget field associated with this resource contains the widget ID of the last ToggleButton or ToggleButtonGadget to change from unselected to selected. The default value is the widget ID of the first child in the widget.</p>
<dt><code>XmNmenuPost</code></p>
<dd>Specifies an X event description indicating a button event that posts a menu system. The default for <code>XmMENU_POPUP</code> is <code>BMenu Press</code>. The default for <code>XmMENU_OPTION</code>, <code>XmMENU_BAR</code>, and <code>XmWORK_AREA</code> is <code>&lt;Btn1&gt;</code> <code>Press</code>. The <code>XmNmenuPost</code> resource for pulldowns should be consistent with that of the top-level parent menu (although the event type is ignored). Setting this resource to <code>BTransfer Press</code> will conflict with drag and drop operations, which use <code>BTransfer Press</code> as a default button binding. Therefore, this resource cannot be <code>BTransfer Press</code>.</p>
<dt><code>XmNmnemonic</code></p>
<dd>This resource is useful only when <code>XmNrowColumnType</code> is set to <code>XmMENU_OPTION</code>. It specifies a keysym for a key that, when pressed by the user along with the <code>MAlt</code> modifier, posts the associated Pulldown menu pane. The first character in the OptionMenu label string that exactly matches the mnemonic in the character set specified in <code>XmNmnemonicCharSet</code> is underlined. The user can post the menu by pressing either the shifted or the unshifted mnemonic key. The default is no mnemonic.</p>
<dt><code>XmNmnemonicCharSet</code></p>
<dd>Specifies the character set of the mnemonic for an OptionMenu. The default is <code>XmFONTLIST_DEFAULT_TAG</code>. If the RowColumn widget is any type other than <code>XmMENU_OPTION</code>, this resource is not meaningful.</p>
<dt><code>XmNnumColumns</code></p>
<dd>Specifies the number of minor dimension extensions that are made to accommodate the entries; this attribute is meaningful only when <code>XmNpacking</code> is set to <code>XmPACK_COLUMN</code>.</p>
<dd>For vertically oriented RowColumn widgets, this attribute indicates how many columns are built; the number of entries per column is adjusted to maintain this number of columns, if possible.</p>
<dd>For horizontally oriented RowColumn widgets, this attribute indicates how many rows are built.</p>
<dd>The default value is 1. In an OptionMenu the value is forced to 1. The value must be greater than 0 (zero).</p>
<dt><code>XmNorientation</code></p>
<dd>Determines whether RowColumn layouts are row-major or column-major. In a column-major layout, the children of the RowColumn are laid out in columns within the widget. In a row-major layout the children of the RowColumn are laid out in rows. The direction of the horizontal layout in the row-major layout (from left or right), and the wrapping in the column-major layout (vertical), depend on the <code>XmNlayoutDirection</code> resource of the widget. The <code>XmVERTICAL</code> resource value selects a column-major layout. <code>XmHORIZONTAL</code> selects a row-major layout.</p>
<dd>When creating a MenuBar or an OptionMenu, the default is <code>XmHORIZONTAL</code>. Otherwise, the default value is <code>XmVERTICAL</code>. The results of specifying a value of <code>XmVERTICAL</code> for a MenuBar are undefined.</p>
<dt><code>XmNpacking</code></p>
<dd>Specifies how to pack the items contained within a RowColumn widget. This can be set to <code>XmPACK_TIGHT, XmPACK_COLUMN</code> or <code>XmPACK_NONE</code>. When a RowColumn widget packs the items it contains, it determines its major dimension using the value of the <code>XmNorientation</code> resource.</p>
<dd><code>XmPACK_TIGHT</code> indicates that given the current major dimension (for example, vertical if <code>XmNorientation</code> is <code>XmVERTICAL</code>), entries are placed one after the other until the RowColumn widget must wrap. RowColumn wraps when there is no room left for a complete child in that dimension. Wrapping occurs by beginning a new row or column in the next available space. Wrapping continues, as often as necessary, until all of the children are laid out. In the vertical dimension (columns), boxes are set to the same width; in the horizontal dimension (rows), boxes are set to the same depth. Each entry&#8217;s position in the major dimension is left unaltered (for example, <code>XmNy</code> is left unchanged when <code>XmNorientation</code> is <code>XmVERTICAL</code>); its position in the minor dimension is set to the same value as the greatest entry in that particular row or column. The position in the minor dimension of any particular row or column is independent of all other rows or columns.</p>
<dd><code>XmPACK_COLUMN</code> indicates that all entries are placed in identically sized boxes. The boxes are based on the largest height and width values of all the children widgets. The value of the <code>XmNnumColumns</code> resource determines how many boxes are placed in the major dimension, before extending in the minor dimension.</p>
<dd><code>XmPACK_NONE</code> indicates that no packing is performed. The <i>x</i> and <i>y</i> attributes of each entry are left alone, and the RowColumn widget attempts to become large enough to enclose all entries.</p>
<dd>When <code>XmCreateRadioBox</code> is called or when <code>XmNrowColumnType</code> is set to <code>XmWORK_AREA</code> and <code>XmNradioBehavior</code> is True, the default value of <code>XmNpacking</code> is <code>XmPACK_COLUMN</code>. In an OptionMenu the value is initialized to <code>XmPACK_TIGHT</code>. Otherwise, the value defaults to <code>XmPACK_TIGHT</code>.</p>
<dt><code>XmNpopupEnabled</code></p>
<dd>Allows the menu system to enable keyboard input (accelerators and mnemonics) defined for the Popup menu pane and any of its submenus. The Popup menu pane needs to be informed whenever its accessibility to the user changes because posting of the Popup menu pane is controlled by the application. This resource can take four values, including:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmPOPUP_KEYBOARD</code></p>
<dd>Specifies that the keyboard input&#8212;accelerators and mnemonics&#8212;defined for the Popup menu pane and any of its submenus is enabled. This is the default.</p>
<dt><code>XmPOPUP_DISABLED</code></p>
<dd>Specifies that the keyboard input is disabled.</p>
<dt><code>XmPOPUP_AUTOMATIC</code></p>
<dd>Specifies that the keyboard is enabled for automatic popup menus.</p>
<dt><code>XmPOPUP_AUTOMATIC_RECURSIVE</code></p>
<dd>Specifies that the keyboard is enabled for recursive automatic popup menus.</dl>
</dl>
<dt><code>XmNradioAlwaysOne</code></p>
<dd>If True, forces the active ToggleButton or ToggleButtonGadget to be automatically selected after having been unselected (if no other toggle was activated). If False, the active toggle may be unselected. The default value is True. This resource is important only when <code>XmNradioBehavior</code> is True.</p>
<dd>The application can always add and subtract toggles from RowColumn regardless of the selected/unselected state of the toggle. The application can also manage and unmanage toggle children of RowColumn at any time regardless of state. Therefore, the application can sometimes create a RowColumn that has <code>XmNradioAlwaysOne</code> set to True and none of the toggle children selected. The result is undefined if the value of this resource is True and the application sets more than one ToggleButton at a time.</p>
<dt><code>XmNradioBehavior</code></p>
<dd>Specifies a Boolean value that when True, indicates that the RowColumn widget should enforce a RadioBox-type behavior on all of its children that are ToggleButtons or ToggleButtonGadgets.</p>
<dd>When the value of this resource is True, <code>XmNindicatorType</code> defaults to <code>XmONE_OF_MANY</code> for ToggleButton and ToggleButtonGadget children.</p>
<dd>RadioBox behavior dictates that when one toggle is selected and the user selects another toggle, the first toggle is unselected automatically. The RowColumn usually does not enforce this behavior if the application, rather than the user, changes the state of a toggle. The RowColumn does enforce this behavior if a toggle child is selected with <code>XmToggleButtonSetState</code> or <code>XmToggleButtonGadgetSetState</code> with a <i>notify</i> argument of True.</p>
<dd>When <code>XmCreateRadioBox</code> is called, the default value of <code>XmNradioBehavior</code> is True. Otherwise, the default value is False.</p>
<dt><code>XmNresizeHeight</code></p>
<dd>Requests a new height if necessary, when set to True. When this resource is set to False, the widget does not request a new height regardless of any changes to the widget or its children.</p>
<dt><code>XmNresizeWidth</code></p>
<dd>Requests a new width if necessary, when set to True. When set to False, the widget does not request a new width regardless of any changes to the widget or its children.</p>
<dt><code>XmNrowColumnType</code></p>
<dd>Specifies the type of RowColumn widget to be created. It is a nonstandard resource that cannot be changed after it is set. If an application uses any of the convenience routines, except <code>XmCreateRowColumn</code>, this resource is automatically forced to the appropriate value by the convenience routine. If an application uses the Xt Intrinsics API to create its RowColumn widgets, it must specify this resource itself. The set of possible settings for this resource are</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd><code>XmWORK_AREA</code> (default)</p>
<dt> &bull;</p>
<dd><code>XmMENU_BAR</code></p>
<dt> &bull;</p>
<dd><code>XmMENU_PULLDOWN</code></p>
<dt> &bull;</p>
<dd><code>XmMENU_POPUP</code></p>
<dt> &bull;</p>
<dd><code>XmMENU_OPTION</code></dl>
</dl>
<dd>This resource cannot be changed after the RowColumn widget is created. Any changes attempted through <code>XtSetValues</code> are ignored.</p>
<dd>The value of this resource is used to determine the value of a number of other resources. The descriptions of RowColumn resources explain this when it is the case. The resource <code>XmNnavigationType</code>, inherited from <code>XmManager</code>, is changed to <code>XmNONE</code> if <code>XmNrowColumnType</code> is <code>XmMENU_OPTION</code>.</p>
<dt><code>XmNspacing</code></p>
<dd>Specifies the horizontal and vertical spacing between items contained within the RowColumn widget. The default value is 3 pixels for <code>XmOPTION_MENU</code> and <code>XmWORK_AREA</code> and 0 (zero) for other RowColumn types.</p>
<dt><code>XmNsubMenuId</code></p>
<dd>Specifies the widget ID for the Pulldown menu pane to be associated with an OptionMenu. This resource is useful only when <code>XmNrowColumnType</code> is set to <code>XmMENU_OPTION</code>. The default value is NULL.</p>
<dt><code>XmNtearOffMenuActivateCallback</code></p>
<dd>Specifies the callback list that notifies the application when the tear-off menu pane is about to be activated. It precedes the tear-off&#8217;s map callback.</p>
<dd>Use this resource when your application has shared menu panes and when the torn-off menu can have two or more parents that can have opposing sensitivity states for the same menu item. This resource enables the application to track whether a menu item is sensitive or insensitive and to set the state to the original parent&#8217;s menu item state when the torn-off menu is reposted. The application can use <code>XmGetPostedFromWidget</code> to determine from which parent the menu was torn. The callback reason is <code>XmCR_TEAR_OFF_ACTIVATE</code>. The default is NULL.</p>
<dt><code>XmNtearOffMenuDeactivateCallback</code></p>
<dd>Specifies the callback list that notifies the application when the tear-off menu pane is about to be deactivated. It follows the tear-off&#8217;s unmap callback.</p>
<dd>Use this resource when your application has shared menu panes and when the torn-off menu can have two or more parents that can have opposing sensitivity states for the same menu item. This resource enables the application to track whether a menu item is sensitive or insensitive and to set the state to the original parent&#8217;s menu item state when the torn-off menu is reposted. The application can use <code>XmGetPostedFromWidget</code> to determine from which parent the menu was torn. The callback reason is <code>XmCR_TEAR_OFF_DEACTIVATE</code>. The default is NULL.</p>
<dt><code>XmNtearOffModel</code></p>
<dd>Indicates whether tear-off functionality is enabled or disabled when <code>XmNrowColumnType</code> is set to <code>XmMENU_PULLDOWN</code> or <code>XmMENU_POPUP</code>. The values are <code>XmTEAR_OFF_ENABLED</code> or <code>XmTEAR_OFF_DISABLED</code> (default value). This resource is invalid for type <code>XmMENU_OPTION</code>; however, it does affect any pulldown submenus within an OptionMenu. The function <code>XmRepTypeInstallTearOffModelConverter</code> installs a resource converter for this resource.</p>
<dt><code>XmNtearoffTitle</code></p>
<dd>Used by the TearOff shell to set the title for the window manager to display.</p>
<dt><code>XmNunmapCallback</code></p>
<dd>Specifies a list of callbacks that is called after the window associated with the RowColumn widget has been unmapped. The callback reason is <code>XmCR_UNMAP</code>. The default value is NULL.</p>
<dt><code>XmNwhichButton</code></p>
<dd>This resource is obsolete; it has been replaced by <code>XmNmenuPost</code> and is present for compatibility with older releases of Motif. This resource cannot be 2.</dl>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmRowColumn Constraint Resource Set</code>
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
</table>
</table>
<dl COMPACT>
<dt><code>XmNpositionIndex</code></p>
<dd>Specifies the position of the widget in its parent&#8217;s list of children (the value of the <code>XmNchildren</code> resource). The value is an integer that is no less than 0 (zero) and no greater than the number of children in the list at the time the value is specified. A value of 0 (zero) means that the child is placed at the beginning of the list. The value can also be specified as <code>XmLAST_POSITION</code> (the default), which means that the child is placed at the end of the list. Any other value is ignored. <code>XtGetValues</code> returns the position of the widget in its parent&#8217;s child list at the time of the call to <code>XtGetValues</code>.</p>
<dd>When a widget is inserted into its parent&#8217;s child list, the positions of any existing children that are greater than or equal to the specified widget&#8217;s <code>XmNpositionIndex</code> are increased by 1. The effect of a call to <code>XtSetValues</code> for <code>XmNpositionIndex</code> is to remove the specified widget from its parent&#8217;s child list, decrease by 1 the positions of any existing children that are greater than the specified widget&#8217;s former position in the list, and then insert the specified widget into its parent&#8217;s child list as described in the preceding sentence.</dl>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>Simple Menu Creation Resource Set</code>
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
<td>XmNbuttonAccelerators</td>
<td>XmCButtonAccelerators</td>
<td>StringTable</td>
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
<td>XmNbuttonAcceleratorText</td>
<td>XmCButtonAcceleratorText</td>
<td>XmStringTable</td>
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
<td>XmNbuttonCount</td>
<td>XmCButtonCount</td>
<td>int</td>
<td>0</td>
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
<td>XmNbuttonMnemonicCharSets</td>
<td>XmCButtonMnemonicCharSets</td>
<td>XmStringCharSetTable</td>
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
<td>XmNbuttonMnemonics</td>
<td>XmCButtonMnemonics</td>
<td>XmKeySymTable</td>
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
<td>XmNbuttons</td>
<td>XmCButtons</td>
<td>XmStringTable</td>
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
<td>XmNbuttonSet</td>
<td>XmCButtonSet</td>
<td>int</td>
<td>-1</td>
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
<td>XmNbuttonType</td>
<td>XmCButtonType</td>
<td>XmButtonTypeTable</td>
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
<td>XmNoptionLabel</td>
<td>XmCOptionLabel</td>
<td>XmString</td>
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
<td>XmNoptionMnemonic</td>
<td>XmCOptionMnemonic</td>
<td>KeySym</td>
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
<td>XmNpostFromButton</td>
<td>XmCPostFromButton</td>
<td>int</td>
<td>-1</td>
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
<td>XmNsimpleCallback</td>
<td>XmCCallback</td>
<td>XtCallbackProc</td>
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
<dl COMPACT>
<dt><code>XmNbuttonAccelerators</code></p>
<dd>This resource is for use with the simple menu creation routines. It specifies a list of accelerators for the buttons created. The list contains one element for each button, separator, and title created.</p>
<dt><code>XmNbuttonAcceleratorText</code></p>
<dd>This resource is for use with the simple menu creation routines. It specifies a list of compound strings to display for the accelerators for the buttons created. The list contains one element for each button, separator, and title created.</p>
<dt><code>XmNbuttonCount</code></p>
<dd>This resource is for use with the simple menu creation routines. It specifies the total number of menu buttons, separators, and titles to create. The value must not be negative.</p>
<dt><code>XmNbuttonMnemonicCharSets</code></p>
<dd>This resource is for use with the simple menu creation routines. It specifies a list of character sets with which button mnemonics are to be displayed. The list contains one element for each button, separator, and title created. The default is determined dynamically depending on the locale of the widget.</p>
<dt><code>XmNbuttonMnemonics</code></p>
<dd>This resource is for use with the simple menu creation routines. It specifies a list of mnemonics for the buttons created. The list contains one element for each button, separator, and title created.</p>
<dt><code>XmNbuttons</code></p>
<dd>This resource is for use with the simple menu creation routines. It specifies a list of compound strings to use as labels for the buttons created. The list contains one element for each button, separator, and title created.</p>
<dt><code>XmNbuttonSet</code></p>
<dd>This resource is for use with the simple menu creation routines. It specifies which button of a RadioBox or OptionMenu Pulldown submenu is initially set. The value is an integer <i>n</i> indicating the <i>n</i>th ToggleButtonGadget specified for a RadioBox or the <i>n</i>th PushButtonGadget specified for an OptionMenu Pulldown submenu. The first button specified is number 0. The value must not be negative.</p>
<dt><code>XmNbuttonType</code></p>
<dd>This resource is for use with the simple menu creation routines. It specifies a list of button types associated with the buttons to be created. The list contains one element for each button, separator, and title created. If this resource is not specified, each button in a MenuBar is a CascadeButtonGadget, each button in a RadioBox or CheckBox is a ToggleButtonGadget, and each button in any other type of RowColumn widget is a PushButtonGadget. Each button type is of type <code>XmButtonType</code>, an enumeration with the following possible values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmCASCADEBUTTON</code></p>
<dd>Specifies a CascadeButtonGadget for a MenuBar, Popup menu pane, or Pulldown menu pane.</p>
<dt><code>XmCHECKBUTTON</code></p>
<dd>Specifies a ToggleButtonGadget for a CheckBox, Popup menu pane, or Pulldown menu pane.</p>
<dt><code>XmDOUBLE_SEPARATOR</code></p>
<dd>Specifies a SeparatorGadget for a Popup menu pane, Pulldown menu pane, or OptionMenu Pulldown submenu. The separator type is <code>XmDOUBLE_LINE</code>.</p>
<dt><code>XmPUSHBUTTON</code></p>
<dd>Specifies a PushButtonGadget for a Popup menu pane, Pulldown menu pane, or OptionMenu Pulldown submenu.</p>
<dt><code>XmRADIOBUTTON</code></p>
<dd>Specifies a ToggleButtonGadget for a RadioBox, Popup menu pane, or Pulldown menu pane.</p>
<dt><code>XmSEPARATOR</code></p>
<dd>Specifies a SeparatorGadget for a Popup menu pane, Pulldown menu pane, or OptionMenu Pulldown submenu.</p>
<dt><code>XmTITLE</code></p>
<dd>Specifies a LabelGadget used as a title for a Popup menu pane or Pulldown menu pane.</dl>
</dl>
<dt><code>XmNoptionLabel</code></p>
<dd>This resource is for use with the simple menu creation routines. It specifies a compound string for the label string to be used on the left side of an OptionMenu.</p>
<dt><code>XmNoptionMnemonic</code></p>
<dd>This resource is for use with the simple menu creation routines. It specifies a keysym for a key that, when pressed by the user along with the <code>MAlt</code> modifier, posts the associated Pulldown menu pane for an OptionMenu.</p>
<dt><code>XmNpostFromButton</code></p>
<dd>This resource is for use with the simple menu creation routines. For a Pulldown menu pane, it specifies the button in the parent to which the submenu is attached. The menu is then posted from this button. The value is an integer <i>n</i> indicating the <i>n</i>th CascadeButton or CascadeButtonGadget specified for the parent of the Pulldown menu pane. The first button specified is number 0. The value must not be negative.</p>
<dt><code>XmNsimpleCallback</code></p>
<dd>This resource is for use with the simple menu creation routines. It specifies a callback procedure to be called when a button is activated or when its value changes. This callback function is added to each button after creation. For a CascadeButtonGadget or a PushButtonGadget, the callback is added as the button&#8217;s <code>XmNactivateCallback</code>, and it is called when the button is activated. For a ToggleButtonGadget, the callback is added as the button&#8217;s <code>XmNvalueChangedCallback</code>, and it is called when the button&#8217;s value changes. The button number is passed in the <i>client_data</i> field.</dl>
<h3>Inherited Resources</h3>
<p>RowColumn inherits behavior and resources from the superclasses described in the following tables. For a complete description of each resource, refer to the reference page for that superclass. </p>
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
 Widget <i>widget</i>;
 char <i>* data</i>;
 char <i>* callbackstruct</i>;
} XmRowColumnCallbackStruct;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the callback</dl>
<p> The following fields apply only when the callback reason is <code>XmCR_ACTIVATE</code>; for all other callback reasons, these fields are set to NULL. The <code>XmCR_ACTIVATE</code> callback reason is generated only when the application has supplied an entry callback, which overrides any activation callbacks registered with the individual RowColumn items.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Is set to the widget ID of the RowColumn item that has been activated</p>
<dt><i>data</i></p>
<dd>Contains the client-data value supplied by the application when the RowColumn item&#8217;s activation callback was registered</p>
<dt><i>callbackstruct</i></p>
<dd>Points to the callback structure generated by the RowColumn item&#8217;s activation callback</dl>
<h3>Translations</h3>
<p><code>XmRowColumn</code> translations depend on the value of the <code>XmNrowColumnType</code> resource. </p>
<p> If <code>XmNrowColumnType</code> is set to <code>XmWORK_AREA</code>, <code>XmRowColumn</code> inherits translations from <code>XmManager</code>. </p>
<p> If <code>XmNrowColumnType</code> is set to <code>XmMENU_OPTION</code>, <code>XmRowColumn</code> inherits traversal, <code>&lt;osfActivate&gt;</code>, and <code>&lt;osfCancel&gt;</code> translations from <code>XmManager</code> and has the following additional translations. </p>
<p> The following key names are listed in the X standard key event translation table syntax. This format is the one used by Motif to specify the widget actions corresponding to a given key. A brief overview of the format is provided under <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3). For a complete description of the format, please refer to the X Toolkit Instrinsics Documentation.</p>
<dl COMPACT>
<dt><code>&lt;Btn2Down&gt;</code>:</p>
<dd>MenuGadgetDrag()</p>
<dt><code>c&lt;Btn1Down&gt;</code>:</p>
<dd>MenuGadgetTraverseCurrent()</p>
<dt><code>c&lt;Btn1Up&gt;</code>:</p>
<dd>MenuGadgetTraverseCurrentUp()</p>
<dt><code>&asymp;c</code><code>&lt;BtnDown&gt;</code>:</p>
<dd>MenuBtnDown()</p>
<dt><code>&asymp;c</code><code>&lt;BtnUp&gt;</code>:</p>
<dd>MenuBtnUp()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfHelp&gt;</code>:</p>
<dd>MenuHelp()</dl>
<p> The translations for <code>XmRowColumn</code> if <code>XmNrowColumnType</code> is set to <code>XmMENU_BAR</code> <code>XmMENU_PULLDOWN</code>, or <code>XmMENU_POPUP</code> are described in the following list. In a Popup menu system, <code>&lt;Btn3&gt;</code> also performs the <code>&lt;Btn1&gt;</code> actions.</p>
<dl COMPACT>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfHelp&gt;</code>:</p>
<dd>MenuHelp()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfLeft&gt;</code>:</p>
<dd>MenuGadgetTraverseLeft()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfRight&gt;</code>:</p>
<dd>MenuGadgetTraverseRight()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfUp&gt;</code>:</p>
<dd>MenuGadgetTraverseUp()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfDown&gt;</code>:</p>
<dd>MenuGadgetTraverseDown()</dl>
<h3>Action Routines</h3>
<p>The <code>XmRowColumn</code> action routines are</p>
<dl COMPACT>
<dt>Help():</p>
<dd>Calls the callbacks for <code>XmNhelpCallback</code> if any exist. If there are no help callbacks for this widget, this action calls the help callbacks for the nearest ancestor that has them.</p>
<dt>ManagerGadgetSelect():</p>
<dd>When a gadget child of the menu has the focus, invokes the gadget child&#8217;s behavior associated with <code>&lt;osfSelect&gt;</code>. This generally has the effect of unposting the menu hierarchy and arming and activating the gadget, except that, for a CascadeButtonGadget with a submenu, it posts the submenu.</p>
<dt>MenuBtnDown():</p>
<dd>When a gadget child of the menu has focus, invokes the gadget child&#8217;s behavior associated with <code>&lt;Btn1Down&gt;</code>. This generally has the effect of unposting any menus posted by the parent menu, enabling mouse traversal in the menu, and arming the gadget. For a CascadeButtonGadget with a submenu, it also posts the associated submenu.</p>
<dt>MenuBtnUp():</p>
<dd>When a gadget child of the menu has focus, invokes the gadget child&#8217;s behavior associated with <code>&lt;Btn1Up&gt;</code>. This generally has the effect of unposting the menu hierarchy and activating the gadget, except that for a CascadeButtonGadget with a submenu, it posts the submenu and enables keyboard traversal in the menu.</p>
<dt>MenuGadgetEscape():</p>
<dd>In a top-level Pulldown MenuPane from a MenuBar, unposts the menu, disarms the MenuBar CascadeButton and the MenuBar, and, when the shell&#8217;s keyboard focus policy is <code>XmEXPLICIT</code>, restores keyboard focus to the widget that had the focus before the MenuBar was entered. In other Pulldown MenuPanes, unposts the menu.</p>
<dd>In a Popup MenuPane, unposts the menu and, when the shell&#8217;s keyboard focus policy is <code>XmEXPLICIT</code>, restores keyboard focus to the widget from which the menu was posted. In a TearOff MenuPane that has no submenus posted, dismisses the menu; otherwise, if one or more submenus are posted, unposts the last menu pane.</p>
<dt>MenuGadgetTraverseDown():</p>
<dd>If the current menu item has a submenu and is in a MenuBar, then this action posts the submenu, disarms the current menu item, and arms the submenu&#8217;s first traversable menu item.</p>
<dd>If the current menu item is in a MenuPane, then this action disarms the current menu item and arms the item below it. This action wraps within the MenuPane. The direction of the wrapping depends on the <code>XmNlayoutDirection</code> resource.</p>
<dt>MenuGadgetTraverseLeft():</p>
<dd>When the current menu item is in a MenuBar, this action disarms the current item and arms the MenuBar item to the left. This action wraps within the MenuBar.</p>
<dd>In MenuPanes, if the current menu item is not at the left edge of a MenuPane, this action disarms the current item and arms the item to its left. If the current menu item is at the left edge of a submenu attached to a MenuBar item, then this action unposts the submenu and traverses to the MenuBar item to the left, wrapping if necessary. If that MenuBar item has a submenu, it posts the submenu and arms the first traversable item in the submenu. If the current menu item is at the left edge of a submenu not directly attached to a MenuBar item, then this action unposts the current submenu only.</p>
<dd>In Popup or Torn-off MenuPanes, when the current menu item is at the left edge, this action wraps within the MenuPane. If the current menu item is at the left edge of the MenuPane and not in the top row, this action wraps to the rightmost menu item in the row above. If the current menu item is in the upper, leftmost corner, this action wraps to the tear-off control, if present, or else it wraps to the bottom, rightmost menu item in the MenuPane.</p>
<dd>The preceding description applies when the <code>XmNlayoutDirection</code> horizontal direction is <code>XmLEFT_TO_RIGHT</code>. If the <code>XmNlayoutDirection</code> horizontal direction is <code>XmRIGHT_TO_LEFT</code>, then the following applies.</p>
<dd>If the current menu item is in a MenuBar, then this action disarms the current item and arms the MenuBar item to the left. This action wraps within the MenuBar.</p>
<dd>In MenuPanes, if the current menu item is a CascadeButton, then this action posts its associated submenu. If the current menu item is not a CascadeButton and is not at the left edge of a MenuPane, this action disarms the current item and arms the item to its left, wrapping if necessary. If the current menu item is not a CascadeButton and is at the left edge of a submenu that is a descendent of a MenuBar, then this action unposts all submenus and traverses to the MenuBar item to the left. If that MenuBar item has a submenu, it posts the submenu and arms the submenu&#8217;s first traversable item.</p>
<dd>In Popup or Torn-off menus, if the current menu item is not a CascadeButton and is at the left edge of a row (except the bottom row), this action wraps to the rightmost menu item in the row below. If the current menu item is not a CascadeButton and is in the bottom, leftmost corner of a Popup or Pulldown MenuPane, this action wraps to the tear-off control, if present, or else it wraps to the top, rightmost menu item of the MenuPane.</p>
<dt>MenuGadgetTraverseRight():</p>
<dd>If the current menu item is in a MenuBar, then this action disarms the current item and arms the MenuBar item to the right. This action wraps within the MenuBar.</p>
<dd>In MenuPanes, if the current menu item is a CascadeButton, then this action posts its associated submenu. If the current menu item is not a CascadeButton and is not at the right edge of a MenuPane, this action disarms the current item and arms the item to its right, wrapping if necessary. If the current menu item is not a CascadeButton and is at the right edge of a submenu that is a descendent of a MenuBar, then this action unposts all submenus and traverses to the MenuBar item to the right. If that MenuBar item has a submenu, it posts the submenu and arms the submenu&#8217;s first traversable item.</p>
<dd>In Popup or Torn-off menus, if the current menu item is not a CascadeButton and is at the right edge of a row (except the bottom row), this action wraps to the leftmost menu item in the row below. If the current menu item is not a CascadeButton and is in the bottom, rightmost corner of a Popup or Pulldown MenuPane, this action wraps to the tear-off control, if present, or else it wraps to the top, leftmost menu item of the MenuPane.</p>
<dd>The preceding description applies when the <code>XmNlayoutDirection</code> horizontal direction is <code>XmLEFT_TO_RIGHT</code>. If the <code>XmNlayoutDirection</code> horizontal direction is <code>XmRIGHT_TO_LEFT</code>, then the following applies. When the current menu item is in a MenuBar, this action disarms the current item and arms the MenuBar item to the left. This action wraps within the MenuBar.</p>
<dd>In MenuPanes, if the current menu item is not at the right edge of a MenuPane, this action disarms the current item and arms the item to its right. If the current menu item is at the right edge of a submenu attached to a MenuBar item, then this action unposts the submenu and traverses to the MenuBar item to the right, wrapping if necessary. If that MenuBar item has a submenu, it posts the submenu and arms the first traversable item in the submenu. If the current menu item is at the right edge of a submenu not directly attached to a MenuBar item, then this action unposts the current submenu only.</p>
<dd>In Popup or Torn-off MenuPanes, when the current menu item is at the right edge, this action wraps within the MenuPane. If the current menu item is at the right edge of the MenuPane and not in the top row, this action wraps to the leftmost menu item in the row above. If the current menu item is in the upper, rightmost corner, this action wraps to the tear-off control, if present, or else it wraps to the bottom, leftmost menu item in the MenuPane.</p>
<dt>MenuGadgetTraverseUp():</p>
<dd>When the current menu item is in a MenuPane, then this action disarms the current menu item and arms the item above it. This action wraps within the MenuPane. The direction of the wrapping depends on the <code>XmNlayoutDirection</code> resource.</dl>
<h3>Related Behavior</h3>
<p>The following menu functions are available:</p>
<dl COMPACT>
<dt><code>&lt;osfMenuBar&gt;</code>:</p>
<dd>In any non-popup descendant of a MenuBar&#8217;s parent, excluding the MenuBar itself, this action enables keyboard traversal and moves keyboard focus to the first item in the MenuBar. In the MenuBar or any menu cascaded from it, this action unposts the menu hierarchy and, when the shell&#8217;s keyboard focus policy is <code>XmEXPLICIT</code>, restores focus to the widget that had the focus when the menu system was entered.</p>
<dt><code>&lt;osfMenu&gt;</code>:</p>
<dd>Pops up the menu associated with the control that has the keyboard focus. Enables keyboard traversal in the menu. In the Popup menu system or any menu cascaded from it, this action unposts the menu hierarchy and, when the shell&#8217;s keyboard focus policy is <code>XmEXPLICIT</code>, restores focus to the widget that had the focus when the menu system was entered.</dl>
<h3>Virtual Bindings</h3>
<p>The bindings for virtual keys are vendor specific. For information about bindings for virtual buttons and keys, see <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-composite/">Composite</a></code>(3), <code><a href="/docs/linux/man/3-constraint/">Constraint</a></code>(3), <code><a href="/docs/linux/man/3-core/">Core</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatemenubar/">XmCreateMenuBar</a></code>(3), <code><a href="/docs/linux/man/3-xmcreateoptionmenu/">XmCreateOptionMenu</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatepopupmenu/">XmCreatePopupMenu</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatepulldownmenu/">XmCreatePulldownMenu</a></code>(3), <code><a href="/docs/linux/man/3-xmcreateradiobox/">XmCreateRadioBox</a></code>(3), <code><a href="/docs/linux/man/3-xmcreaterowcolumn/">XmCreateRowColumn</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatesimplecheckbox/">XmCreateSimpleCheckBox</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatesimplemenubar/">XmCreateSimpleMenuBar</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatesimpleoptionmenu/">XmCreateSimpleOptionMenu</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatesimplepopupmenu/">XmCreateSimplePopupMenu</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatesimplepulldownmenu/">XmCreateSimplePulldownMenu</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatesimpleradiobox/">XmCreateSimpleRadioBox</a></code>(3), <code><a href="/docs/linux/man/3-xmcreateworkarea/">XmCreateWorkArea</a></code>(3), <code><a href="/docs/linux/man/3-xmgetmenucursor/">XmGetMenuCursor</a></code>(3), <code><a href="/docs/linux/man/3-xmgetpostedfromwidget/">XmGetPostedFromWidget</a></code>(3), <code>XmGetTearOffControl</code>, <code><a href="/docs/linux/man/3-xmlabel/">XmLabel</a></code>(3), <code><a href="/docs/linux/man/3-xmmanager/">XmManager</a></code>(3), <code><a href="/docs/linux/man/3-xmmenuposition/">XmMenuPosition</a></code>(3), <code><a href="/docs/linux/man/3-xmoptionbuttongadget/">XmOptionButtonGadget</a></code>(3), <code><a href="/docs/linux/man/3-xmoptionlabelgadget/">XmOptionLabelGadget</a></code>(3), <code>XmRepTypeInstallTearOffModelConverter</code>, <code><a href="/docs/linux/man/3-xmsetmenucursor/">XmSetMenuCursor</a></code>(3), <code><a href="/docs/linux/man/3-xmupdatedisplay/">XmUpdateDisplay</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatemanagedrowcolumn/">XmVaCreateManagedRowColumn</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreaterowcolumn/">XmVaCreateRowColumn</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatesimplecheckbox/">XmVaCreateSimpleCheckBox</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatesimplemenubar/">XmVaCreateSimpleMenuBar</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatesimpleoptionmenu/">XmVaCreateSimpleOptionMenu</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatesimplepopupmenu/">XmVaCreateSimplePopupMenu</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatesimplepulldownmenu/">XmVaCreateSimplePulldownMenu</a></code>(3), and <code><a href="/docs/linux/man/3-xmvacreatesimpleradiobox/">XmVaCreateSimpleRadioBox</a></code>(3).</p>
