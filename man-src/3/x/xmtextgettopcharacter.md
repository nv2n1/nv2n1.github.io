---
title: "xmtextgettopcharacter(3)"
name: "xmtextgettopcharacter"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextgettopcharacter/"
description: "XmTextGetTopCharacter — A Text function that accesses the position of the first character displayed"
---

<p><code>XmTextGetTopCharacter</code> &#8212; A Text function that accesses the position of the first character displayed</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Text.h&gt;
<code>XmTextPosition XmTextGetTopCharacter</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmTextGetTopCharacter</code> accesses the position of the text at the top of the Text widget. If there is no text in the Text widget (in other words, <code>XmNvalue</code> contains an empty string), then <code>XmTextGetTopCharacter</code> returns 0. </p>
<p> Suppose that the <code>XmNtopCharacter</code> resource has been set to a value greater than the number of characters in the text widget. In this case, <code>XmTextGetTopCharacter</code> returns an <code>XmTextPosition</code> value identifying the position of the first character in the last line of text in a multiline case; otherwise, it identifies the position of the last character in the line.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the Text widget ID</dl>
<p> For a complete definition of Text and its associated resources, see <code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
<h2>Return</h2>
<p>Returns an <code>XmTextPosition</code> value that indicates the state of the <code>XmNtopCharacter</code> resource. This is an integer number of characters from the beginning of the text buffer. The first character position is 0 (zero).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
