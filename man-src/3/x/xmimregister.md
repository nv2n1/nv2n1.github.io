---
title: "xmimregister(3)"
name: "xmimregister"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmimregister/"
description: "XmImRegister — An input manager function that registers a widget with an input manager"
---

<p><code>XmImRegister</code> &#8212; An input manager function that registers a widget with an input manager</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/XmIm.h&gt;
<code>void XmImRegister</code>(
<code>Widget widget</code>,
<code>unsigned int reserved</code>);</pre>
<h2>Description</h2>
<p><code>XmImRegister</code> registers a widget with its input manager. This adds the specified widget to a list of widgets that are supported by the input manager for an input method. If an input method has not been opened by a previous call to <code>XmImRegister</code>, the first time this routine is called it opens an input method using the <code>XmNinputMethod</code> resource for the VendorShell. If the <code>XmNinputMethod</code> is NULL, an input method is opened using the current locale. </p>
<p> If an input method cannot be opened in the current locale, <code>XLookupString</code> provides input processing. </p>
<p> The application is responsible for unregistering a widget by calling <code>XmImUnregister</code>. </p>
<p> Note that the Text, TextField, and List widgets already call the <code>XmImRegister</code> function internally. You should not call this function for these widgets before calling <code>XmImUnregister</code> first.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the widget to be registered.</p>
<dt><i>reserved</i></p>
<dd>This argument is not used in the current release of Motif. The value should always be 0 (zero).</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmimgetxim/">XmImGetXIM</a></code>(3), <code><a href="/docs/linux/man/3-xmimmblookupstring/">XmImMbLookupString</a></code>(3), and <code><a href="/docs/linux/man/3-xmimunregister/">XmImUnregister</a></code>(3).</p>
