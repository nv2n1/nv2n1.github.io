---
title: "xmimgetxic(3)"
name: "xmimgetxic"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmimgetxic/"
description: "XmImGetXIC — An input manager function that obtains an XIC for a widget"
---

<p><code>XmImGetXIC</code> &#8212; An input manager function that obtains an XIC for a widget</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/XmIm.h&gt;
<code>XIC XmImGetXIC</code>(
<code>Widget widget</code>,
<code>XmInputPolicy input_policy</code>,
<code>ArgList args</code>,
<code>Cardinal num_args</code>);</pre>
<h2>Description</h2>
<p><code>XmImGetXIC</code> creates and registers an X Input Context (XIC) with the specified arguments for <i>widget</i>. If <code>XmINHERIT_POLICY</code> is specified for <i>input_policy</i>, a new XIC will be created only if required to by the arguments or by the <code>VendorShell</code> input policy. Any existing XIC registered with <i>widget</i> is unregistered. </p>
<p> Refer to the <code>VendorShell</code> reference page for further details.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of a widget for which an Input Context is to be created.</p>
<dt><i>input_policy</i></p>
<dd>Specifies the type of input policy. It accepts the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmINHERIT_POLICY</code></p>
<dd>Inherits the policy from <code>VendorShell</code>.</p>
<dt><code>XmPER_WIDGET</code></p>
<dd>Creates a new XIC for this widget.</p>
<dt><code>XmPER_SHELL</code></p>
<dd>Creates a new XIC for the shell, if needed.</dl>
</dl>
<dt><i>args</i></p>
<dd>Specifies an <code>XtArgList</code> parameter to use for creating the XIC.</p>
<dt><i>num_args</i></p>
<dd>Specifies the number of arguments in the <i>args</i> parameter.</dl>
<h2>Return</h2>
<p>Returns the created XIC. The application is responsible for freeing the returned XIC by calling <code>XmImFreeXIC</code>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmimsetxic/">XmImSetXIC</a></code>(3) and <code><a href="/docs/linux/man/3-xmimfreexic/">XmImFreeXIC</a></code>(3).</p>
