---
title: "tk_getanchorfromobj(3)"
name: "tk_getanchorfromobj"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_getanchorfromobj/"
description: "Tk_GetAnchorFromObj, Tk_GetAnchor, Tk_NameOfAnchor – translate between strings and anchor positions"
---

<p>Tk_GetAnchorFromObj, Tk_GetAnchor, Tk_NameOfAnchor &#8211; translate between strings and anchor positions </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
int
<code>Tk_GetAnchorFromObj(</code><i>interp, objPtr, anchorPtr</i><code>)</code>
int
<code>Tk_GetAnchor(</code><i>interp, string, anchorPtr</i><code>)</code>
const char *
<code>Tk_NameOfAnchor(</code><i>anchor</i><code>)</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter to use for error reporting, or NULL.</p>
<dd>Tcl_Obj <i>*objPtr</i> (in/out) String value contains name of anchor point: &#8220;n&#8221;, &#8220;ne&#8221;, &#8220;e&#8221;, &#8220;se&#8221;, &#8220;s&#8221;, &#8220;sw&#8221;, &#8220;w&#8221;, &#8220;nw&#8221;, or &#8220;center&#8221;; internal rep will be modified to cache corresponding Tk_Anchor.</p>
<dd>const char <i>*string</i> (in) Same as <i>objPtr</i> except description of anchor point is passed as a string.</p>
<dd>int <i>*anchorPtr</i> (out) Pointer to location in which to store anchor position corresponding to <i>objPtr</i> or <i>string</i>.</p>
<dd>Tk_Anchor <i>anchor</i> (in) Anchor position, e.g. <code>TCL_ANCHOR_CENTER</code>.
</dl>
<h2>Description</h2>
<p><code>Tk_GetAnchorFromObj</code> places in <i>*anchorPtr</i> an anchor position (enumerated type <code>Tk_Anchor</code>) corresponding to <i>objPtr</i>&#8216;s value. The result will be one of <code>TK_ANCHOR_N</code>, <code>TK_ANCHOR_NE</code>, <code>TK_ANCHOR_E</code>, <code>TK_ANCHOR_SE</code>, <code>TK_ANCHOR_S</code>, <code>TK_ANCHOR_SW</code>, <code>TK_ANCHOR_W</code>, <code>TK_ANCHOR_NW</code>, or <code>TK_ANCHOR_CENTER</code>. Anchor positions are typically used for indicating a point on an object that will be used to position the object, e.g. <code>TK_ANCHOR_N</code> means position the top center point of the object at a particular place. </p>
<p> Under normal circumstances the return value is <code>TCL_OK</code> and <i>interp</i> is unused. If <i>string</i> does not contain a valid anchor position or an abbreviation of one of these names, <code>TCL_ERROR</code> is returned, <i>*anchorPtr</i> is unmodified, and an error message is stored in <i>interp</i>&#8216;s result if <i>interp</i> is not NULL. <code>Tk_GetAnchorFromObj</code> caches information about the return value in <i>objPtr</i>, which speeds up future calls to <code>Tk_GetAnchorFromObj</code> with the same <i>objPtr</i>. </p>
<p> <code>Tk_GetAnchor</code> is identical to <code>Tk_GetAnchorFromObj</code> except that the description of the anchor is specified with a string instead of an object. This prevents <code>Tk_GetAnchor</code> from caching the return value, so <code>Tk_GetAnchor</code> is less efficient than <code>Tk_GetAnchorFromObj</code>. </p>
<p> <code>Tk_NameOfAnchor</code> is the logical inverse of <code>Tk_GetAnchor</code>. Given an anchor position such as <code>TK_ANCHOR_N</code> it returns a statically-allocated string corresponding to <i>anchor</i>. If <i>anchor</i> is not a legal anchor value, then &#8220;unknown anchor position&#8221; is returned.</p>
<h2>Keywords</h2>
<p>anchor position</p>
