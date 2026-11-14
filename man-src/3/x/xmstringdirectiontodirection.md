---
title: "xmstringdirectiontodirection(3)"
name: "xmstringdirectiontodirection"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringdirectiontodirection/"
description: "XmStringDirectionToDirection — A function that converts from XmStringDirection to XmDirection"
---

<p><code>XmStringDirectionToDirection</code> &#8212; A function that converts from XmStringDirection to XmDirection</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmDirection XmStringDirectionToDirection</code>(
<code>XmStringDirection direction</code>);</pre>
<h2>Description</h2>
<p><code>XmStringDirectionToDirection</code> converts the specified <code>XmStringDirection</code> direction value to its equivalent <code>XmDirection</code> value. This function provides backward compatibility with the <code>XmStringDirection</code> data type.</p>
<dl COMPACT>
<dt><i>direction</i></p>
<dd>Specifies the <code>XmStringDirection</code> value to be converted.</dl>
<h2>Return</h2>
<p>Returns the following <code>XmDirection</code> values:</p>
<dl COMPACT>
<dt><code>XmLEFT_TO_RIGHT</code></p>
<dd>If the <i>direction</i> argument is <code>XmSTRING_DIRECTION_L_TO_R</code>.</p>
<dt><code>XmRIGHT_TO_LEFT</code></p>
<dd>If the <i>direction</i> argument is <code>XmSTRING_DIRECTION_R_TO_L</code>.</p>
<dt><code>XmDEFAULT_DIRECTION</code></p>
<dd>If the <i>direction</i> argument was not either of the above.</dl>
<h2>Related Information</h2>
<p><code><a href="/docs/linux/man/3-xmstringdirection/">XmStringDirection</a></code>(3) and <code><a href="/docs/linux/man/3-xmdirection/">XmDirection</a></code>(3).</p>
