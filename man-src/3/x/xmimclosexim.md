---
title: "xmimclosexim(3)"
name: "xmimclosexim"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmimclosexim/"
description: "XmImCloseXIM — An input manager function that releases the input method associated with a specified widget"
---

<p><code>XmImCloseXIM</code> &#8212; An input manager function that releases the input method associated with a specified widget</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/XmIm.h&gt;
<code>void XmImCloseXIM</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmImCloseXIM</code> closes all input contexts associated with the Input Method (IM) of <i>widget</i>. <i>widget</i> is used to identify the Display that specifies the Input Method opened for the widget. Upon closure, all widgets registered with the input contexts are unregistered. Also, the Input Method specified by Display is closed.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of a widget whose reference Input Method is to be closed.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmimgetxim/">XmImGetXIM</a></code>(3) and <code><a href="/docs/linux/man/3-xmimregister/">XmImRegister</a></code>(3).</p>
