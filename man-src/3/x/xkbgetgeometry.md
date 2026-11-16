---
title: "xkbgetgeometry(3)"
name: "xkbgetgeometry"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbgetgeometry/"
description: "XkbGetGeometry – Loads a keyboard geometry if you already have the keyboard description"
---

<p>XkbGetGeometry &#8211; Loads a keyboard geometry if you already have the keyboard description </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbGetGeometry</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>XkbDescPtr </code><i>xkb</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dt></dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></dt>
<dd>
</dd><dd>connection to the X server</dd>
<dt><i>&#8211; xkb</i></dt>
<dd>keyboard description that contains the ID for the keyboard and into which the geometry should be loaded</dd></dl>
<h2>Description</h2>
<p>You can load a keyboard geometry as part of the keyboard description returned by <i>XkbGetKeyboard. </i> However, if a keyboard description has been previously loaded, you can instead obtain the geometry by calling the <i>XkbGetGeometry. </i> In this case, the geometry returned is the one associated with the keyboard whose device ID is contained in the keyboard description. </p>
<p> <i>XkbGetGeometry </i> can return BadValue, BadImplementation, BadName, BadAlloc, or BadLength errors or Success if it succeeds.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></dt>
<dd>Unable to allocate storage</dd>
<dt><code>BadImplementation</code></dt>
<dd>Invalid reply from server</dd>
<dt><code>BadLength</code></dt>
<dd>The length of a request is shorter or longer than that required to minimally contain the arguments</dd>
<dt><code>BadName</code></dt>
<dd>A font or color of the specified name does not exist</dd>
<dt><code>BadValue</code></dt>
<dd>An argument is out of range</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbgetkeyboard/">XkbGetKeyboard</a></code>(3)</p>
