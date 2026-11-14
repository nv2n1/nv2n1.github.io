---
title: "xkbgetkeysyms(3)"
name: "xkbgetkeysyms"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbgetkeysyms/"
description: "XkbGetKeySyms – Obtain the symbols for a subset of the keys in a keyboard description"
---

<p>XkbGetKeySyms &#8211; Obtain the symbols for a subset of the keys in a keyboard description </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbGetKeySyms</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>unsigned int </code><i>first</i><code>,</code> <code>unsigned int </code><i>num</i><code>,</code> <code>XkbDescPtr </code><i>xkb</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></p>
<dd>
<dd>connection to X server</p>
<dt><i>&#8211; first</i></p>
<dd>keycode of first key to get</p>
<dt><i>&#8211; num</i></p>
<dd>number of keycodes for which syms desired</p>
<dt><i>&#8211; xkb</i></p>
<dd>Xkb description to be updated</dl>
<h2>Description</h2>
<p><i>XkbGetKeySyms </i> sends a request to the server to obtain the set of keysyms bound to <i>num </i> keys starting with the key whose keycode is <i>first. </i> It waits for a reply and returns the keysyms in the <i>map.syms </i> field of <i>xkb. </i> If successful, <i>XkbGetKeySyms </i> returns Success. The <i>xkb </i> parameter must be a pointer to a valid Xkb keyboard description. </p>
<p> If the client <i>map </i> in the xkb parameter has not been allocated, <i>XkbGetKeySyms </i> allocates and initializes it before obtaining the symbols. </p>
<p> If a compatible version of Xkb is not available in the server or the Xkb extension has not been properly initialized, <i>XkbGetKeySyms </i> returns BadAccess. If <i>num </i> is less than 1 or greater than XkbMaxKeyCount, <i>XkbGetKeySyms </i> returns BadValue. If any allocation errors occur, <i>XkbGetKeySyms </i> returns BadAlloc.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>Success</p>
<dd>The <i>XkbGetKeySyms </i> function returns Success if it gets a reply to a request to the server to obtain the set of keysyms bound to <i>num </i> keys starting with the key whose keycode is <i>first. </i></dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAccess</code></p>
<dd>The Xkb extension has not been properly initialized</p>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage</p>
<dt><code>BadValue</code></p>
<dd>An argument is out of range </p>
</dl>
