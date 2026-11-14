---
title: "xmtextsettopcharacter(3)"
name: "xmtextsettopcharacter"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextsettopcharacter/"
description: "XmTextSetTopCharacter — A Text function that sets the position of the first character displayed"
---

<p><code>XmTextSetTopCharacter</code> &#8212; A Text function that sets the position of the first character displayed</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Text.h&gt;
<code>void XmTextSetTopCharacter</code>(
<code>Widget widget</code>,
<code>XmTextPosition top_character</code>);</pre>
<h2>Description</h2>
<p><code>XmTextSetTopCharacter</code> sets the position of the text at the top of the Text widget. If the <code>XmNeditMode</code> is <code>XmMULTI_LINE_EDIT</code>, the line of text that contains <i>top_character</i> is displayed at the top of the widget without the text shifting left or right. If the edit mode is <code>XmSINGLE_LINE_EDIT</code>, the text moves horizontally so that <i>top_character</i> is the first character displayed.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the Text widget ID</p>
<dt><i>top_character</i></p>
<dd>Specifies the position in the text to display at the top of the widget. This is an integer number of characters from the beginning of the text buffer. The first character position is 0 (zero).</dl>
<p> For a complete definition of Text and its associated resources, see <code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
