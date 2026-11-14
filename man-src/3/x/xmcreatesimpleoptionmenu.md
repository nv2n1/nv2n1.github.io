---
title: "xmcreatesimpleoptionmenu(3)"
name: "xmcreatesimpleoptionmenu"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcreatesimpleoptionmenu/"
description: "XmCreateSimpleOptionMenu — A RowColumn widget convenience creation function"
---

<p><code>XmCreateSimpleOptionMenu</code> &#8212; A RowColumn widget convenience creation function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/RowColumn.h&gt;
<code>Widget XmCreateSimpleOptionMenu</code>(
<code>Widget parent</code>,
<code>String name</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmCreateSimpleOptionMenu</code> creates an instance of a RowColumn widget of type <code>XmMENU_OPTION</code> and returns the associated widget ID. </p>
<p> This routine creates an OptionMenu and its submenu containing PushButtonGadget or CascadeButtonGadget children. The name of each button is <code>button_</code><i>n</i>, where <i>n</i> is an integer from 0 (zero) to the number of buttons in the menu minus 1. The name of each separator is <code>separator_</code><i>n</i>, where <i>n</i> is an integer from 0 (zero) to the number of separators in the menu minus 1. Buttons and separators are named and created in the order they are specified in the RowColumn simple menu creation resources supplied in the argument list.</p>
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
<p> A number of resources exist specifically for use with this and other simple menu creation routines. The only button types allowed in the <code>XmNbuttonType</code> resource are <code>XmPUSHBUTTON</code>, <code>XmCASCADEBUTTON</code>, <code>XmSEPARATOR</code>, and <code>XmDOUBLE_SEPARATOR</code>. For a complete definition of RowColumn and its associated resources, see <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the RowColumn widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmcreateoptionmenu/">XmCreateOptionMenu</a></code>(3), <code><a href="/docs/linux/man/3-xmcreaterowcolumn/">XmCreateRowColumn</a></code>(3), <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3), and <code><a href="/docs/linux/man/3-xmvacreatesimpleoptionmenu/">XmVaCreateSimpleOptionMenu</a></code>(3).</p>
