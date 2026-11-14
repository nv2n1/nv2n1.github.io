---
title: "tk_nameofcapstyle(3)"
name: "tk_nameofcapstyle"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_nameofcapstyle/"
description: "Tk_GetCapStyle, Tk_NameOfCapStyle – translate between strings and cap styles"
---

<p>Tk_GetCapStyle, Tk_NameOfCapStyle &#8211; translate between strings and cap styles </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
int
<code>Tk_GetCapStyle(</code><i>interp, string, capPtr</i><code>)</code>
const char *
<code>Tk_NameOfCapStyle(</code><i>cap</i><code>)</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter to use for error reporting.</p>
<dd>const char <i>*string</i> (in) String containing name of cap style: one of &#8220;butt&#8221;, &#8220;projecting&#8221;, or &#8220;round&#8221;.</p>
<dd>int <i>*capPtr</i> (out) Pointer to location in which to store X cap style corresponding to <i>string</i>.</p>
<dd>int <i>cap</i> (in) Cap style: one of <code>CapButt</code>, <code>CapProjecting</code>, or <code>CapRound</code>. </p>
</dl>
<h2>Description</h2>
<p><code>Tk_GetCapStyle</code> places in <i>*capPtr</i> the X cap style corresponding to <i>string</i>. This will be one of the values <code>CapButt</code>, <code>CapProjecting</code>, or <code>CapRound</code>. Cap styles are typically used in X graphics contexts to indicate how the end-points of lines should be capped. See the X documentation for information on what each style implies. </p>
<p> Under normal circumstances the return value is <code>TCL_OK</code> and <i>interp</i> is unused. If <i>string</i> does not contain a valid cap style or an abbreviation of one of these names, then an error message is stored in <i>interp-&gt;result</i>, <code>TCL_ERROR</code> is returned, and <i>*capPtr</i> is unmodified. </p>
<p> <code>Tk_NameOfCapStyle</code> is the logical inverse of <code>Tk_GetCapStyle</code>. Given a cap style such as <code>CapButt</code> it returns a statically-allocated string corresponding to <i>cap</i>. If <i>cap</i> is not a legal cap style, then &#8220;unknown cap style&#8221; is returned. </p>
<h2>Keywords</h2>
<p>butt, cap style, projecting, round</p>
