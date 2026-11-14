---
title: "xmoptionlabelgadget(3)"
name: "xmoptionlabelgadget"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmoptionlabelgadget/"
description: "XmOptionLabelGadget — A RowColumn function that obtains the widget ID for the LabelGadget in an OptionMenu"
---

<p><code>XmOptionLabelGadget</code> &#8212; A RowColumn function that obtains the widget ID for the LabelGadget in an OptionMenu</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/RowColumn.h&gt;
<code>Widget XmOptionLabelGadget</code>(
<code>Widget option_menu</code>);</pre>
<h2>Description</h2>
<p><code>XmOptionLabelGadget</code> provides the application with the means for obtaining the widget ID for the internally created LabelGadget. Once the application has obtained the widget ID, it can adjust the visuals for the LabelGadget, if desired.</p>
<dl COMPACT>
<dt><i>option_menu</i></p>
<dd>Specifies the OptionMenu widget ID</dl>
<p> When an application creates an instance of the OptionMenu widget, the widget creates two internal gadgets. One is a LabelGadget that is used to display RowColumn&#8217;s <code>XmNlabelString</code> resource. The other is a CascadeButtonGadget that displays the current selection and provides the means for posting the OptionMenu&#8217;s submenu. </p>
<p> The user can specify resources in a resource file for the automatically created widgets and gadgets of an OptionMenu. The following list identifies the names of these widgets (or gadgets) and the associated OptionMenu areas.</p>
<dl COMPACT>
<dt>Option Menu Label Gadget</p>
<dd><code>OptionLabel</code></p>
<dt>Option Menu Cascade Button</p>
<dd><code>OptionButton</code></dl>
<p> For a complete definition of RowColumn and its associated resources, see <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the widget ID for the internal label.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmcreateoptionmenu/">XmCreateOptionMenu</a></code>(3), <code><a href="/docs/linux/man/3-xmlabelgadget/">XmLabelGadget</a></code>(3), <code><a href="/docs/linux/man/3-xmoptionbuttongadget/">XmOptionButtonGadget</a></code>(3), and <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3).</p>
