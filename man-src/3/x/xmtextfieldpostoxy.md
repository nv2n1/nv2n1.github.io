---
title: "xmtextfieldpostoxy(3)"
name: "xmtextfieldpostoxy"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtextfieldpostoxy/"
description: "XmTextFieldPosToXY — A TextField function that accesses the x and y position of a character position"
---

<p><code>XmTextFieldPosToXY</code> &#8212; A TextField function that accesses the x and y position of a character position</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/TextF.h&gt;
<code>Boolean XmTextFieldPosToXY</code>(
<code>Widget widget</code>,
<code>XmTextPosition position</code>,
<code>Position *x</code>,
<code>Position *y</code>);</pre>
<h2>Description</h2>
<p><code>XmTextFieldPosToXY</code> accesses the <i>x</i> and <i>y</i> position, relative to the upper left corner of the TextField widget, of a given character position in the text buffer.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the TextField widget ID</p>
<dt><i>position</i></p>
<dd>Specifies the character position in the text for which the <i>x</i> and <i>y</i> position is accessed. This is an integer number of characters from the beginning of the buffer. The first character position is 0.</p>
<dt><i>x</i></p>
<dd>Specifies the pointer in which the <i>x</i> position is returned. The returned position is the distance from the left side of the widget to the left border of the character. This value is meaningful only if the function returns True.</p>
<dt><i>y</i></p>
<dd>Specifies the pointer in which the <i>y</i> position is returned. The returned position is the distance from the top of the widget to the character&#8217;s baseline. This value is meaningful only if the function returns True.</dl>
<p> For a complete definition of TextField and its associated resources, see <code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
<h2>Return</h2>
<p>This function returns True if the character position is displayed in the TextField widget; otherwise, it returns False, and no <i>x</i> or <i>y</i> value is returned.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3).</p>
