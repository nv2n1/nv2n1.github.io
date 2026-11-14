---
title: "xmtextenableredisplay(3)"
name: "xmtextenableredisplay"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextenableredisplay/"
description: "XmTextEnableRedisplay — A Text function that forces the visual update of a Text widget"
---

<p><code>XmTextEnableRedisplay</code> &#8212; A Text function that forces the visual update of a Text widget</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Text.h&gt;
<code>void XmTextEnableRedisplay</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmTextEnableRedisplay</code> is used in conjunction with <code>XmTextDisableRedisplay</code>, which suppresses visual update of the Text widget. When <code>XmTextEnableRedisplay</code> is called, it determines if any visual attributes have been set or modified for the specified widget since <code>XmTextDisableRedisplay</code> was called. If so, it forces the widget to update its visual display for all of the intervening changes. Any subsequent changes that affect visual appearance cause the widget to update its visual display. This function also causes the insertion cursor, which is not shown while redisplay is disabled, to be restored.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the Text widget ID</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtextdisableredisplay/">XmTextDisableRedisplay</a></code>(3).</p>
