---
title: "xmlistsetaddmode(3)"
name: "xmlistsetaddmode"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmlistsetaddmode/"
description: "XmListSetAddMode — A List function that sets add mode in the list"
---

<p><code>XmListSetAddMode</code> &#8212; A List function that sets add mode in the list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/List.h&gt;
<code>void XmListSetAddMode</code>(
<code>Widget widget</code>,
<code>Boolean state</code>);</pre>
<h2>Description</h2>
<p><code>XmListSetAddMode</code> allows applications control over Add Mode in the extended selection model. This function ensures that the mode it sets is compatible with the selection policy (<code>XmNselectionPolicy</code>) of the widget. For example, it cannot put the widget into add mode when the value of <code>XmNselectionPolicy</code> is <code>XmBROWSE_SELECT</code>.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the List widget</p>
<dt><i>state</i></p>
<dd>Specifies whether to activate or deactivate Add Mode. If <i>state</i> is True, Add Mode is activated. If <i>state</i> is False, Add Mode is deactivated.</dl>
<p> For a complete definition of List and its associated resources, see <code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
