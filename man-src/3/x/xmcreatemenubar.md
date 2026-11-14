---
title: "xmcreatemenubar(3)"
name: "xmcreatemenubar"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcreatemenubar/"
description: "XmCreateMenuBar — A RowColumn widget convenience creation function"
---

<p><code>XmCreateMenuBar</code> &#8212; A RowColumn widget convenience creation function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/RowColumn.h&gt;
<code>Widget XmCreateMenuBar</code>(
<code>Widget parent</code>,
<code>String name</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmCreateMenuBar</code> creates an instance of a RowColumn widget of type <code>XmMENU_BAR</code> and returns the associated widget ID. It is provided as a convenience function for creating RowColumn widgets configured to operate as a MenuBar and is not implemented as a separate widget class. </p>
<p> The MenuBar widget is generally used for building a Pulldown menu system. Typically, a MenuBar is created and placed along the top of the application window, and several CascadeButtons are inserted as the children. Each of the CascadeButtons has a Pulldown menu pane associated with it. These Pulldown menu panes must have been created as children of the MenuBar. The user interacts with the MenuBar by using either the mouse or the keyboard. </p>
<p> The MenuBar displays a 3-D shadow along its border. The application controls the shadow attributes using the visual-related resources supported by <code>XmManager</code>. </p>
<p> The MenuBar widget is homogeneous in that it accepts only children that are a subclass of <code>XmCascadeButton</code> or <code>XmCascadeButtonGadget</code>. Attempting to insert a child of a different class results in a warning message. </p>
<p> If the MenuBar does not have enough room to fit all of its subwidgets on a single line, the MenuBar attempts to wrap the remaining entries onto additional lines if allowed by the geometry manager of the parent widget.</p>
<dl COMPACT>
<dt><i>parent</i></p>
<dd>Specifies the parent widget ID</p>
<dt><i>name</i></p>
<dd>Specifies the name of the created widget</p>
<dt><i>arglist</i></p>
<dd>Specifies the argument list</p>
<dt><i>argcount</i></p>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>)</dl>
<p> For a complete definition of RowColumn and its associated resources, see <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the RowColumn widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmcascadebutton/">XmCascadeButton</a></code>(3), <code><a href="/docs/linux/man/3-xmcascadebuttongadget/">XmCascadeButtonGadget</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatepulldownmenu/">XmCreatePulldownMenu</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatesimplemenubar/">XmCreateSimpleMenuBar</a></code>(3), <code><a href="/docs/linux/man/3-xmmanager/">XmManager</a></code>(3), <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3), and <code><a href="/docs/linux/man/3-xmvacreatesimplemenubar/">XmVaCreateSimpleMenuBar</a></code>(3).</p>
