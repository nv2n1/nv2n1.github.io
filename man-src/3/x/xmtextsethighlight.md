---
title: "xmtextsethighlight(3)"
name: "xmtextsethighlight"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextsethighlight/"
description: "XmTextSetHighlight — A Text function that highlights text"
---

<p><code>XmTextSetHighlight</code> &#8212; A Text function that highlights text</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Text.h&gt;
<code>void XmTextSetHighlight</code>(
<code>Widget widget</code>,
<code>XmTextPosition left</code>,
<code>XmTextPosition right</code>,
<code>XmHighlightMode mode</code>);</pre>
<h2>Description</h2>
<p><code>XmTextSetHighlight</code> highlights text between the two specified character positions. The <i>mode</i> parameter determines the type of highlighting. Highlighting text merely changes the visual appearance of the text; it does not set the selection.</p>
<dl COMPACT>
<dt><i>widget</i></dt>
<dd>Specifies the Text widget ID</dd>
<dt><i>left</i></dt>
<dd>Specifies the position of the left boundary of text to be highlighted. This is an integer number of characters from the beginning of the text buffer. The first character position is 0 (zero).</dd>
<dt><i>right</i></dt>
<dd>Specifies the position of the right boundary of text to be highlighted. This is an integer number of characters from the beginning of the text buffer. The first character position is 0 (zero).</dd>
<dt><i>mode</i></dt>
<dd>Specifies the type of highlighting to be done. A value of <code>XmHIGHLIGHT_NORMAL</code> removes highlighting. A value of <code>XmHIGHLIGHT_SELECTED</code> highlights the text using reverse video. A value of <code>XmHIGHLIGHT_SECONDARY_SELECTED</code> highlights the text using underlining.</dd></dl>
<p> For a complete definition of Text and its associated resources, see <code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
