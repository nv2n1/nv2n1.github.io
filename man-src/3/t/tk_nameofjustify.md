---
title: "tk_nameofjustify(3)"
name: "tk_nameofjustify"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_nameofjustify/"
description: "Tk_GetJustifyFromObj, Tk_GetJustify, Tk_NameOfJustify – translate between strings and justification styles"
---

<p>Tk_GetJustifyFromObj, Tk_GetJustify, Tk_NameOfJustify &#8211; translate between strings and justification styles </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
int
<code>Tk_GetJustifyFromObj(</code><i>interp, objPtr, justifyPtr</i><code>)</code>
int
<code>Tk_GetJustify(</code><i>interp, string, justifyPtr</i><code>)</code>
const char *
<code>Tk_NameOfJustify(</code><i>justify</i><code>)</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter to use for error reporting, or NULL.</p>
<dd>Tcl_Obj <i>*objPtr</i> (in/out) String value contains name of justification style, one of &#8220;left&#8221;, &#8220;right&#8221;, or &#8220;center&#8221;. The internal rep will be modified to cache corresponding justify value.</p>
<dd>const char <i>*string</i> (in) Same as <i>objPtr</i> except description of justification style is passed as a string.</p>
<dd>int <i>*justifyPtr</i> (out) Pointer to location in which to store justify value corresponding to <i>objPtr</i> or <i>string</i>.</p>
<dd>Tk_Justify <i>justify</i> (in) Justification style (one of the values listed below).
</dl>
<h2>Description</h2>
<p><code>Tk_GetJustifyFromObj</code> places in <i>*justifyPtr</i> the justify value corresponding to <i>objPtr</i>&#8216;s value. This value will be one of the following:</p>
<dl COMPACT>
<dt><code>TK_JUSTIFY_LEFT</code></p>
<dd>Means that the text on each line should start at the left edge of the line; as a result, the right edges of lines may be ragged.</p>
<dt><code>TK_JUSTIFY_RIGHT</code></p>
<dd>Means that the text on each line should end at the right edge of the line; as a result, the left edges of lines may be ragged.</p>
<dt><code>TK_JUSTIFY_CENTER</code></p>
<dd>Means that the text on each line should be centered; as a result, both the left and right edges of lines may be ragged.</dl>
<p> Under normal circumstances the return value is <code>TCL_OK</code> and <i>interp</i> is unused. If <i>objPtr</i> does not contain a valid justification style or an abbreviation of one of these names, <code>TCL_ERROR</code> is returned, <i>*justifyPtr</i> is unmodified, and an error message is stored in <i>interp</i>&#8216;s result if <i>interp</i> is not NULL. <code>Tk_GetJustifyFromObj</code> caches information about the return value in <i>objPtr</i>, which speeds up future calls to <code>Tk_GetJustifyFromObj</code> with the same <i>objPtr</i>. </p>
<p> <code>Tk_GetJustify</code> is identical to <code>Tk_GetJustifyFromObj</code> except that the description of the justification is specified with a string instead of an object. This prevents <code>Tk_GetJustify</code> from caching the return value, so <code>Tk_GetJustify</code> is less efficient than <code>Tk_GetJustifyFromObj</code>. </p>
<p> <code>Tk_NameOfJustify</code> is the logical inverse of <code>Tk_GetJustify</code>. Given a justify value it returns a statically-allocated string corresponding to <i>justify</i>. If <i>justify</i> is not a legal justify value, then &#8220;unknown justification style&#8221; is returned. </p>
<h2>Keywords</h2>
<p>center, fill, justification, string</p>
