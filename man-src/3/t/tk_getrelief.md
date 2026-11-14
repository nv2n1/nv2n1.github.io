---
title: "tk_getrelief(3)"
name: "tk_getrelief"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_getrelief/"
description: "Tk_GetReliefFromObj, Tk_GetRelief, Tk_NameOfRelief – translate between strings and relief values"
---

<p>Tk_GetReliefFromObj, Tk_GetRelief, Tk_NameOfRelief &#8211; translate between strings and relief values </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
int
<code>Tk_GetReliefFromObj(</code><i>interp, objPtr, reliefPtr</i><code>)</code>
int
<code>Tk_GetRelief(</code><i>interp, name, reliefPtr</i><code>)</code>
const char *
<code>Tk_NameOfRelief(</code><i>relief</i><code>)</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter to use for error reporting.</p>
<dd>Tcl_Obj <i>*objPtr</i> (in/out) String value contains name of relief, one of &#8220;flat&#8221;, &#8220;groove&#8221;, &#8220;raised&#8221;, &#8220;ridge&#8221;, &#8220;solid&#8221;, or &#8220;sunken&#8221;; the internal rep will be modified to cache corresponding relief value.</p>
<dd>char <i>*string</i> (in) Same as <i>objPtr</i> except description of relief is passed as a string.</p>
<dd>int <i>*reliefPtr</i> (out) Pointer to location in which to store relief value corresponding to <i>objPtr</i> or <i>name</i>.</p>
<dd>const char<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><i>*name</i><br />
 Name of the relief.</p>
<dd>int <i>relief</i> (in) Relief value (one of <code>TK_RELIEF_FLAT</code>, <code>TK_RELIEF_RAISED</code>, <code>TK_RELIEF_SUNKEN</code>, <code>TK_RELIEF_GROOVE</code>, <code>TK_RELIEF_SOLID</code>, or <code>TK_RELIEF_RIDGE</code>).
</dl>
<h2>Description</h2>
<p><code>Tk_GetReliefFromObj</code> places in <i>*reliefPtr</i> the relief value corresponding to the value of <i>objPtr</i>. This value will be one of <code>TK_RELIEF_FLAT</code>, <code>TK_RELIEF_RAISED</code>, <code>TK_RELIEF_SUNKEN</code>, <code>TK_RELIEF_GROOVE</code>, <code>TK_RELIEF_SOLID</code>, or <code>TK_RELIEF_RIDGE</code>. Under normal circumstances the return value is <code>TCL_OK</code> and <i>interp</i> is unused. If <i>objPtr</i> does not contain one of the valid relief names or an abbreviation of one of them, then <code>TCL_ERROR</code> is returned, <i>*reliefPtr</i> is unmodified, and an error message is stored in <i>interp</i>&#8216;s result if <i>interp</i> is not NULL. <code>Tk_GetReliefFromObj</code> caches information about the return value in <i>objPtr</i>, which speeds up future calls to <code>Tk_GetReliefFromObj</code> with the same <i>objPtr</i>. </p>
<p> <code>Tk_GetRelief</code> is identical to <code>Tk_GetReliefFromObj</code> except that the description of the relief is specified with a string instead of an object. This prevents <code>Tk_GetRelief</code> from caching the return value, so <code>Tk_GetRelief</code> is less efficient than <code>Tk_GetReliefFromObj</code>. </p>
<p> <code>Tk_NameOfRelief</code> is the logical inverse of <code>Tk_GetRelief</code>. Given a relief value it returns the corresponding string (<code>flat</code>, <code>raised</code>, <code>sunken</code>, <code>groove</code>, <code>solid</code>, or <code>ridge</code>). If <i>relief</i> is not a legal relief value, then &#8220;unknown relief&#8221; is returned.</p>
<h2>Keywords</h2>
<p>name, relief, string</p>
