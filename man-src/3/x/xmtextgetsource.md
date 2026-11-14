---
title: "xmtextgetsource(3)"
name: "xmtextgetsource"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextgetsource/"
description: "XmTextGetSource — A Text function that accesses the source of the widget"
---

<p><code>XmTextGetSource</code> &#8212; A Text function that accesses the source of the widget</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Text.h&gt;
<code>XmTextSource XmTextGetSource</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmTextGetSource</code> accesses the source of the Text widget. Text widgets can share sources of text so that editing in one widget is reflected in another. This function accesses the source of one widget so that it can be made the source of another widget, using the function <code><a href="/docs/linux/man/3-xmtextsetsource/">XmTextSetSource</a></code>(3). </p>
<p> Setting a new text source destroys the old text source if no other Text widgets are using that source. To replace a text source but keep it for later use, create an unmanaged Text widget and set its source to the text source you want to keep.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the Text widget ID</dl>
<p> For a complete definition of Text and its associated resources, see <code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
<h2>Return</h2>
<p>Returns an <code>XmTextSource</code> value that represents the source of the Text widget.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
