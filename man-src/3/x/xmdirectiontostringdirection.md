---
title: "xmdirectiontostringdirection(3)"
name: "xmdirectiontostringdirection"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmdirectiontostringdirection/"
description: "XmDirectionToStringDirection — A function that converts an XmDirection value to an XmStringDirection value"
---

<p><code>XmDirectionToStringDirection</code> &#8212; A function that converts an XmDirection value to an XmStringDirection value</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
XmStringDirection XmDirectionToStringDirection (<i>dir</i>)
 XmDirection <i>dir</i>;
(<code>void</code>)</pre>
<h2>Description</h2>
<p><code>XmDirectionToStringDirection</code> converts the specified <code>XmDirection</code> direction value to its equivalent <code>XmStringDirection</code> value. Basically, if the <code>XmDirection</code> value has a horizontal direction specification, that horizontal element is used; otherwise, the <code>XmStringDirection</code> value is interpreted as <code>XmSTRING_DIRECTION_L_TO_R</code>. This function provides backward compatibility with the <code>XmStringDirection</code> data type. </p>
<p> Note that the Motif toolkit also contains an <code>XmStringDirectionToDirection</code> routine to convert an <code>XmStringDirection</code> value to its <code>XmDirection</code> equivalent.</p>
<dl COMPACT>
<dt><i>dir</i></dt>
<dd>Specifies the <code>XmDirection</code> value to be converted.</dd></dl>
<h2>Return</h2>
<p>Returns the following <code>XmStringDirection</code> values:</p>
<dl COMPACT>
<dt><code>XmSTRING_DIRECTION_R_TO_L</code></dt>
<dd>If the <i>dir</i> argument has a right to left horizontal direction value in it, for example <code>XmRIGHT_TO_LEFT_TOP_TO_BOTTOM</code>.</dd>
<dt><code>XmSTRING_DIRECTION_L_TO_R</code></dt>
<dd>If the <i>dir</i> argument has a left to right horizontal direction in it, for example <code>XmLEFT_TO_RIGHT_TOP_TO_BOTTOM</code>, or if the horizontal direction value in the <i>dir</i> argument is ambiguous, such as in the <code>XmTOP_TO_BOTTOM</code> value.</dd>
<dt><code>XmSTRING_DIRECTION_DEFAULT</code></dt>
<dd>If there was no horizontal direction specified.</dd></dl>
<h2>Related Information</h2>
<p><code><a href="/docs/linux/man/3-xmdirection/">XmDirection</a></code>(3), <code><a href="/docs/linux/man/3-xmdirectionmatch/">XmDirectionMatch</a></code>(3), <code><a href="/docs/linux/man/3-xmdirectionmatchpartial/">XmDirectionMatchPartial</a></code>(3), <code><a href="/docs/linux/man/3-xmdirectiontostringdirection/">XmDirectionToStringDirection</a></code>(3), <code><a href="/docs/linux/man/3-xmstring/">XmString</a></code>(3), <code><a href="/docs/linux/man/3-xmstringdirection/">XmStringDirection</a></code>(3), and <code><a href="/docs/linux/man/3-xmstringdirectiontodirection/">XmStringDirectionToDirection</a></code>(3),</p>
