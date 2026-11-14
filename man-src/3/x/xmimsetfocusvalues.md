---
title: "xmimsetfocusvalues(3)"
name: "xmimsetfocusvalues"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmimsetfocusvalues/"
description: "XmImSetFocusValues — An input manager function that notifies an input manager that a widget has received input focus and updates the input context attributes"
---

<p><code>XmImSetFocusValues</code> &#8212; An input manager function that notifies an input manager that a widget has received input focus and updates the input context attributes</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/XmIm.h&gt;
<code>void XmImSetFocusValues</code>(
<code>Widget widget</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>,
);</pre>
<h2>Description</h2>
<p><code>XmImSetFocusValues</code> notifies the input manager that the specified widget has received input focus. This function also updates the attributes of the input context associated with the widget. The focus window for the XIC is set to the window of the widget. The <i>arglist</i> argument is a list of attribute/value pairs for the input context. This function passes the attributes and values to <code>XICSetValues</code>. The caller of this routine should pass in only those values that have changed since the last call to any of these functions; <code>XmImSetValues</code>, <code>XmImSetFocusValues</code>, <code>XmImVaSetValues</code>, or <code>XmImVaSetFocusValues</code>. See the description in the <code><a href="/docs/linux/man/3-xmimsetvalues/">XmImSetValues</a></code>(3) reference page for a list of associated resources. </p>
<p> If the previous parameters for the widget&#8217;s XIC do not allow the previously registered XIC to be reused, that XIC will be unregistered, and a new one will be created and registered with the widget. Note that sharing of data is preserved.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the widget registered with the input manager.</p>
<dt><i>arglist</i></p>
<dd>Specifies the list of attribute/value pairs to be passed to <code>XICSetValues</code>. See the description in the <code><a href="/docs/linux/man/3-xmimsetvalues/">XmImSetValues</a></code>(3) man page for a description of resources.</p>
<dt><i>argcount</i></p>
<dd>Specifies the number of attribute/values pairs in the argument list (<i>arglist)</i></dl>
<p> Note that the Text and TextField widgets call the <code>XmImSetFocusValues</code> function when they receive focus. Therefore, further calls to the <code>XmImSetFocusValues</code> function for these widgets are unnecessary.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmimsetvalues/">XmImSetValues</a></code>(3), <code><a href="/docs/linux/man/3-xmimvasetfocusvalues/">XmImVaSetFocusValues</a></code>(3), and <code><a href="/docs/linux/man/3-xmimvasetvalues/">XmImVaSetValues</a></code>(3).</p>
