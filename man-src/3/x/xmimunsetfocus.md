---
title: "xmimunsetfocus(3)"
name: "xmimunsetfocus"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmimunsetfocus/"
description: "XmImUnsetFocus — An input manager function that notifies an input method that a widget has lost input focus"
---

<p><code>XmImUnsetFocus</code> &#8212; An input manager function that notifies an input method that a widget has lost input focus</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/XmIm.h&gt;
<code>void XmImUnsetFocus</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmImUnsetFocus</code> unsets a specified widget&#8217;s focus, then notifies the input manager that the specified widget has lost its input focus. </p>
<p> Note that the Text, TextField, and List widgets already call the <code>XmImUnsetFocus</code> internally. Therefore, further calls to the <code>XmImUnsetFocus</code> function for those widgets are unnecessary.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the widget registered with the input manager</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmimsetfocusvalues/">XmImSetFocusValues</a></code>(3) and <code><a href="/docs/linux/man/3-xmimvasetfocusvalues/">XmImVaSetFocusValues</a></code>(3).</p>
