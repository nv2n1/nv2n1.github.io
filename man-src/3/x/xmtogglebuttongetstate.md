---
title: "xmtogglebuttongetstate(3)"
name: "xmtogglebuttongetstate"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtogglebuttongetstate/"
description: "XmToggleButtonGetState — A ToggleButton function that obtains the state of a ToggleButton"
---

<p><code>XmToggleButtonGetState</code> &#8212; A ToggleButton function that obtains the state of a ToggleButton</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/ToggleB.h&gt;
<code>Boolean XmToggleButtonGetState</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmToggleButtonGetState</code> obtains the state of a ToggleButton.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ToggleButton widget ID</dl>
<p> For a complete definition of ToggleButton and its associated resources, see <code><a href="/docs/linux/man/3-xmtogglebutton/">XmToggleButton</a></code>(3).</p>
<h2>Return</h2>
<p>Returns True if the button is selected and False if the button is unselected.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtogglebutton/">XmToggleButton</a></code>(3).</p>
