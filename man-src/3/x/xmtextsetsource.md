---
title: "xmtextsetsource(3)"
name: "xmtextsetsource"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextsetsource/"
description: "XmTextSetSource — A Text function that sets the source of the widget"
---

<p><code>XmTextSetSource</code> &#8212; A Text function that sets the source of the widget</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Text.h&gt;
<code>void XmTextSetSource</code>(
<code>Widget widget</code>,
<code>XmTextSource source</code>,
<code>XmTextPosition top_character</code>,
<code>XmTextPosition cursor_position</code>);</pre>
<h2>Description</h2>
<p><code>XmTextSetSource</code> sets the source of the Text widget. Text widgets can share sources of text so that editing in one widget is reflected in another. This function sets the source of one widget so that it can share the source of another widget. </p>
<p> Setting a new text source destroys the old text source if no other Text widgets are using that source. To replace a text source but keep it for later use, create an unmanaged Text widget and set its source to the text source you want to keep.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the Text widget ID.</p>
<dt><i>source</i></p>
<dd>Specifies the source with which the widget displays text. This can be a value returned by the <code><a href="/docs/linux/man/3-xmtextgetsource/">XmTextGetSource</a></code>(3) function. If no source is specified, the widget creates a default string source.</p>
<dt><i>top_character</i></p>
<dd>Specifies the position in the text to display at the top of the widget. This is an integer number of characters from the beginning of the text buffer. The first character position is 0 (zero).</p>
<dt><i>cursor_position</i></p>
<dd>Specifies the position in the text at which the insert cursor is located. This is an integer number of characters from the beginning of the text buffer. The first character position is 0 (zero).</dl>
<p> For a complete definition of Text and its associated resources, see <code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
