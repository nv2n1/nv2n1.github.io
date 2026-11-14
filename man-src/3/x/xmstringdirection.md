---
title: "xmstringdirection(3)"
name: "xmstringdirection"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringdirection/"
description: "XmStringDirection — Data type for the direction of display in a string"
---

<p><code>XmStringDirection</code> &#8212; Data type for the direction of display in a string</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;</pre>
<h2>Description</h2>
<p><code>XmStringDirection</code> is the data type for specifying the direction in which the system displays characters of a string, or characters of a segment of a compound string. This is an enumeration with three possible values:</p>
<dl COMPACT>
<dt><code>XmSTRING_DIRECTION_L_TO_R</code></p>
<dd>Specifies left to right display</p>
<dt><code>XmSTRING_DIRECTION_R_TO_L</code></p>
<dd>Specifies right to left display</p>
<dt><code>XmSTRING_DIRECTION_DEFAULT</code></p>
<dd>Specifies that the display direction will be set by the widget in which the compound string is to be displayed.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstring/">XmString</a></code>(3).</p>
