---
title: "xmimvasetvalues(3)"
name: "xmimvasetvalues"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmimvasetvalues/"
description: "XmImVaSetValues — An input manager function that updates attributes of an input context"
---

<p><code>XmImVaSetValues</code> &#8212; An input manager function that updates attributes of an input context</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/XmIm.h&gt;
<code>void XmImVaSetValues</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmImVaSetValues</code> updates attributes of the input context associated with the specified widget. This function passes the attributes to <code>XICSetValues</code>. The initial call to this routine should pass in all of the input context attributes. Thereafter, the application programmer calls <code>XmImVaSetValues</code> only if a value has changed. See the description in the <code><a href="/docs/linux/man/3-xmimsetvalues/">XmImSetValues</a></code>(3) man page for a list of associated resources. </p>
<p> This routine uses the ANSI C variable-length argument list (varargs) calling convention. The variable-length argument list consists of groups of arguments each of which contains an attribute followed by the value of the attribute. The last argument in the list must be NULL. </p>
<p> Note that the List and TextField widgets call the <code>XmImVaSetValues</code> function internally. Therefore, further calls to the <code>XmImVaSetValues</code> function for these widgets are unnecessary.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the widget registered with the input manager</dl>
<p> For more information on variable-length argument lists, see the X Toolkit Intrinsics documentation.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmimsetfocusvalues/">XmImSetFocusValues</a></code>(3), <code><a href="/docs/linux/man/3-xmimsetvalues/">XmImSetValues</a></code>(3), and <code><a href="/docs/linux/man/3-xmimvasetfocusvalues/">XmImVaSetFocusValues</a></code>(3).</p>
