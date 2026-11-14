---
title: "xmcreateoptionmenu(3)"
name: "xmcreateoptionmenu"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcreateoptionmenu/"
description: "XmCreateOptionMenu — A RowColumn widget convenience creation function"
---

<p><code>XmCreateOptionMenu</code> &#8212; A RowColumn widget convenience creation function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/RowColumn.h&gt;
<code>Widget XmCreateOptionMenu</code>(
<code>Widget parent</code>,
<code>String name</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmCreateOptionMenu</code> creates an instance of a RowColumn widget of type <code>XmMENU_OPTION</code> and returns the associated widget ID. </p>
<p> It is provided as a convenience function for creating a RowColumn widget configured to operate as an OptionMenu and is not implemented as a separate widget class. </p>
<p> The OptionMenu widget is a specialized RowColumn manager composed of a label, a selection area, and a single Pulldown menu pane. When an application creates an OptionMenu widget, it supplies the label string and the Pulldown menu pane. In order for the operation to be successful, there must be a valid <code>XmNsubMenuId</code> resource set when this function is called. The LabelGadget and the selection area (a CascadeButtonGadget) are created by the OptionMenu. </p>
<p> The OptionMenu&#8217;s Pulldown menu pane must not contain any ToggleButtons or ToggleButtonGadgets. The results of including CascadeButtons or CascadeButtonGadgets in the OptionMenu&#8217;s Pulldown menu pane are undefined. </p>
<p> An OptionMenu is laid out with the label displayed on one side of the widget and the selection area on the other side when <code>XmNorientation</code> is <code>XmHORIZONTAL</code>. The layout of the label with respect to the selection area depends on the <code>XmNlayoutDirection</code> resource in the horizontal orientation. If the value is <code>XmVERTICAL</code>, the label is above the selection area. The selection area has a dual purpose; it displays the label of the last item selected from the associated Pulldown menu pane, and it provides the means for posting the Pulldown menu pane. </p>
<p> The OptionMenu typically does not display any 3-D visuals around itself or the internal LabelGadget. By default, the internal CascadeButtonGadget has a visible 3-D shadow. The application may change this by getting the CascadeButtonGadget ID using <code>XmOptionButtonGadget</code>, and then calling <code>XtSetValues</code> using the standard visual-related resources. </p>
<p> The Pulldown menu pane is posted when the mouse pointer is moved over the selection area and a mouse button that is defined by OptionMenu&#8217;s RowColumn parent is pressed. The Pulldown menu pane is posted and positioned so that the last selected item is directly over the selection area. The mouse is then used to arm the desired menu item. When the mouse button is released, the armed menu item is selected and the label within the selection area is changed to match that of the selected item. By default, <code>BSelect</code> is used to interact with an OptionMenu. The default can be changed with the RowColumn resource <code>XmNmenuPost</code>. </p>
<p> The OptionMenu also operates with the keyboard interface mechanism. If the application has established a mnemonic with the OptionMenu, pressing <code>&lt;Alt&gt;</code> with the mnemonic causes the Pulldown menu pane to be posted with traversal enabled. The standard traversal keys can then be used to move within the menu pane. Pressing <code>&lt;Return&gt;</code> or typing a mnemonic or accelerator for one of the menu items selects that item. </p>
<p> An application may use the <code>XmNmenuHistory</code> resource to indicate which item in the Pulldown menu pane should be treated as the current choice and have its label displayed in the selection area. By default, the first selectable item in the Pulldown menu pane is used.</p>
<dl COMPACT>
<dt><i>parent</i></p>
<dd>Specifies the parent widget ID</p>
<dt><i>name</i></p>
<dd>Specifies the name of the created widget</p>
<dt><i>arglist</i></p>
<dd>Specifies the argument list</p>
<dt><i>argcount</i></p>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>)</dl>
<p> The user can specify resources in a resource file for the automatically created widgets and gadgets of an OptionMenu. These widgets (or gadgets) and the associated OptionMenu areas are</p>
<dl COMPACT>
<dt>Option Menu Label Gadget</p>
<dd><code>OptionLabel</code></p>
<dt>Option Menu Cascade Button</p>
<dd><code>OptionButton</code></dl>
<p> For a complete definition of RowColumn and its associated resources, see <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the RowColumn widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmcascadebuttongadget/">XmCascadeButtonGadget</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatepulldownmenu/">XmCreatePulldownMenu</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatesimpleoptionmenu/">XmCreateSimpleOptionMenu</a></code>(3), <code><a href="/docs/linux/man/3-xmlabelgadget/">XmLabelGadget</a></code>(3), <code><a href="/docs/linux/man/3-xmoptionbuttongadget/">XmOptionButtonGadget</a></code>(3), <code><a href="/docs/linux/man/3-xmoptionlabelgadget/">XmOptionLabelGadget</a></code>(3), <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3), and <code><a href="/docs/linux/man/3-xmvacreatesimpleoptionmenu/">XmVaCreateSimpleOptionMenu</a></code>(3).</p>
