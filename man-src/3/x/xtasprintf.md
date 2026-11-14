---
title: "xtasprintf(3)"
name: "xtasprintf"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtasprintf/"
description: "XtMalloc, XtCalloc, XtRealloc, XtFree, XtNew, XtNewString – memory management functions"
---

<p>XtMalloc, XtCalloc, XtRealloc, XtFree, XtNew, XtNewString &#8211; memory management functions </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>char *XtMalloc(Cardinal <i>size</i>);</p>
<dd>char *XtCalloc(Cardinal <i>num</i>, Cardinal <i>size</i>);</p>
<dd>char *XtRealloc(char *<i>ptr</i>, Cardinal <i>num</i>);</p>
<dd>void XtFree(char *<i>ptr</i>);</p>
<dt> <i>type</i> *XtNew(<i>type</i>);</p>
<dd>String XtNewString(String <i>string</i>);</p>
<dd>Cardinal XtAsprintf(char **<i>new_string</i>, const char *<i>format</i>, &#8230;);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>num</i></p>
<dd>Specifies the number of bytes or array elements.</p>
<dt><i>ptr</i></p>
<dd>Specifies a pointer to the old storage or to the block of storage that is to be freed.</p>
<dt><i>size</i></p>
<dd>Specifies the size of an array element (in bytes) or the number of bytes desired.</p>
<dt><i>string</i></p>
<dd>Specifies a previously declared string.</p>
<dt><i>type</i></p>
<dd>Specifies a previously declared data type.</p>
<dt><i>new_string</i></p>
<dd>Specifies a pointer to write a newly allocated string to.</p>
<dt><i>format</i></p>
<dd>Specifies a formatting string as defined by <a href="//www.systutorials.com/docs/linux/man/3c-sprintf/">sprintf</a>(3c)</dl>
<h2>Description</h2>
<p>The <code>XtMalloc</code> functions returns a pointer to a block of storage of at least the specified size bytes. If there is insufficient memory to allocate the new block, <code>XtMalloc</code> calls <code>XtErrorMsg</code>. </p>
<p> The <code>XtCalloc</code> function allocates space for the specified number of array elements of the specified size and initializes the space to zero. If there is insufficient memory to allocate the new block, <code>XtCalloc</code> calls <code>XtErrorMsg</code>. </p>
<p> The <code>XtRealloc</code> function changes the size of a block of storage (possibly moving it). Then, it copies the old contents (or as much as will fit) into the new block and frees the old block. If there is insufficient memory to allocate the new block, <code>XtRealloc</code> calls <code>XtErrorMsg</code>. If ptr is NULL, <code>XtRealloc</code> allocates the new storage without copying the old contents; that is, it simply calls <code>XtMalloc</code>. </p>
<p> The <code>XtFree</code> function returns storage and allows it to be reused. If ptr is NULL, <code>XtFree</code> returns immediately. </p>
<p> <code>XtNew</code> returns a pointer to the allocated storage. If there is insufficient memory to allocate the new block, <code>XtNew</code> calls <code>XtErrorMsg</code>. <code>XtNew</code> is a convenience macro that calls <code>XtMalloc</code> with the following arguments specified: </p>
<dl COMPACT>
<dd>((type *) XtMalloc((unsigned) sizeof(type))</dl>
<p> <code>XtNewString</code> returns a pointer to a new string which is a duplicate of <i>string</i>. If there is insufficient memory to allocate the new block, or the argument is NULL <code>XtNewString</code> returns NULL. The memory can be freed with <code>XtFree</code>. </p>
<p> The <code>XtAsprintf</code> function allocates space for a string large enough to hold the string specified by the <a href="//www.systutorials.com/docs/linux/man/3c-sprintf/">sprintf</a>(3c) format pattern when used with the remaining arguments, and fills it with the formatted results. The address of the allocated string is placed into the pointer passed as ret. The length of the string (not including the terminating null byte) is returned. If there is insufficient memory to allocate the new block, <code>XtAsprintf</code> calls <code>XtErrorMsg</code>.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
