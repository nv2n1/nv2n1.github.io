---
title: "xkbgetkeyactions(3)"
name: "xkbgetkeyactions"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbgetkeyactions/"
description: "XkbGetKeyActions – Update the actions (the key_acts array) for a subset of the keys in a keyboard description"
---

<p>XkbGetKeyActions &#8211; Update the actions (the key_acts array) for a subset of the keys in a keyboard description </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbGetKeyActions</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>unsigned int </code><i>first</i><code>,</code> <code>unsigned int </code><i>num</i><code>,</code> <code>XkbDescPtr </code><i>xkb</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></p>
<dd>
<dd>connection to X server</p>
<dt><i>&#8211; first</i></p>
<dd>keycode of first key of interest</p>
<dt><i>&#8211; num</i></p>
<dd>number of keys desired</p>
<dt><i>&#8211; xkb</i></p>
<dd>pointer to keyboard description where result is stored</dl>
<h2>Description</h2>
<p><i>XkbGetKeyActions </i> sends a request to the server to obtain the actions for <i>num </i> keys on the keyboard starting with key <i>first. </i> It waits for a reply and returns the actions in the <i>server-&gt;key_acts </i> field of <i>xkb. </i> If successful, <i>XkbGetKeyActions </i> returns Success. The <i>xkb </i> parameter must be a pointer to a valid Xkb keyboard description. </p>
<p> If the <i>server </i> map, in the <i>xkb </i> parameter, has not been allocated, <i>XkbGetKeyActions </i> allocates and initializes it before obtaining the actions. </p>
<p> If the server does not have a compatible version of Xkb, or the Xkb extension has not been properly initialized, <i>XkbGetKeyActions </i> returns BadAccess. If <i>num </i> is less than 1 or greater than XkbMaxKeyCount, <i>XkbGetKeyActions </i> returns BadValue. If any allocation errors occur, <i>XkbGetKeyActions </i> returns BadAlloc.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAccess</code></p>
<dd>The Xkb extension has not been properly initialized</p>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage</p>
<dt><code>BadValue</code></p>
<dd>An argument is out of range </p>
</dl>
