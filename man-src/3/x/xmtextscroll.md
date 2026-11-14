---
title: "xmtextscroll(3)"
name: "xmtextscroll"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextscroll/"
description: "XmTextScroll — A Text function that scrolls text"
---

<p><code>XmTextScroll</code> &#8212; A Text function that scrolls text</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Text.h&gt;
<code>void XmTextScroll</code>(
<code>Widget widget</code>,
<code>int lines</code>);</pre>
<h2>Description</h2>
<p><code>XmTextScroll</code> scrolls text by a given number of lines in a Text widget. The sign of the number is interpreted according to the value of the <code>XmNlayoutDirection</code> resource.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the Text widget ID</p>
<dt><i>lines</i></p>
<dd>Specifies the number of lines of text to scroll. A positive value causes text to scroll upward; a negative value causes text to scroll downward. Note that the text will scroll only as long as one line of text remains visible in the window.</p>
<dd>If a navigator exists, this function uses the <code>XmQTnavigator</code> trait to update the vertical navigator&#8217;s value.</p>
<dd>In the case of vertical writing, a positive value causes the text to scroll forward; a negative value causes the lines to scroll backward.</dl>
<p> For a complete definition of Text and its associated resources, see <code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
