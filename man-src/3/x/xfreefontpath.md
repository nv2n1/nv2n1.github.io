---
title: "xfreefontpath(3)"
name: "xfreefontpath"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xfreefontpath/"
description: "XSetFontPath, XGetFontPath, XFreeFontPath – set, get, or free the font search path"
---

<p>XSetFontPath, XGetFontPath, XFreeFontPath &#8211; set, get, or free the font search path </p>
<h2>Syntax</h2>
<p>int XSetFontPath(Display *<i>display</i>, char **<i>directories</i>, int <i>ndirs</i>);</p>
<dl COMPACT>
<dd>char **XGetFontPath(Display *<i>display</i>, int *<i>npaths_return</i>);</p>
<dd>int XFreeFontPath(char **<i>list</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>directories</i></p>
<dd>Specifies the directory path used to look for a font. Setting the path to the empty list restores the default path defined for the X server.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>list</i></p>
<dd>Specifies the array of strings you want to free.</p>
<dt><i>ndirs</i></p>
<dd>Specifies the number of directories in the path.</p>
<dt><i>npaths_return</i></p>
<dd>Returns the number of strings in the font path array.</dl>
<h2>Description</h2>
<p>The <code>XSetFontPath</code> function defines the directory search path for font lookup. There is only one search path per X server, not one per client. The encoding and interpretation of the strings are implementation-dependent, but typically they specify directories or font servers to be searched in the order listed. An X server is permitted to cache font information internally; for example, it might cache an entire font from a file and not check on subsequent opens of that font to see if the underlying font file has changed. However, when the font path is changed, the X server is guaranteed to flush all cached information about fonts for which there currently are no explicit resource IDs allocated. The meaning of an error from this request is implementation-dependent. </p>
<p> <code>XSetFontPath</code> can generate a <code>BadValue</code> error. </p>
<p> The <code>XGetFontPath</code> function allocates and returns an array of strings containing the search path. The contents of these strings are implementation-dependent and are not intended to be interpreted by client applications. When it is no longer needed, the data in the font path should be freed by using <code>XFreeFontPath</code>. </p>
<p> The <code>XFreeFontPath</code> function frees the data allocated by <code>XGetFontPath</code>.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xlistfont/">XListFont</a>(3), <a href="/docs/linux/man/3-xloadfonts/">XLoadFonts</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
