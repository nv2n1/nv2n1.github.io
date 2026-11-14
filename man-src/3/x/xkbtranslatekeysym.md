---
title: "xkbtranslatekeysym(3)"
name: "xkbtranslatekeysym"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbtranslatekeysym/"
description: "XkbTranslateKeySym – Find the string and symbol associated with a keysym for a given keyboard state"
---

<p>XkbTranslateKeySym &#8211; Find the string and symbol associated with a keysym for a given keyboard state </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>int XkbTranslateKeySym</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>KeySym *</code><i>sym_inout</i><code>,</code> <code>unsigned int </code><i>mods</i><code>,</code> <code>char *</code><i>buf</i><code>,</code> <code>int </code><i>nbytes</i><code>,</code> <code>int *</code><i>extra_rtrn</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></p>
<dd>
<dd>connection to X server</p>
<dt><i>&#8211; sym_inout</i></p>
<dd>symbol to be translated; result of translation</p>
<dt><i>&#8211; mods</i></p>
<dd>modifiers to apply to sym_inout</p>
<dt><i>&#8211; buf</i></p>
<dd>buffer into which returned string is written</p>
<dt><i>&#8211; nbytes</i></p>
<dd>size of buffer in bytes</p>
<dt><i>&#8211; extra_rtrn</i></p>
<dd>number of bytes overflow</dl>
<h2>Description</h2>
<p><i>XkbTranslateKeySym </i> applies the transformations specified in <i>mods </i> to the symbol specified by <i>sym_inout. </i> It returns in <i>buf </i> the string, if any, associated with the keysym for the current locale. If the transformations in <i>mods </i> changes the keysym, <i>sym_inout </i> is updated accordingly. If the string returned is larger than <i>nbytes,</i> a count of bytes that does not fit into the buffer is returned in <i>extra_rtrn. XkbTranslateKeySym </i> returns the number of bytes it placed into <i>buf.</i></p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>buf</p>
<dd>Returns the string, if any, associated with the keysym for the current locale. </p>
</dl>
