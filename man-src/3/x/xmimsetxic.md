---
title: "xmimsetxic(3)"
name: "xmimsetxic"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmimsetxic/"
description: "XmImSetXIC — An input manager function that registers an existing XIC with a widget"
---

<p><code>XmImSetXIC</code> &#8212; An input manager function that registers an existing XIC with a widget</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/XmIm.h&gt;
<code>XIC XmImSetXIC</code>(
<code>Widget widget</code>,
<code>XIC xic</code>);</pre>
<h2>Description</h2>
<p><code>XmImSetXIC</code> registers the specified X Input Context (XIC) with <i>widget</i>. Any existing XIC registered for <i>widget</i> is unregistered. The new XIC registered for <i>widget</i> is returned. </p>
<p> If <i>xic</i> was not created by <code>XmImGetXIC</code> or <code>XmImRegister</code>, it will not be subject to closing activities when it has no widgets registered with it.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of a widget for which a new Input Context is to be registered.</p>
<dt><i>xic</i></p>
<dd>Specifies the Input Context to be registered with the widget. If <i>xic</i> is NULL, the function returns the current <code>XIC</code> used by <i>widget</i>.</dl>
<h2>Return</h2>
<p>Returns the new XIC registered for <i>widget</i>. The application is responsible for freeing the returned XIC. To free the XIC, call <code>XmImFreeXIC</code>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmimgetxic/">XmImGetXIC</a></code>(3) and <code><a href="/docs/linux/man/3-xmimfreexic/">XmImFreeXIC</a></code>(3).</p>
