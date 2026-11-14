---
title: "xmimunregister(3)"
name: "xmimunregister"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmimunregister/"
description: "XmImUnregister — An input manager function that removes a widget from association with its input manager"
---

<p><code>XmImUnregister</code> &#8212; An input manager function that removes a widget from association with its input manager</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/XmIm.h&gt;
<code>void XmImUnregister</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmImUnregister</code> removes the specified widget from the list of widgets registered for input by the input manager. </p>
<p> Note that the Text, TextField, and List widgets already call the <code>XmImRegister</code> internally. You should call the <code>XmImUnregister</code> function for these widgets before calling <code>XmImRegister</code>.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the widget to be unregistered</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmimregister/">XmImRegister</a></code>(3).</p>
