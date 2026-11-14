---
title: "xmtextdisableredisplay(3)"
name: "xmtextdisableredisplay"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextdisableredisplay/"
description: "XmTextDisableRedisplay — A Text function that temporarily prevents visual update of the Text widget"
---

<p><code>XmTextDisableRedisplay</code> &#8212; A Text function that temporarily prevents visual update of the Text widget</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Text.h&gt;
<code>void XmTextDisableRedisplay</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmTextDisableRedisplay</code> prevents redisplay of the specified Text widget even though its visual attributes have been modified. The visual appearance of the widget remains unchanged until <code>XmTextEnableRedisplay</code> is called, although the insertion cursor is not displayed. This allows an application to make multiple changes to the widget without causing intermediate visual updates.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the Text widget ID</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtextenableredisplay/">XmTextEnableRedisplay</a></code>(3).</p>
