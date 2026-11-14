---
title: "xmtextshowposition(3)"
name: "xmtextshowposition"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextshowposition/"
description: "XmTextShowPosition — A Text function that forces text at a given position to be displayed"
---

<p><code>XmTextShowPosition</code> &#8212; A Text function that forces text at a given position to be displayed</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Text.h&gt;
<code>void XmTextShowPosition</code>(
<code>Widget widget</code>,
<code>XmTextPosition position</code>);</pre>
<h2>Description</h2>
<p><code>XmTextShowPosition</code> forces text at the specified position to be displayed. If the <code>XmNautoShowCursorPosition</code> resource is True, the application should also set the insert cursor to this position.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the Text widget ID</p>
<dt><i>position</i></p>
<dd>Specifies the character position to be displayed. This is an integer number of characters from the beginning of the text buffer. The first character position is 0 (zero).</dl>
<p> If a navigator exists, this function uses the <code>XmQTnavigator</code> trait to update the horizontal navigator&#8217;s value. </p>
<p> For a complete definition of Text and its associated resources, see <code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
