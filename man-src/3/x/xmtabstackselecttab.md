---
title: "xmtabstackselecttab(3)"
name: "xmtabstackselecttab"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtabstackselecttab/"
description: "XmTabStackSelectTab — A TabStack function that sets the currently displayed child"
---

<p><code>XmTabStackSelectTab</code> &#8212; A TabStack function that sets the currently displayed child</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/TabStack.h&gt;
<code>void XmTabStackSelectTab</code>(
<code>Widget widget</code>,
<code>Boolean notify);
</code></pre>
<h2>Description</h2>
<p><code>XmTabStackSelectTab</code> sets the currently displayed child of the TabStack.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the TabStack widget ID</p>
<dt><i>notify</i></p>
<dd>Specifies weather to call XmNtabSelectedCallback as usual in response to the change of state</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtabstack/">XmTabStack</a></code>(3).</p>
