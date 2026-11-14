---
title: "xmtextsetaddmode(3)"
name: "xmtextsetaddmode"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextsetaddmode/"
description: "XmTextSetAddMode — A Text function that sets the state of Add mode"
---

<p><code>XmTextSetAddMode</code> &#8212; A Text function that sets the state of Add mode</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Text.h&gt;
<code>void XmTextSetAddMode</code>(
<code>Widget widget</code>,
<code>Boolean state</code>);</pre>
<h2>Description</h2>
<p><code>XmTextSetAddMode</code> controls whether or not the Text widget is in Add mode. When the widget is in Add mode, the insert cursor can be moved without disturbing the primary selection.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the Text widget ID</p>
<dt><i>state</i></p>
<dd>Specifies whether or not the widget is in Add mode. A value of True turns on Add mode; a value of False turns off Add mode.</dl>
<p> For a complete definition of Text and its associated resources, see <code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
