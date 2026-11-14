---
title: "xmimvasetfocusvalues(3)"
name: "xmimvasetfocusvalues"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmimvasetfocusvalues/"
description: "XmImVaSetFocusValues — An input manager function that notifies an input manager that a widget has received input focus and updates the input context attributes"
---

<p><code>XmImVaSetFocusValues</code> &#8212; An input manager function that notifies an input manager that a widget has received input focus and updates the input context attributes</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/XmIm.h&gt;
<code>void XmImVaSetFocusValues</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmImVaSetFocusValues</code> notifies the input manager that the specified widget has received input focus. This function also updates the attributes of the input context associated with the widget. This function passes the attributes and values to <code>XICSetValues</code>. The caller of this routine should pass in only those values that have changed since the last call to any of these functions; <code>XmImVaSetValues</code>, <code>XmImVaSetFocusValues</code>, <code>XmImSetValues</code>, or <code>XmImSetFocusValues</code>. See the description in the <code><a href="/docs/linux/man/3-xmimsetvalues/">XmImSetValues</a></code>(3) reference page for a list of associated resources. </p>
<p> This routine uses the ANSI C variable-length argument list (varargs) calling conventions. The variable-length argument list consists of groups of arguments each of which contains an attribute followed by the value of the attribute. The last argument in the list must be NULL </p>
<p> Note that the List and TextField widgets call the <code>XmImVaSetFocusValues</code> function when they receive focus. Therefore, further calls to the <code>XmImVaSetFocusValues</code> function for these widgets are unnecessary.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the widget registered with the input manager</dl>
<p> For more information on variable-length argument lists, see the X Toolkit Intrinsics documentation.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmimsetfocusvalues/">XmImSetFocusValues</a></code>(3), <code><a href="/docs/linux/man/3-xmimsetvalues/">XmImSetValues</a></code>(3), and <code><a href="/docs/linux/man/3-xmimvasetvalues/">XmImVaSetValues</a></code>(3).</p>
