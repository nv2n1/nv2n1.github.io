---
title: "xmvacreatesimpleradiobox(3)"
name: "xmvacreatesimpleradiobox"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmvacreatesimpleradiobox/"
description: "XmVaCreateSimpleRadioBox — A RowColumn widget convenience creation function"
---

<p><code>XmVaCreateSimpleRadioBox</code> &#8212; A RowColumn widget convenience creation function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/RowColumn.h&gt;
<code>Widget XmVaCreateSimpleRadioBox</code>(
<code>Widget parent</code>,
<code>String name</code>,
<code>int button_set</code>,
<code>XtCallbackProc callback</code>);</pre>
<h2>Description</h2>
<p><code>XmVaCreateSimpleRadioBox</code> creates an instance of a RowColumn widget of type <code>XmWORK_AREA</code> and returns the associated widget ID. This routine uses the ANSI C variable-length argument list (<i>varargs</i>) calling convention. </p>
<p> This routine creates a RadioBox and its ToggleButtonGadget children. The name of each button is <code>button_</code><i>n</i>, where <i>n</i> is an integer from 0 (zero) to the number of buttons in the menu minus 1.</p>
<dl COMPACT>
<dt><i>parent</i></p>
<dd>Specifies the parent widget ID.</p>
<dt><i>name</i></p>
<dd>Specifies the name of the created widget.</p>
<dt><i>button_set</i></p>
<dd>Specifies which button is initially set. The value is the integer <i>n</i> in the button name <code>button_</code><i>n</i>.</p>
<dt><i>callback</i></p>
<dd>Specifies a callback procedure to be called when a button&#8217;s value changes. This callback function is added to each button after creation as the button&#8217;s <code>XmNvalueChangedCallback</code>. The callback function is called when a button&#8217;s value changes, and the button number is returned in the <i>client_data</i> field.</dl>
<p> The variable portion of the argument list consists of groups of arguments. The first argument in each group is a constant or a string and determines which arguments follow in that group. The last argument in the list must be NULL. Following are the possible first arguments in each group of <i>varargs</i>:</p>
<dl COMPACT>
<dt><code>XmVaRADIOBUTTON</code></p>
<dd>This is followed by four additional arguments. The set specifies one button in the RadioBox and some of its resource values. Following are the additional four arguments, in order:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><i>label</i></p>
<dd>The label string, of type <code>XmString</code>.</p>
<dt><i>mnemonic</i></p>
<dd>The mnemonic, of type <code>KeySym</code>. This is ignored in this release.</p>
<dt><i>accelerator</i></p>
<dd>The accelerator, of type <code>String</code>. This is ignored in this release.</p>
<dt><i>accelerator_text</i></p>
<dd>The accelerator text, of type <code>XmString</code>. This is ignored in this release.</dl>
</dl>
<dt><i>resource_name</i></p>
<dd>This is followed by one additional argument, the value of the resource, of type <code>XtArgVal</code>. The pair specifies a resource and its value for the RowColumn widget.</p>
<dt><code>XtVaTypedArg</code></p>
<dd>This is followed by four additional arguments. The set specifies a resource and its value for the RowColumn widget. A resource type conversion is performed if necessary. Following are the additional four arguments, in this order:</p>
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
<p> For more information on variable-length argument lists, see the X Toolkit Intrinsics documentation. </p>
<p> A number of resources exist specifically for use with this and other simple menu creation routines. For a complete definition of RowColumn and its associated resources, see <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the RowColumn widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmcreateradiobox/">XmCreateRadioBox</a></code>(3), <code><a href="/docs/linux/man/3-xmcreaterowcolumn/">XmCreateRowColumn</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatesimplecheckbox/">XmCreateSimpleCheckBox</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatesimpleradiobox/">XmCreateSimpleRadioBox</a></code>(3), <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3), and <code><a href="/docs/linux/man/3-xmvacreatesimplecheckbox/">XmVaCreateSimpleCheckBox</a></code>(3),</p>
