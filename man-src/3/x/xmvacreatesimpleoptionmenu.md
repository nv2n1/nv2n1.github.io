---
title: "xmvacreatesimpleoptionmenu(3)"
name: "xmvacreatesimpleoptionmenu"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmvacreatesimpleoptionmenu/"
description: "XmVaCreateSimpleOptionMenu — A RowColumn widget convenience creation function"
---

<p><code>XmVaCreateSimpleOptionMenu</code> &#8212; A RowColumn widget convenience creation function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/RowColumn.h&gt;
<code>Widget XmVaCreateSimpleOptionMenu</code>(
<code>Widget parent</code>,
<code>String name</code>,
<code>XmString option_label</code>,
<code>KeySym option_mnemonic</code>,
<code>int button_set</code>,
<code>XtCallbackProc callback</code>);</pre>
<h2>Description</h2>
<p><code>XmVaCreateSimpleOptionMenu</code> creates an instance of a RowColumn widget of type <code>XmMENU_OPTION</code> and returns the associated widget ID. This routine uses the ANSI C variable-length argument list (<i>varargs</i>) calling convention. </p>
<p> This routine creates an OptionMenu and its Pulldown submenu containing PushButtonGadget or CascadeButtonGadget children. The name of each button is <code>button_</code><i>n</i>, where <i>n</i> is an integer from 0 (zero) to the number of buttons in the menu minus 1. The name of each separator is <code>separator_</code><i>n</i>, where <i>n</i> is an integer from 0 (zero) to the number of separators in the menu minus 1. Buttons and separators are named and created in the order in which they are specified in the variable portion of the argument list.</p>
<dl COMPACT>
<dt><i>parent</i></p>
<dd>Specifies the parent widget ID</p>
<dt><i>name</i></p>
<dd>Specifies the name of the created widget</p>
<dt><i>option_label</i></p>
<dd>Specifies the label string to be used on the left side of the OptionMenu.</p>
<dt><i>option_mnemonic</i></p>
<dd>Specifies a keysym for a key that, when pressed by the user, posts the associated Pulldown menu pane.</p>
<dt><i>button_set</i></p>
<dd>Specifies which PushButtonGadget is initially set. The value is the integer <i>n</i> that corresponds to the <i>n</i>th PushButtonGadget specified in the variable portion of the argument list. Only a PushButtonGadget can be set, and only PushButtonGadgets are counted in determining the integer <i>n</i>. The first PushButtonGadget is number 0 (zero).</p>
<dt><i>callback</i></p>
<dd>Specifies a callback procedure to be called when a button is activated. This callback function is added to each button after creation as the button&#8217;s <code>XmNactivateCallback</code>. The callback function is called when a button is activated, and the button number is returned in the <i>client_data</i> field.</dl>
<p> The variable portion of the argument list consists of groups of arguments. The first argument in each group is a constant or a string and determines which arguments follow in that group. The last argument in the list must be NULL. Following are the possible first arguments in each group of <i>varargs</i>:</p>
<dl COMPACT>
<dt><code>XmVaPUSHBUTTON</code></p>
<dd>This is followed by four additional arguments. The set specifies one button in the OptionMenu&#8217;s Pulldown submenu and some of its resource values. The button created is a PushButtonGadget. Following are the additional four arguments, in order:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><i>label</i></p>
<dd>The label string, of type <code>XmString</code></p>
<dt><i>mnemonic</i></p>
<dd>The mnemonic, of type <code>KeySym</code></p>
<dt><i>accelerator</i></p>
<dd>The accelerator, of type <code>String</code></p>
<dt><i>accelerator_text</i></p>
<dd>The accelerator text, of type <code>XmString</code></dl>
</dl>
<dt><code>XmVaSEPARATOR</code></p>
<dd>This is followed by no additional arguments. It specifies one separator in the OptionMenu&#8217;s Pulldown submenu.</p>
<dt><code>XmVaDOUBLE_SEPARATOR</code></p>
<dd>This is followed by no additional arguments. It specifies one separator in the OptionMenu&#8217;s Pulldown submenu. The separator type is <code>XmDOUBLE_LINE</code>.</p>
<dt><i>resource_name</i></p>
<dd>This is followed by one additional argument, the value of the resource, of type <code>XtArgVal</code>. The pair specifies a resource and its value for the Pulldown submenu.</p>
<dt><code>XtVaTypedArg</code></p>
<dd>This is followed by four additional arguments. The set specifies a resource and its value for the Pulldown submenu. A resource type conversion is performed if necessary. Following are the additional four arguments, in order:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><i>name</i></p>
<dd>The resource name, of type <code>String</code></p>
<dt><i>type</i></p>
<dd>The type of the resource value supplied, of type <code>String</code></p>
<dt><i>value</i></p>
<dd>The resource value (or a pointer to the resource value, depending on the type and size of the value), of type <code>XtArgVal</code></p>
<dt><i>size</i></p>
<dd>The size of the resource value in bytes, of type <i>int</i></dl>
</dl>
<dt><code>XtVaNestedList</code></p>
<dd>This is followed by one additional argument of type <code>XtVarArgsList</code>. This argument is a nested list of <i>varargs</i> returned by <code>XtVaCreateArgsList</code>.</dl>
<p> The user can specify resources in a resource file for the automatically created widgets and gadgets of an OptionMenu. The following list identifies the names of these widgets (or gadgets) and the associated OptionMenu areas:</p>
<dl COMPACT>
<dt>Option Menu Label Gadget</p>
<dd><code>OptionLabel</code></p>
<dt>Option Menu Cascade Button</p>
<dd><code>OptionButton</code></dl>
<p> For more information on variable-length argument lists, see the X Toolkit Intrinsics documentation. </p>
<p> A number of resources exist specifically for use with this and other simple menu creation routines. For a complete definition of RowColumn and its associated resources, see <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the RowColumn widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmcreateoptionmenu/">XmCreateOptionMenu</a></code>(3), <code><a href="/docs/linux/man/3-xmcreaterowcolumn/">XmCreateRowColumn</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatesimpleoptionmenu/">XmCreateSimpleOptionMenu</a></code>(3), and <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3).</p>
