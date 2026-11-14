---
title: "tk_getjoinstyle(3)"
name: "tk_getjoinstyle"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_getjoinstyle/"
description: "Tk_GetJoinStyle, Tk_NameOfJoinStyle – translate between strings and join styles"
---

<p>Tk_GetJoinStyle, Tk_NameOfJoinStyle &#8211; translate between strings and join styles </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
int
<code>Tk_GetJoinStyle(</code><i>interp, string, joinPtr</i><code>)</code>
const char *
<code>Tk_NameOfJoinStyle(</code><i>join</i><code>)</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter to use for error reporting.</p>
<dd>const char <i>*string</i> (in) String containing name of join style: one of &#8220;bevel&#8221;, &#8220;miter&#8221;, or &#8220;round&#8221;.</p>
<dd>int <i>*joinPtr</i> (out) Pointer to location in which to store X join style corresponding to <i>string</i>.</p>
<dd>int <i>join</i> (in) Join style: one of <code>JoinBevel</code>, <code>JoinMiter</code>, <code>JoinRound</code>. </p>
</dl>
<h2>Description</h2>
<p><code>Tk_GetJoinStyle</code> places in <i>*joinPtr</i> the X join style corresponding to <i>string</i>, which will be one of <code>JoinBevel</code>, <code>JoinMiter</code>, or <code>JoinRound</code>. Join styles are typically used in X graphics contexts to indicate how adjacent line segments should be joined together. See the X documentation for information on what each style implies. </p>
<p> Under normal circumstances the return value is <code>TCL_OK</code> and <i>interp</i> is unused. If <i>string</i> does not contain a valid join style or an abbreviation of one of these names, then an error message is stored in <i>interp-&gt;result</i>, <code>TCL_ERROR</code> is returned, and <i>*joinPtr</i> is unmodified. </p>
<p> <code>Tk_NameOfJoinStyle</code> is the logical inverse of <code>Tk_GetJoinStyle</code>. Given a join style such as <code>JoinBevel</code> it returns a statically-allocated string corresponding to <i>join</i>. If <i>join</i> is not a legal join style, then &#8220;unknown join style&#8221; is returned. </p>
<h2>Keywords</h2>
<p>bevel, join style, miter, round</p>
